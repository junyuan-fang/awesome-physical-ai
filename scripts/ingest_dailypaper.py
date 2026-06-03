"""Ingest new papers from your dailypaper pipeline JSON into data/papers.yaml.

Workflow (designed to run from your daily cron, after dailypaper review):
    1. Read enriched JSON output from dailypaper.
    2. Skip entries already in data/papers.yaml (by arxiv_id).
    3. Skip 💤 (low-relevance) entries — only ingest 🔥 / 👀.
    4. Map dailypaper category → awesome category (best-effort heuristics).
    5. Append to data/papers.yaml.
    6. Re-render README.md.

Usage:
    python scripts/ingest_dailypaper.py /path/to/daily_papers_enriched.json
    # or use default:
    python scripts/ingest_dailypaper.py
"""
from __future__ import annotations

import json
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
PAPERS_YAML = ROOT / "data" / "papers.yaml"

DEFAULT_INPUT = Path.home() / "code/claude_bot/dailypaper/output/daily_papers_enriched.json"

# Mapping from dailypaper tags / method_names to awesome category ids.
# Order matters — first match wins.
CATEGORY_HEURISTICS: list[tuple[str, str]] = [
    ("vla", "vla"),
    ("vision-language-action", "vla"),
    ("foundation model", "foundation-models"),
    ("world model", "foundation-models"),
    ("teleop", "teleoperation"),
    ("teleoperation", "teleoperation"),
    ("locomotion", "locomotion"),
    ("walking", "locomotion"),
    ("humanoid", "locomotion"),
    ("manipulation", "manipulation"),
    ("grasp", "manipulation"),
    ("dexterous", "manipulation"),
    ("bimanual", "manipulation"),
    ("sim2real", "sim2real"),
    ("sim-to-real", "sim2real"),
    ("domain randomization", "sim2real"),
    ("gaussian splatting", "scene"),
    ("nerf", "scene"),
    ("scene understanding", "scene"),
    ("3d segmentation", "scene"),
    ("navigation", "navigation"),
    ("embodied qa", "navigation"),
    ("diffusion policy", "rl-il"),
    ("imitation learning", "rl-il"),
    ("reinforcement learning", "rl-il"),
]


def guess_category(paper: dict[str, Any]) -> str:
    """Best-effort category mapping."""
    haystack = " ".join(
        str(x).lower()
        for x in (
            paper.get("title", ""),
            paper.get("abstract", ""),
            " ".join(paper.get("tags", []) or []),
            " ".join(paper.get("method_names", []) or []),
        )
    )
    for needle, cat in CATEGORY_HEURISTICS:
        if needle in haystack:
            return cat
    return "manipulation"  # default bucket


def convert(paper: dict[str, Any]) -> dict[str, Any]:
    """Convert dailypaper JSON entry → awesome papers.yaml entry."""
    return {
        "arxiv_id": paper.get("arxiv_id") or paper.get("id"),
        "title": paper.get("title", "").strip(),
        "authors": paper.get("authors_short")
        or _short_authors(paper.get("authors", [])),
        "date": (paper.get("submission_date") or paper.get("date", ""))[:7],
        "category": guess_category(paper),
        "tags": paper.get("tags", [])[:4],
        "abstract_short": (paper.get("abstract_short") or paper.get("abstract", ""))[
            :240
        ],
        "links": {
            "arxiv": paper.get("arxiv_url")
            or f"https://arxiv.org/abs/{paper.get('arxiv_id', '')}",
            "project": paper.get("project_url", ""),
            "code": paper.get("code_url", ""),
            "demo": paper.get("demo_url", ""),
        },
        "highlight": paper.get("review_rating", "👀"),
        "added": date.today().isoformat(),
        "source": "dailypaper",
    }


def _short_authors(authors: list[str] | str) -> str:
    if isinstance(authors, str):
        return authors
    if not authors:
        return ""
    if len(authors) == 1:
        return authors[0]
    return f"{authors[0]} et al."


def main(argv: list[str]) -> int:
    input_path = Path(argv[1]) if len(argv) > 1 else DEFAULT_INPUT
    if not input_path.exists():
        print(f"❌ Input not found: {input_path}", file=sys.stderr)
        return 1

    with input_path.open() as f:
        incoming = json.load(f)
    if isinstance(incoming, dict):
        incoming = incoming.get("papers", [])

    existing_doc = yaml.safe_load(PAPERS_YAML.read_text()) or {}
    existing_papers: list[dict[str, Any]] = existing_doc.get("papers", [])
    existing_ids = {p.get("arxiv_id") for p in existing_papers}

    added = 0
    for p in incoming:
        if (p.get("review_rating") or "") not in ("🔥", "👀"):
            continue
        if p.get("arxiv_id") in existing_ids:
            continue
        entry = convert(p)
        existing_papers.append(entry)
        existing_ids.add(entry["arxiv_id"])
        added += 1

    if added == 0:
        print("✅ No new high-relevance papers to add.")
        return 0

    PAPERS_YAML.write_text(
        yaml.safe_dump(
            {"papers": existing_papers},
            sort_keys=False,
            allow_unicode=True,
            width=120,
        ),
        encoding="utf-8",
    )
    print(f"✅ Added {added} new paper(s) to {PAPERS_YAML.name}.")

    # Re-render README
    subprocess.check_call(
        [sys.executable, str(ROOT / "scripts" / "generate_readme.py")]
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
