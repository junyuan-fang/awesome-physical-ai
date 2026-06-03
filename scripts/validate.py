"""Validate data/*.yaml schema. Run before committing.

Exit code 0 if valid, non-zero otherwise.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

REQUIRED_PAPER_KEYS = {"title", "category", "date", "links"}
REQUIRED_COMPANY_KEYS = {"name", "region", "focus"}
REQUIRED_LIST_KEYS = {"name", "desc", "links"}


def err(msg: str) -> None:
    print(f"❌ {msg}", file=sys.stderr)


def validate_papers(known_cats: set[str]) -> int:
    path = DATA / "papers.yaml"
    if not path.exists():
        return 0
    data = yaml.safe_load(path.read_text()) or {}
    errors = 0
    for i, p in enumerate(data.get("papers", [])):
        missing = REQUIRED_PAPER_KEYS - p.keys()
        if missing:
            err(f"papers[{i}] ({p.get('title', '?')}): missing keys {missing}")
            errors += 1
        cat = p.get("category")
        if cat and cat not in known_cats:
            err(f"papers[{i}] ({p.get('title', '?')}): unknown category '{cat}'")
            errors += 1
    return errors


def validate_companies() -> int:
    path = DATA / "companies.yaml"
    if not path.exists():
        return 0
    data = yaml.safe_load(path.read_text()) or {}
    errors = 0
    for i, c in enumerate(data.get("companies", [])):
        missing = REQUIRED_COMPANY_KEYS - c.keys()
        if missing:
            err(f"companies[{i}] ({c.get('name', '?')}): missing keys {missing}")
            errors += 1
    return errors


def validate_simple_list(filename: str, root_key: str) -> int:
    path = DATA / filename
    if not path.exists():
        return 0
    data = yaml.safe_load(path.read_text()) or {}
    errors = 0
    for i, item in enumerate(data.get(root_key, [])):
        missing = REQUIRED_LIST_KEYS - item.keys()
        if missing:
            err(f"{root_key}[{i}] ({item.get('name', '?')}): missing keys {missing}")
            errors += 1
    return errors


def main() -> int:
    cats_doc = yaml.safe_load((DATA / "categories.yaml").read_text()) or {}
    known_cats: set[str] = set()
    for c in cats_doc.get("categories", []):
        known_cats.add(c["id"])
        for sub in c.get("subcategories", []) or []:
            known_cats.add(sub["id"])

    errors = 0
    errors += validate_papers(known_cats)
    errors += validate_companies()
    errors += validate_simple_list("datasets.yaml", "datasets")
    errors += validate_simple_list("simulators.yaml", "simulators")
    errors += validate_simple_list("benchmarks.yaml", "benchmarks")
    errors += validate_simple_list("tools.yaml", "tools")

    if errors:
        err(f"\n{errors} validation error(s).")
        return 1
    print("✅ All data files valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
