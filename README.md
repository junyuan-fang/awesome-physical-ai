# Awesome Physical AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A **continuously maintained** list of resources on Physical AI, Embodied AI, and Humanoid Robotics — focused on **2025-2026+** state-of-the-art.

🤖 **Auto-updated** from arXiv + HuggingFace daily papers via a custom pipeline.
📅 Last updated: **2026-06-03** · 📊 **12** papers · 🏢 **19** companies · 🎮 **7** simulators

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
- 🔥 **Cosmos World Foundation Model Platform for Physical AI** (2025-01) — *NVIDIA*
  - NVIDIA's open world model platform for physical AI training data generation.
  - [arXiv](https://arxiv.org/abs/2501.03575) · [project](https://www.nvidia.com/en-us/ai/cosmos/) · [code](https://github.com/NVIDIA/Cosmos) · `world-model · nvidia · physical-ai`
- 🔥 **Genie: Generative Interactive Environments** (2024-02) — *DeepMind*
  - Foundation world model trained on internet videos, generates controllable 2D environments.
  - [arXiv](https://arxiv.org/abs/2402.15391) · [project](https://sites.google.com/view/genie-2024/home) · `world-model · interactive · deepmind`

## <a id="manipulation"></a>🦾 Manipulation

*Grasping, dexterous, bimanual manipulation*
- 🔥 **ALOHA Unleashed: A Simple Recipe for Robot Dexterity** (2024-10) — *Zhao et al.*
  - Diffusion policy + large-scale teleop data for dexterous bimanual manipulation.
  - [arXiv](https://arxiv.org/abs/2410.13126) · [project](https://aloha-unleashed.github.io) · `bimanual · diffusion · dexterous`
- 🔥 **HumanPlus: Humanoid Shadowing and Imitation from Humans** (2024-06) — *Fu et al.*
  - End-to-end shadowing of human motion for full-body humanoid skills.
  - [arXiv](https://arxiv.org/abs/2406.10454) · [project](https://humanoid-ai.github.io) · [code](https://github.com/MarkFzp/humanplus) · `humanoid · imitation · teleop`

## <a id="locomotion"></a>🦿 Locomotion

*Humanoid, quadruped, bipedal walking and running*
*No entries yet — [contribute one!](CONTRIBUTING.md)*

## <a id="teleoperation"></a>🕹️ Teleoperation

*VR, wearable, and exoskeleton-based data collection*
- 🔥 **OpenTeleVision: Open-source Immersive Teleoperation with Stereo Visual Feedback** (2024-07) — *Cheng et al.*
  - Open-source VR teleoperation system with binocular stereo feedback.
  - [arXiv](https://arxiv.org/abs/2407.01512) · [project](https://robot-tv.github.io) · [code](https://github.com/OpenTeleVision/TeleVision) · `vr · stereo · open-source`
- 🔥 **Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation** (2024-01) — *Fu et al.*
  - $32k mobile teleop platform that learns dexterous bimanual mobile tasks.
  - [arXiv](https://arxiv.org/abs/2401.02117) · [project](https://mobile-aloha.github.io) · [code](https://github.com/MarkFzp/mobile-aloha) · `mobile · bimanual · low-cost`

## <a id="sim2real"></a>🌉 Sim-to-Real

*Domain randomization, sim-to-real transfer, deployment*
- 👀 **Eureka: Human-Level Reward Design via Coding Large Language Models** (2023-10) — *Ma et al.*
  - LLM-generated reward functions trained in Isaac Gym, deployed to real robots.
  - [arXiv](https://arxiv.org/abs/2310.12931) · [project](https://eureka-research.github.io) · [code](https://github.com/eureka-research/Eureka) · `reward-design · llm · isaac`

## <a id="scene"></a>🌍 3D Scene Understanding

*NeRF, Gaussian Splatting, segmentation for robotics*
- 🔥 **3D Gaussian Splatting for Real-Time Radiance Field Rendering** (2023-08) — *Kerbl et al.*
  - Real-time, high-quality radiance field rendering via differentiable Gaussian splatting.
  - [arXiv](https://arxiv.org/abs/2308.04079) · [project](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) · [code](https://github.com/graphdeco-inria/gaussian-splatting) · `gaussian-splatting · novel-view-synthesis`

## <a id="navigation"></a>🧭 Navigation & Mobility

*Visual navigation, embodied QA, mobile robots*
*No entries yet — [contribute one!](CONTRIBUTING.md)*

## <a id="rl-il"></a>🎯 RL & Imitation Learning

*Diffusion policies, behavior cloning, RL for robotics*
- 🔥 **Diffusion Policy: Visuomotor Policy Learning via Action Diffusion** (2023-03) — *Chi et al.*
  - Action-space diffusion for robust visuomotor policies — now a default baseline.
  - [arXiv](https://arxiv.org/abs/2303.04137) · [project](https://diffusion-policy.cs.columbia.edu) · [code](https://github.com/real-stanford/diffusion_policy) · `diffusion · imitation · visuomotor`

## <a id="datasets"></a>📦 Datasets

*Robot trajectories, demonstrations, scene datasets*
- **[Open X-Embodiment (RT-X)](https://robotics-transformer-x.github.io)** — Cross-embodiment robot dataset spanning 22 robot types, 1M+ trajectories. · *1M+ episodes* · [paper](https://arxiv.org/abs/2310.08864) · [code](https://github.com/google-deepmind/open_x_embodiment)
- **[LIBERO](https://libero-project.github.io)** — Lifelong robot learning benchmark — 130 manipulation tasks. · [paper](https://arxiv.org/abs/2306.03310) · [code](https://github.com/Lifelong-Robot-Learning/LIBERO)
- **[DROID](https://droid-dataset.github.io)** — Diverse, real-world manipulation dataset from 564 scenes, 13 institutions. · *76k demonstrations* · [paper](https://arxiv.org/abs/2403.12945)
- **[BridgeData V2](https://rail-berkeley.github.io/bridgedata)** — Large-scale tabletop manipulation dataset for generalization research. · *60k trajectories* · [paper](https://arxiv.org/abs/2308.12952)
- **[Habitat-Matterport 3D (HM3D)](https://aihabitat.org/datasets/hm3d/)** — 1000+ photorealistic indoor 3D scenes for embodied AI training. · [paper](https://arxiv.org/abs/2109.08238)
- **[ARIO (All Robots In One)](https://imaei.github.io/project_pages/ario/)** — Unified cross-embodiment robot learning dataset. · [paper](https://arxiv.org/abs/2408.10899)

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
- **[CALVIN](http://calvin.cs.uni-freiburg.de)** — Long-horizon, language-conditioned manipulation benchmark. · [paper](https://arxiv.org/abs/2112.03227) · [code](https://github.com/mees/calvin)
- **[Meta-World](https://meta-world.github.io)** — 50 manipulation tasks for multi-task and meta-RL. · [paper](https://arxiv.org/abs/1910.10897) · [code](https://github.com/Farama-Foundation/Metaworld)
- **[LIBERO](https://libero-project.github.io)** — Lifelong robot learning benchmark — 130 manipulation tasks across 4 task suites. · [paper](https://arxiv.org/abs/2306.03310)
- **[RLBench](https://sites.google.com/view/rlbench)** — 100 vision-guided manipulation tasks with CoppeliaSim. · [paper](https://arxiv.org/abs/1909.12271) · [code](https://github.com/stepjam/RLBench)
- **[ProcTHOR](https://procthor.allenai.org)** — 10,000+ procedurally generated household scenes for embodied AI. · [paper](https://arxiv.org/abs/2206.06994)

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

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=junyuan-fang/awesome-physical-ai&type=Date)](https://star-history.com/#junyuan-fang/awesome-physical-ai&Date)

## 🤝 Contributing

This list is auto-fed from a [daily paper aggregation pipeline](https://github.com/junyuan-fang/personal_planning), but PRs are very welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## 📜 License

[MIT](LICENSE) © 2026 [@junyuan-fang](https://github.com/junyuan-fang)
