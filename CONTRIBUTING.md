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

**Do NOT edit `README.md` directly** — it is auto-generated from `data/`.

Use existing entries as a template. Run locally before pushing:

```bash
pip install -r requirements.txt
python scripts/validate.py
python scripts/generate_readme.py
```

GitHub Actions will reject PRs that fail validation.

## 3. Quality bar

- ✅ Papers should have a verifiable arXiv link or official paper PDF
- ✅ Companies should have a website or official LinkedIn page
- ✅ Tools/sims should have an open-source repo or official docs page
- ❌ No personal blog posts unless they cover novel methodology
- ❌ No paid/closed-source SaaS without a free tier
- ❌ No vague "we're building AGI" startups without product or technical evidence

## Auto-update note

Papers are auto-ingested from my [daily paper aggregation pipeline](https://github.com/junyuan-fang/personal_planning) via `scripts/ingest_dailypaper.py`. Only entries rated 🔥 or 👀 by the human-in-the-loop review stage land here.

PR-submitted entries are kept alongside auto-ingested ones.

## License

By contributing you agree your contributions will be MIT licensed (see [LICENSE](LICENSE)).
