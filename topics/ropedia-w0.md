# Ropedia W0 / 跨具身 loco-manipulation 世界模型专题

> 单篇纵向档案。评分与开放状态以 [`docs/index.md`](../docs/index.md) 和 [`data/papers.yaml`](../data/papers.yaml) 为准；文中数字均为**作者报告**。

## 1. 一句话

用「相机位姿 + 投影骨架」把人类与不同机器人本体统一到同一运动学条件接口，构建自我中心 loco-manipulation 世界模型 Ropedia W0，并用 1 万小时人类视频 + 3 千小时机器人数据训练。

## 2. 问题

现有世界模型多聚焦固定底座、夹爪操作，较少同时建模**移动引起的视角变化**与**灵巧操作**；跨本体时，动作空间维度与语义不一致，难以共享一个模型。人类自我中心视频数量大，但常缺度量相机轨迹、手部标注噪声大、格式异构。

## 3. 方法

- **统一运动学表示**：相机位姿编码移动（loco），投影骨架编码操作（manip）；机器人骨架 = 本体前向运动学 + 人工关键点标注/校正。
- **两阶段训练**：人类自我中心视频预训练（约 10k h）→ 人类/机器人等概率中训练（约 3k h）→ 蒸馏为 4 步生成器（LongLive / Causal Forcing）。
- **规模**：5B dense 与 A14B MoE（基于 Wan2.2-I2V-A14B，约 27B 总参数、14B 激活）。
- **条件注入**：相机 ray map 与骨架渲染在空间上对齐注入视频 token；手腕位姿与宽 FOV 骨架通过额外 cross-attention 分支。

## 4. 数据与基准

- **Xp-Data**：约 10k h 人类 + 3k h 机器人；14 个人类数据集 + 13 个机器人数据集 + 6,000+ h 自采四鱼眼视频；统一 RGB、相机轨迹、骨架与 caption。
- **Xp-Teleop**：27 段约 1 小时，Unitree G1 + 两副 6-DoF 灵巧手，543 个人工标注原子片段 / 30 类技能，含 RGB-D、位姿、骨架、机器人状态、语言、触觉与头显 IMU。
- **评测**：DreamDojo（GR-1 In-lab / EgoDex / DreamDojo-HV）、Ψ0、ω-HOME、Xp-Teleop、AgiBot；外加训练中未见过的 EgoSuite / OpenAoE 人类视频。

## 5. 作者报告的结果

- 五个跨具身基准上 PSNR/SSIM/LPIPS 与相机轨迹误差优于 DreamDojo、Cosmos3 等基线。
- 未见人类视频：ATE 1.542、PCK@0.1 81.3%。
- DreamDojo 1% 后训练即超过其 100% 基线；数据规模增加带来单调提升。
- 消融：去掉骨架条件 PSNR 降 3.8 / 1.8 dB（A14B / 5B）；去掉相机条件在移动视角降 1.3 dB。
- 蒸馏：4 步 5B 学生单卡 21.3 fps，支持分钟级 rollout。

## 6. 开放状态（2026-10-22 核验）

| 项 | 状态 |
|---|---|
| 代码 | 🟡 partial：5B 推理代码与 5B pre/mid-train 权重；训练/后训练代码、A14B、评测代码未发布 |
| 权重 | open：5B（CC BY-NC 4.0） |
| 数据 | partial：Xp-Teleop 已发布（CC BY 4.0）；Xp-Data 未发布 |
| 许可 | Apache-2.0（仓库）；权重 CC BY-NC 4.0 |
| 链接 | [project](https://ropedia.github.io/ropedia-w0/) · [code](https://github.com/Ropedia/ropedia-w0) · [arXiv](https://arxiv.org/abs/2610.26855) |

## 7. 局限与待核验

- 主指标是视频预测代理；真机闭环仅作应用演示，非受控对比。
- 骨架标注质量、跨本体几何一致性、长时程漂移仍需独立验证。
- **待核验**：Xp-Data 与后训练代码的发布时间；A14B 权重与基准微调 checkpoint。

## 8. 相关跟踪

- [EgoXperience](https://arxiv.org/abs/2610.26625)（68）——50 h 自我中心数据 EgoX-Data-6M + EgoX-Bench，单次前向联合重建相机、深度、双手与物体 6DoF。
- [λ0](https://arxiv.org/abs/2610.00438)（68）——500 h 第一视角全身数据 HumanVerse-500 三阶段预训练，人形全身 VLA。
- [ScaleNav](https://arxiv.org/abs/2610.25690)（86）——互联网自我中心视频预训练 + 动作对齐的导航 WAM。
- [GRAIL](https://arxiv.org/abs/2606.05160)（83）——3D 资产 + 视频先验生成人形 loco-manipulation 数据。
- [Ego2Robot](https://arxiv.org/abs/2608.02580)（数据集，截至 2026-10 未公开）——人手视频重定向到 15 种机械臂，18,561 h。
- Xp-Teleop（基准，本页与 README 数据集/基准区均有入口）。

## 9. 阅读路径

1. 先读本页 + [2026-10-22 日报](../digests/daily/2026-10-22.md) 的 Ropedia 条目。
2. 再看 arXiv 的 Data / Method / Experiments（重点看 Table 2–5 与消融）。
3. 最后核对 [project](https://ropedia.github.io/ropedia-w0/) / [repo](https://github.com/Ropedia/ropedia-w0) 的实际发布范围（推理 vs 训练）。
