# Awesome Physical AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A **continuously maintained** list of resources on Physical AI, Embodied AI, and Humanoid Robotics — focused on **2025-2026+** state-of-the-art.

🤖 **Auto-updated** from arXiv + HuggingFace daily papers via a custom pipeline.
📅 Last updated: **2026-06-03** · 📊 **27** papers · 🏢 **19** companies · 🎮 **7** simulators

Maintained by [@junyuan-fang](https://github.com/junyuan-fang). PRs welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Contents

- [🤖 Foundation Models for Robotics](#foundation-models)
- [🦾 Manipulation](#manipulation)
- [🦿 Locomotion](#locomotion)
- [🕹️ Teleoperation](#teleoperation)
- [🌉 Sim-to-Real](#sim2real)
- [🌍 3D Scene Understanding](#scene)
- [🧭 Navigation & Mobility](#navigation)
- [🎯 RL & Imitation Learning](#rl-il)
- [📦 Datasets](#datasets)
- [🎮 Simulators](#simulators)
- [📊 Benchmarks](#benchmarks)
- [🛠️ Tools & Libraries](#tools)
- [🏢 Companies & Industry](#companies)
- [📚 Tutorials & Surveys](#tutorials)
---

## <a id="foundation-models"></a>🤖 Foundation Models for Robotics

*Generalist policies, VLA, world models*
- 🔥 **stable-worldmodel: A Reproducibility-First Infrastructure for World Models** (2026-05) — *Anonymous*
  - Clean baselines + planning solver + LeRobot-native datasets — the 'HuggingFace moment' for world models.
  - [arXiv](https://arxiv.org/abs/2605.21800) · `world-model · infrastructure · lerobot · benchmark`
- 🔥 **RAW-Dream: Reward-Aligned World Model Without Task Data** (2026-05) — *Anonymous*
  - Joint WAM: off-the-shelf VLM as reward; zero-shot task adaptation via imagined trajectories; dual-noise verification.
  - [arXiv](https://arxiv.org/abs/2605.12334) · `world-model · joint-wam · vlm-reward`
- 🔥 **World Action Model Survey: Cascaded vs Joint Taxonomy** (2026-05) — *Anonymous*
  - Unifies NVIDIA Cosmos / DreamZero / LeVERB / PhysiFlow / HEX in a Cascaded vs Joint framework — the WAM entry-point reference.
  - [arXiv](https://arxiv.org/abs/2605.12090) · `survey · world-model · wam-taxonomy`
- 👀 **HEX: Humanoid Embodied World Model** (2026-04) — *Anonymous*
  - Humanoid-centric world model in the WAM family — see WAM survey 2605.12090 for taxonomy placement.
  - [arXiv](https://arxiv.org/abs/2604.07993) · `world-model · humanoid`
- 📜 **Cosmos World Foundation Model Platform for Physical AI** (2025-01) — *NVIDIA*
  - NVIDIA's open world model platform for physical AI training data generation.
  - [arXiv](https://arxiv.org/abs/2501.03575) · [project](https://www.nvidia.com/en-us/ai/cosmos/) · [code](https://github.com/NVIDIA/Cosmos) · `world-model · nvidia · physical-ai`

## <a id="manipulation"></a>🦾 Manipulation

*Grasping, dexterous, bimanual manipulation*
- 🔥 **HandITL: Interactive Imitation Learning for High-DoF Dexterous Manipulation** (2026-05) — *Anonymous*
  - −99.8% jitter, −87.5% grasp failure; corrections boost downstream policy by +19% on long-horizon tasks.
  - [arXiv](https://arxiv.org/abs/2605.15157) · `dexterous · interactive-il · teleop`
- 🔥 **Dexterous Hand Research: A Comprehensive Survey (2026)** (2026-05) — *Anonymous*
  - Most comprehensive dexterous-hand survey to date — methods, datasets, evaluation; positions tactile as the next-stage key modality.
  - [arXiv](https://arxiv.org/abs/2605.13925) · `survey · dexterous · tactile`
- 📜 **ALOHA Unleashed: A Simple Recipe for Robot Dexterity** (2024-10) — *Zhao et al.*
  - Diffusion policy + large-scale teleop data for dexterous bimanual manipulation — community baseline.
  - [arXiv](https://arxiv.org/abs/2410.13126) · [project](https://aloha-unleashed.github.io) · `bimanual · diffusion · dexterous`

## <a id="locomotion"></a>🦿 Locomotion

*Humanoid, quadruped, bipedal walking and running*
- 🔥 **SPRINT: Spectral-Priors Reinforced Humanoid Sprinting** (2026-05) — *Anonymous*
  - Humanoid sprint at 6 m/s — public-data first-tier (vs Optimus Gen 3 1.2 m/s, Figure 03 ~2 m/s).
  - [arXiv](https://arxiv.org/abs/2605.28549) · `humanoid · sprint · frequency-domain`

## <a id="teleoperation"></a>🕹️ Teleoperation

*VR, wearable, and exoskeleton-based data collection*
- 📜 **OpenTeleVision: Open-source Immersive Teleoperation with Stereo Visual Feedback** (2024-07) — *Cheng et al.*
  - Open-source VR teleoperation system with binocular stereo feedback — community reference.
  - [arXiv](https://arxiv.org/abs/2407.01512) · [project](https://robot-tv.github.io) · [code](https://github.com/OpenTeleVision/TeleVision) · `vr · stereo · open-source`
- 📜 **Mobile ALOHA: Learning Bimanual Mobile Manipulation** (2024-01) — *Fu et al.*
  - $32k mobile teleop platform — community baseline for whole-body teleop.
  - [arXiv](https://arxiv.org/abs/2401.02117) · [project](https://mobile-aloha.github.io) · [code](https://github.com/MarkFzp/mobile-aloha) · `mobile · bimanual · low-cost`

## <a id="sim2real"></a>🌉 Sim-to-Real

*Domain randomization, sim-to-real transfer, deployment*
- 🔥 **Imagine2Real: Video-Generated HOI Priors for Zero-Shot Humanoid Sim2Real** (2026-05) — *Anonymous*
  - Use video generation as latent prior for human-object interaction; zero-shot mocap deployment, geometry-free.
  - [arXiv](https://arxiv.org/abs/2605.22272) · `hoi · video-prior · zero-shot`

## <a id="scene"></a>🌍 3D Scene Understanding

*NeRF, Gaussian Splatting, segmentation for robotics*
- 🔥 **PhysX-Omni: Simulation-Ready 3D Generation for Robotics** (2026-05) — *Anonymous*
  - Unified rigid/deformable/articulated sim-ready 3D gen via VLM-tailored geometry; releases PhysXVerse dataset + PhysX-Bench (6 dims).
  - [arXiv](https://arxiv.org/abs/2605.21572) · `sim-ready · 3d-generation · vlm`
- 📜 **3D Gaussian Splatting for Real-Time Radiance Field Rendering** (2023-08) — *Kerbl et al.*
  - Real-time, high-quality radiance field rendering — now ubiquitous in 3D scene understanding pipelines.
  - [arXiv](https://arxiv.org/abs/2308.04079) · [project](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) · [code](https://github.com/graphdeco-inria/gaussian-splatting) · `gaussian-splatting · novel-view-synthesis`

## <a id="navigation"></a>🧭 Navigation & Mobility

*Visual navigation, embodied QA, mobile robots*
*No entries yet — [contribute one!](CONTRIBUTING.md)*

## <a id="rl-il"></a>🎯 RL & Imitation Learning

*Diffusion policies, behavior cloning, RL for robotics*
- 📜 **Diffusion Policy: Visuomotor Policy Learning via Action Diffusion** (2023-03) — *Chi et al.*
  - Action-space diffusion — now the default visuomotor policy baseline.
  - [arXiv](https://arxiv.org/abs/2303.04137) · [project](https://diffusion-policy.cs.columbia.edu) · [code](https://github.com/real-stanford/diffusion_policy) · `diffusion · imitation · visuomotor`

## <a id="datasets"></a>📦 Datasets

*Robot trajectories, demonstrations, scene datasets*


### Manipulation Demonstrations

- **[Open X-Embodiment (RT-X)](https://robotics-transformer-x.github.io)** — Cross-embodiment robot dataset spanning 22 robot types, 1M+ trajectories. · *1M+ episodes* · [paper](https://arxiv.org/abs/2310.08864) · [code](https://github.com/google-deepmind/open_x_embodiment)
- **[DROID](https://droid-dataset.github.io)** — Diverse real-world manipulation dataset from 564 scenes, 13 institutions. · *76k demonstrations* · [paper](https://arxiv.org/abs/2403.12945)
- **[BridgeData V2](https://rail-berkeley.github.io/bridgedata)** — Large-scale tabletop manipulation dataset for generalization research. · *60k trajectories* · [paper](https://arxiv.org/abs/2308.12952)
- **[ARIO (All Robots In One)](https://imaei.github.io/project_pages/ario/)** — Unified cross-embodiment robot learning dataset. · [paper](https://arxiv.org/abs/2408.10899)
- **[AgiBot World](https://agibot-world.com)** — Large-scale humanoid manipulation dataset from AgiBot's real-world deployments.

### 3D Scenes

- **[Habitat-Matterport 3D (HM3D)](https://aihabitat.org/datasets/hm3d/)** — 1000+ photorealistic indoor 3D scenes for embodied AI training. · [paper](https://arxiv.org/abs/2109.08238)
- **[ScanNet++](https://kaldir.vc.in.tum.de/scannetpp/)** — 1006 high-fidelity indoor scenes with sub-mm geometry & DSLR captures. · [paper](https://arxiv.org/abs/2308.11417)
- **[Replica Dataset](https://github.com/facebookresearch/Replica-Dataset)** — 18 high-quality reconstructions of indoor spaces (Meta Reality Labs). · [paper](https://arxiv.org/abs/1906.05797)
- **[3D-FRONT / 3D-FUTURE](https://tianchi.aliyun.com/specials/promotion/alibaba-3d-scene-dataset)** — Synthetic indoor scenes with high-quality furniture CAD models (Alibaba). · [paper](https://arxiv.org/abs/2011.09127)

### Egocentric / Human Video

- **[Ego4D](https://ego4d-data.org)** — 3,670 hours of egocentric video across 74 worldwide locations. · *3,670 hours* · [paper](https://arxiv.org/abs/2110.07058)
- **[EPIC-KITCHENS-100](https://epic-kitchens.github.io/2024)** — Long-form egocentric kitchen activity dataset for action understanding. · *100 hours* · [paper](https://arxiv.org/abs/2006.13256)
- **[HOI4D](https://hoi4d.github.io)** — 4D egocentric dataset for category-level human-object interaction. · [paper](https://arxiv.org/abs/2203.01577)

### Motion Capture / Whole-Body

- **[AMASS](https://amass.is.tue.mpg.de)** — Unifies 15 mocap datasets in a common SMPL skeleton — 40+ hours of motion. · [paper](https://arxiv.org/abs/1904.03278)
- **[HumanML3D](https://github.com/EricGuo5513/HumanML3D)** — 14,616 motions with text annotations for motion-language tasks. · [paper](https://arxiv.org/abs/2202.04257) · [code](https://github.com/EricGuo5513/HumanML3D)

### Sim-Generated

- **[RoboCasa-Gen](https://robocasa.ai)** — Large-scale procedurally generated household tasks rendered in MuJoCo. · [paper](https://arxiv.org/abs/2406.02523)
- **[PhysXVerse](https://arxiv.org/abs/2605.21572)** — First general-purpose simulation-ready 3D dataset (released with PhysX-Omni, 2026). · [paper](https://arxiv.org/abs/2605.21572)

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

### Manipulation

- **[CALVIN](http://calvin.cs.uni-freiburg.de)** — Long-horizon, language-conditioned manipulation benchmark. · [paper](https://arxiv.org/abs/2112.03227) · [code](https://github.com/mees/calvin)
- **[Meta-World](https://meta-world.github.io)** — 50 manipulation tasks for multi-task and meta-RL evaluation. · [paper](https://arxiv.org/abs/1910.10897) · [code](https://github.com/Farama-Foundation/Metaworld)
- **[LIBERO](https://libero-project.github.io)** — Lifelong robot learning benchmark — 130 manipulation tasks across 4 suites. · [paper](https://arxiv.org/abs/2306.03310)
- **[RLBench](https://sites.google.com/view/rlbench)** — 100 vision-guided manipulation tasks with CoppeliaSim. · [paper](https://arxiv.org/abs/1909.12271) · [code](https://github.com/stepjam/RLBench)
- **[AliasBench](https://arxiv.org/abs/2605.14712)** — Benchmark probing multimodal-imitation ambiguity in VLA (used in IntentVLA 2026). · [paper](https://arxiv.org/abs/2605.14712)

### Navigation

- **[ProcTHOR](https://procthor.allenai.org)** — 10,000+ procedurally generated household scenes for embodied AI. · [paper](https://arxiv.org/abs/2206.06994)
- **[Habitat ObjectNav](https://aihabitat.org/challenge/2023/)** — Standard object-goal navigation in HM3D / MP3D. · [paper](https://arxiv.org/abs/2210.13063)
- **[OVMM](https://arxiv.org/abs/2310.13724)** — Open-vocabulary mobile manipulation benchmark (Habitat 3.0). · [paper](https://arxiv.org/abs/2310.13724)

### Locomotion / Whole-Body

- **[HumanoidBench](https://humanoid-bench.github.io)** — MuJoCo-based humanoid locomotion + whole-body manipulation benchmark. · [paper](https://arxiv.org/abs/2403.10506) · [code](https://github.com/carlosferrazza/humanoid-bench)

### VLA Generalization & OOD

- **[SimplerEnv](https://simpler-env.github.io)** — Reproducible real-to-sim eval suite — measures VLA gap between real and sim deployment. · [paper](https://arxiv.org/abs/2405.05941) · [code](https://github.com/simpler-env/SimplerEnv)
- **[PhysX-Bench](https://arxiv.org/abs/2605.21572)** — 6-dim evaluation (geometry/scale/material/affordance/kinematics/function) — released with PhysX-Omni, 2026. · [paper](https://arxiv.org/abs/2605.21572)

### Multi-Skill / Long-Horizon

- **[BEHAVIOR-1K](https://behavior.stanford.edu/behavior-1k)** — 1,000 long-horizon household activities in OmniGibson — the largest activity benchmark. · [paper](https://arxiv.org/abs/2403.09227)
- **[RoboCasa-Bench](https://robocasa.ai)** — 100+ atomic + composite household tasks running on RoboCasa-Gen scenes. · [paper](https://arxiv.org/abs/2406.02523)

## <a id="tools"></a>🛠️ Tools & Libraries

*Open-source frameworks for building embodied AI*
- **[LeRobot](https://huggingface.co/lerobot)** — Hugging Face's end-to-end robotics framework — datasets, models, hardware. · [code](https://github.com/huggingface/lerobot)
- **[Diffusion Policy](https://github.com/real-stanford/diffusion_policy)** — Reference implementation of action-space diffusion policies. · [paper](https://arxiv.org/abs/2303.04137) · [code](https://github.com/real-stanford/diffusion_policy)
- **[OpenVLA](https://openvla.github.io)** — Open-source 7B Vision-Language-Action foundation model. · [code](https://github.com/openvla/openvla)
- **[AnyGrasp SDK](https://graspnet.net/anygrasp.html)** — General object grasping in cluttered scenes. · [paper](https://arxiv.org/abs/2212.08333) · [code](https://github.com/graspnet/anygrasp_sdk)
- **[Curobo](https://curobo.org)** — NVIDIA's GPU-accelerated motion planning library. · [code](https://github.com/NVlabs/curobo)
- **[nvdiffrast](https://nvlabs.github.io/nvdiffrast/)** — Modular differentiable rendering primitives from NVIDIA. · [code](https://github.com/NVlabs/nvdiffrast)

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

### 🇺🇸 United States

- **[Physical Intelligence](https://www.physicalintelligence.company)** · vla / manipulation / foundation-model · *π0, π0.5* · Sergey Levine + Chelsea Finn led, formerly Google Robotics.
- **[Skild AI](https://www.skild.ai)** · foundation-model / generalist · CMU spinout, generalist robot foundation model.
- **[Figure](https://www.figure.ai)** · humanoid / manipulation · *Figure 02, Helix*
- **[Tesla Optimus](https://www.tesla.com/we-robot)** · humanoid · *Optimus Gen 2, Optimus Gen 3* · In-house Tesla program, not standalone company.
- **[Apptronik](https://apptronik.com)** · humanoid · *Apollo*
- **[Agility Robotics](https://agilityrobotics.com)** · humanoid / logistics · *Digit*
- **[Boston Dynamics](https://www.bostondynamics.com)** · humanoid / quadruped · *Atlas (electric), Spot, Stretch*

### 🇨🇳 China

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

### 🇪🇺 Europe

- **[1X Technologies](https://www.1x.tech)** · humanoid / world-model · *NEO, EVE*

### 🇨🇦 Canada

- **[Sanctuary AI](https://sanctuary.ai)** · humanoid · *Phoenix Gen 7*

## <a id="tutorials"></a>📚 Tutorials & Surveys

*Surveys, books, and tutorial materials*
*No entries yet — [contribute one!](CONTRIBUTING.md)*


---

## 🆕 Recent additions (last 45 days)

- 🔥 **AHEAD: Adaptive Hierarchical Embodied Action Decoding for Dynamic VLA Deployment** (2026-06) · *Anonymous (under review)* · [arXiv](https://arxiv.org/abs/2606.02486) · `vla`
- 🔥 **Hide-and-Seek: Step-Level Failure Detection for VLA under Conformal Prediction** (2026-05) · *Anonymous* · [arXiv](https://arxiv.org/abs/2605.30834) · `vla`
- 🔥 **Qwen-VLA: Alibaba's Embodied Foundation Model** (2026-05) · *Alibaba* · [arXiv](https://arxiv.org/abs/2605.30280) · `vla`
- 🔥 **SPRINT: Spectral-Priors Reinforced Humanoid Sprinting** (2026-05) · *Anonymous* · [arXiv](https://arxiv.org/abs/2605.28549) · `locomotion`
- 👀 **Continual VLA: Catastrophic Forgetting in Heterogeneous Real-World Demonstrations** (2026-05) · *Anonymous* · [arXiv](https://arxiv.org/abs/2605.26820) · `vla`
- 👀 **GesVLA: Pointing Gesture Grounding for Vision-Language-Action Models** (2026-05) · *Xuan et al.* · [arXiv](https://arxiv.org/abs/2605.22812) · [project](https://gwxuan.github.io/GesVLA/) · `vla`
- 🔥 **Imagine2Real: Video-Generated HOI Priors for Zero-Shot Humanoid Sim2Real** (2026-05) · *Anonymous* · [arXiv](https://arxiv.org/abs/2605.22272) · `sim2real`
- 🔥 **AVP: Action-Visual Primitives for Decoupled VLA Architecture** (2026-05) · *Anonymous* · [arXiv](https://arxiv.org/abs/2605.22183) · `vla`
- 🔥 **stable-worldmodel: A Reproducibility-First Infrastructure for World Models** (2026-05) · *Anonymous* · [arXiv](https://arxiv.org/abs/2605.21800) · `foundation-models`
- 🔥 **PhysX-Omni: Simulation-Ready 3D Generation for Robotics** (2026-05) · *Anonymous* · [arXiv](https://arxiv.org/abs/2605.21572) · `scene`
- 🔥 **Hierarchical 'Brain-Cerebellum' Architecture for Robot Manipulation** (2026-05) · *Anonymous* · [arXiv](https://arxiv.org/abs/2605.21133) · `vla`
- 🔥 **HandITL: Interactive Imitation Learning for High-DoF Dexterous Manipulation** (2026-05) · *Anonymous* · [arXiv](https://arxiv.org/abs/2605.15157) · `manipulation`
- 🔥 **IntentVLA: History-Conditioned Action Prediction for VLA** (2026-05) · *Anonymous* · [arXiv](https://arxiv.org/abs/2605.14712) · `vla`
- 🔥 **Dexterous Hand Research: A Comprehensive Survey (2026)** (2026-05) · *Anonymous* · [arXiv](https://arxiv.org/abs/2605.13925) · `manipulation`
- 🔥 **RAW-Dream: Reward-Aligned World Model Without Task Data** (2026-05) · *Anonymous* · [arXiv](https://arxiv.org/abs/2605.12334) · `foundation-models`

> 🤖 *Auto-rolled forward from `data/papers.yaml` every push. Older entries naturally drop out of this window but remain in their category section.*

---

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=junyuan-fang/awesome-physical-ai&type=Date)](https://star-history.com/#junyuan-fang/awesome-physical-ai&Date)

## 🤝 Contributing

This list is auto-fed from a [daily paper aggregation pipeline](https://github.com/junyuan-fang/personal_planning), but PRs are very welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## 📜 License

[MIT](LICENSE) © 2026 [@junyuan-fang](https://github.com/junyuan-fang)
