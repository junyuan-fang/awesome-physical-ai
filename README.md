<div align="center">

# 🤖 Awesome Physical AI

**A continuously maintained, auto-updated list of Physical AI · Embodied AI · Humanoid Robotics — focused on 2025–2026+ state-of-the-art.**

*持续自动更新的具身智能 / 物理 AI / 人形机器人资源列表 · 论文描述中英双语，面向中文社区*

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Maintained](https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg)](https://github.com/junyuan-fang/awesome-physical-ai/commits/master)
![Last updated](https://img.shields.io/badge/Last%20updated-2026--10--23-blue.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

📊 **233** papers&nbsp; · &nbsp;🏢 **19** companies&nbsp; · &nbsp;🎮 **8** simulators&nbsp; · &nbsp;📦 **22** datasets&nbsp; · &nbsp;📊 **25** benchmarks

🔥 **37** must-read&nbsp; · &nbsp;👀 **67** notable&nbsp; · &nbsp;📋 **129** also tracked

<sub>🤖 Discovered daily from arXiv + HuggingFace daily papers, then screened & scored by a [two-layer review](docs/METHODOLOGY.md) · 每日从原始渠道发现，经两层筛选与四维评分后收录</sub>

</div>

> 💡 **Legend / 图例**: 🔥 must-read（总分 ≥80 且证据 ≥3）· 👀 notable（65–79）· 📜 classic landmark · `81/100` = 贡献 30% + 证据 25% + 开放 30% + 团队 15% · 💻 substantive code · 🟡 partial · 📄 placeholder repo · 🧩 adjacent（数据/基准/基础设施）· 🏛️ accepted venue · 📝 full review. Click any **▸ section** to expand / 点击展开折叠区.
>
> 📚 Full ranked index with affiliations & open status: [docs/index.md](docs/index.md) · Scan reports: [digests/](digests/) (latest: [2026-10-22](digests/daily/2026-10-22.md))
---

## ⭐ This week's picks / 本周精选

- 🔥 **[Long-WAM: Scaling the Context of World-Action Models](https://arxiv.org/abs/2610.10528)** — *Wei Huang et al.* · `2026-10-07` · `88/100`（C4·E5·O4·T5） · 💻
  > 自回归视频预训练 + 因果世界-动作模型：GR-1 上 19.2 s 上下文把成功率从 63.3% 提到 78.7%，RTX 5090 每动作块 107.4 ms。 · [🌐 project](https://nvlabs.github.io/LongLive/Long-WAM/) · [💻 code](https://github.com/NVlabs/LongLive) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](https://arxiv.org/abs/2610.26855)** — *Tianqi Liu et al.* · `2026-10-19` · `86/100`（C5·E4·O4·T4） · 🟡
  > Ropedia W0 用相机位姿+投影骨架统一人/机器人运动，建 1.3 万小时 Xp-Data 与 Xp-Teleop；作者报告在 DreamDojo、ω-HOME 等五个跨具身基准上视频预测领先。 · [🌐 project](https://ropedia.github.io/ropedia-w0/) · [💻 code](https://github.com/Ropedia/ropedia-w0) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation](https://arxiv.org/abs/2610.25690)** — *Yihui Yang et al.* · `2026-10-19` · `86/100`（C4·E4·O5·T4） · 💻
  > ScaleNav 用互联网自我中心视频做指令条件视频预训练再对齐动作；作者报告 Short-Horizon OVON 86.5%、HabitatGS-LN 94.9%，Go2 真机 83.3%。 · [🌐 project](https://zju3dv.github.io/ScaleNav/) · [💻 code](https://github.com/MachEmbodied/ScaleNav) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[LeWAM: End-to-End World and Action Modeling with JEPAs](https://arxiv.org/abs/2610.12818)** — *Minghao Fu et al.* · `2026-10-08` · `86/100`（C4·E4·O5·T4） · 💻
  > 首个端到端 JEPA：联合潜状态预测与动作 flow matching，在 10 个仿真任务上把接触密集/长程任务的规划成功率做到 89.7%/46.2%，规划快 32.3 倍。 · [🌐 project](https://le-wam.github.io/) · [💻 code](https://github.com/MinghaoFu/lewam) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[HumanoidToolBench: Benchmarking Humanoid Tool Use from Selection to Mobile Execution](https://arxiv.org/abs/2610.02089)** — *Kyochul Jang et al.* · `2026-10-01` · `86/100`（C4·E4·O5·T4） · 💻 · 🧩 *adjacent*
  > 发布 HumanoidToolBench：18 个人形工具使用任务（3 场景×3 执行层级×2 工具集模式）与 3.1k 条仿真/真机 G1 示教；7 个策略仿真、3 个真机评测，移动使用阶段成功率大幅下降。 · [🌐 project](https://snu-pi.github.io/HumanoidToolBench/) · [💻 code](https://github.com/SNU-PI/HumanoidToolBench) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[Breaking the Vision-Action Shortcut: Latent Interface Training for Generalizable Robotics Foundation Models](https://arxiv.org/abs/2609.12641)** — *Jianman Lin et al.* · `2026-09-11` · `86/100`（C4·E4·O5·T4） · 💻
  > 提出 Latent Interface Training 两阶段训练：先学无图像的空间目标动作先验，再经位姿监督潜接口注入视觉；4 个 VLA/WAM 架构上 LIBERO-Plus 总体提升 3.87–10.70 点。 · [🌐 project](https://magiclab-nus.github.io/LIT/?v=37955c5) · [💻 code](https://github.com/MAGICLAB-NUS/LIT) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining](https://arxiv.org/abs/2609.07398)** — *Yuran Wang et al.* · `2026-09-07` · `86/100`（C5·E4·O4·T4） · 💻
  > OpenWAM 把世界-动作模型拆成可组合模块并系统消融，用 6,369 小时数据训练 OpenWAM-α；作者报告 LIBERO 99.3%、EBench 49.4、真机 RoboDojo 24.4% 成功率。 · [🌐 project](https://openwam-official.github.io/) · [💻 code](https://github.com/OpenWAM-Official/OpenWAM) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[Has GPT-6-Astra Achieved Embodied Intelligence?](https://arxiv.org/abs/2610.22471)** — *SenseNova et al.* · `2026-10-15` · `85/100`（C4·E5·O4·T4） · 💻 · 🧩 *adjacent*
  > 该报告在 12 个基准上用 ICL+扩展步数协议评测 GPT-6-Astra，并在 8 类真机平台验证；作者报告 LIBERO-Ultra-Long 98.8%、RoboDojo 81.9%，但成本与实体验证仍是瓶颈。 · [🌐 project](https://sensenova.ai/has-gpt-6-astra-achieved-embodied-intelligence) · [💻 code](https://github.com/OpenSenseNova/SenseNova-RoboRSI) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[Reflex: Visually Grounded Reactive Humanoid Control](https://arxiv.org/abs/2610.12772)** — *Taoyang Jia et al.* · `2026-10-08` · `80/100`（C4·E4·O4·T4） · 💻
  > 三阶段训练的人形全身接箱框架：仿真第一视角 RGB-D 抓接成功率 85.7%，Unitree G1 真机 2.5 m/5 m 处达 65%/40%。 · [🌐 project](https://toberj.github.io/reflex/) · [💻 code](https://github.com/ToberJ/reflex) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)** — *Qize Yu et al.* · `2026-09-30` · `80/100`（C4·E4·O4·T4） · 💻
  > GroundingPI 是 4B 接地基础模型，34 个基准平均 73.68%；作为 VLA 视觉骨干，作者报告 RoboTwin 2.0 四个 OOD 设置全胜、RoboCasa-GR1 用 50% 演示超过基线 75%。 · [🌐 project](https://groundingpi.github.io/) · [💻 code](https://github.com/groundingpi/GroundingPI) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[Grounded Action Model: 3D Grounding as a Foundation for Robotics](https://arxiv.org/abs/2609.23863)** — *Gehao Zhang et al.* · `2026-09-20` · `80/100`（C4·E4·O4·T4） · 💻
  > GAM 以可提示 3D 接地模型为骨干、只用任务物体构建观测；作者报告 RoboTwin 2.0 平均 55.3%、LIBERO-PRO 61%，真机视觉偏移下 17/20 对 π0.5 的 4/20。 · [🌐 project](https://grounded-action-model.github.io/) · [💻 code](https://github.com/GehaoZhang6/Grounded-Action-Model) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[RoboTok: A Scalable Data Engine for Internet Demonstration Video Retrieval and Dexterous Manipulation Learning](https://arxiv.org/abs/2609.03199)** — *Howard Qian et al.* · `2026-09-02` · `80/100`（C4·E4·O4·T4） · 💻 · 🧩 *adjacent*
  > RoboTok 以躯干中心 3D 手轨迹学习运动嵌入，从网络视频检索演示；作者报告真机灵巧操作平均成功率比最强基线高 42.2 个百分点。 · [🌐 project](https://rice-robotpi-lab.github.io/RoboTok/) · [💻 code](https://github.com/Rice-RobotPI-Lab/RoboTok-Code) · [📝 review](digests/daily/2026-10-22.md)

- 👀 **[GreenWAM: A World Foundation Model for Robotics](https://arxiv.org/abs/2610.18774)** — *Gennady Sidorov et al.* · `2026-10-13` · `77/100`（C4·E4·O4·T3） · 🟡
  > GreenWAM 以 79 维解剖动作空间统一 20 类双臂机器人，世界模型与策略共用一套权重；作者报告 RoboTwin 2.0 平均 67.54%、人形真机 ID 95.6%。 · [🌐 project](https://greenvla.github.io/GreenWAM/) · [💻 code](https://github.com/greenvla/GreenWAM) · [📝 review](digests/daily/2026-10-22.md)

- 👀 **[VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models](https://arxiv.org/abs/2610.21306)** — *Qi Lu et al.* · `2026-10-15` · `71/100`（C3·E4·O4·T3） · 💻
  > VLA-Δ 在预训练中用未来状态差文本、结构化转移槽与光流显式监督物理状态变化；作者报告 LIBERO 98.4%、RoboTwin 2.0 平均 90.06%，真机 68.0%。 · [🌐 project](https://zju-omniai.github.io/VLA-Delta/) · [💻 code](https://github.com/ZJU-OmniAI/VLA-Delta) · [📝 review](digests/daily/2026-10-22.md)

- 👀 **[MotorMind: Scaffolding General Vision Language Models for Zero-Shot Robot Manipulation](https://arxiv.org/abs/2609.38078)** — *Bingxuan Li et al.* · `2026-09-29` · `71/100`（C4·E4·O3·T3） · 💻
  > MotorMind 让冻结通用 VLM 经中层级动作与异步监控直接控制机器人；作者报告 LIBERO-PRO 基础 66.7%、扰动 53.8%，真机 xArm6 平均 95%。 · [🌐 project](https://motor-mind.github.io) · [💻 code](https://github.com/Motor-Mind/MotorMind-Code) · [📝 review](digests/daily/2026-10-22.md)


---

## 🏆 Top-20 / 总榜

当前评分前 20（优先级 → 总分 → 首次公开日期），括号内为 `C/E/O/T` 分数构成；完整索引见 [docs/index.md](docs/index.md)。

1. 📜 **[OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)** — *Kim et al.* · `2024-06-13` · `100/100`（C5·E5·O5·T5） · 💻
  > 基于 Llama 2 + DINOv2/SigLIP 的 7B 开源 VLA，用 97 万条 OXE 示范训练；作者报告 29 项真机任务上比 RT-2-X 高 16.5 个百分点，支持 LoRA 与量化。 · [🌐 project](https://openvla.github.io) · [💻 code](https://github.com/openvla/openvla) · [📝 review](digests/migration-2026-10-22.md)

2. 📜 **[Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137)** — *Chi et al.* · `2023-03-07` · 🏛️ **RSS 2023** · `100/100`（C5·E5·O5·T5） · 💻
  > 把视觉运动策略表示为动作空间的条件去噪扩散过程，配合滚动时域控制与时序扩散 Transformer；作者报告在 4 个基准 15 项任务上平均提升 46.9%。 · [🌐 project](https://diffusion-policy.cs.columbia.edu) · [💻 code](https://github.com/real-stanford/diffusion_policy) · [📝 review](digests/migration-2026-10-22.md)

3. 📜 **[GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)** — *NVIDIA* · `2025-03-18` · `95/100`（C5·E4·O5·T5） · 💻
  > NVIDIA 开放的人形通用 VLA：System 2 VLM + System 1 DiT flow-matching 双系统，用真机、仿真、神经生成轨迹与人类视频「数据金字塔」训练；作者报告在三套仿真基准与 GR-1 真机上优于基线。 · [🌐 project](https://developer.nvidia.com/isaac/gr00t) · [💻 code](https://github.com/NVIDIA/Isaac-GR00T) · [📝 review](digests/migration-2026-10-22.md)

4. 📜 **[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2308.04079)** — *Kerbl et al.* · `2023-08-08` · 🏛️ **ACM TOG 2023** · `94/100`（C5·E5·O4·T5） · 💻 · 🧩 *adjacent*
  > 以可优化的各向异性 3D 高斯表示场景并配合可微分块光栅化，在 1080p 下实现 ≥30fps 实时新视角合成，作者报告画质与 Mip-NeRF360 相当且训练更快。 · [🌐 project](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) · [💻 code](https://github.com/graphdeco-inria/gaussian-splatting) · [📝 review](digests/migration-2026-10-22.md)

5. 📜 **[Cosmos World Foundation Model Platform for Physical AI](https://arxiv.org/abs/2501.03575)** — *NVIDIA* · `2025-01-07` · `89/100`（C5·E4·O4·T5） · 💻
  > NVIDIA 开放的世界基础模型平台：视频数据筛选管线、因果视频 tokenizer、扩散与自回归预训练 WFM 及后训练示例，权重以宽松许可发布。 · [🌐 project](https://www.nvidia.com/en-us/ai/cosmos/) · [💻 code](https://github.com/nvidia-cosmos/cosmos-predict1) · [📝 review](digests/migration-2026-10-22.md)

6. 🔥 **[Long-WAM: Scaling the Context of World-Action Models](https://arxiv.org/abs/2610.10528)** — *Wei Huang et al.* · `2026-10-07` · `88/100`（C4·E5·O4·T5） · 💻
  > 自回归视频预训练 + 因果世界-动作模型：GR-1 上 19.2 s 上下文把成功率从 63.3% 提到 78.7%，RTX 5090 每动作块 107.4 ms。 · [🌐 project](https://nvlabs.github.io/LongLive/Long-WAM/) · [💻 code](https://github.com/NVlabs/LongLive) · [📝 review](digests/daily/2026-10-22.md)

7. 🔥 **[Flex-$\pi$: A Multi-Stream World-Action Model with Compute Flexibility](https://arxiv.org/abs/2608.10860)** — *Yan, Ge et al.* · `2026-08-11` · `88/100`（C4·E5·O4·T5） · 💻
  > Flex-π 用冻结的 Wan VAE 同时编码 RGB 与 3D 点图，加上 DINO 语义，与动作联合去噪，单个 checkpoint 支持从纯动作到全联合生成；作者报告在真机双臂灵巧任务上比最强基线高 2–7 倍。 · [💻 code](https://github.com/geyan21/flex-pi) · [📝 review](digests/migration-2026-10-22.md)

8. 🔥 **[Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](https://arxiv.org/abs/2610.26855)** — *Tianqi Liu et al.* · `2026-10-19` · `86/100`（C5·E4·O4·T4） · 🟡
  > Ropedia W0 用相机位姿+投影骨架统一人/机器人运动，建 1.3 万小时 Xp-Data 与 Xp-Teleop；作者报告在 DreamDojo、ω-HOME 等五个跨具身基准上视频预测领先。 · [🌐 project](https://ropedia.github.io/ropedia-w0/) · [💻 code](https://github.com/Ropedia/ropedia-w0) · [📝 review](digests/daily/2026-10-22.md)

9. 🔥 **[ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation](https://arxiv.org/abs/2610.25690)** — *Yihui Yang et al.* · `2026-10-19` · `86/100`（C4·E4·O5·T4） · 💻
  > ScaleNav 用互联网自我中心视频做指令条件视频预训练再对齐动作；作者报告 Short-Horizon OVON 86.5%、HabitatGS-LN 94.9%，Go2 真机 83.3%。 · [🌐 project](https://zju3dv.github.io/ScaleNav/) · [💻 code](https://github.com/MachEmbodied/ScaleNav) · [📝 review](digests/daily/2026-10-22.md)

10. 🔥 **[LeWAM: End-to-End World and Action Modeling with JEPAs](https://arxiv.org/abs/2610.12818)** — *Minghao Fu et al.* · `2026-10-08` · `86/100`（C4·E4·O5·T4） · 💻
  > 首个端到端 JEPA：联合潜状态预测与动作 flow matching，在 10 个仿真任务上把接触密集/长程任务的规划成功率做到 89.7%/46.2%，规划快 32.3 倍。 · [🌐 project](https://le-wam.github.io/) · [💻 code](https://github.com/MinghaoFu/lewam) · [📝 review](digests/daily/2026-10-22.md)

11. 🔥 **[HumanoidToolBench: Benchmarking Humanoid Tool Use from Selection to Mobile Execution](https://arxiv.org/abs/2610.02089)** — *Kyochul Jang et al.* · `2026-10-01` · `86/100`（C4·E4·O5·T4） · 💻 · 🧩 *adjacent*
  > 发布 HumanoidToolBench：18 个人形工具使用任务（3 场景×3 执行层级×2 工具集模式）与 3.1k 条仿真/真机 G1 示教；7 个策略仿真、3 个真机评测，移动使用阶段成功率大幅下降。 · [🌐 project](https://snu-pi.github.io/HumanoidToolBench/) · [💻 code](https://github.com/SNU-PI/HumanoidToolBench) · [📝 review](digests/daily/2026-10-22.md)

12. 🔥 **[Breaking the Vision-Action Shortcut: Latent Interface Training for Generalizable Robotics Foundation Models](https://arxiv.org/abs/2609.12641)** — *Jianman Lin et al.* · `2026-09-11` · `86/100`（C4·E4·O5·T4） · 💻
  > 提出 Latent Interface Training 两阶段训练：先学无图像的空间目标动作先验，再经位姿监督潜接口注入视觉；4 个 VLA/WAM 架构上 LIBERO-Plus 总体提升 3.87–10.70 点。 · [🌐 project](https://magiclab-nus.github.io/LIT/?v=37955c5) · [💻 code](https://github.com/MAGICLAB-NUS/LIT) · [📝 review](digests/daily/2026-10-22.md)

13. 🔥 **[OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining](https://arxiv.org/abs/2609.07398)** — *Yuran Wang et al.* · `2026-09-07` · `86/100`（C5·E4·O4·T4） · 💻
  > OpenWAM 把世界-动作模型拆成可组合模块并系统消融，用 6,369 小时数据训练 OpenWAM-α；作者报告 LIBERO 99.3%、EBench 49.4、真机 RoboDojo 24.4% 成功率。 · [🌐 project](https://openwam-official.github.io/) · [💻 code](https://github.com/OpenWAM-Official/OpenWAM) · [📝 review](digests/daily/2026-10-22.md)

14. 📜 **[RDT-1B: A Diffusion Foundation Model for Bimanual Manipulation](https://arxiv.org/abs/2410.07864)** — *Liu et al.* · `2024-10-10` · `86/100`（C4·E4·O5·T4） · 💻
  > 1.2B 参数扩散 Transformer 双臂操作基础模型，用物理可解释的统一动作空间在多机器人数据上预训练；作者报告在 ALOHA 真机上零样本泛化与 1–5 次示范学新技能均优于 ACT、OpenVLA、Octo。 · [🌐 project](https://rdt-robotics.github.io/rdt-robotics/) · [💻 code](https://github.com/thu-ml/RoboticsDiffusionTransformer) · [📝 review](digests/migration-2026-10-22.md)

15. 🔥 **[Has GPT-6-Astra Achieved Embodied Intelligence?](https://arxiv.org/abs/2610.22471)** — *SenseNova et al.* · `2026-10-15` · `85/100`（C4·E5·O4·T4） · 💻 · 🧩 *adjacent*
  > 该报告在 12 个基准上用 ICL+扩展步数协议评测 GPT-6-Astra，并在 8 类真机平台验证；作者报告 LIBERO-Ultra-Long 98.8%、RoboDojo 81.9%，但成本与实体验证仍是瓶颈。 · [🌐 project](https://sensenova.ai/has-gpt-6-astra-achieved-embodied-intelligence) · [💻 code](https://github.com/OpenSenseNova/SenseNova-RoboRSI) · [📝 review](digests/daily/2026-10-22.md)

16. 🔥 **[CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators](https://arxiv.org/abs/2608.27406)** — *Liu, Kechen et al.* · `2026-08-27` · `83/100`（C4·E4·O5·T3） · 💻
  > CLAP 用末端位姿、语言与潜动作统一异构动作空间并以课程式训练跨具身视频世界模型，作者报告在 DROID 上接近或超过单具身 Ctrl-World，并可零样本用于多策略规划。 · [💻 code](https://github.com/omni-CLAP/clap) · [📝 review](digests/migration-2026-10-22.md)

17. 🔥 **[Geometric Action Model for Robot Policy Learning](https://arxiv.org/abs/2606.17046)** — *Han, Jisang et al.* · `2026-06-15` · `83/100`（C4·E4·O4·T5） · 💻
  > 把几何基础模型 DA3 在中间层切开插入因果预测器，同时解码未来深度与动作；作者报告 1.4B 模型 LIBERO-Plus 85.5%、单步 6.9 ms，真机换视角更稳健。 · [🌐 project](https://cvlab-kaist.github.io/Geometric-Action-Model/) · [💻 code](https://github.com/cvlab-kaist/Geometric-Action-Model) · [📝 review](digests/migration-2026-10-22.md)

18. 🔥 **[World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis](https://arxiv.org/abs/2606.05979)** — *Yang, Yi et al.* · `2026-06-04` · `83/100`（C4·E4·O5·T3） · 💻
  > 提出世界-语言-动作模型 WLA：自回归 VLM 骨干同时预测文本子任务与经 World Expert 监督的物理动态，推理可关闭世界分支；WLA-0（2B 激活）作者报告 RoboTwin2.0 Clean 92.94%、RMBench 56.5%、单次推理 40 ms。 · [💻 code](https://github.com/SJTU-DENG-Lab/WLA) · [📝 review](digests/migration-2026-10-22.md)

19. 🔥 **[GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](https://arxiv.org/abs/2606.05160)** — *Xie, Tianyi et al.* · `2026-06-03` · `83/100`（C4·E4·O4·T5） · 💻 · 🧩 *adjacent*
  > 在已知几何与尺度的 3D 场景中用视频基础模型生成人-物交互、再做度量 4D 重建并重定向到人形的全虚拟数据流水线 GRAIL；生成 2 万+序列，仅用其数据训练的 G1 真机拾取 84%、爬楼 90%。 · [🌐 project](https://research.nvidia.com/labs/dair/grail/) · [💻 code](https://github.com/NVlabs/GRAIL) · [📝 review](digests/migration-2026-10-22.md)

20. 📜 **[Mobile ALOHA: Learning Bimanual Mobile Manipulation](https://arxiv.org/abs/2401.02117)** — *Fu et al.* · `2024-01-04` · `83/100`（C4·E4·O4·T5） · 💻 · 🧩 *adjacent*
  > 低成本（<3.2 万美元）全身遥操作双臂移动操作平台，并与静态 ALOHA 数据协同训练；作者报告每任务 50 条示范时协同训练可将成功率最多提升 90 个百分点。 · [🌐 project](https://mobile-aloha.github.io) · [💻 code](https://github.com/MarkFzp/mobile-aloha) · [📝 review](digests/migration-2026-10-22.md)


---

## 🌐 What is Physical AI?

**Physical AI** is AI that perceives, reasons about, and acts in the *physical* world through a body — robots, humanoids, manipulators. Unlike chatbots that output text, these systems output **actions** and must obey physics, contact, and real-time constraints.

> **物理 AI / 具身智能**：让 AI 通过「身体」（机器人 / 人形 / 机械臂）感知、推理并作用于真实物理世界。区别于只输出文本的对话模型，它输出的是**动作**，必须遵守物理、接触和实时性约束。

This list covers the full stack: **foundation models** (VLA, world models) → **policies** (manipulation, locomotion, navigation) → **data** (teleoperation, datasets) → **infrastructure** (simulators, benchmarks, sim-to-real) → **industry** (humanoid companies). It does **not** cover pure LLMs, classical control without learning, or non-embodied CV/NLP.

---

## 🚀 Where to Start

New to the field? Pick a track by your background / 新手按背景选择起点：

| Your background / 你的背景 | Suggested reading path / 推荐路线 |
|---|---|
| 🧠 **ML / LLM** | [Foundation Models](#foundation-models) → [RL & Imitation Learning](#rl-il) |
| 🦾 **Manipulation** | [Manipulation](#manipulation) → [Teleoperation](#teleoperation) → [Datasets](#datasets) |
| 🌉 **Sim-to-real** | [Simulators](#simulators) → [Sim-to-Real](#sim2real) → [Benchmarks](#benchmarks) |
| 🦿 **Humanoids / locomotion** | [Locomotion](#locomotion) → [Companies & Industry](#companies) |
| 📈 **Industry tracking** | [Companies & Industry](#companies) — valuation tracker + US / CN / EU players |

---

## 📐 How we score / 打分标准

每篇按四个维度各打 1–5 分，总分 = **6×C + 5×E + 6×O + 3×T**（满分 100）。分数构成会直接显示在每条论文后面，例如 `86/100（C5·E4·O4·T4）`。

- **C 贡献重要性（30%）** — 新范式 / 基础模型 / 关键资源的增量大小。
- **E 证据强度（25%）** — 多基准、强基线、消融、真机或大规模验证。
- **O 开放与可复现（30%）** — 代码 / 权重 / 数据 / 许可在**当前**是否真的开放。
- **T 团队背景（15%）** — 可核实的相关积累；信息不足默认 3，不因没有高校排名扣分。

**优先级**：🔥 总分 ≥80 且 E≥3 · 👀 65–79 · 观察中 <65 · 暂不评级（关键依据不足）。完整评分锚点与复查规则见 [docs/METHODOLOGY.md](docs/METHODOLOGY.md)。

---

## Contents

- **📚 Research** — [🤖 Foundation Models for Robotics](#foundation-models) · [🦾 Manipulation](#manipulation) · [🦿 Locomotion](#locomotion) · [🕹️ Teleoperation](#teleoperation) · [🌉 Sim-to-Real](#sim2real) · [🌍 3D Scene Understanding](#scene) · [🧭 Navigation & Mobility](#navigation) · [🎯 RL & Imitation Learning](#rl-il)
- **🧰 Resources** — [📦 Datasets](#datasets) · [🎮 Simulators](#simulators) · [📊 Benchmarks](#benchmarks) · [🛠️ Tools & Libraries](#tools) · [📚 Tutorials & Surveys](#tutorials)
- **🏢 Industry** — [🏢 Companies & Industry](#companies)
- **🧭 Topics** — [World-Action Models](topics/world-action-models.md) · [Ropedia W0](topics/ropedia-w0.md)


---

## 🧭 Topics / 专题

纵向深挖某个方向或系列，不受每日扫描篇幅限制；数据仍以 `data/papers.yaml` 为准，评分与开放状态随索引更新。

- **[World-Action Models](topics/world-action-models.md)** — 统一分类、已跟踪 WAM 系统、评测与开放问题
- **[Ropedia W0](topics/ropedia-w0.md)** — 跨具身 loco-manipulation 世界模型与 Xp-Data / Xp-Teleop

---

## <a id="foundation-models"></a>🤖 Foundation Models for Robotics

*Generalist policies, VLA, world models*

### Vision-Language-Action (VLA) · 67

<details open>
<summary>🔥 <b>Must-read & notable / 重点与值得关注</b> · 29 papers</summary>

- 🔥 **[Breaking the Vision-Action Shortcut: Latent Interface Training for Generalizable Robotics Foundation Models](https://arxiv.org/abs/2609.12641)** — *Jianman Lin et al.* · `2026-09-11` · `86/100`（C4·E4·O5·T4） · 💻
  > 提出 Latent Interface Training 两阶段训练：先学无图像的空间目标动作先验，再经位姿监督潜接口注入视觉；4 个 VLA/WAM 架构上 LIBERO-Plus 总体提升 3.87–10.70 点。 · [🌐 project](https://magiclab-nus.github.io/LIT/?v=37955c5) · [💻 code](https://github.com/MAGICLAB-NUS/LIT) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[Has GPT-6-Astra Achieved Embodied Intelligence?](https://arxiv.org/abs/2610.22471)** — *SenseNova et al.* · `2026-10-15` · `85/100`（C4·E5·O4·T4） · 💻 · 🧩 *adjacent*
  > 该报告在 12 个基准上用 ICL+扩展步数协议评测 GPT-6-Astra，并在 8 类真机平台验证；作者报告 LIBERO-Ultra-Long 98.8%、RoboDojo 81.9%，但成本与实体验证仍是瓶颈。 · [🌐 project](https://sensenova.ai/has-gpt-6-astra-achieved-embodied-intelligence) · [💻 code](https://github.com/OpenSenseNova/SenseNova-RoboRSI) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[Geometric Action Model for Robot Policy Learning](https://arxiv.org/abs/2606.17046)** — *Han, Jisang et al.* · `2026-06-15` · `83/100`（C4·E4·O4·T5） · 💻
  > 把几何基础模型 DA3 在中间层切开插入因果预测器，同时解码未来深度与动作；作者报告 1.4B 模型 LIBERO-Plus 85.5%、单步 6.9 ms，真机换视角更稳健。 · [🌐 project](https://cvlab-kaist.github.io/Geometric-Action-Model/) · [💻 code](https://github.com/cvlab-kaist/Geometric-Action-Model) · [📝 review](digests/migration-2026-10-22.md)

- 🔥 **[World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis](https://arxiv.org/abs/2606.05979)** — *Yang, Yi et al.* · `2026-06-04` · `83/100`（C4·E4·O5·T3） · 💻
  > 提出世界-语言-动作模型 WLA：自回归 VLM 骨干同时预测文本子任务与经 World Expert 监督的物理动态，推理可关闭世界分支；WLA-0（2B 激活）作者报告 RoboTwin2.0 Clean 92.94%、RMBench 56.5%、单次推理 40 ms。 · [💻 code](https://github.com/SJTU-DENG-Lab/WLA) · [📝 review](digests/migration-2026-10-22.md)

- 🔥 **[FlashVLA: Streaming Action Decoding for Fast and Asynchronous VLA Inference](https://arxiv.org/abs/2608.27384)** — *Li, Zekai et al.* · `2026-08-27` · `80/100`（C4·E4·O4·T4） · 💻
  > FlashVLA 让多个动作块以错开的噪声水平在流式缓冲区中联合去噪，每步产出一个可执行块，作者报告 LIBERO 上异步执行 2.43 倍提速且成功率升至 97.8%，真机 30 Hz 控制。 · [💻 code](https://github.com/z-lab/flashvla) · [📝 review](digests/migration-2026-10-22.md)

- 🔥 **[$\tau_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation](https://arxiv.org/abs/2608.16885)** — *Cai, Xiaowei et al.* · `2026-08-17` · `80/100`（C4·E4·O4·T4） · 💻
  > τ0-VLA 用 40,115 小时真机数据训练分层机器人基础模型，高层以世界模型预测子任务结果并做束搜索；作者报告真机长程任务平均成功率 45%（π0.5 为 22.5%），测试时计算进一步提升，代码与权重已开源。 · [🌐 project](https://tau0-vla.github.io/) · [💻 code](https://github.com/sii-research/tau-0-vla) · [📝 review](digests/migration-2026-10-22.md)

- 🔥 **[TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM](https://arxiv.org/abs/2607.27205)** — *Xie, Hengyi et al.* · `2026-07-29` · `80/100`（C4·E4·O4·T4） · 💻
  > 去掉 LLM 主干、以 BERT 文本编码与双向视觉-语言交叉注意力直接映射到动作块的紧凑 VLA；作者报告 0.2B 参数在 LIBERO 平均 97.6%、RTX 4090 上 31.2 ms 与 0.9 GiB 显存，0.4B 版 RoboTwin 2.0 达 88.06%。 · [🌐 project](https://huggingface.co/papers/2607.27180) · [💻 code](https://github.com/H-EmbodVis/TurboVLA) · [📝 review](digests/migration-2026-10-22.md)

- 🔥 **[Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories](https://arxiv.org/abs/2607.15330)** — *Xiaomi Robotics Team et al.* · `2026-07-16` · `80/100`（C4·E4·O4·T4） · 💻
  > 小米以 10 万+小时 UMI 真实轨迹（VLM 自动标注状态转移）预训练 2.6B–10.5B VLA，再用约 1 万小时跨本体数据后训练；作者报告 RoboCasa365 成功率 57.4%（此前最佳 46.6%）。 · [🌐 project](https://arxiv.org/abs/2607.15330) · [💻 code](https://github.com/XiaomiRobotics/Xiaomi-Robotics-1) · [📝 review](digests/migration-2026-10-22.md)

- 🔥 **[Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization](https://arxiv.org/abs/2601.12993)** — *Luo, Hao et al.* · `2026-01-19` · `80/100`（C4·E4·O4·T4） · 💻
  > 以人类交互轨迹为「母语」的跨本体 VLA：3.5 万小时 UniHand-2.0 语料、30 种本体统一动作空间；作者报告 LIBERO 98.9%、RoboCasa 53.9%，单一检查点控制 5 种真机。 · [🌐 project](https://research.beingbeyond.com/being-h05) · [💻 code](https://github.com/BeingBeyond/Being-H) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[$N_0$-VTLA: Scaling Vision-Tactile-Language-Action Model with Latent Tactile Tokens](https://arxiv.org/abs/2607.23782)** — *NeoteAI Team et al.* · `2026-07-26` · `77/100`（C4·E4·O4·T3） · 💻
  > 在大规模视触觉数据上预训练的视觉-触觉-语言-动作模型，以预测的潜触觉 token 条件动作专家，并用 ALTER 离线 RL 从部署数据改进；作者报告 9 个真机任务全胜、20 任务仿真平均 63.8%（最强基线 44.0%）。 · [🌐 project](https://arxiv.org/abs/2607.23782) · [💻 code](https://github.com/neoteai/N0-VTLA) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[GigaBrain-0.7: Scaling Embodied Foundation Models to Emergent Capabilities with a Three-System Architecture](https://arxiv.org/abs/2608.15875)** — *GigaBrain Team et al.* · `2026-08-16` · `75/100`（C4·E3·O4·T4） · 💻
  > GigaBrain-0.7 以理解规划、预测评估（世界价值模型）、动作控制三系统架构，在 3.7 万小时异构具身数据上单阶段预训练；作者报告零样本、语言跟随和后训练成功率均优于 GigaBrain-0 与 π0.5，并开放 3.5B 权重。 · [🌐 project](https://tau0-vla.github.io/) · [💻 code](https://github.com/open-gigaai/giga-brain-0) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[XPolicyLab: A Unified Standard and Open Ecosystem for Robot Policy Evaluation and Deployment](https://arxiv.org/abs/2608.09892)** — *Community, XPolicyLab et al.* · `2026-08-10` · `75/100`（C4·E3·O4·T4） · 💻 · 🧩 *adjacent*
  > XPolicyLab 用统一观测/动作 schema 和依赖隔离的 client/server 服务接入 42 个机器人策略，同一套 adapter 可以在 RoboTwin、RoboDojo 仿真和真机评测中复用。 · [💻 code](https://github.com/XPolicyLab/XPolicyLab) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[From Foundation to Application: Improving VLA Models in Practice](https://arxiv.org/abs/2607.06403)** — *Wu, Wei et al.* · `2026-07-07` · `75/100`（C4·E3·O4·T4） · 💻
  > LingBot-VLA 2.0 用约 6 万小时数据（5 万小时 20 种机器人轨迹+1 万小时人类第一视角视频）预训练，加入动作专家 MoE 与深度/视频双教师未来预测蒸馏；作者报告 GM-100 通才设置下优于 1.0 版。 · [🌐 project](https://technology.robbyant.com/lingbot-vla-v2) · [💻 code](https://github.com/robbyant/lingbot-vla-v2) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation](https://arxiv.org/abs/2608.09771)** — *Wang, Jingkai et al.* · `2026-08-10` · `74/100`（C3·E4·O4·T4） · 💻
  > 0.5B 紧凑策略 SLIM 用掩码轨迹预测学习动作锚定的观测隐变量，作者报告 LIBERO 97.5%、LIBERO-Plus 零样本 77.45%、CALVIN 平均长度 4.556，并做了真机验证。 · [🌐 project](https://kzz1031.github.io/slim-project-page/) · [💻 code](https://github.com/kzz1031/SLIM) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[LARA: Latent Action Representation Alignment for Vision-Language-Action Models](https://arxiv.org/abs/2606.07100)** — *Liu, Mengya et al.* · `2026-06-05` · `74/100`（C4·E4·O3·T4） · 💻
  > 以 REPA 式表征对齐联合训练潜动作模型与扩散 VLA，可用于预训练、后训练增强与潜动作精炼；作者报告 OXE 约束下 LIBERO 88.6%，G1 真机少样本适配平均提升约 32%。 · [💻 code](https://github.com/lmy1001/LARA) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding](https://arxiv.org/abs/2606.06155)** — *Yu, Qize et al.* · `2026-06-04` · `74/100`（C4·E4·O3·T4） · 💻
  > 在 MoT 架构中加入 Which2Act/Where2Act/How2Act 结构化可供性预测作为中间监督，用 8.8M 定位/指点样本三阶段训练；作者报告 LIBERO 平均 95.8%，真机复杂任务 82.9% 对 π0 44.8%。 · [🌐 project](https://skywalker-yqz.github.io/AffordanceVLA/) · [💻 code](https://github.com/Skywalker-yqz/AffordanceVLA) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation](https://arxiv.org/abs/2604.07993)** — *Bai, Shuanghao et al.* · `2026-04-09` · `74/100`（C4·E4·O3·T4） · 💻
  > 面向全尺寸双足人形的全身操作 VLA：人形对齐的统一状态表示 + MoE 本体感知预测器 + 历史 token；作者报告在天工 2.0/3.0 真机 7 项任务上优于 π0、GR00T N1.5 等基线。 · [💻 code](https://github.com/Open-X-Humanoid/HEX) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models](https://arxiv.org/abs/2610.21306)** — *Qi Lu et al.* · `2026-10-15` · `71/100`（C3·E4·O4·T3） · 💻
  > VLA-Δ 在预训练中用未来状态差文本、结构化转移槽与光流显式监督物理状态变化；作者报告 LIBERO 98.4%、RoboTwin 2.0 平均 90.06%，真机 68.0%。 · [🌐 project](https://zju-omniai.github.io/VLA-Delta/) · [💻 code](https://github.com/ZJU-OmniAI/VLA-Delta) · [📝 review](digests/daily/2026-10-22.md)

- 👀 **[What Matters for Latent Actions in Robot Learning](https://arxiv.org/abs/2608.19613)** — *Bu, Xizhou et al.* · `2026-08-20` · `71/100`（C3·E4·O4·T3） · 💻 · 🧩 *adjacent*
  > 在统一框架下系统比较41种潜动作模型设计（建模范式、正则、集成方式），结论包括LAPO仍是强基线、正则强度比类型更关键，潜动作微调VLM可改善下游策略。 · [🌐 project](https://carldegio.github.io/latent_action.github.io) · [💻 code](https://github.com/XizoB/What-Matters-for-Latent-Actions-in-Robot-Learning) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[World Tokens: Enhancing Embodied Policies with Training-Time World Modeling](https://arxiv.org/abs/2608.09730)** — *Tang, Qu et al.* · `2026-08-10` · `71/100`（C3·E4·O4·T3） · 💻
  > world tokens 同时条件化训练期视频去噪器并作为动作专家唯一上下文，部署时移除视频分支；作者报告 LIBERO 98.2%、SIMPLER WidowX 71.5%，延迟约 62 ms。 · [🌐 project](https://kzz1031.github.io/slim-project-page/) · [💻 code](https://github.com/kzz1031/SLIM) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[T-Rex: Tactile-Reactive Dexterous Manipulation](https://arxiv.org/abs/2606.17055)** — *Niu, Dantong et al.* · `2026-06-15` · `71/100`（C4·E4·O2·T5）
  > 100 小时触觉同步双臂灵巧数据中训练+低频动作专家/高频触觉专家级联流匹配的 VLA；作者报告 12 项真机触觉任务平均成功率 65%，比最强基线高 30 个百分点。 · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[IntentVLA: Short-Horizon Intent Modeling for Aliased Robot Manipulation](https://arxiv.org/abs/2605.14712)** — *Lian, Shijie et al.* · `2026-05-14` · 🏛️ **EMNLP 2026** · `71/100`（C4·E4·O3·T3） · 🟡
  > IntentVLA 用冻结 VGGT 编码近期视觉历史并融入 VLA，抑制观测混叠下的意图切换；作者报告自建 AliasBench 平均成功率 45.8%（基线 9.0%），SimplerEnv 72.9%、LIBERO 98.6%。 · [💻 code](https://github.com/ZGC-EmbodyAI/IntentVLA) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent RL](https://arxiv.org/abs/2608.16837)** — *Gu, Langzhe et al.* · `2026-08-17` · `68/100`（C4·E4·O2·T4）
  > HAF 将通用流匹配 VLA 改为"行走/头部→腰部→双臂"三阶段分层去噪，并在冻结骨干上做 DCT 低维噪声空间离线到在线 SAC；作者报告 7 项真机人形任务平均分 70.5%，高于最强基线 53.3%。 · [🌐 project](https://tau0-vla.github.io/) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[G0.5: One Autoregressive Stream for Robot Reasoning and Action](https://arxiv.org/abs/2608.11739)** — *Liu, Yicheng et al.* · `2026-08-12` · `68/100`（C4·E4·O2·T4） · 📄
  > Galaxea G0.5 用单一自回归解码器在同一 token 流中生成推理与动作，配合跨具身 RVQ 动作分词与视觉记忆；作者报告 R1 真机微调 76.7%、BEHAVIOR 挑战 31.4%、LIBERO 98.9%。 · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models](https://arxiv.org/abs/2607.26991)** — *Tan, Derek Ming Siang et al.* · `2026-07-29` · `68/100`（C3·E4·O3·T4） · 🟡
  > 在冻结 VLA 推理时，用基于动作专家潜变量训练的离线 RL 流策略组合引导动作采样，且仅在失败检测器报警时启用；作者报告 SIMPLER/PolaRiS 分布外任务最高提升 17.3%。 · [🌐 project](https://arxiv.org/abs/2607.23783) · [💻 code](https://github.com/marmotlab/RL2-VLA) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[Qwen-VLA: Alibaba's Embodied Foundation Model](https://arxiv.org/abs/2605.30280)** — *Alibaba* · `2026-05-28` · `68/100`（C4·E4·O2·T4） · 📄
  > Qwen-VLA 以 Qwen3.5-4B 加 DiT 动作专家统一操作、导航与轨迹预测；作者报告单一模型 LIBERO 97.9%、Simpler-WidowX 73.7%、RoboTwin 86.1/87.2%、R2R OSR 69.0%。 · [🌐 project](https://qwen.ai/blog?id=qwenvla) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action Framework for 3D Manipulation](https://arxiv.org/abs/2608.05042)** — *Li, Peiyan et al.* · `2026-08-05` · `67/100`（C3·E5·O2·T4）
  > 在 BridgeVLA 的多视图热力图 3D VLA 上加入时序记忆与可重渲染的点云空间记忆，支持记忆依赖与双臂任务；作者报告 RMBench、MemoryBench 上达到最优，并在两种真机平台验证。 · [🌐 project](https://arxiv.org/abs/2608.02580) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots](https://arxiv.org/abs/2607.02501)** — *Xu, Ling et al.* · `2026-07-02` · `66/100`（C3·E3·O4·T3） · 💻 · 🧩 *adjacent*
  > 面向 VLA 与世界-动作模型的可移植 C++ 推理运行时，五层架构支持多速率执行与量化；作者报告相对 Python 基线推理加速 1.05–2.70 倍、显存降低 7%–77%，成功率多数接近基线。 · [🌐 project](https://arxiv.org/abs/2607.23909) · [💻 code](https://github.com/SEU-PAISys/Embodied.cpp) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction](https://arxiv.org/abs/2506.13751)** — *Xue, Haoru et al.* · `2025-06-16` · `66/100`（C4·E3·O2·T5）
  > 人形全身控制的视觉-语言基准 LeVERB-Bench（150+ 任务/10 类）与分层潜动作框架 LeVERB；作者报告零样本总成功率 58.5%，约为朴素分层 VLA 的 7.8 倍。 · [📝 review](digests/migration-2026-10-22.md)

</details>

<details>
<summary>📋 <b>Also tracked / 观察中与暂不评级</b> · 35 papers</summary>

- **[EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](https://arxiv.org/abs/2609.01281)** — *Wang, Wei et al.* · `2026-09-01` · `63/100`（C3·E3·O3·T4） · 💻
  > EmbodiedSkills 以三个独立世界动作模型预测冻结 VLA 候选动作的潜在后果并据分歧与效应一致性选优，作者报告 MetaWorld MT50 成功率由 76.28% 升至 78.64%、CLIPort 由 33.94% 升至 36.83%。 · [💻 code](https://github.com/DCDmllm/EmbodiedSkills) · [📝 review](digests/migration-2026-10-22.md)

- **[ActionMap: Robot Policy Learning via Voxel Action Heatmap](https://arxiv.org/abs/2606.06904)** — *Yang, Pei et al.* · `2026-06-05` · `62/100`（C3·E4·O2·T4）
  > 用预测平移/旋转体素热力图的动作头替换 VLA 原生解码器，以高斯软标签交叉熵训练；作者报告 LIBERO 上相对 OpenVLA-OFT 的 L1 头同步数提升 8.2 个点，并在低数据下更高效。 · [📝 review](digests/migration-2026-10-22.md)

- **[GeoAlign: Beyond Semantics with State-Guided Spatial Alignment in VLA Models](https://arxiv.org/abs/2606.03240)** — *Chen, Yizhi et al.* · `2026-06-02` · `62/100`（C3·E4·O2·T4）
  > GeoAlign 以本体状态生成查询，从 RGB-D 后训练的几何编码器提取 8 个几何 token 条件化 GR00T 动作头；作者报告 LIBERO 99.0%、Fractal 85.3%、ALOHA 真机 78.8%。 · [📝 review](digests/migration-2026-10-22.md)

- **[Intercepting the Future: Latent-Space Predictive World Model for Dynamic VLA Manipulation](https://arxiv.org/abs/2606.02486)** — *Syed, Shahram Najam et al.* · `2026-06-01` · 🏛️ **CoRL 2026** · `62/100`（C4·E4·O1·T4）
  > AHEAD 给冻结 OpenVLA 外挂 4.9M 参数潜空间世界模型以预测未来特征；作者报告 20 个动态仿真场景成功率 79–97%（最强基线 31–58%），真机接抛射物 19/30，基线全为 0。 · [📝 review](digests/migration-2026-10-22.md)

- **[Hide-and-Seek in Trajectories: Discovering Failure Signals for VLA Runtime Monitoring](https://arxiv.org/abs/2605.30834)** — *Park, Seongheon et al.* · `2026-05-29` · 🏛️ **NeurIPS 2026** · `62/100`（C3·E4·O2·T4） · 📄 · 🧩 *adjacent*
  > Hide-and-Seek 仅用轨迹级成败标签，以轨迹间/内对比损失训练 VLA 运行时失败检测器；作者报告在 LIBERO-10、VLABench 与真机上对 OpenVLA、π0、π0.5 均优于 SAFE 等基线。 · [🌐 project](https://seongheon-96.github.io/hide_and_seek_site/) · [📝 review](digests/migration-2026-10-22.md)

- **[Self-Evolving Coding Agents: From Digital Programs to Physical-World Intelligence](https://arxiv.org/abs/2609.35432)** — *Hongcheng Gao et al.* · `2026-09-28` · `60/100`（C4·E3·O2·T3） · 📄
  > 提出 Physical Coding（Code as World + Code as Policy）与 HexaAnything 智能体；在 RoboCasa365 上把 XR-1 的总体成功率从 56.6% 提到 61.1%。 · [🌐 project](https://hexafuture.ai/blog/physical-coding) · [📝 review](digests/daily/2026-10-22.md)

- **[Zetta $\zeta$: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence](https://arxiv.org/abs/2608.16590)** — *Ding, Xin et al.* · `2026-08-17` · `60/100`（C4·E3·O2·T3）
  > Zetta 为冻结的 VLA 演化代码化运行时 critic 与恢复技能，形成闭环具身 harness；作者报告在 LIBERO-Pro 与 RoboCasa 留出种子上分别达 90.8% 与 93.6%，并配套 Z-Infra 提升 rollout 吞吐。 · [🌐 project](https://grange007.github.io/HAF) · [📝 review](digests/migration-2026-10-22.md)

- **[Does VLA Even Know the Basics? Measuring Commonsense and World Knowledge Retention in Vision-Language-Action Models](https://arxiv.org/abs/2606.19297)** — *Kachaev, Nikita et al.* · `2026-06-17` · `60/100`（C3·E3·O3·T3） · 💻 · 🧩 *adjacent*
  > 提出 Act2Answer 协议，把 VLM 知识基准改造成“放方块选答案”的桌面操作回合；作者评测 7 个 VLA 后报告其在颜色、形状等简单概念上表现好，而在更丰富语义类别上多接近随机。 · [🌐 project](https://orca-wm.github.io/) · [💻 code](https://github.com/CognitiveAISystems/Act2Answer) · [📝 review](digests/migration-2026-10-22.md)

- **[GesVLA: Pointing Gesture Grounding for Vision-Language-Action Models](https://arxiv.org/abs/2605.22812)** — *Xuan et al.* · `2026-05-21` · `60/100`（C3·E3·O3·T3） · 💻
  > GesVLA 把指点手势作为与语言并行的指令模态，双 VLM 结构加半合成手势数据；作者报告 ARX5 真机三项挑选任务平均成功率 83.3%，纯文本 VLA 为 31.7%，手势意图识别准确率 94.3%。 · [🌐 project](https://gwxuan.github.io/GesVLA/) · [💻 code](https://github.com/GWxuan/GesVLA) · [📝 review](digests/migration-2026-10-22.md)

- **[SparkVLA: Stop-Aware Hierarchical VLA with Adaptive Action Chunking for Long-Horizon Manipulation](https://arxiv.org/abs/2608.16172)** — *Lei, Xunyao et al.* · `2026-08-17` · `59/100`（C3·E4·O2·T3）
  > SparkVLA 把子任务终止与动作块执行长度放进同一候选集统一排序，作者报告在 RoboCerebra 上成功率 47.12%，比官方分层基线高 30.57 个百分点，并有真机长程任务验证。 · [📝 review](digests/migration-2026-10-22.md)

- **[DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for Cross-Embodiment Manipulation](https://arxiv.org/abs/2608.06374)** — *Li, Junfeng et al.* · `2026-08-06` · `59/100`（C3·E4·O2·T3）
  > 以未来帧生成监督学习跨本体动力学先验，按本体路由的 MoE 头输出原生动作；单一权重作者报告 LIBERO 98.0%、RoboCasa-GR1 59.25%、RoboTwin 2.0 89.02%。 · [🌐 project](https://arxiv.org/abs/2608.05369) · [📝 review](digests/migration-2026-10-22.md)

- **[World-to-Wrist: Task-Conditioned Future Wrist Modeling for Fine-Grained Robot Manipulation](https://arxiv.org/abs/2608.05369)** — *Pan, Yuhao et al.* · `2026-08-05` · `59/100`（C3·E4·O2·T3）
  > 以 VLM 中的潜在建模 token 为接口、结合腕部历史预测未来腕部 V-JEPA 潜变量并注入动作头，辅以 W2-CoT 结构化标注；作者报告 LIBERO 98.5%、LIBERO-Plus 84.0%，推理超 80 Hz。 · [🌐 project](https://arxiv.org/abs/2608.05369) · [📝 review](digests/migration-2026-10-22.md)

- **[3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training](https://arxiv.org/abs/2606.04436)** — *Shi, Jiaxin et al.* · `2026-06-03` · `59/100`（C3·E4·O2·T3）
  > 通过 3D 数据联合训练、对齐 VGGT 的几何适配器和推理锚点 token 自蒸馏，让 2D 输入的 VLA 隐式获得 3D 空间推理；作者报告 LIBERO 平均 98.7%、LIBERO-Plus 零样本 81.0%、SimplerEnv 72.9%。 · [📝 review](digests/migration-2026-10-22.md)

- **[Gaze2Act: Gaze-Conditioned Vision-Language-Action Policies for Interactive Robot Manipulation](https://arxiv.org/abs/2605.30282)** — *Zuo, Kuangji et al.* · `2026-05-28` · `59/100`（C3·E4·O2·T3）
  > Gaze2Act 把第一视角注视映射到机器人视角，以视觉提示和动作头条件注入 GR00T N1.5；作者报告 G1 上 15 个任务平均成功率 83.5%，高于 RoboGround 39.6%、ControlVLA 41.5%。 · [📝 review](digests/migration-2026-10-22.md)

- **[Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action](https://arxiv.org/abs/2605.22283)** — *Li, Pengteng et al.* · `2026-05-21` · 🏛️ **ICML 2026** · `59/100`（C3·E4·O2·T3）
  > SOMA 为 VLA 加入由可动头部相机扫描构建、在线更新并按指令检索的空间记忆，解决目标出视野的操作；作者报告 5 个真实出视野任务均优于 GR00T-N1.5 等基线，SimplerEnv 视觉匹配平均 63.2%。 · [📝 review](digests/migration-2026-10-22.md)

- **[Towards Human-Like Manipulation through RL-Augmented Teleoperation and Mixture-of-Dexterous-Experts VLA](https://arxiv.org/abs/2603.08122)** — *Tang, Tutian et al.* · `2026-03-09` · `57/100`（C3·E3·O2·T4）
  > RL 原子技能 IMCopilot 既辅助遥操作采集又作 VLA 底层原语，MoDE-VLA 以残差注入融合力/触觉；作者报告 4 项接触密集真机任务平均成功率 34%，π0 基线为 15%。 · [📝 review](digests/migration-2026-10-22.md)

- **[BORA: Bridging Offline Reinforcement Learning and Online Residual Adaptation for Real-World Dexterous VLA Models](https://arxiv.org/abs/2605.30226)** — *Chen, Zhongxi et al.* · `2026-05-28` · `56/100`（C3·E4·O1·T4）
  > BORA 在一致性策略 VLA 中集成动作条件 critic，离线训练后冻结基座、在线只学轻量残差 actor，并用局部策略辅助灵巧手人工纠正；作者报告 6 个真实灵巧任务每任务 20 条在线轨迹后成功率 60.8%→82.5%。 · [📝 review](digests/migration-2026-10-22.md)

- **[EXIMO: VLM Guided Exploration of VLA Policies](https://arxiv.org/abs/2608.19891)** — *Sukhija, Bhavya et al.* · `2026-08-20` · `54/100`（C3·E3·O1·T5）
  > EXIMO 以「VLM 编排探索→蒸馏 SFT→残差离策略 RL」三阶段微调 VLA，作者报告在 ALOHA 仿真 22 个长程/推理任务上样本效率与最终成功率均优于直接 RL 基线。 · [🌐 project](https://carldegio.github.io/latent_action.github.io) · [📝 review](digests/migration-2026-10-22.md)

- **[EATR-Stereo: Embodiment-Aware Routing of Paired Stereo Evidence for Humanoid Vision-Language-Action Control](https://arxiv.org/abs/2608.17453)** — *Wu, Songwei et al.* · `2026-08-18` · `53/100`（C3·E4·O1·T3）
  > EATR-Stereo 保留主视图 token，用交叉注意力从另一目构建对齐的辅助 token，并按分身体段本体状态路由；作者报告 33 自由度人形真机长程任务全程成功率 60%，遮挡恢复 80%。 · [🌐 project](https://tengbo-yu.github.io/PRISM/) · [📝 review](digests/migration-2026-10-22.md)

- **[StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models](https://arxiv.org/abs/2608.11671)** — *Xu, Siyu et al.* · `2026-08-12` · `53/100`（C3·E4·O1·T3）
  > StellaVLA 以检索到的一条结构化示范（任务计划、子目标、语言化 3D 运动）作上下文，并用并行语言专家联合训练；作者报告 LIBERO 98.8%、LIBERO-Plus 85.1%，VLA-Arena 总分 0.63。 · [📝 review](digests/migration-2026-10-22.md)

- **[Hidden in Plain Sight: Diffusion-Based Unrestricted Robotic Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2608.10393)** — *Han, Jiahui et al.* · `2026-08-11` · `53/100`（C3·E4·O1·T3） · 🧩 *adjacent*
  > DURA 沿预训练扩散模型的隐轨迹优化外观自然的对抗贴片，支持只用动作输出的黑盒攻击；作者报告在 LIBERO 上对 OpenVLA 的白盒 ASR 为 100%，并在 Franka 真机上打印贴片复现了攻击效果。 · [📝 review](digests/migration-2026-10-22.md)

- **[AtlasVLA: Persistent World-Ego State Modeling for Vision-Language-Action Models](https://arxiv.org/abs/2608.06729)** — *Zhao, Guiyu et al.* · `2026-08-07` · `53/100`（C3·E4·O1·T3）
  > AtlasVLA 只用腕部相机，靠体素哈希的 4D 持久世界记忆和自我工作记忆为 DiT 动作头提供条件；作者报告 LIBERO 平均 97.6%，真机长时程任务比 MemoryVLA 高 9 个点。 · [📝 review](digests/migration-2026-10-22.md)

- **[ElegantVLA: Learning When to Think for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2605.29438)** — *Li, Ye et al.* · `2026-05-28` · `53/100`（C3·E4·O1·T3） · 🧩 *adjacent*
  > ElegantVLA 用 RL 调度器按表征稳定性与运动线索为 VLA 骨干和动作头选择计算复用档位，无需重训；作者报告 SimplerEnv 上 CogACT 加速 3.77×，真机控制频率 13.8→26.3 Hz。 · [📝 review](digests/migration-2026-10-22.md)

- **[Lost in Reconstruction: Aligning Action Representations with Language in Vision-Language-Action Models](https://arxiv.org/abs/2608.10484)** — *Wenjie, Li et al.* · `2026-08-11` · `51/100`（C3·E3·O1·T4）
  > SALT 在 VQ-VAE 动作 tokenizer 中加入“让冻结语言模型从量化动作隐变量还原指令”的对齐损失；作者报告 SimplerEnv 平均成功率为 71.9%，VQ-VAE 和 FAST 分别为 42.7% 和 31.2%。 · [📝 review](digests/migration-2026-10-22.md)

- **[TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies](https://arxiv.org/abs/2606.06491)** — *Jing, Dong et al.* · `2026-06-04` · `51/100`（C3·E3·O1·T4）
  > 通过合并/拆分动作对示教重定时（VSTA）并把速度作为条件输入，使单个 VLA 可双向调速；作者报告 LIBERO 上默认速度成功率不降反升，并可借 GPT-4o 动态调度速度。 · [📝 review](digests/migration-2026-10-22.md)

- **[TTT-VLA: Test-Time Latent Prompt Optimization for Vision-Language-Action Models](https://arxiv.org/abs/2606.03127)** — *Zhang, Wenbo et al.* · `2026-06-02` · `51/100`（C3·E3·O1·T4）
  > TTT-VLA 训练时为 VLA 学习一个由状态接地代理任务约束的潜在提示，部署时只用自监督信号在环境交互数据上优化该提示；作者报告 SimplerEnv WidowX 平均成功率 51.1%→67.4%。 · [📝 review](digests/migration-2026-10-22.md)

- **[LIBERO-VIFO: Benchmarking the Capability and Safety of Visual Cue Following in Vision-Language-Action Models](https://arxiv.org/abs/2608.17600)** — *Qian, Zhengyan et al.* · `2026-08-18` · `48/100`（C3·E3·O1·T3） · 🧩 *adjacent*
  > LIBERO-VIFO 在 40 个 LIBERO 任务上构建 8 类、1,347 个视觉提示实例，同时评测 VLA 跟随授权提示的能力与受未授权提示诱导的风险；作者报告无语言指令时 7 个模型仍有 32–60% 会执行提示所指任务。 · [📝 review](digests/migration-2026-10-22.md)

- **[NebulaVLA: A Dual-Frequency Vision-Language-Action Model With Guide Action for Robotic Manipulation](https://arxiv.org/abs/2608.16503)** — *Zhao, Cong et al.* · `2026-08-17` · `48/100`（C3·E3·O1·T3）
  > NebulaVLA 采用 10 Hz 语义规划 + 20 Hz DiT 控制的异步双频架构，配合 GESTURE-7 动作表示与 Guide Action 平滑拼接，作者报告 LIBERO-Plus 总成功率 85.5%，真机延迟降至 42 ms。 · [📝 review](digests/migration-2026-10-22.md)

- **[Temporal GRPO: Beyond Trajectory-Level Credit in Vision-Language-Action Reinforcement Learning](https://arxiv.org/abs/2608.13026)** — *Zhou, Yao et al.* · `2026-08-13` · `48/100`（C3·E3·O1·T3）
  > Temporal GRPO 将任务拆成可检测阶段，只在进入同一阶段的 rollout 间比较，并把阶段优势分配到对应动作区间，缓解 VLA 强化后训练中的轨迹级信用混叠；作者报告 RoboTwin 2.0 各时域组均取得最高成功率。 · [📝 review](digests/migration-2026-10-22.md)

- **[DREAM-Chunk: Reactive Action Chunking with Latent World Model](https://arxiv.org/abs/2606.18589)** — *Chen, Wenxi et al.* · `2026-06-17` · `48/100`（C3·E3·O1·T3）
  > 测试时采样多条动作块并用轻量潜在世界模型推演，按观测潜态最接近者切换执行块，无需微调 VLA；作者报告 SO-101 上 USB 插拔 75%→95% 等真机提升。 · [📝 review](digests/migration-2026-10-22.md)

- **[Can VLA Models Learn from Real-World Data Continually without Forgetting?](https://arxiv.org/abs/2605.26820)** — *Zhu, Jiarun et al.* · `2026-05-26` · `48/100`（C3·E3·O1·T3） · 🧩 *adjacent*
  > 构建 10 个真机单臂/双臂任务的 VLA 持续学习基准，作者报告朴素顺序微调严重遗忘（单臂 AS 31.4、BWT -81.0），而配置得当的经验回放 AS 达 97.2，并优于同算力的多任务联合训练。 · [📝 review](digests/migration-2026-10-22.md)

- **[Neural Introspection Gating for Adaptive KV-Cache Reuse in Vision-Language-Action Models](https://arxiv.org/abs/2608.10824)** — *Wu, Zhijie et al.* · `2026-08-11` · 🏛️ **IROS 2026** · `45/100`（C2·E3·O1·T4）
  > Gated VLA-Cache 用 top-2 动作 token 的 logit 间隔作为置信度，在低置信时让 KV 缓存失效并完整重算；作者报告在 LIBERO-Goal/Long 上收回了 VLA-Cache 损失的全部精度，同时保留约 80% 的算力节省。 · [📝 review](digests/migration-2026-10-22.md)

- **[PhysiFlow: Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent Flow Matching and Robust Tracking](https://arxiv.org/abs/2603.05410)** — *Qin, Weikai et al.* · `2026-03-05` · `42/100`（C2·E3·O1·T3）
  > 仿生「多脑」人形全身 VLA：CVAE 语义潜变量 + flow matching 动作生成 + RL 跟踪器；作者报告 Isaac Lab 9 项任务平均成功率 74.9%，复现的 LeVERB 为 65.0%。 · [📝 review](digests/migration-2026-10-22.md)

- **[HODAgent: Towards On-Demand, Responsive Humanoids for Physical World Human Interaction](https://arxiv.org/abs/2608.17584)** — *Chen, Wang Warren et al.* · `2026-08-18`
  > HODAgent 是面向服务场景的人形机器人 System-2 智能体（交互器、规划器、执行器与分层记忆）；摘要称仿真 164 例联合成功率 84.8%/91.5%，但论文已被作者撤回，结论无法核验。 · [📝 review](digests/migration-2026-10-22.md)

- **[Action with Visual Primitives](https://arxiv.org/abs/2605.22183)** — *Guo, Weilong et al.* · `2026-05-21`
  > AVP 让 VLM 先推断下一阶段目标并输出视觉基元 token，再条件化 flow-matching 动作专家；摘要称真机抓放比 π0.5 成功率高 37.04%，但该论文已于 v4 撤稿，结果无法核验。 · [📝 review](digests/migration-2026-10-22.md)

</details>

<details>
<summary>📜 <b>Classic landmarks / 经典奠基</b> · 3 papers</summary>

- 📜 **[GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734)** — *NVIDIA* · `2025-03-18` · `95/100`（C5·E4·O5·T5） · 💻
  > NVIDIA 开放的人形通用 VLA：System 2 VLM + System 1 DiT flow-matching 双系统，用真机、仿真、神经生成轨迹与人类视频「数据金字塔」训练；作者报告在三套仿真基准与 GR-1 真机上优于基线。 · [🌐 project](https://developer.nvidia.com/isaac/gr00t) · [💻 code](https://github.com/NVIDIA/Isaac-GR00T) · [📝 review](digests/migration-2026-10-22.md)

- 📜 **[RDT-1B: A Diffusion Foundation Model for Bimanual Manipulation](https://arxiv.org/abs/2410.07864)** — *Liu et al.* · `2024-10-10` · `86/100`（C4·E4·O5·T4） · 💻
  > 1.2B 参数扩散 Transformer 双臂操作基础模型，用物理可解释的统一动作空间在多机器人数据上预训练；作者报告在 ALOHA 真机上零样本泛化与 1–5 次示范学新技能均优于 ACT、OpenVLA、Octo。 · [🌐 project](https://rdt-robotics.github.io/rdt-robotics/) · [💻 code](https://github.com/thu-ml/RoboticsDiffusionTransformer) · [📝 review](digests/migration-2026-10-22.md)

- 📜 **[OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)** — *Kim et al.* · `2024-06-13` · `100/100`（C5·E5·O5·T5） · 💻
  > 基于 Llama 2 + DINOv2/SigLIP 的 7B 开源 VLA，用 97 万条 OXE 示范训练；作者报告 29 项真机任务上比 RT-2-X 高 16.5 个百分点，支持 LoRA 与量化。 · [🌐 project](https://openvla.github.io) · [💻 code](https://github.com/openvla/openvla) · [📝 review](digests/migration-2026-10-22.md)

</details>


### World Models · 62

<details open>
<summary>🔥 <b>Must-read & notable / 重点与值得关注</b> · 29 papers</summary>

- 🔥 **[Long-WAM: Scaling the Context of World-Action Models](https://arxiv.org/abs/2610.10528)** — *Wei Huang et al.* · `2026-10-07` · `88/100`（C4·E5·O4·T5） · 💻
  > 自回归视频预训练 + 因果世界-动作模型：GR-1 上 19.2 s 上下文把成功率从 63.3% 提到 78.7%，RTX 5090 每动作块 107.4 ms。 · [🌐 project](https://nvlabs.github.io/LongLive/Long-WAM/) · [💻 code](https://github.com/NVlabs/LongLive) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[Flex-$\pi$: A Multi-Stream World-Action Model with Compute Flexibility](https://arxiv.org/abs/2608.10860)** — *Yan, Ge et al.* · `2026-08-11` · `88/100`（C4·E5·O4·T5） · 💻
  > Flex-π 用冻结的 Wan VAE 同时编码 RGB 与 3D 点图，加上 DINO 语义，与动作联合去噪，单个 checkpoint 支持从纯动作到全联合生成；作者报告在真机双臂灵巧任务上比最强基线高 2–7 倍。 · [💻 code](https://github.com/geyan21/flex-pi) · [📝 review](digests/migration-2026-10-22.md)

- 🔥 **[Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](https://arxiv.org/abs/2610.26855)** — *Tianqi Liu et al.* · `2026-10-19` · `86/100`（C5·E4·O4·T4） · 🟡
  > Ropedia W0 用相机位姿+投影骨架统一人/机器人运动，建 1.3 万小时 Xp-Data 与 Xp-Teleop；作者报告在 DreamDojo、ω-HOME 等五个跨具身基准上视频预测领先。 · [🌐 project](https://ropedia.github.io/ropedia-w0/) · [💻 code](https://github.com/Ropedia/ropedia-w0) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[LeWAM: End-to-End World and Action Modeling with JEPAs](https://arxiv.org/abs/2610.12818)** — *Minghao Fu et al.* · `2026-10-08` · `86/100`（C4·E4·O5·T4） · 💻
  > 首个端到端 JEPA：联合潜状态预测与动作 flow matching，在 10 个仿真任务上把接触密集/长程任务的规划成功率做到 89.7%/46.2%，规划快 32.3 倍。 · [🌐 project](https://le-wam.github.io/) · [💻 code](https://github.com/MinghaoFu/lewam) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining](https://arxiv.org/abs/2609.07398)** — *Yuran Wang et al.* · `2026-09-07` · `86/100`（C5·E4·O4·T4） · 💻
  > OpenWAM 把世界-动作模型拆成可组合模块并系统消融，用 6,369 小时数据训练 OpenWAM-α；作者报告 LIBERO 99.3%、EBench 49.4、真机 RoboDojo 24.4% 成功率。 · [🌐 project](https://openwam-official.github.io/) · [💻 code](https://github.com/OpenWAM-Official/OpenWAM) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators](https://arxiv.org/abs/2608.27406)** — *Liu, Kechen et al.* · `2026-08-27` · `83/100`（C4·E4·O5·T3） · 💻
  > CLAP 用末端位姿、语言与潜动作统一异构动作空间并以课程式训练跨具身视频世界模型，作者报告在 DROID 上接近或超过单具身 Ctrl-World，并可零样本用于多策略规划。 · [💻 code](https://github.com/omni-CLAP/clap) · [📝 review](digests/migration-2026-10-22.md)

- 🔥 **[RynnWorld-4D: 4D Embodied World Models for Robotic Manipulation](https://arxiv.org/abs/2607.06559)** — *Zhao, Haoyu et al.* · `2026-07-07` · `80/100`（C4·E4·O4·T4） · 💻
  > 由单张 RGB-D 图与语言指令同步生成未来 RGB、深度与光流的 4D 世界模型，配套 2.54 亿帧 Rynn4DDataset 与逆动力学策略头；作者报告真机灵巧操作上优于 π0.5、DP 等基线。 · [🌐 project](https://alibaba-damo-academy.github.io/RynnWorld-4D.github.io/) · [💻 code](https://github.com/alibaba-damo-academy/RynnWorld-4D) · [📝 review](digests/migration-2026-10-22.md)

- 🔥 **[$\texttt{WEAVER}$, Better, Faster, Longer: An Effective World Model for Robotic Manipulation](https://arxiv.org/abs/2606.13672)** — *Jain, Arnav Kumar et al.* · `2026-06-11` · `80/100`（C4·E4·O4·T4） · 💻
  > 多视角潜空间流匹配世界模型，兼顾保真、长时一致与速度；作者报告真机策略评估相关性 0.870、合成数据使 π0.5 成功率提升 38%、测试时规划提升 14%。 · [🌐 project](https://arnavkj1995.github.io/WEAVER/) · [💻 code](https://github.com/arnavkj1995/WEAVER) · [📝 review](digests/migration-2026-10-22.md)

- 🔥 **[$\mu_0$: A Scalable 3D Interaction-Trace World Model](https://arxiv.org/abs/2606.13769)** — *Lee, Seungjae et al.* · `2026-06-11` · 🏛️ **CoRL 2026** · `80/100`（C4·E4·O4·T4） · 💻
  > 从异构视频自动提取事件级 3D 交互轨迹训练轨迹世界模型 μ0，冻结后接动作专家；作者报告 UR3 真机三任务平均 91.7%，RoboCasa365 上 30.25% 高于 π0。 · [🌐 project](https://mu0-wm.github.io/) · [💻 code](https://github.com/Yoonkyo/mu0) · [📝 review](digests/migration-2026-10-22.md)

- 🔥 **[OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics](https://arxiv.org/abs/2606.04463)** — *Wu, Zhuoyuan et al.* · `2026-06-03` · `80/100`（C4·E4·O4·T4） · 🟡
  > 用 2D 运动学骨架渲染统一条件化多种机械臂与人手的动作条件视频世界模型 OSCAR（微调 Cosmos-Predict2.5-2B），作者报告在 RoboArena 7 个策略上虚拟评测与真机结果显著相关。 · [🌐 project](https://wuzy2115.github.io/oscar-project-page/) · [💻 code](https://github.com/wuzy2115/oscar-public) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[GreenWAM: A World Foundation Model for Robotics](https://arxiv.org/abs/2610.18774)** — *Gennady Sidorov et al.* · `2026-10-13` · `77/100`（C4·E4·O4·T3） · 🟡
  > GreenWAM 以 79 维解剖动作空间统一 20 类双臂机器人，世界模型与策略共用一套权重；作者报告 RoboTwin 2.0 平均 67.54%、人形真机 ID 95.6%。 · [🌐 project](https://greenvla.github.io/GreenWAM/) · [💻 code](https://github.com/greenvla/GreenWAM) · [📝 review](digests/daily/2026-10-22.md)

- 👀 **[Keep the Future, Drop the Rollout: RIFT for World Action Models](https://arxiv.org/abs/2608.11521)** — *Zhang, Chushan et al.* · `2026-08-12` · `77/100`（C4·E4·O4·T3） · 💻
  > RIFT 用可学习的预期 token 一次前向生成未来 K/V 缓存，取代世界动作模型的迭代视频 rollout；作者报告 LIBERO 98.8%、提速 3.1–9.2 倍，真机三任务平均成功率 45.3%。 · [💻 code](https://github.com/ChushanZhang/RIFT) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[$N_0$-TWAM: Scaling Tactile-Native World-Action Model for Contact-Rich Manipulation](https://arxiv.org/abs/2607.23783)** — *NeoteAI Team et al.* · `2026-07-26` · `77/100`（C4·E4·O4·T3） · 💻
  > 触觉原生的世界-动作模型，在同一流匹配目标下联合预测未来视觉、触觉与动作；作者报告 UniVTAC 平均成功率 84.5%，8 项真机接触任务整体优于 π0.5 等基线。 · [🌐 project](https://arxiv.org/abs/2607.23782) · [💻 code](https://github.com/neoteai/N0-TWAM) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[PAWBench: How Far Are We from Probabilistically Aligned World Modeling?](https://arxiv.org/abs/2608.27345)** — *Pu, Yuandong et al.* · `2026-08-27` · `74/100`（C3·E4·O4·T4） · 💻 · 🧩 *adjacent*
  > PAWBench 用 50 个随机物理场景检验视频生成模型重复采样能否复现正确的结果分布，作者报告 11 个模型均未能同时匹配参考概率并覆盖全部合理结果。 · [🌐 project](https://pawbench.github.io/) · [💻 code](https://github.com/Andrew0613/PAWBench) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[DriftWorld: Fast World Modeling through Drifting](https://arxiv.org/abs/2607.15065)** — *Lu, Susie et al.* · `2026-07-16` · `74/100`（C4·E4·O3·T4） · 💻
  > 将 drifting 生成模型用于动作条件世界模型，单次前向生成未来帧（40+ FPS）；作者报告在 Bridge-V2、RT-1 等 5 个数据集上比扩散基线快 12 倍以上且画质相当或更好，并可用于动作筛选与离线策略评估。 · [🌐 project](https://arxiv.org/abs/2607.15330) · [💻 code](https://github.com/Susie-Lu/driftworld) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[Kairos: A Regret-Aware Native World-Action Model Stack for Physical AI](https://arxiv.org/abs/2606.16533)** — *Kairos Team et al.* · `2026-06-15` · `72/100`（C4·E3·O4·T3） · 💻
  > 4B 原生世界-动作模型栈，以“控制充分状态”为目标，结合跨本体数据课程、混合线性时序注意力与部署协同设计；作者报告在多项具身世界模型与世界-动作基准上领先并具效率优势。 · [🌐 project](https://arxiv.org/abs/2607.19191) · [💻 code](https://github.com/kairos-agi/kairos) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation](https://arxiv.org/abs/2605.21800)** — *Maes, Lucas et al.* · `2026-05-20` · `72/100`（C3·E3·O4·T5） · 💻 · 🧩 *adjacent*
  > 世界模型开源统一平台 swm：Lance 数据层、DINO-WM/LeWM/TD-MPC2 等基线、CEM/MPPI 规划器与可控扰动环境；作者在 Push-T 上复现基线，并显示轻微分布偏移即令规划成功率骤降。 · [💻 code](https://github.com/galilai-group/stable-worldmodel) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention for Video Generation and World Models](https://arxiv.org/abs/2608.18484)** — *Taghavi, Pardis et al.* · `2026-08-19` · `71/100`（C3·E4·O4·T3） · 💻 · 🧩 *adjacent*
  > SparsePR 以响应耦合分组与探针拟合残差重建实现免训练块稀疏注意力，作者报告在 Cosmos-Predict2.5 等四个视频/世界模型上端到端加速 1.48–2.61 倍且保真度优于 SVG2 等基线。 · [🌐 project](https://pardistaghavi.github.io/SparsePR-website/) · [💻 code](https://github.com/PardisTaghavi/SparsePR) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[Hydra-0: Action Flow for Generalist World Modeling and Control](https://arxiv.org/abs/2608.18077)** — *Li, Hongyu et al.* · `2026-08-18` · `71/100`（C4·E4·O2·T5）
  > 以“动作流”（像素平面轨迹）统一表示跨本体动作的视频世界模型，作者报告机器人/物体运动误差较动作条件基线降90.4%/60.2%，RoboLab开环评测成功率相关r=0.96。 · [🌐 project](https://unireflex.github.io/) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[Masked Visual Actions for Unified World Modeling](https://arxiv.org/abs/2607.19343)** — *Alzayer, Hadi et al.* · `2026-07-21` · `71/100`（C4·E4·O2·T5）
  > 把机器人动作表示为像素空间中被部分揭示的实体轨迹掩膜来条件视频模型，同一检查点兼作前向与逆向模型；作者报告 DROID/BEHAVIOR 上重建指标明显优于 Ctrl-World，并用于策略评估与规划。 · [🌐 project](https://arxiv.org/abs/2607.15330) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding](https://arxiv.org/abs/2607.19876)** — *Liu, Zeyu et al.* · `2026-07-22` · 🏛️ **ECCV 2026** · `69/100`（C3·E3·O4·T4） · 💻 · 🧩 *adjacent*
  > 不依赖逆动力学模型，用分割+深度+FoundationPose 从生成视频直接提取末端 6D 位姿并在 ManiSkill3 中闭环执行，评测具身视频世界模型；含 20 任务、4 个评测套件与 SPARC/可操作度指标。 · [🌐 project](https://arxiv.org/abs/2607.19191) · [💻 code](https://github.com/minecraft-zzz/KineBench) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[iMaC: Translating Actions into Motion and Contact Images for Embodied World Models](https://arxiv.org/abs/2606.09813)** — *Wu, Zhenyu et al.* · `2026-06-08` · `69/100`（C4·E3·O3·T4） · 💻
  > 把未来关节动作经 URDF/FK 渲染为运动图像、结合预测深度构建机器人-场景接触图像，作为视频世界模型的稠密控制；作者报告八项真机任务中六项的世界模型评分与真实策略表现强相关。 · [🌐 project](https://imac-wm.github.io/) · [💻 code](https://github.com/imac-wm/iMac) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models](https://arxiv.org/abs/2605.31158)** — *Lu, Jiacheng et al.* · `2026-05-29` · `69/100`（C3·E3·O4·T4） · 💻 · 🧩 *adjacent*
  > Light Interaction 按相机位姿相似度裁剪空间记忆、自适应时间窗、复用去噪步输出，并以 Triton 融合的 3D 块稀疏注意力加速交互式视频世界模型；作者报告 HY-WorldPlay 免训练加速 2.59×。 · [🌐 project](https://2843721358l-del.github.io/Light-Interaction-Project/) · [💻 code](https://github.com/2843721358l-del/Light-Interaction-Project) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[WALL-SS: Scaling Long-horizon World Models via Next-Scale Autoregression](https://arxiv.org/abs/2608.26239)** — *Zhang, Maeve et al.* · `2026-08-26` · `68/100`（C4·E4·O2·T4） · 📄
  > WALL-SS 以动作条件的逐尺度自回归生成机器人多视角未来，配合尺度压缩长程记忆与在线对齐，作者报告可稳定生成分钟级流式推演，并在 600 对真机-生成闭环回放中与真实结果较一致。 · [🌐 project](http://x2robot.com/pages/ss) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World Models](https://arxiv.org/abs/2608.14022)** — *Li, Xinye et al.* · `2026-08-14` · `66/100`（C3·E3·O4·T3） · 💻
  > 四阶段渐进因果训练把双向动作条件视频生成器蒸馏为1/2/4步交互世界模型；作者报告在Minecraft配对轨迹上多项画质与控制指标领先，1步版约72 FPS。 · [🌐 project](https://asdfo123.github.io/ForgeWM) · [💻 code](https://github.com/asdfo123/ForgeWM) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU](https://arxiv.org/abs/2607.19191)** — *Jiang, Fan et al.* · `2026-07-21` · `66/100`（C3·E3·O4·T3） · 💻
  > 动作条件视频世界模型，经因果蒸馏与 LongForcing 抑制长程漂移，作者报告单张 RTX 5090 上 720P 最高 16 FPS、动作到首帧延迟 1.2 秒，并在 WorldRoamBench 上可控性有竞争力。 · [🌐 project](https://abot-world.amap.com/) · [💻 code](https://github.com/amap-cvlab/ABot-World) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[AlayaWorld: Interactive Long-Horizon World Modeling -- Full Technical Report](https://arxiv.org/abs/2607.18367)** — *AlayaWorld Team et al.* · `2026-07-20` · `66/100`（C3·E3·O4·T3） · 💻 · 🧩 *adjacent*
  > 基于 LTX-2.3 视频 DiT 的交互式长时视频世界模型，结合时空记忆、防漂移训练与 4 步蒸馏；作者报告在 iWorld-Bench 多数指标上优于 Matrix-Game 2.0、HY-World 1.5 等开源模型。 · [🌐 project](https://arxiv.org/abs/2607.18367) · [💻 code](https://github.com/AlayaLab/AlayaWorld) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[DreamX-World 1.0: A General-Purpose Interactive World Model](https://arxiv.org/abs/2606.16993)** — *DreamX Team et al.* · `2026-06-15` · `66/100`（C3·E3·O4·T3） · 💻
  > 基于 Wan2.2 的通用交互式视频世界模型，含 E-PRoPE 相机控制、场景记忆与可组合事件，作者报告 8 卡 RTX 5090 达 16 FPS，自建评测总分 84.76。 · [🌐 project](https://amap-ml.github.io/DreamX_World/) · [💻 code](https://github.com/AMAP-ML/DreamX-World) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[MemoryWAM: Efficient World Action Modeling with Persistent Memory](https://arxiv.org/abs/2606.20562)** — *Yang, Sizhe et al.* · `2026-06-18` · `65/100`（C4·E4·O1·T5）
  > 以近期帧、事件边界锚帧与少量 gist token 组成混合记忆的世界-动作模型；作者报告 RMBench 平均成功率比 LingBot-VA 高 4.8 个百分点，且推理延迟与显存更低。 · [📝 review](digests/migration-2026-10-22.md)

</details>

<details>
<summary>📋 <b>Also tracked / 观察中与暂不评级</b> · 32 papers</summary>

- **[Learning How the World Evolves: Extrapolative Video World Models via Latent Dynamics Reasoning](https://arxiv.org/abs/2608.09926)** — *Li, Haodong et al.* · `2026-08-10` · `63/100`（C3·E3·O3·T4） · 🟡 · 🧩 *adjacent*
  > LDR 把隐状态转移写成显式运动学积分，只回归三阶及以上残差；作者报告在 PhyWorld 五类物理任务上，ID-OOD 误差差距比 DiT 基线小 20 倍以上，参数少 26 倍。 · [🌐 project](https://lat-dyn-reason.github.io/) · [💻 code](https://github.com/adobe-research/LDR) · [📝 review](digests/migration-2026-10-22.md)

- **[Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models](https://arxiv.org/abs/2606.25473)** — *Zheng, Kaiwen et al.* · `2026-06-24` · `63/100`（C3·E3·O3·T4） · 💻 · 🧩 *adjacent*
  > 将 rCM 扩展到自回归视频扩散，用 teacher-forcing 一致性蒸馏初始化 self-forcing DMD；作者报告 2 步因果 Wan2.1-1.3B 在 VBench-T2V 达 84.63，并演示 Cosmos 3 交互式世界模型。 · [💻 code](https://github.com/NVlabs/rcm) · [📝 review](digests/migration-2026-10-22.md)

- **[World Value Models for Robotic Manipulation](https://arxiv.org/abs/2606.24742)** — *Wang, Zhihao et al.* · `2026-06-23` · `63/100`（C4·E3·O2·T4） · 📄
  > 以视频世界模型为骨干构建通用机器人价值模型 WVM，并发布含 800 条次优轨迹的 Suboptimal-Value-Bench；作者报告其在专家与次优数据上的 VOC 均优于 GVL、VLAC 等基线。 · [🌐 project](https://zh1hao.wang/wvm/) · [📝 review](digests/migration-2026-10-22.md)

- **[Sensorimotor World Models: Perception for Action via Inverse Dynamics](https://arxiv.org/abs/2606.20104)** — *Ivashkov, Petr et al.* · `2026-06-18` · `63/100`（C3·E3·O3·T4） · 💻
  > 用单一逆动力学正则端到端训练 JEPA 式潜在世界模型，防止表征坍缩并偏向可控自由度；作者报告在四个仿真控制任务上规划成功率持平或优于 SIGReg 基线。 · [💻 code](https://github.com/petr-ivashkov/sensorimotor-world-model) · [📝 review](digests/migration-2026-10-22.md)

- **[Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation](https://arxiv.org/abs/2606.17030)** — *Zhang, Jie et al.* · `2026-06-15` · `63/100`（C4·E3·O2·T4）
  > 以自然语言为统一动作接口的 20B 具身视频世界模型，在 860 万视频-文本对上训练；作者报告 EWMBench 总分 4.60、DreamGen Bench 4.952 均居首。 · [🌐 project](https://pre.qwen.ai/blog?id=qwen-robotworld) · [📝 review](digests/migration-2026-10-22.md)

- **[WorldOlympiad: Can Your World Model Survive a Triathlon?](https://arxiv.org/abs/2606.11129)** — *Zhao, Yuke et al.* · `2026-06-09` · `63/100`（C3·E3·O3·T4） · 💻 · 🧩 *adjacent*
  > 提出覆盖机器人、游戏、真实视频的视频世界模型基准，从物理、几何、交互三条赛道评测 8 个模型，作者报告几何一致性普遍不足（最高 0.424）。 · [🌐 project](https://alibaba-damo-academy.github.io/WorldOlympiad/) · [💻 code](https://github.com/alibaba-damo-academy/WorldOlympiad) · [📝 review](digests/migration-2026-10-22.md)

- **[Latent Spatial Memory for Video World Models](https://arxiv.org/abs/2606.09828)** — *Wang, Weijie et al.* · `2026-06-08` · `63/100`（C3·E3·O3·T4） · 💻
  > 把视频世界模型的 3D 记忆从 RGB 点云搬到扩散潜空间，作者报告端到端生成最高提速 10.57 倍、显存降 55 倍，WorldScore 平均分 70.36 居对比方法首位。 · [🌐 project](https://microsoft.github.io/LatentSpatialMemory/) · [💻 code](https://github.com/microsoft/LatentSpatialMemory) · [📝 review](digests/migration-2026-10-22.md)

- **[MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.09215)** — *Zheng, Jia et al.* · `2026-06-08` · `62/100`（C4·E4·O1·T4）
  > 以 Cosmos 视频 DiT 单次前向的中间去噪特征条件化动作 DiT，预测统一全身运动潜变量驱动人形移动操作；作者报告 G1 九项真机任务总体成功率比最强 VLA 基线高 30 个点以上。 · [🌐 project](https://kairos-homeworld.github.io/) · [📝 review](digests/migration-2026-10-22.md)

- **[Dreaming when Necessary: Advancing World Action Models with Adaptive Multi-Modal Reasoning](https://arxiv.org/abs/2606.07089)** — *Tang, Yinzhou et al.* · `2026-06-05` · `62/100`（C3·E4·O2·T4）
  > 用轻量路由器按执行阶段决定是否调用文本子任务推理与视频想象，其余步骤只解码动作；作者报告 LIBERO-Long 99.1%、RoboTwin 2.0 困难子集最优，推理效率接近纯动作 WAM。 · [📝 review](digests/migration-2026-10-22.md)

- **[Reinforcing VLAs in Task-Agnostic World Models](https://arxiv.org/abs/2605.12334)** — *Wang, Yucen et al.* · `2026-05-12` · `62/100`（C4·E4·O1·T4）
  > RAW-Dream 在任务无关视频世界模型中用 VLM 零样本奖励 RL 微调 VLA，并以双噪声验证过滤幻觉；作者报告 LIBERO 四个未见套件平均成功率从 1-shot SFT 的 43.4% 提至 52.3–57.1%。 · [📝 review](digests/migration-2026-10-22.md)

- **[SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space](https://arxiv.org/abs/2608.01397)** — *Zhao, Ruiteng et al.* · `2026-08-02` · `59/100`（C3·E4·O2·T3） · 📄
  > 在策略自身表征空间中用可学习动态 token 与 EMA 目标预测动作条件下的未来潜状态，并以 VGGT 几何监督塑形；0.9B 模型作者报告 LIBERO 98.5%、LIBERO-Plus 零样本 73.0%。 · [🌐 project](https://sg-wam.github.io/) · [📝 review](digests/migration-2026-10-22.md)

- **[ContactWorld: What Matters in Vision-Tactile World Models for Contact-Rich Manipulation](https://arxiv.org/abs/2606.13877)** — *Zhang, Zhiyuan et al.* · `2026-06-11` · `59/100`（C3·E4·O2·T3） · 🧩 *adjacent*
  > 固定世界模型与 MPC 规划框架，系统比较视觉与触觉表征在 12 个接触密集任务上的作用；作者报告点云+触觉力场仿真平均成功率 36.1% 最高，并做 900 次真机验证。 · [📝 review](digests/migration-2026-10-22.md)

- **[H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models](https://arxiv.org/abs/2608.13049)** — *Rong, Dingyi et al.* · `2026-08-13` · `57/100`（C3·E3·O2·T4） · 📄 · 🧩 *adjacent*
  > H2R-Bench 用 120 条 EgoDex 人类视频构造 240 个人到机器人（夹爪/灵巧手）视频迁移案例，从目标、动作、接触、具身、画质五个维度评测 11 个视频生成模型；作者报告 Seedance 2.0 居首，多数模型在具身与接触上失败。 · [🌐 project](https://rongdingyi.github.io/H2R-Bench/) · [📝 review](digests/migration-2026-10-22.md)

- **[WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reactivity](https://arxiv.org/abs/2608.02603)** — *Yang, Yuxue et al.* · `2026-08-03` · `57/100`（C3·E3·O2·T4） · 📄 · 🧩 *adjacent*
  > 分四层（视觉质量、控制遵循、空间一致、世界反应性）评测视频世界模型的基准，含 8 项任务 1,474 个用例；作者评测 20 个相机/动作/语言驱动模型，发现无一兼顾覆盖与表现。 · [🌐 project](https://huggingface.co/papers/2608.01735) · [📝 review](digests/migration-2026-10-22.md)

- **[Wonder: Video World Model Done Better](https://arxiv.org/abs/2607.26037)** — *Xu, Jiacong et al.* · `2026-07-28` · `57/100`（C3·E3·O2·T4）
  > 实时相机可控视频世界模型，用像素空间坐标场做相机条件、稀疏注意力检索长时记忆并改进自蒸馏；作者报告 16 FPS 分钟级生成，在自建 I2V/V2V 基准上视觉质量与相机跟随误差优于近期流式世界模型。 · [🌐 project](https://arxiv.org/abs/2607.26037) · [📝 review](digests/migration-2026-10-22.md)

- **[MemLearner: Learning to Query Context memory for Video World Models](https://arxiv.org/abs/2606.31734)** — *Yu, Jiwen et al.* · `2026-06-30` · 🏛️ **ECCV 2026** · `57/100`（C3·E3·O2·T4） · 🧩 *adjacent*
  > 用视频生成模型自身的 query token 自适应检索历史上下文作为视频世界模型记忆；作者报告在含遮挡与动态物体的自建数据上 PSNR/LPIPS/FVD 均优于 CaM、VMem 等基线。 · [🌐 project](https://yujiwen.github.io/memlearner/) · [📝 review](digests/migration-2026-10-22.md)

- **[Targeting World Models to Compromise Robot Learning Pipelines](https://arxiv.org/abs/2606.09499)** — *Rathbun, Ethan et al.* · `2026-06-08` · 🏛️ **CoRL Spotlight** · `57/100`（C4·E3·O1·T4） · 🧩 *adjacent*
  > 提出视觉提示劫持与视觉转移劫持两类攻击，在看似安全的遥操作数据中植入扰动，经世界模型生成后毒化下游策略；作者报告在 DINO-WM 上实现端到端 PPO 后门，并对 Cosmos-Predict2.5 给出概念验证。 · [📝 review](digests/migration-2026-10-22.md)

- **[DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation](https://arxiv.org/abs/2608.13489)** — *DreamX Team et al.* · `2026-08-13` · `54/100`（C3·E3·O2·T3） · 📄
  > DreamX-Phi 1.0 在 Wan2.2-5B 上用逐臂 SE(3) 的 PRoPE 注意力编码动作、加深度分支与 SAM3+V-JEPA 物体一致性监督，并做 DMD 少步蒸馏；作者报告在 WorldArena 2.0 快照中 Track 1 第一、Track 2 并列第二。 · [🌐 project](https://github.com/AMAP-ML/DreamX-Phi) · [📝 review](digests/migration-2026-10-22.md)

- **[WorldCycle: Self-Verifiable Reinforcement Learning for Long-Horizon Video World Models](https://arxiv.org/abs/2608.04964)** — *Gu, Bohai et al.* · `2026-08-05` · `54/100`（C3·E3·O2·T3）
  > 利用可逆动作循环必然回到初始状态这一约束，为交互式视频世界模型构造免标注的空间闭合与时间一致奖励做 RL 后训练；作者报告在自建 CycleBench 上回归漂移最多降 44%。 · [🌐 project](https://arxiv.org/abs/2608.02580) · [📝 review](digests/migration-2026-10-22.md)

- **[STRIPS-WM: Learning Grounded Propositional STRIPS-style World Models from Images](https://arxiv.org/abs/2606.06832)** — *Ajith, Abhiroop et al.* · `2026-06-05` · 🏛️ **CoRL 2026** · `54/100`（C3·E3·O2·T3）
  > 仅从“图像-高层动作-图像”转移中学出抽象任务图，再用 CP-SAT 学二值谓词与 STRIPS 算子并蒸馏到视觉分类器，实现由起止图像做经典规划；作者报告在视觉重排任务上规划成功率优于 LatPlan 等基线。 · [📝 review](digests/migration-2026-10-22.md)

- **[PiL-World: A Chunk-Wise World Model for VLA Policy-in-the-Loop Evaluation](https://arxiv.org/abs/2606.05773)** — *Ma, Chong et al.* · `2026-06-04` · `54/100`（C3·E3·O2·T3） · 🧩 *adjacent*
  > 面向 VLA 闭环评测的分块世界模型 PiL-World，交替 VLA 推理与多视角未来观测生成；作者报告在三个双臂真机任务上将真机与想象评测的成功率误差从 63.2%（Ctrl-World）降到 12.0%。 · [📝 review](digests/migration-2026-10-22.md)

- **[DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation](https://arxiv.org/abs/2608.20114)** — *Ma, Siyuan et al.* · `2026-08-20` · `53/100`（C3·E4·O1·T3）
  > DECOWAM 在冻结的 FastWAM 上加入残差适配器、未来信息瓶颈、底盘/机械臂解耦潜变量与底盘速度条件，作者报告在自建 ARMDOG 回放上动作 MSE 降 21.7%，79 次真机试验中全身协调性最好。 · [🌐 project](https://humanoidtennis.github.io/AdaPT/) · [📝 review](digests/migration-2026-10-22.md)

- **[Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation](https://arxiv.org/abs/2606.18960)** — *Zheng, Zirui et al.* · `2026-06-17` · 🏛️ **CoRL 2026** · `53/100`（C3·E4·O1·T3）
  > 以腕部视角 4D surfel 记忆按未来动作检索历史帧，增强多视角动作条件世界模型；作者报告策略评估与真机相关性比 Ctrl-World 高 14.5%，合成数据使长时程任务成功率 58%→72%。 · [📝 review](digests/migration-2026-10-22.md)

- **[Discrete-WAM: Unified Discrete Vision-Action Token Editing for World-Policy Learning](https://arxiv.org/abs/2606.05645)** — *Yao, Ziyang et al.* · `2026-06-04` · `53/100`（C3·E4·O1·T3）
  > 自动驾驶世界-策略统一模型 Discrete-WAM：视觉、决策与加速度动作共享离散 token 空间，层级决策+并行 token 编辑规划；作者报告 NAVSIM v2 EPDMS 90.4、v1 PDMS 92.2，生成 FVD 80.0。 · [📝 review](digests/migration-2026-10-22.md)

- **[GeoSem-WAM: Geometry- and Semantic-Aware World Action Models](https://arxiv.org/abs/2606.03188)** — *Ma, Fulong et al.* · `2026-06-02` · `53/100`（C3·E4·O1·T3）
  > GeoSem-WAM 在 Fast-WAM 训练中加入未来几何与语义预测辅助头、推理时丢弃；作者报告 LIBERO 98.55%、RoboTwin 2.0 92.52%，Franka 真机平均 88.9%→95.4%。 · [📝 review](digests/migration-2026-10-22.md)

- **[ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models](https://arxiv.org/abs/2608.13438)** — *Zheng, Gehan et al.* · `2026-08-13` · `51/100`（C3·E3·O1·T4） · 🧩 *adjacent*
  > ContactGuard 用多视角动作条件潜在世界模型在夹爪闭合前推演策略动作块的后果，以线性探针判断是否中止；作者报告在四个真机抓取场景中优于单视角、当前状态和 FAIL-Detect 等失败检测基线。 · [📝 review](digests/migration-2026-10-22.md)

- **[Toward the Cognitive--Physical Limits of Embodied Intelligence through a World-Model-Centric Autonomous Racing Agent](https://arxiv.org/abs/2608.10618)** — *Shan, Zitong et al.* · `2026-08-11` · `51/100`（C3·E3·O1·T4）
  > 以世界模型为中心的自动驾驶赛车智能体，从接近极限的成功与失败数据中学习交互演化和动力学边界；作者报告真车定位感知在 256.3 km/h 下稳定，仿真对抗场景交互成功率为 88.3%。 · [📝 review](digests/migration-2026-10-22.md)

- **[Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control](https://arxiv.org/abs/2607.25337)** — *Bai, Jiaxin et al.* · `2026-07-28` · `51/100`（C3·E3·O2·T2）
  > 在 LeWM 的 JEPA 骨干上从无奖励示范中挖掘有向时序代价用于潜空间 MPC；作者报告 Two-Room 成功率 100%（LeWM 97.4%），OGB-Cube 提升 14.2 个百分点，四个环境均不低于 LeWM 与 RC-aux。 · [🌐 project](https://arxiv.org/abs/2607.26037) · [📝 review](digests/migration-2026-10-22.md)

- **[CLAW: Learning Continuous Latent Action World Models via Adversarial Latent Regularization](https://arxiv.org/abs/2606.04130)** — *Ayalew, Tewodros et al.* · `2026-06-02` · `51/100`（C3·E3·O1·T4）
  > CLAW 从无动作标注视频端到端联合学习连续潜动作与扩散世界模型，用梯度反转的对抗正则防止未来信息泄漏；作者报告在 VP2 六任务中四项、Crafter/Procgen 四任务中三项规划成功率最高，并用于真机 UR5 策略预训练。 · [📝 review](digests/migration-2026-10-22.md)

- **[One Future, Every Robot: Label-Efficient Collective-State Prediction with Decentralized JEPA](https://arxiv.org/abs/2607.28443)** — *Gazzaev, Alan-Barsag et al.* · `2026-07-30` · `48/100`（C3·E3·O1·T3）
  > CS-JEPA 让每台机器人仅凭本地历史与邻居消息预测同一潜空间集体未来，无一致性损失；作者报告仿真中集体状态误差较重建基线降 28.4%，拓扑/规模迁移下降 64–76%。 · [🌐 project](https://arxiv.org/abs/2607.23782) · [📝 review](digests/migration-2026-10-22.md)

- **[WAM-RL: World-Action Model Reinforcement Learning with Reconstruction Rewards and Online Video SFT](https://arxiv.org/abs/2606.17906)** — *Qian, Zezhong et al.* · `2026-06-16` · `46/100`（C3·E2·O1·T4）
  > 在 Genie Envisioner-ACT 上对世界模型做在线视频 SFT（KL 约束）、对动作头用重建奖励做 RL；作者报告 LIBERO-Object 成功率 68%→82%，RLBench Water Plants 19%→22%。 · [🌐 project](https://cvlab-kaist.github.io/Geometric-Action-Model) · [📝 review](digests/migration-2026-10-22.md)

- **[WorldDiT: A Unified Diffusion Architecture for World and Action Modeling](https://arxiv.org/abs/2607.23909)** — *Wang, Sen et al.* · `2026-07-27` · `37/100`（C2·E2·O1·T3）
  > 单个 DiT 同时以流匹配生成动作块并预测未来 RGB patch（仅训练期辅助），不用大 VLM 骨干；作者报告 399M 参数在 LIBERO 四套件平均 94.9%，位于参数-成功率帕累托前沿。 · [🌐 project](https://arxiv.org/abs/2607.23909) · [📝 review](digests/migration-2026-10-22.md)

</details>

<details>
<summary>📜 <b>Classic landmarks / 经典奠基</b> · 1 paper</summary>

- 📜 **[Cosmos World Foundation Model Platform for Physical AI](https://arxiv.org/abs/2501.03575)** — *NVIDIA* · `2025-01-07` · `89/100`（C5·E4·O4·T5） · 💻
  > NVIDIA 开放的世界基础模型平台：视频数据筛选管线、因果视频 tokenizer、扩散与自回归预训练 WFM 及后训练示例，权重以宽松许可发布。 · [🌐 project](https://www.nvidia.com/en-us/ai/cosmos/) · [💻 code](https://github.com/nvidia-cosmos/cosmos-predict1) · [📝 review](digests/migration-2026-10-22.md)

</details>


### Other Generalist Models · 8

<details open>
<summary>🔥 <b>Must-read & notable / 重点与值得关注</b> · 5 papers</summary>

- 🔥 **[GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601)** — *Qize Yu et al.* · `2026-09-30` · `80/100`（C4·E4·O4·T4） · 💻
  > GroundingPI 是 4B 接地基础模型，34 个基准平均 73.68%；作为 VLA 视觉骨干，作者报告 RoboTwin 2.0 四个 OOD 设置全胜、RoboCasa-GR1 用 50% 演示超过基线 75%。 · [🌐 project](https://groundingpi.github.io/) · [💻 code](https://github.com/groundingpi/GroundingPI) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[Grounded Action Model: 3D Grounding as a Foundation for Robotics](https://arxiv.org/abs/2609.23863)** — *Gehao Zhang et al.* · `2026-09-20` · `80/100`（C4·E4·O4·T4） · 💻
  > GAM 以可提示 3D 接地模型为骨干、只用任务物体构建观测；作者报告 RoboTwin 2.0 平均 55.3%、LIBERO-PRO 61%，真机视觉偏移下 17/20 对 π0.5 的 4/20。 · [🌐 project](https://grounded-action-model.github.io/) · [💻 code](https://github.com/GehaoZhang6/Grounded-Action-Model) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance](https://arxiv.org/abs/2608.09853)** — *Huang, Dongchi et al.* · `2026-08-10` · `80/100`（C4·E4·O4·T4） · 💻
  > RynnValue 以“到目标的时间距离”为监督，在 7000+ 小时异构数据上训练价值基础模型，作者报告 RBM-EVAL-OOD 上 Kendall τ 为 0.704，并在真机 RL、数据筛选和推理引导中带来提升。 · [🌐 project](https://alibaba-damo-academy.github.io/RynnValue.github.io) · [💻 code](https://github.com/alibaba-damo-academy/RynnValue) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[EgoXperience: Learning World-Grounded Egocentric Representations from Human Experience](https://arxiv.org/abs/2610.26625)** — *Xinhao Ji et al.* · `2026-10-19` · `68/100`（C4·E4·O2·T4） · 📄
  > EgoXperience 构建 50 小时自我中心数据 EgoX-Data-6M 与基准 EgoX-Bench，EgoX 单次前向联合重建相机、深度、双手与物体 6DoF；作者报告 EgoX-Bench 手部误差降至 113.24 mm。 · [🌐 project](https://ropedia.github.io/EgoXperience) · [📝 review](digests/daily/2026-10-22.md)

- 👀 **[PhysBrain 1.5: From Vision-Language Models to Physical Foundation Models](https://arxiv.org/abs/2609.14973)** — *DeepCybo Team et al.* · `2026-09-14` · `66/100`（C4·E3·O3·T3） · 🟡
  > PhysBrain 1.5 在 Qwen3-VL 上把语言、末端轨迹与未来 RGB/深度/机器人掩码统一为离散 token 联合自回归训练，8B 模型在 28 个具身理解基准上平均 72.5，为开源最高。 · [🌐 project](https://deepcybo-physai.github.io/PhysBrain-1.5/) · [💻 code](https://github.com/DeepCybo-PhysAI/PhysBrain-1.5) · [📝 review](digests/daily/2026-10-22.md)

</details>

<details>
<summary>📋 <b>Also tracked / 观察中与暂不评级</b> · 3 papers</summary>

- **[Orca: The World is in Your Mind](https://arxiv.org/abs/2606.30534)** — *Wang, Yihao et al.* · `2026-06-29` · `63/100`（C3·E3·O3·T4） · 🟡
  > BAAI 提出以“下一状态预测”学习统一世界隐空间的 Orca，用 12.5 万小时视频与 1.6 亿事件标注预训练；冻结主干后接文本、图像、动作读出头，作者报告优于同规模基线。 · [🌐 project](https://orca-wm.github.io/) · [💻 code](https://github.com/orca-wm/Orca) · [📝 review](digests/migration-2026-10-22.md)

- **[HumanScale: Egocentric Human Video Can Outperform Real-Robot Data for Embodied Pretraining](https://arxiv.org/abs/2606.20521)** — *Ma, Juncheng et al.* · `2026-06-18` · `63/100`（C4·E3·O2·T4） · 📄 · 🧩 *adjacent*
  > 在 5000 小时等规模下比较第一视角人类视频与遥操作机器人数据做 WAM 预训练；作者报告人类视频在未见任务上动作验证损失约低 20%，且随规模对数线性下降。 · [📝 review](digests/migration-2026-10-22.md)

- **[Self-Evolving Embodied Agents via Skill-Harness Evolution](https://arxiv.org/abs/2608.11350)** — *Wang, Peidong et al.* · `2026-08-11` · `51/100`（C3·E3·O1·T4）
  > SHAPER 冻结规划器与执行器参数，只用少量 rollout 演化文本技能与上下文构造代码；作者报告 VLABench 自建四个划分平均成功率从 28.25% 升至 34.50%，ESI-Bench 子集准确率从 32.5% 升至 49.8%。 · [📝 review](digests/migration-2026-10-22.md)

</details>


<sub>[⬆ back to top](#contents)</sub>

## <a id="manipulation"></a>🦾 Manipulation

*Grasping, dexterous, bimanual manipulation*
<details open>
<summary>🔥 <b>Must-read & notable / 重点与值得关注</b> · 11 papers</summary>

- 🔥 **[HumanoidToolBench: Benchmarking Humanoid Tool Use from Selection to Mobile Execution](https://arxiv.org/abs/2610.02089)** — *Kyochul Jang et al.* · `2026-10-01` · `86/100`（C4·E4·O5·T4） · 💻 · 🧩 *adjacent*
  > 发布 HumanoidToolBench：18 个人形工具使用任务（3 场景×3 执行层级×2 工具集模式）与 3.1k 条仿真/真机 G1 示教；7 个策略仿真、3 个真机评测，移动使用阶段成功率大幅下降。 · [🌐 project](https://snu-pi.github.io/HumanoidToolBench/) · [💻 code](https://github.com/SNU-PI/HumanoidToolBench) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[RoboTok: A Scalable Data Engine for Internet Demonstration Video Retrieval and Dexterous Manipulation Learning](https://arxiv.org/abs/2609.03199)** — *Howard Qian et al.* · `2026-09-02` · `80/100`（C4·E4·O4·T4） · 💻 · 🧩 *adjacent*
  > RoboTok 以躯干中心 3D 手轨迹学习运动嵌入，从网络视频检索演示；作者报告真机灵巧操作平均成功率比最强基线高 42.2 个百分点。 · [🌐 project](https://rice-robotpi-lab.github.io/RoboTok/) · [💻 code](https://github.com/Rice-RobotPI-Lab/RoboTok-Code) · [📝 review](digests/daily/2026-10-22.md)

- 👀 **[SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deformable-Object Manipulation](https://arxiv.org/abs/2608.18701)** — *Jing, Bowen et al.* · `2026-08-19` · `72/100`（C4·E3·O4·T3） · 💻 · 🧩 *adjacent*
  > 可变形物体视触觉仿真数据集与基准（4000条示范、50+资产），提出形变感知成功率DSR；作者报告12个分布内配置中均存在完成任务但超形变容限的成功回合。 · [💻 code](https://github.com/TuojingAI/SoftVTBench) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[MotorMind: Scaffolding General Vision Language Models for Zero-Shot Robot Manipulation](https://arxiv.org/abs/2609.38078)** — *Bingxuan Li et al.* · `2026-09-29` · `71/100`（C4·E4·O3·T3） · 💻
  > MotorMind 让冻结通用 VLM 经中层级动作与异步监控直接控制机器人；作者报告 LIBERO-PRO 基础 66.7%、扰动 53.8%，真机 xArm6 平均 95%。 · [🌐 project](https://motor-mind.github.io) · [💻 code](https://github.com/Motor-Mind/MotorMind-Code) · [📝 review](digests/daily/2026-10-22.md)

- 👀 **[TacPAC: Tactile Prediction and Real-Time Action Correction in World-Action Models for Contact-Rich Manipulation](https://arxiv.org/abs/2609.05266)** — *Ma, Zipei et al.* · `2026-09-04` · `71/100`（C4·E4·O3·T3） · 💻
  > TacPAC 在预测视觉与触觉的世界-动作模型上加入触觉专家，执行中将实时触觉与缓存的预期接触对照来修正剩余动作，作者报告五个真机接触密集任务平均成功率由 22% 升至 64%。 · [🌐 project](https://github.com/LogosRoboticsGroup/TacPAC) · [💻 code](https://github.com/LogosRoboticsGroup/TacPAC) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[Robots Acquire Manipulation Skills in Seconds from a Single Human Video](https://arxiv.org/abs/2607.20033)** — *Chen, Guangyan et al.* · `2026-07-22` · `71/100`（C4·E4·O3·T3） · 💻
  > HOST 推理时从单条人类视频获得新操作技能、无需参数更新；作者报告 50 个新任务平均约 29 秒习得、成功率 62%，高于用 50 条示教微调的 Wall-OSS（56%）且不遗忘旧技能。 · [🌐 project](https://arxiv.org/abs/2607.20033) · [💻 code](https://github.com/CGuangyan-BIT/HOST) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[Learning from Fleet Experience: Collective Experience Learning Across 96 Robots](https://arxiv.org/abs/2610.25736)** — *Chao Yu et al.* · `2026-10-19` · `68/100`（C4·E4·O2·T4） · 🟡
  > 用机队部署经验替代专家纠正：FERT 从成功轨迹检索与失败相关的片段，96 台真机 5 个任务达 93.3–99.2% 成功率。 · [🌐 project](https://cel-robot-learning.github.io) · [💻 code](https://github.com/RLinf/RLinf) · [📝 review](digests/daily/2026-10-22.md)

- 👀 **[Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data](https://arxiv.org/abs/2608.02580)** — *Wang, Ye et al.* · `2026-08-03` · `68/100`（C4·E4·O2·T4） · 🧩 *adjacent*
  > 将第一人称人手操作视频经动作重定向、机械臂渲染替换与多级筛选转为 15 种机械臂数据，共 18,561 小时；作者报告与真机数据 1:1 联合预训练提升 RoboTwin 扰动泛化与真机表现。 · [🌐 project](https://arxiv.org/abs/2608.02580) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[Pre-training Visual Dexterity in Simulation](https://arxiv.org/abs/2608.15917)** — *Kamat, Sarthak et al.* · `2026-08-16` · `66/100`（C4·E3·O2·T5）
  > SPD 用 VR 在 MuJoCo 中遥操作采集 75 小时双手灵巧操作数据预训练扩散 Transformer，再用 1–2 小时真机数据微调；作者报告在 5 项 56 自由度真机任务上均优于从零训练的 BC。 · [🌐 project](https://gigabrain0.github.io/) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[Real-World Cooperative Bimanual Dexterous Grasp of Large Objects from Single-View Observations](https://arxiv.org/abs/2608.10383)** — *Li, Ziming et al.* · `2026-08-11` · 🏛️ **IROS 2026** · `66/100`（C3·E3·O4·T3） · 💻
  > 用遥操作采集的真机多模态数据训练 DDPM，从单视角点云生成双臂灵巧手的抓取关节构型，再结合运动规划和力引导微调执行；作者报告在未见过的大物体上总成功率为 61.9%。 · [💻 code](https://github.com/zhangdana483/real_bi_dex_grasp) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[UniReflex: Plug-and-Play Force Control for Pretrained Generative Policies via Fast-Slow Reflex](https://arxiv.org/abs/2608.17432)** — *Huang, Yan et al.* · `2026-08-18` · `65/100`（C4·E4·O2·T3）
  > UniReflex 截取冻结生成式策略（DP、π0、DreamZero）动作头的隐表示，驱动快速反射网络输出变阻抗与参考力；作者报告在 5 项真机接触任务的接触阶段成功率提升 20–60 个百分点。 · [🌐 project](https://unireflex.github.io/) · [📝 review](digests/migration-2026-10-22.md)

</details>

<details>
<summary>📋 <b>Also tracked / 观察中与暂不评级</b> · 17 papers</summary>

- **[RoboEdit: Turning Human Manipulation Videos into Scalable Robot Experience](https://arxiv.org/abs/2608.18948)** — *Guo, Yaowei et al.* · `2026-08-19` · `63/100`（C4·E3·O2·T4） · 🧩 *adjacent*
  > 将人手操作视频编辑为多种机器人手的物理合理视频并解码3D手部状态，构建17.4万对、1410万帧配对数据集RoboEdit-14M；作者报告编辑质量优于8种视频编辑基线。 · [🌐 project](https://adept-dexterity.github.io/) · [📝 review](digests/migration-2026-10-22.md)

- **[Affordance2Action: Task-Conditioned Scene-level Affordance Grounding for Real-Time Manipulation](https://arxiv.org/abs/2606.04172)** — *Liu, Litao et al.* · `2026-06-02` · `62/100`（C3·E4·O2·T4） · 🧩 *adjacent*
  > 面向任务条件、场景级、一对多的部件 affordance 定位，构建 A2A-Bench 与智能体辅助标注流水线，并以 SAM3 适配的实时定位模型为扩散策略提供空间先验；TRPS 上作者报告 55.41 gIoU、约 9.7 FPS。 · [📝 review](digests/migration-2026-10-22.md)

- **[GOAG: Generative and Object-Agnostic Grasp Planner for Dexterous Robotic Manipulation](https://arxiv.org/abs/2608.19759)** — *Merand, Julien et al.* · `2026-08-20` · 🏛️ **IROS 2026** · `60/100`（C3·E3·O3·T3） · 💻
  > 训练时只用夹爪自身几何与抓取分类学学习接触分布的CVAE抓取规划器，推理时才引入物体；作者报告MultiDex三种灵巧手平均成功率86.93%，且无需物体抓取数据。 · [🌐 project](https://cea-list.github.io/goagweb/) · [💻 code](https://github.com/CEA-LIST/GOAG) · [📝 review](digests/migration-2026-10-22.md)

- **[CoToGrasp: Contact-Topology-Conditioned Dexterous Grasp Synthesis via Canonical Workspace Learning](https://arxiv.org/abs/2608.19776)** — *Merand, Julien et al.* · `2026-08-20` · 🏛️ **ECCV 2026** · `60/100`（C3·E3·O3·T3） · 💻
  > 以21种接触拓扑模板为条件、在夹爪规范工作空间中物体无关训练的灵巧抓取生成器；作者报告在DexGraspNet上稳定性与拓扑符合度优于分类学感知基线Dexonomy。 · [🌐 project](https://cea-list.github.io/goagweb/) · [💻 code](https://github.com/CEA-LIST/CoToGrasp) · [📝 review](digests/migration-2026-10-22.md)

- **[PRISM: Precision and contact-rich Real-world Industrial Skill dataset with Multimodal sensing](https://arxiv.org/abs/2608.17962)** — *Yu, Tengbo et al.* · `2026-08-18` · `60/100`（C3·E3·O3·T3） · 📄 · 🧩 *adjacent*
  > 面向工业精密装配的多模态接触丰富操作数据集：25+任务、5000+条遥操作轨迹（45小时），同步RGB-D、力/力矩、触觉与本体状态，覆盖3种机器人与3种遥操作方式。 · [🌐 project](https://unireflex.github.io/) · [📝 review](digests/migration-2026-10-22.md)

- **[PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration](https://arxiv.org/abs/2608.21031)** — *Lin, Chen-Yu et al.* · `2026-08-21` · `57/100`（C3·E3·O2·T4）
  > PhysCaP 为代码即策略智能体加入由关节力矩与夹爪形变估计质量、刚度的模块及规划/排序双智能体，作者报告在三个真机任务和 LIBERO 中以更少交互与更短时间达到相当或更高成功率。 · [🌐 project](https://physcap.github.io) · [📝 review](digests/migration-2026-10-22.md)

- **[DexFuture: Hierarchical Future-State Visuomotor Targeting for Bimanual Dexterous Tool Use](https://arxiv.org/abs/2606.05699)** — *Li, Runfa Blark et al.* · `2026-06-04` · `57/100`（C3·E3·O2·T4）
  > 高层从视觉-本体历史预测未来手-工具-物体目标轨迹，低层目标条件策略高频跟踪；作者报告 OakInk2 双手工具任务上达到特权目标策略约 90% 表现，比 DexWM 式 CEM 规划快约 250 倍。 · [📝 review](digests/migration-2026-10-22.md)

- **[Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum](https://arxiv.org/abs/2605.21133)** — *Liang, Zhizhao et al.* · `2026-05-20` · `57/100`（C3·E3·O2·T4）
  > 以 VLM 驱动的“主动空间大脑”负责主动视角感知与任务分解、多智能体“动作小脑”生成全身动作，无需任务真机数据；作者报告 G1 人形五类空间操作困难设定成功率 55–70%，高于 TrajBooster、CaP 等基线。 · [📝 review](digests/migration-2026-10-22.md)

- **[H2R-Grounder: A Paired-Data-Free Paradigm for Translating Human Interaction Videos into Physically Grounded Robot Videos](https://arxiv.org/abs/2512.09406)** — *Ci, Hai et al.* · `2025-12-10` · `57/100`（C3·E3·O2·T4） · 📄 · 🧩 *adjacent*
  > H2R-Grounder 将机械臂从机器人视频中抹除并叠加夹爪位姿标记，微调 Wan2.2 学会"放回"机械臂，测试时把人手视频转成机器人视频，无需配对数据；作者报告在 DexYCB 人评中多数维度优于基线。 · [🌐 project](https://showlab.github.io/H2R-Grounder/) · [📝 review](digests/migration-2026-10-22.md)

- **[Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents](https://arxiv.org/abs/2606.23085)** — *Zhang, Haoran et al.* · `2026-06-22` · `56/100`（C3·E4·O1·T4） · 🧩 *adjacent*
  > 用 V-JEPA 2-AC 动作条件预测潜变量+因果 Transformer 做长时程操作失败检测，仅需轨迹级成败标签并用函数型共形预测定阈；作者报告 BEHAVIOR-1K 上 ROC-AUC 0.76、平衡准确率 0.78。 · [🌐 project](https://haoranzhangumich.github.io/Forsight_web/) · [📝 review](digests/migration-2026-10-22.md)

- **[LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories](https://arxiv.org/abs/2608.18618)** — *Tang, Zhipeng et al.* · `2026-08-19` · `54/100`（C3·E3·O2·T3） · 🧩 *adjacent*
  > 化学实验室灵巧操作的分层真机+仿真基准，含原子技能、组合技能与长时程流程三级；作者报告π0.5原子技能最佳，但三种策略均无法完成完整实验流程。 · [🌐 project](https://shepherd1226.github.io/gigabrain-wbc-0.5/) · [📝 review](digests/migration-2026-10-22.md)

- **[PartialBiGrasp: Inferring Hidden Local Geometry for Bimanual Grasping from Partial Views](https://arxiv.org/abs/2608.19188)** — *Kaura, Ayush et al.* · `2026-08-19` · `54/100`（C3·E3·O2·T3）
  > 从单视角部分点云生成力封闭双臂抓取对，用卷积占据网络推断隐藏局部几何并做占据引导细化；作者报告DG16M测试集力封闭率55.2%，显著高于各基线。 · [📝 review](digests/migration-2026-10-22.md)

- **[HiTac-WAM: A Hierarchical Tactile World Action Model for Contact-Rich Robot Manipulation](https://arxiv.org/abs/2608.19574)** — *Xue, Chao et al.* · `2026-08-20` · `53/100`（C3·E4·O1·T3）
  > 为世界动作模型的每个候选动作块预测接触→形变→滑移的分层触觉未来，用于候选排序与执行中偏差重规划；作者报告三项真机任务平均成功率由31.1%升至72.2%。 · [🌐 project](https://carldegio.github.io/latent_action.github.io) · [📝 review](digests/migration-2026-10-22.md)

- **[Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation](https://arxiv.org/abs/2605.21811)** — *Wu, Albert et al.* · `2026-05-20` · `51/100`（C3·E3·O1·T4）
  > SafePBDS 用 pullback 控制屏障函数把任务流形安全约束转为构型空间加速度线性约束，并提供残差动作接口；作者报告 Franka-Allegro 真机抓取成功率 92.5%，手内旋转超 360°。 · [📝 review](digests/migration-2026-10-22.md)

- **[Throwing a Tight Spiral American Football by a Humanoid Robot](https://arxiv.org/abs/2608.16642)** — *Mahboob, Zaid et al.* · `2026-08-17` · 🏛️ **Humanoids 2026** · `43/100`（C3·E2·O1·T3）
  > 首次让 Unitree G1 人形机器人投出旋转稳定的橄榄球螺旋传球：轨迹优化完成投掷段，查表式 MPC 调控手指释放段，作者报告旋转效率最高 93.6%。 · [📝 review](digests/migration-2026-10-22.md)

- **[EaDex: A Cross-Embodiment Dexterous Manipulation Framework from Low-Cost Demonstrations](https://arxiv.org/abs/2606.03268)** — *Zhao, Qian et al.* · `2026-06-02` · `37/100`（C2·E2·O1·T3）
  > EaDex 用单个 RGB-D 相机采集人手示范、经 MANO 拟合与重定向生成跨灵巧手示范，并按接触奖励动态退火示范权重；作者报告 3 种灵巧手×3 个铰接物体仿真平均成功率 23.5%→36.5%。 · [📝 review](digests/migration-2026-10-22.md)

- **[Attention from Action, for Action: Emergent Visual Bottlenecks for Policy Learning](https://arxiv.org/abs/2608.13422)** — *Zhuang, Zheyu et al.* · `2026-08-13` · 🏛️ **CoRL 2026** · 💻
  > Seeker 仅用动作监督从冻结 DINOv3 特征中学出随任务进度变化的关注区域，用于裁剪、背景增强与点云过滤，作者报告真机平均成功率由最佳基线 48.3% 提升到 76.7%。 · [🌐 project](http://koalagripper.rai-inst.com) · [💻 code](https://github.com/zheyu-zhuang/seeker) · [📝 review](digests/migration-2026-10-22.md)

</details>

<details>
<summary>📜 <b>Classic landmarks / 经典奠基</b> · 1 paper</summary>

- 📜 **[ALOHA Unleashed: A Simple Recipe for Robot Dexterity](https://arxiv.org/abs/2410.13126)** — *Zhao et al.* · `2024-10-17` · `65/100`（C4·E4·O1·T5）
  > 在 ALOHA 2 上采集 2.6 万条示范并训练 Transformer 扩散策略，首次端到端完成系鞋带、挂衬衫等灵巧双臂任务；作者报告扩散损失明显优于 ACT 式 L1 回归。 · [🌐 project](https://aloha-unleashed.github.io) · [📝 review](digests/migration-2026-10-22.md)

</details>


<sub>[⬆ back to top](#contents)</sub>

## <a id="locomotion"></a>🦿 Locomotion

*Humanoid, quadruped, bipedal walking and running*
<details open>
<summary>🔥 <b>Must-read & notable / 重点与值得关注</b> · 8 papers</summary>

- 🔥 **[GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](https://arxiv.org/abs/2606.05160)** — *Xie, Tianyi et al.* · `2026-06-03` · `83/100`（C4·E4·O4·T5） · 💻 · 🧩 *adjacent*
  > 在已知几何与尺度的 3D 场景中用视频基础模型生成人-物交互、再做度量 4D 重建并重定向到人形的全虚拟数据流水线 GRAIL；生成 2 万+序列，仅用其数据训练的 G1 真机拾取 84%、爬楼 90%。 · [🌐 project](https://research.nvidia.com/labs/dair/grail/) · [💻 code](https://github.com/NVlabs/GRAIL) · [📝 review](digests/migration-2026-10-22.md)

- 🔥 **[Reflex: Visually Grounded Reactive Humanoid Control](https://arxiv.org/abs/2610.12772)** — *Taoyang Jia et al.* · `2026-10-08` · `80/100`（C4·E4·O4·T4） · 💻
  > 三阶段训练的人形全身接箱框架：仿真第一视角 RGB-D 抓接成功率 85.7%，Unitree G1 真机 2.5 m/5 m 处达 65%/40%。 · [🌐 project](https://toberj.github.io/reflex/) · [💻 code](https://github.com/ToberJ/reflex) · [📝 review](digests/daily/2026-10-22.md)

- 👀 **[HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers](https://arxiv.org/abs/2606.06493)** — *Yang, Lizhi et al.* · `2026-06-04` · `74/100`（C4·E4·O3·T4） · 💻
  > 把动作跟踪、行走、摔倒恢复三个教师按动作切片与上下文蒸馏进单个 MoE 学生，以 10 维任务空间指令驱动 29 自由度 G1；作者报告匹配对比中鲁棒工作空间最大并完成 VLM 驱动的真机移动操作。 · [💻 code](https://github.com/lzyang2000/HANDOFF) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking](https://arxiv.org/abs/2606.03985)** — *Qi, Zekun et al.* · `2026-06-02` · 🏛️ **CVPR 2026** · `74/100`（C4·E4·O3·T4） · 🟡
  > Humanoid-GPT 把约 300 个 PPO 专家蒸馏进因果 Transformer，基于 20 亿帧动作语料做人形零样本全身跟踪；作者报告 AMASS 测试成功率随规模升至 92.6%，G1 真机零样本跟踪舞蹈。 · [🌐 project](https://qizekun.github.io/humanoid-gpt/) · [💻 code](https://github.com/GalaxyGeneralRobotics/Humanoid-GPT) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[LadderMan: Learning Humanoid Perceptive Ladder Climbing](https://arxiv.org/abs/2606.05873)** — *Zhao, Siheng et al.* · `2026-06-04` · `71/100`（C4·E4·O2·T5）
  > 人形感知爬梯系统 LadderMan：单条动捕参考经混合运动跟踪学多个爬梯专家，再以 DAgger+RL 蒸馏为深度视觉策略，借立体深度基础模型零样本上真机；G1 在三种真实梯子上爬梯并可在梯上遥操作作业。 · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[Towards a General Humanoid Loco-Manipulation Model via Egocentric Whole-Body Human Data Pretraining](https://arxiv.org/abs/2610.00438)** — *Chongyang Xu et al.* · `2026-09-30` · `68/100`（C4·E4·O2·T4）
  > 用 500 小时第一视角人体全身运动数据 HumanVerse-500 做三阶段预训练得到人形全身 VLA λ0；SIMPLE 六任务报告 90.0% 成功率，4 个真机任务平均 62.5%。 · [📝 review](digests/daily/2026-10-22.md)

- 👀 **[GigaBrain-WBC-0.5: A Behavior World Model for Robust Whole-Body Control with Environment Interaction](https://arxiv.org/abs/2608.18234)** — *Cheng, Ziyang et al.* · `2026-08-18` · `65/100`（C4·E4·O2·T3）
  > 行为世界模型式人形全身跟踪控制器，联合预测动作、下一状态与行为分布；作者报告地形交互成功率81.3%（最佳基线4.3倍）、摔倒恢复率99.3%。 · [🌐 project](https://adept-dexterity.github.io/) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking](https://arxiv.org/abs/2606.04829)** — *Lu, Zuxing et al.* · `2026-06-03` · `65/100`（C3·E4·O3·T3） · 💻
  > 用模态专属编码器把机器人关节角、人体姿态、末端位姿映射到共享潜空间，单阶段 RL 训练一个人形全身控制器 M3imic；作者报告在未见 OMOMO 测试集上末端模态成功率 98.42%，并在 G1 上真机验证。 · [💻 code](https://github.com/Renforce-Dynamics/MultiModalWBC) · [📝 review](digests/migration-2026-10-22.md)

</details>

<details>
<summary>📋 <b>Also tracked / 观察中与暂不评级</b> · 12 papers</summary>

- **[TAGA: Terrain-aware Active Gaze Learning for Generalizable Agile Humanoid Locomotion](https://arxiv.org/abs/2606.05880)** — *Li, Peizhuo et al.* · `2026-06-04` · `62/100`（C3·E4·O2·T4）
  > 人形主动“注视”感知行走框架 TAGA：用深度图与本体感知预测高度图中的关注区域并裁剪编码，经 RL 自然涌现注视行为；作者报告 G1 真机跨越 1.2 m 沟壑并通过稀疏落脚点。 · [📝 review](digests/migration-2026-10-22.md)

- **[StairMaster: Learning to Conquer Risky Hollow Stairs for Agile Quadrupedal Robots](https://arxiv.org/abs/2606.25765)** — *Tang, Xincheng et al.* · `2026-06-24` · `59/100`（C3·E4·O2·T3）
  > 三阶段强化学习框架 StairMaster 结合交叉注意力视觉编码、空间感知循环记忆与深度噪声建模；作者报告 Unitree Go2 零样本迁移后在 37°/55° 镂空楼梯真机成功率 93.3%/63.3%。 · [📝 review](digests/migration-2026-10-22.md)

- **[SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour](https://arxiv.org/abs/2606.19928)** — *Lan, Kaixin et al.* · `2026-06-18` · `59/100`（C4·E4·O1·T3）
  > 把左右镜像等变性硬嵌入 RSSM 世界模型与 actor-critic，用于四足跑酷；作者报告真机跨越 2.13 m 间隙、攀上 1.63 m 平台，并对镜像地形零样本泛化。 · [📝 review](digests/migration-2026-10-22.md)

- **[MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.06139)** — *Taouil, Ilyass et al.* · `2026-06-04` · `57/100`（C4·E3·O1·T4）
  > 不依赖遥操作或人类动作重定向，用 LLM 引导的进化程序搜索接触序列、配合分层运动学/动力学轨迹优化，发现长时程人形 loco-manipulation 动作，并经 RL 跟踪策略零样本部署到真机。 · [📝 review](digests/migration-2026-10-22.md)

- **[Tac4Loco: Learning Spatiotemporal Plantar Pressure Representations for Humanoid Locomotion](https://arxiv.org/abs/2608.15766)** — *Liu, Ziyun et al.* · `2026-08-16` · `54/100`（C3·E3·O2·T3）
  > Tac4Loco 把每只脚 60 单元的足底压力阵列量化为保拓扑的序数表示，经时空双分支编码后输入人形机器人行走策略；作者报告仿真坡面存活率从 22.0% 升至 77.9%，并在 G1 真机零样本走过泡沫平台与碎石路。 · [📝 review](digests/migration-2026-10-22.md)

- **[CoRe-MoE: Contrastive Reweighted Mixture of Experts for Multi-Terrain Humanoid Locomotion with Gait Adaptation](https://arxiv.org/abs/2606.04718)** — *Huang, Kailun et al.* · `2026-06-03` · `54/100`（C3·E3·O2·T3）
  > 两阶段 RL 框架 CoRe-MoE：先用双 AMP 专家学走跑平滑切换，再加以 SwAV 对比学习训练门控的深度感知 MoE 残差分支适应多地形，作者报告 Unitree G1 零样本部署走跑过台阶、坡道、障碍。 · [📝 review](digests/migration-2026-10-22.md)

- **[MILD: Tractable Terrain Modeling for Learning Improved Bipedal Locomotion on Deformable Surfaces](https://arxiv.org/abs/2608.19955)** — *Luo, Zeren et al.* · `2026-08-20` · 🏛️ **RA-L** · `53/100`（C3·E4·O1·T3）
  > MILD 用离散单元颗粒介质接触模型在仿真中刻画脚-软地非均匀交互并训练地形感知 RL 双足控制器，作者报告真机在泡沫、沙地等六类软地面上成功率与能效优于对比方法。 · [🌐 project](https://cea-list.github.io/cotograspweb/) · [📝 review](digests/migration-2026-10-22.md)

- **[SPRINT: Efficient Spectral Priors for Humanoid Athletic Sprints](https://arxiv.org/abs/2605.28549)** — *Wei, Yantong et al.* · `2026-05-27` · `53/100`（C3·E4·O1·T3）
  > SPRINT 仅用 5 段（14 秒）人体步态训练频率自适应谱先验，生成参考关节轨迹再由残差 RL 稳定；作者报告 Unitree G1 零样本实机冲刺在 6 m/s 指令下实测约 5.9 m/s，并可平滑切换步态。 · [📝 review](digests/migration-2026-10-22.md)

- **[Robust Brachiation on a Life-Sized Dual-Arm Robot Using Waypoint-Guided Reinforcement Learning](https://arxiv.org/abs/2608.17320)** — *Iwata, Ayumu et al.* · `2026-08-18` · 🏛️ **IROS 2026** · `51/100`（C3·E3·O1·T4）
  > 提出路点引导强化学习 WGRL，用稀疏末端路点加任务成功与机械能奖励，在真人尺寸双臂机器人上零样本实现单杠悬臂摆荡移动，真机穿越 4 根横杆并出现失败后加大摆幅重试的恢复行为。 · [🌐 project](https://tengbo-yu.github.io/PRISM/) · [📝 review](digests/migration-2026-10-22.md)

- **[Imagine2Real: Towards Zero-shot Humanoid-Object Interaction via Video Generative Priors](https://arxiv.org/abs/2605.22272)** — *Chen, Jiahe et al.* · `2026-05-21` · `51/100`（C3·E3·O1·T4）
  > Imagine2Real 用视频生成模型合成人形-物体交互视频，提取机器人基座、双手与物体的稀疏 4D 关键点，在行为基础模型潜空间内跟踪；作者报告 MuJoCo 中搬箱成功率 82.65%，并在动捕环境下零样本实机演示。 · [📝 review](digests/migration-2026-10-22.md)

- **[DynaWM: Dynamics-Aware Distillation with World Model and Momentum Targets for Smooth Locomotion over Continuous Stairs](https://arxiv.org/abs/2606.24089)** — *Hou, Haidong et al.* · `2026-06-23` · 🏛️ **IROS 2026** · `48/100`（C3·E3·O1·T3）
  > 在并发师生框架中以世界模型状态预测正则教师编码器、以动量目标编码器稳定学生蒸馏，用于双足轮式机器人连续楼梯；作者报告 20 cm 宽台阶成功率 89.3%，CTS 等基线失败。 · [📝 review](digests/migration-2026-10-22.md)

- **[T-GMP: Terrain-conditioned Generative Motion Priors for Versatile and Natural Humanoid Locomotion](https://arxiv.org/abs/2606.06944)** — *Guo, Junhong et al.* · `2026-06-05` · `48/100`（C3·E3·O1·T3）
  > 用 CVAE 从少量地形配对的动捕-状态数据学习地形条件运动先验，并以地形条件判别器做对抗式 RL；作者报告七类地形通过率均高于 AMP 与纯 RL 基线，并在 Kuavo 人形真机上部署。 · [📝 review](digests/migration-2026-10-22.md)

</details>


<sub>[⬆ back to top](#contents)</sub>

## <a id="teleoperation"></a>🕹️ Teleoperation

*VR, wearable, and exoskeleton-based data collection*
<details open>
<summary>🔥 <b>Must-read & notable / 重点与值得关注</b> · 3 papers</summary>

- 🔥 **[RynnWorld-Teleop: An Action-Conditioned World Model for Digital Teleoperation](https://arxiv.org/abs/2607.06558)** — *Zhao, Haoyu et al.* · `2026-07-07` · `80/100`（C4·E4·O4·T4） · 💻 · 🧩 *adjacent*
  > 提出“数字遥操作”：操作者手部位姿流驱动机器人视角视频世界模型实时生成演示（单卡 H100 40+ FPS）；作者报告 300 条真机数据叠加 300 条生成数据后 π0.5 平均成功率由 82.9% 升至 89.3%。 · [💻 code](https://github.com/alibaba-damo-academy/RynnWorld-Teleop) · [📝 review](digests/migration-2026-10-22.md)

- 🔥 **[VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training](https://arxiv.org/abs/2606.04708)** — *Yang, Siyuan et al.* · `2026-06-03` · `80/100`（C4·E4·O4·T4） · 💻 · 🧩 *adjacent*
  > 针对 UMI 数据训练 VLA 的腕部鱼眼视觉失配与人采轨迹物理不可行两大问题，构建 800 万条 UMI-VQA、跨本体物理校验打分流水线与两阶段联合训练；作者报告 20 个真机任务上优于 π0.5 等基线。 · [💻 code](https://github.com/TeleHuman/umi-vista) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[ORCA: A Platform for Open-Source Dexterity Research](https://arxiv.org/abs/2606.14561)** — *Capuano, Francesco et al.* · `2026-06-12` · `67/100`（C3·E2·O5·T3） · 💻 · 🧩 *adjacent*
  > 围绕可 3D 打印的 17 自由度 Orcahand 发布控制、MuJoCo 仿真、消费级设备遥操作与重定向一体化软件栈，原生接入 LeRobot，全部 MIT 开源。 · [💻 code](https://github.com/orcahand/orca_core) · [📝 review](digests/migration-2026-10-22.md)

</details>

<details>
<summary>📋 <b>Also tracked / 观察中与暂不评级</b> · 5 papers</summary>

- **[MonoDuo: Using One Robot Arm to Learn Bimanual Policies](https://arxiv.org/abs/2605.29298)** — *Bajamahal, Sandeep et al.* · `2026-05-28` · 🏛️ **ICRA 2026** · `60/100`（C3·E3·O2·T5）
  > MonoDuo 用"单臂机器人+人手协作"采集双臂示范，经手部姿态估计、分割与修复合成目标双臂机器人数据；作者报告 UR5e 双臂零样本成功率最高 70%，加 25 条目标示范微调后较从零训练提升 65–70 个百分点。 · [📝 review](digests/migration-2026-10-22.md)

- **[HapTile: A Haptic-Informed Vision-Tactile-Language-Action Dataset for Contact-Rich Imitation Learning](https://arxiv.org/abs/2606.04825)** — *Alian, Amirhosein et al.* · `2026-06-03` · `58/100`（C3·E2·O3·T4） · 📄 · 🧩 *adjacent*
  > 带操作者触觉反馈的遥操作采集的视触觉语言动作数据集 HapTile：UR5e+双指尖视触觉传感器，38 任务 1726 条示范；Diffusion Policy 与 π0 基线显示触觉输入效果随任务而异。 · [📝 review](digests/migration-2026-10-22.md)

- **[Hand-in-the-Loop: Improving VLA Policies for Dexterous Manipulation via Seamless Hand-Arm Intervention](https://arxiv.org/abs/2605.15157)** — *Li, Zhuohang et al.* · `2026-05-14` · `57/100`（C3·E3·O2·T4） · 🧩 *adjacent*
  > HandITL 以介入时刻为锚的相对手部重定向和基于速度的手臂共享控制，消除灵巧手 VLA 人工介入时的“手势跳变”；作者报告介入抖动降低 99.8%，用其纠错数据微调后三项长程任务平均比遥操作数据高 19%。 · [📝 review](digests/migration-2026-10-22.md)

- **[NestDex: Nested Policy Learning with Copilot Assisted Teleoperation for Dexterous Manipulation](https://arxiv.org/abs/2608.13362)** — *Zhao, James et al.* · `2026-08-13` · `48/100`（C3·E3·O1·T3）
  > NestDex 让操作者只控制机械臂、用单自由度离合器调节学习到的手部技能，由视觉语言选择器切换技能来采集灵巧操作示范，再训练外层视觉运动策略；作者报告示范采集成功率与效率高于 AnyTeleop。 · [📝 review](digests/migration-2026-10-22.md)

- **[Koala Gripper: Co-designing Robotic Grippers and Data-Capture Devices for Scaling Dexterous Manipulation Learning](https://arxiv.org/abs/2608.20546)** — *Hajj-Ahmad, Amar et al.* · `2026-08-20` · `43/100`（C3·E2·O1·T3） · 🧩 *adjacent*
  > Koala 协同设计手持数采器与机器人三自由度夹爪（双拇指、低反射质量连杆），作者展示其可完成多类抓取与工具使用，并以手持与遥操作数据训练扩散策略在 FR3 上执行。 · [🌐 project](https://github.com/AMAP-ML/DreamX-Phi) · [📝 review](digests/migration-2026-10-22.md)

</details>

<details>
<summary>📜 <b>Classic landmarks / 经典奠基</b> · 2 papers</summary>

- 📜 **[OpenTeleVision: Open-source Immersive Teleoperation with Stereo Visual Feedback](https://arxiv.org/abs/2407.01512)** — *Cheng et al.* · `2024-07-01` · `75/100`（C4·E3·O4·T4） · 💻 · 🧩 *adjacent*
  > 基于 Apple Vision Pro 的沉浸式遥操作系统：机器人头部主动立体相机随操作者头部转动并回传立体视频；作者报告在 H1、GR-1 人形上采集数据训练的 ACT 策略完成 4 项长时程精细任务。 · [🌐 project](https://robot-tv.github.io) · [💻 code](https://github.com/OpenTeleVision/TeleVision) · [📝 review](digests/migration-2026-10-22.md)

- 📜 **[Mobile ALOHA: Learning Bimanual Mobile Manipulation](https://arxiv.org/abs/2401.02117)** — *Fu et al.* · `2024-01-04` · `83/100`（C4·E4·O4·T5） · 💻 · 🧩 *adjacent*
  > 低成本（<3.2 万美元）全身遥操作双臂移动操作平台，并与静态 ALOHA 数据协同训练；作者报告每任务 50 条示范时协同训练可将成功率最多提升 90 个百分点。 · [🌐 project](https://mobile-aloha.github.io) · [💻 code](https://github.com/MarkFzp/mobile-aloha) · [📝 review](digests/migration-2026-10-22.md)

</details>


<sub>[⬆ back to top](#contents)</sub>

## <a id="sim2real"></a>🌉 Sim-to-Real

*Domain randomization, sim-to-real transfer, deployment*
<details open>
<summary>🔥 <b>Must-read & notable / 重点与值得关注</b> · 4 papers</summary>

- 👀 **[Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking](https://arxiv.org/abs/2608.20087)** — *Huang, Tao et al.* · `2026-08-20` · `74/100`（C4·E4·O3·T4） · 💻
  > AdaPT 从转播视频学习纳达尔等职业网球风格，以速度自适应的规划-跟踪分层框架缩小 sim-to-real 差距，作者报告在 Unitree G1 真机多拍与发球上击球率高于 Vid2Player3D 等基线。 · [🌐 project](https://humanoidtennis.github.io/AdaPT/) · [💻 code](https://github.com/noitom-robotics/AdaPT) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[ADEPT: Accelerating Dexterity via Pre-Training and Post-Training using Reinforcement Learning](https://arxiv.org/abs/2608.19182)** — *Lee, Jayjun et al.* · `2026-08-19` · 🏛️ **CoRL 2026** · `71/100`（C4·E4·O2·T5）
  > 先在通用物体摆位任务上大规模RL预训练灵巧策略，再以BC蒸馏+评论家预热+保守PPO后训练下游任务，零样本迁移至Kuka-Allegro与Flexiv-Sharpa真机完成插孔等长时程任务。 · [🌐 project](https://adept-dexterity.github.io/) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[TAM: Torque Adaptation Module for Robust Motion Transfer in Manipulation](https://arxiv.org/abs/2606.06218)** — *Son, Dongwon et al.* · `2026-06-04` · 🏛️ **CoRL 2026** · `71/100`（C4·E4·O2·T5）
  > 在低层控制器与力矩接口之间插入只看本体历史的学习型残差力矩模块，纯仿真训练即可零样本上真机；作者报告在 Franka 上同一组权重改善 RL 推箱、BC 翻转与 MPC 平衡任务，优于在线辨识与 RMA。 · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[Mana: Dexterous Manipulation of Articulated Tools](https://arxiv.org/abs/2606.13677)** — *Yin, Zhao-Heng et al.* · `2026-06-11` · `66/100`（C4·E3·O2·T5）
  > 把灵巧铰接工具操作当作"动画"问题：程序化抓取关键帧+运动规划+RL 生成仿真数据训练点云扩散策略，作者报告四类工具零样本真机抓取与操作约 70% 成功。 · [📝 review](digests/migration-2026-10-22.md)

</details>

<details>
<summary>📋 <b>Also tracked / 观察中与暂不评级</b> · 5 papers</summary>

- **[RoboGesture: Real-Time Semantic-aligned Co-Speech Gestures Generation for Humanoid Interaction](https://arxiv.org/abs/2608.28693)** — *Wang, Zifan et al.* · `2026-08-27` · 🏛️ **ECCV 2026** · `63/100`（C3·E3·O3·T4） · 🟡
  > RoboGesture 结合 300 余类手势数据、分层语音-语义对齐器、流式流匹配动作生成与 MPC 安全过滤，作者报告在 BEAT 与 SemanticBEAT 上优于基线，并在 G1 真机实现实时语音交互手势。 · [🌐 project](https://RoboGesture.github.io) · [💻 code](https://github.com/GalaxyGeneralRobotics/RoboGesture) · [📝 review](digests/migration-2026-10-22.md)

- **[Tactile Sim2Real without Tactile Simulation via Bottlenecked Latent Reconstruction](https://arxiv.org/abs/2608.15897)** — *Yang, Fan et al.* · `2026-08-16` · `62/100`（C4·E4·O1·T4）
  > SBLR 在仿真中用点云加指尖力的"神谕传感器"训练策略，用整流流网络在潜空间对齐真实触觉，并以瓶颈重建适应信息损失；作者报告 GelSight Mini 与 DIGIT 真机零样本成功率 85%–97.5%，高于物理触觉仿真基线 7.5–15 个百分点。 · [📝 review](digests/migration-2026-10-22.md)

- **[Video2Sim2Real: Full-Stack Autonomous Dexterous Skill Acquisition from a Single Human Video](https://arxiv.org/abs/2606.08828)** — *Han, Yunhai et al.* · `2026-06-07` · `62/100`（C3·E4·O2·T4）
  > 从单段人类 RGB-D 视频重建数字孪生、以物体中心关键帧优化重定向轨迹，再用 IL 校准感知误差与残差 RL 微调手指；作者报告 7 个真机灵巧任务平均成功率 95.7%，FoundationPose 基线 15.7%。 · [📝 review](digests/migration-2026-10-22.md)

- **[SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors](https://arxiv.org/abs/2606.23444)** — *Rao, Pratyaksh et al.* · `2026-06-22` · `59/100`（C3·E4·O1·T5）
  > JEPA 式潜在动力学模型+物理启发探针+MPPI 用于四旋翼实时控制，仅用域随机化仿真数据训练并零样本上机；作者报告长时程开环预测误差低于直接预测模型，户外负载/换桨下仍稳定跟踪。 · [📝 review](digests/migration-2026-10-22.md)

- **[Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement](https://arxiv.org/abs/2606.18953)** — *Kim, Kinam et al.* · `2026-06-17` · `56/100`（C3·E4·O1·T4）
  > 以 6-DoF 物体位姿+本体状态+VLA 基础动作为观测，在 MuJoCo 中训练残差 RL 并零样本迁移到 FR3；作者报告五项真机任务平均成功率 42%→76%。 · [🌐 project](https://www.microsoft.com/en-us/research/articles/object-centric-residual-rl/) · [📝 review](digests/migration-2026-10-22.md)

</details>


<sub>[⬆ back to top](#contents)</sub>

## <a id="scene"></a>🌍 3D Scene Understanding

*NeRF, Gaussian Splatting, segmentation for robotics*
<details open>
<summary>🔥 <b>Must-read & notable / 重点与值得关注</b> · 1 paper</summary>

- 👀 **[PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects](https://arxiv.org/abs/2605.21572)** — *Cao, Ziang et al.* · `2026-05-20` · `78/100`（C4·E3·O4·T5） · 💻 · 🧩 *adjacent*
  > PhysX-Omni 用 VLM 统一生成刚体、可形变与铰接的仿真就绪 3D 资产，并发布 PhysXVerse（8.7K 资产）与 PhysX-Bench；作者报告几何与物理属性指标多数优于 PhysX-Anything 等。 · [🌐 project](https://physx-omni.github.io) · [💻 code](https://github.com/physx-omni/PhysX-Omni) · [📝 review](digests/migration-2026-10-22.md)

</details>

<details>
<summary>📋 <b>Also tracked / 观察中与暂不评级</b> · 3 papers</summary>

- **[HomeWorld: A Unified Floorplan-to-Furnished Framework for Generating Controllable, Densely Interactive Whole-Home Scenes](https://arxiv.org/abs/2606.06390)** — *Li, Wenbo et al.* · `2026-06-04` · `57/100`（C3·E3·O2·T4） · 📄 · 🧩 *adjacent*
  > 以 30 万真实户型训练 LLM 生成可控户型，再经俯视/第一视角“漫游”式图像生成、VLM 纠错与小物体摆放得到可仿真的整屋场景；作者报告布局碰撞与越界率低于 Holodeck、LayoutVLM 等。 · [📝 review](digests/migration-2026-10-22.md)

- **[ERQA-Plus: A Diagnostic Benchmark for Reasoning in Embodied AI](https://arxiv.org/abs/2606.17639)** — *Yang, Hong et al.* · `2026-06-16` · `54/100`（C2·E3·O3·T3） · 🧩 *adjacent*
  > 基于 711 张机器人视角图像构建 1,766 道按具身推理分类的问答诊断基准；作者报告最强 Qwen3-VL-32B 选择题准确率 83.4%，时序推理与路径规划仍是短板。 · [📝 review](digests/migration-2026-10-22.md)

- **[VISA: VLM-Guided Instance Semantic Auditing for 3D Occupancy World Models](https://arxiv.org/abs/2606.13460)** — *Xian, Ruiqi et al.* · `2026-06-11` · `45/100`（C2·E3·O1·T4）
  > 训练期让离线 VLM 对物体裁剪做结构化"语义审计"并蒸馏进占据栅格世界模型，作者报告 nuScenes 上 GaussianWorld mIoU 21.36→21.91，推理不变。 · [📝 review](digests/migration-2026-10-22.md)

</details>

<details>
<summary>📜 <b>Classic landmarks / 经典奠基</b> · 1 paper</summary>

- 📜 **[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2308.04079)** — *Kerbl et al.* · `2023-08-08` · 🏛️ **ACM TOG 2023** · `94/100`（C5·E5·O4·T5） · 💻 · 🧩 *adjacent*
  > 以可优化的各向异性 3D 高斯表示场景并配合可微分块光栅化，在 1080p 下实现 ≥30fps 实时新视角合成，作者报告画质与 Mip-NeRF360 相当且训练更快。 · [🌐 project](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) · [💻 code](https://github.com/graphdeco-inria/gaussian-splatting) · [📝 review](digests/migration-2026-10-22.md)

</details>


<sub>[⬆ back to top](#contents)</sub>

## <a id="navigation"></a>🧭 Navigation & Mobility

*Visual navigation, embodied QA, mobile robots*
<details open>
<summary>🔥 <b>Must-read & notable / 重点与值得关注</b> · 4 papers</summary>

- 🔥 **[ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation](https://arxiv.org/abs/2610.25690)** — *Yihui Yang et al.* · `2026-10-19` · `86/100`（C4·E4·O5·T4） · 💻
  > ScaleNav 用互联网自我中心视频做指令条件视频预训练再对齐动作；作者报告 Short-Horizon OVON 86.5%、HabitatGS-LN 94.9%，Go2 真机 83.3%。 · [🌐 project](https://zju3dv.github.io/ScaleNav/) · [💻 code](https://github.com/MachEmbodied/ScaleNav) · [📝 review](digests/daily/2026-10-22.md)

- 🔥 **[Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation](https://arxiv.org/abs/2608.17512)** — *Feng, Hongyan et al.* · `2026-08-18` · `80/100`（C4·E4·O4·T4） · 💻
  > TAMP-Nav（Embodied-Navigator）让 VLM 只在图像上点选像素再投影成 3D 路点，配合按需推理、锚点轨迹记忆与两级 GRPO；作者报告 R2R-CE 未见验证集成功率 66.2%，仅用 9 万条轨迹训练。 · [🌐 project](https://zju-omniai.github.io/Embodied-Navigator/) · [💻 code](https://github.com/ZJU-OmniAI/Embodied-Omni) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[HumanCLAW: Can Vision-Language Models Act Through a Body?](https://arxiv.org/abs/2607.27180)** — *Li, Siyao et al.* · `2026-07-29` · `75/100`（C4·E3·O4·T4） · 💻 · 🧩 *adjacent*
  > 将 VLM 决策与底层运动执行解耦的人形具身评测框架，VLM 每步发出原子技能、由技能条件运动生成器在半物理仿真中执行；作者报告 9 个 VLM 在 1,218 个找-走-坐任务上最好成功率仅 16.8%。 · [🌐 project](https://human-claw.github.io/) · [💻 code](https://github.com/Human-CLAW/HumanCLAW) · [📝 review](digests/migration-2026-10-22.md)

- 👀 **[Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System](https://arxiv.org/abs/2606.18112)** — *Zhang, Jiazhao et al.* · `2026-06-16` · `68/100`（C4·E4·O2·T4） · 📄
  > 基于 Qwen3-VL 的多任务导航模型，以可在推理时重配置的任务模式与观测参数服务上层智能体；作者报告 VLN-CE RxR SR 76.5%、EVT-Bench TR 90.0%、NAVSIM PDMS 91.4。 · [🌐 project](https://qwen.ai/blog?id=qwen-robotnav) · [📝 review](digests/migration-2026-10-22.md)

</details>

<details>
<summary>📋 <b>Also tracked / 观察中与暂不评级</b> · 7 papers</summary>

- **[MAD: Mapping-Aware World Models for Agile Quadrotor Flight](https://arxiv.org/abs/2606.04534)** — *Zhang, Xinhong et al.* · `2026-06-03` · `56/100`（C3·E4·O1·T4）
  > 视觉四旋翼的几何感知世界模型 MAD：以机体中心占据/可见性栅格和本体状态代替原图重建作为监督，作者报告仿真最高 9.66 m/s、真实森林飞行 5.05 m/s。 · [📝 review](digests/migration-2026-10-22.md)

- **[HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments](https://arxiv.org/abs/2608.12860)** — *Pham, Quan-Dung et al.* · `2026-08-13` · `54/100`（C3·E3·O2·T3） · 🧩 *adjacent*
  > HumanoidVLN 在 Isaac Sim 中用 RL 行走策略加 PD/MPC 跟踪器驱动四种人形机器人做 VLN，含 87 个场景、933 条回合；作者报告 JanusVLN 平均成功率最高（43.55%），H1 上跌倒率最高达 71%。 · [🌐 project](https://humanoid-vln.github.io/) · [📝 review](digests/migration-2026-10-22.md)

- **[NavVerse: Benchmarking Indoor-to-Outdoor Embodied Navigation in Continuous Robot Simulation](https://arxiv.org/abs/2607.19695)** — *Wu, Junzhe et al.* · `2026-07-22` · `54/100`（C3·E3·O2·T3） · 🧩 *adjacent*
  > 基于 Isaac Sim 的室内到室外连续物理导航基准，含 ObjNav/VLN/PlaceNav 共 1 万 episode 与安全指标；作者报告最好的零样本基线 UniNaVid 成功率仅约 11%。 · [🌐 project](https://arxiv.org/abs/2607.19191) · [📝 review](digests/migration-2026-10-22.md)

- **[NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation](https://arxiv.org/abs/2606.13494)** — *Azuma, Daichi et al.* · `2026-06-11` · `54/100`（C3·E3·O2·T3）
  > 在 Cosmos Predict2 潜画布中联合去噪未来视角、目标进度值与动作块，免去 CEM 规划；作者报告 Diablo 真机 24 次图像目标导航成功率 79.2%。 · [📝 review](digests/migration-2026-10-22.md)

- **[Learning to Evolve: Multi-modal Interactive Fields for Robust Humanoid Navigation in Dynamic Environments](https://arxiv.org/abs/2605.21935)** — *Jiang, Peifeng et al.* · `2026-05-21` · 🏛️ **RSS 2026** · `54/100`（C3·E3·O2·T3）
  > 面向人形机器人的多模态交互场 MIF：置信度感知语义 3DGS 抑制步态抖动、差异触发局部记忆更新、按需网格重建做交互位姿安全校验；作者报告 Unitree G1 真实动态办公室中重定位成功率 12%→94%。 · [📝 review](digests/migration-2026-10-22.md)

- **[Learning-Based Behavior Planning for Automated Driving: Real-World Integration and Deployment](https://arxiv.org/abs/2608.12198)** — *Busch, Jean-Pierre et al.* · `2026-08-12` · 🏛️ **Uni-DAS Workshop 2026** · `52/100`（C2·E2·O3·T4） · 🟡
  > 混合规划架构：模仿学习的行为规划网络提出参考轨迹，优化式监督层施加可行驶与安全约束并保留规则式兜底；作者报告开环评测结果并在 RWTH 研究车辆 karl. 上完成试验场部署。 · [💻 code](https://github.com/openads-project/ackermann_trajectory_control) · [📝 review](digests/migration-2026-10-22.md)

- **[NavWM: A Unified Navigation World Model for Foresight-Driven Planning](https://arxiv.org/abs/2606.24101)** — *Mei, Yanghong et al.* · `2026-06-23` · 🏛️ **ECCV 2026** · `48/100`（C3·E3·O1·T3）
  > 以 Mamba 骨干统一潜在世界推理、锚点式多模态轨迹提议与 CDiT 视觉前瞻，用世界模型挑选候选轨迹；作者报告图像目标导航已见环境 SR 0.72，高于 UniWM 的 0.66。 · [📝 review](digests/migration-2026-10-22.md)

</details>


<sub>[⬆ back to top](#contents)</sub>

## <a id="rl-il"></a>🎯 RL & Imitation Learning

*Diffusion policies, behavior cloning, RL for robotics*
<details open>
<summary>🔥 <b>Must-read & notable / 重点与值得关注</b> · 1 paper</summary>

- 👀 **[Revisiting Open-Loop Execution in Robotics: Toward Reactive, Higher-Performing Policies](https://arxiv.org/abs/2608.15938)** — *Zeng, Michael et al.* · `2026-08-16` · `77/100`（C4·E4·O3·T5） · 📄 · 🧩 *adjacent*
  > 通过受控实验指出长开环执行主要在弥补短上下文策略模仿非马尔可夫示教的缺陷，作者报告在 4 个仿真和 2 个真机任务上加长上下文后最具反应性的闭环策略表现最好。 · [🌐 project](https://revisiting-open-loop-action-chunking.github.io/) · [📝 review](digests/migration-2026-10-22.md)

</details>

<details>
<summary>📋 <b>Also tracked / 观察中与暂不评级</b> · 4 papers</summary>

- **[RoboStriker: Latent-Space Strategic Games for Autonomous Humanoid Boxing](https://arxiv.org/abs/2608.16195)** — *Yin, Kangning et al.* · `2026-08-17` · `63/100`（C4·E3·O2·T4）
  > RoboStriker 把人形机器人拳击建模为潜空间零和博弈，在预训练运动解码器的有界潜空间中做神经虚拟自博弈，作者报告胜率与击打效率优于原始关节空间方法，并在两台 G1 上真机对打。 · [🌐 project](https://grange007.github.io/HAF) · [📝 review](digests/migration-2026-10-22.md)

- **[ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning](https://arxiv.org/abs/2606.17011)** — *Xiao, Wei et al.* · `2026-06-15` · `57/100`（C3·E3·O2·T4）
  > 针对人形机器人遥操作干预数据不完美，提出乐观价值估计与人类经验视频辅助的 VLA 后训练；作者报告两项真机任务三轮迭代后成功率分别升至 80.0% 和 86.7%。 · [📝 review](digests/migration-2026-10-22.md)

- **[Dream2Reward: Transition-Alignment Reward Models from Positive Demonstrations for Robotic Manipulation](https://arxiv.org/abs/2608.18787)** — *Zhang, Haoyu et al.* · `2026-08-19` · `53/100`（C3·E4·O1·T3）
  > 仅用成功示范学习语言条件的潜空间成功转移场，以方向与幅度对齐给出稠密奖励；作者报告真机失败检测AUC 0.95，并提升LIBERO在线RL与真机离线RL效果。 · [📝 review](digests/migration-2026-10-22.md)

- **[Prism-GRPO: Faster VLA Policy Optimization via Splitting Same-outcome Groups](https://arxiv.org/abs/2608.17423)** — *Deng, Zeyun et al.* · `2026-08-18` · `53/100`（C3·E4·O1·T3）
  > Prism-GRPO 在二值成功奖励上叠加有界的执行质量分，把全成功/全失败的退化组拆分成可学习信号；作者报告在 4 个 RoboTwin 任务上达到目标成功率最多少用 56% 的 rollout，并抑制奖励作弊。 · [🌐 project](https://unireflex.github.io/) · [📝 review](digests/migration-2026-10-22.md)

</details>

<details>
<summary>📜 <b>Classic landmarks / 经典奠基</b> · 1 paper</summary>

- 📜 **[Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137)** — *Chi et al.* · `2023-03-07` · 🏛️ **RSS 2023** · `100/100`（C5·E5·O5·T5） · 💻
  > 把视觉运动策略表示为动作空间的条件去噪扩散过程，配合滚动时域控制与时序扩散 Transformer；作者报告在 4 个基准 15 项任务上平均提升 46.9%。 · [🌐 project](https://diffusion-policy.cs.columbia.edu) · [💻 code](https://github.com/real-stanford/diffusion_policy) · [📝 review](digests/migration-2026-10-22.md)

</details>


<sub>[⬆ back to top](#contents)</sub>

## <a id="datasets"></a>📦 Datasets

*Robot trajectories, demonstrations, scene datasets*
<details>
<summary>📁 <b>Manipulation Demonstrations</b> · 7 datasets</summary>

- **[Open X-Embodiment (RT-X)](https://robotics-transformer-x.github.io)** — Cross-embodiment robot dataset spanning 22 robot types, 1M+ trajectories. · *1M+ episodes* · [paper](https://arxiv.org/abs/2310.08864) · [code](https://github.com/google-deepmind/open_x_embodiment) · 🔗 used by [11 tracked papers](docs/index.md#resource-open-x-embodiment)
- **[DROID](https://droid-dataset.github.io)** — Diverse real-world manipulation dataset from 564 scenes, 13 institutions. · *76k demonstrations* · [paper](https://arxiv.org/abs/2403.12945) · 🔗 used by [18 tracked papers](docs/index.md#resource-droid)
- **[BridgeData V2](https://rail-berkeley.github.io/bridgedata)** — Large-scale tabletop manipulation dataset for generalization research. · *60k trajectories* · [paper](https://arxiv.org/abs/2308.12952) · 🔗 used by [12 tracked papers](docs/index.md#resource-bridgedata-v2)
- **[ARIO (All Robots In One)](https://imaei.github.io/project_pages/ario/)** — Unified cross-embodiment robot learning dataset. · [paper](https://arxiv.org/abs/2408.10899)
- **[AgiBot World](https://agibot-world.com)** — Large-scale humanoid manipulation dataset from AgiBot's real-world deployments. · 🔗 used by [19 tracked papers](docs/index.md#resource-agibot-world)
- **[PRISM](https://tengbo-yu.github.io/PRISM/)** — Real-world contact-rich industrial manipulation dataset, 25+ tasks, 5k+ teleoperated trajectories with RGB-D, F/T, tactile and robot state across 3 robots. · [paper](https://arxiv.org/abs/2608.17962)
- **[ToolBook](https://snu-pi.github.io/HumanoidToolBench/)** — 3,094 human demonstrations of humanoid tool use, 3,003 in simulation and 91 on a real Unitree G1. · [code](https://github.com/SNU-PI/HumanoidToolBench)

</details>
<details>
<summary>📁 <b>3D Scenes</b> · 4 datasets</summary>

- **[Habitat-Matterport 3D (HM3D)](https://aihabitat.org/datasets/hm3d/)** — 1000+ photorealistic indoor 3D scenes for embodied AI training. · [paper](https://arxiv.org/abs/2109.08238)
- **[ScanNet++](https://kaldir.vc.in.tum.de/scannetpp/)** — 1006 high-fidelity indoor scenes with sub-mm geometry & DSLR captures. · [paper](https://arxiv.org/abs/2308.11417)
- **[Replica Dataset](https://github.com/facebookresearch/Replica-Dataset)** — 18 high-quality reconstructions of indoor spaces (Meta Reality Labs). · [paper](https://arxiv.org/abs/1906.05797)
- **[3D-FRONT / 3D-FUTURE](https://tianchi.aliyun.com/specials/promotion/alibaba-3d-scene-dataset)** — Synthetic indoor scenes with high-quality furniture CAD models (Alibaba). · [paper](https://arxiv.org/abs/2011.09127)

</details>
<details>
<summary>📁 <b>Egocentric / Human Video</b> · 5 datasets</summary>

- **[Ego4D](https://ego4d-data.org)** — 3,670 hours of egocentric video across 74 worldwide locations. · *3,670 hours* · [paper](https://arxiv.org/abs/2110.07058) · 🔗 used by [4 tracked papers](docs/index.md#resource-ego4d)
- **[EPIC-KITCHENS-100](https://epic-kitchens.github.io/2024)** — Long-form egocentric kitchen activity dataset for action understanding. · *100 hours* · [paper](https://arxiv.org/abs/2006.13256) · 🔗 used by [2 tracked papers](docs/index.md#resource-epic-kitchens-100)
- **[HOI4D](https://hoi4d.github.io)** — 4D egocentric dataset for category-level human-object interaction. · [paper](https://arxiv.org/abs/2203.01577) · 🔗 used by [3 tracked papers](docs/index.md#resource-hoi4d)
- **[ScaleNav-Data](https://zju3dv.github.io/ScaleNav/)** — 18,249 段互联网自我中心导航视频片段（含指令标注）与 2,600 条 Habitat-GS 仿真 episode（含对齐动作）。 · [code](https://github.com/MachEmbodied/ScaleNav)
- **[EgoX-Data-6M](https://ropedia.github.io/EgoXperience)** — 50 小时任务驱动的自我中心操作与移动视频（101 个刚性物体、270 个任务脚本），含统一度量世界坐标下的相机、深度、双手、物体标注与秒级任务描述。 · [paper](https://arxiv.org/abs/2610.26625) · 🔗 used by [1 tracked paper](docs/index.md#resource-egox-data-6m)

</details>
<details>
<summary>📁 <b>Motion Capture / Whole-Body</b> · 2 datasets</summary>

- **[AMASS](https://amass.is.tue.mpg.de)** — Unifies 15 mocap datasets in a common SMPL skeleton — 40+ hours of motion. · [paper](https://arxiv.org/abs/1904.03278) · 🔗 used by [6 tracked papers](docs/index.md#resource-amass)
- **[HumanML3D](https://github.com/EricGuo5513/HumanML3D)** — 14,616 motions with text annotations for motion-language tasks. · [paper](https://arxiv.org/abs/2202.04257) · [code](https://github.com/EricGuo5513/HumanML3D)

</details>
<details>
<summary>📁 <b>Sim-Generated</b> · 4 datasets</summary>

- **[RoboCasa-Gen](https://robocasa.ai)** — Large-scale procedurally generated household tasks rendered in MuJoCo. · [paper](https://arxiv.org/abs/2406.02523) · 🔗 used by [1 tracked paper](docs/index.md#resource-robocasa-gen)
- **[PhysXVerse](https://arxiv.org/abs/2605.21572)** — First general-purpose simulation-ready 3D dataset (released with PhysX-Omni, 2026). · [paper](https://arxiv.org/abs/2605.21572) · 🔗 used by [1 tracked paper](docs/index.md#resource-physxverse)
- **[GRAIL Humanoid Loco-Manipulation](https://github.com/NVlabs/GRAIL)** — 由 GRAIL 流水线生成的 2 万+条 Unitree G1 人形 loco-manipulation 序列（拾取、全身操作、坐下、地形穿越），源自视频世界模型与 3D 资产 · [paper](https://arxiv.org/abs/2606.05160) · [code](https://github.com/NVlabs/GRAIL)
- **[Ego2Robot](https://www-ye.github.io/ego2robot_blog/)** — 由第一人称人手操作视频经动作重定向与机械臂渲染合成的 18,561 小时机器人训练数据，覆盖 15 种机械臂形态（截至 2026-10 尚未公开）。 · [paper](https://arxiv.org/abs/2608.02580) · 🔗 used by [1 tracked paper](docs/index.md#resource-ego2robot-data)

</details>

<sub>[⬆ back to top](#contents)</sub>

## <a id="simulators"></a>🎮 Simulators

*Isaac Sim, MuJoCo, Genesis, and friends*

| Simulator | What it is | Backend / tags | Links |
|---|---|---|---|
| **[Isaac Lab](https://isaac-sim.github.io/IsaacLab)** | NVIDIA's modular RL training framework built on Isaac Sim. | `rl` `gpu-accelerated` `nvidia` | [💻 code](https://github.com/isaac-sim/IsaacLab) |
| **[Isaac Sim](https://developer.nvidia.com/isaac/sim)** | NVIDIA's full robot simulator with photorealistic rendering. | `photorealistic` `gpu` `nvidia` |  |
| **[Genesis](https://genesis-embodied-ai.github.io)** | Universal physics engine for robotics — built in pure Python, 43M FPS claim. | `physics` `python` `multi-material` | [📄 paper](https://arxiv.org/abs/2412.04268) · [💻 code](https://github.com/Genesis-Embodied-AI/Genesis) |
| **[MuJoCo MJX](https://mujoco.readthedocs.io/en/latest/mjx.html)** | GPU/TPU-accelerated JAX-based version of MuJoCo for massive parallel rollouts. | `jax` `gpu` `parallel` | [💻 code](https://github.com/google-deepmind/mujoco) |
| **[Habitat 3.0](https://aihabitat.org)** | Photorealistic embodied AI sim with humans, navigation + manipulation. | `navigation` `humans` `photorealistic` | [📄 paper](https://arxiv.org/abs/2310.13724) · [💻 code](https://github.com/facebookresearch/habitat-sim) |
| **[RoboCasa](https://robocasa.ai)** | Large-scale household simulation framework on top of MuJoCo. | `household` `mujoco` `large-scale` | [📄 paper](https://arxiv.org/abs/2406.02523) · [💻 code](https://github.com/robocasa/robocasa) |
| **[ManiSkill 3](https://maniskill.ai)** | GPU-parallelized manipulation skill learning sim. | `manipulation` `gpu` | [💻 code](https://github.com/haosulab/ManiSkill) |
| **[MotrixSim (Motphys / 谋先飞)](https://www.motphys.com/en/products)** | Homegrown Chinese real-time physics engine for multibody dynamics & robotics — generalized coordinates + implicit solver, GPU multi-world parallel training. Powers the MIIT/CAS-backed AGIROS embodied-AI ecosystem. | `physics` `gpu` `multibody` `china` | [💻 code](https://github.com/Motphys/motrixsim-docs) |

<sub>[⬆ back to top](#contents)</sub>

## <a id="benchmarks"></a>📊 Benchmarks

*Standardized evaluations for embodied AI*
<details>
<summary>📐 <b>Manipulation</b> · 12 benchmarks</summary>

- **[CALVIN](http://calvin.cs.uni-freiburg.de)** — Long-horizon, language-conditioned manipulation benchmark. · [paper](https://arxiv.org/abs/2112.03227) · [code](https://github.com/mees/calvin) · 🔗 used by [5 tracked papers](docs/index.md#resource-calvin)
- **[Meta-World](https://meta-world.github.io)** — 50 manipulation tasks for multi-task and meta-RL evaluation. · [paper](https://arxiv.org/abs/1910.10897) · [code](https://github.com/Farama-Foundation/Metaworld) · 🔗 used by [1 tracked paper](docs/index.md#resource-meta-world)
- **[LIBERO](https://libero-project.github.io)** — Lifelong robot learning benchmark — 130 manipulation tasks across 4 suites. · [paper](https://arxiv.org/abs/2306.03310) · 🔗 used by [61 tracked papers](docs/index.md#resource-libero)
- **[RLBench](https://sites.google.com/view/rlbench)** — 100 vision-guided manipulation tasks with CoppeliaSim. · [paper](https://arxiv.org/abs/1909.12271) · [code](https://github.com/stepjam/RLBench) · 🔗 used by [4 tracked papers](docs/index.md#resource-rlbench)
- **[AliasBench](https://arxiv.org/abs/2605.14712)** — Benchmark probing multimodal-imitation ambiguity in VLA (used in IntentVLA 2026). · [paper](https://arxiv.org/abs/2605.14712) · 🔗 used by [1 tracked paper](docs/index.md#resource-aliasbench)
- **[RoboTwin 2.0](https://github.com/RoboTwin-Platform/RoboTwin)** — 可扩展的双臂操作数据生成器与基准，含 50 个双臂任务，提供 clean 与强域随机化两种设置。 · [paper](https://arxiv.org/abs/2506.18088) · [code](https://github.com/RoboTwin-Platform/RoboTwin) · 🔗 used by [10 tracked papers](docs/index.md#resource-robotwin-2)
- **[KineBench](https://github.com/minecraft-zzz/KineBench)** — 基于 ManiSkill3 的具身视频世界模型闭环评测基准，用显式 6D 位姿提取替代 IDM，含 20 个操作任务与 4 个评测套件。 · [paper](https://arxiv.org/abs/2607.19876) · [code](https://github.com/minecraft-zzz/KineBench)
- **[RoboTwin 2.0](https://robotwin-platform.github.io)** — Bimanual manipulation simulation benchmark with 50 tasks under clean and domain-randomized settings. · [paper](https://arxiv.org/abs/2506.18088) · 🔗 used by [2 tracked papers](docs/index.md#resource-robotwin)
- **[H2R-Bench](https://rongdingyi.github.io/H2R-Bench/)** — Benchmark of human-to-robot manipulation video generation, 240 EgoDex-based transfer cases scored on goal, action, contact, embodiment and video quality. · [paper](https://arxiv.org/abs/2608.13049) · [code](https://github.com/Rongdingyi/H2R-Bench) · 🔗 used by [1 tracked paper](docs/index.md#resource-h2r-bench)
- **[SoftVTBench](https://github.com/TuojingAI/SoftVTBench)** — Isaac-based visuo-tactile deformable-object pick-and-place dataset and benchmark with evaluator-only FEM states and Deformation-aware Success Rate (DSR). · [paper](https://arxiv.org/abs/2608.18701) · [code](https://github.com/TuojingAI/SoftVTBench)
- **[HumanoidToolBench](https://snu-pi.github.io/HumanoidToolBench/)** — 18-task humanoid tool-use benchmark: 3 scenarios x 3 execution levels x 2 tool-set modes, 55 tool assets. · [code](https://github.com/SNU-PI/HumanoidToolBench)
- **[EgoX-Bench](https://ropedia.github.io/EgoXperience)** — 从 EgoX-Data-6M 留出的 1 小时质量受控子集，覆盖工作台操作、跨房间交互与户外 loco-manipulation，用于联合评测相机、深度、手与物体重建。 · [paper](https://arxiv.org/abs/2610.26625) · 🔗 used by [1 tracked paper](docs/index.md#resource-egox-bench)

</details>
<details>
<summary>📐 <b>Navigation</b> · 7 benchmarks</summary>

- **[ProcTHOR](https://procthor.allenai.org)** — 10,000+ procedurally generated household scenes for embodied AI. · [paper](https://arxiv.org/abs/2206.06994)
- **[Habitat ObjectNav](https://aihabitat.org/challenge/2023/)** — Standard object-goal navigation in HM3D / MP3D. · [paper](https://arxiv.org/abs/2210.13063)
- **[OVMM](https://arxiv.org/abs/2310.13724)** — Open-vocabulary mobile manipulation benchmark (Habitat 3.0). · [paper](https://arxiv.org/abs/2310.13724)
- **[NavVerse](https://umich-curly.github.io/NavVerse-Benchmark/)** — Isaac Sim 上的室内/室外/室内到室外连续物理导航基准，含 ObjNav、VLN、PlaceNav 三类任务与安全指标。 · [paper](https://arxiv.org/abs/2607.19695)
- **[HumanCLAW-Bench](https://human-claw.github.io/)** — 基于 HSSD 的人形具身评测基准，VLM 发出原子技能、运动生成器在半物理仿真中执行，含 1,218 个寻找-导航-交互长程 episode。 · [paper](https://arxiv.org/abs/2607.27180) · [code](https://github.com/Human-CLAW/HumanCLAW)
- **[HumanoidVLN](https://humanoid-vln.github.io/)** — Physics-grounded VLN benchmark in Isaac Sim with four humanoid embodiments, 87 curated scenes (artist + 3DGS) and 933 instruction episodes. · [paper](https://arxiv.org/abs/2608.12860) · 🔗 used by [1 tracked paper](docs/index.md#resource-humanoidvln)
- **[HabitatGS-LN](https://zju3dv.github.io/ScaleNav/)** — 基于 Habitat-GS/InteriorGS 的语言条件局部导航基准，157 个 episode/45 个留出场景，要求按属性与空间关系定位可见目标并停靠。 · [code](https://github.com/MachEmbodied/ScaleNav)

</details>
<details>
<summary>📐 <b>Locomotion / Whole-Body</b> · 1 benchmarks</summary>

- **[HumanoidBench](https://humanoid-bench.github.io)** — MuJoCo-based humanoid locomotion + whole-body manipulation benchmark. · [paper](https://arxiv.org/abs/2403.10506) · [code](https://github.com/carlosferrazza/humanoid-bench)

</details>
<details>
<summary>📐 <b>VLA Generalization & OOD</b> · 2 benchmarks</summary>

- **[SimplerEnv](https://simpler-env.github.io)** — Reproducible real-to-sim eval suite — measures VLA gap between real and sim deployment. · [paper](https://arxiv.org/abs/2405.05941) · [code](https://github.com/simpler-env/SimplerEnv) · 🔗 used by [13 tracked papers](docs/index.md#resource-simplerenv)
- **[PhysX-Bench](https://arxiv.org/abs/2605.21572)** — 6-dim evaluation (geometry/scale/material/affordance/kinematics/function) — released with PhysX-Omni, 2026. · [paper](https://arxiv.org/abs/2605.21572) · 🔗 used by [1 tracked paper](docs/index.md#resource-physx-bench)

</details>
<details>
<summary>📐 <b>Multi-Skill / Long-Horizon</b> · 3 benchmarks</summary>

- **[BEHAVIOR-1K](https://behavior.stanford.edu/behavior-1k)** — 1,000 long-horizon household activities in OmniGibson — the largest activity benchmark. · [paper](https://arxiv.org/abs/2403.09227) · 🔗 used by [4 tracked papers](docs/index.md#resource-behavior-1k)
- **[RoboCasa-Bench](https://robocasa.ai)** — 100+ atomic + composite household tasks running on RoboCasa-Gen scenes. · [paper](https://arxiv.org/abs/2406.02523) · 🔗 used by [12 tracked papers](docs/index.md#resource-robocasa-bench)
- **[Xp-Teleop](https://ropedia.github.io/ropedia-w0/)** — Unitree G1 双六自由度灵巧手长时程 loco-manipulation 遥操作世界模型评测集，27 段约 1 小时、543 个原子片段/30 类技能，含 RGB-D、位姿、骨架与触觉。 · [code](https://github.com/Ropedia/ropedia-w0)

</details>

<sub>[⬆ back to top](#contents)</sub>

## <a id="tools"></a>🛠️ Tools & Libraries

*Open-source frameworks for building embodied AI*

| Tool | What it is | Links |
|---|---|---|
| **[LeRobot](https://huggingface.co/lerobot)** | Hugging Face's end-to-end robotics framework — datasets, models, hardware. | ✅ [💻 code](https://github.com/huggingface/lerobot) |
| **[Diffusion Policy](https://github.com/real-stanford/diffusion_policy)** | Reference implementation of action-space diffusion policies. | ✅ [💻 code](https://github.com/real-stanford/diffusion_policy) · [📄 paper](https://arxiv.org/abs/2303.04137) |
| **[OpenVLA](https://openvla.github.io)** | Open-source 7B Vision-Language-Action foundation model. | ✅ [💻 code](https://github.com/openvla/openvla) |
| **[AnyGrasp SDK](https://graspnet.net/anygrasp.html)** | General object grasping in cluttered scenes. | ✅ [💻 code](https://github.com/graspnet/anygrasp_sdk) · [📄 paper](https://arxiv.org/abs/2212.08333) |
| **[Curobo](https://curobo.org)** | NVIDIA's GPU-accelerated motion planning library. | ✅ [💻 code](https://github.com/NVlabs/curobo) |
| **[nvdiffrast](https://nvlabs.github.io/nvdiffrast/)** | Modular differentiable rendering primitives from NVIDIA. | ✅ [💻 code](https://github.com/NVlabs/nvdiffrast) |

<sub>[⬆ back to top](#contents)</sub>

## <a id="companies"></a>🏢 Companies & Industry

*Humanoid and embodied AI startups with valuation tracker*
### 💰 Valuation Tracker

| Company | Region | Focus | Latest Round | Valuation | Date |
|---|---|---|---|---|---|
| **Figure** | US | humanoid, manipulation | Series B $675,000,000 | $2,600,000,000 | 2024-02 |
| **Physical Intelligence** | US | vla, manipulation, foundation-model | Series A $400,000,000 | $2,400,000,000 | 2024-11 |
| **Skild AI** | US | foundation-model, generalist | Series A $300,000,000 | $1,500,000,000 | 2024-07 |
| **1X Technologies** | Norway | humanoid, world-model | Series B $100,000,000 | $1,300,000,000 | 2024-01 |
| **Tesla Optimus** | US | humanoid | — | — | — |
| **Apptronik** | US | humanoid | Series A $350,000,000 | — | 2025-02 |
| **Agility Robotics** | US | humanoid, logistics | Series B $150,000,000 | — | 2024 |
| **Boston Dynamics** | US | humanoid, quadruped | — | — | — |
| **Sanctuary AI** | CA | humanoid | — | — | — |
| **宇树科技 (Unitree Robotics)** | CN | locomotion, humanoid, quadruped | — | — | — |
| **智元机器人 (AgiBot)** | CN | humanoid, manipulation | — | — | — |
| **银河通用 (Galbot)** | CN | humanoid, manipulation, vla | — | — | — |
| **星海图 (Galaxea AI)** | CN | humanoid, manipulation | — | — | — |
| **月泉仿生** | CN | humanoid, manipulation | — | — | — |
| **加速进化 (Booster Robotics)** | CN | humanoid | — | — | — |
| **云深处科技 (DeepRobotics)** | CN | quadruped, humanoid | — | — | — |
| **傅利叶智能 (Fourier Intelligence)** | CN | humanoid, rehabilitation | — | — | — |
| **追觅 (Dreame)** | CN | service-robot, humanoid | — | — | — |
| **逐际动力 (LimX Dynamics)** | CN | humanoid, locomotion | — | — | — |

<details>
<summary>🇺🇸 <b>United States</b> · 7 companies</summary>

- **[Physical Intelligence](https://www.physicalintelligence.company)** · vla / manipulation / foundation-model · *π0, π0.5* · Sergey Levine + Chelsea Finn led, formerly Google Robotics.
- **[Skild AI](https://www.skild.ai)** · foundation-model / generalist · CMU spinout, generalist robot foundation model.
- **[Figure](https://www.figure.ai)** · humanoid / manipulation · *Figure 02, Helix*
- **[Tesla Optimus](https://www.tesla.com/we-robot)** · humanoid · *Optimus Gen 2, Optimus Gen 3* · In-house Tesla program, not standalone company.
- **[Apptronik](https://apptronik.com)** · humanoid · *Apollo*
- **[Agility Robotics](https://agilityrobotics.com)** · humanoid / logistics · *Digit*
- **[Boston Dynamics](https://www.bostondynamics.com)** · humanoid / quadruped · *Atlas (electric), Spot, Stretch*

</details>

<details>
<summary>🇨🇳 <b>China</b> · 10 companies</summary>

- **[宇树科技 (Unitree Robotics)](https://www.unitree.com)** · locomotion / humanoid / quadruped · *G1, H1, Go2, B2*
- **[智元机器人 (AgiBot)](https://www.agibot.com)** · humanoid / manipulation · *远征 A2, 灵犀 X1* · By 稚晖君, former Huawei genius youth.
- **[银河通用 (Galbot)](https://www.galbot.com)** · humanoid / manipulation / vla · Wang He, PKU professor + Yu Tianyi.
- **[星海图 (Galaxea AI)](#)** · humanoid / manipulation · *R1*
- **[月泉仿生](#)** · humanoid / manipulation
- **[加速进化 (Booster Robotics)](#)** · humanoid · *Booster T1*
- **[云深处科技 (DeepRobotics)](https://www.deeprobotics.cn)** · quadruped / humanoid · *X30, Lite3*
- **[傅利叶智能 (Fourier Intelligence)](https://www.fftai.com)** · humanoid / rehabilitation · *GR-1, GR-2*
- **[追觅 (Dreame)](#)** · service-robot / humanoid
- **[逐际动力 (LimX Dynamics)](#)** · humanoid / locomotion · *CL-1*

</details>

<details>
<summary>🌍 <b>Europe & Canada</b> · 2 companies</summary>

- **[1X Technologies](https://www.1x.tech)** · humanoid / world-model · *NEO, EVE*
- **[Sanctuary AI](https://sanctuary.ai)** · humanoid · *Phoenix Gen 7*

</details>
<sub>[⬆ back to top](#contents)</sub>

## <a id="tutorials"></a>📚 Tutorials & Surveys

*Surveys, books, and tutorial materials*
<details>
<summary>📋 <b>Also tracked / 观察中与暂不评级</b> · 6 papers</summary>

- **[World Action Models: A Survey](https://arxiv.org/abs/2606.20781)** — *Shen, Qiuhong et al.* · `2026-06-18` · `63/100`（C4·E3·O2·T4） · 📄 · 🧩 *adjacent*
  > 世界-动作模型（WAM）综述：界定其与 VLA、视频世界模型的边界，按“渲染后解码/仅潜空间/无视频生成”三类及四轴结构梳理现有工作与数据、评测和开放问题。 · [🌐 project](https://world-action-models.github.io/) · [📝 review](digests/migration-2026-10-22.md)

- **[Progress Reward Modeling for Robotic Learning: A Comprehensive Survey](https://arxiv.org/abs/2607.21655)** — *Zhang, Jianshu et al.* · `2026-07-22` · `55/100`（C3·E2·O3·T3） · 📄 · 🧩 *adjacent*
  > 机器人学习中进度奖励建模的综述，按接口（输入/目标/输出）、构造方法（冻结基础模型、时序监督、指令微调、程序化奖励）与数据/基准三层梳理，并讨论局限与方向。 · [🌐 project](https://arxiv.org/abs/2607.23909) · [📝 review](digests/migration-2026-10-22.md)

- **[The Embodiment Gap in Robot Foundation Models](https://arxiv.org/abs/2608.18433)** — *Domae, Yukiyasu et al.* · `2026-08-19` · 🏛️ **TMLR 2026** · `43/100`（C3·E2·O1·T3） · 🧩 *adjacent*
  > 围绕“本体差距”的机器人基础模型综述：用双轴图定位跨本体共享结构与目标机器人剩余工作，并提出报告卡与本体适配曲线（EAC）补充成功率之外的报告。 · [🌐 project](https://shepherd1226.github.io/gigabrain-wbc-0.5/) · [📝 review](digests/migration-2026-10-22.md)

- **[Weights or Skills? A Survey of Robot-Learning Techniques: from Action-Predicting Weights to Robots that Write their Own Skills](https://arxiv.org/abs/2608.01851)** — *Jena, Gaytri et al.* · `2026-08-03` · `43/100`（C3·E2·O1·T3） · 🧩 *adjacent*
  > 以“权重 vs 技能”为主轴梳理机器人学习，把 code-as-policy 按自我改进程度分为五级，覆盖 77 个代表系统并附 225 篇外围工作，讨论机器人技能市场的开放问题。 · [🌐 project](https://arxiv.org/abs/2608.06374) · [📝 review](digests/migration-2026-10-22.md)

- **[Towards Robotic Dexterous Hand Intelligence: A Survey](https://arxiv.org/abs/2605.13925)** — *Zhao, Weiguang et al.* · `2026-05-13` · `43/100`（C3·E2·O1·T3） · 🧩 *adjacent*
  > 机器人灵巧手综述：从驱动/传动/感知硬件与代表手型对比、按任务类别梳理 RL/IL/扩散策略/VLA 方法演进、汇总数据集与评测三方面整合，并讨论主要局限与未来方向。 · [📝 review](digests/migration-2026-10-22.md)

- **[World Action Models: The Next Frontier in Embodied AI](https://arxiv.org/abs/2605.12090)** — *Wang, Siyin et al.* · `2026-05-12` · 🟡 · 🧩 *adjacent*
  > 综述「世界动作模型」(WAM)：给出定义，按 Cascaded / Joint 两类及生成模态、条件方式、动作解码细分已有工作，并梳理数据生态与评测协议。 · [🌐 project](https://openmoss.github.io/Awesome-WAM/) · [💻 code](https://github.com/OpenMOSS/Awesome-WAM) · [📝 review](digests/migration-2026-10-22.md)

</details>


<sub>[⬆ back to top](#contents)</sub>


---

## 🗞️ Scan reports / 扫描报告

Each daily run writes a report with its coverage window, inclusion cap, candidate / exclusion statistics and a full review per included paper (problem → method → results & conditions → limits, open status with `last_check`). Weekly (≤15) and monthly (≤30) picks are rolled up from them.

- Latest daily report: [2026-10-22](digests/daily/2026-10-22.md)
- All reports: [digests/](digests/) · Methodology: [docs/METHODOLOGY.md](docs/METHODOLOGY.md) · Ranked index: [docs/index.md](docs/index.md)

---

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=junyuan-fang/awesome-physical-ai&type=Date)](https://star-history.com/#junyuan-fang/awesome-physical-ai&Date)

## 🤝 Contributing

This list is fed by a daily discovery → two-layer review pipeline ([methodology](docs/METHODOLOGY.md)), but PRs are very welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

**Inclusion criteria / 收录标准** (keep the list high-signal):
- ✅ Has a public paper (arXiv/venue) **or** open-source code / project page
- ✅ Comes with a one-line description of its contribution / 一句话说明贡献
- ✅ Relevant to physical AI: embodiment, manipulation, locomotion, world models, sim-to-real, etc.
- ❌ No paywalled-only resources, vague "we're building AGI" startups, or dead links

## 📜 License

[MIT](LICENSE) © 2026 [@junyuan-fang](https://github.com/junyuan-fang)
