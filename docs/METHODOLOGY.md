# Curation methodology / 收录与评审方法

本仓库的论文收录流程改编自内部 `vla_survey` 工作流：**宽进（自动发现）+ 严评（两层筛选、四维评分）+ 持续复查（开放状态）**。规则的可执行部分在 `scripts/curation.py` 与 `scripts/validate.py` 中，CI 会拒绝违反这些约束的数据。

## 1. 每轮流程

```
fetch_candidates.py ──► pipeline/candidates/<date>.json + pipeline/cache/papers/<id>.md
        │                    （原始渠道发现 · 去重 · 相关性预筛 · 仓库探测 · 正文抽取）
        ▼
reviewer（人或 agent）填写 pipeline/reviews/<date>.yaml        ← 本文第 3–6 节
        ▼
apply_reviews.py ──► data/papers.yaml · data/triage_log.yaml · data/runs.yaml
                     digests/daily/<date>.md · README.md · docs/index.md
```

一条命令跑完非人工部分：`bash scripts/run_daily.sh fetch`，评审写完后 `bash scripts/run_daily.sh apply`。

## 2. 时间窗口与数量上限

- 时区 `Asia/Shanghai`。令 `d = max(1, 本次扫描日 − 上次已完成扫描的覆盖截止日)`，本轮**新增**收录上限 `cap = min(5·d, 20)`（`data/config.yaml` 可调）。间隔 1/2/3 天 → 5/10/15 篇，≥4 天 → 20 篇。
- 窗口向上次截止日之前重叠回看 2 天；已收录 / 已分诊的 arXiv ID 不重复处理。
- **上限是天花板不是目标**，不为凑数降低门槛。超过上限时 `apply_reviews.py` 优先保留核心路线，再按总分取前 `cap`，其余记为 `defer`（理由 "over cap"）。
- 周精选 ≤15、月精选 ≤30（`make_digest.py`），按首次公开日期归属周期，迟发现的工作标注「迟发现」。
- 状态复查（开放状态变化、重新评分）只更新原条目，不占新增名额。

## 3. 第一层：轻量分诊（triage）

只读缓存文件开头的元数据和摘要，必要时扫一眼 Introduction。每篇给出 `triage`：

| 决定 | 含义 |
|---|---|
| `include` | 进入第二层深评，可能收录 |
| `defer` | 材料不足以判断（如只有宣传页、HTML 不可用且摘要含糊）；记入 triage_log，后续可重新考虑 |
| `exclude` | 不在范围 / 重复 / 无可核查实质内容 / 增量过小；写一句 `reason` |

**范围**：通过「身体」感知并作用于物理世界的学习系统——VLA、world model（用于决策/控制/仿真）、操作、行走、遥操作与数据采集、sim-to-real、具身 3D 场景理解、导航、机器人 RL/IL，以及直接服务于这些方向的数据集、基准、仿真器、训练/评测基础设施和综述。
**不纳入**：纯 LLM/VLM、与具身无关的 CV/NLP、无学习成分的经典控制、纯硬件宣传、无论文/技术报告支撑的发布。

作者单位在此层只做背景记录（`affiliations` 按论文署名列全，不推断实习/合作关系）。没有开源代码**不是**自动排除理由。

## 4. 第二层：深入核验与评分

读缓存中的 Introduction、方法、实验、结论/局限及图表标题；关键结论必要时打开 arXiv 原文/附录、项目页和仓库。在 `evidence_read` 中如实记录读过的范围（`abstract / intro / method / experiments / appendix / project / code`）。**只读摘要不得打分**；`must-read` 必须读过实验部分（validate 强制）。

四个维度各打 1–5 分：总分 = 6·C + 5·E + 6·O + 3·T（即权重 30 / 25 / 30 / 15，满分 100）。每个维度写一句依据（`rationale`）。

| 分 | C 贡献重要性 (30%) | E 证据强度 (25%) | O 开放与可复现 (30%) | T 团队背景 (15%) |
|---|---|---|---|---|
| 5 | 新范式/基础模型/关键资源，相对已有工作增量大且清晰 | 多基准 + 强基线 + 消融 + 真机或大规模验证 + 泛化测试 | 实质代码 + 权重 + 数据，许可清晰，有复现说明 | 该方向公认领先团队，近 5 年有多项标志性成果/资源 |
| 4 | 明确的方法/资源增量，可能影响一个子方向 | 多基准或真机，基线和消融较完整 | 实质代码 + 权重或数据之一，许可清晰 | 有可核实的强相关积累 |
| 3 | 扎实但增量有限 | 单一基准或仅仿真，但对照合理 | 实质代码或明确的部分开放 | 有一定相关成果；**信息不足时默认 3 并在 pending_checks 注明** |
| 2 | 小改进 / 已有技术组合 | 实验薄弱、基线缺失或仅 demo | 仅占位仓库 / 只有项目页 / 声称将开源 | 相关积累有限 |
| 1 | 几乎无新意 | 几乎无定量证据 | 无任何开放资源 | — （不因无高校排名扣分；公司按其可核实的研究产出评估） |

