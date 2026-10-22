#!/usr/bin/env bash
# Daily pipeline entry point (see docs/METHODOLOGY.md).
#
#   bash scripts/run_daily.sh fetch [YYYY-MM-DD]   # discovery + prefilter + cache → review stub
#   (reviewer fills pipeline/reviews/<date>.yaml)
#   bash scripts/run_daily.sh apply [YYYY-MM-DD]   # merge, digest, recheck, roll-ups, validate
set -euo pipefail
cd "$(dirname "$0")/.."

PY=${PYTHON:-python3}
DAY=${2:-$(TZ=Asia/Shanghai date +%F)}

case "${1:-}" in
  fetch)
    "$PY" scripts/fetch_candidates.py --date "$DAY"
    ;;
  apply)
    "$PY" scripts/apply_reviews.py "pipeline/reviews/$DAY.yaml" --no-readme
    "$PY" scripts/recheck_open.py
    # Weekly picks on Mondays (previous ISO week), monthly report on the 1st (previous month).
    if [ "$(date -d "$DAY" +%u)" = "1" ]; then
      "$PY" scripts/digest.py --week "$(date -d "$DAY - 7 days" +%F)"
    fi
    if [ "$(date -d "$DAY" +%d)" = "01" ]; then
      "$PY" scripts/digest.py --month "$(date -d "$DAY - 1 day" +%Y-%m)"
    fi
    "$PY" scripts/generate_readme.py
    "$PY" scripts/validate.py
    "$PY" scripts/check_duplicates.py
    ;;
  *)
    echo "usage: $0 fetch|apply [YYYY-MM-DD]" >&2
    exit 2
    ;;
esac
