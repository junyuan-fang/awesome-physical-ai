"""Validate data/*.yaml schema and curation invariants. Run before committing.

Exit code 0 if valid, non-zero otherwise.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from curation import (  # noqa: E402
    ASSET_STATUS,
    CODE_STATUS,
    CONTRIBUTIONS,
    DATA,
    EVIDENCE_LEVELS,
    ROUTES,
    TRIAGE,
    USE_ROLES,
    WEIGHTS,
    compute_total,
    derive_priority,
    highlight_for,
    load_yaml,
)

REQUIRED_PAPER_KEYS = {"title", "category", "date", "links", "review", "open"}
REQUIRED_COMPANY_KEYS = {"name", "region", "focus"}
REQUIRED_LIST_KEYS = {"id", "name", "desc", "links"}
DATE_RE = re.compile(r"^\d{4}-\d{2}(-\d{2})?$")
DAY_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class Errors:
    def __init__(self) -> None:
        self.n = 0

    def __call__(self, msg: str) -> None:
        print(f"❌ {msg}", file=sys.stderr)
        self.n += 1


def validate_paper(i: int, p: dict, known_cats: set[str], resource_ids: set[str], err: Errors) -> None:
    tag = f"papers[{i}] ({p.get('arxiv_id') or p.get('title', '?')})"
    missing = REQUIRED_PAPER_KEYS - p.keys()
    if missing:
        err(f"{tag}: missing keys {sorted(missing)}")
        return
    if p["category"] not in known_cats:
        err(f"{tag}: unknown category '{p['category']}'")
    if not DATE_RE.match(str(p["date"])):
        err(f"{tag}: date must be YYYY-MM-DD (first public version), got {p['date']!r}")
    if p.get("route") and p["route"] not in ROUTES:
        err(f"{tag}: route must be one of {ROUTES}")
    if p.get("contribution") and p["contribution"] not in CONTRIBUTIONS:
        err(f"{tag}: contribution must be one of {CONTRIBUTIONS}")

    review = p["review"] or {}
    scores = review.get("scores")
    if scores:
        if set(scores) != set(WEIGHTS):
            err(f"{tag}: review.scores must have exactly {sorted(WEIGHTS)}")
        elif not all(isinstance(scores[k], int) and 1 <= scores[k] <= 5 for k in WEIGHTS):
            err(f"{tag}: review.scores must be integers in 1..5")
        else:
            if review.get("total") != compute_total(scores):
                err(f"{tag}: review.total {review.get('total')} != 6C+5E+6O+3T = {compute_total(scores)}")
            evidence = review.get("evidence_read") or []
            if not set(evidence) <= set(EVIDENCE_LEVELS):
                err(f"{tag}: unknown evidence_read level in {evidence}")
            if set(evidence) <= {"abstract"}:
                err(f"{tag}: scored papers must be read beyond the abstract (evidence_read)")
            if review.get("priority") == "must-read" and "experiments" not in evidence:
                err(f"{tag}: must-read requires 'experiments' in evidence_read")
            if not review.get("rationale"):
                err(f"{tag}: scored papers need review.rationale")
            if not DAY_RE.match(str(review.get("reviewed", ""))):
                err(f"{tag}: scored papers need review.reviewed (YYYY-MM-DD)")
    if review.get("priority") != derive_priority(scores):
        err(f"{tag}: review.priority {review.get('priority')!r} != derived {derive_priority(scores)!r}")
    if p.get("highlight", "") != highlight_for(p):
        err(f"{tag}: highlight {p.get('highlight')!r} != derived {highlight_for(p)!r} (run apply/finalize)")

    open_ = p["open"] or {}
    if open_.get("code", "unknown") not in CODE_STATUS:
        err(f"{tag}: open.code must be one of {CODE_STATUS}")
    if open_.get("code") in ("placeholder", "partial", "substantive") and not open_.get("repo"):
        err(f"{tag}: open.code={open_['code']} requires open.repo")
    for k in ("weights", "data"):
        if open_.get(k, "unknown") not in ASSET_STATUS:
            err(f"{tag}: open.{k} must be one of {ASSET_STATUS}")
    for k in ("first_check", "last_check"):
        if open_.get(k) and not DAY_RE.match(str(open_[k])):
            err(f"{tag}: open.{k} must be YYYY-MM-DD")

    for u in p.get("uses") or []:
        if u.get("resource") not in resource_ids:
            err(f"{tag}: uses → unknown resource id {u.get('resource')!r}")
        if u.get("role") not in USE_ROLES:
            err(f"{tag}: uses role must be one of {USE_ROLES}")


def validate_papers(known_cats: set[str], resource_ids: set[str], err: Errors) -> None:
    for i, p in enumerate(load_yaml(DATA / "papers.yaml", "papers")):
        validate_paper(i, p, known_cats, resource_ids, err)


def validate_companies(err: Errors) -> None:
    for i, c in enumerate(load_yaml(DATA / "companies.yaml", "companies")):
        missing = REQUIRED_COMPANY_KEYS - c.keys()
        if missing:
            err(f"companies[{i}] ({c.get('name', '?')}): missing keys {missing}")


def validate_resource_list(filename: str, root_key: str, err: Errors) -> set[str]:
    ids: set[str] = set()
    for i, item in enumerate(load_yaml(DATA / filename, root_key)):
        missing = REQUIRED_LIST_KEYS - item.keys()
        if missing:
            err(f"{root_key}[{i}] ({item.get('name', '?')}): missing keys {missing}")
        rid = item.get("id")
        if rid in ids:
            err(f"{root_key}[{i}]: duplicate id {rid!r}")
        ids.add(rid)
        access = item.get("access")
        if access and access not in ASSET_STATUS:
            err(f"{root_key}[{i}] ({rid}): access must be one of {ASSET_STATUS}")
    return ids


def validate_triage_log(err: Errors) -> None:
    for i, t in enumerate(load_yaml(DATA / "triage_log.yaml", "entries")):
        if t.get("decision") not in TRIAGE:
            err(f"triage_log[{i}] ({t.get('arxiv_id')}): decision must be one of {TRIAGE}")


def main() -> int:
    err = Errors()
    known_cats: set[str] = set()
    for c in load_yaml(DATA / "categories.yaml", "categories"):
        known_cats.add(c["id"])
        for sub in c.get("subcategories", []) or []:
            known_cats.add(sub["id"])

    resource_ids: set[str] = set()
    all_ids: list[str] = []
    for filename, key in (
        ("datasets.yaml", "datasets"),
        ("benchmarks.yaml", "benchmarks"),
        ("simulators.yaml", "simulators"),
        ("tools.yaml", "tools"),
    ):
        ids = validate_resource_list(filename, key, err)
        all_ids += list(ids)
        resource_ids |= ids
    dup = {x for x in all_ids if all_ids.count(x) > 1}
    if dup:
        err(f"resource ids must be unique across datasets/benchmarks/simulators/tools: {sorted(dup)}")

    validate_papers(known_cats, resource_ids, err)
    validate_companies(err)
    validate_triage_log(err)

    if err.n:
        print(f"\n❌ {err.n} validation error(s).", file=sys.stderr)
        return 1
    print("✅ All data files valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
