"""Re-check open-source status on the vla_survey cadence.

    python scripts/recheck_open.py [--all] [--limit N]

Due when: first_check < 182 days ago and last_check ≥ 7 days ago (weekly),
otherwise last_check ≥ 30 days ago (monthly). For papers without a repo we look
for a newly linked one (HF papers API, project page). When the code status moves
between levels, O is nudged by the level difference (clamped to 1..5), total and
priority are recomputed and a `history` line is recorded. Old digests stay as
snapshots; changes are summarised in digests/rechecks/<date>.md.
"""
from __future__ import annotations

import argparse
import logging
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

import sources  # noqa: E402
from curation import (  # noqa: E402
    CODE_LEVEL,
    DIGESTS,
    ROOT,
    finalize_review,
    load_config,
    load_papers,
    parse_date,
    save_papers,
    today,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger("recheck")


def is_due(o: dict[str, Any], cfg: dict[str, Any]) -> bool:
    if not o.get("last_check"):
        return True
    now = parse_date(today())
    since_first = (now - parse_date(o.get("first_check") or o["last_check"])).days
    since_last = (now - parse_date(o["last_check"])).days
    rc = cfg["recheck"]
    interval = rc["weekly_interval_days"] if since_first < rc["weekly_until_days"] else rc["monthly_interval_days"]
    return since_last >= interval


def recheck(p: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    o = p.get("open") or {}
    repo = o.get("repo") or ""
    if not repo:
        hf = sources.hf_paper(str(p.get("arxiv_id", "")))
        repo = sources.normalize_github(hf.get("github", "")) or sources.find_github_on_page(
            (p.get("links") or {}).get("project", "") or hf.get("project", "")
        )
    return p, sources.probe_repo(repo) if repo else {"code": "no-repo"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="ignore cadence")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()
    cfg = load_config()
    papers = load_papers()
    due = [p for p in papers if args.all or is_due(p.get("open") or {}, cfg)]
    if args.limit:
        due = due[: args.limit]
    log.info("%d/%d papers due for open-status recheck", len(due), len(papers))

    with ThreadPoolExecutor(max_workers=6) as ex:
        results = list(ex.map(recheck, due))

    changes: list[str] = []
    for p, probe in results:
        o = p.setdefault("open", {})
        old, new = o.get("code", "unknown"), probe.get("code", "unknown")
        if new == "unknown":  # transient failure: keep the previous state, don't bump last_check
            continue
        if probe.get("repo"):
            o["repo"] = probe["repo"]
        if probe.get("license") and o.get("license", "unknown") in ("unknown", "none-found"):
            o["license"] = probe["license"]
        if probe.get("stats"):
            o["stats"] = probe["stats"]
        o.setdefault("first_check", today())
        o["last_check"] = today()
        if old == new:
            continue
        o["code"] = new
        if old == "unknown":  # first observation, not a change
            if new in ("partial", "substantive") and o.get("repo"):
                p.setdefault("links", {})["code"] = o["repo"]
            continue
        if new in ("partial", "substantive") and o.get("repo"):
            p.setdefault("links", {})["code"] = o["repo"]
        msg = f"open.code {old} → {new}"
        scores = (p.get("review") or {}).get("scores")
        lo, ln = CODE_LEVEL.get(old), CODE_LEVEL.get(new)
        if scores and lo is not None and ln is not None and lo != ln:
            o_new = max(1, min(5, scores["O"] + (ln - lo)))
            if o_new != scores["O"]:
                msg += f"; O {scores['O']} → {o_new}"
                scores["O"] = o_new
        before = (p.get("review") or {}).get("priority")
        finalize_review(p)
        after = p["review"]["priority"]
        if before != after:
            msg += f"; priority {before} → {after}"
        p.setdefault("history", []).append({"date": today(), "change": msg + " (recheck)"})
        changes.append(f"- [{p['title']}](https://arxiv.org/abs/{p.get('arxiv_id')}) — {msg}")

    save_papers(papers)
    if changes:
        out = DIGESTS / "rechecks" / f"{today()}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            f"# 开放状态复查：{today()}\n\n复查 {len(due)} 篇，状态变化 {len(changes)} 篇（变化只更新原条目，不占新增名额）。\n\n"
            + "\n".join(changes)
            + "\n",
            encoding="utf-8",
        )
        log.info("wrote %s", out.relative_to(ROOT))
    log.info("rechecked %d, changed %d", len(due), len(changes))
    return 0


if __name__ == "__main__":
    sys.exit(main())
