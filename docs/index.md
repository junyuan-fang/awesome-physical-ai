# 累积索引 / Ranked index

> 最近完成扫描：2026-10-23，源数据 `data/papers.yaml`。每个类别内：核心与相邻路线混排，按优先级 → 总分 → 日期排序；评分口径见 [METHODOLOGY](METHODOLOGY.md)。
> 历史 digest 是时间快照，**当前评分与开放状态以本索引为准**。

共 238 篇：🔥 38 · 👀 70 · 观察中 126 · 暂不评级 4

- [Other Generalist Models](#cat-foundation-general) · 8
- [Locomotion / Whole-Body](#cat-locomotion) · 20
- [Manipulation](#cat-manipulation) · 31
- [Navigation](#cat-navigation) · 11
- [RL & Imitation Learning](#cat-rl-il) · 6
- [3D Scene Understanding](#cat-scene) · 5
- [Sim-to-Real](#cat-sim2real) · 9
- [Teleoperation](#cat-teleoperation) · 10
- [Tutorials & Surveys](#cat-tutorials) · 6
- [Vision-Language-Action (VLA)](#cat-vla) · 69
- [World Models](#cat-world-model) · 63
- [数据集 / 基准使用关系](#resources)

## <a id="cat-foundation-general"></a>Other Generalist Models

| 论文 | 首次公开 | 路线 | 优先级 | 总分 (C/E/O/T) | 开源（last_check） | 作者/单位 | 报告 |
|---|---|---|---|---|---|---|---|
| [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601) | 2026-09-30 | 核心 | 🔥 重点阅读 | **80** (4/4/4/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | XPeng Inc.; Peking University; The University of Hong Kong | [📝](../digests/daily/2026-10-22.md) |
| [Grounded Action Model: 3D Grounding as a Foundation for Robotics](https://arxiv.org/abs/2609.23863) | 2026-09-20 | 核心 | 🔥 重点阅读 | **80** (4/4/4/4) | 💻 实质代码 · MIT (2026-10-22) | Northwestern University; University of Washington; National University of Singapore | [📝](../digests/daily/2026-10-22.md) |
| [RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance](https://arxiv.org/abs/2608.09853) | 2026-08-10 | 核心 | 🔥 重点阅读 | **80** (4/4/4/4) | 💻 实质代码 (2026-10-22) | DAMO Academy, Alibaba Group; Hupan Lab | [📝](../digests/migration-2026-10-22.md) |
| [EgoXperience: Learning World-Grounded Egocentric Representations from Human Experience](https://arxiv.org/abs/2610.26625) | 2026-10-19 | 核心 | 👀 值得关注 | **68** (4/4/2/4) | 📄 占位仓库 (2026-10-22) | Ropedia; Nanyang Technological University; Tsinghua University | [📝](../digests/daily/2026-10-22.md) |
| [PhysBrain 1.5: From Vision-Language Models to Physical Foundation Models](https://arxiv.org/abs/2609.14973) | 2026-09-14 | 核心 | 👀 值得关注 | **66** (4/3/3/3) | 🟡 部分开放 (2026-10-22) | DeepCybo | [📝](../digests/daily/2026-10-22.md) |
| [Orca: The World is in Your Mind](https://arxiv.org/abs/2606.30534) | 2026-06-29 | 核心 | 观察中 | **63** (3/3/3/4) | 🟡 部分开放 (2026-10-22) | Beijing Academy of Artificial Intelligence | [📝](../digests/migration-2026-10-22.md) |
| [HumanScale: Egocentric Human Video Can Outperform Real-Robot Data for Embodied Pretraining](https://arxiv.org/abs/2606.20521) | 2026-06-18 | 相邻 | 观察中 | **63** (4/3/2/4) | 📄 占位仓库 (2026-10-22) | PKU; NUS; MIT | [📝](../digests/migration-2026-10-22.md) |
| [Self-Evolving Embodied Agents via Skill-Harness Evolution](https://arxiv.org/abs/2608.11350) | 2026-08-11 | 核心 | 观察中 | **51** (3/3/1/4) | 未找到仓库 (2026-10-22) | Northeastern University; Microsoft Research | [📝](../digests/migration-2026-10-22.md) |

## <a id="cat-locomotion"></a>Locomotion / Whole-Body

| 论文 | 首次公开 | 路线 | 优先级 | 总分 (C/E/O/T) | 开源（last_check） | 作者/单位 | 报告 |
|---|---|---|---|---|---|---|---|
| [GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors](https://arxiv.org/abs/2606.05160) | 2026-06-03 | 相邻 | 🔥 重点阅读 | **83** (4/4/4/5) | 💻 实质代码 · custom (2026-10-22) | NVIDIA; UCLA | [📝](../digests/migration-2026-10-22.md) |
| [Reflex: Visually Grounded Reactive Humanoid Control](https://arxiv.org/abs/2610.12772) | 2026-10-08 | 核心 | 🔥 重点阅读 | **80** (4/4/4/4) | 💻 实质代码 · MIT (2026-10-22) | University of Washington; Stanford University; University of Southern California | [📝](../digests/daily/2026-10-22.md) |
| [HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers](https://arxiv.org/abs/2606.06493) | 2026-06-04 | 核心 | 👀 值得关注 | **74** (4/4/3/4) | 💻 实质代码 (2026-10-22) | California Institute of Technology; The Institute for Human & Machine Cognition | [📝](../digests/migration-2026-10-22.md) |
| [Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking](https://arxiv.org/abs/2606.03985) | 2026-06-02 | 核心 | 👀 值得关注 | **74** (4/4/3/4) | 🟡 部分开放 · Apache-2.0 (2026-10-22) | Tsinghua University; Galbot Inc.; Shanghai Jiao Tong University | [📝](../digests/migration-2026-10-22.md) |
| [LadderMan: Learning Humanoid Perceptive Ladder Climbing](https://arxiv.org/abs/2606.05873) | 2026-06-04 | 核心 | 👀 值得关注 | **71** (4/4/2/5) | 未找到仓库 (2026-10-22) | Amazon FAR; USC; UC Berkeley | [📝](../digests/migration-2026-10-22.md) |
| [Towards a General Humanoid Loco-Manipulation Model via Egocentric Whole-Body Human Data Pretraining](https://arxiv.org/abs/2610.00438) | 2026-09-30 | 核心 | 👀 值得关注 | **68** (4/4/2/4) | 未找到仓库 (2026-10-22) | Alibaba Group; Sichuan University; Shanghai Innovation Institute | [📝](../digests/daily/2026-10-22.md) |
| [GigaBrain-WBC-0.5: A Behavior World Model for Robust Whole-Body Control with Environment Interaction](https://arxiv.org/abs/2608.18234) | 2026-08-18 | 核心 | 👀 值得关注 | **65** (4/4/2/3) | 未找到仓库 (2026-10-22) | Cheng, Ziyang et al. | [📝](../digests/migration-2026-10-22.md) |
| [M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking](https://arxiv.org/abs/2606.04829) | 2026-06-03 | 核心 | 👀 值得关注 | **65** (3/4/3/3) | 💻 实质代码 (2026-10-22) | School of Automation, Southeast University; School of Vehicle and Mobility, Tsinghua University; Department of Robotics, Mohamed Bin Zayed University of Artificial Intelligence | [📝](../digests/migration-2026-10-22.md) |
| [TAGA: Terrain-aware Active Gaze Learning for Generalizable Agile Humanoid Locomotion](https://arxiv.org/abs/2606.05880) | 2026-06-04 | 核心 | 观察中 | **62** (3/4/2/4) | 未找到仓库 (2026-10-22) | MarmotLab, National University of Singapore; Center of X-Mechanics, Zhejiang University; South China University of Technology | [📝](../digests/migration-2026-10-22.md) |
| [StairMaster: Learning to Conquer Risky Hollow Stairs for Agile Quadrupedal Robots](https://arxiv.org/abs/2606.25765) | 2026-06-24 | 核心 | 观察中 | **59** (3/4/2/3) | 未找到仓库 (2026-10-22) | Shanghai Jiao Tong University | [📝](../digests/migration-2026-10-22.md) |
| [SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour](https://arxiv.org/abs/2606.19928) | 2026-06-18 | 核心 | 观察中 | **59** (4/4/1/3) | 未找到仓库 (2026-10-22) | Mirrorme Technology Co., Ltd. Shanghai, China.; Center for X-Mechanics, Zhejiang University, Hangzhou, China.; ZJU-Hangzhou Global Scientific and Technology Innovation Center, Hangzhou, China. | [📝](../digests/migration-2026-10-22.md) |
| [MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.06139) | 2026-06-04 | 核心 | 观察中 | **57** (4/3/1/4) | 未找到仓库 (2026-10-22) | Technical University of Munich, Germany; New York University, USA; Carnegie Mellon University, USA | [📝](../digests/migration-2026-10-22.md) |
| [Tac4Loco: Learning Spatiotemporal Plantar Pressure Representations for Humanoid Locomotion](https://arxiv.org/abs/2608.15766) | 2026-08-16 | 核心 | 观察中 | **54** (3/3/2/3) | 未找到仓库 (2026-10-22) | The Hong Kong University of Science and Technology (Guangzhou); The University of Hong Kong; Nanyang Technological University | [📝](../digests/migration-2026-10-22.md) |
| [CoRe-MoE: Contrastive Reweighted Mixture of Experts for Multi-Terrain Humanoid Locomotion with Gait Adaptation](https://arxiv.org/abs/2606.04718) | 2026-06-03 | 核心 | 观察中 | **54** (3/3/2/3) | 未找到仓库 (2026-10-22) | Hong Kong University of Science and Technology (Guangzhou); Guangdong University of Technology; South China Agricultural University | [📝](../digests/migration-2026-10-22.md) |
| [MILD: Tractable Terrain Modeling for Learning Improved Bipedal Locomotion on Deformable Surfaces](https://arxiv.org/abs/2608.19955) | 2026-08-20 | 核心 | 观察中 | **53** (3/4/1/3) | 未找到仓库 (2026-10-22) | Adaptive Robotic Controls Lab (ArcLab), Department of Mechanical Engineering, The University of Hong Kong; School of Mechanical and Electrical Engineering, Beijing Institute of Technology; Graduate School of Information Science and Technology, The University of Tokyo | [📝](../digests/migration-2026-10-22.md) |
| [SPRINT: Efficient Spectral Priors for Humanoid Athletic Sprints](https://arxiv.org/abs/2605.28549) | 2026-05-27 | 核心 | 观察中 | **53** (3/4/1/3) | 未找到仓库 (2026-10-22) | College of Intelligence Science and Technology, National University of Defense Technology, China; School of Artificial Intelligence and Robotics, Hunan University, China | [📝](../digests/migration-2026-10-22.md) |
| [Robust Brachiation on a Life-Sized Dual-Arm Robot Using Waypoint-Guided Reinforcement Learning](https://arxiv.org/abs/2608.17320) | 2026-08-18 | 核心 | 观察中 | **51** (3/3/1/4) | 未找到仓库 (2026-10-22) | Department of Mechano-Informatics, Graduate School of Information Science and Technology, The University of Tokyo | [📝](../digests/migration-2026-10-22.md) |
| [Imagine2Real: Towards Zero-shot Humanoid-Object Interaction via Video Generative Priors](https://arxiv.org/abs/2605.22272) | 2026-05-21 | 核心 | 观察中 | **51** (3/3/1/4) | 未找到仓库 (2026-10-22) | Zhejiang University; Shanghai AI Laboratory; The Chinese University of Hong Kong | [📝](../digests/migration-2026-10-22.md) |
| [DynaWM: Dynamics-Aware Distillation with World Model and Momentum Targets for Smooth Locomotion over Continuous Stairs](https://arxiv.org/abs/2606.24089) | 2026-06-23 | 核心 | 观察中 | **48** (3/3/1/3) | 未找到仓库 (2026-10-22) | School of Mechatronical Engineering, Beijing Institute of Technology | [📝](../digests/migration-2026-10-22.md) |
| [T-GMP: Terrain-conditioned Generative Motion Priors for Versatile and Natural Humanoid Locomotion](https://arxiv.org/abs/2606.06944) | 2026-06-05 | 核心 | 观察中 | **48** (3/3/1/3) | 未找到仓库 (2026-10-22) | Harbin Institute of Technology; Leju Robotics | [📝](../digests/migration-2026-10-22.md) |

## <a id="cat-manipulation"></a>Manipulation

| 论文 | 首次公开 | 路线 | 优先级 | 总分 (C/E/O/T) | 开源（last_check） | 作者/单位 | 报告 |
|---|---|---|---|---|---|---|---|
| [HumanoidToolBench: Benchmarking Humanoid Tool Use from Selection to Mobile Execution](https://arxiv.org/abs/2610.02089) | 2026-10-01 | 相邻 | 🔥 重点阅读 | **86** (4/4/5/4) | 💻 实质代码 · MIT (2026-10-22) | Seoul National University; University of Massachusetts Amherst; Google Research | [📝](../digests/daily/2026-10-22.md) |
| [RoboTok: A Scalable Data Engine for Internet Demonstration Video Retrieval and Dexterous Manipulation Learning](https://arxiv.org/abs/2609.03199) | 2026-09-02 | 相邻 | 🔥 重点阅读 | **80** (4/4/4/4) | 💻 实质代码 · MIT (2026-10-22) | Rice University; NVIDIA | [📝](../digests/daily/2026-10-22.md) |
| [SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deformable-Object Manipulation](https://arxiv.org/abs/2608.18701) | 2026-08-19 | 相邻 | 👀 值得关注 | **72** (4/3/4/3) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Tuojing Intelligence; Tsinghua University; King’s College London | [📝](../digests/migration-2026-10-22.md) |
| [DONIC: Generalist Dexterous Bimanual Tracking Control from Human Demonstrations](https://arxiv.org/abs/2610.29997) | 2026-10-21 | 核心 | 👀 值得关注 | **71** (4/4/3/3) | 💻 实质代码 (2026-10-23) | Ropedia | [📝](../digests/daily/2026-10-23.md) |
| [MotorMind: Scaffolding General Vision Language Models for Zero-Shot Robot Manipulation](https://arxiv.org/abs/2609.38078) | 2026-09-29 | 核心 | 👀 值得关注 | **71** (4/4/3/3) | 💻 实质代码 (2026-10-22) | University of Illinois Urbana-Champaign | [📝](../digests/daily/2026-10-22.md) |
| [TacPAC: Tactile Prediction and Real-Time Action Correction in World-Action Models for Contact-Rich Manipulation](https://arxiv.org/abs/2609.05266) | 2026-09-04 | 核心 | 👀 值得关注 | **71** (4/4/3/3) | 💻 实质代码 · MIT (2026-10-22) | School of Data Science, Fudan University; Shanghai Innovation Institute; NeoteAI | [📝](../digests/migration-2026-10-22.md) |
| [Robots Acquire Manipulation Skills in Seconds from a Single Human Video](https://arxiv.org/abs/2607.20033) | 2026-07-22 | 核心 | 👀 值得关注 | **71** (4/4/3/3) | 💻 实质代码 (2026-10-22) | Beijing Institute of Technology; X Square Robot; Tsinghua University | [📝](../digests/migration-2026-10-22.md) |
| [Learning from Fleet Experience: Collective Experience Learning Across 96 Robots](https://arxiv.org/abs/2610.25736) | 2026-10-19 | 核心 | 👀 值得关注 | **68** (4/4/2/4) | 🟡 部分开放 · Apache-2.0 (2026-10-22) | Tsinghua University; AgiBot; Infinigence AI | [📝](../digests/daily/2026-10-22.md) |
| [Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data](https://arxiv.org/abs/2608.02580) | 2026-08-03 | 相邻 | 👀 值得关注 | **68** (4/4/2/4) | 未找到仓库 (2026-10-22) | AIM3 Lab, Renmin University of China; Qwen Team, Alibaba Inc.; ShanghaiTech University | [📝](../digests/migration-2026-10-22.md) |
| [RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation](https://arxiv.org/abs/2610.27861) | 2026-10-20 | 相邻 | 👀 值得关注 | **66** (3/3/4/3) | 💻 实质代码 · MIT (2026-10-23) | Fudan University; Shenzhen Loop Area Institute; The Chinese University of Hong Kong | [📝](../digests/daily/2026-10-23.md) |
| [Pre-training Visual Dexterity in Simulation](https://arxiv.org/abs/2608.15917) | 2026-08-16 | 核心 | 👀 值得关注 | **66** (4/3/2/5) | 未找到仓库 (2026-10-22) | Stanford University; MIT; Scale AI | [📝](../digests/migration-2026-10-22.md) |
| [Real-World Cooperative Bimanual Dexterous Grasp of Large Objects from Single-View Observations](https://arxiv.org/abs/2608.10383) | 2026-08-11 | 核心 | 👀 值得关注 | **66** (3/3/4/3) | 💻 实质代码 · Apache-2.0 (2026-10-22) | School of Computer Science, The University of Auckland; College of Computer Science, Chongqing University; College of Electronic and Information Engineering, Southwest University | [📝](../digests/migration-2026-10-22.md) |
| [UniReflex: Plug-and-Play Force Control for Pretrained Generative Policies via Fast-Slow Reflex](https://arxiv.org/abs/2608.17432) | 2026-08-18 | 核心 | 👀 值得关注 | **65** (4/4/2/3) | 未找到仓库 (2026-10-22) | Tsinghua University Shenzhen International Graduate School; Nanyang Technological University; X Square Robot | [📝](../digests/migration-2026-10-22.md) |
| 📜 [ALOHA Unleashed: A Simple Recipe for Robot Dexterity](https://arxiv.org/abs/2410.13126) | 2024-10-17 | 核心 | 👀 值得关注 | **65** (4/4/1/5) | 未找到仓库 (2026-10-22) | Google DeepMind | [📝](../digests/migration-2026-10-22.md) |
| [RoboEdit: Turning Human Manipulation Videos into Scalable Robot Experience](https://arxiv.org/abs/2608.18948) | 2026-08-19 | 相邻 | 观察中 | **63** (4/3/2/4) | 未找到仓库 (2026-10-22) | University of California, Los Angeles; Massachusetts Institute of Technology; University of Utah | [📝](../digests/migration-2026-10-22.md) |
| [Affordance2Action: Task-Conditioned Scene-level Affordance Grounding for Real-Time Manipulation](https://arxiv.org/abs/2606.04172) | 2026-06-02 | 相邻 | 观察中 | **62** (3/4/2/4) | 未找到仓库 (2026-10-22) | Department of Computer Science, Rutgers University-New Brunswick; The Hong Kong University of Science and Technology (GZ); Shanghai AI Laboratory | [📝](../digests/migration-2026-10-22.md) |
| [GOAG: Generative and Object-Agnostic Grasp Planner for Dexterous Robotic Manipulation](https://arxiv.org/abs/2608.19759) | 2026-08-20 | 核心 | 观察中 | **60** (3/3/3/3) | 💻 实质代码 (2026-10-22) | Université Paris-Saclay, CEA, List, F-91120 Palaiseau, France; Ecole Centrale de Lyon, CNRS, LIRIS, UMR5205, Institut Universitaire de France (IUF), F-69130 Ecully, France | [📝](../digests/migration-2026-10-22.md) |
| [CoToGrasp: Contact-Topology-Conditioned Dexterous Grasp Synthesis via Canonical Workspace Learning](https://arxiv.org/abs/2608.19776) | 2026-08-20 | 核心 | 观察中 | **60** (3/3/3/3) | 💻 实质代码 (2026-10-22) | Université Paris-Saclay, CEA, List, F-91120 Palaiseau, France; Ecole Centrale Lyon, CNRS, LIRIS, UMR5205, Institut Universitaire de France (IUF), F-69130 Ecully, France | [📝](../digests/migration-2026-10-22.md) |
| [PRISM: Precision and contact-rich Real-world Industrial Skill dataset with Multimodal sensing](https://arxiv.org/abs/2608.17962) | 2026-08-18 | 相邻 | 观察中 | **60** (3/3/3/3) | 📄 占位仓库 (2026-10-22) | State Key Laboratory of General Artificial Intelligence, School of Intelligence Science and Technology, Peking University; Delta Intelligence; PKU-Wuhan Institute for Artificial Intelligence | [📝](../digests/migration-2026-10-22.md) |
| [PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration](https://arxiv.org/abs/2608.21031) | 2026-08-21 | 核心 | 观察中 | **57** (3/3/2/4) | 未找到仓库 (2026-10-22) | National Taiwan University; NVIDIA Research; National Yang Ming Chiao Tung University | [📝](../digests/migration-2026-10-22.md) |
| [DexFuture: Hierarchical Future-State Visuomotor Targeting for Bimanual Dexterous Tool Use](https://arxiv.org/abs/2606.05699) | 2026-06-04 | 核心 | 观察中 | **57** (3/3/2/4) | 未找到仓库 (2026-10-22) | UC San Diego | [📝](../digests/migration-2026-10-22.md) |
| [Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum](https://arxiv.org/abs/2605.21133) | 2026-05-20 | 核心 | 观察中 | **57** (3/3/2/4) | 未找到仓库 (2026-10-22) | School of Computer Science and Engineering, Sun Yat-sen University, China; Peng Cheng Laboratory, China; Key Laboratory of Machine Intelligence and Advanced Computing, Ministry of Education, China | [📝](../digests/migration-2026-10-22.md) |
| [H2R-Grounder: A Paired-Data-Free Paradigm for Translating Human Interaction Videos into Physically Grounded Robot Videos](https://arxiv.org/abs/2512.09406) | 2025-12-10 | 相邻 | 观察中 | **57** (3/3/2/4) | 📄 占位仓库 (2026-10-22) | Show Lab, National University of Singapore | [📝](../digests/migration-2026-10-22.md) |
| [Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents](https://arxiv.org/abs/2606.23085) | 2026-06-22 | 相邻 | 观察中 | **56** (3/4/1/4) | 未找到仓库 (2026-10-22) | University of Michigan; Princeton University; University of Virginia | [📝](../digests/migration-2026-10-22.md) |
| [LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories](https://arxiv.org/abs/2608.18618) | 2026-08-19 | 相邻 | 观察中 | **54** (3/3/2/3) | 未找到仓库 (2026-10-22) | University of Science and Technology of China; The Chinese University of Hong Kong; iFLYTEK | [📝](../digests/migration-2026-10-22.md) |
| [PartialBiGrasp: Inferring Hidden Local Geometry for Bimanual Grasping from Partial Views](https://arxiv.org/abs/2608.19188) | 2026-08-19 | 核心 | 观察中 | **54** (3/3/2/3) | 未找到仓库 (2026-10-22) | Robotics Research Center, IIIT Hyderabad | [📝](../digests/migration-2026-10-22.md) |
| [HiTac-WAM: A Hierarchical Tactile World Action Model for Contact-Rich Robot Manipulation](https://arxiv.org/abs/2608.19574) | 2026-08-20 | 核心 | 观察中 | **53** (3/4/1/3) | 未找到仓库 (2026-10-22) | Institute of Automation, Chinese Academy of Sciences; ImprintX Robotics; Beijing Academy of Artificial Intelligence | [📝](../digests/migration-2026-10-22.md) |
| [Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation](https://arxiv.org/abs/2605.21811) | 2026-05-20 | 核心 | 观察中 | **51** (3/3/1/4) | 未找到仓库 (2026-10-22) | Computer Science Department, Stanford University; Laboratory of Signals and Systems, University of Paris-Saclay, CNRS, CentraleSupélec; Toyota Research Institute | [📝](../digests/migration-2026-10-22.md) |
| [Throwing a Tight Spiral American Football by a Humanoid Robot](https://arxiv.org/abs/2608.16642) | 2026-08-17 | 核心 | 观察中 | **43** (3/2/1/3) | 未找到仓库 (2026-10-22) | Department of Computer Science, Iowa State University | [📝](../digests/migration-2026-10-22.md) |
| [EaDex: A Cross-Embodiment Dexterous Manipulation Framework from Low-Cost Demonstrations](https://arxiv.org/abs/2606.03268) | 2026-06-02 | 核心 | 观察中 | **37** (2/2/1/3) | 未找到仓库 (2026-10-22) | Faculty of Robot Science and Engineering, Northeastern University; Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences; School of Automation, Nanjing University of Information Science and Technology | [📝](../digests/migration-2026-10-22.md) |
| [Attention from Action, for Action: Emergent Visual Bottlenecks for Policy Learning](https://arxiv.org/abs/2608.13422) | 2026-08-13 | 核心 | 暂不评级 | — | 💻 实质代码 · MIT (2026-10-22) | KTH Royal Institute of Technology; University of Freiburg; Universität Hamburg | [📝](../digests/migration-2026-10-22.md) |

## <a id="cat-navigation"></a>Navigation

| 论文 | 首次公开 | 路线 | 优先级 | 总分 (C/E/O/T) | 开源（last_check） | 作者/单位 | 报告 |
|---|---|---|---|---|---|---|---|
| [ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation](https://arxiv.org/abs/2610.25690) | 2026-10-19 | 核心 | 🔥 重点阅读 | **86** (4/4/5/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Zhejiang University; Li Auto Inc.; Shenzhen University | [📝](../digests/daily/2026-10-22.md) |
| [Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation](https://arxiv.org/abs/2608.17512) | 2026-08-18 | 核心 | 🔥 重点阅读 | **80** (4/4/4/4) | 💻 实质代码 · MulanPSL-2.0 (2026-10-22) | School of Software Technology, Zhejiang University; Zhejiang Humanoid Robot Innovation Center Co., Ltd. | [📝](../digests/migration-2026-10-22.md) |
| [HumanCLAW: Can Vision-Language Models Act Through a Body?](https://arxiv.org/abs/2607.27180) | 2026-07-29 | 相邻 | 👀 值得关注 | **75** (4/3/4/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Meta; Nanyang Technological University; University of Washington | [📝](../digests/migration-2026-10-22.md) |
| [Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System](https://arxiv.org/abs/2606.18112) | 2026-06-16 | 核心 | 👀 值得关注 | **68** (4/4/2/4) | 📄 占位仓库 (2026-10-22) | Qwen Team | [📝](../digests/migration-2026-10-22.md) |
| [MAD: Mapping-Aware World Models for Agile Quadrotor Flight](https://arxiv.org/abs/2606.04534) | 2026-06-03 | 核心 | 观察中 | **56** (3/4/1/4) | 未找到仓库 (2026-10-22) | State Key Lab of Autonomous Intelligent Unmanned Systems, Beijing Institute of Technology; Zhongguancun Academy; School of Computer Science and Technology, Tongji University | [📝](../digests/migration-2026-10-22.md) |
| [HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments](https://arxiv.org/abs/2608.12860) | 2026-08-13 | 相邻 | 观察中 | **54** (3/3/2/3) | 未找到仓库 (2026-10-22) | VinMotion, Inc., Vietnam; University of Southern California, USA | [📝](../digests/migration-2026-10-22.md) |
| [NavVerse: Benchmarking Indoor-to-Outdoor Embodied Navigation in Continuous Robot Simulation](https://arxiv.org/abs/2607.19695) | 2026-07-22 | 相邻 | 观察中 | **54** (3/3/2/3) | 未找到仓库 (2026-10-22) | University of Michigan, Ann Arbor; Tsinghua University | [📝](../digests/migration-2026-10-22.md) |
| [NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation](https://arxiv.org/abs/2606.13494) | 2026-06-11 | 核心 | 观察中 | **54** (3/3/2/3) | 未找到仓库 (2026-10-22) | The University of Tokyo; National Institute of Informatics; AIRoA | [📝](../digests/migration-2026-10-22.md) |
| [Learning to Evolve: Multi-modal Interactive Fields for Robust Humanoid Navigation in Dynamic Environments](https://arxiv.org/abs/2605.21935) | 2026-05-21 | 核心 | 观察中 | **54** (3/3/2/3) | 未找到仓库 (2026-10-22) | State Key Laboratory of General Artificial Intelligence, Peking University, Shenzhen Graduate School; Oxford Robotics Institute, University of Oxford; Institute for Machine Learning, Department of Computer Science, ETH Zurich | [📝](../digests/migration-2026-10-22.md) |
| [Learning-Based Behavior Planning for Automated Driving: Real-World Integration and Deployment](https://arxiv.org/abs/2608.12198) | 2026-08-12 | 核心 | 观察中 | **52** (2/2/3/4) | 🟡 部分开放 · Apache-2.0 (2026-10-22) | Institute for Automotive Engineering (ika), RWTH Aachen University, Germany; Chair of Automotive Technology (FTM), Technical University of Munich | [📝](../digests/migration-2026-10-22.md) |
| [NavWM: A Unified Navigation World Model for Foresight-Driven Planning](https://arxiv.org/abs/2606.24101) | 2026-06-23 | 核心 | 观察中 | **48** (3/3/1/3) | 未找到仓库 (2026-10-22) | Institute of Automation, Chinese Academy of Sciences; School of Artificial Intelligence, University of Chinese Academy of Sciences; Beihang University | [📝](../digests/migration-2026-10-22.md) |

## <a id="cat-rl-il"></a>RL & Imitation Learning

| 论文 | 首次公开 | 路线 | 优先级 | 总分 (C/E/O/T) | 开源（last_check） | 作者/单位 | 报告 |
|---|---|---|---|---|---|---|---|
| 📜 [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137) | 2023-03-07 | 核心 | 🔥 重点阅读 | **100** (5/5/5/5) | 💻 实质代码 · MIT (2026-10-22) | Columbia University; Toyota Research Institute; MIT | [📝](../digests/migration-2026-10-22.md) |
| [Revisiting Open-Loop Execution in Robotics: Toward Reactive, Higher-Performing Policies](https://arxiv.org/abs/2608.15938) | 2026-08-16 | 相邻 | 👀 值得关注 | **77** (4/4/3/5) | 📄 占位仓库 · MIT (2026-10-22) | Massachusetts Institute of Technology; Mundane Systems Inc.; University of California, Berkeley | [📝](../digests/migration-2026-10-22.md) |
| [RoboStriker: Latent-Space Strategic Games for Autonomous Humanoid Boxing](https://arxiv.org/abs/2608.16195) | 2026-08-17 | 核心 | 观察中 | **63** (4/3/2/4) | 未找到仓库 (2026-10-22) | Shanghai Jiao Tong University; Shanghai Artificial Intelligence Laboratory; Huazhong University of Science and Technology | [📝](../digests/migration-2026-10-22.md) |
| [ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning](https://arxiv.org/abs/2606.17011) | 2026-06-15 | 核心 | 观察中 | **57** (3/3/2/4) | 未找到仓库 (2026-10-22) | XPENG Robotics; Fudan University; The Chinese University of Hong Kong | [📝](../digests/migration-2026-10-22.md) |
| [Dream2Reward: Transition-Alignment Reward Models from Positive Demonstrations for Robotic Manipulation](https://arxiv.org/abs/2608.18787) | 2026-08-19 | 核心 | 观察中 | **53** (3/4/1/3) | 未找到仓库 (2026-10-22) | School of Artificial Intelligence, University of Chinese Academy of Sciences; State Key Laboratory of Multimodal Artificial Intelligence Systems, Institute of Automation, Chinese Academy of Sciences; JD Explore Academy | [📝](../digests/migration-2026-10-22.md) |
| [Prism-GRPO: Faster VLA Policy Optimization via Splitting Same-outcome Groups](https://arxiv.org/abs/2608.17423) | 2026-08-18 | 核心 | 观察中 | **53** (3/4/1/3) | 未找到仓库 (2026-10-22) | Purdue University; AWS AI | [📝](../digests/migration-2026-10-22.md) |

## <a id="cat-scene"></a>3D Scene Understanding

| 论文 | 首次公开 | 路线 | 优先级 | 总分 (C/E/O/T) | 开源（last_check） | 作者/单位 | 报告 |
|---|---|---|---|---|---|---|---|
| 📜 [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2308.04079) | 2023-08-08 | 相邻 | 🔥 重点阅读 | **94** (5/5/4/5) | 💻 实质代码 · custom (2026-10-22) | Inria, Université Côte d’Azur, France; Max-Planck-Institut für Informatik, Germany | [📝](../digests/migration-2026-10-22.md) |
| [PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects](https://arxiv.org/abs/2605.21572) | 2026-05-20 | 相邻 | 👀 值得关注 | **78** (4/3/4/5) | 💻 实质代码 · custom (2026-10-22) | S-Lab, Nanyang Technological University; ACE Robotics | [📝](../digests/migration-2026-10-22.md) |
| [HomeWorld: A Unified Floorplan-to-Furnished Framework for Generating Controllable, Densely Interactive Whole-Home Scenes](https://arxiv.org/abs/2606.06390) | 2026-06-04 | 相邻 | 观察中 | **57** (3/3/2/4) | 📄 占位仓库 (2026-10-22) | Ace Robotics; CUHK MMLab; Shenzhen Loop Area Institute | [📝](../digests/migration-2026-10-22.md) |
| [ERQA-Plus: A Diagnostic Benchmark for Reasoning in Embodied AI](https://arxiv.org/abs/2606.17639) | 2026-06-16 | 相邻 | 观察中 | **54** (2/3/3/3) | 未找到仓库 (2026-10-22) | Centre for Frontier AI Research, Agency for Science, Technology and Research, Singapore; College of Computing and Data Science, Nanyang Technological University, Singapore | [📝](../digests/migration-2026-10-22.md) |
| [VISA: VLM-Guided Instance Semantic Auditing for 3D Occupancy World Models](https://arxiv.org/abs/2606.13460) | 2026-06-11 | 核心 | 观察中 | **45** (2/3/1/4) | 未找到仓库 (2026-10-22) | University of Maryland College Park, USA; Independent Researcher, USA; Stanford University, USA | [📝](../digests/migration-2026-10-22.md) |

## <a id="cat-sim2real"></a>Sim-to-Real

| 论文 | 首次公开 | 路线 | 优先级 | 总分 (C/E/O/T) | 开源（last_check） | 作者/单位 | 报告 |
|---|---|---|---|---|---|---|---|
| [Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking](https://arxiv.org/abs/2608.20087) | 2026-08-20 | 核心 | 👀 值得关注 | **74** (4/4/3/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Noitom Robotics; Shanghai AI Laboratory; Shanghai Jiao Tong University | [📝](../digests/migration-2026-10-22.md) |
| [ADEPT: Accelerating Dexterity via Pre-Training and Post-Training using Reinforcement Learning](https://arxiv.org/abs/2608.19182) | 2026-08-19 | 核心 | 👀 值得关注 | **71** (4/4/2/5) | 未找到仓库 (2026-10-22) | NVIDIA Corporation; Robotics Department, University of Michigan | [📝](../digests/migration-2026-10-22.md) |
| [TAM: Torque Adaptation Module for Robust Motion Transfer in Manipulation](https://arxiv.org/abs/2606.06218) | 2026-06-04 | 核心 | 👀 值得关注 | **71** (4/4/2/5) | 未找到仓库 (2026-10-22) | KAIST; Allen Institute for AI; University of Toronto | [📝](../digests/migration-2026-10-22.md) |
| [Mana: Dexterous Manipulation of Articulated Tools](https://arxiv.org/abs/2606.13677) | 2026-06-11 | 核心 | 👀 值得关注 | **66** (4/3/2/5) | 未找到仓库 (2026-10-22) | UC Berkeley; CMU; Stanford University | [📝](../digests/migration-2026-10-22.md) |
| [RoboGesture: Real-Time Semantic-aligned Co-Speech Gestures Generation for Humanoid Interaction](https://arxiv.org/abs/2608.28693) | 2026-08-27 | 核心 | 观察中 | **63** (3/3/3/4) | 🟡 部分开放 · MIT (2026-10-22) | Tsinghua University; Galbot Inc.; Beijing Institute of Technology | [📝](../digests/migration-2026-10-22.md) |
| [Tactile Sim2Real without Tactile Simulation via Bottlenecked Latent Reconstruction](https://arxiv.org/abs/2608.15897) | 2026-08-16 | 核心 | 观察中 | **62** (4/4/1/4) | 未找到仓库 (2026-10-22) | University of Michigan, Ann Arbor, MI, USA; Google DeepMind | [📝](../digests/migration-2026-10-22.md) |
| [Video2Sim2Real: Full-Stack Autonomous Dexterous Skill Acquisition from a Single Human Video](https://arxiv.org/abs/2606.08828) | 2026-06-07 | 核心 | 观察中 | **62** (3/4/2/4) | 未找到仓库 (2026-10-22) | Georgia Institute of Technology; University of Pennsylvania; Toyota Research Institute | [📝](../digests/migration-2026-10-22.md) |
| [SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors](https://arxiv.org/abs/2606.23444) | 2026-06-22 | 核心 | 观察中 | **59** (3/4/1/5) | 未找到仓库 (2026-10-22) | University of California Berkeley, Department of Electrical Engineering and Computer Sciences, Berkeley, CA 94720, USA; New York University, New York, NY, USA; Brown University, Providence, RI, USA | [📝](../digests/migration-2026-10-22.md) |
| [Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement](https://arxiv.org/abs/2606.18953) | 2026-06-17 | 核心 | 观察中 | **56** (3/4/1/4) | 未找到仓库 (2026-10-22) | KAIST, South Korea; Microsoft Research Asia - Tokyo, Japan; The University of Tokyo, Japan | [📝](../digests/migration-2026-10-22.md) |

## <a id="cat-teleoperation"></a>Teleoperation

| 论文 | 首次公开 | 路线 | 优先级 | 总分 (C/E/O/T) | 开源（last_check） | 作者/单位 | 报告 |
|---|---|---|---|---|---|---|---|
| 📜 [Mobile ALOHA: Learning Bimanual Mobile Manipulation](https://arxiv.org/abs/2401.02117) | 2024-01-04 | 相邻 | 🔥 重点阅读 | **83** (4/4/4/5) | 💻 实质代码 · MIT (2026-10-22) | Stanford University | [📝](../digests/migration-2026-10-22.md) |
| [RynnWorld-Teleop: An Action-Conditioned World Model for Digital Teleoperation](https://arxiv.org/abs/2607.06558) | 2026-07-07 | 相邻 | 🔥 重点阅读 | **80** (4/4/4/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Hong Kong Embodied AI Lab; CUHK; Alibaba Group | [📝](../digests/migration-2026-10-22.md) |
| [VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training](https://arxiv.org/abs/2606.04708) | 2026-06-03 | 相邻 | 🔥 重点阅读 | **80** (4/4/4/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Institute of AI (TeleAI), China Telecom; University of Science and Technology of China; Northwestern Polytechnical University | [📝](../digests/migration-2026-10-22.md) |
| 📜 [OpenTeleVision: Open-source Immersive Teleoperation with Stereo Visual Feedback](https://arxiv.org/abs/2407.01512) | 2024-07-01 | 相邻 | 👀 值得关注 | **75** (4/3/4/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | UC San Diego; MIT | [📝](../digests/migration-2026-10-22.md) |
| [ORCA: A Platform for Open-Source Dexterity Research](https://arxiv.org/abs/2606.14561) | 2026-06-12 | 相邻 | 👀 值得关注 | **67** (3/2/5/3) | 💻 实质代码 · MIT (2026-10-22) | University of Oxford; ETH Zurich; Orca Dexterity | [📝](../digests/migration-2026-10-22.md) |
| [MonoDuo: Using One Robot Arm to Learn Bimanual Policies](https://arxiv.org/abs/2605.29298) | 2026-05-28 | 核心 | 观察中 | **60** (3/3/2/5) | 未找到仓库 (2026-10-22) | University of California, Berkeley | [📝](../digests/migration-2026-10-22.md) |
| [HapTile: A Haptic-Informed Vision-Tactile-Language-Action Dataset for Contact-Rich Imitation Learning](https://arxiv.org/abs/2606.04825) | 2026-06-03 | 相邻 | 观察中 | **58** (3/2/3/4) | 📄 占位仓库 (2026-10-22) | King’s College London, UK; Huawei, Noah’s Ark Lab, UK; University College London, UK | [📝](../digests/migration-2026-10-22.md) |
| [Hand-in-the-Loop: Improving VLA Policies for Dexterous Manipulation via Seamless Hand-Arm Intervention](https://arxiv.org/abs/2605.15157) | 2026-05-14 | 相邻 | 观察中 | **57** (3/3/2/4) | 未找到仓库 (2026-10-22) | State Key Laboratory of Mechanical System and Vibration, School of Mechanical Engineering, Shanghai Jiao Tong University; Shanghai Key Laboratory of Intelligent Robotics, Meta Robotics Institute, Shanghai Jiao Tong University; ByteDance Seed | [📝](../digests/migration-2026-10-22.md) |
| [NestDex: Nested Policy Learning with Copilot Assisted Teleoperation for Dexterous Manipulation](https://arxiv.org/abs/2608.13362) | 2026-08-13 | 核心 | 观察中 | **48** (3/3/1/3) | 未找到仓库 (2026-10-22) | School of Computer Science, The University of Sydney, Australia; Australian Centre for Robotics, The University of Sydney, Australia; College of Connected Computing, Vanderbilt University, TN, USA | [📝](../digests/migration-2026-10-22.md) |
| [Koala Gripper: Co-designing Robotic Grippers and Data-Capture Devices for Scaling Dexterous Manipulation Learning](https://arxiv.org/abs/2608.20546) | 2026-08-20 | 相邻 | 观察中 | **43** (3/2/1/3) | 未找到仓库 (2026-10-22) | Hajj-Ahmad, Amar et al. | [📝](../digests/migration-2026-10-22.md) |

## <a id="cat-tutorials"></a>Tutorials & Surveys

| 论文 | 首次公开 | 路线 | 优先级 | 总分 (C/E/O/T) | 开源（last_check） | 作者/单位 | 报告 |
|---|---|---|---|---|---|---|---|
| [World Action Models: A Survey](https://arxiv.org/abs/2606.20781) | 2026-06-18 | 相邻 | 观察中 | **63** (4/3/2/4) | 📄 占位仓库 (2026-10-22) | National University of Singapore | [📝](../digests/migration-2026-10-22.md) |
| [Progress Reward Modeling for Robotic Learning: A Comprehensive Survey](https://arxiv.org/abs/2607.21655) | 2026-07-22 | 相邻 | 观察中 | **55** (3/2/3/3) | 📄 占位仓库 · MIT (2026-10-22) | Northwestern University; Carnegie Mellon University; University of Wisconsin–Madison | [📝](../digests/migration-2026-10-22.md) |
| [The Embodiment Gap in Robot Foundation Models](https://arxiv.org/abs/2608.18433) | 2026-08-19 | 相邻 | 观察中 | **43** (3/2/1/3) | 未找到仓库 (2026-10-22) | National Institute of Advanced Industrial Science and Technology (AIST), Japan | [📝](../digests/migration-2026-10-22.md) |
| [Weights or Skills? A Survey of Robot-Learning Techniques: from Action-Predicting Weights to Robots that Write their Own Skills](https://arxiv.org/abs/2608.01851) | 2026-08-03 | 相邻 | 观察中 | **43** (3/2/1/3) | 未找到仓库 (2026-10-22) | UC Berkeley; San Jose State University; Meta | [📝](../digests/migration-2026-10-22.md) |
| [Towards Robotic Dexterous Hand Intelligence: A Survey](https://arxiv.org/abs/2605.13925) | 2026-05-13 | 相邻 | 观察中 | **43** (3/2/1/3) | 未找到仓库 (2026-10-22) | University of Liverpool; The Chinese University of Hong Kong; Xi’an Jiaotong-Liverpool University | [📝](../digests/migration-2026-10-22.md) |
| [World Action Models: The Next Frontier in Embodied AI](https://arxiv.org/abs/2605.12090) | 2026-05-12 | 相邻 | 暂不评级 | — | 🟡 部分开放 · MIT (2026-10-22) | Wang, Siyin et al. | [📝](../digests/migration-2026-10-22.md) |

## <a id="cat-vla"></a>Vision-Language-Action (VLA)

| 论文 | 首次公开 | 路线 | 优先级 | 总分 (C/E/O/T) | 开源（last_check） | 作者/单位 | 报告 |
|---|---|---|---|---|---|---|---|
| 📜 [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) | 2024-06-13 | 核心 | 🔥 重点阅读 | **100** (5/5/5/5) | 💻 实质代码 · MIT (2026-10-22) | Stanford University; UC Berkeley; Toyota Research Institute | [📝](../digests/migration-2026-10-22.md) |
| 📜 [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734) | 2025-03-18 | 核心 | 🔥 重点阅读 | **95** (5/4/5/5) | 💻 实质代码 · Apache-2.0 (2026-10-22) | NVIDIA | [📝](../digests/migration-2026-10-22.md) |
| [Breaking the Vision-Action Shortcut: Latent Interface Training for Generalizable Robotics Foundation Models](https://arxiv.org/abs/2609.12641) | 2026-09-11 | 核心 | 🔥 重点阅读 | **86** (4/4/5/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | South China University of Technology; National University of Singapore; Nanyang Technological University | [📝](../digests/daily/2026-10-22.md) |
| 📜 [RDT-1B: A Diffusion Foundation Model for Bimanual Manipulation](https://arxiv.org/abs/2410.07864) | 2024-10-10 | 核心 | 🔥 重点阅读 | **86** (4/4/5/4) | 💻 实质代码 · MIT (2026-10-22) | Department of Computer Science & Technology, Institute for AI, BNRist Center, Tsinghua-Bosch Joint ML Center, THBI Lab, Tsinghua University | [📝](../digests/migration-2026-10-22.md) |
| [Has GPT-6-Astra Achieved Embodied Intelligence?](https://arxiv.org/abs/2610.22471) | 2026-10-15 | 相邻 | 🔥 重点阅读 | **85** (4/5/4/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | SenseNova | [📝](../digests/daily/2026-10-22.md) |
| [Geometric Action Model for Robot Policy Learning](https://arxiv.org/abs/2606.17046) | 2026-06-15 | 核心 | 🔥 重点阅读 | **83** (4/4/4/5) | 💻 实质代码 · MIT (2026-10-22) | KAIST AI; ETH Zurich; ETH AI Center | [📝](../digests/migration-2026-10-22.md) |
| [World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis](https://arxiv.org/abs/2606.05979) | 2026-06-04 | 核心 | 🔥 重点阅读 | **83** (4/4/5/3) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Shanghai Jiao Tong University (SJTU); Shanghai Innovation Institute (SII); Huazhong University of Science and Technology (HUST) | [📝](../digests/migration-2026-10-22.md) |
| [FlashVLA: Streaming Action Decoding for Fast and Asynchronous VLA Inference](https://arxiv.org/abs/2608.27384) | 2026-08-27 | 核心 | 🔥 重点阅读 | **80** (4/4/4/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | UC San Diego; MIT | [📝](../digests/migration-2026-10-22.md) |
| [$\tau_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation](https://arxiv.org/abs/2608.16885) | 2026-08-17 | 核心 | 🔥 重点阅读 | **80** (4/4/4/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Shanghai Innovation Institute; Agibot Finch; The Chinese University of Hong Kong | [📝](../digests/migration-2026-10-22.md) |
| [TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM](https://arxiv.org/abs/2607.27205) | 2026-07-29 | 核心 | 🔥 重点阅读 | **80** (4/4/4/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Huazhong University of Science and Technology | [📝](../digests/migration-2026-10-22.md) |
| [Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories](https://arxiv.org/abs/2607.15330) | 2026-07-16 | 核心 | 🔥 重点阅读 | **80** (4/4/4/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Xiaomi Robotics | [📝](../digests/migration-2026-10-22.md) |
| [Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization](https://arxiv.org/abs/2601.12993) | 2026-01-19 | 核心 | 🔥 重点阅读 | **80** (4/4/4/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | BeingBeyond Team | [📝](../digests/migration-2026-10-22.md) |
| [$N_0$-VTLA: Scaling Vision-Tactile-Language-Action Model with Latent Tactile Tokens](https://arxiv.org/abs/2607.23782) | 2026-07-26 | 核心 | 👀 值得关注 | **77** (4/4/4/3) | 💻 实质代码 · Apache-2.0 (2026-10-22) | NeoteAI; Fudan TEAI | [📝](../digests/migration-2026-10-22.md) |
| [GigaBrain-0.7: Scaling Embodied Foundation Models to Emergent Capabilities with a Three-System Architecture](https://arxiv.org/abs/2608.15875) | 2026-08-16 | 核心 | 👀 值得关注 | **75** (4/3/4/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | GigaBrain Team | [📝](../digests/migration-2026-10-22.md) |
| [XPolicyLab: A Unified Standard and Open Ecosystem for Robot Policy Evaluation and Deployment](https://arxiv.org/abs/2608.09892) | 2026-08-10 | 相邻 | 👀 值得关注 | **75** (4/3/4/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | MMLab@HKU; THU | [📝](../digests/migration-2026-10-22.md) |
| [From Foundation to Application: Improving VLA Models in Practice](https://arxiv.org/abs/2607.06403) | 2026-07-07 | 核心 | 👀 值得关注 | **75** (4/3/4/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Wu, Wei et al. | [📝](../digests/migration-2026-10-22.md) |
| [SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation](https://arxiv.org/abs/2608.09771) | 2026-08-10 | 核心 | 👀 值得关注 | **74** (3/4/4/4) | 💻 实质代码 · MIT (2026-10-22) | Fudan University; Beijing Academy of Artificial Intelligence; Tsinghua University | [📝](../digests/migration-2026-10-22.md) |
| [LARA: Latent Action Representation Alignment for Vision-Language-Action Models](https://arxiv.org/abs/2606.07100) | 2026-06-05 | 核心 | 👀 值得关注 | **74** (4/4/3/4) | 💻 实质代码 (2026-10-22) | State Key Laboratory of General Artificial Intelligence, BIGAI; Peking University; Delta Intelligence | [📝](../digests/migration-2026-10-22.md) |
| [AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding](https://arxiv.org/abs/2606.06155) | 2026-06-04 | 核心 | 👀 值得关注 | **74** (4/4/3/4) | 💻 实质代码 · MIT (2026-10-22) | Peking University; HKUST (GZ); The Chinese University of Hong Kong | [📝](../digests/migration-2026-10-22.md) |
| [HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation](https://arxiv.org/abs/2604.07993) | 2026-04-09 | 核心 | 👀 值得关注 | **74** (4/4/3/4) | 💻 实质代码 (2026-10-22) | Beijing Innovation Center of Humanoid Robotics; Xi’an Jiaotong University; Nankai University | [📝](../digests/migration-2026-10-22.md) |
| [AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics](https://arxiv.org/abs/2610.28589) | 2026-10-20 | 核心 | 👀 值得关注 | **72** (4/3/4/3) | 💻 实质代码 · Apache-2.0 (2026-10-23) | University of Central Florida; University of Southern California; Michigan State University | [📝](../digests/daily/2026-10-23.md) |
| [VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models](https://arxiv.org/abs/2610.21306) | 2026-10-15 | 核心 | 👀 值得关注 | **71** (3/4/4/3) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Zhejiang University; Central South University | [📝](../digests/daily/2026-10-22.md) |
| [What Matters for Latent Actions in Robot Learning](https://arxiv.org/abs/2608.19613) | 2026-08-20 | 相邻 | 👀 值得关注 | **71** (3/4/4/3) | 💻 实质代码 · MIT (2026-10-22) | College of Intelligent Robotics and Advanced Manufacturing, Fudan University; Xiaomi EV; Tsinghua Shenzhen International Graduate School, Tsinghua University | [📝](../digests/migration-2026-10-22.md) |
| [World Tokens: Enhancing Embodied Policies with Training-Time World Modeling](https://arxiv.org/abs/2608.09730) | 2026-08-10 | 核心 | 👀 值得关注 | **71** (3/4/4/3) | 💻 实质代码 · MIT (2026-10-22) | JIUTIAN Research; Zhongguancun Academy | [📝](../digests/migration-2026-10-22.md) |
| [T-Rex: Tactile-Reactive Dexterous Manipulation](https://arxiv.org/abs/2606.17055) | 2026-06-15 | 核心 | 👀 值得关注 | **71** (4/4/2/5) | 未找到仓库 (2026-10-22) | UC Berkeley; NVIDIA; Stanford | [📝](../digests/migration-2026-10-22.md) |
| [IntentVLA: Short-Horizon Intent Modeling for Aliased Robot Manipulation](https://arxiv.org/abs/2605.14712) | 2026-05-14 | 核心 | 👀 值得关注 | **71** (4/4/3/3) | 🟡 部分开放 (2026-10-22) | Huazhong University of Science and Technology; Zhongguancun Academy; Harbin Institute of Technology | [📝](../digests/migration-2026-10-22.md) |
| [HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent RL](https://arxiv.org/abs/2608.16837) | 2026-08-17 | 核心 | 👀 值得关注 | **68** (4/4/2/4) | 未找到仓库 (2026-10-22) | Peking University; Beijing Innovation Center of Humanoid Robotics; Nankai University | [📝](../digests/migration-2026-10-22.md) |
| [G0.5: One Autoregressive Stream for Robot Reasoning and Action](https://arxiv.org/abs/2608.11739) | 2026-08-12 | 核心 | 👀 值得关注 | **68** (4/4/2/4) | 📄 占位仓库 (2026-10-22) | Galaxea Team | [📝](../digests/migration-2026-10-22.md) |
| [RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models](https://arxiv.org/abs/2607.26991) | 2026-07-29 | 核心 | 👀 值得关注 | **68** (3/4/3/4) | 🟡 部分开放 · Apache-2.0 (2026-10-22) | National University of Singapore; University of Toronto; Singapore Technologies Engineering | [📝](../digests/migration-2026-10-22.md) |
| [Qwen-VLA: Alibaba's Embodied Foundation Model](https://arxiv.org/abs/2605.30280) | 2026-05-28 | 核心 | 👀 值得关注 | **68** (4/4/2/4) | 📄 占位仓库 (2026-10-22) | Qwen Team | [📝](../digests/migration-2026-10-22.md) |
| [BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action Framework for 3D Manipulation](https://arxiv.org/abs/2608.05042) | 2026-08-05 | 核心 | 👀 值得关注 | **67** (3/5/2/4) | 未找到仓库 (2026-10-22) | New Laboratory of Pattern Recognition (NLPR), Institute of Automation, Chinese Academy of Sciences; School of Artificial Intelligence, University of Chinese Academy of Sciences; FiveAges | [📝](../digests/migration-2026-10-22.md) |
| [Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots](https://arxiv.org/abs/2607.02501) | 2026-07-02 | 相邻 | 👀 值得关注 | **66** (3/3/4/3) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Southeast University; Nanjing University; Microsoft Research | [📝](../digests/migration-2026-10-22.md) |
| [LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction](https://arxiv.org/abs/2506.13751) | 2025-06-16 | 核心 | 👀 值得关注 | **66** (4/3/2/5) | 未找到仓库 (2026-10-22) | University of California Berkeley; Norwegian University of Science and Technology; Simon Fraser University | [📝](../digests/migration-2026-10-22.md) |
| [EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](https://arxiv.org/abs/2609.01281) | 2026-09-01 | 核心 | 观察中 | **63** (3/3/3/4) | 💻 实质代码 (2026-10-22) | College of Computer Science and Technology, Zhejiang University; Nanjing University of Aeronautics and Astronautics; Cornell University | [📝](../digests/migration-2026-10-22.md) |
| [ActionMap: Robot Policy Learning via Voxel Action Heatmap](https://arxiv.org/abs/2606.06904) | 2026-06-05 | 核心 | 观察中 | **62** (3/4/2/4) | 未找到仓库 (2026-10-22) | Show Lab, National University of Singapore; NVIDIA | [📝](../digests/migration-2026-10-22.md) |
| [GeoAlign: Beyond Semantics with State-Guided Spatial Alignment in VLA Models](https://arxiv.org/abs/2606.03240) | 2026-06-02 | 核心 | 观察中 | **62** (3/4/2/4) | 未找到仓库 (2026-10-22) | Tongji University; Shanghai Innovation Institute; Shanghai Jiao Tong University | [📝](../digests/migration-2026-10-22.md) |
| [Intercepting the Future: Latent-Space Predictive World Model for Dynamic VLA Manipulation](https://arxiv.org/abs/2606.02486) | 2026-06-01 | 核心 | 观察中 | **62** (4/4/1/4) | 未找到仓库 (2026-10-22) | Robotics Institute, Carnegie Mellon University, Pittsburgh, USA | [📝](../digests/migration-2026-10-22.md) |
| [Hide-and-Seek in Trajectories: Discovering Failure Signals for VLA Runtime Monitoring](https://arxiv.org/abs/2605.30834) | 2026-05-29 | 相邻 | 观察中 | **62** (3/4/2/4) | 📄 占位仓库 (2026-10-22) | University of Wisconsin–Madison; Georgia Institute of Technology | [📝](../digests/migration-2026-10-22.md) |
| [From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation](https://arxiv.org/abs/2610.29560) | 2026-10-21 | 核心 | 观察中 | **60** (3/3/3/3) | 💻 实质代码 · Apache-2.0 (2026-10-23) | University of Science and Technology of China; Shanghai Artificial Intelligence Laboratory; Shanghai Jiao Tong University | [📝](../digests/daily/2026-10-23.md) |
| [Self-Evolving Coding Agents: From Digital Programs to Physical-World Intelligence](https://arxiv.org/abs/2609.35432) | 2026-09-28 | 核心 | 观察中 | **60** (4/3/2/3) | 📄 占位仓库 (2026-10-22) | HexaFuture | [📝](../digests/daily/2026-10-22.md) |
| [Zetta $\zeta$: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence](https://arxiv.org/abs/2608.16590) | 2026-08-17 | 核心 | 观察中 | **60** (4/3/2/3) | 未找到仓库 (2026-10-22) | Institute for AI Industry Research (AIR), Tsinghua University; Z-Trans AI | [📝](../digests/migration-2026-10-22.md) |
| [Does VLA Even Know the Basics? Measuring Commonsense and World Knowledge Retention in Vision-Language-Action Models](https://arxiv.org/abs/2606.19297) | 2026-06-17 | 相邻 | 观察中 | **60** (3/3/3/3) | 💻 实质代码 · MIT (2026-10-22) | CogAI Lab; FusionBrain Lab; IAI MSU | [📝](../digests/migration-2026-10-22.md) |
| [GesVLA: Pointing Gesture Grounding for Vision-Language-Action Models](https://arxiv.org/abs/2605.22812) | 2026-05-21 | 核心 | 观察中 | **60** (3/3/3/3) | 💻 实质代码 (2026-10-22) | Tsinghua University; Dexmal | [📝](../digests/migration-2026-10-22.md) |
| [SparkVLA: Stop-Aware Hierarchical VLA with Adaptive Action Chunking for Long-Horizon Manipulation](https://arxiv.org/abs/2608.16172) | 2026-08-17 | 核心 | 观察中 | **59** (3/4/2/3) | 未找到仓库 (2026-10-22) | Beijing Institute of Technology; Tsinghua University | [📝](../digests/migration-2026-10-22.md) |
| [DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for Cross-Embodiment Manipulation](https://arxiv.org/abs/2608.06374) | 2026-08-06 | 核心 | 观察中 | **59** (3/4/2/3) | 未找到仓库 (2026-10-22) | The Hong Kong University of Science and Technology (Guangzhou); COCO Matrix | [📝](../digests/migration-2026-10-22.md) |
| [World-to-Wrist: Task-Conditioned Future Wrist Modeling for Fine-Grained Robot Manipulation](https://arxiv.org/abs/2608.05369) | 2026-08-05 | 核心 | 观察中 | **59** (3/4/2/3) | 未找到仓库 (2026-10-22) | The Hong Kong University of Science and Technology; National University of Singapore; Nanyang Technological University | [📝](../digests/migration-2026-10-22.md) |
| [3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training](https://arxiv.org/abs/2606.04436) | 2026-06-03 | 核心 | 观察中 | **59** (3/4/2/3) | 未找到仓库 (2026-10-22) | Shanghai Jiao Tong University; Daimon Robotics; Harbin Institute of Technology | [📝](../digests/migration-2026-10-22.md) |
| [Gaze2Act: Gaze-Conditioned Vision-Language-Action Policies for Interactive Robot Manipulation](https://arxiv.org/abs/2605.30282) | 2026-05-28 | 核心 | 观察中 | **59** (3/4/2/3) | 未找到仓库 (2026-10-22) | MARS Lab, Nanyang Technological University | [📝](../digests/migration-2026-10-22.md) |
| [Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action](https://arxiv.org/abs/2605.22283) | 2026-05-21 | 核心 | 观察中 | **59** (3/4/2/3) | 未找到仓库 (2026-10-22) | Thrust of Artificial Intelligence, The Hong Kong University of Science and Technology (Guangzhou), China; AI2Robotics; Department of Computer Science and Engineering, The Hong Kong University of Science and Technology, Hong Kong SAR, China | [📝](../digests/migration-2026-10-22.md) |
| [Towards Human-Like Manipulation through RL-Augmented Teleoperation and Mixture-of-Dexterous-Experts VLA](https://arxiv.org/abs/2603.08122) | 2026-03-09 | 核心 | 观察中 | **57** (3/3/2/4) | 未找到仓库 (2026-10-22) | Zhongguancun Academy; National University of Singapore; Shanghai Jiao Tong University | [📝](../digests/migration-2026-10-22.md) |
| [BORA: Bridging Offline Reinforcement Learning and Online Residual Adaptation for Real-World Dexterous VLA Models](https://arxiv.org/abs/2605.30226) | 2026-05-28 | 核心 | 观察中 | **56** (3/4/1/4) | 未找到仓库 (2026-10-22) | Shanghai Jiao Tong University; Shanghai AI Laboratory; USTC | [📝](../digests/migration-2026-10-22.md) |
| [EXIMO: VLM Guided Exploration of VLA Policies](https://arxiv.org/abs/2608.19891) | 2026-08-20 | 核心 | 观察中 | **54** (3/3/1/5) | 未找到仓库 (2026-10-22) | Google DeepMind | [📝](../digests/migration-2026-10-22.md) |
| [EATR-Stereo: Embodiment-Aware Routing of Paired Stereo Evidence for Humanoid Vision-Language-Action Control](https://arxiv.org/abs/2608.17453) | 2026-08-18 | 核心 | 观察中 | **53** (3/4/1/3) | 未找到仓库 (2026-10-22) | Harbin Institute of Technology; Honor | [📝](../digests/migration-2026-10-22.md) |
| [StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models](https://arxiv.org/abs/2608.11671) | 2026-08-12 | 核心 | 观察中 | **53** (3/4/1/3) | 未找到仓库 (2026-10-22) | Xu, Siyu et al. | [📝](../digests/migration-2026-10-22.md) |
| [Hidden in Plain Sight: Diffusion-Based Unrestricted Robotic Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2608.10393) | 2026-08-11 | 相邻 | 观察中 | **53** (3/4/1/3) | 未找到仓库 (2026-10-22) | Xi'an Jiaotong University; Shanghai AI Laboratory; University of Science and Technology of China | [📝](../digests/migration-2026-10-22.md) |
| [AtlasVLA: Persistent World-Ego State Modeling for Vision-Language-Action Models](https://arxiv.org/abs/2608.06729) | 2026-08-07 | 核心 | 观察中 | **53** (3/4/1/3) | 未找到仓库 (2026-10-22) | Institute of Automation, Chinese Academy of Sciences; University of Chinese Academy of Sciences; Beijing Freedo Technology Co., Ltd. | [📝](../digests/migration-2026-10-22.md) |
| [ElegantVLA: Learning When to Think for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2605.29438) | 2026-05-28 | 相邻 | 观察中 | **53** (3/4/1/3) | 未找到仓库 (2026-10-22) | Tsinghua University; University of Illinois at Urbana-Champaign | [📝](../digests/migration-2026-10-22.md) |
| [Lost in Reconstruction: Aligning Action Representations with Language in Vision-Language-Action Models](https://arxiv.org/abs/2608.10484) | 2026-08-11 | 核心 | 观察中 | **51** (3/3/1/4) | 未找到仓库 (2026-10-22) | Carnegie Mellon University | [📝](../digests/migration-2026-10-22.md) |
| [TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies](https://arxiv.org/abs/2606.06491) | 2026-06-04 | 核心 | 观察中 | **51** (3/3/1/4) | 未找到仓库 (2026-10-22) | UNC; RUC | [📝](../digests/migration-2026-10-22.md) |
| [TTT-VLA: Test-Time Latent Prompt Optimization for Vision-Language-Action Models](https://arxiv.org/abs/2606.03127) | 2026-06-02 | 核心 | 观察中 | **51** (3/3/1/4) | 未找到仓库 (2026-10-22) | ByteDance Seed; The University of Adelaide; Tsinghua University | [📝](../digests/migration-2026-10-22.md) |
| [LIBERO-VIFO: Benchmarking the Capability and Safety of Visual Cue Following in Vision-Language-Action Models](https://arxiv.org/abs/2608.17600) | 2026-08-18 | 相邻 | 观察中 | **48** (3/3/1/3) | 未找到仓库 (2026-10-22) | Qian, Zhengyan et al. | [📝](../digests/migration-2026-10-22.md) |
| [NebulaVLA: A Dual-Frequency Vision-Language-Action Model With Guide Action for Robotic Manipulation](https://arxiv.org/abs/2608.16503) | 2026-08-17 | 核心 | 观察中 | **48** (3/3/1/3) | 未找到仓库 (2026-10-22) | ZTE Corporation | [📝](../digests/migration-2026-10-22.md) |
| [Temporal GRPO: Beyond Trajectory-Level Credit in Vision-Language-Action Reinforcement Learning](https://arxiv.org/abs/2608.13026) | 2026-08-13 | 核心 | 观察中 | **48** (3/3/1/3) | 未找到仓库 (2026-10-22) | Institute of Software Chinese Academy of Sciences, Beijing, China; University of Chinese Academy of Sciences, Beijing, China | [📝](../digests/migration-2026-10-22.md) |
| [DREAM-Chunk: Reactive Action Chunking with Latent World Model](https://arxiv.org/abs/2606.18589) | 2026-06-17 | 核心 | 观察中 | **48** (3/3/1/3) | 未找到仓库 (2026-10-22) | Purdue University; Stanford University | [📝](../digests/migration-2026-10-22.md) |
| [Can VLA Models Learn from Real-World Data Continually without Forgetting?](https://arxiv.org/abs/2605.26820) | 2026-05-26 | 相邻 | 观察中 | **48** (3/3/1/3) | 未找到仓库 (2026-10-22) | HKU; EIT, Ningbo; SUSTech | [📝](../digests/migration-2026-10-22.md) |
| [Neural Introspection Gating for Adaptive KV-Cache Reuse in Vision-Language-Action Models](https://arxiv.org/abs/2608.10824) | 2026-08-11 | 核心 | 观察中 | **45** (2/3/1/4) | 未找到仓库 (2026-10-22) | Graduate School of Information Science and Technology, The University of Tokyo | [📝](../digests/migration-2026-10-22.md) |
| [PhysiFlow: Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent Flow Matching and Robust Tracking](https://arxiv.org/abs/2603.05410) | 2026-03-05 | 核心 | 观察中 | **42** (2/3/1/3) | 未找到仓库 (2026-10-22) | Department of Automation, Shanghai Jiao Tong University | [📝](../digests/migration-2026-10-22.md) |
| [HODAgent: Towards On-Demand, Responsive Humanoids for Physical World Human Interaction](https://arxiv.org/abs/2608.17584) | 2026-08-18 | 核心 | 暂不评级 | — | 未找到仓库 (2026-10-22) | Chen, Wang Warren et al. | [📝](../digests/migration-2026-10-22.md) |
| [Action with Visual Primitives](https://arxiv.org/abs/2605.22183) | 2026-05-21 | 核心 | 暂不评级 | — | 未找到仓库 (2026-10-22) | Guo, Weilong et al. | [📝](../digests/migration-2026-10-22.md) |

## <a id="cat-world-model"></a>World Models

| 论文 | 首次公开 | 路线 | 优先级 | 总分 (C/E/O/T) | 开源（last_check） | 作者/单位 | 报告 |
|---|---|---|---|---|---|---|---|
| 📜 [Cosmos World Foundation Model Platform for Physical AI](https://arxiv.org/abs/2501.03575) | 2025-01-07 | 核心 | 🔥 重点阅读 | **89** (5/4/4/5) | 💻 实质代码 · Apache-2.0 (2026-10-22) | NVIDIA | [📝](../digests/migration-2026-10-22.md) |
| [Long-WAM: Scaling the Context of World-Action Models](https://arxiv.org/abs/2610.10528) | 2026-10-07 | 核心 | 🔥 重点阅读 | **88** (4/5/4/5) | 💻 实质代码 · Apache-2.0 (2026-10-22) | NVIDIA; MIT; HKU | [📝](../digests/daily/2026-10-22.md) |
| [Flex-$\pi$: A Multi-Stream World-Action Model with Compute Flexibility](https://arxiv.org/abs/2608.10860) | 2026-08-11 | 核心 | 🔥 重点阅读 | **88** (4/5/4/5) | 💻 实质代码 · MIT (2026-10-22) | University of Washington; Allen Institute for AI | [📝](../digests/migration-2026-10-22.md) |
| [Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](https://arxiv.org/abs/2610.26855) | 2026-10-19 | 核心 | 🔥 重点阅读 | **86** (5/4/4/4) | 🟡 部分开放 · Apache-2.0 (2026-10-22) | Nanyang Technological University; Ropedia; Duke University | [📝](../digests/daily/2026-10-22.md) |
| [LeWAM: End-to-End World and Action Modeling with JEPAs](https://arxiv.org/abs/2610.12818) | 2026-10-08 | 核心 | 🔥 重点阅读 | **86** (4/4/5/4) | 💻 实质代码 · MIT (2026-10-22) | UC San Diego; ETH Zurich; University of British Columbia | [📝](../digests/daily/2026-10-22.md) |
| [OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining](https://arxiv.org/abs/2609.07398) | 2026-09-07 | 核心 | 🔥 重点阅读 | **86** (5/4/4/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | National University of Singapore; Tsinghua University; Peking University | [📝](../digests/daily/2026-10-22.md) |
| [Agentic World Action Models](https://arxiv.org/abs/2610.30136) | 2026-10-21 | 核心 | 🔥 重点阅读 | **83** (4/4/4/5) | 💻 实质代码 · Apache-2.0 (2026-10-23) | UC Berkeley; NVIDIA; University of Pennsylvania | [📝](../digests/daily/2026-10-23.md) |
| [CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators](https://arxiv.org/abs/2608.27406) | 2026-08-27 | 核心 | 🔥 重点阅读 | **83** (4/4/5/3) | 💻 实质代码 · MIT (2026-10-22) | Princeton University | [📝](../digests/migration-2026-10-22.md) |
| [RynnWorld-4D: 4D Embodied World Models for Robotic Manipulation](https://arxiv.org/abs/2607.06559) | 2026-07-07 | 核心 | 🔥 重点阅读 | **80** (4/4/4/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Hong Kong Embodied AI Lab; CUHK; Hupan Lab | [📝](../digests/migration-2026-10-22.md) |
| [$\texttt{WEAVER}$, Better, Faster, Longer: An Effective World Model for Robotic Manipulation](https://arxiv.org/abs/2606.13672) | 2026-06-11 | 核心 | 🔥 重点阅读 | **80** (4/4/4/4) | 💻 实质代码 · MIT (2026-10-22) | Mila - Québec AI Institute; Université de Montréal; Carnegie Mellon University | [📝](../digests/migration-2026-10-22.md) |
| [$\mu_0$: A Scalable 3D Interaction-Trace World Model](https://arxiv.org/abs/2606.13769) | 2026-06-11 | 核心 | 🔥 重点阅读 | **80** (4/4/4/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Seoul National University; University of Maryland, College Park; All Purpose AI | [📝](../digests/migration-2026-10-22.md) |
| [OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics](https://arxiv.org/abs/2606.04463) | 2026-06-03 | 核心 | 🔥 重点阅读 | **80** (4/4/4/4) | 🟡 部分开放 · Apache-2.0 (2026-10-22) | Peking University; University of Michigan; NVIDIA | [📝](../digests/migration-2026-10-22.md) |
| [GreenWAM: A World Foundation Model for Robotics](https://arxiv.org/abs/2610.18774) | 2026-10-13 | 核心 | 👀 值得关注 | **77** (4/4/4/3) | 🟡 部分开放 · OpenMDW-1.1 (2026-10-22) | Brain Team, Sber Robotics Center | [📝](../digests/daily/2026-10-22.md) |
| [Keep the Future, Drop the Rollout: RIFT for World Action Models](https://arxiv.org/abs/2608.11521) | 2026-08-12 | 核心 | 👀 值得关注 | **77** (4/4/4/3) | 💻 实质代码 · MIT (2026-10-22) | Australian National University; FreiNexus; Beijing Normal University | [📝](../digests/migration-2026-10-22.md) |
| [$N_0$-TWAM: Scaling Tactile-Native World-Action Model for Contact-Rich Manipulation](https://arxiv.org/abs/2607.23783) | 2026-07-26 | 核心 | 👀 值得关注 | **77** (4/4/4/3) | 💻 实质代码 · CC-BY-NC (2026-10-22) | NeoteAI Team; Fudan TEAI Team | [📝](../digests/migration-2026-10-22.md) |
| [PAWBench: How Far Are We from Probabilistically Aligned World Modeling?](https://arxiv.org/abs/2608.27345) | 2026-08-27 | 相邻 | 👀 值得关注 | **74** (3/4/4/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Shanghai Jiao Tong University; Shanghai AI Laboratory; Krea AI | [📝](../digests/migration-2026-10-22.md) |
| [DriftWorld: Fast World Modeling through Drifting](https://arxiv.org/abs/2607.15065) | 2026-07-16 | 核心 | 👀 值得关注 | **74** (4/4/3/4) | 💻 实质代码 (2026-10-22) | Massachusetts Institute of Technology; Harvard University | [📝](../digests/migration-2026-10-22.md) |
| [Kairos: A Regret-Aware Native World-Action Model Stack for Physical AI](https://arxiv.org/abs/2606.16533) | 2026-06-15 | 核心 | 👀 值得关注 | **72** (4/3/4/3) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Kairos Team et al. | [📝](../digests/migration-2026-10-22.md) |
| [stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation](https://arxiv.org/abs/2605.21800) | 2026-05-20 | 相邻 | 👀 值得关注 | **72** (3/3/4/5) | 💻 实质代码 · MIT (2026-10-22) | Mila & Université de Montréal; New York University; Universidade Federal de Minas Gerais | [📝](../digests/migration-2026-10-22.md) |
| [Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention for Video Generation and World Models](https://arxiv.org/abs/2608.18484) | 2026-08-19 | 相邻 | 👀 值得关注 | **71** (3/4/4/3) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Texas A&M University | [📝](../digests/migration-2026-10-22.md) |
| [Hydra-0: Action Flow for Generalist World Modeling and Control](https://arxiv.org/abs/2608.18077) | 2026-08-18 | 核心 | 👀 值得关注 | **71** (4/4/2/5) | 未找到仓库 (2026-10-22) | NVIDIA; Brown University; Columbia University | [📝](../digests/migration-2026-10-22.md) |
| [Masked Visual Actions for Unified World Modeling](https://arxiv.org/abs/2607.19343) | 2026-07-21 | 核心 | 👀 值得关注 | **71** (4/4/2/5) | 未找到仓库 (2026-10-22) | Stanford University; University of Maryland, College Park; Harvard University | [📝](../digests/migration-2026-10-22.md) |
| [KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding](https://arxiv.org/abs/2607.19876) | 2026-07-22 | 相邻 | 👀 值得关注 | **69** (3/3/4/4) | 💻 实质代码 · MIT (2026-10-22) | Institute of Artificial Intelligence (TeleAI), China Telecom, China; National University of Singapore, Singapore; Fudan University, China | [📝](../digests/migration-2026-10-22.md) |
| [iMaC: Translating Actions into Motion and Contact Images for Embodied World Models](https://arxiv.org/abs/2606.09813) | 2026-06-08 | 核心 | 👀 值得关注 | **69** (4/3/3/4) | 💻 实质代码 (2026-10-22) | GigaAI; Tsinghua University; Nanyang Technological University | [📝](../digests/migration-2026-10-22.md) |
| [Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models](https://arxiv.org/abs/2605.31158) | 2026-05-29 | 相邻 | 👀 值得关注 | **69** (3/3/4/4) | 💻 实质代码 · MIT (2026-10-22) | Zhejiang University; NVIDIA | [📝](../digests/migration-2026-10-22.md) |
| [WALL-SS: Scaling Long-horizon World Models via Next-Scale Autoregression](https://arxiv.org/abs/2608.26239) | 2026-08-26 | 核心 | 👀 值得关注 | **68** (4/4/2/4) | 📄 占位仓库 · MIT (2026-10-22) | X Square Robot | [📝](../digests/migration-2026-10-22.md) |
| [ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World Models](https://arxiv.org/abs/2608.14022) | 2026-08-14 | 核心 | 👀 值得关注 | **66** (3/3/4/3) | 💻 实质代码 · Apache-2.0 (2026-10-22) | CUHK; Tencent PCG; FDU | [📝](../digests/migration-2026-10-22.md) |
| [ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU](https://arxiv.org/abs/2607.19191) | 2026-07-21 | 核心 | 👀 值得关注 | **66** (3/3/4/3) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Jiang, Fan et al. | [📝](../digests/migration-2026-10-22.md) |
| [AlayaWorld: Interactive Long-Horizon World Modeling -- Full Technical Report](https://arxiv.org/abs/2607.18367) | 2026-07-20 | 相邻 | 👀 值得关注 | **66** (3/3/4/3) | 💻 实质代码 · custom (2026-10-22) | Alaya Lab | [📝](../digests/migration-2026-10-22.md) |
| [DreamX-World 1.0: A General-Purpose Interactive World Model](https://arxiv.org/abs/2606.16993) | 2026-06-15 | 核心 | 👀 值得关注 | **66** (3/3/4/3) | 💻 实质代码 · Apache-2.0 (2026-10-22) | DreamX Team | [📝](../digests/migration-2026-10-22.md) |
| [MemoryWAM: Efficient World Action Modeling with Persistent Memory](https://arxiv.org/abs/2606.20562) | 2026-06-18 | 核心 | 👀 值得关注 | **65** (4/4/1/5) | 未找到仓库 (2026-10-22) | The Chinese University of Hong Kong; Tsinghua University; Zhejiang University | [📝](../digests/migration-2026-10-22.md) |
| [Learning How the World Evolves: Extrapolative Video World Models via Latent Dynamics Reasoning](https://arxiv.org/abs/2608.09926) | 2026-08-10 | 相邻 | 观察中 | **63** (3/3/3/4) | 🟡 部分开放 · CC-BY-NC (2026-10-22) | UCSD; Adobe | [📝](../digests/migration-2026-10-22.md) |
| [Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models](https://arxiv.org/abs/2606.25473) | 2026-06-24 | 相邻 | 观察中 | **63** (3/3/3/4) | 💻 实质代码 · Apache-2.0 (2026-10-22) | Tsinghua University; NVIDIA; UT Austin | [📝](../digests/migration-2026-10-22.md) |
| [World Value Models for Robotic Manipulation](https://arxiv.org/abs/2606.24742) | 2026-06-23 | 核心 | 观察中 | **63** (4/3/2/4) | 📄 占位仓库 (2026-10-22) | ByteDance Seed; Peking University; Tsinghua University | [📝](../digests/migration-2026-10-22.md) |
| [Sensorimotor World Models: Perception for Action via Inverse Dynamics](https://arxiv.org/abs/2606.20104) | 2026-06-18 | 核心 | 观察中 | **63** (3/3/3/4) | 💻 实质代码 · MIT (2026-10-22) | Max Planck Institute for Intelligent Systems, Tübingen, Germany; Department of Computer Science, Brown University, Providence, RI, USA; ELLIS Institute, Tübingen, Germany | [📝](../digests/migration-2026-10-22.md) |
| [Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation](https://arxiv.org/abs/2606.17030) | 2026-06-15 | 核心 | 观察中 | **63** (4/3/2/4) | 未找到仓库 (2026-10-22) | Qwen Team | [📝](../digests/migration-2026-10-22.md) |
| [WorldOlympiad: Can Your World Model Survive a Triathlon?](https://arxiv.org/abs/2606.11129) | 2026-06-09 | 相邻 | 观察中 | **63** (3/3/3/4) | 💻 实质代码 (2026-10-22) | The Hong Kong University of Science and Technology; Monash University; TRE, Alibaba Group | [📝](../digests/migration-2026-10-22.md) |
| [Latent Spatial Memory for Video World Models](https://arxiv.org/abs/2606.09828) | 2026-06-08 | 核心 | 观察中 | **63** (3/3/3/4) | 💻 实质代码 · MIT (2026-10-22) | Zhejiang University; Microsoft Research; Adelaide University | [📝](../digests/migration-2026-10-22.md) |
| [MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.09215) | 2026-06-08 | 核心 | 观察中 | **62** (4/4/1/4) | 未找到仓库 (2026-10-22) | Mondo Robotics; HKUST (GZ); HKUST | [📝](../digests/migration-2026-10-22.md) |
| [Dreaming when Necessary: Advancing World Action Models with Adaptive Multi-Modal Reasoning](https://arxiv.org/abs/2606.07089) | 2026-06-05 | 核心 | 观察中 | **62** (3/4/2/4) | 未找到仓库 (2026-10-22) | Tsinghua University; Manifold AI | [📝](../digests/migration-2026-10-22.md) |
| [Reinforcing VLAs in Task-Agnostic World Models](https://arxiv.org/abs/2605.12334) | 2026-05-12 | 核心 | 观察中 | **62** (4/4/1/4) | 未找到仓库 (2026-10-22) | Nanjing University; University of Illinois at Urbana-Champaign; University of Technology Sydney | [📝](../digests/migration-2026-10-22.md) |
| [SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space](https://arxiv.org/abs/2608.01397) | 2026-08-02 | 核心 | 观察中 | **59** (3/4/2/3) | 📄 占位仓库 (2026-10-22) | Zhao, Ruiteng et al. | [📝](../digests/migration-2026-10-22.md) |
| [ContactWorld: What Matters in Vision-Tactile World Models for Contact-Rich Manipulation](https://arxiv.org/abs/2606.13877) | 2026-06-11 | 相邻 | 观察中 | **59** (3/4/2/3) | 未找到仓库 (2026-10-22) | Department of Industrial Engineering, Purdue University; Department of Mechanical Engineering, Texas A&M University | [📝](../digests/migration-2026-10-22.md) |
| [H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models](https://arxiv.org/abs/2608.13049) | 2026-08-13 | 相邻 | 观察中 | **57** (3/3/2/4) | 📄 占位仓库 (2026-10-22) | Shanghai Jiao Tong University; Shanghai Artificial Intelligence Laboratory | [📝](../digests/migration-2026-10-22.md) |
| [WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reactivity](https://arxiv.org/abs/2608.02603) | 2026-08-03 | 相邻 | 观察中 | **57** (3/3/2/4) | 📄 占位仓库 (2026-10-22) | CASIA; SLAI; CUHK | [📝](../digests/migration-2026-10-22.md) |
| [Wonder: Video World Model Done Better](https://arxiv.org/abs/2607.26037) | 2026-07-28 | 核心 | 观察中 | **57** (3/3/2/4) | 未找到仓库 (2026-10-22) | Adobe Research; Johns Hopkins University | [📝](../digests/migration-2026-10-22.md) |
| [MemLearner: Learning to Query Context memory for Video World Models](https://arxiv.org/abs/2606.31734) | 2026-06-30 | 相邻 | 观察中 | **57** (3/3/2/4) | 未找到仓库 (2026-10-22) | The University of Hong Kong; Fudan University; Zhejiang University | [📝](../digests/migration-2026-10-22.md) |
| [Targeting World Models to Compromise Robot Learning Pipelines](https://arxiv.org/abs/2606.09499) | 2026-06-08 | 相邻 | 观察中 | **57** (4/3/1/4) | 未找到仓库 (2026-10-22) | Northeastern University; University of Massachusetts Amherst | [📝](../digests/migration-2026-10-22.md) |
| [DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation](https://arxiv.org/abs/2608.13489) | 2026-08-13 | 核心 | 观察中 | **54** (3/3/2/3) | 📄 占位仓库 · MIT (2026-10-22) | DreamX Team | [📝](../digests/migration-2026-10-22.md) |
| [WorldCycle: Self-Verifiable Reinforcement Learning for Long-Horizon Video World Models](https://arxiv.org/abs/2608.04964) | 2026-08-05 | 核心 | 观察中 | **54** (3/3/2/3) | 未找到仓库 (2026-10-22) | The Hong Kong University of Science and Technology; Wuhan University; AI Technology Center, Tencent Video, Tencent | [📝](../digests/migration-2026-10-22.md) |
| [STRIPS-WM: Learning Grounded Propositional STRIPS-style World Models from Images](https://arxiv.org/abs/2606.06832) | 2026-06-05 | 核心 | 观察中 | **54** (3/3/2/3) | 未找到仓库 (2026-10-22) | Department of Robotics Engineering, Worcester Polytechnic Institute, United States | [📝](../digests/migration-2026-10-22.md) |
| [PiL-World: A Chunk-Wise World Model for VLA Policy-in-the-Loop Evaluation](https://arxiv.org/abs/2606.05773) | 2026-06-04 | 相邻 | 观察中 | **54** (3/3/2/3) | 未找到仓库 (2026-10-22) | Tongji University; AIRC, Midea Group | [📝](../digests/migration-2026-10-22.md) |
| [DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation](https://arxiv.org/abs/2608.20114) | 2026-08-20 | 核心 | 观察中 | **53** (3/4/1/3) | 未找到仓库 (2026-10-22) | Tsinghua University; Shanghai Artificial Intelligence Laboratory; Harbin Institute of Technology | [📝](../digests/migration-2026-10-22.md) |
| [Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation](https://arxiv.org/abs/2606.18960) | 2026-06-17 | 核心 | 观察中 | **53** (3/4/1/3) | 未找到仓库 (2026-10-22) | Dalian University of Technology; Samsung R&D Institute China-Beijing (SRCB), China | [📝](../digests/migration-2026-10-22.md) |
| [Discrete-WAM: Unified Discrete Vision-Action Token Editing for World-Policy Learning](https://arxiv.org/abs/2606.05645) | 2026-06-04 | 核心 | 观察中 | **53** (3/4/1/3) | 未找到仓库 (2026-10-22) | Xiaomi EV | [📝](../digests/migration-2026-10-22.md) |
| [GeoSem-WAM: Geometry- and Semantic-Aware World Action Models](https://arxiv.org/abs/2606.03188) | 2026-06-02 | 核心 | 观察中 | **53** (3/4/1/3) | 未找到仓库 (2026-10-22) | HKUST(GZ); OC; HKU | [📝](../digests/migration-2026-10-22.md) |
| [ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models](https://arxiv.org/abs/2608.13438) | 2026-08-13 | 相邻 | 观察中 | **51** (3/3/1/4) | 未找到仓库 (2026-10-22) | College of Connected Computing, Vanderbilt University, USA; School of Computer Science, The University of Sydney, Australia; Australian Centre for Robotics, The University of Sydney, Australia | [📝](../digests/migration-2026-10-22.md) |
| [Toward the Cognitive--Physical Limits of Embodied Intelligence through a World-Model-Centric Autonomous Racing Agent](https://arxiv.org/abs/2608.10618) | 2026-08-11 | 核心 | 观察中 | **51** (3/3/1/4) | 未找到仓库 (2026-10-22) | School of Mechanical and Aerospace Engineering, Nanyang Technological University; K2 Holding, L.L.C, Abu Dhabi, United Arab Emirates | [📝](../digests/migration-2026-10-22.md) |
| [Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control](https://arxiv.org/abs/2607.25337) | 2026-07-28 | 核心 | 观察中 | **51** (3/3/2/2) | 未找到仓库 (2026-10-22) | Hong Kong Baptist University | [📝](../digests/migration-2026-10-22.md) |
| [CLAW: Learning Continuous Latent Action World Models via Adversarial Latent Regularization](https://arxiv.org/abs/2606.04130) | 2026-06-02 | 核心 | 观察中 | **51** (3/3/1/4) | 未找到仓库 (2026-10-22) | University of Chicago; Argonne National Laboratory; Toyota Technological Institute at Chicago | [📝](../digests/migration-2026-10-22.md) |
| [One Future, Every Robot: Label-Efficient Collective-State Prediction with Decentralized JEPA](https://arxiv.org/abs/2607.28443) | 2026-07-30 | 核心 | 观察中 | **48** (3/3/1/3) | 未找到仓库 (2026-10-22) | ITMO University | [📝](../digests/migration-2026-10-22.md) |
| [WAM-RL: World-Action Model Reinforcement Learning with Reconstruction Rewards and Online Video SFT](https://arxiv.org/abs/2606.17906) | 2026-06-16 | 核心 | 观察中 | **46** (3/2/1/4) | 未找到仓库 (2026-10-22) | State Key Laboratory of Multimedia Information Processing, School of Computer Science, Peking University; Northeastern University; Tsinghua University | [📝](../digests/migration-2026-10-22.md) |
| [WorldDiT: A Unified Diffusion Architecture for World and Action Modeling](https://arxiv.org/abs/2607.23909) | 2026-07-27 | 核心 | 观察中 | **37** (2/2/1/3) | 未找到仓库 (2026-10-22) | Bagel Labs | [📝](../digests/migration-2026-10-22.md) |

## <a id="resources"></a>数据集 / 基准使用关系

只登记论文正文或实验设置中明确写出的关系；在某基准上评测 ≠ 用其 demos 训练。

### <a id="resource-open-x-embodiment"></a>Open X-Embodiment (RT-X)

- 预训练 · [CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators](https://arxiv.org/abs/2608.27406) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [What Matters for Latent Actions in Robot Learning](https://arxiv.org/abs/2608.19613) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Dream2Reward: Transition-Alignment Reward Models from Positive Demonstrations for Robotic Manipulation](https://arxiv.org/abs/2608.18787) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance](https://arxiv.org/abs/2608.09853) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [World Value Models for Robotic Manipulation](https://arxiv.org/abs/2606.24742) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Geometric Action Model for Robot Policy Learning](https://arxiv.org/abs/2606.17046) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [LARA: Latent Action Representation Alignment for Vision-Language-Action Models](https://arxiv.org/abs/2606.07100) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Reinforcing VLAs in Task-Agnostic World Models](https://arxiv.org/abs/2605.12334) · 2026-05 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization](https://arxiv.org/abs/2601.12993) · 2026-01 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734) · 2025-03 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) · 2024-06 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-droid"></a>DROID

- 预训练 · [VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models](https://arxiv.org/abs/2610.21306) · 2026-10 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators](https://arxiv.org/abs/2608.27406) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Hydra-0: Action Flow for Generalist World Modeling and Control](https://arxiv.org/abs/2608.18077) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation](https://arxiv.org/abs/2608.13489) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [G0.5: One Autoregressive Stream for Robot Reasoning and Action](https://arxiv.org/abs/2608.11739) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data](https://arxiv.org/abs/2608.02580) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models](https://arxiv.org/abs/2607.26991) · 2026-07 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [Masked Visual Actions for Unified World Modeling](https://arxiv.org/abs/2607.19343) · 2026-07 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation](https://arxiv.org/abs/2606.18960) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation](https://arxiv.org/abs/2606.17030) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Kairos: A Regret-Aware Native World-Action Model Stack for Physical AI](https://arxiv.org/abs/2606.16533) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [$\texttt{WEAVER}$, Better, Faster, Longer: An Effective World Model for Robotic Manipulation](https://arxiv.org/abs/2606.13672) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding](https://arxiv.org/abs/2606.06155) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics](https://arxiv.org/abs/2606.04463) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Qwen-VLA: Alibaba's Embodied Foundation Model](https://arxiv.org/abs/2605.30280) · 2026-05 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [H2R-Grounder: A Paired-Data-Free Paradigm for Translating Human Interaction Videos into Physically Grounded Robot Videos](https://arxiv.org/abs/2512.09406) · 2025-12 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734) · 2025-03 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) · 2024-06 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-bridgedata-v2"></a>BridgeData V2

- 微调/后训练 · [PhysBrain 1.5: From Vision-Language Models to Physical Foundation Models](https://arxiv.org/abs/2609.14973) · 2026-09 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators](https://arxiv.org/abs/2608.27406) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [G0.5: One Autoregressive Stream for Robot Reasoning and Action](https://arxiv.org/abs/2608.11739) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [Lost in Reconstruction: Aligning Action Representations with Language in Vision-Language-Action Models](https://arxiv.org/abs/2608.10484) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [World Tokens: Enhancing Embodied Policies with Training-Time World Modeling](https://arxiv.org/abs/2608.09730) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models](https://arxiv.org/abs/2607.26991) · 2026-07 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [DriftWorld: Fast World Modeling through Drifting](https://arxiv.org/abs/2607.15065) · 2026-07 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [DriftWorld: Fast World Modeling through Drifting](https://arxiv.org/abs/2607.15065) · 2026-07 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation](https://arxiv.org/abs/2606.17030) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Qwen-VLA: Alibaba's Embodied Foundation Model](https://arxiv.org/abs/2605.30280) · 2026-05 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734) · 2025-03 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Cosmos World Foundation Model Platform for Physical AI](https://arxiv.org/abs/2501.03575) · 2025-01 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-agibot-world"></a>AgiBot World

- 预训练 · [Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](https://arxiv.org/abs/2610.26855) · 2026-10 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](https://arxiv.org/abs/2610.26855) · 2026-10 · [报告](../digests/daily/2026-10-22.md)
- 预训练 · [Long-WAM: Scaling the Context of World-Action Models](https://arxiv.org/abs/2610.10528) · 2026-10 · [报告](../digests/daily/2026-10-22.md)
- 微调/后训练 · [PhysBrain 1.5: From Vision-Language Models to Physical Foundation Models](https://arxiv.org/abs/2609.14973) · 2026-09 · [报告](../digests/daily/2026-10-22.md)
- 预训练 · [WALL-SS: Scaling Long-horizon World Models via Next-Scale Autoregression](https://arxiv.org/abs/2608.26239) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [GigaBrain-0.7: Scaling Embodied Foundation Models to Emergent Capabilities with a Three-System Architecture](https://arxiv.org/abs/2608.15875) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation](https://arxiv.org/abs/2608.13489) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Flex-$\pi$: A Multi-Stream World-Action Model with Compute Flexibility](https://arxiv.org/abs/2608.10860) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance](https://arxiv.org/abs/2608.09853) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data](https://arxiv.org/abs/2608.02580) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [RynnWorld-4D: 4D Embodied World Models for Robotic Manipulation](https://arxiv.org/abs/2607.06559) · 2026-07 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [HumanScale: Egocentric Human Video Can Outperform Real-Robot Data for Embodied Pretraining](https://arxiv.org/abs/2606.20521) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation](https://arxiv.org/abs/2606.17030) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Kairos: A Regret-Aware Native World-Action Model Stack for Physical AI](https://arxiv.org/abs/2606.16533) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics](https://arxiv.org/abs/2606.04463) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Qwen-VLA: Alibaba's Embodied Foundation Model](https://arxiv.org/abs/2605.30280) · 2026-05 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation](https://arxiv.org/abs/2604.07993) · 2026-04 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization](https://arxiv.org/abs/2601.12993) · 2026-01 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734) · 2025-03 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-ego4d"></a>Ego4D

- 预训练 · [PhysBrain 1.5: From Vision-Language Models to Physical Foundation Models](https://arxiv.org/abs/2609.14973) · 2026-09 · [报告](../digests/daily/2026-10-22.md)
- 预训练 · [DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation](https://arxiv.org/abs/2608.13489) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation](https://arxiv.org/abs/2606.17030) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734) · 2025-03 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-epic-kitchens-100"></a>EPIC-KITCHENS-100

- 预训练 · [Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation](https://arxiv.org/abs/2606.17030) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics](https://arxiv.org/abs/2606.04463) · 2026-06 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-hoi4d"></a>HOI4D

- 评测 · [EgoXperience: Learning World-Grounded Egocentric Representations from Human Experience](https://arxiv.org/abs/2610.26625) · 2026-10 · [报告](../digests/daily/2026-10-22.md)
- 预训练 · [Towards a General Humanoid Loco-Manipulation Model via Egocentric Whole-Body Human Data Pretraining](https://arxiv.org/abs/2610.00438) · 2026-09 · [报告](../digests/daily/2026-10-22.md)
- 预训练 · [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734) · 2025-03 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-amass"></a>AMASS

- 评测 · [GigaBrain-WBC-0.5: A Behavior World Model for Robust Whole-Body Control with Environment Interaction](https://arxiv.org/abs/2608.18234) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [HumanCLAW: Can Vision-Language Models Act Through a Body?](https://arxiv.org/abs/2607.27180) · 2026-07 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [TAGA: Terrain-aware Active Gaze Learning for Generalizable Agile Humanoid Locomotion](https://arxiv.org/abs/2606.05880) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [CoRe-MoE: Contrastive Reweighted Mixture of Experts for Multi-Terrain Humanoid Locomotion with Gait Adaptation](https://arxiv.org/abs/2606.04718) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking](https://arxiv.org/abs/2606.03985) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Imagine2Real: Towards Zero-shot Humanoid-Object Interaction via Video Generative Priors](https://arxiv.org/abs/2605.22272) · 2026-05 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-robocasa-gen"></a>RoboCasa-Gen

- 预训练 · [Geometric Action Model for Robot Policy Learning](https://arxiv.org/abs/2606.17046) · 2026-06 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-physxverse"></a>PhysXVerse

- 提出 · [PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects](https://arxiv.org/abs/2605.21572) · 2026-05 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-ego2robot-data"></a>Ego2Robot

- 提出 · [Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data](https://arxiv.org/abs/2608.02580) · 2026-08 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-egox-data-6m"></a>EgoX-Data-6M

- 提出 · [EgoXperience: Learning World-Grounded Egocentric Representations from Human Experience](https://arxiv.org/abs/2610.26625) · 2026-10 · [报告](../digests/daily/2026-10-22.md)

### <a id="resource-calvin"></a>CALVIN

- 评测 · [GreenWAM: A World Foundation Model for Robotics](https://arxiv.org/abs/2610.18774) · 2026-10 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](https://arxiv.org/abs/2609.01281) · 2026-09 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation](https://arxiv.org/abs/2608.09771) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation](https://arxiv.org/abs/2608.09771) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding](https://arxiv.org/abs/2606.06155) · 2026-06 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-meta-world"></a>Meta-World

- 评测 · [EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](https://arxiv.org/abs/2609.01281) · 2026-09 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-libero"></a>LIBERO

- 评测 · [Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](https://arxiv.org/abs/2610.26855) · 2026-10 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [Has GPT-6-Astra Achieved Embodied Intelligence?](https://arxiv.org/abs/2610.22471) · 2026-10 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models](https://arxiv.org/abs/2610.21306) · 2026-10 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [GreenWAM: A World Foundation Model for Robotics](https://arxiv.org/abs/2610.18774) · 2026-10 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [Long-WAM: Scaling the Context of World-Action Models](https://arxiv.org/abs/2610.10528) · 2026-10 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [MotorMind: Scaffolding General Vision Language Models for Zero-Shot Robot Manipulation](https://arxiv.org/abs/2609.38078) · 2026-09 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [Self-Evolving Coding Agents: From Digital Programs to Physical-World Intelligence](https://arxiv.org/abs/2609.35432) · 2026-09 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [Grounded Action Model: 3D Grounding as a Foundation for Robotics](https://arxiv.org/abs/2609.23863) · 2026-09 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [Breaking the Vision-Action Shortcut: Latent Interface Training for Generalizable Robotics Foundation Models](https://arxiv.org/abs/2609.12641) · 2026-09 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining](https://arxiv.org/abs/2609.07398) · 2026-09 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [FlashVLA: Streaming Action Decoding for Fast and Asynchronous VLA Inference](https://arxiv.org/abs/2608.27384) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration](https://arxiv.org/abs/2608.21031) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [What Matters for Latent Actions in Robot Learning](https://arxiv.org/abs/2608.19613) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Dream2Reward: Transition-Alignment Reward Models from Positive Demonstrations for Robotic Manipulation](https://arxiv.org/abs/2608.18787) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [LIBERO-VIFO: Benchmarking the Capability and Safety of Visual Cue Following in Vision-Language-Action Models](https://arxiv.org/abs/2608.17600) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [SparkVLA: Stop-Aware Hierarchical VLA with Adaptive Action Chunking for Long-Horizon Manipulation](https://arxiv.org/abs/2608.16172) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Temporal GRPO: Beyond Trajectory-Level Credit in Vision-Language-Action Reinforcement Learning](https://arxiv.org/abs/2608.13026) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Keep the Future, Drop the Rollout: RIFT for World Action Models](https://arxiv.org/abs/2608.11521) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models](https://arxiv.org/abs/2608.11671) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [G0.5: One Autoregressive Stream for Robot Reasoning and Action](https://arxiv.org/abs/2608.11739) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Hidden in Plain Sight: Diffusion-Based Unrestricted Robotic Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2608.10393) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Neural Introspection Gating for Adaptive KV-Cache Reuse in Vision-Language-Action Models](https://arxiv.org/abs/2608.10824) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Flex-$\pi$: A Multi-Stream World-Action Model with Compute Flexibility](https://arxiv.org/abs/2608.10860) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [World Tokens: Enhancing Embodied Policies with Training-Time World Modeling](https://arxiv.org/abs/2608.09730) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [World Tokens: Enhancing Embodied Policies with Training-Time World Modeling](https://arxiv.org/abs/2608.09730) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation](https://arxiv.org/abs/2608.09771) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation](https://arxiv.org/abs/2608.09771) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [AtlasVLA: Persistent World-Ego State Modeling for Vision-Language-Action Models](https://arxiv.org/abs/2608.06729) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for Cross-Embodiment Manipulation](https://arxiv.org/abs/2608.06374) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for Cross-Embodiment Manipulation](https://arxiv.org/abs/2608.06374) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [World-to-Wrist: Task-Conditioned Future Wrist Modeling for Fine-Grained Robot Manipulation](https://arxiv.org/abs/2608.05369) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [World-to-Wrist: Task-Conditioned Future Wrist Modeling for Fine-Grained Robot Manipulation](https://arxiv.org/abs/2608.05369) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space](https://arxiv.org/abs/2608.01397) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space](https://arxiv.org/abs/2608.01397) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM](https://arxiv.org/abs/2607.27205) · 2026-07 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM](https://arxiv.org/abs/2607.27205) · 2026-07 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [WorldDiT: A Unified Diffusion Architecture for World and Action Modeling](https://arxiv.org/abs/2607.23909) · 2026-07 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [WorldDiT: A Unified Diffusion Architecture for World and Action Modeling](https://arxiv.org/abs/2607.23909) · 2026-07 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents](https://arxiv.org/abs/2606.23085) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [WAM-RL: World-Action Model Reinforcement Learning with Reconstruction Rewards and Online Video SFT](https://arxiv.org/abs/2606.17906) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [Geometric Action Model for Robot Policy Learning](https://arxiv.org/abs/2606.17046) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Geometric Action Model for Robot Policy Learning](https://arxiv.org/abs/2606.17046) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [Targeting World Models to Compromise Robot Learning Pipelines](https://arxiv.org/abs/2606.09499) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [ActionMap: Robot Policy Learning via Voxel Action Heatmap](https://arxiv.org/abs/2606.06904) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Dreaming when Necessary: Advancing World Action Models with Adaptive Multi-Modal Reasoning](https://arxiv.org/abs/2606.07089) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [LARA: Latent Action Representation Alignment for Vision-Language-Action Models](https://arxiv.org/abs/2606.07100) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis](https://arxiv.org/abs/2606.05979) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding](https://arxiv.org/abs/2606.06155) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies](https://arxiv.org/abs/2606.06491) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training](https://arxiv.org/abs/2606.04436) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training](https://arxiv.org/abs/2606.04708) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [GeoSem-WAM: Geometry- and Semantic-Aware World Action Models](https://arxiv.org/abs/2606.03188) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [GeoAlign: Beyond Semantics with State-Guided Spatial Alignment in VLA Models](https://arxiv.org/abs/2606.03240) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Affordance2Action: Task-Conditioned Scene-level Affordance Grounding for Real-Time Manipulation](https://arxiv.org/abs/2606.04172) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Hide-and-Seek in Trajectories: Discovering Failure Signals for VLA Runtime Monitoring](https://arxiv.org/abs/2605.30834) · 2026-05 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Qwen-VLA: Alibaba's Embodied Foundation Model](https://arxiv.org/abs/2605.30280) · 2026-05 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [IntentVLA: Short-Horizon Intent Modeling for Aliased Robot Manipulation](https://arxiv.org/abs/2605.14712) · 2026-05 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Reinforcing VLAs in Task-Agnostic World Models](https://arxiv.org/abs/2605.12334) · 2026-05 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Reinforcing VLAs in Task-Agnostic World Models](https://arxiv.org/abs/2605.12334) · 2026-05 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization](https://arxiv.org/abs/2601.12993) · 2026-01 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246) · 2024-06 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-rlbench"></a>RLBench

- 评测 · [AtlasVLA: Persistent World-Ego State Modeling for Vision-Language-Action Models](https://arxiv.org/abs/2608.06729) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 微调/后训练 · [BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action Framework for 3D Manipulation](https://arxiv.org/abs/2608.05042) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action Framework for 3D Manipulation](https://arxiv.org/abs/2608.05042) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [WAM-RL: World-Action Model Reinforcement Learning with Reconstruction Rewards and Online Video SFT](https://arxiv.org/abs/2606.17906) · 2026-06 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-aliasbench"></a>AliasBench

- 提出 · [IntentVLA: Short-Horizon Intent Modeling for Aliased Robot Manipulation](https://arxiv.org/abs/2605.14712) · 2026-05 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-simplerenv"></a>SimplerEnv

- 评测 · [G0.5: One Autoregressive Stream for Robot Reasoning and Action](https://arxiv.org/abs/2608.11739) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Lost in Reconstruction: Aligning Action Representations with Language in Vision-Language-Action Models](https://arxiv.org/abs/2608.10484) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [World Tokens: Enhancing Embodied Policies with Training-Time World Modeling](https://arxiv.org/abs/2608.09730) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models](https://arxiv.org/abs/2607.26991) · 2026-07 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Does VLA Even Know the Basics? Measuring Commonsense and World Knowledge Retention in Vision-Language-Action Models](https://arxiv.org/abs/2606.19297) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [LARA: Latent Action Representation Alignment for Vision-Language-Action Models](https://arxiv.org/abs/2606.07100) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training](https://arxiv.org/abs/2606.04436) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [TTT-VLA: Test-Time Latent Prompt Optimization for Vision-Language-Action Models](https://arxiv.org/abs/2606.03127) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [GeoAlign: Beyond Semantics with State-Guided Spatial Alignment in VLA Models](https://arxiv.org/abs/2606.03240) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Qwen-VLA: Alibaba's Embodied Foundation Model](https://arxiv.org/abs/2605.30280) · 2026-05 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [ElegantVLA: Learning When to Think for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2605.29438) · 2026-05 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action](https://arxiv.org/abs/2605.22283) · 2026-05 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [IntentVLA: Short-Horizon Intent Modeling for Aliased Robot Manipulation](https://arxiv.org/abs/2605.14712) · 2026-05 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-physx-bench"></a>PhysX-Bench

- 提出 · [PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects](https://arxiv.org/abs/2605.21572) · 2026-05 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-behavior-1k"></a>BEHAVIOR-1K

- 评测 · [Has GPT-6-Astra Achieved Embodied Intelligence?](https://arxiv.org/abs/2610.22471) · 2026-10 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [G0.5: One Autoregressive Stream for Robot Reasoning and Action](https://arxiv.org/abs/2608.11739) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Masked Visual Actions for Unified World Modeling](https://arxiv.org/abs/2607.19343) · 2026-07 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents](https://arxiv.org/abs/2606.23085) · 2026-06 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-robocasa-bench"></a>RoboCasa-Bench

- 评测 · [RoboCasa-Shift: Stage-Aware Robustness Evaluation of Vision-Language-Action Policies in Long-Horizon Household Manipulation](https://arxiv.org/abs/2610.27861) · 2026-10 · [报告](../digests/daily/2026-10-23.md)
- 评测 · [Long-WAM: Scaling the Context of World-Action Models](https://arxiv.org/abs/2610.10528) · 2026-10 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601) · 2026-09 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining](https://arxiv.org/abs/2609.07398) · 2026-09 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [EATR-Stereo: Embodiment-Aware Routing of Paired Stereo Evidence for Humanoid Vision-Language-Action Control](https://arxiv.org/abs/2608.17453) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Zetta $\zeta$: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence](https://arxiv.org/abs/2608.16590) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Masked Visual Actions for Unified World Modeling](https://arxiv.org/abs/2607.19343) · 2026-07 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories](https://arxiv.org/abs/2607.15330) · 2026-07 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Geometric Action Model for Robot Policy Learning](https://arxiv.org/abs/2606.17046) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [$\mu_0$: A Scalable 3D Interaction-Trace World Model](https://arxiv.org/abs/2606.13769) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding](https://arxiv.org/abs/2606.06155) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization](https://arxiv.org/abs/2601.12993) · 2026-01 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734) · 2025-03 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-robotwin-2"></a>RoboTwin 2.0

- 评测 · [Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](https://arxiv.org/abs/2610.26855) · 2026-10 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [VLA-$Δ$: Learning Physical State Transition for Vision-Language-Action Models](https://arxiv.org/abs/2610.21306) · 2026-10 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [GreenWAM: A World Foundation Model for Robotics](https://arxiv.org/abs/2610.18774) · 2026-10 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [Long-WAM: Scaling the Context of World-Action Models](https://arxiv.org/abs/2610.10528) · 2026-10 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601) · 2026-09 · [报告](../digests/daily/2026-10-22.md)
- 微调/后训练 · [Grounded Action Model: 3D Grounding as a Foundation for Robotics](https://arxiv.org/abs/2609.23863) · 2026-09 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [Grounded Action Model: 3D Grounding as a Foundation for Robotics](https://arxiv.org/abs/2609.23863) · 2026-09 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining](https://arxiv.org/abs/2609.07398) · 2026-09 · [报告](../digests/daily/2026-10-22.md)
- 评测 · [FlashVLA: Streaming Action Decoding for Fast and Asynchronous VLA Inference](https://arxiv.org/abs/2608.27384) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [GeoSem-WAM: Geometry- and Semantic-Aware World Action Models](https://arxiv.org/abs/2606.03188) · 2026-06 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-robotwin"></a>RoboTwin 2.0

- 评测 · [Flex-$\pi$: A Multi-Stream World-Action Model with Compute Flexibility](https://arxiv.org/abs/2608.10860) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [XPolicyLab: A Unified Standard and Open Ecosystem for Robot Policy Evaluation and Deployment](https://arxiv.org/abs/2608.09892) · 2026-08 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-humanoidvln"></a>HumanoidVLN

- 提出 · [HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments](https://arxiv.org/abs/2608.12860) · 2026-08 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-h2r-bench"></a>H2R-Bench

- 提出 · [H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models](https://arxiv.org/abs/2608.13049) · 2026-08 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-egox-bench"></a>EgoX-Bench

- 提出 · [EgoXperience: Learning World-Grounded Egocentric Representations from Human Experience](https://arxiv.org/abs/2610.26625) · 2026-10 · [报告](../digests/daily/2026-10-22.md)

### <a id="resource-isaac-lab"></a>Isaac Lab

- 评测 · [Tactile Sim2Real without Tactile Simulation via Bottlenecked Latent Reconstruction](https://arxiv.org/abs/2608.15897) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [Mana: Dexterous Manipulation of Articulated Tools](https://arxiv.org/abs/2606.13677) · 2026-06 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [PhysiFlow: Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent Flow Matching and Robust Tracking](https://arxiv.org/abs/2603.05410) · 2026-03 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-isaac-sim"></a>Isaac Sim

- 评测 · [HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments](https://arxiv.org/abs/2608.12860) · 2026-08 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [NavVerse: Benchmarking Indoor-to-Outdoor Embodied Navigation in Continuous Robot Simulation](https://arxiv.org/abs/2607.19695) · 2026-07 · [报告](../digests/migration-2026-10-22.md)
- 评测 · [LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction](https://arxiv.org/abs/2506.13751) · 2025-06 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-genesis"></a>Genesis

- 评测 · [EaDex: A Cross-Embodiment Dexterous Manipulation Framework from Low-Cost Demonstrations](https://arxiv.org/abs/2606.03268) · 2026-06 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-habitat-3-0"></a>Habitat 3.0

- 评测 · [ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation](https://arxiv.org/abs/2610.25690) · 2026-10 · [报告](../digests/daily/2026-10-22.md)

### <a id="resource-robocasa"></a>RoboCasa

- 微调/后训练 · [Masked Visual Actions for Unified World Modeling](https://arxiv.org/abs/2607.19343) · 2026-07 · [报告](../digests/migration-2026-10-22.md)
- 预训练 · [GR00T N1: An Open Foundation Model for Generalist Humanoid Robots](https://arxiv.org/abs/2503.14734) · 2025-03 · [报告](../digests/migration-2026-10-22.md)

### <a id="resource-maniskill-3"></a>ManiSkill 3

- 评测 · [KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding](https://arxiv.org/abs/2607.19876) · 2026-07 · [报告](../digests/migration-2026-10-22.md)

