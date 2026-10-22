# Contributing to Awesome Physical AI

Thanks for your interest in keeping this list fresh! Three ways to contribute:

## 1. Open an issue (easiest)

Pick one of the templates:
- **Add a paper** — propose a new paper
- **Suggest a company** — add or update a startup
- **Report outdated info** — flag stale entries

I'll triage and merge or convert into a PR.

## 2. Open a PR

Edit the relevant YAML file under `data/`:

| You want to add a... | Edit this file |
|---|---|
| Paper | `data/papers.yaml` |
| Startup / company | `data/companies.yaml` |
| Dataset | `data/datasets.yaml` |
| Simulator | `data/simulators.yaml` |
| Benchmark | `data/benchmarks.yaml` |
| Tool / library | `data/tools.yaml` |
| New category section | `data/categories.yaml` |

**Do NOT edit `README.md` or `docs/index.md` directly** — both are auto-generated from `data/`.

Use existing entries as a template. A paper needs at least `title / category / date / links / review / open`;
a PR-submitted paper may enter as `review: {priority: unrated}` and `open: {code: unknown}` — it will be
scored by the next review run. If you do score it, follow [docs/METHODOLOGY.md](docs/METHODOLOGY.md):
four 1–5 scores with a one-line rationale each, `evidence_read` beyond the abstract, and let
`scripts/apply_reviews.py` (or `curation.finalize_review`) derive `total / priority / highlight` — never hand-set 🔥.
Datasets / benchmarks / simulators / tools need a unique `id`, which papers reference in `uses`.

Run locally before pushing:

```bash
pip install -r requirements.txt
python scripts/validate.py
python scripts/generate_readme.py
```

GitHub Actions will reject PRs that fail validation (schema, score formula, derived priority, `uses` ids).

## 3. Quality bar

- ✅ Papers should have a verifiable arXiv link or official paper PDF
- ✅ Companies should have a website or official LinkedIn page
- ✅ Tools/sims should have an open-source repo or official docs page
- ❌ No personal blog posts unless they cover novel methodology
- ❌ No paid/closed-source SaaS without a free tier
- ❌ No vague "we're building AGI" startups without product or technical evidence

## Auto-update note

Every morning (08:00 Asia/Shanghai) a scheduled agent runs the pipeline described in
[docs/METHODOLOGY.md](docs/METHODOLOGY.md):

1. `scripts/run_daily.sh fetch` — discover candidates directly from arXiv + HuggingFace daily papers,
   dedupe against `data/papers.yaml` and `data/triage_log.yaml`, prefilter, probe repos, cache full text.
2. The agent fills `pipeline/reviews/<date>.yaml`: layer-1 triage, then layer-2 reading and four-dimension scoring.
3. `scripts/run_daily.sh apply` — enforce the run cap, merge, write `digests/daily/<date>.md`,
   re-check open-source status on the weekly/monthly cadence, roll up weekly/monthly picks, re-render, validate.

Every judgement (including exclusions) is committed in `pipeline/reviews/` and `data/triage_log.yaml`,
so you can audit or overturn it in a PR. The legacy ingesters (`ingest_dailypaper.py`,
`ingest_from_news_archive.py`) still work but add papers as `unrated` until reviewed.

## License

By contributing you agree your contributions will be MIT licensed (see [LICENSE](LICENSE)).
