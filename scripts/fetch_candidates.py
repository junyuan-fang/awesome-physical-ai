"""Discovery + layer-0 prefilter for one scan run.

    python scripts/fetch_candidates.py [--date YYYY-MM-DD] [--start YYYY-MM-DD] [--kind daily|backfill]

1. Work out the scan window: from (last covered end − overlap_days) to the scan date.
   The per-run cap is d = max(1, scan_date − last_end); cap = min(cap_per_day·d, cap_max).
2. Pull candidates straight from primary channels: arXiv API (all of cs.RO, plus
   cs.CV/cs.AI/cs.LG papers that hit a strong keyword) and HuggingFace daily papers.
3. Drop anything already in data/papers.yaml or data/triage_log.yaml.
4. Rank the rest with a cheap relevance score and keep a pool of cap·triage_pool_factor.
5. For the pool: resolve code/project links, probe the repo, and condense the arXiv
   HTML into pipeline/cache/papers/<id>.md so the reviewer reads real method/experiment text.
6. Write pipeline/candidates/<date>.json and a review stub pipeline/reviews/<date>.yaml.

The review stub is then filled by a reviewer (human or agent) following
docs/METHODOLOGY.md, and merged with scripts/apply_reviews.py.
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

import sources  # noqa: E402
from curation import (  # noqa: E402
    PIPELINE,
    TRIAGE_LOG,
    dump_yaml,
    last_run,
    load_config,
    load_papers,
    load_yaml,
    parse_date,
    run_cap,
    today,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger("fetch")

CACHE = PIPELINE / "cache" / "papers"


def window(args: argparse.Namespace, cfg: dict[str, Any]) -> tuple[str, str, str | None]:
    """Return (start, end, last_covered_end)."""
    end = args.date
    prev = last_run()
    if prev:
        last_end = prev["window_end"]
    else:
        # First run of the new pipeline: continue from the newest tracked paper.
        dates = [str(p.get("date", "")) for p in load_papers() if len(str(p.get("date", ""))) == 10]
        last_end = max(dates) if dates else None
    if args.start:
        start = args.start
    elif last_end:
        start = (parse_date(last_end) - timedelta(days=int(cfg.get("overlap_days", 2)))).isoformat()
    else:
        start = (parse_date(end) - timedelta(days=3)).isoformat()
    return start, end, last_end


def keyword_score(rec: dict[str, Any], cfg: dict[str, Any]) -> tuple[int, int]:
    title = " " + rec["title"].lower() + " "
    text = title + rec["abstract"].lower()
    strong = sum((3 if k in title else 2) for k in cfg["strong_keywords"] if k in text)
    weak = sum(1 for k in cfg["weak_keywords"] if k in text)
    return strong, weak


def relevance(rec: dict[str, Any], hf: dict[str, Any], cfg: dict[str, Any]) -> float:
    strong, weak = keyword_score(rec, cfg)
    score = strong + 0.5 * weak
    if rec["categories"] and rec["categories"][0] == "cs.RO":
        score += 2
    score += min(hf.get("upvotes", 0), 50) / 5
    if hf.get("github") or "github.com" in (rec["comment"] + rec["abstract"]).lower():
        score += 2
    if sources.ARXIV_ID_RE and any(v in rec["comment"] for v in ("CoRL", "RSS", "ICRA", "NeurIPS", "ICLR", "CVPR", "IROS")):
        score += 1
    return round(score, 2)


def discover(start: str, end: str, cfg: dict[str, Any]) -> list[dict[str, Any]]:
    rng = f"submittedDate:[{start.replace('-', '')}0000 TO {end.replace('-', '')}2359]"
    recs = sources.arxiv_search(f"cat:cs.RO AND {rng}", max_results=5000)
    others = " OR ".join(f"cat:{c}" for c in cfg["arxiv_categories"] if c != "cs.RO")
    kw = " OR ".join(
        f'abs:"{k.strip()}"' for k in ("vision-language-action", "embodied", "humanoid", "robot", "robotic manipulation", "world model")
    )
    recs += sources.arxiv_search(f"({others}) AND ({kw}) AND {rng}", max_results=3000)
    uniq: dict[str, dict[str, Any]] = {}
    for r in recs:
        uniq.setdefault(r["arxiv_id"], r)
    return list(uniq.values())


def hf_signals(start: str, end: str) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    d = parse_date(start)
    while d <= parse_date(end):
        for item in sources.hf_daily(d.isoformat()):
            if item["arxiv_id"]:
                out[item["arxiv_id"]] = item
        d += timedelta(days=1)
    return out


def enrich(cand: dict[str, Any]) -> dict[str, Any]:
    """Resolve links, probe the repo and cache condensed full text."""
    aid = cand["arxiv_id"]
    hf = cand.get("hf") or {}
    if not hf.get("github") and not hf.get("project"):
        hf = {**hf, **sources.hf_paper(aid)}
    text = sources.fetch_paper_text(aid)
    repo = sources.normalize_github(hf.get("github", ""))
    if not repo:
        for blob in (cand["comment"], cand["abstract"]):
            for m in sources.GITHUB_RE.finditer(blob):
                repo = repo or sources.normalize_github(m.group(0))
    if not repo and text and text["github"]:
        repo = text["github"][0]
    project = hf.get("project", "")
    if not repo and project:
        repo = sources.find_github_on_page(project)
    probe = sources.probe_repo(repo) if repo else {"code": "no-repo"}
    cand.update(hf=hf, project=project, probe=probe)
    cand["affiliations"] = text["affiliations"] if text else []
    cand["fulltext"] = bool(text)
    write_cache(cand, text)
    return cand


def write_cache(cand: dict[str, Any], text: dict[str, Any] | None) -> None:
    CACHE.mkdir(parents=True, exist_ok=True)
    probe = cand.get("probe", {})
    lines = [
        f"# {cand['title']}",
        "",
        f"- arXiv: https://arxiv.org/abs/{cand['arxiv_id']} (first version {cand['published']}, latest {cand['version']} {cand['updated']})",
        f"- categories: {', '.join(cand['categories'])}",
        f"- authors: {', '.join(cand['authors'][:25])}{' …' if len(cand['authors']) > 25 else ''}",
        f"- affiliations (from arXiv HTML): {'; '.join(cand.get('affiliations') or []) or 'not found in HTML — check the PDF'}",
        f"- comment: {cand['comment'] or '—'}",
        f"- journal_ref: {cand['journal_ref'] or '—'}",
        f"- project page: {cand.get('project') or '—'}",
        f"- HF upvotes: {cand.get('hf', {}).get('upvotes', 0)}",
        f"- repo probe: {json.dumps(probe, ensure_ascii=False)}",
        "",
        "## Abstract",
        "",
        cand["abstract"],
        "",
    ]
    if text:
        lines += ["## Condensed full text (arXiv HTML)", ""]
        for heading, body in text["sections"]:
            lines += [f"### {heading}", "", body, ""]
        if text["captions"]:
            lines += ["## Figure / table captions", ""] + [f"- {c}" for c in text["captions"]] + [""]
        if text["huggingface"]:
            lines += ["## HuggingFace links in paper", ""] + [f"- {u}" for u in text["huggingface"]] + [""]
    else:
        lines += ["*(No arXiv HTML available — read the PDF before scoring evidence.)*", ""]
    (CACHE / f"{cand['arxiv_id']}.md").write_text("\n".join(lines), encoding="utf-8")


def review_stub(cand: dict[str, Any]) -> dict[str, Any]:
    probe = cand.get("probe", {})
    return {
        "arxiv_id": cand["arxiv_id"],
        "title": cand["title"],
        "prefilter_score": cand["relevance"],
        "triage": None,  # include | defer | exclude
        "reason": None,
        "category": None,
        "route": None,
        "contribution": None,
        "tags": [],
        "affiliations": cand.get("affiliations") or [],
        "one_liner": None,
        "summary": None,
        "venue": "",
        "scores": {"C": None, "E": None, "O": None, "T": None},
        "rationale": {"C": None, "E": None, "O": None, "T": None},
        "evidence_read": [],
        "pending_checks": [],
        "open": {
            "code": probe.get("code", "unknown"),
            "repo": probe.get("repo", ""),
            "weights": "unknown",
            "data": "unknown",
            "license": probe.get("license", "unknown"),
            "note": "",
        },
        "uses": [],
        "new_resources": [],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=today(), help="scan date (window end)")
    ap.add_argument("--start", help="override window start")
    ap.add_argument("--kind", default="daily", choices=["daily", "backfill"])
    ap.add_argument("--pool", type=int, help="override triage pool size")
    args = ap.parse_args()
    cfg = load_config()

    start, end, last_end = window(args, cfg)
    d, cap = run_cap(end, last_end, cfg)
    pool_size = args.pool or min(cap * int(cfg["triage_pool_factor"]), int(cfg["triage_pool_max"]))
    log.info("window %s → %s · last covered end %s · d=%d cap=%d pool=%d", start, end, last_end, d, cap, pool_size)

    recs = discover(start, end, cfg)
    hf = hf_signals(start, end)
    # HF daily papers can surface items outside the arXiv query (e.g. cs.CL embodied work).
    missing = [aid for aid in hf if aid not in {r["arxiv_id"] for r in recs}]
    extra = sources.arxiv_by_ids(missing) if missing else {}
    recs += [r for r in extra.values() if start <= r["published"] <= end]

    tracked = {str(p.get("arxiv_id")) for p in load_papers()}
    triaged = {str(t["arxiv_id"]) for t in load_yaml(TRIAGE_LOG, "entries")}
    fresh = [r for r in recs if r["arxiv_id"] not in tracked and r["arxiv_id"] not in triaged]
    in_scope = []
    for r in fresh:
        strong, _ = keyword_score(r, cfg)
        if "cs.RO" in r["categories"] or strong > 0:
            r["hf"] = hf.get(r["arxiv_id"], {})
            r["relevance"] = relevance(r, r["hf"], cfg)
            in_scope.append(r)
    in_scope.sort(key=lambda r: -r["relevance"])
    pool = in_scope[:pool_size]
    log.info(
        "fetched %d · already tracked/triaged %d · out of scope %d · pool %d",
        len(recs), len(recs) - len(fresh), len(fresh) - len(in_scope), len(pool),
    )

    with ThreadPoolExecutor(max_workers=6) as ex:
        pool = list(ex.map(enrich, pool))

    run = {
        "scan_date": end,
        "kind": args.kind,
        "window_start": start,
        "window_end": end,
        "last_covered_end": last_end,
        "d": d,
        "cap": cap,
        "stats": {
            "fetched": len(recs),
            "already_tracked_or_triaged": len(recs) - len(fresh),
            "out_of_scope": len(fresh) - len(in_scope),
            "below_pool_cut": max(0, len(in_scope) - len(pool)),
            "pool": len(pool),
        },
        "sources": ["arXiv API (cs.RO all; cs.CV/cs.AI/cs.LG keyword query)", "HuggingFace daily papers"],
    }
    out = PIPELINE / "candidates" / f"{end}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"run": run, "candidates": pool}, ensure_ascii=False, indent=1), encoding="utf-8")
    stub = PIPELINE / "reviews" / f"{end}.yaml"
    if stub.exists():
        log.warning("%s exists — not overwriting a review in progress", stub)
    else:
        dump_yaml(stub, {"run": run, "items": [review_stub(c) for c in pool]})
    log.info("wrote %s and %s", out.relative_to(PIPELINE.parent), stub.relative_to(PIPELINE.parent))
    return 0


if __name__ == "__main__":
    sys.exit(main())
