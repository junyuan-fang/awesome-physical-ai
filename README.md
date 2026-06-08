# Awesome Physical AI

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Maintained](https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg)](https://github.com/junyuan-fang/awesome-physical-ai/commits/master)
![Last updated](https://img.shields.io/badge/Last%20updated-2026--06--08-blue.svg)
![Papers](https://img.shields.io/badge/Papers-63-success.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> A **continuously maintained** list of resources on Physical AI, Embodied AI, and Humanoid Robotics — focused on **2025-2026+** state-of-the-art.
> 一个**持续自动更新**的具身智能 / 物理 AI / 人形机器人资源列表（论文描述中英双语，面向中文社区）。

🤖 **Auto-updated** from arXiv + HuggingFace daily papers via a custom pipeline · 每日自动同步.
📊 **63** papers · 🏢 **19** companies · 🎮 **7** simulators · 📦 **16** datasets · 📊 **13** benchmarks

> 💡 **Legend / 图例**: 🔥 must-read · 👀 worth-knowing · 📜 classic landmark · 🏛️ accepted venue · 🌐 project · 💻 code. Click any **▸ section** to expand / 点击展开折叠区.

---

## 🚀 Where to Start

New to the field? Pick a track / 新手按背景选择起点：

- 🧠 **From an ML / LLM background** → start with [Foundation Models](#foundation-models) (VLA & world models), then [RL & Imitation Learning](#rl-il).
- 🦾 **Building a manipulation system** → [Manipulation](#manipulation) → [Teleoperation](#teleoperation) (data collection) → [Datasets](#datasets).
- 🌉 **Caring about sim-to-real** → [Simulators](#simulators) → [Sim-to-Real](#sim2real) → [Benchmarks](#benchmarks).
- 🦿 **Into humanoids / locomotion** → [Locomotion](#locomotion) → [Companies & Industry](#companies).
- 📈 **Tracking the industry** → [Companies & Industry](#companies) (valuation tracker + US/CN/EU players).

---

## Contents

**📚 Research**
· [🤖 Foundation Models for Robotics](#foundation-models) · [🦾 Manipulation](#manipulation) · [🦿 Locomotion](#locomotion) · [🕹️ Teleoperation](#teleoperation) · [🌉 Sim-to-Real](#sim2real) · [🌍 3D Scene Understanding](#scene) · [🧭 Navigation & Mobility](#navigation) · [🎯 RL & Imitation Learning](#rl-il) 
**🧰 Resources**
· [📦 Datasets](#datasets) · [🎮 Simulators](#simulators) · [📊 Benchmarks](#benchmarks) · [🛠️ Tools & Libraries](#tools) · [📚 Tutorials & Surveys](#tutorials) 
**🏢 Industry**
· [🏢 Companies & Industry](#companies) 
---

## <a id="foundation-models"></a>🤖 Foundation Models for Robotics

*Generalist policies, VLA, world models*
<details open>
<summary>🆕 <b>2026</b> · 11 papers</summary>

- 🔥 **[Discrete-WAM: Unified Discrete Vision-Action Token Editing for World-Policy Learning](https://arxiv.org/abs/2606.05645)** — *Yao, Ziyang et al.* · `2026-06-04`
  > Autonomous driving requires reasoning about how ego actions shape the evolution of the surrounding world. However, most end-to-end methods rely on direct state-to-action mappings, capturing correlations without explicitly modeling...
- 🔥 **[World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis](https://arxiv.org/abs/2606.05979)** — *Yang, Yi et al.* · `2026-06-04`
  > We propose world-language-action (WLA) models as a new class of embodied foundation models. WLA takes textual instructions, images, and robot states as inputs to jointly predict textual subtasks, subgoal images, and robot actions,...
- 🔥 **[3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training](https://arxiv.org/abs/2606.04436)** — *Shi, Jiaxin et al.* · `2026-06-03`
  > We propose a 3D-thinking-guided co-training framework that enables vision-language-action (VLA) models to perform 3D spatial reasoning implicitly during action prediction. Our core insight is that 3D geometry perception and 3D spatial...
- 🔥 **[OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics](https://arxiv.org/abs/2606.04463)** — *Wu, Zhuoyuan et al.* · `2026-06-03`
  > 与昨日讨论的 罗剑岚 Critic 主线 + 6/3 GN0 三件套 同根：用 WAM 做 virtual policy evaluation = 把"评价模型"具体化；拿 NVIDIA Cosmos-Predict2.5 做底座是这一波 Cosmos 生态首批应用 · [🌐 project](https://qizekun.github.io/humanoid-gpt/)
- 🔥 **[MAD: Mapping-Aware World Models for Agile Quadrotor Flight](https://arxiv.org/abs/2606.04534)** — *Zhang, Xinhong et al.* · `2026-06-03`
  > Agile quadrotor flight in cluttered scenes requires more than a reactive mapping from a depth image to a control command: the vehicle must remember which regions have been observed, infer nearby occupied space, and act under partial...
- 🔥 **[CLAW: Learning Continuous Latent Action World Models via Adversarial Latent Regularization](https://arxiv.org/abs/2606.04130)** — *Ayalew, Tewodros et al.* · `2026-06-02`
  > We introduce CLAW, a fully end-to-end self-supervised framework for learning a world model jointly with continuous latent action representations directly from action-free videos. Our approach leverages adversarial latent regularization...
- 🔥 **[Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models](https://arxiv.org/abs/2605.31158)** — *Lu, Jiacheng et al.* · `2026-05-29`
  > Interactive video world models generate video chunk by chunk in response to user-controlled camera movements, enabling applications such as real-time game simulation, virtual scene navigation, and embodied AI training. However, scaling to...
- 🔥 **[stable-worldmodel: A Reproducibility-First Infrastructure for World Models](https://arxiv.org/abs/2605.21800)** — *Anonymous* · `2026-05-20`
  > 给 WAM 阵营（昨天提的 RAW-Dream、DreamZero、PhysiFlow 等）提供统一基础设施；推动 world model 研究从"各家造轮子"走向 reproducibility-first
- 🔥 **[RAW-Dream: Reward-Aligned World Model Without Task Data](https://arxiv.org/abs/2605.12334)** — *Anonymous* · `2026-05-12`
  > 把"训世界模型也要任务数据"这个束缚拆掉；是 Joint WAM 阵营最新代表（昨天 WAM survey 给的 taxonomy）
- 🔥 **[World Action Model Survey: Cascaded vs Joint Taxonomy](https://arxiv.org/abs/2605.12090)** — *Anonymous* · `2026-05-12`
  > 把 2025 H2 - 2026 H1 散落工作（NVIDIA Cosmos / DreamZero / LeVERB / PhysiFlow / HEX 等）收编进统一框架；为产业 + 学术界提供 共同的概念锚：Cascaded vs Joint
- 👀 **[HEX: Humanoid Embodied World Model](https://arxiv.org/abs/2604.07993)** — *Anonymous* · `2026-04-09`
  > "首个 full-sized 双足人形的全身 VLA 框架"；Full-sized 双足是产业最难做的形态（重心高、足底支撑窄）
</details>
<details>
<summary>📜 <b>Earlier landmarks</b> · 1 paper</summary>

- 📜 **[Cosmos World Foundation Model Platform for Physical AI](https://arxiv.org/abs/2501.03575)** — *NVIDIA* · `2025-01-07`
  > NVIDIA's open world model platform for physical AI training data generation. · [🌐 project](https://www.nvidia.com/en-us/ai/cosmos/) · [💻 code](https://github.com/NVIDIA/Cosmos)
</details>

## <a id="manipulation"></a>🦾 Manipulation

*Grasping, dexterous, bimanual manipulation*
<details open>
<summary>🆕 <b>2026</b> · 5 papers</summary>

- 🔥 **[EaDex: A Cross-Embodiment Dexterous Manipulation Framework from Low-Cost Demonstrations](https://arxiv.org/abs/2606.03268)** — *Zhao, Qian et al.* · `2026-06-02`
  > Dexterous manipulation learning has long been hindered by the high costs of data and training, as pure reinforcement learning typically requires large-scale interactive exploration and imitation learning depends on high-quality...
- 🔥 **[Affordance2Action: Task-Conditioned Scene-level Affordance Grounding for Real-Time Manipulation](https://arxiv.org/abs/2606.04172)** — *Liu, Litao et al.* · `2026-06-02`
  > Task-conditioned manipulation requires grounding instructions to task-relevant functional parts rather than object categories. This setting is scene-dependent and often one-to-many in cluttered scenes: the same object may afford different...
- 🔥 **[Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation](https://arxiv.org/abs/2605.21811)** — *Wu, Albert et al.* · `2026-05-20`
  > Robotic dexterous manipulation requires continuously reconciling objectives and constraints defined on heterogeneous geometric spaces: a robot controlled on a $\mathbb{R}^7$ configuration manifold may need to track end effector poses on...
- 🔥 **[HandITL: Interactive Imitation Learning for High-DoF Dexterous Manipulation](https://arxiv.org/abs/2605.15157)** — *Anonymous* · `2026-05-14`
  > 解决 high-DoF 灵巧操作的 IIL 命令匹配难题；给 ROBOTERA、银河通用、智元等"teleop 路线"公司提供新工具
- 🔥 **[Dexterous Hand Research: A Comprehensive Survey (2026)](https://arxiv.org/abs/2605.13925)** — *Anonymous* · `2026-05-13`
  > 这是当前最完整的灵巧手研究综述，与最近几篇 VLA / WAM survey 形成完整文献地图；触觉 modality（与 TARS VLTA / Sanctuary Phoenix Gen 8 / HandITL 一线产业 / 论文趋势呼应）被作为下一阶段关键
</details>
<details>
<summary>📜 <b>Earlier landmarks</b> · 1 paper</summary>

- 📜 **[ALOHA Unleashed: A Simple Recipe for Robot Dexterity](https://arxiv.org/abs/2410.13126)** — *Zhao et al.* · `2024-10-17`
  > Diffusion policy + large-scale teleop data for dexterous bimanual manipulation — community baseline. · [🌐 project](https://aloha-unleashed.github.io)
</details>

## <a id="locomotion"></a>🦿 Locomotion

*Humanoid, quadruped, bipedal walking and running*
<details open>
<summary>🆕 <b>2026</b> · 6 papers</summary>

- 🔥 **[TAGA: Terrain-aware Active Gaze Learning for Generalizable Agile Humanoid Locomotion](https://arxiv.org/abs/2606.05880)** — *Li, Peizhuo et al.* · `2026-06-04`
  > Agile humanoid locomotion across diverse challenging terrain demands both wide perceptual coverage and precise local geometry understanding. Motivated by the way humans selectively look at relevant terrain during locomotion, we introduce...
- 🔥 **[HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers](https://arxiv.org/abs/2606.06493)** — *Yang, Lizhi et al.* · `2026-06-04`
  > For a humanoid robot to be deployed in the real world, the choice of command space (i.e., the interface between task planning and whole-body control) is crucial. Existing whole-body controllers typically demand dense kinematic or spatial...
- 🔥 **[CoRe-MoE: Contrastive Reweighted Mixture of Experts for Multi-Terrain Humanoid Locomotion with Gait Adaptation](https://arxiv.org/abs/2606.04718)** — *Huang, Kailun et al.* · `2026-06-03`
  > Humans primarily rely on walking and running to traverse complex terrains, without resorting to unnecessarily complex motion patterns. Similarly, humanoid robots should achieve smooth transitions between walking and running while...
- 🔥 **[M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking](https://arxiv.org/abs/2606.04829)** — *Lu, Zuxing et al.* · `2026-06-03`
  > Building a general-purpose whole-body controller is essential for enabling diverse motion capabilities in humanoid robots across a wide range of downstream tasks, including locomotion and loco-manipulation. Different tasks rely on...
- 🔥 **[SPRINT: Spectral-Priors Reinforced Humanoid Sprinting](https://arxiv.org/abs/2605.28549)** — *Anonymous* · `2026-05-27`
  > 6 m/s 是当前 humanoid 短跑公开数字第一档（vs Tesla Optimus Gen 3 行走 1.2 m/s、Figure 03 慢跑 2 m/s）；Spectral priors 是"frequency domain reference 库"思路 — 比 motion capture demos 数据效率高很多
- 🔥 **[Learning to Evolve: Multi-modal Interactive Fields for Robust Humanoid Navigation in Dynamic Environments](https://arxiv.org/abs/2605.21935)** — *Jiang, Peifeng et al.* · `2026-05-21`
  > Safe manipulation-oriented navigation for humanoid robots requires scene memory that remains reliable under locomotion-induced perceptual distortion, environmental changes, and interaction-level geometric safety constraints. Existing...
</details>

## <a id="teleoperation"></a>🕹️ Teleoperation

*VR, wearable, and exoskeleton-based data collection*
<details open>
<summary>🆕 <b>2026</b> · 8 papers</summary>

- 🔥 **[PiL-World: A Chunk-Wise World Model for VLA Policy-in-the-Loop Evaluation](https://arxiv.org/abs/2606.05773)** — *Ma, Chong et al.* · `2026-06-04`
  > 与 5/30 罗剑岚 τ0-WM "Critic + WM 评估" 主线精确同根；与 6/3 OSCAR (Cosmos-Predict2.5 + 2D 骨架 conditioning) virtual policy evaluation 互补 · [🌐 project](https://qizekun.github.io/humanoid-gpt/)
- 🔥 **[LadderMan: Learning Humanoid Perceptive Ladder Climbing](https://arxiv.org/abs/2606.05873)** — *Zhao, Siheng et al.* · `2026-06-04`
  > Humanoid robots hold great promise for operating in human-centered environments, yet ladder climbing remains one of the most challenging tasks due to sparse footholds and handholds, complex whole-body coordination, and sensitivity to...
- 🔥 **[MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.06139)** — *Taouil, Ilyass et al.* · `2026-06-04`
  > We present MotionDisco, a framework that discovers contact-rich, long-horizon humanoid loco-manipulation motions from scratch, without relying on teleoperation or motion retargeting from human demonstrations. This is challenging because...
- 🔥 **[VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training](https://arxiv.org/abs/2606.04708)** — *Yang, Siyuan et al.* · `2026-06-03`
  > Universal Manipulation Interface (UMI) enables scalable real-world robot data collection without hardware-specific teleoperation, yet leveraging UMI data to train large-scale Vision-Language-Action (VLA) models remains fundamentally...
- 🔥 **[HapTile: A Haptic-Informed Vision-Tactile-Language-Action Dataset for Contact-Rich Imitation Learning](https://arxiv.org/abs/2606.04825)** — *Alian, Amirhosein et al.* · `2026-06-03`
  > Despite the importance of tactile sensing for reliable manipulation, most existing Vision-Language-Action (VLA) datasets remain vision-only, and those that do incorporate tactile information typically lack the joint combination of task...
- 🔥 **[GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](https://arxiv.org/abs/2606.05160)** — *Xie, Tianyi et al.* · `2026-06-03`
  > Scaling humanoid loco-manipulation requires robot-compatible demonstrations across diverse objects, whole-body motions, and scene geometries, but teleoperation and motion capture are difficult to scale because each collection depends on...
- 🔥 **[MonoDuo: Using One Robot Arm to Learn Bimanual Policies](https://arxiv.org/abs/2605.29298)** — *Bajamahal, Sandeep et al.* · `2026-05-28`
  > Bimanual coordination is essential for many real-world manipulation tasks, yet learning bimanual robot policies is limited by the scarcity of bimanual robots and datasets. Single-arm robots, however, are widely available in research labs....
- 👀 **[Towards Human-Like Manipulation through RL-Augmented Teleoperation and Mixture-of-Dexterous-Experts VLA](https://arxiv.org/abs/2603.08122)** — *Tang, Tutian et al.* · `2026-03-09`
  > While Vision-Language-Action (VLA) models have demonstrated remarkable success in robotic manipulation, their application has largely been confined to low-degree-of-freedom end-effectors performing simple, vision-guided pick-and-place...
</details>
<details>
<summary>📜 <b>Earlier landmarks</b> · 2 papers</summary>

- 📜 **[OpenTeleVision: Open-source Immersive Teleoperation with Stereo Visual Feedback](https://arxiv.org/abs/2407.01512)** — *Cheng et al.* · `2024-07-01`
  > Open-source VR teleoperation system with binocular stereo feedback — community reference. · [🌐 project](https://robot-tv.github.io) · [💻 code](https://github.com/OpenTeleVision/TeleVision)
- 📜 **[Mobile ALOHA: Learning Bimanual Mobile Manipulation](https://arxiv.org/abs/2401.02117)** — *Fu et al.* · `2024-01-04`
  > $32k mobile teleop platform — community baseline for whole-body teleop. · [🌐 project](https://mobile-aloha.github.io) · [💻 code](https://github.com/MarkFzp/mobile-aloha)
</details>

## <a id="sim2real"></a>🌉 Sim-to-Real

*Domain randomization, sim-to-real transfer, deployment*
<details open>
<summary>🆕 <b>2026</b> · 1 paper</summary>

- 🔥 **[Imagine2Real: Video-Generated HOI Priors for Zero-Shot Humanoid Sim2Real](https://arxiv.org/abs/2605.22272)** — *Anonymous* · `2026-05-21`
  > 解决 humanoid 与物体交互的"3D 数据从哪来"瓶颈；用 video 生成模型作为 prior，与 NVIDIA Cosmos / GR00T-Dreams 同思路但场景更细：HOI 而非通用 manipulation
</details>
<details>
<summary>📜 <b>Earlier landmarks</b> · 1 paper</summary>

- 👀 **[LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction](https://arxiv.org/abs/2506.13751)** — *Xue, Haoru et al.* · `2025-06-16`
  > Vision-language-action (VLA) models have demonstrated strong semantic understanding and zero-shot generalization, yet most existing systems assume an accurate low-level controller with hand-crafted action "vocabulary" such as end-effector...
</details>

## <a id="scene"></a>🌍 3D Scene Understanding

*NeRF, Gaussian Splatting, segmentation for robotics*
<details open>
<summary>🆕 <b>2026</b> · 2 papers</summary>

- 🔥 **[GeoSem-WAM: Geometry- and Semantic-Aware World Action Models](https://arxiv.org/abs/2606.03188)** — *Ma, Fulong et al.* · `2026-06-02`
  > Recent World Action Models (WAMs) have demonstrated impressive capabilities in embodied decision-making. However, whether their effectiveness stems from explicit future imagination during inference or representation learning induced by...
- 🔥 **[PhysX-Omni: Simulation-Ready 3D Generation for Robotics](https://arxiv.org/abs/2605.21572)** — *Anonymous* · `2026-05-20`
  > 为 robotic policy learning 和 simulation-ready scene generation 提供原料；减少 robotics 仿真数据手工建模成本
</details>
<details>
<summary>📜 <b>Earlier landmarks</b> · 1 paper</summary>

- 📜 **[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2308.04079)** — *Kerbl et al.* · `2023-08-08`
  > Real-time, high-quality radiance field rendering — now ubiquitous in 3D scene understanding pipelines. · [🌐 project](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) · [💻 code](https://github.com/graphdeco-inria/gaussian-splatting)
</details>

## <a id="navigation"></a>🧭 Navigation & Mobility

*Visual navigation, embodied QA, mobile robots*
*No entries yet — [contribute one!](CONTRIBUTING.md)*

## <a id="rl-il"></a>🎯 RL & Imitation Learning

*Diffusion policies, behavior cloning, RL for robotics*
<details>
<summary>📜 <b>Earlier landmarks</b> · 1 paper</summary>

- 📜 **[Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137)** — *Chi et al.* · `2023-03-07`
  > Action-space diffusion — now the default visuomotor policy baseline. · [🌐 project](https://diffusion-policy.cs.columbia.edu) · [💻 code](https://github.com/real-stanford/diffusion_policy)
</details>

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

## <a id="simulators"></a>🎮 Simulators

*Isaac Sim, MuJoCo, Genesis, and friends*
- **[Isaac Lab](https://isaac-sim.github.io/IsaacLab)** — NVIDIA's modular RL training framework built on Isaac Sim. · [code](https://github.com/isaac-sim/IsaacLab)
- **[Isaac Sim](https://developer.nvidia.com/isaac/sim)** — NVIDIA's full robot simulator with photorealistic rendering.
- **[Genesis](https://genesis-embodied-ai.github.io)** — Universal physics engine for robotics — built in pure Python, 43M FPS claim. · [paper](https://arxiv.org/abs/2412.04268) · [code](https://github.com/Genesis-Embodied-AI/Genesis)
- **[MuJoCo MJX](https://mujoco.readthedocs.io/en/latest/mjx.html)** — GPU/TPU-accelerated JAX-based version of MuJoCo for massive parallel rollouts. · [code](https://github.com/google-deepmind/mujoco)
- **[Habitat 3.0](https://aihabitat.org)** — Photorealistic embodied AI sim with humans, navigation + manipulation. · [paper](https://arxiv.org/abs/2310.13724) · [code](https://github.com/facebookresearch/habitat-sim)
- **[RoboCasa](https://robocasa.ai)** — Large-scale household simulation framework on top of MuJoCo. · [paper](https://arxiv.org/abs/2406.02523) · [code](https://github.com/robocasa/robocasa)
- **[ManiSkill 3](https://maniskill.ai)** — GPU-parallelized manipulation skill learning sim. · [code](https://github.com/haosulab/ManiSkill)

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

## <a id="tools"></a>🛠️ Tools & Libraries

*Open-source frameworks for building embodied AI*
- **[LeRobot](https://huggingface.co/lerobot)** — Hugging Face's end-to-end robotics framework — datasets, models, hardware. · ✅ open-source · [💻 code](https://github.com/huggingface/lerobot)
- **[Diffusion Policy](https://github.com/real-stanford/diffusion_policy)** — Reference implementation of action-space diffusion policies. · ✅ open-source · [💻 code](https://github.com/real-stanford/diffusion_policy) · [📄 paper](https://arxiv.org/abs/2303.04137)
- **[OpenVLA](https://openvla.github.io)** — Open-source 7B Vision-Language-Action foundation model. · ✅ open-source · [💻 code](https://github.com/openvla/openvla)
- **[AnyGrasp SDK](https://graspnet.net/anygrasp.html)** — General object grasping in cluttered scenes. · ✅ open-source · [💻 code](https://github.com/graspnet/anygrasp_sdk) · [📄 paper](https://arxiv.org/abs/2212.08333)
- **[Curobo](https://curobo.org)** — NVIDIA's GPU-accelerated motion planning library. · ✅ open-source · [💻 code](https://github.com/NVlabs/curobo)
- **[nvdiffrast](https://nvlabs.github.io/nvdiffrast/)** — Modular differentiable rendering primitives from NVIDIA. · ✅ open-source · [💻 code](https://github.com/NVlabs/nvdiffrast)

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
## <a id="tutorials"></a>📚 Tutorials & Surveys

*Surveys, books, and tutorial materials*
*No entries yet — [contribute one!](CONTRIBUTING.md)*


---

## 🆕 Recent additions (last 45 days)

<details>
<summary><b>Show 15 recently added papers</b></summary>

- 🔥 **[Discrete-WAM: Unified Discrete Vision-Action Token Editing for World-Policy Learning](https://arxiv.org/abs/2606.05645)** `2026-06-04` · *Yao, Ziyang et al.* · `foundation-models`
- 🔥 **[PiL-World: A Chunk-Wise World Model for VLA Policy-in-the-Loop Evaluation](https://arxiv.org/abs/2606.05773)** `2026-06-04` · *Ma, Chong et al.* · [🌐](https://qizekun.github.io/humanoid-gpt/) · `teleoperation`
- 🔥 **[LadderMan: Learning Humanoid Perceptive Ladder Climbing](https://arxiv.org/abs/2606.05873)** `2026-06-04` · *Zhao, Siheng et al.* · `teleoperation`
- 🔥 **[TAGA: Terrain-aware Active Gaze Learning for Generalizable Agile Humanoid Locomotion](https://arxiv.org/abs/2606.05880)** `2026-06-04` · *Li, Peizhuo et al.* · `locomotion`
- 🔥 **[World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis](https://arxiv.org/abs/2606.05979)** `2026-06-04` · *Yang, Yi et al.* · `foundation-models`
- 🔥 **[MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.06139)** `2026-06-04` · *Taouil, Ilyass et al.* · `teleoperation`
- 🔥 **[AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding](https://arxiv.org/abs/2606.06155)** `2026-06-04` · *Yu, Qize et al.* · `vla`
- 🔥 **[TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies](https://arxiv.org/abs/2606.06491)** `2026-06-04` · *Jing, Dong et al.* · `vla`
- 🔥 **[HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers](https://arxiv.org/abs/2606.06493)** `2026-06-04` · *Yang, Lizhi et al.* · `locomotion`
- 🔥 **[3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training](https://arxiv.org/abs/2606.04436)** `2026-06-03` · *Shi, Jiaxin et al.* · `foundation-models`
- 🔥 **[OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics](https://arxiv.org/abs/2606.04463)** `2026-06-03` · *Wu, Zhuoyuan et al.* · [🌐](https://qizekun.github.io/humanoid-gpt/) · `foundation-models`
- 🔥 **[MAD: Mapping-Aware World Models for Agile Quadrotor Flight](https://arxiv.org/abs/2606.04534)** `2026-06-03` · *Zhang, Xinhong et al.* · `foundation-models`
- 🔥 **[VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training](https://arxiv.org/abs/2606.04708)** `2026-06-03` · *Yang, Siyuan et al.* · `teleoperation`
- 🔥 **[CoRe-MoE: Contrastive Reweighted Mixture of Experts for Multi-Terrain Humanoid Locomotion with Gait Adaptation](https://arxiv.org/abs/2606.04718)** `2026-06-03` · *Huang, Kailun et al.* · `locomotion`
- 🔥 **[HapTile: A Haptic-Informed Vision-Tactile-Language-Action Dataset for Contact-Rich Imitation Learning](https://arxiv.org/abs/2606.04825)** `2026-06-03` · *Alian, Amirhosein et al.* · `teleoperation`

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
