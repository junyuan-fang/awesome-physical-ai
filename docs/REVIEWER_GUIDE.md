# Reviewer guide (for humans and agents)

How to fill a review file (`pipeline/reviews/<date>.yaml` or a part `pipeline/reviews/parts/<stem>-NN.yaml`).
The rules behind every field are in [METHODOLOGY.md](METHODOLOGY.md) — read it first.

## Per item

1. **Open the cache file** `pipeline/cache/papers/<arxiv_id>.md`. It has metadata, affiliations from the arXiv HTML,
   the repo probe result, the abstract and condensed Introduction / Method / Experiments / Conclusion text plus figure/table captions.
2. **Layer 1 — triage** (metadata + abstract, skim the intro if the scope is unclear):
   - `exclude` + one-line `reason` when out of scope (not embodied / pure LLM-VLM / classical control without learning /
     no verifiable substance / pure marketing) or the contribution is clearly marginal for this list.
     Start the reason with a short category, e.g. `超出范围：纯 VLM 推理基准`, `增量过小：…`, `材料不足：…`.
   - `defer` + reason when the material is insufficient to judge (no HTML, vague abstract, only a teaser page).
   - `include` otherwise → continue.
3. **Layer 2 — read and score** from the condensed text. Open the arXiv abstract/HTML page, project page or repo only
   when a score hinges on a fact the cache does not show (e.g. whether real-robot experiments exist, whether the repo
   has training code). Record what you actually read in `evidence_read`.
   - `scores` C/E/O/T as integers 1–5 using the anchor table; one short Chinese `rationale` per dimension.
   - If you cannot score reliably, leave all four `null` and list concrete `pending_checks` → the paper stays `unrated`.
   - Do **not** compute total/priority; `apply_reviews.py` derives them (🔥 needs total ≥ 80 and E ≥ 3).
4. **Write**
   - `one_liner`: ≤ 120 Chinese characters, what it does + headline result with its benchmark.
   - `summary`: ~300–400 Chinese characters following the causal chain
     「为解决 X，提出 Y；在 Z 条件下作者报告 R；该结果提示…，但仍受…限制」. Name benchmarks, metrics, baselines and conditions
     next to any number; say 作者报告 rather than 证明.
   - `category`, `route` (core / adjacent), `contribution`, up to 5 lowercase `tags`.
   - `affiliations`: list every affiliation as printed in the paper (clean up "Affiliation:" prefixes, dedupe). Do not infer.
   - `venue`: only if the arXiv comment / journal ref states acceptance (e.g. `CoRL 2026`); otherwise leave `""`.
5. **Open status** — start from the probe (`open.code`, `repo`, `license`); correct it if the probe is obviously wrong
   (e.g. the repo is the project-page site → `placeholder`; README says code is coming → `placeholder`/`partial`) and
   explain in `open.note`. Set `weights` / `data` from the paper/README (`open / partial / gated / none / unknown / n/a`).
6. **Resources** — `uses` only for datasets/benchmarks/simulators/tools explicitly named in the data or experiment setup:
   `{resource: <id>, role: proposes|pretrain|finetune|eval}`. Valid ids are the `id:` fields in
   `data/datasets.yaml`, `data/benchmarks.yaml`, `data/simulators.yaml`, `data/tools.yaml`. A new resource worth tracking
   (widely used or proposed by this paper with a public entry) goes in `new_resources` with
   `kind` (dataset|benchmark|simulator|tool), `id`, `name`, `desc`, `links`, and `subcategory` for datasets
   (`manipulation-demos | scene-3d | egocentric-human | mocap-motion | sim-generated`) or benchmarks
   (`manipulation | navigation | locomotion | vla-generalization | multi-skill`).

## YAML hygiene

- Keep every item and its `arxiv_id`; edit fields in place. Quote strings containing `: ` or starting with special
  characters; use `|` block scalars for long text.
- Validate your file (no changes are made):
  `wsl -d Ubuntu --cd <worktree> -- python3 scripts/apply_reviews.py <your file> --check`
  (or `python3 scripts/apply_reviews.py <file> --check` on Linux/macOS). Fix every reported item.

## Calibration

- Most solid papers land at 60–79. Reserve C5/E5 for clearly field-shaping work with broad, rigorous evidence.
- O is about what is open **now** (verified), not promises. A repo with only a README is O2 at most.
- T: unknown team → 3 with a pending check; never penalise companies for having no university ranking; never raise E
  because of the team.
