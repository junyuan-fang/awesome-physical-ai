"""Fail if data/papers.yaml has duplicate arxiv_ids. Run in PR CI."""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "data" / "papers.yaml"


def main() -> int:
    doc = yaml.safe_load(PAPERS.read_text()) or {}
    ids = [p.get("arxiv_id") for p in doc.get("papers", []) if p.get("arxiv_id")]
    dups = {k: v for k, v in Counter(ids).items() if v > 1}
    if dups:
        print("❌ Duplicate arxiv_ids found:", file=sys.stderr)
        for k, v in dups.items():
            print(f"   {k}: {v}x", file=sys.stderr)
        return 1
    print(f"✅ No duplicates ({len(ids)} unique papers).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
