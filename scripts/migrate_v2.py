"""One-off migration of data/*.yaml to the v2 curation schema.

    python scripts/migrate_v2.py              # schema migration (idempotent)
    python scripts/migrate_v2.py --prepare    # also probe repos + cache full text + write re-review stub

Schema migration:
  * papers: add `review` (unrated until re-reviewed) and `open` (code status unknown),
    turn the old 📜 into `classic: true`, drop date-derived 🔥 (highlight is now derived).
  * datasets / benchmarks / simulators / tools: add a stable `id` used by papers' `uses`.
"""
from __future__ import annotations

import argparse
import logging
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from curation import DATA, PIPELINE, dump_yaml, finalize_review, load_papers, load_yaml, save_papers, today  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger("migrate")

RESOURCE_FILES = [
    ("datasets.yaml", "datasets"),
    ("benchmarks.yaml", "benchmarks"),
    ("simulators.yaml", "simulators"),
    ("tools.yaml", "tools"),
]


def slug(name: str) -> str:
    name = re.sub(r"\(.*?\)", "", name)
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def migrate_resources() -> None:
    seen: set[str] = set()
    for filename, key in RESOURCE_FILES:
        path = DATA / filename
        raw = path.read_text(encoding="utf-8")
        items = load_yaml(path, key)
        header = "".join(line + "\n" for line in raw.splitlines() if line.startswith("#"))
        for item in items:
            rid = item.get("id") or slug(item["name"])
            if rid in seen:
                rid = f"{rid}-{key[:-1]}"
            seen.add(rid)
            item.pop("id", None)
            # Put id first for readability.
            rebuilt = {"id": rid, **item}
            item.clear()
            item.update(rebuilt)
        path.write_text(header + "\n", encoding="utf-8")
        with path.open("a", encoding="utf-8") as f:
            import yaml

            from curation import _Dumper

            f.write(yaml.dump({key: items}, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=120))
        log.info("%s: %d items with ids", filename, len(items))


def migrate_paper(p: dict[str, Any]) -> dict[str, Any]:
    if p.get("highlight") == "📜":
        p["classic"] = True
    p.setdefault("review", {"priority": "unrated"})
    links = p.get("links") or {}
    p.setdefault(
        "open",
        {
            "code": "unknown",
            "repo": links.get("code", "") or "",
            "weights": "unknown",
            "data": "unknown",
            "license": "unknown",
        },
    )
    # Drop empty link fields left by the old ingesters.
    p["links"] = {k: v for k, v in links.items() if v}
    finalize_review(p)
    return p


def prepare_rereview(papers: list[dict[str, Any]]) -> None:
    import sources
    from fetch_candidates import enrich

    ids = [str(p["arxiv_id"]) for p in papers if p.get("arxiv_id")]
    meta = sources.arxiv_by_ids(ids)
    log.info("arXiv metadata for %d/%d papers", len(meta), len(ids))
    cands = []
    for p in papers:
        aid = str(p.get("arxiv_id") or "")
        m = meta.get(aid)
        if not m:
            log.warning("no arXiv metadata for %s (%s) — will review from links only", aid, p["title"][:60])
            continue
        m["hf"] = {"github": (p.get("links") or {}).get("code", ""), "project": (p.get("links") or {}).get("project", "")}
        m["relevance"] = None
        cands.append(m)
    with ThreadPoolExecutor(max_workers=6) as ex:
        cands = list(ex.map(enrich, cands))
    by_id = {c["arxiv_id"]: c for c in cands}

    items = []
    for p in papers:
        aid = str(p.get("arxiv_id") or "")
        c = by_id.get(aid, {})
        probe = c.get("probe", {})
        items.append(
            {
                "arxiv_id": aid,
                "title": p["title"],
                "triage": "include",
                "reason": None,
                "date_v1": c.get("published") or p.get("date"),
                "category": p.get("category"),
                "route": None,
                "contribution": None,
                "tags": p.get("tags") or [],
                "affiliations": c.get("affiliations") or [],
                "one_liner": p.get("abstract_short"),
                "summary": None,
                "venue": p.get("venue", ""),
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
        )
    import json

    out = PIPELINE / "candidates" / f"migration-{today()}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"candidates": cands}, ensure_ascii=False, indent=1), encoding="utf-8")
    run = {"scan_date": today(), "kind": "migration", "note": "re-review of all papers tracked before the v2 pipeline"}
    dump_yaml(PIPELINE / "reviews" / f"migration-{today()}.yaml", {"run": run, "items": items})
    log.info("wrote re-review stub with %d items", len(items))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prepare", action="store_true")
    args = ap.parse_args()

    if not all(i.get("id") for f, k in RESOURCE_FILES for i in load_yaml(DATA / f, k)):
        migrate_resources()
    papers = [migrate_paper(p) for p in load_papers()]
    save_papers(papers)
    log.info("migrated %d papers", len(papers))
    if args.prepare:
        prepare_rereview(papers)
    return 0


if __name__ == "__main__":
    sys.exit(main())
