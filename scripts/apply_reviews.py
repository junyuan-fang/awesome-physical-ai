"""Merge a filled review file into the dataset and render the run's digest.

    python scripts/apply_reviews.py pipeline/reviews/2026-10-22.yaml [--no-readme]

* Rejects incomplete reviews (lists every missing field) so the reviewer can fix them.
* Enforces the run cap on NEW inclusions (core route first, then total score);
  overflow becomes `defer` with reason "over cap".
* Adds new papers / updates re-reviewed ones (changes recorded in `history`).
* Logs exclude / defer decisions in data/triage_log.yaml so they are not re-fetched.
* Registers `new_resources` in datasets / benchmarks / simulators / tools.
* Appends the run to data/runs.yaml, writes digests/daily/<date>.md, re-renders README.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

import digest  # noqa: E402
from curation import (  # noqa: E402
    ASSET_STATUS,
    CODE_STATUS,
    USE_ROLES,
    CONTRIBUTIONS,
    DATA,
    DIGESTS,
    PIPELINE,
    ROOT,
    ROUTES,
    RUNS_YAML,
    TRIAGE,
    TRIAGE_LOG,
    WEIGHTS,
    compute_total,
    dump_yaml,
    finalize_review,
    load_papers,
    load_yaml,
    save_papers,
    today,
)

RESOURCE_FILE = {
    "dataset": ("datasets.yaml", "datasets"),
    "benchmark": ("benchmarks.yaml", "benchmarks"),
    "simulator": ("simulators.yaml", "simulators"),
    "tool": ("tools.yaml", "tools"),
}
INCLUDE_REQUIRED = ("category", "route", "contribution", "one_liner", "summary", "evidence_read")


def resource_ids() -> set[str]:
    ids: set[str] = set()
    for fname, key in RESOURCE_FILE.values():
        ids |= {r.get("id") for r in load_yaml(DATA / fname, key)}
    return ids


def check_item(it: dict[str, Any], known_cats: set[str], known_res: set[str] | None = None) -> list[str]:
    errs = []
    if it.get("triage") not in TRIAGE:
        return [f"triage must be one of {TRIAGE}"]
    if it["triage"] != "include":
        if not it.get("reason"):
            errs.append("reason required for exclude/defer")
        return errs
    for k in INCLUDE_REQUIRED:
        if not it.get(k):
            errs.append(f"missing {k}")
    if it.get("category") and it["category"] not in known_cats:
        errs.append(f"unknown category {it['category']!r}")
    if it.get("route") and it["route"] not in ROUTES:
        errs.append(f"route must be one of {ROUTES}")
    if it.get("contribution") and it["contribution"] not in CONTRIBUTIONS:
        errs.append(f"contribution must be one of {CONTRIBUTIONS}")
    scores = it.get("scores") or {}
    filled = [k for k in WEIGHTS if scores.get(k) not in (None, "")]
    if filled and len(filled) != len(WEIGHTS):
        errs.append("scores must be all filled or all null (unrated)")
    if filled:
        if not all(isinstance(scores[k], int) and 1 <= scores[k] <= 5 for k in WEIGHTS):
            errs.append("scores must be integers 1..5")
        if not all((it.get("rationale") or {}).get(k) for k in WEIGHTS):
            errs.append("rationale needed for every scored dimension")
        if set(it.get("evidence_read") or []) <= {"abstract"}:
            errs.append("scoring requires reading beyond the abstract")
    elif not it.get("pending_checks"):
        errs.append("unrated items must list pending_checks")
    if known_res is not None:
        new_ids = {r.get("id") for r in it.get("new_resources") or []}
        for r in it.get("new_resources") or []:
            if r.get("kind") not in RESOURCE_FILE or not all(r.get(k) for k in ("id", "name", "desc")):
                errs.append(f"new_resources entry needs kind∈{list(RESOURCE_FILE)}, id, name, desc: {r}")
        for u in it.get("uses") or []:
            if u.get("resource") not in known_res | new_ids:
                errs.append(f"uses → unknown resource {u.get('resource')!r} (add it to new_resources)")
            if u.get("role") not in USE_ROLES:
                errs.append(f"uses role must be one of {USE_ROLES}")
    o = it.get("open") or {}
    if o.get("code", "unknown") not in CODE_STATUS:
        errs.append(f"open.code must be one of {CODE_STATUS}")
    for k in ("weights", "data"):
        if o.get(k, "unknown") not in ASSET_STATUS:
            errs.append(f"open.{k} must be one of {ASSET_STATUS}")
    return errs


def short_authors(authors: list[str] | str) -> str:
    if isinstance(authors, str):
        return authors
    if not authors:
        return ""
    return authors[0] if len(authors) == 1 else f"{authors[0]} et al."


def build_review(it: dict[str, Any], reviewer: str) -> dict[str, Any]:
    scores = it.get("scores") or {}
    review: dict[str, Any] = {}
    if all(scores.get(k) not in (None, "") for k in WEIGHTS):
        review["scores"] = {k: int(scores[k]) for k in WEIGHTS}
        review["rationale"] = {k: it["rationale"][k] for k in WEIGHTS}
    review["evidence_read"] = list(it.get("evidence_read") or [])
    if it.get("pending_checks"):
        review["pending_checks"] = list(it["pending_checks"])
    review["reviewed"] = today()
    review["reviewer"] = reviewer
    return review


def build_open(it: dict[str, Any], cand: dict[str, Any], prev: dict[str, Any] | None) -> dict[str, Any]:
    o = dict(it.get("open") or {})
    prev = prev or {}
    out = {
        "code": o.get("code") or "unknown",
        "repo": o.get("repo") or "",
        "weights": o.get("weights") or "unknown",
        "data": o.get("data") or "unknown",
        "license": o.get("license") or "unknown",
    }
    if o.get("note"):
        out["note"] = o["note"]
    stats = (cand.get("probe") or {}).get("stats")
    if stats:
        out["stats"] = stats
    out["first_check"] = prev.get("first_check") or today()
    out["last_check"] = today()
    return out


def register_resources(items: list[dict[str, Any]]) -> list[str]:
    added = []
    existing: dict[str, set[str]] = {}
    for kind, (fname, key) in RESOURCE_FILE.items():
        existing[kind] = {r.get("id") for r in load_yaml(DATA / fname, key)}
    all_ids = set().union(*existing.values())
    for it in items:
        for res in it.get("new_resources") or []:
            kind = res.get("kind")
            if kind not in RESOURCE_FILE or not res.get("id") or res["id"] in all_ids:
                continue
            fname, key = RESOURCE_FILE[kind]
            path = DATA / fname
            doc = load_yaml(path)
            entry = {k: v for k, v in res.items() if k != "kind" and v not in (None, "", [])}
            entry.setdefault("links", {})
            entry["added"] = today()
            entry["last_check"] = today()
            doc.setdefault(key, []).append(entry)
            header = "".join(l + "\n" for l in path.read_text(encoding="utf-8").splitlines() if l.startswith("#"))
            dump_yaml(path, doc)
            if header:
                path.write_text(header + "\n" + path.read_text(encoding="utf-8"), encoding="utf-8")
            all_ids.add(res["id"])
            added.append(f"{kind}:{res['id']}")
    return added


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("review_file")
    ap.add_argument("--no-readme", action="store_true")
    ap.add_argument("--check", action="store_true", help="validate the review file only; change nothing")
    ap.add_argument("--reviewer", default="claude (agent review, human-auditable)")
    args = ap.parse_args()

    review_path = Path(args.review_file)
    doc = load_yaml(review_path)
    run = dict(doc.get("run") or {})
    items: list[dict[str, Any]] = doc.get("items") or []
    stem = review_path.stem
    cand_path = PIPELINE / "candidates" / f"{stem}.json"
    cands = {}
    if cand_path.exists():
        cands = {c["arxiv_id"]: c for c in json.loads(cand_path.read_text(encoding="utf-8"))["candidates"]}

    known_cats = set()
    for c in load_yaml(DATA / "categories.yaml", "categories"):
        known_cats.add(c["id"])
        known_cats |= {s["id"] for s in c.get("subcategories", []) or []}

    known_res = resource_ids()
    problems = {it.get("arxiv_id"): check_item(it, known_cats, known_res) for it in items}
    problems = {k: v for k, v in problems.items() if v}
    if problems:
        for aid, errs in problems.items():
            print(f"❌ {aid}: {'; '.join(errs)}", file=sys.stderr)
        print(f"\n{len(problems)} incomplete review item(s) — fix {review_path} and re-run.", file=sys.stderr)
        return 1
    if args.check:
        n_inc = sum(1 for it in items if it["triage"] == "include")
        print(f"✅ {review_path.name}: {len(items)} items valid ({n_inc} include, {len(items) - n_inc} exclude/defer)")
        return 0

    papers = load_papers()
    by_id = {str(p.get("arxiv_id")): p for p in papers}
    kind = run.get("kind", "daily")

    new_incl = [it for it in items if it["triage"] == "include" and str(it["arxiv_id"]) not in by_id]
    if kind in ("daily", "backfill") and run.get("cap") is not None:
        cap = int(run["cap"])

        def rank(it: dict[str, Any]) -> tuple:
            s = it.get("scores") or {}
            total = compute_total(s) if all(isinstance(s.get(k), int) for k in WEIGHTS) else 0
            return (0 if it.get("route") == "core" else 1, -total)

        ordered = sorted(new_incl, key=rank)
        for it in ordered[cap:]:
            it["triage"] = "defer"
            it["reason"] = f"over cap（本轮上限 {cap}，按核心优先+总分排序未入选）"
        new_incl = ordered[:cap]

    digest_rel = f"digests/daily/{run.get('scan_date', today())}.md" if kind != "migration" else f"digests/migration-{run.get('scan_date', today())}.md"
    included: list[dict[str, Any]] = []
    removed = 0
    skipped: list[dict[str, Any]] = []
    for it in items:
        aid = str(it["arxiv_id"])
        cand = cands.get(aid, {})
        prev = by_id.get(aid)
        if it["triage"] != "include":
            entry = {
                "arxiv_id": aid,
                "title": it.get("title") or cand.get("title", ""),
                "decision": it["triage"],
                "reason": it.get("reason"),
                "date": today(),
                "run": stem,
            }
            skipped.append(entry)
            if prev is not None:  # re-review decided it is out of scope
                papers.remove(prev)
                removed += 1
            continue

        if prev is None and it not in new_incl:
            continue
        reviewer = args.reviewer
        if prev is None:
            p: dict[str, Any] = {
                "arxiv_id": aid,
                "title": cand.get("title") or it.get("title"),
                "authors": short_authors(cand.get("authors") or []),
                "date": cand.get("published") or it.get("date_v1"),
                "category": it["category"],
                "links": {"arxiv": f"https://arxiv.org/abs/{aid}"},
                "added": today(),
                "source": "arxiv" if not (cand.get("hf") or {}).get("upvotes") else "arxiv+hf-daily",
                "digest": digest_rel,
            }
            if cand.get("updated") and cand.get("updated") != p["date"]:
                p["updated"] = cand["updated"]
            if cand.get("published") and run.get("last_covered_end") and cand["published"] < run["last_covered_end"]:
                p["late_found"] = True
            papers.append(p)
            by_id[aid] = p
        else:
            p = prev
            p.setdefault("history", [])
            if it.get("date_v1") and len(str(it["date_v1"])) == 10 and str(p.get("date")) != str(it["date_v1"]):
                p["history"].append({"date": today(), "change": f"date {p.get('date')} → {it['date_v1']} (arXiv v1)"})
                p["date"] = str(it["date_v1"])
            if p.get("category") != it["category"]:
                p["history"].append({"date": today(), "change": f"category {p.get('category')} → {it['category']}"})
            p.setdefault("digest", digest_rel)

        old_priority = (p.get("review") or {}).get("priority", "unrated")
        p["category"] = it["category"]
        p["route"] = it["route"]
        p["contribution"] = it["contribution"]
        if it.get("tags"):
            p["tags"] = list(it["tags"])[:5]
        if it.get("affiliations"):
            p["affiliations"] = list(it["affiliations"])
        if it.get("venue"):
            p["venue"] = it["venue"]
        p["abstract_short"] = it["one_liner"].strip()
        p["summary"] = it["summary"].strip()
        p["review"] = build_review(it, reviewer)
        p["open"] = build_open(it, cand, (prev or {}).get("open"))
        if p["open"].get("repo") and p["open"]["code"] in ("partial", "substantive"):
            p["links"]["code"] = p["open"]["repo"]
        project = it.get("project") or cand.get("project")
        if project:
            p["links"]["project"] = project
        if it.get("uses"):
            p["uses"] = [{"resource": u["resource"], "role": u["role"]} for u in it["uses"]]
        finalize_review(p)
        if prev is not None and old_priority != p["review"]["priority"]:
            p["history"].append({"date": today(), "change": f"priority {old_priority} → {p['review']['priority']} (re-review)"})
        if prev is not None and not p.get("history"):
            p.pop("history", None)
        included.append(p)

    # Keep key order stable and readable.
    order = [
        "arxiv_id", "title", "authors", "affiliations", "date", "updated", "venue", "category", "route",
        "contribution", "tags", "abstract_short", "summary", "links", "highlight", "classic", "review",
        "open", "uses", "added", "source", "digest", "late_found", "history",
    ]
    papers = [{k: p[k] for k in order if k in p} | {k: v for k, v in p.items() if k not in order} for p in papers]
    save_papers(papers)

    log = load_yaml(TRIAGE_LOG)
    log.setdefault("entries", [])
    known = {str(e["arxiv_id"]) for e in log["entries"]}
    log["entries"] += [s for s in skipped if s["arxiv_id"] not in known]
    dump_yaml(TRIAGE_LOG, log)

    res_added = register_resources([it for it in items if it["triage"] == "include"])

    runs = load_yaml(RUNS_YAML)
    runs.setdefault("runs", [])
    run_rec = {k: v for k, v in run.items() if k != "note"}
    run_rec.update(
        included=len([it for it in items if it["triage"] == "include"]),
        excluded=len([s for s in skipped if s["decision"] == "exclude"]),
        deferred=len([s for s in skipped if s["decision"] == "defer"]),
        removed=removed,
        new_resources=res_added,
        digest=digest_rel,
        applied=today(),
    )
    runs["runs"] = [r for r in runs["runs"] if not (r.get("scan_date") == run_rec.get("scan_date") and r.get("kind") == kind)]
    runs["runs"].append(run_rec)
    dump_yaml(RUNS_YAML, runs)

    out = ROOT / digest_rel
    out.parent.mkdir(parents=True, exist_ok=True)
    if kind == "migration":
        text = digest.render_migration(run, included, skipped, out)
    else:
        text = digest.render_daily(run, included, skipped, out)
    out.write_text(text, encoding="utf-8")

    print(
        f"✅ applied {review_path.name}: {len(included)} included/updated, {len(skipped)} excluded/deferred, "
        f"{removed} removed, resources +{len(res_added)} → {digest_rel}"
    )
    if not args.no_readme:
        import generate_readme

        generate_readme.main()
    return 0


if __name__ == "__main__":
    sys.exit(main())
