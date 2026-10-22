"""Shared curation logic: schema constants, scoring, priority, YAML I/O, run caps.

The rules here are the executable form of docs/METHODOLOGY.md (adapted from the
vla_survey workflow): two-layer screening, four-dimension scoring, open-status
tracking with a recheck cadence, and per-run inclusion caps.
"""
from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PIPELINE = ROOT / "pipeline"
DIGESTS = ROOT / "digests"
PAPERS_YAML = DATA / "papers.yaml"
RUNS_YAML = DATA / "runs.yaml"
TRIAGE_LOG = DATA / "triage_log.yaml"
CONFIG_YAML = DATA / "config.yaml"

# ---------------------------------------------------------------- schema enums
ROUTES = ("core", "adjacent")
CONTRIBUTIONS = ("model", "method", "data", "benchmark", "infra", "system", "survey", "hardware")
PRIORITIES = ("must-read", "notable", "watching", "unrated")
EVIDENCE_LEVELS = ("abstract", "intro", "method", "experiments", "appendix", "project", "code")
CODE_STATUS = ("no-repo", "placeholder", "partial", "substantive", "unknown")
ASSET_STATUS = ("open", "partial", "gated", "none", "unknown", "n/a")
USE_ROLES = ("proposes", "pretrain", "finetune", "eval")
TRIAGE = ("include", "defer", "exclude")

PRIORITY_BADGE = {"must-read": "🔥", "notable": "👀", "watching": "", "unrated": ""}
PRIORITY_RANK = {"must-read": 0, "notable": 1, "watching": 2, "unrated": 3}
CODE_BADGE = {
    "substantive": "💻",
    "partial": "🟡",
    "placeholder": "📄",
    "no-repo": "",
    "unknown": "",
}
# Ordinal openness of the code release, used to nudge the O score on recheck.
CODE_LEVEL = {"unknown": None, "no-repo": 0, "placeholder": 0, "partial": 1, "substantive": 2}

# Weights from vla_survey: C 30% / E 25% / O 30% / T 15%; score s in 1..5 → s/5*w.
WEIGHTS = {"C": 6, "E": 5, "O": 6, "T": 3}


def compute_total(scores: dict[str, int]) -> int:
    return sum(WEIGHTS[k] * int(scores[k]) for k in WEIGHTS)


def derive_priority(scores: dict[str, int] | None) -> str:
    """must-read: total ≥ 80 and E ≥ 3 · notable: 65–79 · watching: < 65."""
    if not scores or any(scores.get(k) in (None, "") for k in WEIGHTS):
        return "unrated"
    total = compute_total(scores)
    if total >= 80 and int(scores["E"]) >= 3:
        return "must-read"
    if total >= 65:
        return "notable"
    return "watching"


def highlight_for(paper: dict[str, Any]) -> str:
    if paper.get("classic"):
        return "📜"
    return PRIORITY_BADGE[paper.get("review", {}).get("priority", "unrated")]


def finalize_review(paper: dict[str, Any]) -> None:
    """Recompute derived fields (total, priority, highlight) in place."""
    review = paper.setdefault("review", {})
    scores = review.get("scores")
    if scores and all(scores.get(k) not in (None, "") for k in WEIGHTS):
        review["total"] = compute_total(scores)
    else:
        review.pop("total", None)
    review["priority"] = derive_priority(scores)
    paper["highlight"] = highlight_for(paper)


def sort_key(paper: dict[str, Any]) -> tuple:
    review = paper.get("review", {})
    return (
        PRIORITY_RANK.get(review.get("priority", "unrated"), 3),
        -(review.get("total") or 0),
        _neg_date(paper.get("date", "")),
    )


def _neg_date(d: str) -> str:
    # Invert digits so that ascending sort puts newer dates first.
    return "".join(chr(ord("9") - ord(c) + ord("0")) if c.isdigit() else c for c in str(d))


# ------------------------------------------------------------------- YAML I/O
class _Dumper(yaml.SafeDumper):
    pass


def _str_presenter(dumper: yaml.SafeDumper, value: str):
    style = "|" if "\n" in value else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=style)


_Dumper.add_representer(str, _str_presenter)


def load_yaml(path: Path, key: str | None = None, default: Any = None):
    if not path.exists():
        return default if default is not None else ([] if key else {})
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if key:
        return data.get(key, default if default is not None else [])
    return data


def dump_yaml(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.dump(data, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )


def load_papers() -> list[dict[str, Any]]:
    return load_yaml(PAPERS_YAML, "papers")


def save_papers(papers: list[dict[str, Any]]) -> None:
    dump_yaml(PAPERS_YAML, {"papers": papers})


def load_config() -> dict[str, Any]:
    return load_yaml(CONFIG_YAML)


def today() -> str:
    return date.today().isoformat()


def parse_date(s: str) -> date:
    return datetime.strptime(str(s)[:10], "%Y-%m-%d").date()


# ------------------------------------------------------------------ run caps
def run_cap(scan_date: str, last_end: str | None, cfg: dict[str, Any] | None = None) -> tuple[int, int]:
    """Return (d, cap) with d = max(1, scan_date - last_end) and cap = min(per_day·d, max)."""
    cfg = cfg or load_config()
    per_day = int(cfg.get("cap_per_day", 5))
    cap_max = int(cfg.get("cap_max", 20))
    if not last_end:
        return 1, cap_max
    d = max(1, (parse_date(scan_date) - parse_date(last_end)).days)
    return d, min(per_day * d, cap_max)


def last_run() -> dict[str, Any] | None:
    runs = load_yaml(RUNS_YAML, "runs")
    regular = [r for r in runs if r.get("kind", "daily") == "daily"]
    return regular[-1] if regular else None
