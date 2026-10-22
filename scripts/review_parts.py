"""Split a review stub into parts for parallel reviewers, and merge them back.

    python scripts/review_parts.py split pipeline/reviews/2026-10-22.yaml --n 4
    python scripts/review_parts.py merge pipeline/reviews/2026-10-22.yaml

Parts live in pipeline/reviews/parts/<stem>-NN.yaml; merge keeps the stub's order
and refuses to merge if an item is missing from every part.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from curation import dump_yaml, load_yaml  # noqa: E402


def parts_dir(path: Path) -> Path:
    return path.parent / "parts"


def split(path: Path, n: int) -> None:
    doc = load_yaml(path)
    items = doc["items"]
    size = -(-len(items) // n)
    for i in range(n):
        chunk = items[i * size : (i + 1) * size]
        if not chunk:
            continue
        out = parts_dir(path) / f"{path.stem}-{i + 1:02d}.yaml"
        dump_yaml(out, {"run": doc.get("run"), "items": chunk})
        print(f"{out} · {len(chunk)} items")


def merge(path: Path) -> int:
    doc = load_yaml(path)
    reviewed = {}
    for part in sorted(parts_dir(path).glob(f"{path.stem}-*.yaml")):
        for it in load_yaml(part).get("items") or []:
            reviewed[str(it["arxiv_id"])] = it
    missing = [str(it["arxiv_id"]) for it in doc["items"] if str(it["arxiv_id"]) not in reviewed]
    if missing:
        print(f"❌ {len(missing)} item(s) missing from parts: {missing[:10]}", file=sys.stderr)
        return 1
    doc["items"] = [reviewed[str(it["arxiv_id"])] for it in doc["items"]]
    dump_yaml(path, doc)
    print(f"✅ merged {len(doc['items'])} items into {path}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["split", "merge"])
    ap.add_argument("review_file")
    ap.add_argument("--n", type=int, default=4)
    args = ap.parse_args()
    path = Path(args.review_file)
    if args.cmd == "split":
        split(path, args.n)
        return 0
    return merge(path)


if __name__ == "__main__":
    sys.exit(main())
