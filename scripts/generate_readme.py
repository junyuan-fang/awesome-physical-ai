"""Render README.md from data/*.yaml using templates/README.md.j2.

Usage:
    python scripts/generate_readme.py
"""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

import yaml
from jinja2 import ChainableUndefined, Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TEMPLATES = ROOT / "templates"
OUTPUT = ROOT / "README.md"


def load_yaml(path: Path, key: str | None = None):
    if not path.exists():
        return [] if key else {}
    with path.open() as f:
        data = yaml.safe_load(f) or {}
    return data.get(key, []) if key else data


def main() -> int:
    categories = load_yaml(DATA / "categories.yaml", "categories")
    categories.sort(key=lambda c: c.get("order", 999))

    # Normalize companies — fill missing fields with defaults so template sort works
    companies_raw = load_yaml(DATA / "companies.yaml", "companies")
    for c in companies_raw:
        c.setdefault("last_valuation_usd", 0)
        c.setdefault("funding", [])
        c.setdefault("products", [])
        c.setdefault("website", "")
        c.setdefault("notes", "")

    context = {
        "categories": categories,
        "papers": load_yaml(DATA / "papers.yaml", "papers"),
        "companies": companies_raw,
        "datasets": load_yaml(DATA / "datasets.yaml", "datasets"),
        "simulators": load_yaml(DATA / "simulators.yaml", "simulators"),
        "benchmarks": load_yaml(DATA / "benchmarks.yaml", "benchmarks"),
        "tools": load_yaml(DATA / "tools.yaml", "tools"),
        "last_updated": date.today().isoformat(),
        "year": date.today().year,
    }
    context["stats"] = {
        "papers": len(context["papers"]),
        "companies": len(context["companies"]),
        "simulators": len(context["simulators"]),
        "datasets": len(context["datasets"]),
        "benchmarks": len(context["benchmarks"]),
        "tools": len(context["tools"]),
    }

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES)),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
        undefined=ChainableUndefined,
    )
    tmpl = env.get_template("README.md.j2")
    rendered = tmpl.render(**context)

    OUTPUT.write_text(rendered, encoding="utf-8")
    print(f"✅ Wrote {OUTPUT.relative_to(ROOT)} — {context['stats']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
