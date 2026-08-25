<div align="center">

# 🤖 Awesome Physical AI

**A continuously maintained, auto-updated list of Physical AI · Embodied AI · Humanoid Robotics — focused on 2025–2026+ state-of-the-art.**

*持续自动更新的具身智能 / 物理 AI / 人形机器人资源列表 · 论文描述中英双语，面向中文社区*

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Maintained](https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg)](https://github.com/junyuan-fang/awesome-physical-ai/commits/master)
![Last updated](https://img.shields.io/badge/Last%20updated-2026--08--25-blue.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

📊 **219** papers&nbsp; · &nbsp;🏢 **19** companies&nbsp; · &nbsp;🎮 **8** simulators&nbsp; · &nbsp;📦 **16** datasets&nbsp; · &nbsp;📊 **13** benchmarks

<sub>🤖 Auto-synced daily from arXiv + HuggingFace daily papers · 每日自动同步</sub>

</div>

> 💡 **Legend / 图例**: 🔥 must-read · 👀 worth-knowing · 📜 classic landmark · 🏛️ accepted venue · 🌐 project · 💻 code. Click any **▸ section** to expand / 点击展开折叠区.

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

## Contents

- **📚 Research** — [🤖 Foundation Models for Robotics](#foundation-models) · [🦾 Manipulation](#manipulation) · [🦿 Locomotion](#locomotion) · [🕹️ Teleoperation](#teleoperation) · [🌉 Sim-to-Real](#sim2real) · [🌍 3D Scene Understanding](#scene) · [🧭 Navigation & Mobility](#navigation) · [🎯 RL & Imitation Learning](#rl-il)
- **🧰 Resources** — [📦 Datasets](#datasets) · [🎮 Simulators](#simulators) · [📊 Benchmarks](#benchmarks) · [🛠️ Tools & Libraries](#tools) · [📚 Tutorials & Surveys](#tutorials)
- **🏢 Industry** — [🏢 Companies & Industry](#companies)

---

## <a id="foundation-models"></a>🤖 Foundation Models for Robotics

*Generalist policies, VLA, world models*
<details open>
<summary>🆕 <b>2026</b> · 72 papers</summary>

- 🔥 **[The Embodiment Gap in Robot Foundation Models](https://arxiv.org/abs/2608.18433)** — *Domae, Yukiyasu et al.* · `2026-08-19`
  > Robot foundation models (RFMs), including vision-language-action (VLA) policies, are often discussed through a scaling view: more data, larger models, and broader benchmarks should improve generalization. · [🌐 project](https://shepherd1226.github.io/gigabrain-wbc-0.5/)
- 🔥 **[Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention for Video Generation and World Models](https://arxiv.org/abs/2608.18484)** — *Taghavi, Pardis et al.* · `2026-08-19`
  > Training-free block-sparse attention can accelerate video transformers, but row-wise attention concentration does not by itself specify an executable sparse operator.
- 🔥 **[Hydra-0: Action Flow for Generalist World Modeling and Control](https://arxiv.org/abs/2608.18077)** — *Li, Hongyu et al.* · `2026-08-18`
  > We introduce Hydra-0, a generalist world model conditioned on action flow, which represents robot actions as pixel motion. · [🌐 project](https://unireflex.github.io/)
- 🔥 **[$\tau_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation](https://arxiv.org/abs/2608.16885)** — *Cai, Xiaowei et al.* · `2026-08-17`
  > Long-horizon robot manipulation requires a robot to both execute individual skills reliably and sequence them coherently over extended tasks. · [🌐 project](https://tau0-vla.github.io/)
- 🔥 **[GigaBrain-0.7: Scaling Embodied Foundation Models to Emergent Capabilities with a Three-System Architecture](https://arxiv.org/abs/2608.15875)** — *GigaBrain Team et al.* · `2026-08-16`
  > 注意：项目页对应的是 GigaBrain-0，不是 0.7，页面内容与本文不完全对应。 · [🌐 project](https://tau0-vla.github.io/)
- 🔥 **[ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World Models](https://arxiv.org/abs/2608.14022)** — *Li, Xinye et al.* · `2026-08-14`
  > Action-conditioned video world models require low-latency causal generation and reliable responses to game-native controls. · [🌐 project](https://asdfo123.github.io/ForgeWM)
- 🔥 **[H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models](https://arxiv.org/abs/2608.13049)** — *Rong, Dingyi et al.* · `2026-08-13`
  > arXiv：2608.13049 · 已校验投稿日：2026-08-13；机构：Dingyi Rong, Yue Shi, Chaofan Ma, Jiezhang Cao, Zongrui Wang, Zeyu Zhang, 穆尧, 翟广涛 等 —— 作者群指向 SJTU + HKU/上海 AI Lab，abs 页未明示，属推断。
- 🔥 **[ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models](https://arxiv.org/abs/2608.13438)** — *Zheng, Gehan et al.* · `2026-08-13`
  > arXiv：2608.13438 · 已校验投稿日：2026-08-13；机构：Gehan Zheng, Matthew Johnson-Roberson, Weiming Zhi —— CMU Robotics Institute（和第 5 篇同组）
- 🔥 **[DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation](https://arxiv.org/abs/2608.13489)** — *DreamX Team et al.* · `2026-08-13`
  > arXiv：2608.13489 · 已校验投稿日：2026-08-13；机构：AMAP-ML（阿里巴巴高德 ML 团队）"DreamX Team" — Rui Chen, Xiangxiang Chu, Geng Li, Jifan Li, Qingfeng Shi, Datao Tang, Jing Tang, Jun Wang, Pengfei Zhang · [🌐 project](https://github.com/AMAP-ML/DreamX-Phi)
- 🔥 **[Toward the Cognitive--Physical Limits of Embodied Intelligence through a World-Model-Centric Autonomous Racing Agent](https://arxiv.org/abs/2608.10618)** — *Shan, Zitong et al.* · `2026-08-11`
  > Embodied artificial intelligence aims to develop agents that perceive, reason, and act through continuous interaction with the physical world.
- 🔥 **[VIScore: Diagnosing Planning-Relevant Quality in Latent World Models](https://arxiv.org/abs/2608.11174)** — *Wu, Haiyu et al.* · `2026-08-11`
  > Regulating the latent space to an isotropic Gaussian distribution provides a stable and information-maximized landscape for world model planning.
- 🔥 **[Self-Evolving Embodied Agents via Skill-Harness Evolution](https://arxiv.org/abs/2608.11350)** — *Wang, Peidong et al.* · `2026-08-11`
  > Embodied agents are increasingly built as systems around foundation models, where performance depends not only on model weights but also on the skills, context, action interfaces, and execution harness surrounding the …
- 🔥 **[World Tokens: Enhancing Embodied Policies with Training-Time World Modeling](https://arxiv.org/abs/2608.09730)** — *Tang, Qu et al.* · `2026-08-10`
  > 机构：JIUTIAN Research（中国移动九天）· 中关村学院 · [🌐 project](https://kzz1031.github.io/slim-project-page/)
- 🔥 **[SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation](https://arxiv.org/abs/2608.09771)** — *Wang, Jingkai et al.* · `2026-08-10`
  > 机构：复旦大学 / 北京智源人工智能研究院（BAAI）/ 清华大学 / 中国人民大学 · [🌐 project](https://kzz1031.github.io/slim-project-page/)
- 🔥 **[RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance](https://arxiv.org/abs/2608.09853)** — *Huang, Dongchi et al.* · `2026-08-10`
  > 机构：DAMO Academy, Alibaba Group；Hupan Lab · [🌐 project](https://alibaba-damo-academy.github.io/RynnValue.github.io)
- 🔥 **[EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinforcement Learning](https://arxiv.org/abs/2608.06197)** — *Xu, Zishan et al.* · `2026-08-06`
  > 核心：agent 交替生成工具调用与自己模拟的环境响应（world rehearsal），降低对外部环境依赖、支持测试时私有推演；定位：偏 agentic RL，非机器人本体，但"把环境模型压进权重"这条路对具身端的低成本 rollout 有直接借鉴 · [🌐 project](https://arxiv.org/abs/2608.06374)
- 🔥 **[WorldCycle: Self-Verifiable Reinforcement Learning for Long-Horizon Video World Models](https://arxiv.org/abs/2608.04964)** — *Gu, Bohai et al.* · `2026-08-05`
  > 核心：用可逆动作循环做自监督信号，spatial closure + temporal consistency 双奖励；意义：面向长时程规划的 physically grounded 视频世界模型——与 WM 评测四件套（KineBench 等）形成"训练侧"呼应 · [🌐 project](https://arxiv.org/abs/2608.02580)
- 🔥 **[WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reactivity](https://arxiv.org/abs/2608.02603)** — *Yang, Yuxue et al.* · `2026-08-03`
  > 机构：CUHK（16 作者协作）；核心：从"表观外观"到"内在反应性"两个层次分层评测，覆盖比 VBench/WorldModelBench 更广 · [🌐 project](https://huggingface.co/papers/2608.01735)
- 🔥 **[Weights or Skills? A Survey of Robot-Learning Techniques: from Action-Predicting Weights to Robots that Write their Own Skills](https://arxiv.org/abs/2608.01851)** — *Jena, Gaytri et al.* · `2026-08-03`
  > 核心：把机器人学习分成两条路线对照——冻结权重的 VLA vs 自己写可执行技能代码的 agent；梳理 code-as-policy 与技能发现中的自改进机制；指出空缺：机器人技能市场在适配、安全、标准化上仍是空白 · [🌐 project](https://arxiv.org/abs/2608.06374)
- 🔥 **[SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space](https://arxiv.org/abs/2608.01397)** — *Zhao, Ruiteng et al.* · `2026-08-02`
  > World Action Models (WAMs) couple action generation with prediction of future states.
- 🔥 **[Mental World Modeling](https://arxiv.org/abs/2607.27201)** — *Fei, Hao et al.* · `2026-07-29`
  > 核心：面向 agent 的心智世界模型，规划相关；Project: · [🌐 project](https://arxiv.org/abs/2607.23783)
- 🔥 **[Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control](https://arxiv.org/abs/2607.25337)** — *Bai, Jiaxin et al.* · `2026-07-28`
  > 机构：Hong Kong Baptist University；核心：给 JEPA-style WM 加"时序距离"意识，让 latent WM 在 planning 时更知道"离目标还有多远"，直接服务 MPC；对比 LeWM、CEM · [🌐 project](https://arxiv.org/abs/2607.26037)
- 🔥 **[Wonder: Video World Model Done Better](https://arxiv.org/abs/2607.26037)** — *Xu, Jiacong et al.* · `2026-07-28`
  > 机构：Adobe Research + Johns Hopkins University；核心：改进 video WM 的物理一致性 / 长时序生成，DiT 主干 + KV cache 复用 + DMD 蒸馏 + RPE 位置编码；内部数据集 "Inspatio-World"；宣称在物理一致性上比 Sora 系列 WM 更"真" · [🌐 project](https://arxiv.org/abs/2607.26037)
- 🔥 **[WorldDiT: A Unified Diffusion Architecture for World and Action Modeling](https://arxiv.org/abs/2607.23909)** — *Wang, Sen et al.* · `2026-07-27`
  > 机构：Bagel Labs；核心：把 WAM（World-Action Model）从两阶段（先 WM 后 policy）并成单一 DiT backbone——统一扩散架构同时预测未来帧与动作 · [🌐 project](https://arxiv.org/abs/2607.23909)
- 🔥 **[$N_0$-VTLA: Scaling Vision-Tactile-Language-Action Model with Latent Tactile Tokens](https://arxiv.org/abs/2607.23782)** — *NeoteAI Team et al.* · `2026-07-26`
  > 核心：把触觉 token 直接塞进 VLA 主干（视觉-触觉-语言-动作），规模化验证；与 7/26 N₀-Foundation 3 万小时触觉数据集配套；意义：触觉从"感知补丁"升格为 VLA/WAM 的第一等模态 · [🌐 project](https://arxiv.org/abs/2607.23782)
- 🔥 **[KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding](https://arxiv.org/abs/2607.19876)** — *Liu, Zeyu et al.* · `2026-07-22`
  > 机构：复旦 + NUS 等；核心：不依赖逆动力学模型，直接用运动学 grounding 评估 WM 生成的物理合理性（ManiSkill3 + FoundationPose 验证）——补上"WM 论文只报 FVD"的评测盲区 · [🌐 project](https://arxiv.org/abs/2607.19191)
- 🔥 **[Progress Reward Modeling for Robotic Learning: A Comprehensive Survey](https://arxiv.org/abs/2607.21655)** — *Zhang, Jianshu et al.* · `2026-07-22`
  > 机构：西北大学；核心：机器人学习奖励建模的首个系统 survey——覆盖进度奖励、稀疏奖励重塑、语言奖励、VLM 奖励等 · [🌐 project](https://arxiv.org/abs/2607.23909)
- 🔥 **[ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU](https://arxiv.org/abs/2607.19191)** — *Jiang, Fan et al.* · `2026-07-21`
  > We present ABot-World-0, an action-conditioned video world model for real-time, long-horizon closed-loop interaction, supported by a multi-source data infrastructure spanning AAA games, simulation engines, and internet …
- 🔥 **[Masked Visual Actions for Unified World Modeling](https://arxiv.org/abs/2607.19343)** — *Alzayer, Hadi et al.* · `2026-07-21`
  > 核心：把机器人动作投影为图像对齐稠密掩膜，让 video diffusion 直接读图作为动作条件，绕开 embodiment-specific action space；DROID/BEHAVIOR benchmark；意义：cross-embodiment VLA scale-up 的关键胶水层——用视觉 mask 代替动作向量 · [🌐 project](https://arxiv.org/abs/2607.15330)
- 🔥 **[AlayaWorld: Interactive Long-Horizon World Modeling -- Full Technical Report](https://arxiv.org/abs/2607.18367)** — *AlayaWorld Team et al.* · `2026-07-20`
  > 机构：Alaya Lab（商汤系背景）；热度：HF Trending 46 upvotes · [🌐 project](https://arxiv.org/abs/2607.18367)
- 🔥 **[AutoWorldModel-Bench: A State-Centric Benchmark for Automated World-Model Research](https://arxiv.org/abs/2608.11216)** — *Moodi, Marjan et al.* · `2026-07-20`
  > World modeling is an unsettled field: architectures, training objectives, and state representations interact in complex ways, and no single recipe dominates across environments.
- 🔥 **[DriftWorld: Fast World Modeling through Drifting](https://arxiv.org/abs/2607.15065)** — *Lu, Susie et al.* · `2026-07-16`
  > 机构：MIT + Harvard。；核心：提出 Drifting 范式——在特征空间（DINOv3）而非像素空间做世界模型 rollout，比 Ctrl-World 快 17 倍（Push-T 场景 479 倍 / 30+ fps）；配合 Action-Accentuated Drifting 与 Motion Weighting，FVD 从 168 降到 6.20。 · [🌐 project](https://arxiv.org/abs/2607.15330)
- 🔥 **[AlayaWorld: Long-Horizon and Playable Video World Generation](https://arxiv.org/abs/2607.06291)** — *AlayaWorld Team et al.* · `2026-07-07`
  > 之前 video WM 只做 RGB pixel（Cosmos / Sora），本文首次把 depth + optical flow 融进 WM 训练 = 几何 + 动力学 grounded WM；SOTA on real-world benchmarks
- 🔥 **[From Foundation to Application: Improving VLA Models in Practice](https://arxiv.org/abs/2607.06403)** — *Wu, Wei et al.* · `2026-07-07`
  > 一个 VLA 团队在 4 个月内 pretraining 数据从 ~5K 小时扩到 60K 小时 = 12× 扩量 = 说明中国大厂已 catching up 到"foundation VLA 数据规模"层次；跨 20 embodiment + whole-body DoF = "通用 VLA foundation"落地方向明确
- 🔥 **[RynnWorld-4D: 4D Embodied World Models for Robotic Manipulation](https://arxiv.org/abs/2607.06559)** — *Zhao, Haoyu et al.* · `2026-07-07`
  > 之前 video WM 只做 RGB pixel（Cosmos / Sora），本文首次把 depth + optical flow 融进 WM 训练 = 几何 + 动力学 grounded WM；SOTA on real-world benchmarks
- 🔥 **[MemLearner: Learning to Query Context memory for Video World Models](https://arxiv.org/abs/2606.31734)** — *Yu, Jiwen et al.* · `2026-06-30`
  > 规模上首个 100K+ 小时视频 WM（Sora 训练量级），OOD 泛化在 GalBot 真实机器人得到验证；与 6/17 [[QwenRobotWorld]] + 6/25 [[WorldValueModels]] + 6/26 [[QwenAgentWorld]] 形成"CN 大厂 world model 四大派系"
- 🔥 **[Orca: The World is in Your Mind](https://arxiv.org/abs/2606.30534)** — *Wang, Yihao et al.* · `2026-06-29`
  > 规模上首个 100K+ 小时视频 WM（Sora 训练量级），OOD 泛化在 GalBot 真实机器人得到验证；与 6/17 [[QwenRobotWorld]] + 6/25 [[WorldValueModels]] + 6/26 [[QwenAgentWorld]] 形成"CN 大厂 world model 四大派系" · [🌐 project](https://orca-wm.github.io/)
- 🔥 **[Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models](https://arxiv.org/abs/2606.25473)** — *Zheng, Kaiwen et al.* · `2026-06-24`
  > Autoregressive video diffusion with causal diffusion transformers has emerged as a major paradigm for real-time streaming video generation and action-conditioned interactive world models.
- 🔥 **[NavWM: A Unified Navigation World Model for Foresight-Driven Planning](https://arxiv.org/abs/2606.24101)** — *Mei, Yanghong et al.* · `2026-06-23` · 🏛️ **ECCV 2026**
  > Conventional visual navigation policies often struggle with myopic decision-making and mode collapse in complex environments.
- 🔥 **[World Value Models for Robotic Manipulation](https://arxiv.org/abs/2606.24742)** — *Wang, Zhihao et al.* · `2026-06-23`
  > 字节 Seed Robotics 首次正面 push robotics foundation model 战略论文 — 与 6 月 6/16 [[Mu0]] / 6/16 [[WEAVER]] / 6/17 [[QwenRobotWorld]] / 6/19 [[MemoryWAM]] / 6/24 [[WAMSurvey]] 同 WM/WAM 大家庭；与今日新闻 Zhou Chang 接管 ByteDance Seed …
- 🔥 **[Qwen-AgentWorld: Language World Models for General Agents](https://arxiv.org/abs/2606.24597)** — *Zuo, Yuxin et al.* · `2026-06-23`
  > 与 6/17 [[QwenRobotWorld]]（语言条件视频 WM for 具身）+ 6/19 [[QwenRobotNav]] + 6/25 [[WorldValueModels]]（ByteDance Seed） 形成 CN 大厂"语言 WM × WAM × Value Model"三大派系并立；阿里走"language WM for general agents"，字节走"World Value Model for manipulation"
- 🔥 **[Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents](https://arxiv.org/abs/2606.23085)** — *Zhang, Haoran et al.* · `2026-06-22`
  > Long-horizon tasks are common in real-world robotic deployments, yet failure detection for such tasks remains underexplored.
- 🔥 **[Sensorimotor World Models: Perception for Action via Inverse Dynamics](https://arxiv.org/abs/2606.20104)** — *Ivashkov, Petr et al.* · `2026-06-18`
  > Perception for action suggests that representations of the world should be shaped not by visual fidelity alone, but by their relevance for actions.
- 🔥 **[World Action Models: A Survey](https://arxiv.org/abs/2606.20781)** — *Shen, Qiuhong et al.* · `2026-06-18`
  > World Action Models (WAMs) are embodied predictive-action models that make a forecast of the future available to action.
- 🔥 **[DREAM-Chunk: Reactive Action Chunking with Latent World Model](https://arxiv.org/abs/2606.18589)** — *Chen, Wenxi et al.* · `2026-06-17`
  > Action chunking has become a common interface for vision-language-action (VLA) models, enabling low-frequency policy inference to drive high-frequency robot execution.
- 🔥 **[Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation](https://arxiv.org/abs/2606.18960)** — *Zheng, Zirui et al.* · `2026-06-17`
  > Action-conditioned world models have emerged as a promising paradigm for robot learning, offering a scalable alternative to costly real-world experimentation by generating action-consistent video rollouts.
- 🔥 **[WAM-RL: World-Action Model Reinforcement Learning with Reconstruction Rewards and Online Video SFT](https://arxiv.org/abs/2606.17906)** — *Qian, Zezhong et al.* · `2026-06-16`
  > 与 6/9 [[QGF]] (UCB+Physical Intelligence test-time gradient flow policy RL) + 6/10 [[MODIP]] (Sorbonne MBP DP RL) + 6/8 [[AdaWAM]] (清华 按需 dream) 同月内 "VLA/WAM + RL fine-tune"完整一线；千寻 Spirit v1. · [🌐 project](https://cvlab-kaist.github.io/Geometric-Action-Model)
- 🔥 **[Looped World Models](https://arxiv.org/abs/2606.18208)** — *Lu, Hongyuan Adam et al.* · `2026-06-16`
  > Current world models face a fundamental tension: faithful long-horizon simulation demands deep computation, but deeper models are expensive to deploy and prone to compounding errors.
- 🔥 **[DreamX-World 1.0: A General-Purpose Interactive World Model](https://arxiv.org/abs/2606.16993)** — *DreamX Team et al.* · `2026-06-15`
  > DreamX-World 1.0 is a general-purpose interactive text/image-to-video world model for controllable long-horizon generation.
- 🔥 **[Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation](https://arxiv.org/abs/2606.17030)** — *Zhang, Jie et al.* · `2026-06-15`
  > We introduce Qwen-RobotWorld, a language-conditioned video world model for embodied intelligence.
- 🔥 **[Geometric Action Model for Robot Policy Learning](https://arxiv.org/abs/2606.17046)** — *Han, Jisang et al.* · `2026-06-15`
  > Generalist robot policies must follow user instructions while reasoning about how objects, cameras, and robot actions interact in the 3D physical world.
- 🔥 **[Kairos: A Regret-Aware Native World-Action Model Stack for Physical AI](https://arxiv.org/abs/2606.16533)** — *Kairos Team et al.* · `2026-06-15`
  > Kairos（2606.16533，2026-06-16 提交，超窗口）：SJTU 系 4B "control-sufficient state" 世界-动作模型全栈——不保留全部视觉细节，只学控制所需七类变量（物体状态/空间关系/接触条件/任务进度/动作后果/失败风险/部署不确定性）；WMBench-Robot 9.30、RoboTwin 2.0 96.1、LIBERO-Plus 90. · [🌐 project](https://arxiv.org/abs/2607.19191)
- 🔥 **[VISA: VLM-Guided Instance Semantic Auditing for 3D Occupancy World Models](https://arxiv.org/abs/2606.13460)** — *Xian, Ruiqi et al.* · `2026-06-11`
  > Semantic 3D occupancy provides a voxelized world state for autonomous driving and robot decision making, but object and rare-class errors can affect free-space interpretation, collision checking, and temporal state …
- 🔥 **[NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation](https://arxiv.org/abs/2606.13494)** — *Azuma, Daichi et al.* · `2026-06-11`
  > Goal-conditioned visual navigation requires a robot to act under partial observability by anticipating how its motion will change the future egocentric view and whether that change brings it closer to the goal.
- 🔥 **[$\texttt{WEAVER}$, Better, Faster, Longer: An Effective World Model for Robotic Manipulation](https://arxiv.org/abs/2606.13672)** — *Jain, Arnav Kumar et al.* · `2026-06-11`
  > The potential impacts of world models (WMs, i.e., learned simulators) on robotics are far-reaching -- policy evaluation, policy improvement, and test-time planning -- all with limited real-world interaction.
- 🔥 **[$\mu_0$: A Scalable 3D Interaction-Trace World Model](https://arxiv.org/abs/2606.13769)** — *Lee, Seungjae et al.* · `2026-06-11`
  > 与 6/4 [[PiL-World]] (闭环 chunk-wise WM 评估) + 6/5 [[WLA]] (Unified W+L+A) + 6/8 [[AdaWAM]] (按需 dream) + 6/10 [[MotionWAM]] (humanoid 实时) + 6/16 [[ContactWorld]] (vision-tactile 系统分析) + 6/16 [[WEAVER]] …
- 🔥 **[ContactWorld: What Matters in Vision-Tactile World Models for Contact-Rich Manipulation](https://arxiv.org/abs/2606.13877)** — *Zhang, Zhiyuan et al.* · `2026-06-11`
  > Contact-rich manipulation requires world models to reason over complex contact dynamics from multimodal sensory observations.
- 🔥 **[iMaC: Translating Actions into Motion and Contact Images for Embodied World Models](https://arxiv.org/abs/2606.09813)** — *Wu, Zhenyu et al.* · `2026-06-08`
  > Embodied world models have emerged as a pivotal paradigm for visual robotic decision-making and interactive environment simulation.
- 🔥 **[Latent Spatial Memory for Video World Models](https://arxiv.org/abs/2606.09828)** — *Wang, Weijie et al.* · `2026-06-08`
  > Video world models that maintain 3D spatial consistency across generated frames typically rely on explicit point cloud memory constructed in RGB space.
- 🔥 **[STRIPS-WM: Learning Grounded Propositional STRIPS-style World Models from Images](https://arxiv.org/abs/2606.06832)** — *Ajith, Abhiroop et al.* · `2026-06-05`
  > Robots performing long-horizon visual manipulation observe high-dimensional images, but successful plans depend on action-relevant facts: what can be done now and what changes afterward.
- 🔥 **[Discrete-WAM: Unified Discrete Vision-Action Token Editing for World-Policy Learning](https://arxiv.org/abs/2606.05645)** — *Yao, Ziyang et al.* · `2026-06-04`
  > Autonomous driving requires reasoning about how ego actions shape the evolution of the surrounding world.
- 🔥 **[World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis](https://arxiv.org/abs/2606.05979)** — *Yang, Yi et al.* · `2026-06-04`
  > We propose world-language-action (WLA) models as a new class of embodied foundation models.
- 🔥 **[DexFuture: Hierarchical Future-State Visuomotor Targeting for Bimanual Dexterous Tool Use](https://arxiv.org/abs/2606.05699)** — *Li, Runfa Blark et al.* · `2026-06-04`
  > Bimanual dexterous tool use remains challenging for robots due to high-dimensional hand configurations and complex hand-tool-object dynamics and contact.
- 🔥 **[3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training](https://arxiv.org/abs/2606.04436)** — *Shi, Jiaxin et al.* · `2026-06-03`
  > We propose a 3D-thinking-guided co-training framework that enables vision-language-action (VLA) models to perform 3D spatial reasoning implicitly during action prediction.
- 🔥 **[OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics](https://arxiv.org/abs/2606.04463)** — *Wu, Zhuoyuan et al.* · `2026-06-03`
  > 精确动作条件的视频世界模型 OSCAR：用 2D 骨架渲染做统一 conditioning 跨机械臂 / 人手泛化，在单张 GH200 上微调 Cosmos-Predict2.5-2B；用于 RoboArena 策略的 virtual policy evaluation，仿真评测与真机结果高度相关，且比更大模型 / 更多 GPU 的基线在动作跟随、画质、运动一致性上都更好。 · [🌐 project](https://wuzy2115.github.io/oscar-project-page/)
- 🔥 **[MAD: Mapping-Aware World Models for Agile Quadrotor Flight](https://arxiv.org/abs/2606.04534)** — *Zhang, Xinhong et al.* · `2026-06-03`
  > 面向视觉四旋翼的几何感知世界模型 MAD：不重建原图，而是重建机体中心的占据 / 可见性栅格 + 本体状态，迫使 latent 编码局部几何与可见历史；真实森林飞行达 5.05 m/s，是模块化导航与端到端学习之间的实用折中。
- 🔥 **[CLAW: Learning Continuous Latent Action World Models via Adversarial Latent Regularization](https://arxiv.org/abs/2606.04130)** — *Ayalew, Tewodros et al.* · `2026-06-02`
  > We introduce CLAW, a fully end-to-end self-supervised framework for learning a world model jointly with continuous latent action representations directly from action-free videos.
- 🔥 **[Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models](https://arxiv.org/abs/2605.31158)** — *Lu, Jiacheng et al.* · `2026-05-29`
  > Interactive video world models generate video chunk by chunk in response to user-controlled camera movements, enabling applications such as real-time game simulation, virtual scene navigation, and embodied AI training.
- 🔥 **[stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation](https://arxiv.org/abs/2605.21800)** — *Maes, Lucas et al.* · `2026-05-20`
  > 世界模型研究的统一开源平台 stable-worldmodel (swm)，针对"各家造轮子 / 视频加载慢 / 缺标准泛化基准"三大痛点：Lance 高性能数据层（原生支持 MP4 / HDF5 / LeRobot）+ 经测试的主流 baseline 与 planning solver + 可控视觉 / 几何 / 物理变量的环境套件，支撑可复现的 in-silico 评测。
- 🔥 **[Reinforcing VLAs in Task-Agnostic World Models](https://arxiv.org/abs/2605.12334)** — *Wang, Yucen et al.* · `2026-05-12`
  > 把世界模型学习与下游任务彻底解耦以实现 zero-shot VLA 微调（RAW-Dream）：用 task-free 行为预训练的世界模型做 rollout + 现成 VLM 生成奖励，二者都任务无关；再加 dual-noise 验证过滤幻觉 rollout，证明通用物理先验可替代昂贵的任务相关数据。
- 🔥 **[World Action Models: The Next Frontier in Embodied AI](https://arxiv.org/abs/2605.12090)** — *Wang, Siyin et al.* · `2026-05-12`
  > 把 2025 H2 - 2026 H1 散落工作（NVIDIA Cosmos / DreamZero / LeVERB / PhysiFlow / HEX 等）收编进统一框架；为产业 + 学术界提供 共同的概念锚：Cascaded vs Joint
- 👀 **[HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation](https://arxiv.org/abs/2604.07993)** — *Bai, Shuanghao et al.* · `2026-04-09`
  > "首个 full-sized 双足人形的全身 VLA 框架"；Full-sized 双足是产业最难做的形态（重心高、足底支撑窄）
</details>
<details>
<summary>📜 <b>Earlier landmarks</b> · 1 paper</summary>

- 📜 **[Cosmos World Foundation Model Platform for Physical AI](https://arxiv.org/abs/2501.03575)** — *NVIDIA* · `2025-01-07`
  > NVIDIA's open world model platform for physical AI training data generation. · [🌐 project](https://www.nvidia.com/en-us/ai/cosmos/) · [💻 code](https://github.com/NVIDIA/Cosmos)
</details>

<sub>[⬆ back to top](#contents)</sub>

## <a id="manipulation"></a>🦾 Manipulation

*Grasping, dexterous, bimanual manipulation*
<details open>
<summary>🆕 <b>2026</b> · 21 papers</summary>

- 🔥 **[HiTac-WAM: A Hierarchical Tactile World Action Model for Contact-Rich Robot Manipulation](https://arxiv.org/abs/2608.19574)** — *Xue, Chao et al.* · `2026-08-20`
  > World action models jointly predict future visual observations and actions, whereas existing tactile-aware variants typically represent future touch as an image or latent stream without modeling the physical … · [🌐 project](https://carldegio.github.io/latent_action.github.io)
- 🔥 **[What Matters for Latent Actions in Robot Learning](https://arxiv.org/abs/2608.19613)** — *Bu, Xizhou et al.* · `2026-08-20`
  > Latent Action Models (LAMs) have emerged as a promising paradigm for enabling robot learning to leverage large-scale unlabeled videos through latent actions that serve as compact surrogates for physical actions. · [🌐 project](https://carldegio.github.io/latent_action.github.io)
- 🔥 **[GOAG: Generative and Object-Agnostic Grasp Planner for Dexterous Robotic Manipulation](https://arxiv.org/abs/2608.19759)** — *Merand, Julien et al.* · `2026-08-20`
  > Multifingered grasping is a crucial robotic skill, but current deep-learning grasp planners often struggle to generalize to new objects because they are trained on limited, object-specific datasets. · [🌐 project](https://cea-list.github.io/goagweb/)
- 🔥 **[CoToGrasp: Contact-Topology-Conditioned Dexterous Grasp Synthesis via Canonical Workspace Learning](https://arxiv.org/abs/2608.19776)** — *Merand, Julien et al.* · `2026-08-20`
  > Current dexterous grasp planners primarily optimize for physical stability, focusing on whether an object can be grasped rather than how it should be grasped to support downstream functional tasks. · [🌐 project](https://cea-list.github.io/goagweb/)
- 🔥 **[Koala Gripper: Co-designing Robotic Grippers and Data-Capture Devices for Scaling Dexterous Manipulation Learning](https://arxiv.org/abs/2608.20546)** — *Hajj-Ahmad, Amar et al.* · `2026-08-20`
  > As the demand for larger manipulation datasets grows, handheld robotic gripper data collection and the associated gripper designs become more vital. · [🌐 project](https://github.com/AMAP-ML/DreamX-Phi)
- 🔥 **[LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories](https://arxiv.org/abs/2608.18618)** — *Tang, Zhipeng et al.* · `2026-08-19`
  > Autonomous laboratories hold great promise for accelerating scientific discovery. · [🌐 project](https://shepherd1226.github.io/gigabrain-wbc-0.5/)
- 🔥 **[SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deformable-Object Manipulation](https://arxiv.org/abs/2608.18701)** — *Jing, Bowen et al.* · `2026-08-19`
  > Physical interaction quality is central to deformable-object manipulation, yet most benchmarks evaluate task success alone. A policy may complete the task while allowing slip or causing excessive compression.
- 🔥 **[Dream2Reward: Transition-Alignment Reward Models from Positive Demonstrations for Robotic Manipulation](https://arxiv.org/abs/2608.18787)** — *Zhang, Haoyu et al.* · `2026-08-19`
  > PartialBiGrasp（2608.19188，2026-08-19）部分点云双臂抓取 — https://arxiv.org/abs/2608.19188 ｜ Project: N/A；Dream2Reward（2608.18787，2026-08-19）—
- 🔥 **[RoboEdit: Turning Human Manipulation Videos into Scalable Robot Experience](https://arxiv.org/abs/2608.18948)** — *Guo, Yaowei et al.* · `2026-08-19`
  > Collecting robot hand-object interaction data is costly and embodiment-specific, yet abundant human-object videos remain unusable for robot training. · [🌐 project](https://adept-dexterity.github.io/)
- 🔥 **[PartialBiGrasp: Inferring Hidden Local Geometry for Bimanual Grasping from Partial Views](https://arxiv.org/abs/2608.19188)** — *Kaura, Ayush et al.* · `2026-08-19`
  > PartialBiGrasp（2608.19188，2026-08-19）部分点云双臂抓取 —
- 🔥 **[UniReflex: Plug-and-Play Force Control for Pretrained Generative Policies via Fast-Slow Reflex](https://arxiv.org/abs/2608.17432)** — *Huang, Yan et al.* · `2026-08-18`
  > Generative imitation learning policies excel at trajectory planning but lack closed-loop force regulation, while directly incorporating force modalities often requires redesigning or retraining the network. · [🌐 project](https://unireflex.github.io/)
- 🔥 **[Revisiting Open-Loop Execution in Robotics: Toward Reactive, Higher-Performing Policies](https://arxiv.org/abs/2608.15938)** — *Zeng, Michael et al.* · `2026-08-16`
  > Action chunking --- the practice of predicting a sequence of actions and executing a prefix open-loop --- has emerged as a key enabler of recent progress in imitation learning for robotic manipulation. · [🌐 project](https://revisiting-open-loop-action-chunking.github.io/)
- 🔥 **[Real-World Cooperative Bimanual Dexterous Grasp of Large Objects from Single-View Observations](https://arxiv.org/abs/2608.10383)** — *Li, Ziming et al.* · `2026-08-11`
  > Bimanual dexterous grasping of large objects is a critical challenge in robotic manipulation.
- 🔥 **[$N_0$-TWAM: Scaling Tactile-Native World-Action Model for Contact-Rich Manipulation](https://arxiv.org/abs/2607.23783)** — *NeoteAI Team et al.* · `2026-07-26`
  > 核心：面向 contact-rich manipulation，首个把"触觉→未来状态预测"闭环的 WAM；意义：与 [[FeelWorld]]（CASIA+BAAI）方向共振——WM 的触觉分支正在形成完整栈 · [🌐 project](https://arxiv.org/abs/2607.23782)
- 🔥 **[Robots Acquire Manipulation Skills in Seconds from a Single Human Video](https://arxiv.org/abs/2607.20033)** — *Chen, Guangyan et al.* · `2026-07-22`
  > 机构：北京理工大学 + 清华大学；核心：从单条人类演示视频提取手-物交互轨迹 → DTW 对齐 → AWDA 域自适应映射到机器人本体。"one-shot"在推理期成立，但 Stage 2 训练仍需 5,847 对人-机配对数据；真机成功率约 62% · [🌐 project](https://arxiv.org/abs/2607.20033)
- 🔥 **[Dreaming when Necessary: Advancing World Action Models with Adaptive Multi-Modal Reasoning](https://arxiv.org/abs/2606.07089)** — *Tang, Yinzhou et al.* · `2026-06-05`
  > "always dream" 是 WAM 范式的原罪 — Cosmos3 14B 跑一次 rollout 算力可怕；AdaWAM 按需 dream 是把 WAM 从研究推到部署的必经一步
- 🔥 **[EaDex: A Cross-Embodiment Dexterous Manipulation Framework from Low-Cost Demonstrations](https://arxiv.org/abs/2606.03268)** — *Zhao, Qian et al.* · `2026-06-02`
  > 低成本跨本体灵巧操作框架 EaDex：单 RGB-D 相机捕捉人手 + MANO 建模重定向生成示范，contact-reward 动态退火从"跟示范"过渡到"自主优化"；9 个跨本体设置下比无退火基线相对提升 55.3%。
- 🔥 **[Affordance2Action: Task-Conditioned Scene-level Affordance Grounding for Real-Time Manipulation](https://arxiv.org/abs/2606.04172)** — *Liu, Litao et al.* · `2026-06-02`
  > Task-conditioned manipulation requires grounding instructions to task-relevant functional parts rather than object categories.
- 🔥 **[Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation](https://arxiv.org/abs/2605.21811)** — *Wu, Albert et al.* · `2026-05-20`
  > 用 pullback 控制屏障函数把任务流形的安全约束转成构型空间加速度的线性约束，高层策略可注入低维残差运动而始终保持安全；23-DOF Franka-Allegro 抓取成功率 92.5%，并首次实现模型化掌心朝下手内翻转 >360°。
- 🔥 **[Hand-in-the-Loop: Improving VLA Policies for Dexterous Manipulation via Seamless Hand-Arm Intervention](https://arxiv.org/abs/2605.15157)** — *Li, Zhuohang et al.* · `2026-05-14`
  > 解决 high-DoF 灵巧操作的 IIL 命令匹配难题；给 ROBOTERA、银河通用、智元等"teleop 路线"公司提供新工具
- 🔥 **[Towards Robotic Dexterous Hand Intelligence: A Survey](https://arxiv.org/abs/2605.13925)** — *Zhao, Weiguang et al.* · `2026-05-13`
  > 当前最系统的机器人灵巧手综述：从硬件（驱动 / 传动 / 感知及代表手型的力-柔顺-带宽权衡）、控制与学习方法（按范式分组、按时间梳理演进）、数据与评测三方面整合，厘清领域发展轨迹与关键开放问题。
</details>
<details>
<summary>📜 <b>Earlier landmarks</b> · 2 papers</summary>

- 👀 **[H2R-Grounder: A Paired-Data-Free Paradigm for Translating Human Interaction Videos into Physically Grounded Robot Videos](https://arxiv.org/abs/2512.09406)** — *Ci, Hai et al.* · `2025-12-10`
  > Robots that learn manipulation skills from everyday human videos could acquire broad capabilities without tedious robot data collection.
- 📜 **[ALOHA Unleashed: A Simple Recipe for Robot Dexterity](https://arxiv.org/abs/2410.13126)** — *Zhao et al.* · `2024-10-17`
  > Diffusion policy + large-scale teleop data for dexterous bimanual manipulation — community baseline. · [🌐 project](https://aloha-unleashed.github.io)
</details>

<sub>[⬆ back to top](#contents)</sub>

## <a id="locomotion"></a>🦿 Locomotion

*Humanoid, quadruped, bipedal walking and running*
<details open>
<summary>🆕 <b>2026</b> · 19 papers</summary>

- 🔥 **[MILD: Tractable Terrain Modeling for Learning Improved Bipedal Locomotion on Deformable Surfaces](https://arxiv.org/abs/2608.19955)** — *Luo, Zeren et al.* · `2026-08-20`
  > Enabling robots to walk on yielding terrain is vital for applications ranging from disaster response to planetary exploration. · [🌐 project](https://cea-list.github.io/cotograspweb/)
- 🔥 **[DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation](https://arxiv.org/abs/2608.20114)** — *Ma, Siyuan et al.* · `2026-08-20`
  > Mobile manipulation requires a robot to predict how locomotion and arm motion jointly alter future observations and control. · [🌐 project](https://humanoidtennis.github.io/AdaPT/)
- 🔥 **[Robust Brachiation on a Life-Sized Dual-Arm Robot Using Waypoint-Guided Reinforcement Learning](https://arxiv.org/abs/2608.17320)** — *Iwata, Ayumu et al.* · `2026-08-18`
  > Brachiation is a form of locomotion in which primates move primarily using their arms, enabling traversal in environments without footholds. · [🌐 project](https://tengbo-yu.github.io/PRISM/)
- 🔥 **[HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent RL](https://arxiv.org/abs/2608.16837)** — *Gu, Langzhe et al.* · `2026-08-17`
  > Humanoid robots hold great promise as general-purpose agents in human-centered environments, yet generalist vision-language-action (VLA) foundation models are not readily applicable to humanoid whole-body … · [🌐 project](https://tau0-vla.github.io/)
- 🔥 **[Tac4Loco: Learning Spatiotemporal Plantar Pressure Representations for Humanoid Locomotion](https://arxiv.org/abs/2608.15766)** — *Liu, Ziyun et al.* · `2026-08-16`
  > SparkVLA（2608.16172，8/17）— 链接：https://arxiv.org/abs/2608.16172 ｜ Project: N/A；Tac4Loco（2608.15766，8/16）— 链接：
- 🔥 **[HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments](https://arxiv.org/abs/2608.12860)** — *Pham, Quan-Dung et al.* · `2026-08-13`
  > arXiv：2608.12860 · 已校验投稿日：2026-08-13；机构：Quan-Dung Pham, Anh Dao, The-Anh Nguyen, Minh Nguyen-Dinh, Phuong Nam Dang, Tri Pham, Hung Tran, Bach Dao 等，作者群在越南；两台机器人被匿名为 "Internal-A / Internal-B"，暗示有未披露的产业合作方。abs 页未列机构，不做进一步断言。 · [🌐 project](https://humanoid-vln.github.io/)
- 🔥 **[Flex-$\pi$: A Multi-Stream World-Action Model with Compute Flexibility](https://arxiv.org/abs/2608.10860)** — *Yan, Ge et al.* · `2026-08-11`
  > World-action models (WAMs) predict the future to act better, but nearly all of them predict only RGB latents, trained purely for pixel reconstruction, with no explicit signal for the 3D geometry or object semantics …
- 🔥 **[Learning How the World Evolves: Extrapolative Video World Models via Latent Dynamics Reasoning](https://arxiv.org/abs/2608.09926)** — *Li, Haodong et al.* · `2026-08-10`
  > The world evolves following its dynamics, i.e., its laws of motion. However, leading video diffusion models largely fit the pixels without modeling how the pixels transit over time.
- 🔥 **[StairMaster: Learning to Conquer Risky Hollow Stairs for Agile Quadrupedal Robots](https://arxiv.org/abs/2606.25765)** — *Tang, Xincheng et al.* · `2026-06-24`
  > Climbing hollow stairs remains a challenging problem for quadruped robots due to the high risk of leg trapping, severe depth sparsity, and high-frequency depth-sensing noise.
- 🔥 **[DynaWM: Dynamics-Aware Distillation with World Model and Momentum Targets for Smooth Locomotion over Continuous Stairs](https://arxiv.org/abs/2606.24089)** — *Hou, Haidong et al.* · `2026-06-23`
  > Recent advances in control have enabled bipedal-wheeled robots to traverse slopes and single-step obstacles, yet long staircase traversal remains challenging as current teacher-student frameworks suffer from weakened …
- 🔥 **[SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour](https://arxiv.org/abs/2606.19928)** — *Lan, Kaixin et al.* · `2026-06-18`
  > While latent world models enable the proactive predictions required for extreme parkour, their purely data-driven nature forces them to redundantly encode left-right symmetric interactions as independent patterns.
- 🔥 **[MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.09215)** — *Zheng, Jia et al.* · `2026-06-08`
  > 6/4 PiL-World（闭环 chunk-wise WM 评估） + 6/5 WLA（unified W+L+A） + 6/8 AdaWAM（按需 dream） + 6/10 MotionWAM（实时 humanoid 落地） = WAM 系 2026 H1 四大演化路径完整；MotionWAM 把 WAM 从研究推到"humanoid 实时控制"赛道 — 给 Figure 03 + 1X NEO + 智元远征 A3 + 银河通用 … · [🌐 project](https://kairos-homeworld.github.io/)
- 🔥 **[T-GMP: Terrain-conditioned Generative Motion Priors for Versatile and Natural Humanoid Locomotion](https://arxiv.org/abs/2606.06944)** — *Guo, Junhong et al.* · `2026-06-05`
  > Achieving both anthropomorphic naturalness and robust terrain traversal remains a fundamental challenge in humanoid locomotion.
- 🔥 **[TAGA: Terrain-aware Active Gaze Learning for Generalizable Agile Humanoid Locomotion](https://arxiv.org/abs/2606.05880)** — *Li, Peizhuo et al.* · `2026-06-04`
  > Agile humanoid locomotion across diverse challenging terrain demands both wide perceptual coverage and precise local geometry understanding.
- 🔥 **[HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers](https://arxiv.org/abs/2606.06493)** — *Yang, Lizhi et al.* · `2026-06-04`
  > For a humanoid robot to be deployed in the real world, the choice of command space (i.e., the interface between task planning and whole-body control) is crucial.
- 🔥 **[CoRe-MoE: Contrastive Reweighted Mixture of Experts for Multi-Terrain Humanoid Locomotion with Gait Adaptation](https://arxiv.org/abs/2606.04718)** — *Huang, Kailun et al.* · `2026-06-03`
  > Humans primarily rely on walking and running to traverse complex terrains, without resorting to unnecessarily complex motion patterns.
- 🔥 **[M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking](https://arxiv.org/abs/2606.04829)** — *Lu, Zuxing et al.* · `2026-06-03`
  > Building a general-purpose whole-body controller is essential for enabling diverse motion capabilities in humanoid robots across a wide range of downstream tasks, including locomotion and loco-manipulation.
- 🔥 **[SPRINT: Efficient Spectral Priors for Humanoid Athletic Sprints](https://arxiv.org/abs/2605.28549)** — *Wei, Yantong et al.* · `2026-05-27`
  > 6 m/s 是当前 humanoid 短跑公开数字第一档（vs Tesla Optimus Gen 3 行走 1.2 m/s、Figure 03 慢跑 2 m/s）；Spectral priors 是"frequency domain reference 库"思路 — 比 motion capture demos 数据效率高很多
- 🔥 **[Learning to Evolve: Multi-modal Interactive Fields for Robust Humanoid Navigation in Dynamic Environments](https://arxiv.org/abs/2605.21935)** — *Jiang, Peifeng et al.* · `2026-05-21`
  > 面向人形的多模态交互场（MIF）：不确定性感知 3DGS 抑制步态模糊 + 差异触发的空间记忆更新，专治移动导致的感知畸变；真实动态办公室里重定位成功率 12%→94%，语义内存占用降 91.4%。
</details>

<sub>[⬆ back to top](#contents)</sub>

## <a id="teleoperation"></a>🕹️ Teleoperation

*VR, wearable, and exoskeleton-based data collection*
<details open>
<summary>🆕 <b>2026</b> · 18 papers</summary>

- 🔥 **[EXIMO: VLM Guided Exploration of VLA Policies](https://arxiv.org/abs/2608.19891)** — *Sukhija, Bhavya et al.* · `2026-08-20`
  > How to efficiently finetune robot policies to learn new tasks on the fly? · [🌐 project](https://carldegio.github.io/latent_action.github.io)
- 🔥 **[PRISM: Precision and contact-rich Real-world Industrial Skill dataset with Multimodal sensing](https://arxiv.org/abs/2608.17962)** — *Yu, Tengbo et al.* · `2026-08-18`
  > Recent progress in robotic learning has been fueled by large-scale datasets collected in everyday environments. · [🌐 project](https://unireflex.github.io/)
- 🔥 **[GigaBrain-WBC-0.5: A Behavior World Model for Robust Whole-Body Control with Environment Interaction](https://arxiv.org/abs/2608.18234)** — *Cheng, Ziyang et al.* · `2026-08-18`
  > Whole-body motion tracking policies turn a humanoid into a robust control interface: the teleoperator---or an upstream model---only supplies a coarse movement intent, while the low-level policy keeps the robot balanced … · [🌐 project](https://adept-dexterity.github.io/)
- 🔥 **[Pre-training Visual Dexterity in Simulation](https://arxiv.org/abs/2608.15917)** — *Kamat, Sarthak et al.* · `2026-08-16`
  > Large-scale pre-training has made robot policy fine-tuning increasingly data-efficient, but this progress has largely been driven by datasets and embodiments built around simple parallel-jaw grippers. · [🌐 project](https://gigabrain0.github.io/)
- 🔥 **[NestDex: Nested Policy Learning with Copilot Assisted Teleoperation for Dexterous Manipulation](https://arxiv.org/abs/2608.13362)** — *Zhao, James et al.* · `2026-08-13`
  > arXiv：2608.13362 · 已校验投稿日：2026-08-13；机构：James Zhao, Jinhe Tang, Mingyuan Ba, Weiming Zhi —— CMU Robotics Institute
- 🔥 **[RynnWorld-Teleop: An Action-Conditioned World Model for Digital Teleoperation](https://arxiv.org/abs/2607.06558)** — *Zhao, Haoyu et al.* · `2026-07-07`
  > 之前 video WM 只做 RGB pixel（Cosmos / Sora），本文首次把 depth + optical flow 融进 WM 训练 = 几何 + 动力学 grounded WM；SOTA on real-world benchmarks
- 🔥 **[HumanScale: Egocentric Human Video Can Outperform Real-Robot Data for Embodied Pretraining](https://arxiv.org/abs/2606.20521)** — *Ma, Juncheng et al.* · `2026-06-18`
  > Embodied foundation models are expected to benefit from data scaling like large language models, but face a much tighter data bottleneck.
- 🔥 **[Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement](https://arxiv.org/abs/2606.18953)** — *Kim, Kinam et al.* · `2026-06-17`
  > 与 6/9 [[QGF]] (UCB + Physical Intelligence) + 6/10 [[MODIP]] (Sorbonne) + 6/17 [[WAMRL]] (清华 + 北大) + 今日 OCRR 形成 "VLA + RL fine-tune"完整一线；zero-shot sim-to-real 是 Figure / 1X / 智元 / 银河 / 小鹏 IRON real-world 部署最大成本省略点
- 🔥 **[ORCA: A Platform for Open-Source Dexterity Research](https://arxiv.org/abs/2606.14561)** — *Capuano, Francesco et al.* · `2026-06-12`
  > Robotics manipulation research increasingly focuses on two-finger parallel grippers for their effectiveness, affordability, and ease of teleoperation.
- 🔥 **[Targeting World Models to Compromise Robot Learning Pipelines](https://arxiv.org/abs/2606.09499)** — *Rathbun, Ethan et al.* · `2026-06-08`
  > World models have recently seen a rapid growth in both their popularity and capability as more data efficient tools for generating robot training data or simulating real world environments, with many works proposing …
- 🔥 **[PiL-World: A Chunk-Wise World Model for VLA Policy-in-the-Loop Evaluation](https://arxiv.org/abs/2606.05773)** — *Ma, Chong et al.* · `2026-06-04`
  > 首个面向闭环 VLA 评测的 chunk-wise 世界模型：现有评测多是沿预采轨迹的开环预测，PiL-World 交替"VLA 推理 ↔ 世界模型预测"生成与 rollout 一致的多视角未来观测，无需每步真机执行；还能从失败轨迹学习，三个双臂任务上把真机与仿真成功率的误差从 63.2% 降到 12.0%。
- 🔥 **[LadderMan: Learning Humanoid Perceptive Ladder Climbing](https://arxiv.org/abs/2606.05873)** — *Zhao, Siheng et al.* · `2026-06-04`
  > 让人形稳健爬各种梯子并在梯上操作：两阶段流水线——混合运动跟踪从单条参考动作学多个爬梯专家，蒸馏成统一的深度视觉运动策略；借视觉基础模型弥合深度 sim-to-real，zero-shot 迁移到真机。
- 🔥 **[MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.06139)** — *Taouil, Ilyass et al.* · `2026-06-04`
  > We present MotionDisco, a framework that discovers contact-rich, long-horizon humanoid loco-manipulation motions from scratch, without relying on teleoperation or motion retargeting from human demonstrations.
- 🔥 **[VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training](https://arxiv.org/abs/2606.04708)** — *Yang, Siyuan et al.* · `2026-06-03`
  > 打通 UMI 数据训 VLA 的两大鸿沟——腕部鱼眼畸变 OOD + 人采轨迹违反运动学：UMI-VQA（首个鱼眼 VQA 数据集）做视觉对齐 + 物理校验流水线给轨迹打分过滤不可行动作 + 两阶段联合训练。
- 🔥 **[HapTile: A Haptic-Informed Vision-Tactile-Language-Action Dataset for Contact-Rich Imitation Learning](https://arxiv.org/abs/2606.04825)** — *Alian, Amirhosein et al.* · `2026-06-03`
  > 接触-grounded 视触觉操作数据集 HapTile，在两端嵌入物理交互感知：机器人指尖触觉 + 遥操作端的力反馈示范；覆盖抓放 / 折叠 / 按压 / 堆叠等接触密集技能，每条配语言指令 + 同步视触觉观测与动作轨迹。
- 🔥 **[GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](https://arxiv.org/abs/2606.05160)** — *Xie, Tianyi et al.* · `2026-06-03`
  > 部署前全程虚拟的人形 loco-manipulation 数据生成流水线 GRAIL：组合 3D 资产 + 仿真场景 + 视频基础模型先验，从已知几何 / 尺度的 3D 配置出发重建 metric 4D 人-物交互再重定向到机器人；产出 2 万+ 序列，真机抓取 84%、爬楼 90%。
- 🔥 **[MonoDuo: Using One Robot Arm to Learn Bimanual Policies](https://arxiv.org/abs/2605.29298)** — *Bajamahal, Sandeep et al.* · `2026-05-28`
  > Bimanual coordination is essential for many real-world manipulation tasks, yet learning bimanual robot policies is limited by the scarcity of bimanual robots and datasets.
- 👀 **[Towards Human-Like Manipulation through RL-Augmented Teleoperation and Mixture-of-Dexterous-Experts VLA](https://arxiv.org/abs/2603.08122)** — *Tang, Tutian et al.* · `2026-03-09`
  > 把 VLA 从低自由度抓放推进到双手灵巧"手内操作"：RL 原子技能 IMCopilot 既辅助遥操采数据又当底层执行原语，MoDE-VLA 用残差注入融合力 / 触觉而不损预训练知识；接触密集任务成功率翻倍。
</details>
<details>
<summary>📜 <b>Earlier landmarks</b> · 2 papers</summary>

- 📜 **[OpenTeleVision: Open-source Immersive Teleoperation with Stereo Visual Feedback](https://arxiv.org/abs/2407.01512)** — *Cheng et al.* · `2024-07-01`
  > Open-source VR teleoperation system with binocular stereo feedback — community reference. · [🌐 project](https://robot-tv.github.io) · [💻 code](https://github.com/OpenTeleVision/TeleVision)
- 📜 **[Mobile ALOHA: Learning Bimanual Mobile Manipulation](https://arxiv.org/abs/2401.02117)** — *Fu et al.* · `2024-01-04`
  > $32k mobile teleop platform — community baseline for whole-body teleop. · [🌐 project](https://mobile-aloha.github.io) · [💻 code](https://github.com/MarkFzp/mobile-aloha)
</details>

<sub>[⬆ back to top](#contents)</sub>

## <a id="sim2real"></a>🌉 Sim-to-Real

*Domain randomization, sim-to-real transfer, deployment*
<details open>
<summary>🆕 <b>2026</b> · 8 papers</summary>

- 🔥 **[Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking](https://arxiv.org/abs/2608.20087)** — *Huang, Tao et al.* · `2026-08-20`
  > Humanoid robots have recently demonstrated promising capabilities in real-world ball sports. However, achieving professional motion styles while maintaining strong task performance remains challenging. · [🌐 project](https://humanoidtennis.github.io/AdaPT/)
- 🔥 **[ADEPT: Accelerating Dexterity via Pre-Training and Post-Training using Reinforcement Learning](https://arxiv.org/abs/2608.19182)** — *Lee, Jayjun et al.* · `2026-08-19`
  > We introduce Accelerating Dexterity via Pre-Training (ADEPT), a large-scale reinforcement learning (RL) framework for learning sim-to-real transferable dexterity across high degree-of-freedom (DoF) robot embodiments … · [🌐 project](https://adept-dexterity.github.io/)
- 🔥 **[Tactile Sim2Real without Tactile Simulation via Bottlenecked Latent Reconstruction](https://arxiv.org/abs/2608.15897)** — *Yang, Fan et al.* · `2026-08-16`
  > Robot sensor designs, particularly tactile sensors, are highly diverse and evolve rapidly.
- 🔥 **[SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors](https://arxiv.org/abs/2606.23444)** — *Rao, Pratyaksh et al.* · `2026-06-22`
  > Accurate dynamics models are critical for informed decision-making in robotic systems, particularly for agile aerial vehicles operating under uncertainty.
- 🔥 **[Mana: Dexterous Manipulation of Articulated Tools](https://arxiv.org/abs/2606.13677)** — *Yin, Zhao-Heng et al.* · `2026-06-11`
  > Articulated tool manipulation remains a major challenge in dexterous robotics due to the need to coordinate internal degrees of freedom and contact-rich interactions.
- 🔥 **[Video2Sim2Real: Full-Stack Autonomous Dexterous Skill Acquisition from a Single Human Video](https://arxiv.org/abs/2606.08828)** — *Han, Yunhai et al.* · `2026-06-07`
  > Human manipulation videos are a convenient and intuitive source for robot learning. However, directly transferring human dexterity to robots remains challenging due to perception errors and embodiment gap.
- 🔥 **[TAM: Torque Adaptation Module for Robust Motion Transfer in Manipulation](https://arxiv.org/abs/2606.06218)** — *Son, Dongwon et al.* · `2026-06-04`
  > A policy tuned for one robot often behaves differently on another, whether due to the sim-to-real gap, unknown payloads, or the differing dynamics of two instances of the same robot.
- 🔥 **[Imagine2Real: Towards Zero-shot Humanoid-Object Interaction via Video Generative Priors](https://arxiv.org/abs/2605.22272)** — *Chen, Jiahe et al.* · `2026-05-21`
  > 解决 humanoid 与物体交互的"3D 数据从哪来"瓶颈；用 video 生成模型作为 prior，与 NVIDIA Cosmos / GR00T-Dreams 同思路但场景更细：HOI 而非通用 manipulation
</details>
<details>
<summary>📜 <b>Earlier landmarks</b> · 1 paper</summary>

- 👀 **[LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction](https://arxiv.org/abs/2506.13751)** — *Xue, Haoru et al.* · `2025-06-16`
  > 首个 sim-to-real-ready 的人形全身控制（WBC）vision-language 闭环基准（150+ 任务 / 10 类）+ 分层 latent VLA 框架 LeVERB：高层学 latent 动作词表、低层 RL 全身控制器执行；zero-shot 总成功率 58.5%，比朴素分层 VLA 高 7.8×。
</details>

<sub>[⬆ back to top](#contents)</sub>

## <a id="scene"></a>🌍 3D Scene Understanding

*NeRF, Gaussian Splatting, segmentation for robotics*
<details open>
<summary>🆕 <b>2026</b> · 3 papers</summary>

- 🔥 **[WorldOlympiad: Can Your World Model Survive a Triathlon?](https://arxiv.org/abs/2606.11129)** — *Zhao, Yuke et al.* · `2026-06-09`
  > We introduce WorldOlympiad, a benchmark for diagnosing video-based world models across physical faithfulness, geometric consistency, and interaction fidelity.
- 🔥 **[GeoSem-WAM: Geometry- and Semantic-Aware World Action Models](https://arxiv.org/abs/2606.03188)** — *Ma, Fulong et al.* · `2026-06-02`
  > Recent World Action Models (WAMs) have demonstrated impressive capabilities in embodied decision-making.
- 🔥 **[PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects](https://arxiv.org/abs/2605.21572)** — *Cao, Ziang et al.* · `2026-05-20`
  > 为 robotic policy learning 和 simulation-ready scene generation 提供原料；减少 robotics 仿真数据手工建模成本
</details>
<details>
<summary>📜 <b>Earlier landmarks</b> · 1 paper</summary>

- 📜 **[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2308.04079)** — *Kerbl et al.* · `2023-08-08`
  > Real-time, high-quality radiance field rendering — now ubiquitous in 3D scene understanding pipelines. · [🌐 project](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) · [💻 code](https://github.com/graphdeco-inria/gaussian-splatting)
</details>

<sub>[⬆ back to top](#contents)</sub>

## <a id="navigation"></a>🧭 Navigation & Mobility

*Visual navigation, embodied QA, mobile robots*
<details open>
<summary>🆕 <b>2026</b> · 3 papers</summary>

- 🔥 **[Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation](https://arxiv.org/abs/2608.17512)** — *Feng, Hongyan et al.* · `2026-08-18`
  > Although Large Vision-Language Models (VLMs) have significantly advanced embodied navigation, their direct deployment remains challenging, as existing methods often force VLMs into unnatural action spaces that misalign …
- 🔥 **[ERQA-Plus: A Diagnostic Benchmark for Reasoning in Embodied AI](https://arxiv.org/abs/2606.17639)** — *Yang, Hong et al.* · `2026-06-16`
  > Generalist embodied agents require more than object recognition: they must reason about spatial relations, actions, procedures, human intentions, environmental constraints, and commonsense consequences from situated …
- 🔥 **[Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System](https://arxiv.org/abs/2606.18112)** — *Zhang, Jiazhao et al.* · `2026-06-16`
  > Agentic navigation systems require a base navigation model whose observation strategy can be externally reconfigured at inference time, because instruction following, object search, target tracking, and autonomous …
</details>

<sub>[⬆ back to top](#contents)</sub>

## <a id="rl-il"></a>🎯 RL & Imitation Learning

*Diffusion policies, behavior cloning, RL for robotics*
<details open>
<summary>🆕 <b>2026</b> · 1 paper</summary>

- 🔥 **[RoboStriker: Latent-Space Strategic Games for Autonomous Humanoid Boxing](https://arxiv.org/abs/2608.16195)** — *Yin, Kangning et al.* · `2026-08-17`
  > Achieving human-level competitive intelligence and physical agility in humanoid robots remains a profound challenge, particularly in contact-rich and highly dynamic tasks such as boxing. · [🌐 project](https://grange007.github.io/HAF)
</details>
<details>
<summary>📜 <b>Earlier landmarks</b> · 1 paper</summary>

- 📜 **[Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137)** — *Chi et al.* · `2023-03-07`
  > Action-space diffusion — now the default visuomotor policy baseline. · [🌐 project](https://diffusion-policy.cs.columbia.edu) · [💻 code](https://github.com/real-stanford/diffusion_policy)
</details>

<sub>[⬆ back to top](#contents)</sub>

## <a id="datasets"></a>📦 Datasets

*Robot trajectories, demonstrations, scene datasets*
<details>
<summary>📁 <b>Manipulation Demonstrations</b> · 5 datasets</summary>

- **[Open X-Embodiment (RT-X)](https://robotics-transformer-x.github.io)** — Cross-embodiment robot dataset spanning 22 robot types, 1M+ trajectories. · *1M+ episodes* · [paper](https://arxiv.org/abs/2310.08864) · [code](https://github.com/google-deepmind/open_x_embodiment)
- **[DROID](https://droid-dataset.github.io)** — Diverse real-world manipulation dataset from 564 scenes, 13 institutions. · *76k demonstrations* · [paper](https://arxiv.org/abs/2403.12945)
- **[BridgeData V2](https://rail-berkeley.github.io/bridgedata)** — Large-scale tabletop manipulation dataset for generalization research. · *60k trajectories* · [paper](https://arxiv.org/abs/2308.12952)
- **[ARIO (All Robots In One)](https://imaei.github.io/project_pages/ario/)** — Unified cross-embodiment robot learning dataset. · [paper](https://arxiv.org/abs/2408.10899)
- **[AgiBot World](https://agibot-world.com)** — Large-scale humanoid manipulation dataset from AgiBot's real-world deployments.

</details>
<details>
<summary>📁 <b>3D Scenes</b> · 4 datasets</summary>

- **[Habitat-Matterport 3D (HM3D)](https://aihabitat.org/datasets/hm3d/)** — 1000+ photorealistic indoor 3D scenes for embodied AI training. · [paper](https://arxiv.org/abs/2109.08238)
- **[ScanNet++](https://kaldir.vc.in.tum.de/scannetpp/)** — 1006 high-fidelity indoor scenes with sub-mm geometry & DSLR captures. · [paper](https://arxiv.org/abs/2308.11417)
- **[Replica Dataset](https://github.com/facebookresearch/Replica-Dataset)** — 18 high-quality reconstructions of indoor spaces (Meta Reality Labs). · [paper](https://arxiv.org/abs/1906.05797)
- **[3D-FRONT / 3D-FUTURE](https://tianchi.aliyun.com/specials/promotion/alibaba-3d-scene-dataset)** — Synthetic indoor scenes with high-quality furniture CAD models (Alibaba). · [paper](https://arxiv.org/abs/2011.09127)

</details>
<details>
<summary>📁 <b>Egocentric / Human Video</b> · 3 datasets</summary>

- **[Ego4D](https://ego4d-data.org)** — 3,670 hours of egocentric video across 74 worldwide locations. · *3,670 hours* · [paper](https://arxiv.org/abs/2110.07058)
- **[EPIC-KITCHENS-100](https://epic-kitchens.github.io/2024)** — Long-form egocentric kitchen activity dataset for action understanding. · *100 hours* · [paper](https://arxiv.org/abs/2006.13256)
- **[HOI4D](https://hoi4d.github.io)** — 4D egocentric dataset for category-level human-object interaction. · [paper](https://arxiv.org/abs/2203.01577)

</details>
<details>
<summary>📁 <b>Motion Capture / Whole-Body</b> · 2 datasets</summary>

- **[AMASS](https://amass.is.tue.mpg.de)** — Unifies 15 mocap datasets in a common SMPL skeleton — 40+ hours of motion. · [paper](https://arxiv.org/abs/1904.03278)
- **[HumanML3D](https://github.com/EricGuo5513/HumanML3D)** — 14,616 motions with text annotations for motion-language tasks. · [paper](https://arxiv.org/abs/2202.04257) · [code](https://github.com/EricGuo5513/HumanML3D)

</details>
<details>
<summary>📁 <b>Sim-Generated</b> · 2 datasets</summary>

- **[RoboCasa-Gen](https://robocasa.ai)** — Large-scale procedurally generated household tasks rendered in MuJoCo. · [paper](https://arxiv.org/abs/2406.02523)
- **[PhysXVerse](https://arxiv.org/abs/2605.21572)** — First general-purpose simulation-ready 3D dataset (released with PhysX-Omni, 2026). · [paper](https://arxiv.org/abs/2605.21572)

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
<summary>📐 <b>Manipulation</b> · 5 benchmarks</summary>

- **[CALVIN](http://calvin.cs.uni-freiburg.de)** — Long-horizon, language-conditioned manipulation benchmark. · [paper](https://arxiv.org/abs/2112.03227) · [code](https://github.com/mees/calvin)
- **[Meta-World](https://meta-world.github.io)** — 50 manipulation tasks for multi-task and meta-RL evaluation. · [paper](https://arxiv.org/abs/1910.10897) · [code](https://github.com/Farama-Foundation/Metaworld)
- **[LIBERO](https://libero-project.github.io)** — Lifelong robot learning benchmark — 130 manipulation tasks across 4 suites. · [paper](https://arxiv.org/abs/2306.03310)
- **[RLBench](https://sites.google.com/view/rlbench)** — 100 vision-guided manipulation tasks with CoppeliaSim. · [paper](https://arxiv.org/abs/1909.12271) · [code](https://github.com/stepjam/RLBench)
- **[AliasBench](https://arxiv.org/abs/2605.14712)** — Benchmark probing multimodal-imitation ambiguity in VLA (used in IntentVLA 2026). · [paper](https://arxiv.org/abs/2605.14712)

</details>
<details>
<summary>📐 <b>Navigation</b> · 3 benchmarks</summary>

- **[ProcTHOR](https://procthor.allenai.org)** — 10,000+ procedurally generated household scenes for embodied AI. · [paper](https://arxiv.org/abs/2206.06994)
- **[Habitat ObjectNav](https://aihabitat.org/challenge/2023/)** — Standard object-goal navigation in HM3D / MP3D. · [paper](https://arxiv.org/abs/2210.13063)
- **[OVMM](https://arxiv.org/abs/2310.13724)** — Open-vocabulary mobile manipulation benchmark (Habitat 3.0). · [paper](https://arxiv.org/abs/2310.13724)

</details>
<details>
<summary>📐 <b>Locomotion / Whole-Body</b> · 1 benchmarks</summary>

- **[HumanoidBench](https://humanoid-bench.github.io)** — MuJoCo-based humanoid locomotion + whole-body manipulation benchmark. · [paper](https://arxiv.org/abs/2403.10506) · [code](https://github.com/carlosferrazza/humanoid-bench)

</details>
<details>
<summary>📐 <b>VLA Generalization & OOD</b> · 2 benchmarks</summary>

- **[SimplerEnv](https://simpler-env.github.io)** — Reproducible real-to-sim eval suite — measures VLA gap between real and sim deployment. · [paper](https://arxiv.org/abs/2405.05941) · [code](https://github.com/simpler-env/SimplerEnv)
- **[PhysX-Bench](https://arxiv.org/abs/2605.21572)** — 6-dim evaluation (geometry/scale/material/affordance/kinematics/function) — released with PhysX-Omni, 2026. · [paper](https://arxiv.org/abs/2605.21572)

</details>
<details>
<summary>📐 <b>Multi-Skill / Long-Horizon</b> · 2 benchmarks</summary>

- **[BEHAVIOR-1K](https://behavior.stanford.edu/behavior-1k)** — 1,000 long-horizon household activities in OmniGibson — the largest activity benchmark. · [paper](https://arxiv.org/abs/2403.09227)
- **[RoboCasa-Bench](https://robocasa.ai)** — 100+ atomic + composite household tasks running on RoboCasa-Gen scenes. · [paper](https://arxiv.org/abs/2406.02523)

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
*No entries yet — [contribute one!](CONTRIBUTING.md)*

<sub>[⬆ back to top](#contents)</sub>


---

## 🆕 Recent additions (last 45 days)

<details>
<summary><b>Show 15 recently added papers</b></summary>

- 🔥 **[PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration](https://arxiv.org/abs/2608.21031)** `2026-08-21` · *Lin, Chen-Yu et al.* · [🌐](https://physcap.github.io) · `vla`
- 🔥 **[HiTac-WAM: A Hierarchical Tactile World Action Model for Contact-Rich Robot Manipulation](https://arxiv.org/abs/2608.19574)** `2026-08-20` · *Xue, Chao et al.* · [🌐](https://carldegio.github.io/latent_action.github.io) · `manipulation`
- 🔥 **[What Matters for Latent Actions in Robot Learning](https://arxiv.org/abs/2608.19613)** `2026-08-20` · *Bu, Xizhou et al.* · [🌐](https://carldegio.github.io/latent_action.github.io) · `manipulation`
- 🔥 **[GOAG: Generative and Object-Agnostic Grasp Planner for Dexterous Robotic Manipulation](https://arxiv.org/abs/2608.19759)** `2026-08-20` · *Merand, Julien et al.* · [🌐](https://cea-list.github.io/goagweb/) · `manipulation`
- 🔥 **[CoToGrasp: Contact-Topology-Conditioned Dexterous Grasp Synthesis via Canonical Workspace Learning](https://arxiv.org/abs/2608.19776)** `2026-08-20` · *Merand, Julien et al.* · [🌐](https://cea-list.github.io/goagweb/) · `manipulation`
- 🔥 **[EXIMO: VLM Guided Exploration of VLA Policies](https://arxiv.org/abs/2608.19891)** `2026-08-20` · *Sukhija, Bhavya et al.* · [🌐](https://carldegio.github.io/latent_action.github.io) · `teleoperation`
- 🔥 **[MILD: Tractable Terrain Modeling for Learning Improved Bipedal Locomotion on Deformable Surfaces](https://arxiv.org/abs/2608.19955)** `2026-08-20` · *Luo, Zeren et al.* · [🌐](https://cea-list.github.io/cotograspweb/) · `locomotion`
- 🔥 **[Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking](https://arxiv.org/abs/2608.20087)** `2026-08-20` · *Huang, Tao et al.* · [🌐](https://humanoidtennis.github.io/AdaPT/) · `sim2real`
- 🔥 **[DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation](https://arxiv.org/abs/2608.20114)** `2026-08-20` · *Ma, Siyuan et al.* · [🌐](https://humanoidtennis.github.io/AdaPT/) · `locomotion`
- 🔥 **[Koala Gripper: Co-designing Robotic Grippers and Data-Capture Devices for Scaling Dexterous Manipulation Learning](https://arxiv.org/abs/2608.20546)** `2026-08-20` · *Hajj-Ahmad, Amar et al.* · [🌐](https://github.com/AMAP-ML/DreamX-Phi) · `manipulation`
- 🔥 **[The Embodiment Gap in Robot Foundation Models](https://arxiv.org/abs/2608.18433)** `2026-08-19` · *Domae, Yukiyasu et al.* · [🌐](https://shepherd1226.github.io/gigabrain-wbc-0.5/) · `foundation-models`
- 🔥 **[LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories](https://arxiv.org/abs/2608.18618)** `2026-08-19` · *Tang, Zhipeng et al.* · [🌐](https://shepherd1226.github.io/gigabrain-wbc-0.5/) · `manipulation`
- 🔥 **[SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deformable-Object Manipulation](https://arxiv.org/abs/2608.18701)** `2026-08-19` · *Jing, Bowen et al.* · `manipulation`
- 🔥 **[Dream2Reward: Transition-Alignment Reward Models from Positive Demonstrations for Robotic Manipulation](https://arxiv.org/abs/2608.18787)** `2026-08-19` · *Zhang, Haoyu et al.* · `manipulation`
- 🔥 **[RoboEdit: Turning Human Manipulation Videos into Scalable Robot Experience](https://arxiv.org/abs/2608.18948)** `2026-08-19` · *Guo, Yaowei et al.* · [🌐](https://adept-dexterity.github.io/) · `manipulation`

</details>

> 🤖 *Auto-rolled forward from `data/papers.yaml` every push. Older entries naturally drop out of this window but remain in their category section.*

---

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=junyuan-fang/awesome-physical-ai&type=Date)](https://star-history.com/#junyuan-fang/awesome-physical-ai&Date)

## 🤝 Contributing

This list is auto-fed from a daily paper aggregation pipeline, but PRs are very welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

**Inclusion criteria / 收录标准** (keep the list high-signal):
- ✅ Has a public paper (arXiv/venue) **or** open-source code / project page
- ✅ Comes with a one-line description of its contribution / 一句话说明贡献
- ✅ Relevant to physical AI: embodiment, manipulation, locomotion, world models, sim-to-real, etc.
- ❌ No paywalled-only resources, vague "we're building AGI" startups, or dead links

## 📜 License

[MIT](LICENSE) © 2026 [@junyuan-fang](https://github.com/junyuan-fang)
