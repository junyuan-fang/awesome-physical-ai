# Topics / 专题

纵向深挖某个方向、系列或机构，不受每日扫描篇幅限制。

与 `digests/` 的区别：digest 是**单轮扫描的时间快照**；专题是**跨多篇工作的持续整理**，随索引更新，不重写历史报告。

## 约定

- 一个专题一个文件，文件名用 kebab-case（如 `world-action-models.md`）。
- 数据仍以 `data/papers.yaml` 为准；专题页不维护独立评分，引用 [`docs/index.md`](../docs/index.md) 的当前值。
- 作者报告的数字标注「作者报告」，不跨基准比较；开放状态写 `last_check`。
- 新专题由维护者决定；每日 agent 不自动新建专题。
- 专题页可以引用尚未入库、但已评审的工作（注明「因轮次上限暂缓」）。

## 现有专题

| 专题 | 范围 | 状态 |
|---|---|---|
| [World-Action Models](world-action-models.md) | WAM 的边界、设计轴、代表系统、资源与开放问题 | 活跃 |
| [Ropedia W0](ropedia-w0.md) | 跨具身 loco-manipulation 世界模型、Xp-Data / Xp-Teleop | 活跃 |

## 候选专题（待建）

- **Egocentric human data → robot**：EgoXperience、λ0、ScaleNav、GRAIL、Ego2Robot。
- **Humanoid loco-manipulation**：Ropedia W0、λ0、Reflex、HumanoidToolBench。
- **VLA 效率与实时性**：Long-WAM、FlashVLA、TurboVLA、RIFT、VLA-Rolling。
- **世界模型即评测器**：WEAVER、OSCAR、PiL-World、PAWBench、KineBench。

## 怎么加

1. 在 `topics/` 新建 `<slug>.md`，按「问题 → 方法轴 → 代表工作表 → 资源/评测 → 开放问题 → 局限」组织。
2. 在 `topics/README.md` 的表格里加一行。
3. 在 `templates/README.md.j2` 的 Topics 小节加链接，然后 `python scripts/generate_readme.py`。
4. 提交时只改 `topics/`、`templates/README.md.j2`、`README.md`。