- 不因不开源而否定研究价值，不因单位背景改变 E 分；贡献/证据判断与团队背景分开写。
- 论文自报结果写「作者报告」，不写成「证明」；不同基准、条件下的数字不横向比较。

**优先级（自动推导，不手填）**

| 优先级 | 条件 | README 标记 |
|---|---|---|
| `must-read` 重点阅读 | 总分 ≥ 80 且 E ≥ 3 | 🔥 |
| `notable` 值得关注 | 65–79 | 👀 |
| `watching` 观察中 | < 65（跟进优先级低，不代表工作不可信） | 无 |
| `unrated` 暂不评级 | 关键依据不足，未打分；在 `pending_checks` 写具体缺什么 | 无 |

经典奠基工作另以 `classic: true` 显示 📜。

## 5. 开放状态

`open.code` 由 `fetch_candidates.py` 用 `git clone --filter=blob:none` 探测初值，评审者可在核对仓库内容后修正并在 `open.note` 说明：

| 值 | 含义 |
|---|---|
| `no-repo` | 未找到官方仓库链接（或链接已失效） |
| `placeholder` | 有仓库但无实质相关代码（只有 README / 项目页 / "coming soon"） |
| `partial` | 部分开放（如仅推理代码、仅部分模块） |
| `substantive` | 已公开与论文方法/实验对应的实质代码 |

`weights` / `data` 取 `open / partial / gated / none / unknown / n/a`；`license` 写 SPDX 名或 `unknown`。官方 GitHub 链接本身不等于开源。

**复查节奏**（`recheck_open.py`，每周 CI 运行）：首次核查后 6 个月内每周一次，之后每月一次。代码状态变化时自动按档位差调整 O 分、重算总分与优先级，并在条目 `history` 留痕；历史 digest 不改写。

## 6. 单篇条目写法

- **`one_liner`**（README 展示，≤120 字中文）：一句话说清做了什么、关键结果。
- **`summary`**（约 300–400 字中文，digest 与索引展示）——最重要的字段，按因果链写：
  > 为解决/缓解 X，提出/构建 Y；在 Z 任务/基准/实验条件下作者报告 R。该结果提示……，但尚不能说明 / 仍受……限制。

  数据集/基准/工具写成「为弥补 X 缺口，发布 Y，包含/支持 Z；其覆盖范围或验证结果为……，局限是……」。不孤立罗列数字，交代基准、指标、对照和条件；引用后续版本结果要注明版本。
- **`category`**：`vla / world-model / foundation-general / manipulation / locomotion / teleoperation / sim2real / scene / navigation / rl-il / tutorials`（综述放 `tutorials`）。
- **`route`**：`core`＝主要贡献是具身模型/策略/方法本身；`adjacent`＝数据、基准、基础设施、安全/分析、硬件等支撑性工作。两类分开排序。
- **`contribution`**：`model / method / data / benchmark / infra / system / survey / hardware`。
- **`uses`**：论文明确写出的数据集/基准关系，`resource` 为 `data/{datasets,benchmarks,simulators,tools}.yaml` 中的 `id`，`role` ∈ `proposes / pretrain / finetune / eval`。只登记正文/实验设置中明确写出的关系；在某基准上测试不等于用其 demos 训练。资源尚未登记且值得跟踪时，写进 `new_resources`（需含 `kind / id / name / desc / links / subcategory`）。
- **`venue`**：只在 arXiv comment / journal ref / 官方录用页明确时填写；查不到写空，不推断。
- **`pending_checks`**：只列本次无法确认、值得补证的具体事实；已确认的不开源/局限不算待核验。
- **日期**：`date` 是首次公开（arXiv v1）日期，后续版本不改写它。

## 7. 质量自查（每轮结束前）

范围与时间边界写明；每篇结论能追溯到 `evidence_read`；summary 覆盖问题/方法/结果与条件/局限；开放状态有 `last_check`；无跨基准比较；`uses` 有依据；`python scripts/validate.py` 通过。
