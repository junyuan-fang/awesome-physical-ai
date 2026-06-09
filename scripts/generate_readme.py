"""Render README.md from data/*.yaml using templates/README.md.j2.

Usage:
    python scripts/generate_readme.py
"""
from __future__ import annotations

import re
import sys
from datetime import date, timedelta
from pathlib import Path

import yaml
from jinja2 import ChainableUndefined, Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TEMPLATES = ROOT / "templates"
OUTPUT = ROOT / "README.md"

# Sentence-ending punctuation in both English and Chinese.
_SENTENCE_END = ".!?。！？"


def clean_abstract(text: str, max_len: int = 220) -> str:
    """Tidy a paper one-liner for display.

    Machine-ingested abstracts arrive truncated mid-sentence with a trailing
    ``...``. Curated one-liners (no trailing ellipsis) are left untouched.
    For truncated text we drop the ellipsis and cut back to the last complete
    sentence so the line never ends mid-thought.
    """
    if not text:
        return text
    s = text.strip()
    # Detect & strip a machine-truncation marker (… or ...).
    truncated = bool(re.search(r"(\.\.\.|…)$", s))
    if not truncated:
        return s
    s = re.sub(r"\s*(\.\.\.|…)$", "", s).rstrip()
    # Prefer cutting to the last complete sentence within max_len.
    window = s[:max_len]
    cut = max(window.rfind(c) for c in _SENTENCE_END)
    if cut >= 60:  # keep at least a meaningful clause
        return window[: cut + 1].strip()
    # No sentence boundary found — trim to a word boundary and add an ellipsis.
    if len(s) > max_len:
        s = s[:max_len].rsplit(" ", 1)[0].rstrip()
    return s + " …"


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
        # Used by the "Recent additions" section in the template; YYYY-MM cutoff
        "recent_cutoff": (date.today() - timedelta(days=45)).strftime("%Y-%m"),
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
    env.filters["clean_abstract"] = clean_abstract
    tmpl = env.get_template("README.md.j2")
    rendered = tmpl.render(**context)

    OUTPUT.write_text(rendered, encoding="utf-8")
    print(f"✅ Wrote {OUTPUT.relative_to(ROOT)} — {context['stats']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
