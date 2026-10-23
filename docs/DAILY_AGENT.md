# Daily agent runbook (08:00 Asia/Shanghai)

Self-contained instructions for the scheduled agent that runs the paper pipeline every morning.
Rules: [METHODOLOGY.md](METHODOLOGY.md) · field-by-field procedure: [REVIEWER_GUIDE.md](REVIEWER_GUIDE.md).

## Trigger / 自动触发

- **08:00 Asia/Shanghai（00:00 UTC）**：`.github/workflows/daily_fetch.yml` 自动执行
  `run_daily.sh fetch`，把当天的评审 stub 提交到 `pipeline/reviews/<date>.yaml`。
  GitHub 的定时工作流只在默认分支运行，所以 v2 合并到 master 前它不会生效；合并前
  请在本地/feature 分支用下面的方式触发。
- **评审 + 落地**：`run_daily.sh apply` 要求评审文件已填写，因此这一步由 agent/人完成。
  外部调度器（cc-connect cron、Windows 任务计划、Claude Code headless 等）在 08:00 运行：

  ```bash
  bash scripts/run_agent_daily.sh "$(TZ=Asia/Shanghai date +%F)"
  ```

  若评审仍是 stub，脚本以退出码 2 停下并提示先填 `pipeline/reviews/<date>.yaml`；
  填好后重跑同一命令即可 apply、生成 digest、渲染并校验。
- **可选：CI 内全自动**。若仓库配置了 `ANTHROPIC_API_KEY`，可以在 `daily_fetch.yml`
  之后追加一个调用 Claude Code headless 的 job；这会产生 API 费用，默认未启用。

## 0. Setup

```bash
git fetch origin
# Use master once the v2 pipeline is merged; until then work on the feature branch.
if git show origin/master:scripts/fetch_candidates.py >/dev/null 2>&1; then BR=master; else BR=feat/curation-v2; fi
git checkout "$BR" && git pull --ff-only origin "$BR"
pip install -r requirements.txt
DAY=$(TZ=Asia/Shanghai date +%F)
```

If `data/runs.yaml` already has a `daily` run with `scan_date: $DAY`, stop: today's run is done.

## 1. Fetch

```bash
bash scripts/run_daily.sh fetch "$DAY"
```

This writes `pipeline/reviews/$DAY.yaml` (stub) and `pipeline/cache/papers/<id>.md` (condensed text) for the
candidate pool. If the pool is empty, skip to step 4 and record a short note in the commit message.

## 2. Review

Read `docs/METHODOLOGY.md` and `docs/REVIEWER_GUIDE.md`, then fill every item of `pipeline/reviews/$DAY.yaml`:
layer-1 triage for all, layer-2 reading + scoring for the ones you include. The run cap (`run.cap`) limits new
inclusions; the apply step keeps core-route first, then by total, and defers the rest — so triage honestly and
do not pad. If the pool has more than ~25 items you may split it
(`python scripts/review_parts.py split pipeline/reviews/$DAY.yaml --n 3`), review the parts, then
`python scripts/review_parts.py merge pipeline/reviews/$DAY.yaml`.

Validate until clean: `python scripts/apply_reviews.py pipeline/reviews/$DAY.yaml --check`.

## 3. Apply

```bash
bash scripts/run_daily.sh apply "$DAY"
```

Merges the review, writes `digests/daily/$DAY.md`, re-checks open-source status on cadence, writes weekly
(Mondays) / monthly (1st) roll-ups, re-renders README.md + docs/index.md, validates and checks duplicates.
All must succeed.

## 4. Commit and push

```bash
git add data digests docs README.md pipeline/reviews
git commit -m "chore: daily scan $DAY (+N papers)"   # N = included count from the apply output
git push origin "$BR"
```

Never force-push and never rewrite history. If the push is rejected because the branch moved, `git pull --rebase`
and push again.

## 5. Report

Finish with: window, cap, candidates → pool → included / excluded / deferred, the 🔥 / 👀 titles, any open-status
changes, and any step that failed.
