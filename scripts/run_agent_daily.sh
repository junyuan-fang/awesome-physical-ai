#!/usr/bin/env bash
# Daily agent wrapper: fetch → (fill review) → apply + render + validate + commit.
#
#   bash scripts/run_agent_daily.sh [YYYY-MM-DD]
#
# Only the deterministic halves are automated. The review file
# pipeline/reviews/<date>.yaml must be filled by an agent/human following
# docs/DAILY_AGENT.md; if it is still a stub this script exits with code 2.
set -euo pipefail
cd "$(dirname "$0")/.."

DAY=${1:-$(TZ=Asia/Shanghai date +%F)}
REVIEW="pipeline/reviews/$DAY.yaml"

bash scripts/run_daily.sh fetch "$DAY"

if [[ ! -f "$REVIEW" ]]; then
  echo "❌ $REVIEW not found" >&2
  exit 1
fi

if grep -q "triage: null" "$REVIEW"; then
  echo "⏸  Review stub is still unfilled: $REVIEW"
  echo "   Fill it per docs/DAILY_AGENT.md, then re-run:"
  echo "   bash scripts/run_agent_daily.sh $DAY"
  exit 2
fi

bash scripts/run_daily.sh apply "$DAY"

if [[ -n "$(git status --porcelain data digests docs README.md pipeline/reviews topics)" ]]; then
  git add data digests docs README.md pipeline/reviews topics
  git -c user.name="${GIT_AUTHOR_NAME:-junyuan-fang}" \
      -c user.email="${GIT_AUTHOR_EMAIL:-fangjunyuan1@gmail.com}" \
      commit -m "chore: daily scan $DAY"
  git push
else
  echo "No changes to commit."
fi
