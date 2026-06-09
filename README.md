# Awesome Physical AI

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Maintained](https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg)](https://github.com/junyuan-fang/awesome-physical-ai/commits/master)
![Last updated](https://img.shields.io/badge/Last%20updated-2026--06--09-blue.svg)
![Papers](https://img.shields.io/badge/Papers-66-success.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> A **continuously maintained** list of resources on Physical AI, Embodied AI, and Humanoid Robotics — focused on **2025-2026+** state-of-the-art.
> 一个**持续自动更新**的具身智能 / 物理 AI / 人形机器人资源列表（论文描述中英双语，面向中文社区）。

🤖 **Auto-updated** from arXiv + HuggingFace daily papers via a custom pipeline · 每日自动同步.
📊 **66** papers · 🏢 **19** companies · 🎮 **8** simulators · 📦 **16** datasets · 📊 **13** benchmarks

> 💡 **Legend / 图例**: 🔥 must-read · 👀 worth-knowing · 📜 classic landmark · 🏛️ accepted venue · 🌐 project · 💻 code. Click any **▸ section** to expand / 点击展开折叠区.

---

## 🌐 What is Physical AI?

**Physical AI** is AI that perceives, reasons about, and acts in the *physical* world through a body — robots, humanoids, manipulators. Unlike chatbots that output text, these systems output **actions** and must obey physics, contact, and real-time constraints.

> **物理 AI / 具身智能**：让 AI 通过「身体」（机器人 / 人形 / 机械臂）感知、推理并作用于真实物理世界。区别于只输出文本的对话模型，它输出的是**动作**，必须遵守物理、接触和实时性约束。

This list covers the full stack: **foundation models** (VLA, world models) → **policies** (manipulation, locomotion, navigation) → **data** (teleoperation, datasets) → **infrastructure** (simulators, benchmarks, sim-to-real) → **industry** (humanoid companies). It does **not** cover pure LLMs, classical control without learning, or non-embodied CV/NLP.

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

- **📚 Research** — [🤖 Foundation Models for Robotics](#foundation-models) · [🦾 Manipulation](#manipulation) · [🦿 Locomotion](#locomotion) · [🕹️ Teleoperation](#teleoperation) · [🌉 Sim-to-Real](#sim2real) · [🌍 3D Scene Understanding](#scene) · [🧭 Navigation & Mobility](#navigation) · [🎯 RL & Imitation Learning](#rl-il)
- **🧰 Resources** — [📦 Datasets](#datasets) · [🎮 Simulators](#simulators) · [📊 Benchmarks](#benchmarks) · [🛠️ Tools & Libraries](#tools) · [📚 Tutorials & Surveys](#tutorials)
- **🏢 Industry** — [🏢 Companies & Industry](#companies)

---

## <a id="foundation-models"></a>🤖 Foundation Models for Robotics

*Generalist policies, VLA, world models*
<details open>
<summary>🆕 <b>2026</b> · 12 papers</summary>

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
<summary>🆕 <b>2026</b> · 5 papers</summary>

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
<summary>📜 <b>Earlier landmarks</b> · 1 paper</summary>

- 📜 **[ALOHA Unleashed: A Simple Recipe for Robot Dexterity](https://arxiv.org/abs/2410.13126)** — *Zhao et al.* · `2024-10-17`
  > Diffusion policy + large-scale teleop data for dexterous bimanual manipulation — community baseline. · [🌐 project](https://aloha-unleashed.github.io)
</details>

<sub>[⬆ back to top](#contents)</sub>

## <a id="locomotion"></a>🦿 Locomotion

*Humanoid, quadruped, bipedal walking and running*
<details open>
<summary>🆕 <b>2026</b> · 6 papers</summary>

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
<summary>🆕 <b>2026</b> · 8 papers</summary>

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
<summary>🆕 <b>2026</b> · 2 papers</summary>

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
<summary>🆕 <b>2026</b> · 2 papers</summary>

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
*No entries yet — [contribute one!](CONTRIBUTING.md)*

<sub>[⬆ back to top](#contents)</sub>

## <a id="rl-il"></a>🎯 RL & Imitation Learning

*Diffusion policies, behavior cloning, RL for robotics*
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
- **[Isaac Lab](https://isaac-sim.github.io/IsaacLab)** — NVIDIA's modular RL training framework built on Isaac Sim. `rl` `gpu-accelerated` `nvidia`  · [💻 code](https://github.com/isaac-sim/IsaacLab)
- **[Isaac Sim](https://developer.nvidia.com/isaac/sim)** — NVIDIA's full robot simulator with photorealistic rendering. `photorealistic` `gpu` `nvidia` 
- **[Genesis](https://genesis-embodied-ai.github.io)** — Universal physics engine for robotics — built in pure Python, 43M FPS claim. `physics` `python` `multi-material` · [📄 paper](https://arxiv.org/abs/2412.04268) · [💻 code](https://github.com/Genesis-Embodied-AI/Genesis)
- **[MuJoCo MJX](https://mujoco.readthedocs.io/en/latest/mjx.html)** — GPU/TPU-accelerated JAX-based version of MuJoCo for massive parallel rollouts. `jax` `gpu` `parallel`  · [💻 code](https://github.com/google-deepmind/mujoco)
- **[Habitat 3.0](https://aihabitat.org)** — Photorealistic embodied AI sim with humans, navigation + manipulation. `navigation` `humans` `photorealistic` · [📄 paper](https://arxiv.org/abs/2310.13724) · [💻 code](https://github.com/facebookresearch/habitat-sim)
- **[RoboCasa](https://robocasa.ai)** — Large-scale household simulation framework on top of MuJoCo. `household` `mujoco` `large-scale` · [📄 paper](https://arxiv.org/abs/2406.02523) · [💻 code](https://github.com/robocasa/robocasa)
- **[ManiSkill 3](https://maniskill.ai)** — GPU-parallelized manipulation skill learning sim. `manipulation` `gpu`  · [💻 code](https://github.com/haosulab/ManiSkill)
- **[MotrixSim (Motphys / 谋先飞)](https://www.motphys.com/en/products)** — Homegrown Chinese real-time physics engine for multibody dynamics & robotics — generalized coordinates + implicit solver, GPU multi-world parallel training. Powers the MIIT/CAS-backed AGIROS embodied-AI ecosystem. `physics` `gpu` `multibody` `china`  · [💻 code](https://github.com/Motphys/motrixsim-docs)

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
- **[LeRobot](https://huggingface.co/lerobot)** — Hugging Face's end-to-end robotics framework — datasets, models, hardware. · ✅ open-source · [💻 code](https://github.com/huggingface/lerobot)
- **[Diffusion Policy](https://github.com/real-stanford/diffusion_policy)** — Reference implementation of action-space diffusion policies. · ✅ open-source · [💻 code](https://github.com/real-stanford/diffusion_policy) · [📄 paper](https://arxiv.org/abs/2303.04137)
- **[OpenVLA](https://openvla.github.io)** — Open-source 7B Vision-Language-Action foundation model. · ✅ open-source · [💻 code](https://github.com/openvla/openvla)
- **[AnyGrasp SDK](https://graspnet.net/anygrasp.html)** — General object grasping in cluttered scenes. · ✅ open-source · [💻 code](https://github.com/graspnet/anygrasp_sdk) · [📄 paper](https://arxiv.org/abs/2212.08333)
- **[Curobo](https://curobo.org)** — NVIDIA's GPU-accelerated motion planning library. · ✅ open-source · [💻 code](https://github.com/NVlabs/curobo)
- **[nvdiffrast](https://nvlabs.github.io/nvdiffrast/)** — Modular differentiable rendering primitives from NVIDIA. · ✅ open-source · [💻 code](https://github.com/NVlabs/nvdiffrast)

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

- 🔥 **[Discrete-WAM: Unified Discrete Vision-Action Token Editing for World-Policy Learning](https://arxiv.org/abs/2606.05645)** `2026-06-04` · *Yao, Ziyang et al.* · `foundation-models`
- 🔥 **[PiL-World: A Chunk-Wise World Model for VLA Policy-in-the-Loop Evaluation](https://arxiv.org/abs/2606.05773)** `2026-06-04` · *Ma, Chong et al.* · `teleoperation`
- 🔥 **[LadderMan: Learning Humanoid Perceptive Ladder Climbing](https://arxiv.org/abs/2606.05873)** `2026-06-04` · *Zhao, Siheng et al.* · `teleoperation`
- 🔥 **[TAGA: Terrain-aware Active Gaze Learning for Generalizable Agile Humanoid Locomotion](https://arxiv.org/abs/2606.05880)** `2026-06-04` · *Li, Peizhuo et al.* · `locomotion`
- 🔥 **[World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis](https://arxiv.org/abs/2606.05979)** `2026-06-04` · *Yang, Yi et al.* · `foundation-models`
- 🔥 **[MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.06139)** `2026-06-04` · *Taouil, Ilyass et al.* · `teleoperation`
- 🔥 **[AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding](https://arxiv.org/abs/2606.06155)** `2026-06-04` · *Yu, Qize et al.* · `vla`
- 🔥 **[TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies](https://arxiv.org/abs/2606.06491)** `2026-06-04` · *Jing, Dong et al.* · `vla`
- 🔥 **[HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers](https://arxiv.org/abs/2606.06493)** `2026-06-04` · *Yang, Lizhi et al.* · `locomotion`
- 🔥 **[DexFuture: Hierarchical Future-State Visuomotor Targeting for Bimanual Dexterous Tool Use](https://arxiv.org/abs/2606.05699)** `2026-06-04` · *Li, Runfa Blark et al.* · `foundation-models`
- 🔥 **[TAM: Torque Adaptation Module for Robust Motion Transfer in Manipulation](https://arxiv.org/abs/2606.06218)** `2026-06-04` · *Son, Dongwon et al.* · `sim2real`
- 🔥 **[HomeWorld: A Unified Floorplan-to-Furnished Framework for Generating Controllable, Densely Interactive Whole-Home Scenes](https://arxiv.org/abs/2606.06390)** `2026-06-04` · *Li, Wenbo et al.* · `vla`
- 🔥 **[3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training](https://arxiv.org/abs/2606.04436)** `2026-06-03` · *Shi, Jiaxin et al.* · `foundation-models`
- 🔥 **[OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics](https://arxiv.org/abs/2606.04463)** `2026-06-03` · *Wu, Zhuoyuan et al.* · [🌐](https://wuzy2115.github.io/oscar-project-page/) · `foundation-models`
- 🔥 **[MAD: Mapping-Aware World Models for Agile Quadrotor Flight](https://arxiv.org/abs/2606.04534)** `2026-06-03` · *Zhang, Xinhong et al.* · `foundation-models`

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
