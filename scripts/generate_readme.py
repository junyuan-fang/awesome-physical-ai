"""Render README.md and docs/index.md from data/*.yaml.

Usage:
    python scripts/generate_readme.py
"""
from __future__ import annotations

import re
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import Any

import yaml
from jinja2 import ChainableUndefined, Environment, FileSystemLoader

sys.path.insert(0, str(Path(__file__).resolve().parent))

from curation import CODE_BADGE, PRIORITY_RANK, load_config, sort_key  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TEMPLATES = ROOT / "templates"
OUTPUT = ROOT / "README.md"
INDEX_OUTPUT = ROOT / "docs" / "index.md"

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
    s = " ".join(text.split())
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
    with path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data.get(key, []) if key else data


def paper_groups(papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Split a category's papers into display groups, each sorted by priority/score/date."""
    classic = sorted([p for p in papers if p.get("classic")], key=lambda p: str(p.get("date")), reverse=True)
    rest = [p for p in papers if not p.get("classic")]
    top = sorted([p for p in rest if PRIORITY_RANK[p["review"]["priority"]] <= 1], key=sort_key)
    other = sorted([p for p in rest if PRIORITY_RANK[p["review"]["priority"]] > 1], key=sort_key)
    groups = []
    if top:
        groups.append({"icon": "🔥", "title": "Must-read & notable / 重点与值得关注", "open": True, "papers": top})
    if other:
        groups.append({"icon": "📋", "title": "Also tracked / 观察中与暂不评级", "open": False, "papers": other})
    if classic:
        groups.append({"icon": "📜", "title": "Classic landmarks / 经典奠基", "open": False, "papers": classic})
    return groups


def main() -> int:
    cfg = load_config()
    categories = load_yaml(DATA / "categories.yaml", "categories")
    categories.sort(key=lambda c: c.get("order", 999))
    papers = load_yaml(DATA / "papers.yaml", "papers")
    for p in papers:
        p.setdefault("review", {"priority": "unrated"})
        p.setdefault("open", {})

    # Normalize companies — fill missing fields with defaults so template sort works
    companies_raw = load_yaml(DATA / "companies.yaml", "companies")
    for c in companies_raw:
        c.setdefault("last_valuation_usd", 0)
        c.setdefault("funding", [])
        c.setdefault("products", [])
        c.setdefault("website", "")
        c.setdefault("notes", "")

    # Paper sections: a category with subcategories gets one block per subcategory.
    sections: dict[str, list[dict[str, Any]]] = {}
    for cat in categories:
        if cat.get("source"):
            continue
        blocks = []
        subs = cat.get("subcategories") or []
        for sub in subs:
            items = [p for p in papers if p["category"] == sub["id"]]
            if items:
                blocks.append({"title": sub["title"], "count": len(items), "groups": paper_groups(items)})
        own = [p for p in papers if p["category"] == cat["id"]]
        if own:
            title = "Other" if blocks else None
            blocks.append({"title": title, "count": len(own), "groups": paper_groups(own)})
        sections[cat["id"]] = blocks

    # Resource → papers that use it (from papers' `uses`).
    used_by: dict[str, list[dict[str, Any]]] = {}
    for p in papers:
        for u in p.get("uses") or []:
            used_by.setdefault(u["resource"], []).append({"paper": p, "role": u["role"]})

    week_ago = (date.today() - timedelta(days=7)).isoformat()
    picks = sorted(
        [
            p
            for p in papers
            if str(p.get("added", "")) >= week_ago and p["review"]["priority"] in ("must-read", "notable")
        ],
        key=sort_key,
    )[: int(cfg.get("weekly_cap", 15))]

    digests = sorted((ROOT / "digests" / "daily").glob("*.md"), reverse=True)
    priority_counts = {k: sum(1 for p in papers if p["review"]["priority"] == k) for k in PRIORITY_RANK}

    context = {
        "categories": categories,
        "papers": papers,
        "sections": sections,
        "picks": picks,
        "used_by": used_by,
        "latest_digest": digests[0].relative_to(ROOT).as_posix() if digests else "",
        "code_badge": CODE_BADGE,
        "companies": companies_raw,
        "datasets": load_yaml(DATA / "datasets.yaml", "datasets"),
        "simulators": load_yaml(DATA / "simulators.yaml", "simulators"),
        "benchmarks": load_yaml(DATA / "benchmarks.yaml", "benchmarks"),
        "tools": load_yaml(DATA / "tools.yaml", "tools"),
        "last_updated": date.today().isoformat(),
        "year": date.today().year,
        "priority_counts": priority_counts,
    }
    context["stats"] = {
        "papers": len(papers),
        "companies": len(context["companies"]),
        "simulators": len(context["simulators"]),
        "datasets": len(context["datasets"]),
        "benchmarks": len(context["benchmarks"]),
        "tools": len(context["tools"]),
    }
    context["index_categories"] = [
        {
            "id": cid,
            "title": next(
                (s["title"] for c in categories for s in (c.get("subcategories") or []) if s["id"] == cid),
                next((c["title"] for c in categories if c["id"] == cid), cid),
            ),
            "papers": sorted([p for p in papers if p["category"] == cid], key=sort_key),
        }
        for cid in dict.fromkeys(p["category"] for p in sorted(papers, key=lambda p: p["category"]))
    ]

    # Top-20 overall ranking (priority → total → newest date) and category titles.
    cat_titles: dict[str, str] = {}
    for c in categories:
        cat_titles[c["id"]] = c["title"]
        for sub in c.get("subcategories") or []:
            cat_titles[sub["id"]] = sub["title"]
    context["category_titles"] = cat_titles
    context["top_papers"] = sorted(
        [p for p in papers if (p.get("review") or {}).get("total")], key=sort_key
    )[:20]

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES)),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
        undefined=ChainableUndefined,
    )
    env.filters["clean_abstract"] = clean_abstract
    env.filters["cell"] = lambda s: " ".join(str(s or "").split()).replace("|", "\\|")
    OUTPUT.write_text(env.get_template("README.md.j2").render(**context), encoding="utf-8")
    INDEX_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    INDEX_OUTPUT.write_text(env.get_template("index.md.j2").render(**context), encoding="utf-8")
    print(f"✅ Wrote README.md + docs/index.md — {context['stats']} · {priority_counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
