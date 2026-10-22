# 存量整理报告：2026-10-22

## 本期说明

- **范围：** v2 流程上线前已收录的全部论文，按 [METHODOLOGY](../docs/METHODOLOGY.md) 重新做两层筛选与四维评分。
- **结果：** 保留 213 篇（🔥 重点阅读 25、👀 值得关注 60、观察中 124、暂不评级 4）；移出 13 篇；调整类别 116 篇。
- **变化说明：** 旧版按日期把 2026-04 之后的论文一律标 🔥，现改为由评分推导；🔥/👀 只代表跟进优先级。开放状态由仓库实际内容探测并人工/agent 复核。

## 核心工作

### 1. OpenVLA: An Open-Source Vision-Language-Action Model — 🔥 重点阅读

- **时间：** 2024-06-13（[arXiv](https://arxiv.org/abs/2406.09246)）
- **评分：** C5（首个性能具竞争力的完全开源 VLA 及训练代码库，奠定社区 VLA 基线与微调范式。） / E5（两种真机平台多维泛化评测、对比闭源 RT-2-X 等强基线，含微调、LoRA、量化、设计选择消融与 LIBERO 仿真。） / O5（MIT 代码、HF 权重（含 LIBERO 微调版）公开，训练数据为公开的 Open X-Embodiment，复现说明完整。） / T5（Stanford、Berkeley、TRI、Google DeepMind 等团队，在机器人学习方向有大量标志性成果。） = **100/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** Stanford University；UC Berkeley；Toyota Research Institute；Google DeepMind；Physical Intelligence；MIT
- **分类：** `vla` · 核心 · model
- **核心内容：** VLA 当时多为闭源模型，且缺少在新机器人与新任务上高效微调的实践，限制了社区采用。OpenVLA 以 Prismatic-7B VLM（DINOv2 与 SigLIP 融合视觉编码器 + Llama 2）为骨干，把每维连续动作离散为 256 个 token，在经筛选与配比的 Open X-Embodiment 约 97 万条真机示范上训练。作者在 WidowX（BridgeData V2 设置，17 项任务 170 次）与 Google 机器人（12 项任务 60 次）上做 A/B 对比，报告 OpenVLA 整体成功率比 RT-2-X 高 16.5 个百分点，明显优于 RT-1-X 与 Octo，但在语义泛化上 RT-2-X 仍更强；在 Franka 上用 10–150 条示范微调时，多物体语言任务上优于从零训练的 Diffusion Policy（约高 20.4%）；LoRA 仅训练 1.4% 参数即接近全参微调，4-bit 量化成功率与 bf16 相当。模型与代码全部开源，成为后续 VLA 常用基线。局限包括单图像输入、推理约 6Hz、对高频灵巧控制支持不足，以及 DROID 数据拟合不佳等作者自述问题。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/openvla/openvla)；权重 open，数据 open，许可 MIT。训练数据为公开的 Open X-Embodiment 子集与配比；权重在 HF openvla 组织下。
- **数据/基准关系：** openvla（提出）、open-x-embodiment（预训练）、droid（预训练）、libero（评测）

### 2. Diffusion Policy: Visuomotor Policy Learning via Action Diffusion — 🔥 重点阅读

- **时间：** 2023-03-07（[arXiv](https://arxiv.org/abs/2303.04137)）
- **评分：** C5（把扩散模型引入动作生成的奠基性工作，确立了动作分块 + 扩散的主流策略范式。） / E5（4 个基准 15 项任务、多种子与强基线对比，配合大量消融与多项真机实验（含双臂与液体操作）。） / O5（MIT 代码、实验数据与训练配置公开，作者网站提供实验检查点，复现说明完整。） / T5（Columbia/Stanford 宋舒然团队与 TRI、MIT Tedrake 团队在机器人操作学习方向领先。） = **100/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** Columbia University；Toyota Research Institute；MIT；Stanford University
- **分类：** `rl-il` · 核心 · method
- **核心内容：** 模仿学习中的动作分布常常多模态、具有时序相关性且要求高精度，显式回归会平均化多模态，隐式策略（IBC）训练又不稳定。Diffusion Policy 把视觉运动策略建模为条件 DDPM：以观测为条件，对未来一段动作序列逐步去噪，执行其中部分动作后再滚动重规划；提供 1D 时序 CNN（FiLM 条件）与时序扩散 Transformer 两种骨干，配合端到端训练的 ResNet-18 视觉编码器、平方余弦噪声调度和 DDIM 加速推理（真机约 0.1 秒延迟）。在 Robomimic、Push-T、Block Pushing、Franka Kitchen 等 4 个基准 15 项任务上（3 个种子、多次初始化），作者报告其在所有任务上优于 LSTM-GMM、IBC、BET，平均成功率提升 46.9%；真机 Push-T、马克杯翻转、倒酱与抹酱及双臂任务也取得较高成功率，分析了多模态表达、位置控制协同、动作序列预测和训练稳定性。该方法已成为视觉运动策略的默认基线；局限是推理比单步策略慢，且依赖较多高质量示范。
- **发表状态（核验：2026-10-22）：** RSS 2023
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/real-stanford/diffusion_policy)；权重 open，数据 open，许可 MIT。项目页提供训练数据与实验检查点下载。
- **数据/基准关系：** diffusion-policy（提出）

### 3. GR00T N1: An Open Foundation Model for Generalist Humanoid Robots — 🔥 重点阅读

- **时间：** 2025-03-18（[arXiv](https://arxiv.org/abs/2503.14734)）
- **评分：** C5（开放权重的人形通用基础模型与异构数据金字塔训练方案，已成为人形 VLA 的常用起点。） / E4（三套仿真基准 + GR-1 真机 + 数据量与神经轨迹消融，较完整；真机基线较少且限于桌面操作。） / O5（Apache-2.0 代码、HF 权重与部分仿真训练数据公开，并给出复现仿真结果的说明。） / T5（NVIDIA GEAR 团队在机器人基础模型、仿真与数据生成方向有多项标志性成果。） = **95/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** NVIDIA
- **分类：** `vla` · 核心 · model
- **核心内容：** 人形机器人缺乏可用于大规模预训练的数据，不同本体数据又形成「数据孤岛」。GR00T N1 为此提出双系统 VLA：以 Eagle-2 VLM 作为 System 2 理解视觉与语言，以 DiT flow-matching 动作模块作为 System 1 生成高频动作，二者端到端联合训练，并用逐本体的状态/动作编码器支持从单臂到双手灵巧人形的多种本体。训练数据组织为金字塔：底层为人类视频（以 VQ-VAE 潜动作为标签），中层为仿真与神经生成轨迹，顶层为 GR-1 遥操作、Open X-Embodiment 与 AgiBot-Alpha 真机数据。作者报告在 RoboCasa、DexMimicGen 跨本体套件和 GR-1 桌面任务三套仿真基准上（每任务 100 条示范）优于 Diffusion Policy 等基线，在 GR-1 真机双手操作任务上少量数据即可取得较高成功率，神经轨迹协同训练在低数据量下带来提升。该工作提供了开放权重的人形基础模型和可复现的仿真评测；但真机对照主要是 Diffusion Policy，评测集中于桌面操作，未涉及行走等全身控制。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/NVIDIA/Isaac-GR00T)；权重 open，数据 partial，许可 Apache-2.0。权重在 HF nvidia 组织下（后续版本已到 N1.7）；论文给出仿真数据集 nvidia/PhysicalAI-Robotics-GR00T-X-Embodiment-Sim，真机自采数据未公开。
- **数据/基准关系：** open-x-embodiment（预训练）、droid（预训练）、bridgedata-v2（预训练）、agibot-world（预训练）、ego4d（预训练）、hoi4d（预训练）、robocasa（预训练）、robocasa-bench（评测）

### 4. Cosmos World Foundation Model Platform for Physical AI — 🔥 重点阅读

- **时间：** 2025-01-07（[arXiv](https://arxiv.org/abs/2501.03575)）
- **评分：** C5（首个系统开放的物理 AI 世界基础模型平台，覆盖数据、tokenizer、预训练与后训练全链路，已成为后续工作的基础资源。） / E4（tokenizer 与生成模型有多数据集定量对比和后训练示例，但缺少把 WFM 用于下游策略学习的实证（作者自述）。） / O4（代码与权重公开（论文指向 cosmos-predict1），训练数据含专有视频未公开。） / T5（NVIDIA 在仿真、生成模型与机器人基础设施方向有大量标志性成果。） = **89/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** NVIDIA
- **分类：** `world-model` · 核心 · model
- **核心内容：** 物理 AI 的数据难以安全、规模化地采集，作者提出以「世界基础模型」(WFM) 作为物理世界的数字孪生，采用先预训练通用模型、再针对具体场景后训练的范式。Cosmos 平台包括：基于 Ray 的视频筛选管线，从约 2000 万小时原始视频中切分、过滤、VLM 标注并去重，得到约 1 亿个 2–60 秒片段；一组在小波空间工作、时间因果的连续与离散视频 tokenizer；基于扩散和自回归 Transformer 的预训练 WFM；以及相机控制、机器人操作、自动驾驶等后训练示例和安全护栏。作者报告其 tokenizer 在 DAVIS 与自建 TokenBench（含 BridgeData V2、Ego-Exo4D、BDD100K 等视频）上的重建质量优于 CogVideoX、Omni-Tokenizer 等对照，并开放代码与权重。该平台为机器人策略评估、合成数据和规划等用途提供了可微调的基础模型；但作者明确说明，论文未给出把 WFM 用于策略评估、策略训练或 MPC 的实证结果，训练数据含专有视频且未公开，下游控制价值仍需后续工作验证。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/nvidia-cosmos/cosmos-predict1)；权重 open，数据 none，许可 Apache-2.0。探测命中的 NVIDIA/Cosmos 为索引仓库（无代码）；论文摘要指向的 cosmos-predict1 含实质代码，代码 Apache-2.0，权重采用 NVIDIA Open Model License。
- **数据/基准关系：** bridgedata-v2（评测）

### 5. Flex-$\pi$: A Multi-Stream World-Action Model with Compute Flexibility — 🔥 重点阅读

- **时间：** 2026-08-11（[arXiv](https://arxiv.org/abs/2608.10860)）
- **评分：** C4（发现视频 VAE 可编码点图，并以此构建多流、算力可调的 WAM，对世界-动作模型子方向有明确的方法增量） / E5（五个难度较高的真机双臂任务，含 OOD 与半量数据测试，另有 RoboTwin、LIBERO、LIBERO-Plus 大规模对比，以及输入/输出流和跨模态强制的消融） / O4（仓库（MIT）含训练、评测、真机服务代码，HF 已发布 RoboTwin 与 LIBERO 权重；大规模预训练权重尚未发布） / T5（华盛顿大学 Dieter Fox 组与 AI2，在机器人学习领域是公认的领先团队） = **88/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** University of Washington；Allen Institute for AI
- **分类：** `world-model` · 核心 · model
- **核心内容：** 现有世界-动作模型（WAM）几乎都只预测为像素重建训练的 RGB 隐变量，缺少操作所需的 3D 几何和物体语义监督。作者发现，冻结的视频生成 VAE 几乎能无损地编码 3D 点图，据此提出 6B 参数的 Flex-π：由 Depth Anything 3 生成的点图和 DINOv3 特征与 RGB 一起投影到共享隐空间，在 Mixture-of-Transformers 中与动作联合做 flow matching 去噪；逐流 dropout 加跨模态强制，使同一 checkpoint 可以在任意输入/输出流组合下运行，不需要新传感器，也可以不增加推理延迟。模型在 AgiBot World 上预训练后按任务微调。作者报告：在 YAM 双臂真机的五个任务（含毫米级插装的自修夹爪、软包拉链）上，纯动作模式和全联合模式都优于 π0.5、Fast-WAM 和 ManiFlow，任务越难优势越大；在未见物体、杂乱干扰和半量数据条件下仍保持领先；RoboTwin 50 任务平均成功率为 94.6%，高于所列 VLA 与 WAM 基线；消融显示 DINO 和点图流都带来提升。这提示把几何与语义引入 WAM 的联合预测可以提高示教效率和泛化，但收敛较慢，全联合模式仍比同规模 VLA 慢，在 LIBERO-Plus 上仍落后于数据更多的强 VLM 方法。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/geyan21/flex-pi)；权重 partial，数据 none，许可 MIT。探测未发现仓库，项目页链接到 geyan21/flex-pi；HF 已有 flexpi-robotwin、flexpi-libero 权重，README 写明大规模预训练 checkpoint 计划后续发布
- **数据/基准关系：** agibot-world（预训练）、robotwin（评测）、libero（评测）
- **待核验事项：** 在 AgiBot/YAM/DROID 上大规模预训练的 checkpoint 何时发布

### 6. RDT-1B: A Diffusion Foundation Model for Bimanual Manipulation — 🔥 重点阅读

- **时间：** 2024-10-10（[arXiv](https://arxiv.org/abs/2410.07864)）
- **评分：** C4（早期大规模扩散式双臂基础模型与统一动作空间设计，对双臂 VLA 子方向影响明显。） / E4（真机多维度泛化任务、对比 3 个强基线并有模型/数据/扩散的消融；仅单一平台、无标准仿真基准。） / O5（MIT 代码、1B 与 170M 权重及微调数据集均已公开，README 有训练与部署说明。） / T4（清华朱军团队在扩散模型与机器学习方向积累深厚，机器人方向积累相对较新。） = **86/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** Department of Computer Science & Technology, Institute for AI, BNRist Center, Tsinghua-Bosch Joint ML Center, THBI Lab, Tsinghua University
- **分类：** `vla` · 核心 · model
- **核心内容：** 双臂操作动作分布多模态、数据又稀缺，难以训练基础模型。RDT 用扩散模型表示多模态动作分布，基于 DiT 并针对机器人物理量的非线性与高频变化加入 QKNorm、RMSNorm、MLP 解码器等设计；提出物理可解释的统一动作空间，按物理含义把各机器人的本体感知与动作填入统一向量，从而在超过 100 万条轨迹的多机器人数据集合上预训练，并扩展到 1.2B 参数；再在自采的 6K+ 条多任务双臂数据上微调。在 ALOHA 双臂真机上，作者设计了未见物体、未见场景、指令跟随（如「倒三分之一」）、1/5 次示范学习和推摇杆等灵巧任务，报告 RDT 成功率显著高于 ACT、OpenVLA 和 Octo，消融显示去掉大模型、预训练数据或扩散建模都会明显下降，从零训练的 RDT 在未见物体与场景上表现差。该结果提示跨机器人预训练与统一动作空间对双臂泛化有帮助；但评测只在单一 ALOHA 平台、每项任务试验数有限，且缺少标准仿真基准对比。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/thu-ml/RoboticsDiffusionTransformer)；权重 open，数据 open，许可 MIT。HF 上有 rdt-1b、rdt-170m 与微调数据集 rdt-ft-data。

### 7. CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators — 🔥 重点阅读

- **时间：** 2026-08-27（[arXiv](https://arxiv.org/abs/2608.27406)）
- **评分：** C4（跨具身动作统一与课程训练为视频世界模型提供可复用基础，对子方向有明确影响） / E4（DROID/Bridge/OXE 多数据集对比、动作空间消融、真机规划与新具身适配，但以感知指标为主） / O5（训练与推理代码、多套检查点（MIT）均已公开，训练数据为公开数据集） / T3（普林斯顿两位作者的小团队，可核实积累有限，按默认值） = **83/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** Princeton University
- **分类：** `world-model` · 核心 · model
- **核心内容：** 为解决动作条件视频世界模型局限于单一机器人、无法利用异构人类与机器人视频的问题，作者提出 CLAP：用末端执行器位姿、语言指令和学习到的潜动作三种方式统一不同具身的动作空间，并采用课程式训练——先以潜动作在无标注视频上学物理先验，再落地到末端动作空间以便零样本部署；模型基于 U-Net 潜视频扩散，带历史条件与多视角预测，在 Open X-Embodiment 与 EgoDex 上训练。作者报告其在 DROID 上接近或超过单具身 Ctrl-World，在 OXE 混合数据上潜动作与课程版本保真度最高；绝对动作在末端条件下优于相对动作；以 CLAP 作推理时规划、在 π0.5 与 MolmoAct-2 的候选动作中选优，在 5 个 DROID 真机任务上成功率持平或提高，并能少样本适配双臂 YAM 与 G1 人形。该结果提示跨具身数据可为视频世界模型提供可迁移先验，但评测以感知指标为主，规划依赖 VLM 打分，真机试次与任务规模有限。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/omni-CLAP/clap)；权重 open，数据 n/a，许可 MIT。README 含 clap-train 与评测/部署脚本，HuggingFace omni-CLAP/CLAP 提供跨具身及 DROID/Bridge/YAM/G1 检查点；"coming soon" 仅指引用信息
- **数据/基准关系：** open-x-embodiment（预训练）、droid（评测）、bridgedata-v2（评测）

### 8. Geometric Action Model for Robot Policy Learning — 🔥 重点阅读

- **时间：** 2026-06-15（[arXiv](https://arxiv.org/abs/2606.17046)）
- **评分：** C4（将几何基础模型直接改造为世界-动作策略的结构设计新颖，对 3D 感知策略子方向有明确增量。） / E4（LIBERO、LIBERO-Plus、RoboCasa、真机与多组消融和延迟测试，基线覆盖 VLA、WAM 与几何增强 VLA。） / O4（代码 MIT 开源，HF 上有 LIBERO 后训练权重；预训练权重是否公开未确认。） / T5（KAIST Seungryong Kim、ETH Marco Hutter 与 Marc Pollefeys 均为相关方向公认领先团队。） = **83/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** KAIST AI；ETH Zurich；ETH AI Center
- **分类：** `vla` · 核心 · model
- **核心内容：** 为弥补 VLA 与视频世界-动作模型主要在 2D 表征上工作、对相机视角和环境变化泛化不足的问题，作者提出 Geometric Action Model（GAM）：把预训练几何基础模型 DA3-Giant 在中间层拆开，浅层作观测编码器，在切分处插入以语言、本体状态和历史动作为条件的块因果预测器，预测未来几何潜 token 与动作 token，再交回深层与 DPT 头同时解码未来深度和动作块；在 RoboCasa365、MimicGen 与 Open X-Embodiment 共 78.4 万条轨迹上预训练后按基准后训练。作者报告 LIBERO 上 97.6%，零样本 LIBERO-Plus 扰动评测 85.5%，相机扰动子项较次优提升 9.7 个百分点；单次前向 6.9 ms，约比 Cosmos-Policy 快 55 倍；真机四任务在换外部相机位置时明显优于 π0.5 类基线与 Spatial Forcing；消融显示预训练和切分层位置至关重要。该结果提示把几何先验贯穿整个预测通路可提升视角鲁棒性，但语言推理受冻结 T5 限制，真机每任务仅 20 次试验。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/cvlab-kaist/Geometric-Action-Model)；权重 partial，数据 n/a，许可 MIT。HF 上见 SeonghuJeon/3da-libero-gam（LIBERO 权重）。
- **数据/基准关系：** open-x-embodiment（预训练）、robocasa-gen（预训练）、libero（微调/后训练）、libero（评测）、robocasa-bench（评测）
- **待核验事项：** 预训练（78.4 万轨迹）权重是否公开

### 9. World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis — 🔥 重点阅读

- **时间：** 2026-06-04（[arXiv](https://arxiv.org/abs/2606.05979)）
- **评分：** C4（在 VLM 骨干上统一文本子任务推理与隐式世界建模、并支持从无动作视频学新任务，对 VLA/WAM 融合有明确推进。） / E4（RoboTwin、LIBERO、RMBench 多基准与强基线、多项消融、真机 OOD 与时延、视频学习实验；真机规模有限。） / O5（Apache-2.0 实质代码，多个任务权重与 LeRobot 格式数据集已在 HF 公开。） / T3（上交邓志杰组在扩散/生成模型方向有积累，具身方向成果相对新，按 3 计。） = **83/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** Shanghai Jiao Tong University (SJTU)；Shanghai Innovation Institute (SII)；Huazhong University of Science and Technology (HUST)；South China University of Technology (SCUT)；East China University of Science and Technology (ECUST)；Shanghai University (SHU)；Nanjing University of Posts and Telecommunications (NJUPT)
- **分类：** `vla` · 核心 · model
- **核心内容：** 为结合世界-动作模型（WAM）从视频学习物理动态的能力与 VLA 的语言推理能力，作者提出 WLA：以自回归 Transformer（RynnBrain-2B）为骨干预测“下一状态”，包括文本子任务意图与由 meta-query 输出的紧凑物理动态；后者由 World Expert（SANA-600M）以预测未来画面为目标监督，再与流匹配 Action Expert 共同生成动作。推理默认关闭 World Expert 以降低延迟，也可开启做“采样多个动作块—想象未来—打分选择”的测试时扩展。作者报告 WLA-0 无具身预训练，在 RoboTwin 2.0 Clean/随机化上 92.94%/90.02%，LIBERO 平均 98.6%（测试时扩展 98.9%），在记忆依赖的 RMBench 四任务平均 56.5%（明显高于 Mem-0 的 28.5%），去掉世界或子任务监督均下降；真机 Piper 双臂四任务与 π0.5、Motus 相当且动态投垃圾任务最好；在 RoboTwin 未见任务上，加入无动作标注的同/跨本体视频可把平均成功率从约 13% 提至约 29–34%。该结果提示语言意图与隐式世界建模可互补，但真机仅单平台少量任务，视频学习实验依赖仿真视频。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/SJTU-DENG-Lab/WLA)；权重 open，数据 open，许可 Apache-2.0。HF 上有 LIBERO 与 RMBench 各任务权重及 LIBERO/RoboTwin/RMBench LeRobot 数据
- **数据/基准关系：** libero（评测）

### 10. FlashVLA: Streaming Action Decoding for Fast and Asynchronous VLA Inference — 🔥 重点阅读

- **时间：** 2026-08-27（[arXiv](https://arxiv.org/abs/2608.27384)）
- **评分：** C4（把流式分块扩散引入 VLA 动作解码，同时改善延迟与异步连续性，可直接影响部署实践） / E4（LIBERO、RoboTwin 2.0、三种骨干、多类加速/异步基线、因果掩码消融与真机，但真机试次有限） / O4（实质代码 Apache-2.0 + LIBERO/RoboTwin 微调权重已在 HuggingFace 发布） / T4（刘志坚等在高效模型推理方向有多项可核实成果） = **80/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** UC San Diego；MIT
- **分类：** `vla` · 核心 · method
- **核心内容：** 为同时解决流匹配 VLA 推理延迟高与异步执行时观测过期导致动作不连续的问题，作者提出 FlashVLA：维护一个由多个处于不同噪声水平的动作块组成的流式缓冲区，用块级因果注意力让噪声更大的未来块参考更干净的块，每次前向推进全部块一步、产出一个可执行块；并把冷启动的各种缓冲配置打包进单个样本做多缓冲联合微调。基于 π0.5，作者报告 LIBERO 一步异步下平均成功率由 96.9% 升至 97.8%、每步耗时由 53.8 降到 22.1 ms，优于 VLASH 与 StreamingVLA；RoboTwin 2.0 的 50 个任务同步评测由 86.1% 升至 90.8%，长程子集提升 36.6 点；单次推理延迟低于 Realtime-VLA，并可迁移到 SmolVLA 与 LingBot-VLA。Franka 真机三个任务各 15 次，平均得分 84.4%，高于同步与 RTC。去掉块级因果掩码会使异步成功率降约 10 点。该结果提示联合解码可同时换取速度与连续性，但需额外微调、每回合有冷启动开销。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/z-lab/flashvla)；权重 open，数据 n/a，许可 Apache-2.0。HuggingFace 提供 flashvla-pi05-libero 与 flashvla-pi05-robotwin 权重；真机数据未公开
- **数据/基准关系：** libero（评测）、robotwin-2（评测）

### 11. Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation — 🔥 重点阅读

- **时间：** 2026-08-18（[arXiv](https://arxiv.org/abs/2608.17512)）
- **评分：** C4（像素到 3D 的动作表述、按需推理与两级 GRPO 组合成高效 VLN 框架，对 VLM 导航子方向有明确增量。） / E4（R2R-CE 与 RxR-CE 两个基准、强基线、分块消融、深度噪声鲁棒性和 100 次真机试验，证据较完整。） / O4（Embodied-Omni 仓库含训练（SFT 与 GRPO）、评测与部署代码，7B GRPO 权重在 HF 公开，Mulan PSL v2 许可；MultiNav-CoT 数据公开情况未确认。） / T4（浙大熊蓉、庄越挺等团队在机器人与多模态方向有可核实的强相关积累。） = **80/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** School of Software Technology, Zhejiang University；Zhejiang Humanoid Robot Innovation Center Co., Ltd.
- **分类：** `navigation` · 核心 · method
- **核心内容：** 直接用 VLM 做连续环境视觉语言导航时，原子动作或 3D 坐标回归与其 2D 预训练先验不匹配，逐步思维链拖慢推理，长程记忆又易溢出或丢失关键信息。TAMP-Nav 让 Qwen2.5-VL-7B 先选视角再输出 2D 像素，经深度投影成 3D 路点交给 SLAM 控制器；仅在关键节点触发思维链并存为高保真锚点，其余历史压缩为时空指示 token；先在 9 万条带选择性 CoT 的 MultiNav-CoT 数据上 SFT，再用叠加全局结果奖励与逐步过程奖励的两级 GRPO 对齐。作者报告在 R2R-CE / RxR-CE 未见验证集上成功率 66.2% / 65.7%，高于 DualVLN、NavFoM 等；每条轨迹平均约 9 步交互、单任务 16.58 s；RL 将成功率从 55.7% 提升到 66.2%；自动推理比稠密 CoT 少 73.7% 调用、成功率仅降 0.6 点；真机 100 次室内外试验有对比。不过动作执行依赖深度与 SLAM 控制器，CoT 标注依赖 Gemini 教师，与他法的训练数据规模并不对等。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/ZJU-OmniAI/Embodied-Omni)；权重 open，数据 unknown，许可 MulanPSL-2.0。embodied_navigator/ 子目录含 SFT 与两级 GRPO 训练、连续导航评测和 Go2 部署服务；HF 发布 Embodied-Navigator-7B-GRPO 权重；仓库许可为 Mulan PSL v2
- **待核验事项：** MultiNav-CoT 数据集是否公开

### 12. $\tau_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation — 🔥 重点阅读

- **时间：** 2026-08-17（[arXiv](https://arxiv.org/abs/2608.16885)）
- **评分：** C4（大规模真机数据训练的分层基础模型，并把世界模型引导的测试时搜索落到开放式语言子任务层，对长程 VLA 有明确增量。） / E4（多本体真机长程任务与三个强基线对比、测试时计算的开环与闭环分析及记忆消融，但每项仅 10 次试验。） / O4（仓库含训练、LIBERO 后训练与评测、高层推理与微调代码，低层/高层/世界模型权重均在 HF 开放（Apache-2.0），训练数据仅示例子集。） / T4（上海创智学院与智元团队（含 Jianlan Luo 等）在真机 VLA 与机器人学习方向有可核实的强相关积累。） = **80/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** Shanghai Innovation Institute；Agibot Finch；The Chinese University of Hong Kong
- **分类：** `vla` · 核心 · model
- **核心内容：** 分层 VLA 通常一次前向就决定下一个子任务，困难决策无法获得更多计算。τ0-VLA 的高层由提案、世界模型、价值、反思四个模型组成：带可纠错执行记忆生成子任务，置信度低时对候选子任务用图像编辑式世界模型预测完成画面、价值模型打分并束搜索，再由反思模型给出最终子任务；低层为 Qwen3.5-2B + MoT 流匹配动作专家，在 40,115 小时异构真机数据上分阶段共训练，统一 40 维状态/动作空间覆盖固定基座、移动与双臂本体。作者报告在 AgiBot G1 四项长程真机任务（各 10 次）上分层系统平均成功率 45.0%、进度 87.85%，π0.5 为 22.5%/73.05%，GR00T N1.7 与 LingBot-VLA 更低；在奶茶、整理书、打扫房间上，测试时计算将成功次数由 5/6/5 提升到 7/9/7（各 10 次），下一子任务预测准确率随计算量上升。结果支持对子任务层做测试时搜索的价值，但每项试验仅 10 次，大规模训练数据未公开。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/sii-research/tau-0-vla)；权重 open，数据 partial，许可 Apache-2.0。README 列出训练入口、LIBERO 后训练与评测、高层提案与世界模型推理/微调代码；HF 发布低层策略、LIBERO、提案模型与世界模型 LoRA 权重；数据仅含少量 AgiBot World 示例子集，README 称高层组件逐步发布
- **待核验事项：** 高层策略组件（价值模型、反思模型）是否已全部开源

### 13. RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance — 🔥 重点阅读

- **时间：** 2026-08-10（[arXiv](https://arxiv.org/abs/2608.09853)）
- **评分：** C4（用时间戳派生的时间距离替代偏好/进度监督，把通用价值模型扩展到数千小时异构数据，对机器人奖励建模子方向有明确增量） / E4（有 OOD 排序基准与多条强基线、组件消融、规模对比，并在真机在线/离线 RL、数据筛选和价值引导三类应用中验证；真机任务数较少） / O4（仓库有实质代码，HF 公开了 4B/8B 等多个权重；仓库未检出许可证文件） / T4（阿里达摩院在具身大模型（RynnBrain、RynnVLA 等）方向有可核实的连续产出） = **80/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** DAMO Academy, Alibaba Group；Hupan Lab
- **分类：** `foundation-general` · 核心 · model
- **核心内容：** 通用奖励模型正成为扩展机器人学习的瓶颈：现有方法依赖偏好对或轨迹内归一化进度这类与任务绑定的监督，难以跨本体、跨数据源复用。为此作者提出 RynnValue：以 RynnBrain 为骨干，以从当前观测到语言目标的有向时间距离（cost-to-go）为回归目标。这个标签可以直接从时间戳和重标注的完成点得到，因此能扩展到约 7000 小时、300 万条指令片段（AgiBot、OXE、EgoDex、RoboMIND 等）。为防止模型走捷径，训练中加入随机时间采样、时序打乱、价值隔离注意力和指令错配增强。作者报告：8B 模型在 RBM-EVAL-OOD 六个 OOD 数据集上平均 Kendall τ 为 0.704，高于用偏好监督训练的 Robometer（0.655）和只用进度的对照（0.292）；4B 模型为 0.679。在下游应用中，基于势函数的奖励塑形把真机在线 RL 成功率从 52.5% 提到 72.5%，离线从 63.8% 提到 82.5%；数据筛选把多任务 BC 从 35.0% 提到 42.5%；价值引导把冻结策略从 67.5% 提到 80.0%。消融显示打乱与隔离注意力都很关键。这提示时间距离可以作为可扩展的价值接口，但真机实验任务数量少（四个任务级别），与偏好监督方法的比较也只在单一基准上。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/alibaba-damo-academy/RynnValue)；权重 open，数据 unknown，许可 none-found。HF 合集 Alibaba-DAMO-Academy/rynnvalue 中有 RynnValue-4B、4B-Quantile 和 8B
- **数据/基准关系：** agibot-world（预训练）、open-x-embodiment（预训练）
- **待核验事项：** 仓库许可证（探测未找到 LICENSE）；训练数据的整理与重标注结果是否公开

### 14. TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM — 🔥 重点阅读

- **时间：** 2026-07-29（[arXiv](https://arxiv.org/abs/2607.27205)）
- **评分：** C4（以极小模型挑战 LLM 中心的 VLA 设计，并给出效率-性能权衡的强证据，对高效 VLA 子方向有影响。） / E4（LIBERO 与 RoboTwin 2.0 两个基准、大量强基线、真机 4 任务与语言/编码器/交互方式消融较完整。） / O4（实质代码（Apache-2.0）与 HF 权重已开放，训练数据为公开基准。） / T4（华中科技大学白翔团队在视觉与具身方向有可核实的强相关积累。） = **80/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** Huazhong University of Science and Technology
- **分类：** `vla` · 核心 · model
- **核心内容：** 为解决以大语言模型为中心的 V→L→A 型 VLA 计算与显存开销大、难以实时部署的问题，TurboVLA 采用直接的 V+L→A 结构：DINOv3 编码多视角图像、BERT 编码指令，经由 Grounding DINO 初始化的轻量双向视觉-语言交叉注意力交换信息，再用 ACT 式解码器输出连续动作块。作者报告在 LIBERO 上 0.2B 参数平均成功率 97.6%，RTX 4090 推理时延 31.2 ms、显存 0.9 GiB，CUDA Graph 等运行时优化后时延降至 7.42 ms；0.4B 版本在 RoboTwin 2.0 clean/randomized 平均 88.06%，与 Motus、LingBot-VLA 等大得多且有额外具身预训练的模型相当；在 AgileX Piper 真机 4 个任务上与基线在相同协议下对比。消融显示去掉语言降至 68.5%，双向交互优于单向或拼接。该结果提示执行层操作未必需要 LLM 作为感知-动作中介，但模型不具备开放指令推理和任务分解能力，作者承认面向“打扫房间”这类开放指令仍需扩展，真机任务数量也有限。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/H-EmbodVis/TurboVLA)；权重 open，数据 n/a，许可 Apache-2.0。HF 有 H-EmbodVis/TurboVLA 权重。
- **数据/基准关系：** libero（微调/后训练）、libero（评测）

### 15. Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — 🔥 重点阅读

- **时间：** 2026-07-16（[arXiv](https://arxiv.org/abs/2607.15330)）
- **评分：** C4（以 10 万小时级 UMI 数据加自动状态转移标注训练 VLA 并给出扩展规律，对数据扩展路线有明确影响。） / E4（数据/模型扩展、真机开箱泛化、少样本微调与四个仿真基准对比较完整，但扩展实验只用部分数据。） / O4（代码含后训练、推理与评测（Apache-2.0），发布 5B 权重及基准微调权重，数据与预训练代码未公开。） / T4（小米机器人团队已有前作 Xiaomi-Robotics-0 等可核实的 VLA 成果。） = **80/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** Xiaomi Robotics
- **分类：** `vla` · 核心 · model
- **核心内容：** 为突破真机遥操作数据难以扩展的瓶颈，作者提出 Xiaomi-Robotics-1：采用 Qwen3-VL 主干与 DiT 流匹配动作专家的 Mixture-of-Transformers 结构，并以 Choice Policies 在 VLM 端加辅助动作监督。预训练使用 10 万小时以上的 UMI 手持夹爪与第一视角真实轨迹，以 Qwen3.5-27B 对等长片段自动标注“场景状态转移”描述；后训练用约 1 万小时跨本体数据（含 7200 小时自有移动/双臂机器人数据）对齐机器人本体与祈使式指令。作者报告：在 2 万小时子集上，验证动作误差随数据与模型规模下降；后训练后在 4 个未见环境任务上的开箱成功率从无动作预训练的 26% 升至 75%（5B），10B 达 79%；少量数据微调即可完成装手机、装洗衣机、打印机加纸等新任务；在 RoboCasa、RoboCasa365、VLABench、RoboDojo 四个仿真基准上超过此前方法。结果支持非机器人真实轨迹预训练可扩展的判断，但扩展实验仅用 2 万小时子集，真机试验次数与对照细节需查原文，预训练数据未公开。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/XiaomiRobotics/Xiaomi-Robotics-1)；权重 partial，数据 none，许可 Apache-2.0。探测为 no-repo，项目页链接 XiaomiRobotics/Xiaomi-Robotics-1；已发布 5B 权重与 RoboCasa/RoboCasa365/VLABench 微调权重，2B/10B 与预训练检查点未列出。
- **数据/基准关系：** robocasa-bench（评测）
- **待核验事项：** 真机开箱评测与微调任务的每任务试验次数

### 16. RynnWorld-4D: 4D Embodied World Models for Robotic Manipulation — 🔥 重点阅读

- **时间：** 2026-07-07（[arXiv](https://arxiv.org/abs/2607.06559)）
- **评分：** C4（用 RGB-深度-光流联合生成把视频世界模型推向可直接服务动作的 4D 表示，并配大规模数据与策略头，增量清晰。） / E4（世界模型多指标对比与消融、6 个真机任务多类基线及表征受控对比，较完整，但测试集与平台规模有限。） / O4（代码实质开源（Apache-2.0）并发布模型权重，Rynn4DDataset 发布情况未确认。） / T4（达摩院具身团队与港中文合作，在具身世界模型与 VLA 方向有连续成果。） = **80/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** Hong Kong Embodied AI Lab；CUHK；Hupan Lab；DAMO Academy, Alibaba Group
- **分类：** `world-model` · 核心 · model
- **核心内容：** 为弥补 2D 像素视频世界模型缺乏几何与运动约束、与机器人低层动作差距大的问题，作者以同步 RGB、深度和光流（RGB-DF）作为投影式 4D 表示，深度与光流可反投影为 3D 场景流。RynnWorld-4D 将 Wan2.2-TI2V-5B 扩展为三分支 DiT，用带帧级 3D RoPE 的跨模态联合注意力保持外观、几何与运动一致；训练数据 Rynn4DDataset 1.0 汇集 Epic-Kitchens、EgoVid、RoboMIND、AgiBot 等人类与机器人视频共 2.54 亿帧，以外部模型生成深度、光流与描述伪标签。RynnWorld-4D-Policy 冻结世界模型、单次前向抽取内部特征，经 Flow Former 与动作头输出动作，RTX 5090 上约 9 Hz。在 50 段留出视频上，作者报告深度、光流与重建指标优于 TesserAct、4DNeX 等 4D 基线，并给出架构消融；在 TIANJI M6+WUJI 灵巧手的 6 个真机任务上，策略优于 DP、π0、π0.5、VPP、Mimic-Video，受控对比显示 RGB-DF 表征优于仅 RGB 或 RGB-深度-法线。局限是伪标签依赖外部估计器、真机评测限于单一平台、世界模型测试集较小。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/alibaba-damo-academy/RynnWorld-4D)；权重 open，数据 unknown，许可 Apache-2.0。HF 发布 RynnWorld-4D 权重。
- **数据/基准关系：** agibot-world（预训练）
- **待核验事项：** 真机 6 个任务每任务试验次数；Rynn4DDataset 1.0 伪标签是否公开

### 17. $\texttt{WEAVER}$, Better, Faster, Longer: An Effective World Model for Robotic Manipulation — 🔥 重点阅读

- **时间：** 2026-06-11（[arXiv](https://arxiv.org/abs/2606.13672)）
- **评分：** C4（把世界模型三项下游用途在同一模型上打通并给出关键设计取舍，对机器人世界模型子方向有明确推动。） / E4（视觉指标、策略评估、策略改进与规划均有真机验证并对比 Ctrl-World，但仅五个任务、单一机器人。） / O4（代码 MIT 开源，HF 上有权重与分布外评测数据；复现说明完整度未核实。） / T4（Andrea Bajcsy（CMU）与 Gokul Swamy 等在机器人学习与模仿学习方面有可核实的强相关积累。） = **80/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** Mila - Québec AI Institute；Université de Montréal；Carnegie Mellon University；McGill University
- **分类：** `world-model` · 核心 · model
- **核心内容：** 为让机器人世界模型同时满足保真、长时一致和高效三个条件，从而支撑策略评估、策略改进与测试时规划，作者提出 WEAVER：928M 参数、预测腕部与外部双视角潜变量和本体状态的世界模型，结合稀疏长时记忆+短时历史、diffusion forcing 余弦噪声日程、KV cache 与 rectified flow 蒸馏，并在潜空间上蒸馏 Robometer 奖励头与 critic。在 DROID 上预训练、五个真机 Franka 任务各 50 条数据微调后，作者报告：DROID 验证集与分布外数据上 FID/FVD 优于 Ctrl-World 且推理时间约为其 1/3；真机策略评估中与真实成功率相关系数 0.870；用 WEAVER 生成并按优势筛选的合成数据微调 π0.5，真机成功率平均提升 38%，接近用真实数据微调；best-of-N 测试时规划提升 14%。该结果提示潜空间世界模型已能在中等规模真机设置中替代部分真实交互，但任务仅五个、单一平台，奖励依赖外部模型，规划仍限单个动作块的短视程。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/arnavkj1995/WEAVER)；权重 open，数据 partial，许可 MIT。权重 https://huggingface.co/arnavkj1995/WEAVER；公开的是分布外评测数据 yilin-wu/droid_ood_data，真机微调数据未确认。
- **数据/基准关系：** droid（预训练）
- **待核验事项：** 仓库是否包含 DROID 预训练与真机微调的完整复现说明

### 18. $\mu_0$: A Scalable 3D Interaction-Trace World Model — 🔥 重点阅读

- **时间：** 2026-06-11（[arXiv](https://arxiv.org/abs/2606.13769)）
- **评分：** C4（以查询式 3D 交互轨迹作为可复用世界模型接口并配套可扩展数据引擎，较 TraceGen 有清晰增量。） / E4（轨迹预测基准、RoboCasa365 仿真与真机三任务均有对比和消融，但真机任务少且仿真上不及 π0.5。） / O4（代码 Apache-2.0 开源，HF 上有模型权重；TraceExtract 预训练数据是否公开未确认。） / T4（UMD 的 Furong Huang、Jia-Bin Huang 与 SNU 的 H. Jin Kim 在相关方向有可核实积累。） = **80/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** Seoul National University；University of Maryland, College Park；All Purpose AI
- **分类：** `world-model` · 核心 · model
- **核心内容：** 为在不依赖具身专属动作标签的情况下从大规模视频学习可迁移的运动先验，作者提出以 3D 交互轨迹为预测目标的世界模型 μ0。数据侧的 TraceExtract 用 DINOv2 实体聚类选取物体、工具、手和接触区域的关键点，分块重建并对齐到全局坐标得到 3D 轨迹，再按轨迹加速度切分事件并分层生成描述；模型侧在 SmolVLM2 前缀上加置换等变的 trace expert，以 B 样条控制点和语义流匹配预测未来轨迹。预训练后冻结 μ0，只训练读取其去噪特征的动作专家。作者报告在五个来源的留出集上 2D/3D 轨迹预测 ADE/FDE/DTW 优于 TraceGen 与 VLM 基线；RoboCasa365 八个任务平均成功率 30.25%，高于 Diffusion Policy、π0 与 TraceGen，但低于 π0.5（42%）；UR3 真机三任务平均 91.7%，高于去掉 trace expert 的版本 18.4 个百分点。该结果提示 3D 轨迹可作为无动作预训练的紧凑接口，但实验以桌面夹爪任务为主，不建模力与接触，且对比的 VLA 并非数据量匹配。
- **发表状态（核验：2026-10-22）：** CoRL 2026
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/Yoonkyo/mu0)；权重 open，数据 unknown，许可 Apache-2.0。权重见 https://huggingface.co/furonghuang-lab/mu0
- **数据/基准关系：** robocasa-bench（评测）
- **待核验事项：** TraceExtract 生成的轨迹数据集是否公开

### 19. OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics — 🔥 重点阅读

- **时间：** 2026-06-03（[arXiv](https://arxiv.org/abs/2606.04463)）
- **评分：** C4（统一骨架条件+大规模清洗数据的跨本体世界模型，并落地到真实策略排名评测，对世界模型评测方向有明确增量。） / E4（7 个基线、条件表示与数据组成消融、RoboArena 真机相关性分析；评测集自建、成功判定依赖 GPT-5。） / O4（推理代码（Apache-2.0）、OSCAR-2B 权重与机器人/人类/策略 rollout 数据集已在 HF 公开，训练代码未见。） / T4（NVIDIA/密歇根高俊在 3D 生成与世界模型方向有多项代表性工作。） = **80/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** Peking University；University of Michigan；NVIDIA
- **分类：** `world-model` · 核心 · model
- **核心内容：** 为解决动作条件视频世界模型在机器人策略评测中场景多样性不足、动作跟随不精确、跨本体泛化差的问题，作者提出 OSCAR：一方面构建标准化数据流水线，从 DROID、RH20T、AgiBot、InternData-A1、AIROA-MoMa 及 EgoDex、EPIC-Kitchens 共约 216 万条视频中按长度、静态相机、有效动作、骨架可见性过滤并做语义去重，得到约 18 万条联合训练数据；另一方面以 2D 运动学骨架渲染作为统一条件，适用于不同机械臂乃至人手，在单张 GH200 上两阶段微调 Cosmos-Predict2.5-2B。作者报告在自建的四本体评测集上，与 Kinema4D、Genie Envisioner 等 7 个基线相比 PSNR/LPIPS/FVD 多数最优；骨架与 mesh 条件效果相当而潜在动作条件明显更差，加入人类视频带来正迁移；在 RoboArena 65 个会话、7 个 DROID 策略上，用 GPT-5 判定生成视频成功与否，其排名与真机结果的相关性优于其他条件表示。该结果提示显式骨架条件是精度与泛化的较好折中，但评测依赖 VLM 判定与相机标定质量，仅静态相机，且仓库目前只开放推理。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 部分开放，[仓库](https://github.com/wuzy2115/oscar-public)；权重 open，数据 open，许可 Apache-2.0。README 自述为 public inference release，含推理 CLI 与 HF 权重 zywu2115/OSCAR-2B 及三个数据集，无训练流水线
- **数据/基准关系：** droid（微调/后训练）、agibot-world（微调/后训练）、epic-kitchens-100（微调/后训练）
- **待核验事项：** 训练代码是否会补充开放

### 20. Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization — 🔥 重点阅读

- **时间：** 2026-01-19（[arXiv](https://arxiv.org/abs/2601.12993)）
- **评分：** C4（大规模人本预训练配方 + 统一动作空间 + 部署期稳定化技术，形成完整的跨本体基础模型方案，增量明确。） / E4（LIBERO 与 RoboCasa 两个仿真基准对比大量 VLA 基线，另有 5 种真机评测和多组消融；真机任务为自建，跨工作数字不宜直接比较。） / O4（Apache-2.0 代码与 HF 权重已公开，数据仅发布 UniHand 预览版，README 仍有部分 coming soon。） / T4（BeingBeyond 团队（卢宗青等）此前发布 Being-H0 等工作，在人类视频驱动的机器人学习方向有可核实积累。） = **80/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** BeingBeyond Team
- **分类：** `vla` · 核心 · model
- **核心内容：** 为缓解 VLA 面对形态异构与数据稀缺时难以跨本体迁移的问题，Being-H0.5 提出以人为中心的学习范式：把人类手部交互轨迹视作物理交互的通用「母语」，构建 UniHand-2.0 预训练配方（3.5 万小时以上，含人类第一人称视频、30 种本体的机器人数据及视觉-语言数据），并用统一动作空间把不同机器人控制映射到语义对齐的槽位。模型采用 Mixture-of-Transformers 架构，用 Mixture-of-Flow 区分共享运动基元与本体专属专家；部署侧提出 Manifold-Preserving Gating 应对感知偏移、Universal Async Chunking 适配不同延迟与频率。作者报告 LIBERO 平均成功率 98.9%、RoboCasa 24 任务 53.9%，并以单一检查点在五种真机上完成多类任务，消融显示人本预训练与 MPG+UAC 对少样本适配、长时程和双臂任务有益。该结果提示人类数据可为低资源本体提供先验，但数据配方中各来源的贡献尚未完全拆分，UniHand-2.0 目前仅公开预览版，真机评测由作者自建任务完成。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/BeingBeyond/Being-H)；权重 open，数据 partial，许可 Apache-2.0。HF 上有 BeingBeyond 模型集合；数据仅见 UniHand_Preview；README 提示部分内容 coming soon。
- **数据/基准关系：** open-x-embodiment（预训练）、agibot-world（预训练）、libero（评测）、robocasa-bench（评测）
- **待核验事项：** README 标注部分内容 coming soon，需确认训练代码与完整 UniHand-2.0 是否开放

### 21. Keep the Future, Drop the Rollout: RIFT for World Action Models — 👀 值得关注

- **时间：** 2026-08-12（[arXiv](https://arxiv.org/abs/2608.11521)）
- **评分：** C4（用因果干预厘清 WAM 中未来表征的作用，并据此给出一次前向的部署接口，对 WAM 推理效率有明确增量。） / E4（三个仿真基准加 OOD 测试与真机实验，同骨干匹配对照、消融与 bootstrap 置信区间较完整；RoboTwin 上差距较小。） / O4（仓库含训练/评测代码与 MIT 许可，检查点在 HuggingFace 发布；外部基础模型需自行下载。） / T3（ANU 李宏东组在三维视觉方向积累深厚，但机器人学习方向的标志性成果相对少。） = **77/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Australian National University；FreiNexus；Beijing Normal University
- **分类：** `world-model` · 核心 · method
- **核心内容：** 世界动作模型（WAM）依赖迭代生成未来视频来条件化动作，部署延迟高。作者先在 4 个 WAM、40 个 LIBERO 任务上做配对闭环干预：屏蔽或扰动未来 K/V 缓存会显著改变轨迹并降低成功率，而在整个动作去噪中复用同一份最终干净缓存几乎不影响执行（末端平均位移误差约 1.7–1.9 cm），说明动作读取的是未来表征而非 rollout 过程。据此提出 RIFT：在 Fast-WAM-Joint 架构中放入可学习的预期 token，一次骨干前向构造完整未来缓存，并以条件流匹配作辅助监督。作者报告 LIBERO 总成功率 98.8%，高于同骨干、同数据的 rollout 式方法，延迟降低 3.1–9.2 倍；未再训练时 LIBERO-Plus 为 81.1%；RoboTwin 2.0 干净/随机场景为 92.9%/92.6%；Galaxea R1 Lite 真机三任务各 50 次试验平均 45.3%，比 Fast-WAM-Joint 高 6.0 个百分点。该结果提示 WAM 可保留未来条件化而省去部署时的视频生成，但干预结论限于所测模型与协同去噪设置，RoboTwin 上各方法差距很小，真机仅三项任务。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/ChushanZhang/RIFT)；权重 open，数据 n/a，许可 MIT。探针未发现仓库；论文首页给出该 GitHub 地址，README 含训练与 LIBERO/LIBERO-Plus/RoboTwin 评测命令，检查点托管于 HF PoopBear/RIFT（2026-10-22 核对）。
- **数据/基准关系：** libero（评测）

### 22. $N_0$-VTLA: Scaling Vision-Tactile-Language-Action Model with Latent Tactile Tokens — 👀 值得关注

- **时间：** 2026-07-26（[arXiv](https://arxiv.org/abs/2607.23782)）
- **评分：** C4（首个宣称规模化触觉预训练的 VTLA，并以预测式潜触觉替代当前读数，对触觉 VLA 方向有明确增量。） / E4（9 个真机任务、20 个仿真任务、多个外部基线及离线 RL 改进实验较完整，但基线为内部复现、传感器自研。） / O4（实质代码（Apache-2.0）及基座与任务权重已在 HF 开放；NeoData 文中称已发布但未核实。） / T3（NeoteAI 与复旦 TEAI 的可核实积累信息有限，按默认 3 分。） = **77/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** NeoteAI；Fudan TEAI
- **分类：** `vla` · 核心 · model
- **核心内容：** 为解决现有 VLA 缺少触觉、触觉扩展又多基于小规模任务数据且只用当前触觉读数的问题，N0-VTLA 在 pi0.5 式 PaliGemma 骨干与流匹配动作专家之外加入潜触觉通路：用冻结 DINOv2 编码手指视触觉差分图，经小型预测器结合视觉-语言上下文输出估计下一动作块内触觉变化的潜 token，仅作为动作专家条件而不进入视觉-语言前缀；通过三阶段训练（对比+重建 grounding、对齐、端到端）接入，并在自建多平台视触觉数据集 NeoData 上预训练。此外提出 ALTER，用进度模型、触觉检测的掉落事件和人工纠正生成二值优势标签做离线策略改进。作者报告在 NeoReal 9 个接触丰富真机任务上成功率均超过 pi0.5 与 ACT，UniVTAC 8 任务平均 83.1%（InternVLA-A1 67.1%），NeoSim 12 任务平均 50.8%，ALTER 在三个长程真机任务达 75–95%。该结果提示规模化触觉预训练与预测式触觉条件有效，但传感器为自研视触觉，基线均为内部复现，数据集开放程度待确认。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/neoteai/N0-VTLA)；权重 open，数据 unknown，许可 Apache-2.0。HF 有 NeoteAI/n0-vtla-base 及两个任务权重；论文称 NeoData 为已发布语料，未见链接。
- **待核验事项：** 确认 NeoData 视触觉数据集的发布位置与许可；核实 NeoteAI 团队此前的相关研究产出

### 23. $N_0$-TWAM: Scaling Tactile-Native World-Action Model for Contact-Rich Manipulation — 👀 值得关注

- **时间：** 2026-07-26（[arXiv](https://arxiv.org/abs/2607.23783)）
- **评分：** C4（把触觉作为世界-动作模型的联合预测目标并做大规模预训练，对触觉操作子方向有明确增量。） / E4（公开基准 UniVTAC、自建 NeoSim 与 8 项真机任务加消融，基线覆盖 VLA 与 WAM；但部分基准自建、真机试次有限。） / O4（仓库含实质代码并在 HF 发布多份权重，许可 CC-BY-NC；NeoData 训练数据未见公开。） / T3（NeoteAI 与复旦团队，公开可核实的触觉/具身成果信息有限，按默认 3 分。） = **77/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** NeoteAI Team；Fudan TEAI Team
- **分类：** `world-model` · 核心 · model
- **核心内容：** 为解决接触密集操作中相机难以分辨指尖接触状态、现有世界-动作模型只预测视觉未来的问题，作者提出 N0-TWAM：以视频扩散 Transformer 为骨干，重组为视频/触觉/动作三专家的非对称 Mixture-of-Transformers，仅通过共享自注意力交互；触觉既作为与视频同目标、同因果步预测的未来信号，又经 NeoForce 力表示作为当前观测输入，并用触觉接触事件切分长时程任务阶段。模型在自采 NeoData（六种本体、带逐指触觉）上大规模预训练。作者报告：公开触觉仿真基准 UniVTAC 八任务平均 84.5%，高于 InternVLA-A1 的 67.1% 及纯视觉 WAM 基线；自建 NeoSim 十二任务平均 49.4%（最强基线 45.8%）；PiPER 与 Flexiv 上 8 项真机任务整体最好，优势集中在插座插拔、立瓶等依赖接触状态的任务，消融显示两条触觉通路与预训练规模均有贡献。该结果提示触觉进入世界模型的预测目标对接触任务有益，但 NeoSim 与真机任务均为自建、真机由操作员判定且试次有限，仿真触觉与真实传感器存在差异，训练数据集尚未公开。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/neoteai/N0-TWAM)；权重 open，数据 none，许可 CC-BY-NC。探测到 60 个文件、HF 上有 base 及 NeoSim/UniVTAC 微调权重；预训练数据 NeoData 未公开。
- **待核验事项：** NeoteAI / Fudan TEAI 团队过往具身与触觉研究产出；NeoData 数据集是否会公开

### 24. GigaBrain-0.7: Scaling Embodied Foundation Models to Emergent Capabilities with a Three-System Architecture — 👀 值得关注

- **时间：** 2026-08-16（[arXiv](https://arxiv.org/abs/2608.15875)）
- **评分：** C4（将理解、预测评估与动作三系统结合并扩展到 3.7 万小时数据，作为开放的具身基础模型有明确影响力。） / E3（有数据规模、主干选择、耦合架构与 System 3 接口的消融及真机评测；多为自建任务，本次只读到图表标题级别的实验信息。） / O4（官方仓库有实质代码（Apache-2.0），HuggingFace 已发布 0.7 的 3.5B 基础与基准权重，数据仅发布样例。） / T4（GigaAI 此前发布 GigaBrain-0、GigaWorld 等模型，在具身基础模型方向有可核实积累。） = **75/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** GigaBrain Team
- **分类：** `vla` · 核心 · model
- **核心内容：** 为检验 VLA 能否通过架构设计和更大规模、更异构的数据获得更广泛的跨任务与跨具身泛化，作者提出 GigaBrain-0.7：System 2 为 PaliGemma2-3B，负责场景理解与长程任务分解；System 1 为 PaliGemma2-3B 加 0.5B 动作专家，以流匹配生成连续动作块，并适配不同具身的自由度；System 3 为基于 GigaWorld-1 的 5B 世界价值模型，预测子目标图像与状态价值，为 System 1 提供条件。预训练语料包括 3.7 万小时具身轨迹（真机 55%、UMI 22%、第一人称人类 8%、仿真 4%、世界模型生成 11%）和约 2.7 亿条视觉语言样本，采用视觉语言理解与多具身动作单阶段联合训练，并配有 SFT、离线与在线强化的经验强化流程。作者报告在自研 Maker H01 与 AgileX PiPER 等平台上，零样本多任务语言跟随、后训练成功率优于 GigaBrain-0 与 π0.5，数据规模扩大可持续降低验证损失、提升真机表现，System 3 的子目标图像与价值条件均带来增益。该结果提示多系统协同与数据扩展有效，但主要评测为自建真机任务，与外部方法的对比条件难以独立核验；本次缓存未覆盖完整实验表格。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/open-gigaai/giga-brain-0)；权重 open，数据 partial，许可 Apache-2.0。项目页字段原为 tau0-vla.github.io，与本文无关；论文给出的项目页为 https://gigaai.cc/blog/gigabrain07。HF 有 GigaBrain-0.7-3.5B-Base/EBench/RoboTwin2.0 权重与 SampleData 样例数据。
- **数据/基准关系：** agibot-world（预训练）
- **待核验事项：** 完整实验表格（零样本与后训练成功率、与 π0.5 的对比条件）

### 25. From Foundation to Application: Improving VLA Models in Practice — 👀 值得关注

- **时间：** 2026-07-07（[arXiv](https://arxiv.org/abs/2607.06403)）
- **评分：** C4（大规模多本体数据、全身自由度动作空间与开源权重，对通用 VLA 实践有明确资源与方法增量。） / E3（有两款平台的真机多任务与长程移动操作对比，但每任务试验次数少、提升不均，缺少组件级消融。） / O4（代码实质开源（Apache-2.0）并发布 6B 权重，预训练数据未公开。） / T4（LingBot 系列团队已有 VLA、深度估计等多项连续开源成果。） = **75/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Wu, Wei et al.
- **分类：** `vla` · 核心 · model
- **核心内容：** 为缩小 VLA 基础模型在实验室与实际部署之间的差距，作者在 LingBot-VLA 基础上推出 2.0 版：重做数据清洗管线（基于 jerk 与导数 Z 分数过滤、URDF 投影人工核对），从约 9 万小时原始数据中保留 5 万小时、覆盖 20 种机器人构型的轨迹，并加入 1 万小时人类第一视角视频，用 VLM 自动分割子任务与标注；动作空间扩展到头部、腰部、移动底盘与灵巧手；动作专家采用无辅助损失的 token 级稀疏 MoE；并以 LingBot-Depth 与 DINO-Video 为教师对当前与未来观测做双查询蒸馏。在 GM-100 九个双臂任务的通才混合训练设置下，作者报告 Agilex 与 Galaxea R1 Pro 上平均进度/成功率分别为 66.2/34.4 与 34.6/15.6，高于 GR00T N1.7 与 LingBot-VLA 1.0 等基线；两款平台的长程移动操作（每设置 15 次）在域内与 OOD 下也有提升。但各任务提升不均，成功率总体偏低、试验次数少，且缺少对各新组件的系统消融。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/robbyant/lingbot-vla-v2)；权重 open，数据 none，许可 Apache-2.0。HF 发布 lingbot-vla-v2-6b 及 RoboTwin 微调权重；预训练数据未公开。
- **待核验事项：** 以 PDF 核对作者单位（HTML 未列出，项目页在 robbyant 域名下）；GM-100 每任务试验次数及第二列基线名称

### 26. Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking — 👀 值得关注

- **时间：** 2026-08-20（[arXiv](https://arxiv.org/abs/2608.20087)）
- **评分：** C4（把视频风格学习与速度自适应规划-跟踪结合用于人形球类运动，对高动态风格化技能有明确增量） / E4（仿真多基线（AMP/PULSE/NCP/Vid2Player3D/DeepMimic）+ 两款真机 + 组件消融，但真机试次偏少） / O3（官方仓库有实质代码且 Apache-2.0，权重与动作数据是否公开未核实） / T4（上海 AI Lab 庞江淼团队在人形运动控制方向有多项可核实成果） = **74/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Noitom Robotics；Shanghai AI Laboratory；Shanghai Jiao Tong University；Dobot Robotics
- **分类：** `sim2real` · 核心 · method
- **核心内容：** 为在人形机器人上兼顾职业网球动作风格与击球任务表现，并缓解解耦规划-跟踪架构在真机上的跟踪退化与自回归误差累积，作者提出 AdaPT：从纳达尔、费德勒、德约科维奇转播视频重建并重定向约 1.6 万段动作，训练 MVAE 动作生成器与高层规划器；底层跟踪器在随机执行速度下训练，规划器同时输出动作潜变量与速度适配信号，发球则基于 AdaMimic 训练残差跟踪器。在 Mjlab 仿真中作者报告其在风格（FID）与命中率之间取得较好平衡；在 G1 真机上以发球机 25 次/区域评测，纳达尔风格正反手命中率由 Vid2Player3D 的 28%/28% 提升到 44%/56%，并做了自适应规划器与跟踪器的逐项消融，还在 1.7 m Dobot Atom 上实现无动捕户外发球。该结果提示速度自适应是缩小风格化技能 sim-to-real 差距的有效手段，但对局场地为缩小版、依赖动捕或多目相机定位，真机试次有限。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/noitom-robotics/AdaPT)；权重 unknown，数据 unknown，许可 Apache-2.0。摘要声明代码已公开；探测到 309 个代码文件
- **待核验事项：** 核实仓库是否发布训练好的策略权重与处理后的网球动作数据

### 27. SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation — 👀 值得关注

- **时间：** 2026-08-10（[arXiv](https://arxiv.org/abs/2608.09771)）
- **评分：** C3（用逆/前向动力学掩码预测训练紧凑隐空间策略，思路清晰，但与 JEPA 式表征学习和现有 WAM 相比增量有限） / E4（覆盖 LIBERO、LIBERO-Plus 零样本和 CALVIN 三个仿真基准，另有 5 个真机任务和扰动测试，并做了 Stage-1、损失比例与 EMA 的消融） / O4（仓库有实质代码（MIT），HF 上公开了 CALVIN 和 LIBERO 的权重；真机数据未见公开） / T4（作者来自复旦、智源（BAAI）、清华，在具身模型方向有可核实的积累） = **74/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Fudan University；Beijing Academy of Artificial Intelligence；Tsinghua University；Renmin University of China
- **分类：** `vla` · 核心 · model
- **核心内容：** 大型 VLA 在每个控制步都要跑完整的多模态骨干，像素级世界模型又要预测许多与控制无关的外观细节，两者都推高了计算与延迟。为此作者提出 0.5B 参数的 SLIM：以 DINOv2 观测隐变量和连续动作 token 为输入，用 Mixture-of-Transformers 骨干建模二者的交互。第一阶段做自监督掩码轨迹预测，同时包含逆动力学分支（由当前与未来隐变量重建动作）和前向动力学分支（由当前观测与动作预测 EMA 目标下的未来隐变量）；第二阶段用 flow matching 训练可部署策略。作者报告：仅用 LIBERO 数据训练时原始 LIBERO 达 97.5%，同一 checkpoint 在 LIBERO-Plus 零样本为 77.45%，CALVIN ABC→D 平均序列长度 4.556；在 5 个真机任务（共 750 条示教，含背景、光照、干扰物扰动）上，平均进度分在多数设置下最高，背景扰动下略低于 π0.5 类基线；推理延迟与显存明显低于 7B 级基线。消融显示第一阶段训练和 EMA 目标都有贡献。这提示把动力学作为训练信号塑造紧凑表征，可能是大骨干之外的一条高效路线，但目前只验证了单一模型规模、没有跨本体预训练，也未说明能否扩展到更多样的任务。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/kzz1031/SLIM)；权重 open，数据 unknown，许可 MIT。HF 上有 kzzwang/SLIM-CALVIN 与 kzzwang/SLIM-LIBERO 两个权重
- **数据/基准关系：** libero（微调/后训练）、libero（评测）、calvin（微调/后训练）、calvin（评测）
- **待核验事项：** 真机示教数据是否公开

### 28. DriftWorld: Fast World Modeling through Drifting — 👀 值得关注

- **时间：** 2026-07-16（[arXiv](https://arxiv.org/abs/2607.15065)）
- **评分：** C4（首次把单步 drifting 生成引入动作条件世界模型，明显降低世界模型用于规划与评估的成本。） / E4（五个数据集、多类世界模型基线、动作筛选与策略评估两类下游及消融，但无真机闭环。） / O3（仓库含各数据集训练与评测代码，README 提供 HF 检查点，但未声明许可证。） / T4（Yilun Du 团队在视频世界模型与生成式规划方向有多项标志性工作。） = **74/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Massachusetts Institute of Technology；Harvard University
- **分类：** `world-model` · 核心 · method
- **核心内容：** 为解决扩散式机器人世界模型多步去噪导致推理过慢、难以支撑在线动作搜索和大规模策略评估的问题，作者提出 DriftWorld：把原用于类别条件图像生成的 drifting 模型改造为动作条件视频预测，在训练期学习漂移场，推理时单次前向即可生成未来帧；关键设计包括单正样本漂移目标、把当前帧作为额外负样本的动作强调，以及在 DINOv2/v3 特征空间计算核并对运动区域加权。在 Push-T、Robomimic、Bridge-V2、RT-1、Language Table 上，作者报告其相对 IRASim、Ctrl-World、GPC、LVDM 等基线快 12 倍以上，多数视觉指标相当或更优；用于 GPC-RANK 动作筛选时 Push-T IoU 由 0.635 升至 0.772；作为离线模拟器，策略得分与真值的相关系数在 Push-T 为 0.98、Robomimic 为 0.996/0.962。该结果提示单步生成可显著降低世界模型规划成本，但闭环验证仅在仿真中完成，真实数据集只做开环视觉评估，U-Net 架构在长时域与复杂场景下的能力仍待检验。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/Susie-Lu/driftworld)；权重 open，数据 n/a，许可 unknown。探测为 no-repo，项目页链接仓库 Susie-Lu/driftworld；README 提供 HF 检查点，RT-1/Bridge 需另下 DINOv3 与 SD3 VAE；未见 LICENSE 文件。
- **数据/基准关系：** bridgedata-v2（预训练）、bridgedata-v2（评测）
- **待核验事项：** 仓库许可证

### 29. LARA: Latent Action Representation Alignment for Vision-Language-Action Models — 👀 值得关注

- **时间：** 2026-06-05（[arXiv](https://arxiv.org/abs/2606.07100)）
- **评分：** C4（用表征对齐打通 LAM 与 VLA 联合训练，适用预训练、后训练和 LAM 精炼三种场景，增量明确。） / E4（LIBERO、SimplerEnv、GR1 仿真与 G1 真机，含受限/非受限两种对比和消融；强基线上增益小。） / O3（代码仓库实质完整并有 HF 权重，但未找到许可证。） / T4（BIGAI 黄思远团队在具身智能与 3D 场景理解方向有多项代表性成果。） = **74/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** State Key Laboratory of General Artificial Intelligence, BIGAI；Peking University；Delta Intelligence
- **分类：** `vla` · 核心 · method
- **核心内容：** 潜动作模型（LAM）能从无标注视频中提取动作监督，但通常与 VLA 分开训练：LAM 得不到真实动作约束，VLA 又受制于冻结的 LAM 表征。LARA 借鉴图像扩散中的表征对齐，把 DiT 动作模型中间层特征与 LAM 的潜动作表征对齐，并让两者联合优化，使 LAM 被真实轨迹约束、VLA 被前向动力学正则，流程分为 LAM 视频预训练、联合预训练与联合后训练。作者报告：仅用 OXE 预训练时 LIBERO 平均 88.6%、SimplerEnv 65.2%，高于 Moto-GPT、LAPA 和自身无对齐 DiT 基线；作为后训练插件，GR00T-N1.6-LARA 在 LIBERO（95.6% 对 95.0%）、SimplerEnv、GR1 仿真上小幅提升；在新具身 GR1 仿真与 Unitree G1 真机 50 示教设定下提升明显（G1 两任务平均 74% 对 56%，各 50 次试验）；用 LARA 对齐后的 LAM 训练 Moto-GPT 也在 SimplerEnv 上更好。消融显示对齐层深度与联合优化都重要，最优层依骨干而异。结果提示表征对齐是连接视频潜动作与动作学习的轻量途径，但在强基线上增益很小，真机任务仅两个。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/lmy1001/LARA)；权重 open，数据 n/a，许可 unknown。HF 权重 https://huggingface.co/MengyaLiu/LARA_full ；仓库未见许可证文件。
- **数据/基准关系：** libero（评测）、simplerenv（评测）、open-x-embodiment（预训练）
- **待核验事项：** 仓库许可证；是否被 ICML 2026 录用（正文关键词与链接暗示，元数据未写明）

### 30. AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding — 👀 值得关注

- **时间：** 2026-06-04（[arXiv](https://arxiv.org/abs/2606.06155)）
- **评分：** C4（将可供性系统化为 VLA 中间监督并配合 MoT 与大规模定位数据，方法增量清晰，可能影响 VLA 中间表示方向。） / E4（覆盖 LIBERO、CALVIN、RoboCasa、LIBERO-Plus 及真机，并有针对数据/结构/训练阶段的对照消融；真机每任务仅 15 次。） / O3（仓库含实质代码且为 MIT 许可，但未确认是否发布本文训练权重与增广标注数据。） / T4（北大、港科广（梁俊卫）、港中文等团队在可供性与 VLA 方向有可核实积累。） = **74/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Peking University；HKUST (GZ)；The Chinese University of Hong Kong；Knowin AI
- **分类：** `vla` · 核心 · model
- **核心内容：** 为缓解 VLM 语义空间与具身控制之间的结构错配、视频预测类中间表示冗余且推理慢的问题，AffordanceVLA 将结构化可供性（操作哪个物体、在哪接触、如何从 3D 形状/布局角度交互）作为训练期中间监督，构建理解专家、可供性生成专家和动作专家组成的 Mixture-of-Transformer 架构，并以三阶段课程训练：先用约 8.8M 条通用定位/指点数据预训练，再在带自动可供性标注的 InternData-A1 仿真数据上协同训练，最后在目标任务微调。作者报告在 LIBERO 四套件平均成功率 95.8%、CALVIN ABC→D 平均链长 4.33，并在 RoboCasa 与 LIBERO-Plus OOD 评测上优于所列基线；消融显示仅加数据（Pi0 架构）提升有限、冻结可供性专家性能崩溃，去掉 Stage II 主要损害泛化。真机上（每任务 15 次）基础任务平均 88.3% 对 π0 70.8%，同图像不同指令的复杂任务 82.9% 对 44.8%。结果提示可供性中间表示有助保持语言-视觉对齐并改进指令跟随，但真机试次较少、训练数据与算力（16×H200）投入大，与基线的数据量对齐程度仍需细看。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/Skywalker-yqz/AffordanceVLA)；权重 unknown，数据 unknown，许可 MIT。探测到的 HF 链接均为第三方基础模型（PaliGemma、pi0_base、Flux 等），非本文权重。
- **数据/基准关系：** libero（评测）、calvin（评测）、robocasa-bench（评测）、droid（预训练）
- **待核验事项：** 仓库是否发布 AffordanceVLA 训练好的权重及自动可供性标注数据；真机机器人平台型号与 DROID 预训练子集规模

### 31. HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers — 👀 值得关注

- **时间：** 2026-06-04（[arXiv](https://arxiv.org/abs/2606.06493)）
- **评分：** C4（动作切片+上下文条件的多教师蒸馏给出面向规划器的紧凑全身控制接口，对人形 WBC 子方向有明确增量。） / E4（有逐级消融、与四个 WBC 的匹配对比、恢复与大规模仿真任务试验及真机演示；真机缺少定量统计。） / O3（项目页链接的官方仓库含训练与部署代码，README 称附带蒸馏策略 ONNX，但未见许可证。） / T4（Caltech Aaron Ames 团队与 IHMC 在双足/人形控制方向积累深厚。） = **74/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** California Institute of Technology；The Institute for Human & Machine Cognition
- **分类：** `locomotion` · 核心 · method
- **核心内容：** 为让高层规划器（人、几何规划器或 VLM）只需给出稀疏的任务空间指令、而不必生成密集的全身运动参考，HANDOFF 分别训练全身动作跟踪、速度指令行走和基于 AMP 的摔倒恢复三个 PPO 教师，再用按动作切片、按上下文加权的多教师 KL 损失加软混合专家，把它们蒸馏为一个 29 自由度学生策略；学生只接收 10 维指令（平面速度、根高度、双腕目标），部署时无需切换策略。作者在 mjlab/MuJoCo 中报告：逐步加入各教师与机制的消融显示速度跟踪误差逐步下降；在统一的差分 IK 适配接口下与 FALCON、OpenHomie、AMO、SONIC 比较，HANDOFF 鲁棒工作空间为 0.277 m³（SONIC 0.265，但可行率 96.2% 高于其 93.0%）；500 个摔倒初始状态下恢复专家才能学会站起；5 类任务各 500 次随机试验中总体成功率 67.2%–100%。真机 G1 上同一策略执行了 6 段 VLM 指令序列，但真机仅为定性展示。结果提示多教师蒸馏是获得紧凑全身控制接口的可行路径，但对比依赖作者设计的适配协议，任务级统计来自仿真。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/lzyang2000/HANDOFF)；权重 partial，数据 none，许可 unknown。原探测仓库 ccrpRepo/AMP_mjlab 为第三方实现；官方仓库取自项目页，含训练脚本与 sim2sim/sim2real 部署代码，README 称附带蒸馏策略 ONNX；动作数据集需外部获取。
- **待核验事项：** 仓库许可证及 deploy/ckpt/policy.onnx 是否确实提供

### 32. Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking — 👀 值得关注

- **时间：** 2026-06-02（[arXiv](https://arxiv.org/abs/2606.03985)）
- **评分：** C4（系统性展示人形跟踪的数据/模型缩放规律并给出可零样本泛化的 Transformer 跟踪器，对全身控制子方向影响明确。） / E4（数据与模型缩放实验、架构对比、三个公开跟踪器基线与真机量化评估，但真机评估片段数有限。） / O3（仓库提供推理、部署代码与预训练 ONNX 权重（Apache-2.0），训练代码与训练数据尚未发布。） / T4（清华弋力、北大王鹤与银河通用团队在人形与具身方向有多项可核实成果。） = **74/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Tsinghua University；Galbot Inc.；Shanghai Jiao Tong University；Peking University；Shanghai Qi Zhi Institute
- **分类：** `locomotion` · 核心 · model
- **核心内容：** 为打破人形动作跟踪中"敏捷性与泛化性此消彼长"的局面，作者认为根源在于数据与模型规模不足，提出 Humanoid-GPT：汇集 AMASS、LAFAN1、Motion-X++、PHUMA、MotionMillion 及内部采集数据，重定向到 29 自由度 Unitree G1 并过滤、时间伸缩增强得到约 20 亿帧语料；用谐波动作嵌入（HME）聚成约 300 个簇，每簇训练 PPO 专家，再以并行 DAgger 把所有专家蒸馏进因果注意力的 GPT 式 Transformer。MuJoCo 中在未见过的 AMASS 测试集上，作者报告成功率随规模单调提升：同为 2M token 时 MLP 76.9%、TCN 81.5%、Humanoid-GPT-S 83.3%，2B token 的 22M 模型 90.4%、80M 模型 92.6%；在四段未见舞蹈上 MPJPE/MPJVE 多数优于 GMT、TWIST、Any2Track 的官方权重。真机 G1 上零样本跟踪动态舞蹈与在线动捕遥操作，TensorRT 部署延迟约为 TWIST 的 1/5。结果提示规模化与 Transformer 结构可同时提升泛化与敏捷性，但部分舞蹈片段上优势不一致，内部数据与训练代码未公开。
- **发表状态（核验：2026-10-22）：** CVPR 2026
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 部分开放，[仓库](https://github.com/GalaxyGeneralRobotics/Humanoid-GPT)；权重 open，数据 none，许可 Apache-2.0。README 已提供推理/评测/真机部署代码与预训练检查点；训练代码与训练数据仍在 TODO 中。
- **数据/基准关系：** amass（预训练）
- **待核验事项：** 训练代码与 20 亿帧训练数据是否按 TODO 发布

### 33. HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation — 👀 值得关注

- **时间：** 2026-04-09（[arXiv](https://arxiv.org/abs/2604.07993)）
- **评分：** C4（针对全尺寸双足人形全身操作提出结构化状态表示与本体感知预测，方法增量清晰，可能影响人形 VLA 子方向。） / E4（两款真机平台 7 项任务 + 长时程任务，对比 4 个强基线，含消融、泛化与失败分析；但每任务试验次数较少（12–18 次）。） / O3（仓库含实质代码，HF 上有权重与数据集，但未找到许可证文件，按许可不清晰降档。） / T4（北京人形机器人创新中心与北大张尚彰团队等，有可核实的人形与 VLA 相关积累。） = **74/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Beijing Innovation Center of Humanoid Robotics；Xi’an Jiaotong University；Nankai University；Peking University
- **分类：** `vla` · 核心 · model
- **核心内容：** 为解决多数 VLA 把机器人各身体部位独立处理、难以在高自由度人形上产生协调全身动作的问题，HEX 采用「高层 VLA + 低层 RL 全身控制器」的分层框架：高层提出人形对齐的通用状态表示，把不同本体的本体感知映射到手臂、手、腿、头、腰等规范身体部位槽位；用基于形态的 MoE 统一本体感知预测器 (UPP) 建模全身协调与短期状态演化；用轻量历史查询特征缓存汇总过去视觉上下文，避免重复编码历史图像；再以残差门控融合与 flow-matching 动作头生成动作；预训练语料超过 1200 万帧、覆盖 7 种人形本体。在天工 2.0 / 3.0 真机 7 项任务（每项 12 次）及长时程搬箱任务上，作者报告 HEX 成功率高于 ACT、SwitchVLA、GR00T N1.5 和 π0，快速反应与长时程场景优势明显，泛化测试中保持领先；消融显示 UPP 贡献最大，预训练主要加快收敛、对单任务最终成功率影响有限。局限：评测仅在自家两款平台、试验次数较少，跨本体收益在多任务设置下尚未充分验证。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/Open-X-Humanoid/HEX)；权重 open，数据 open，许可 unknown。探测到 HF 权重 X-Humanoid/HEX-Model 与数据集 X-Humanoid/HEX-Datasets；仓库未见 LICENSE 文件。
- **数据/基准关系：** agibot-world（预训练）
- **待核验事项：** 仓库许可证未找到，需确认代码/权重/数据的使用许可

### 34. Kairos: A Regret-Aware Native World-Action Model Stack for Physical AI — 👀 值得关注

- **时间：** 2026-06-15（[arXiv](https://arxiv.org/abs/2606.16533)）
- **评分：** C4（完整的世界-动作模型栈并开放 4B 权重，混合线性时序注意力与数据课程对 WAM 方向有参考价值。） / E3（覆盖多项世界模型、世界-动作与效率评测，但作者承认均为代理证据，缓存中未见真机闭环实验。） / O4（实质代码（Apache-2.0）与多份 HF 权重（含 RoboTwin 2.0、LIBERO-Plus 微调版）已开放，训练数据未开放。） / T3（署名为 Kairos Team（含陶大程、王晓刚等），HTML 未列单位，按默认 3 分。） = **72/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Kairos Team et al.
- **分类：** `world-model` · 核心 · model
- **核心内容：** 为解决现有世界模型或侧重像素生成、或缺乏可部署长时状态、难以直接服务具身控制的问题，Kairos 主张世界模型只需学习并维持“控制充分状态”（物体状态、空间关系、接触、任务进度、动作后果、失败风险、部署不确定性）。方法包括：按干预强度组织的跨本体数据课程（开放世界视频→人类行为数据→AgiBotWorld-Beta、DROID 等机器人数据），统一理解/生成/预测的架构与局部-中程-全局三路混合线性时序注意力（LinearDiT），基于执行结果偏好的“遗憾感知”世界-动作对齐训练，以及针对时延与显存的部署协同设计。作者报告在 WorldModelBench 机器人集、PAI-Bench 等具身世界模型基准和世界-动作基准上取得领先或有竞争力的结果，并在 DiT 单步推理时间上随序列长度线性扩展。该结果提示面向控制的状态压缩与线性注意力可兼顾能力与效率，但作者明确各项评测只是“遗憾相关能力”的代理证据，真实闭环遗憾降低与真机自进化留待后续工作。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/kairos-agi/kairos)；权重 open，数据 none，许可 Apache-2.0。HF 有 Kairos3.1-4B-robot-480P 及 RoboTwin2.0、LIBERO-plus 微调权重。
- **数据/基准关系：** agibot-world（预训练）、droid（预训练）
- **待核验事项：** 从 PDF 确认作者单位；核对 RoboTwin 2.0、LIBERO-Plus 等世界-动作基准的具体数值与对照设置

### 35. TacPAC: Tactile Prediction and Real-Time Action Correction in World-Action Models for Contact-Rich Manipulation — 👀 值得关注

- **时间：** 2026-09-04（[arXiv](https://arxiv.org/abs/2609.05266)）
- **评分：** C4（把触觉预测转化为执行期基于预期的实时修正，对触觉 WAM 子方向有清晰增量） / E4（五个真机任务各 20 次、六个外部基线与逐路径消融，但仅单一平台） / O3（仓库含模型、训练与部署代码（MIT），权重与数据集仍在准备中） / T3（复旦张力团队，具身方向积累信息有限，按默认值） = **71/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** School of Data Science, Fudan University；Shanghai Innovation Institute；NeoteAI
- **分类：** `manipulation` · 核心 · model
- **核心内容：** 为解决以视觉为主的世界-动作模型难以捕捉决定接触密集操作成败的局部接触信息，且把触觉当作额外视角预测只能拿到约三分之一收益（预测发生在执行前、触觉反馈在执行中到达）的问题，作者提出 TacPAC：基础模型以视频专家预测未来视觉与触觉、动作专家据此规划动作块；规划完成后缓存预测的接触与计划自身的逐层注意力状态，由触觉专家把每帧新触觉图像与缓存对照，为尚未执行的步骤输出增量修正，单次修正比重新生成动作块便宜 20.7 倍。在 Flexiv 机械臂加双 InTac 触觉传感器的五个任务（插充电头、转移水果、拿薯片、扶正空瓶、插扩展卡，每法每任务 20 次）上，作者报告 TacPAC 在全部任务领先，平均 64%，比最强基线 T-Rex 高 16 点；消融显示去掉缓存访问即降到 47%。该结果提示「对照预期读触觉」是闭环接触操作的有效途径，但仅单一平台与传感器，数据与权重尚未公开。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/LogosRoboticsGroup/TacPAC)；权重 none，数据 none，许可 MIT。探测链接多了句号导致失效；实际仓库含模型、训练、预处理与部署代码，README 称数据与检查点待发布
- **待核验事项：** 跟踪检查点与数据集是否按 README 承诺发布

### 36. ADEPT: Accelerating Dexterity via Pre-Training and Post-Training using Reinforcement Learning — 👀 值得关注

- **时间：** 2026-08-19（[arXiv](https://arxiv.org/abs/2608.19182)）
- **评分：** C4（系统化的灵巧RL预训练-后训练范式与稳定迁移配方，对高自由度sim-to-real方向有明确增量。） / E4（仿真消融、从零训练与直接微调对比，两种本体真机分阶段成功率与视触觉对比，下游任务数较少。） / O2（仅项目页，未见代码仓库。） / T5（NVIDIA西雅图机器人实验室（Handa、Ratliff、Van Wyk）与密歇根Fazeli在灵巧sim-to-real方向有多项标志性成果。） = **71/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** NVIDIA Corporation；Robotics Department, University of Michigan
- **分类：** `sim2real` · 核心 · method
- **核心内容：** 为避免多指灵巧手每个新任务都从零用RL重新发现抓取、提起、手内重定向等基础技能，作者提出ADEPT：先在16种随机尺度基本形状的物体摆位任务上用PPO+ADR+PBT大规模预训练，再迁移到下游接触丰富任务；针对直接PPO微调会迅速遗忘预训练行为的问题，采用BC演员蒸馏、冻结演员的评论家预热与保守学习率/裁剪的PPO；用关节空间几何织物（Geometric Fabric）约束关节极限与碰撞；最后用DAgger蒸馏为双目RGB或RGB+五指触觉学生策略零样本上真机。作者报告预训练策略可零样本完成下游任务的摆位阶段，直接微调会使成功率跌至零而ADEPT稳定提升，并在23自由度Kuka-Allegro上完成FMB星形与方圆插销及碗碟上架、在29自由度Flexiv-Sharpa上完成FMB插销，触觉学生优于纯视觉学生。结果提示RL预训练可作为灵巧操作的可复用先验，但下游任务数量有限，每任务仍需数十亿步后训练，感知遮挡仍是主要失败来源。
- **发表状态（核验：2026-10-22）：** CoRL 2026
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 未找到官方仓库链接，无仓库链接；权重 none，数据 n/a，许可 unknown。论文仅给项目页。
- **待核验事项：** 项目页 https://adept-dexterity.github.io/ 是否提供代码

### 37. Hydra-0: Action Flow for Generalist World Modeling and Control — 👀 值得关注

- **时间：** 2026-08-18（[arXiv](https://arxiv.org/abs/2608.18077)）
- **评分：** C4（用像素动作流统一跨本体世界模型条件并兼顾策略评测与反向控制，对世界模型子方向有明确增量。） / E4（五个验证集、多骨干对比、数据效率曲线与RoboLab相关性分析较完整，但真机控制仅定性单任务。） / O2（项目页代码标注coming soon，暂无权重与代码。） / T5（NVIDIA Isaac团队与Yilun Du、Yunzhu Li、Konidaris等在世界模型与机器人学习方向有多项标志性成果。） = **71/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** NVIDIA；Brown University；Columbia University；Harvard University
- **分类：** `world-model` · 核心 · model
- **核心内容：** 为解决动作条件视频世界模型依赖关节或末端指令、难以跨本体迁移的问题，作者提出Hydra-0：把机器人指令经控制器与相机标定投影为图像平面上的可见点轨迹（action flow），作为视频生成的统一条件；在DROID、ABC-130k、EgoDex等七个来源约2200小时（以可变形物体交互为主）的数据上做多本体中训练，并在Cosmos 2.5与Wan2.2多个骨干上实现，结合自回归转换与DMD2蒸馏加速推理。作者报告：最佳配置相对Cosmos 2.5原生动作条件基线，机器人运动误差降低90.4%、物体运动误差降低60.2%；在IWS六个任务上中训练模型零样本与少数据适配更好；在RoboLab五个策略×六任务开环回放中，生成成功率与参考成功率Pearson r=0.96；反向模式可由人类示范的物体流推断机器人动作。结果提示动作流是连接异构数据、策略评测与控制的有效接口，但真机控制仅有单一弯管任务的定性展示，开环评测不等于闭环仿真，代码尚未发布。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 未找到官方仓库链接，无仓库链接；权重 none，数据 n/a，许可 unknown。探针误取ModelTC/LightX2V（论文使用的第三方推理库）；官方项目页 https://nvidia-isaac.github.io/video_to_data/hydra-0/ 代码标注coming soon。
- **数据/基准关系：** droid（预训练）
- **待核验事项：** 代码与权重是否按项目页承诺发布

### 38. World Tokens: Enhancing Embodied Policies with Training-Time World Modeling — 👀 值得关注

- **时间：** 2026-08-10（[arXiv](https://arxiv.org/abs/2608.09730)）
- **评分：** C3（用排他路由的共享瓶颈让训练期视频监督作用于控制表征，设计清晰，属 WAM/VLA 融合的方法增量。） / E4（LIBERO、SIMPLER 两平台与 R1 Pro 真机，含匹配基线与逐因素机制消融。） / O4（仓库含实质代码（MIT），HF 发布 LIBERO 与 CALVIN 权重。） / T3（中国移动九天研究院与中关村学院，具身方向可核实积累有限，按默认 3 分。） = **71/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** JIUTIAN Research；Zhongguancun Academy
- **分类：** `vla` · 核心 · method
- **核心内容：** 为在不承担在线视频生成开销的前提下让 VLA 获得世界模型带来的动力学表征，作者提出 World Tokens：Perceiver 式 World Adapter 将 Qwen3-VL-2B 的多模态特征映射为固定数量的 world tokens，它们既作为联合微调的 Cosmos Predict2.5-2B 视频去噪器的条件（首帧用 Canny 边缘图而非 RGB，以抑制外观捷径），又是流匹配动作专家唯一的视觉-语言上下文（排他路由，防止绕过）；部署时整个视频分支被移除。作者报告：无具身动作预训练时 LIBERO 平均 98.2%，Long 套件 97.0%，每个动作块 61.85 ms，与 π0.5 相近；消融显示允许绕过 VLM、改用 FFN 适配器或 RGB 锚帧都会使 Long 降到 94% 以下；SIMPLER 视觉匹配 WidowX 平均 71.5%、Google Robot 82.1%；Galaxea R1 Pro 真机放水果 96 次试验成功率 76.0%，对照同骨干 Qwen-GR00T 为 59.4%。该结果提示训练期世界建模经共享瓶颈可直接塑造控制表征，但收益主要体现在 LIBERO-Long 与 SIMPLER，真机仅单一放置任务族，且与带具身预训练模型相比仍有差距。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/kzz1031/SLIM)；权重 open，数据 n/a，许可 MIT。项目页 slim-project-page 对应该仓库（项目原名 SLIM）；探测到 48 个代码文件及 HF 权重 SLIM-LIBERO、SLIM-CALVIN。
- **数据/基准关系：** libero（微调/后训练）、libero（评测）、simplerenv（评测）、bridgedata-v2（微调/后训练）
- **待核验事项：** 作者团队在具身策略方向的既往成果

### 39. Robots Acquire Manipulation Skills in Seconds from a Single Human Video — 👀 值得关注

- **时间：** 2026-07-22（[arXiv](https://arxiv.org/abs/2607.20033)）
- **评分：** C4（把技能获取从训练循环移到推理期、并以进度流形对齐驱动预测，是单视频模仿方向的明确方法增量。） / E4（50 个真机新任务、OSVI 与 VLA 基线、数据/时间效率、遗忘、扰动鲁棒性与逐级消融较完整，但限于单一平台。） / O3（仓库含实质代码，HF 已放出权重，但未找到许可证文件；训练用人类视频数据未见开放。） / T3（北理工与自变量机器人（X Square）、清华在机器人学习上有一定相关成果。） = **71/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Beijing Institute of Technology；X Square Robot；Tsinghua University
- **分类：** `manipulation` · 核心 · method
- **核心内容：** 为解决机器人学习新技能依赖采集示教加离线微调、成本高且会侵蚀已掌握技能的问题，HOST 将技能获取移到推理时：先把机器人轨迹与人类视频映射到共享的任务进度流形上，把预测目标重新定义为与视频未来进度对齐，再以单个自回归模型级联完成“定位当前进度—预测机器人自身未来观测—由预测观测导出动作”。训练分两阶段：19.3 万条、229 个任务的同本体机器人对用于预训练，5,847 条自采人类视频与机器人轨迹配对用于适配。作者在双 ARX R5 臂平台上报告：50 个新任务每任务 20 次试验，平均成功率 62%，比零样本 Wall-OSS 等基线高 45 个百分点，比同样接收视频的 OSVI 基线高 43 个百分点，超过用 50 条示教 LoRA 微调的最强基线，且旧技能成功率不下降，对光照、物体替换和人为干扰较鲁棒。该结果提示“示范驱动预测”可显著降低新技能获取成本，但“单视频”仅在推理期成立，训练仍需大量同本体数据和人-机配对，且只在单一双臂平台上验证。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/CGuangyan-BIT/HOST)；权重 open，数据 unknown，许可 unknown。HF 有 Guangyan/HOST 权重；仓库未检测到许可证文件。
- **待核验事项：** 仓库未检测到许可证，需确认使用条款；确认 5,847 条人类视频配对数据是否计划开放

### 40. Masked Visual Actions for Unified World Modeling — 👀 值得关注

- **时间：** 2026-07-21（[arXiv](https://arxiv.org/abs/2607.19343)）
- **评分：** C4（统一前向/逆向的像素空间动作接口是清晰的表示层增量，可能影响视频世界模型的动作条件化方式。） / E4（两个数据集上与多基线对比、条件信号消融、未见本体泛化，并覆盖仿真与真机的策略评估、规划与逆向建模。） / O2（未找到官方代码仓库，仅有项目页，论文称将发布代码、数据与权重。） / T5（Stanford（李飞飞、吴佳俊、Wetzstein 等）与 Harvard（Yilun Du）团队在具身与生成建模方向有多项标志性成果。） = **71/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Stanford University；University of Maryland, College Park；Harvard University
- **分类：** `world-model` · 核心 · method
- **核心内容：** 为解决视频模型难以接收与其视觉先验对齐、又不依赖特定本体的动作信号这一问题，作者提出 Masked Visual Actions：把动作表示为视频中某个实体（机器人或物体）被部分揭示的时空掩膜轨迹。揭示机器人运动时模型充当前向动力学模型，揭示期望的物体运动时则反推机器人行为。方法以 Wan-Fun-Control 2.2 14B 为基座做 LoRA 微调，仅用约 15 小时 DROID 真实数据与 RoboCasa 仿真数据（分割与渲染两种掩膜构造）。作者报告在 DROID 上 LPIPS/SSIM/PSNR 为 0.0945/0.887/23.74，明显优于 Ctrl-World 等基线；在未见过的 BEHAVIOR 双臂本体和自制夹爪上仍可泛化；在 RoboCasa 与真机上想象 rollout 的成功趋势与真实执行相关，用于 Diffusion Policy 候选排序可提升成功率，逆向建模也能恢复有竞争力的动作。该结果提示像素对齐的动作接口有助于跨本体世界建模，但模型学到的是相关而非因果，推理速度受 14B 基座限制，规划与评估依赖 VLM 判分。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 未找到官方仓库链接，无仓库链接；权重 none，数据 none，许可 unknown。仅有项目页 masked-visual-actions.github.io；附录称将发布代码、数据与权重，当前未见仓库。
- **数据/基准关系：** droid（微调/后训练）、robocasa（微调/后训练）、robocasa-bench（评测）、behavior-1k（评测）
- **待核验事项：** 确认代码、权重与掩膜数据是否已按承诺发布

### 41. T-Rex: Tactile-Reactive Dexterous Manipulation — 👀 值得关注

- **时间：** 2026-06-15（[arXiv](https://arxiv.org/abs/2606.17055)）
- **评分：** C4（大规模触觉灵巧数据集加异步触觉专家架构，对触觉 VLA 子方向有明确的方法与资源增量。） / E4（12 项真机任务、6 个基线、模态与架构及训练阶段消融较完整，但为单一平台。） / O2（论文称数据集开源，但未找到官方仓库或数据链接；探测到的 Isaac-GR00T 并非本文代码。） / T5（Trevor Darrell、Jitendra Malik、Pieter Abbeel、李飞飞与 NVIDIA GEAR 等为公认领先团队。） = **71/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** UC Berkeley；NVIDIA；Stanford；Panasonic；La Sapienza University；ItalAI
- **分类：** `vla` · 核心 · model
- **核心内容：** 为让 VLA 具备对触觉信号的快速反应能力，作者同时补数据和架构两方面短板：一是采集 100 小时、200 多种物体、22 类运动基元的触觉同步双臂灵巧遥操作数据集，用于"中训练"；二是提出 T-Rex 模型，以 Mixture-of-Transformers 包含预测未来视觉潜变量的 latent expert、低频去噪的 action expert 与高频触觉 refinement 的 tactile expert，在固定时间步切分流匹配轨迹实现异步级联去噪，并用时序 VQ-VAE 编码指尖力历史。训练分三阶段：沿用 EgoScale 的 2.2 万小时人类第一视角视频预训练、触觉中训练、约 100 条示教的任务后训练。在 Dexmate Vega-1 双臂加 Sharpa 22 自由度手上的 12 项任务（每项 16 次）中，作者报告平均成功率 65%，最强基线 EgoScale 为 35%；消融显示去掉触觉降 23 个百分点，中训练显著提升低数据下表现。该结果提示触觉中训练与高频细化可有效增强灵巧 VLA，但依赖特定硬件，评测为单平台，数据开源情况尚待核实。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 未找到官方仓库链接，无仓库链接；权重 none，数据 unknown，许可 unknown。探测误把 Nvidia/Isaac-GR00T 当作官方仓库；仅项目页 https://tactile-rex.github.io/，论文称数据集开源但未给出链接。
- **待核验事项：** 100 小时 T-Rex 数据集的实际发布位置与许可；是否发布代码与模型权重

### 42. LadderMan: Learning Humanoid Perceptive Ladder Climbing — 👀 值得关注

- **时间：** 2026-06-04（[arXiv](https://arxiv.org/abs/2606.05873)）
- **评分：** C4（首个系统性学习型人形感知爬梯并支持梯上作业的工作，混合跟踪+蒸馏+深度基础模型的组合对极限人形任务有示范意义。） / E4（仿真大网格评测、对无感知基线、专家学习与 sim2real 组件的真机消融（各 10 次）、与 TWIST2 及人类速度对比。） / O2（仅有项目页 ladderman-robot.github.io；探测到的 NVIDIA/warp 只是所用渲染工具，非官方仓库。） / T5（Amazon FAR 与 Abbeel、Sreenath、Karen Liu、石冠亚等是人形学习控制方向公认领先团队。） = **71/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Amazon FAR；USC；UC Berkeley；Stanford University；CMU
- **分类：** `locomotion` · 核心 · method
- **核心内容：** 为解决人形爬梯中立足点与扶手点稀疏、全身多接触协调困难、对感知与控制误差极敏感，而以往方法多为无感知的模型控制且难泛化的问题，作者提出 LadderMan：先用“混合运动跟踪”（放松上身跟踪、加入以梯子为中心的接触跟踪与爬升奖励）从单条动捕参考中学习不同倾角与踏棍间距的多个状态专家；再用 DAgger 与 PPO 联合目标把专家蒸馏为以深度图为输入的统一视觉运动策略；部署时用 Fast-FoundationStereo 产生更干净的深度，并在训练中加入只保留踏棍的掩码以弱化扶手等背景差异；梯上作业则用上下身解耦的双智能体策略配合 VR 遥操作。作者报告仿真中在大范围倾角与间距组合上成功率多数超过 95%，而无感知运动跟踪基线峰值仅 49%；真机 Unitree G1 在三种梯子上分别 9/10、6/10、7/10，去掉 RL、深度基础模型或踏棍掩码均显著下降；TWIST2 在梯上作业时易失衡。该结果提示感知+蒸馏可把单一参考扩展到多种梯子，但尚未覆盖垂直梯，作业缺灵巧手，代码未见。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 未找到官方仓库链接，无仓库链接；权重 none，数据 n/a，许可 unknown。修正探测结果：github.com/NVIDIA/warp 为论文引用的深度渲染工具而非本文代码；仅有项目页
- **待核验事项：** 是否发布官方代码

### 43. TAM: Torque Adaptation Module for Robust Motion Transfer in Manipulation — 👀 值得关注

- **时间：** 2026-06-04（[arXiv](https://arxiv.org/abs/2606.06218)）
- **评分：** C4（把动力学适应从策略内部移到力矩接口、可复用于不同策略与动作空间，思路清晰且有实际价值。） / E4（真机三类策略对比在线辨识与 RMA，并有控制器切换、负载、跨机器人仿真和消融；任务数量有限。） / O2（仅有项目网站，未找到官方代码仓库（探测结果为引用的 MuJoCo Menagerie）。） / T5（Dieter Fox、Beomjoon Kim、Florian Shkurti 团队在机器人学习与 sim2real 方向成果突出。） = **71/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** KAIST；Allen Institute for AI；University of Toronto；University of Washington
- **分类：** `sim2real` · 核心 · method
- **核心内容：** 为解决同一策略在不同机器人实例、负载或仿真与真实之间动力学差异导致的运动偏差，而又不想让策略本身做域随机化或为每台机器人重新采集辨识数据，TAM 把适应层下移到力矩接口：历史编码器把关节位置、速度与施加力矩的长时历史（附加以理想模型逆动力学计算的物理残差特征）压缩为潜变量，力矩适配器据此对名义力矩输出残差修正，使目标机器人的局部运动响应匹配理想模型。TAM 不读取策略观测、奖励或动作空间，只用与任务无关的随机关节运动在随机化仿真中训练，先在 Panda、Piper、RBY-1、iiwa14、Rizon4 五种机器人上预训练，再做目标机器人仿真微调，不使用真机数据。作者报告在真实 Franka 上，同一组权重挂在视觉 RL 推箱、BC 翻转与 MPC 球盘平衡策略下方，均优于直接执行、粒子滤波在线辨识和 RMA；切换 OSC 控制器和加负载时末端跟踪误差下降；仿真中对未见过的 Google Robot、Unitree Z1 也降低跟踪误差。局限是需要力矩接口与匹配的运动学结构，只学习一步局部对齐、无长时稳定性保证，接触丰富任务中外力仍可能被误判为本体失配。
- **发表状态（核验：2026-10-22）：** CoRL 2026
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 未找到官方仓库链接，无仓库链接；权重 none，数据 none，许可 unknown。探测到的 google-deepmind/mujoco_menagerie 是论文引用的机器人模型库而非本文代码；仅有项目页 https://dongwon-son.github.io/tam-project-page/ 。
- **待核验事项：** 真机任务成功率具体数值（缓存表格数字缺失）；项目页是否给出代码或权重

### 44. IntentVLA: Short-Horizon Intent Modeling for Aliased Robot Manipulation — 👀 值得关注

- **时间：** 2026-05-14（[arXiv](https://arxiv.org/abs/2605.14712)）
- **评分：** C4（明确界定并基准化“观测混叠导致意图切换”问题，给出历史条件化方案与专门基准，对 VLA 子方向有清晰增量。） / E4（自建基准+三个公开仿真基准+50 次真机试验，基线较强且有组件、历史长度与编码器消融。） / O3（仓库已有部分代码，README 仍写部分内容即将发布，未见权重与许可证。） / T3（中关村学院等多校联合团队，相关积累信息有限，按默认 3 分。） = **71/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Huazhong University of Science and Technology；Zhongguancun Academy；Harbin Institute of Technology；The Hong Kong University of Science and Technology (Guangzhou)；Beihang University；Zhengzhou University；Zhongguancun Institute of Artificial Intelligence；East China Normal University；University of Science and Technology of China；DeepCybo
- **分类：** `vla` · 核心 · method
- **核心内容：** 为解决帧条件 VLA 在部分可观测下，相似观测对应不同短程意图而在相邻重规划步之间来回切换、导致动作块冲突的问题，作者提出 IntentVLA：以 Qwen3-VL 4B 编码当前图像和指令，用冻结的 VGGT-1B 编码近期头部相机历史帧，经门控交叉注意力融合并追加一个紧凑的历史证据 token，作为 DiT flow-matching 动作头的条件；同时在 RoboTwin2 上构建含 12 个任务、匹配训练数据的 AliasBench，专门隔离观测混叠。作者报告在 AliasBench 上平均成功率 45.8%，对比帧条件 Qwen3-VL-GR00T 的 9.0%、最佳直接历史输入变体 28.1% 和 MemoryVLA 14.9%；SimplerEnv WidowX 72.9%、LIBERO 平均 98.6%（Long 97.4%），并在 RoboCasa-GR1 与双臂 Franka 真机收零食任务（每模型 50 次）上优于 π0.5、MemoryVLA；消融表明历史融合与意图 token 均有贡献。结果提示短窗口历史能有效缓解局部混叠，但仅针对短程歧义，双手和多目标任务仍偏弱，部分任务（如放勺子）略有下降，仓库仍标注部分内容即将发布。
- **发表状态（核验：2026-10-22）：** EMNLP 2026
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 部分开放，[仓库](https://github.com/ZGC-EmbodyAI/IntentVLA)；权重 unknown，数据 unknown，许可 none-found。探测为 13 个代码文件且 README 含 coming soon。
- **数据/基准关系：** aliasbench（提出）、simplerenv（评测）、libero（评测）
- **待核验事项：** 仓库中 AliasBench 数据与训练代码的实际完整度、许可证；团队在 VLA 方向的既往成果

### 45. iMaC: Translating Actions into Motion and Contact Images for Embodied World Models — 👀 值得关注

- **时间：** 2026-06-08（[arXiv](https://arxiv.org/abs/2606.09813)）
- **评分：** C4（用运动与接触图像作为显式动作控制，对具身世界模型的动作条件化方式有明确增量。） / E3（八项真机任务、两个基线和策略排序相关性分析，但基线少、消融以定性为主且每任务单独微调。） / O3（官方仓库含大量代码，但未确认权重与许可证。） / T4（清华鲁继文团队与极佳科技在具身世界模型方向有多项可核实成果。） = **69/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** GigaAI；Tsinghua University；Nanyang Technological University；Beijing University of Posts and Telecommunications
- **分类：** `world-model` · 核心 · method
- **核心内容：** 动作条件视频世界模型常把未来动作编码为紧凑向量再经注意力或调制注入，模型需要间接推断厘米级动作差异对接触与物体运动的影响，这限制了其作为策略评估器的可靠性。iMaC 基于 WAN2.2 图生视频 DiT，把未来关节动作经 URDF 与正运动学渲染为三视角机器人运动图像，同时联合预测彩色化深度，并用预测深度构建的点云生成当前场景与未来机器人之间的双流距离热力图（接触图像），作为稠密图像式控制；训练时采用多块连续展开以缓解自回归生成的暴露偏差，支持分钟级生成。作者在八项真机长时程操作任务上报告：相对 Ctrl-World 与 ABot-PhysWorld，FID、PSNR、SSIM、FVD 等视频指标更优；以 π 系列与 GigaBrain-0.5 各三个训练检查点做闭环评估，六项任务中世界模型成功率与真机成功率强正相关，两项因相机看不到关键高度关系而相关较弱；定性消融显示运动图像与接触图像缺一不可。结果提示空间显式的动作控制能提升世界模型对动作的响应，但每任务需单独微调模型、依赖估计深度精度，消融主要是定性对比。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/imac-wm/iMac)；权重 unknown，数据 unknown，许可 unknown。仓库探测为实质代码（271 个代码文件），未找到许可证；缓存元数据中的摘要为旧版本，正文以 v1 HTML 为准。
- **待核验事项：** 是否发布模型权重；仓库许可证；HF 数据集 CVPR-2026-WorldModel-Track-Dataset 与本文训练数据的关系

### 46. WALL-SS: Scaling Long-horizon World Models via Next-Scale Autoregression — 👀 值得关注

- **时间：** 2026-08-26（[arXiv](https://arxiv.org/abs/2608.26239)）
- **评分：** C4（把逐尺度自回归、尺度记忆与在线对齐统一到动作条件世界模型，对长程机器人仿真有明确增量） / E4（视频质量对比、长程消融、反事实动作与 600 对闭环一致性评估，但缺少机器人世界模型专门基线） / O2（官方仓库仅含项目页与 PDF，README 列训练/推理代码为待办） / T4（自变量机器人发布过 WALL-OSS 等模型，有可核实的具身基础模型产出） = **68/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** X Square Robot
- **分类：** `world-model` · 核心 · model
- **核心内容：** 为让生成式世界模型从片段级预测走向可变长度、可流式延展且可做奖励优化的统一机器人轨迹模型，自变量机器人提出 WALL-SS：以 InfinityStar 初始化，把观测与动作交错成因果序列，每帧由粗到细逐尺度生成；在各尺度注入对齐的动作表示，近期历史保留细尺度、远期压缩为粗尺度以控制记忆，并用尺度级 dream forcing 适应自生成上下文；最后把视觉生成视作策略，以动作跟随和长期一致性奖励做在线对齐。训练数据包括完整 AgiBot World Beta、ManipArena、私有 X2 机器人与 UMI 数据以及干预/失败恢复轨迹。作者报告其在交互质量、指令跟随和轨迹精度上优于 Wan2.1/2.2、Infinity 等视频生成基线，60 秒推演中 PSNR、FID、FVD 持续更好，并用 30 个任务-检查点单元和 600 对配对回放检验与真机成功率的校准与排序一致性。该结果提示逐尺度自回归可作为长程机器人世界模型的可行路线，但对比对象多为通用视频模型，大量依赖私有数据，代码与权重尚未发布。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 找到仓库但未发现实质相关代码，[仓库](https://github.com/X-Square-Robot/wall-ss)；权重 none，数据 none，许可 MIT。探测到的 Wan2.2 仓库非本文官方仓库；官方仓库 README 称目前只有项目页，代码列为待发布
- **数据/基准关系：** agibot-world（预训练）
- **待核验事项：** 跟踪 X-Square-Robot/wall-ss 是否发布训练与推理代码及权重

### 47. HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent RL — 👀 值得关注

- **时间：** 2026-08-17（[arXiv](https://arxiv.org/abs/2608.16837)）
- **评分：** C4（分层动作流与谱潜空间 RL 共同提供把通用 VLA 迁移到人形全身移动操作的低成本路线，对人形 VLA 子方向有明确增量。） / E4（7 项真机任务对比 4 个强基线，含去噪结构消融、分布外扰动和真机 RL 实验，但每项仅 10 次试验。） / O2（仅有项目页 grange007.github.io/HAF；探测到的 tau-0-vla 仓库属于其他论文。） / T4（北大张尚彤团队与北京人形机器人创新中心在 VLA 与人形方向有多项可核实工作。） = **68/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Peking University；Beijing Innovation Center of Humanoid Robotics；Nankai University
- **分类：** `vla` · 核心 · method
- **核心内容：** 通用 VLA 单阶段生成全身动作，难以协调人形机器人的行走、腰部姿态与双臂操作，而直接用在线 RL 微调大骨干又昂贵且危险。HAF 包含两部分：HAF-VLA 基于预训练流匹配 VLA（π0.5），按运动学依赖依次生成行走与头部、腰部、双臂动作，用阶段嵌入和跨阶段 KV cache 传递前一阶段的干净动作；HAF-Steer 利用流匹配可逆性把示教动作反推为初始噪声，经 DCT 压缩到低维谱空间，先行为克隆再做离线-在线混合 SAC，骨干保持冻结。在天工 2.0/3.0 人形机器人 7 项长程家务任务（每项 10 次）上，作者报告 HAF-VLA 平均归一化得分 70.5%，最强基线为 53.3%，对比 GR00T N1.7、Cosmos Policy、ACT；消融显示增益并非来自更多去噪步数；HAF-Steer 在分布内外设置下均提升成功次数，而 DSRL 出现不安全探索。但每项仅 10 次试验，任务与数据为自采，代码未见公开。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 未找到官方仓库链接，无仓库链接；权重 unknown，数据 unknown，许可 unknown。探测到的 sii-research/tau-0-vla 是 τ0-VLA 的仓库，与本文无关；官方项目页 https://grange007.github.io/HAF
- **待核验事项：** 项目页是否发布 HAF 代码或权重

### 48. G0.5: One Autoregressive Stream for Robot Reasoning and Action — 👀 值得关注

- **时间：** 2026-08-12（[arXiv](https://arxiv.org/abs/2608.11739)）
- **评分：** C4（将 AR 动作分词、原生思维链与视觉记忆整合为可扩展的基础 VLA，对 VLM-as-actor 路线有明确推进。） / E4（覆盖七类评测（真机微调、BEHAVIOR、DROID 零样本、三个仿真基准、语言跟随基准）并有推理流消融；真机任务多为自建。） / O2（目前只核实到项目页（OpenGalaxea/G05 为网页仓库）；探针给出的 openvla-mini 并非本文仓库。） / T4（星海图（Galaxea）此前发布 G0 模型与 Open-Galaxea 数据集，在具身基础模型方向有可核实积累。） = **68/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Galaxea Team
- **分类：** `vla` · 核心 · model
- **核心内容：** 主流 VLA 将 VLM 作为条件编码器、另接流匹配动作专家，VLM 的推理能力只能间接影响动作。为让 VLM 本身成为决策者，作者提出 G0.5：以 Qwen3.5-2B 初始化，一个自回归解码器在同一 token 流中生成可选的思维链（子任务分解、物体框、动作提示）与动作码；动作由按运动部件分组、带时间对比目标的 RVQ 分词器编码到 27 维统一动作空间，只预测活动自由度组以压缩 token；视觉编码器中插入时空注意力实现多秒视觉记忆。在 14 种具身的机器人数据与 VQA 数据上单阶段预训练后，作者报告：R1-Lite/R1-Pro 六个真机任务-具身设置平均 76.7%（π0.5 为 53.3%）；2025 BEHAVIOR 挑战 50 任务单一策略 31.4%；DROID 后训练并在未见环境与物体上零样本 82.5%；LIBERO 98.9%、RoboTwin 2.0 93.3%、SimplerEnv-Bridge 87.3%，并对 AR 与流匹配头、思维链开关做了对比。结果提示自回归 VLA 在合适分词下仍具竞争力，但多数真机任务由作者自建，跨方法比较的条件不尽相同，代码与权重的开放情况尚未核实。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 找到仓库但未发现实质相关代码，[仓库](https://github.com/OpenGalaxea/G05)；权重 unknown，数据 unknown，许可 unknown。探针误配到 Stanford-ILIAD/openvla-mini（第三方仓库），已更正；OpenGalaxea/G05 为 TypeScript 项目页仓库，未见 G0.5 代码（2026-10-22 核对）。
- **数据/基准关系：** droid（微调/后训练）、bridgedata-v2（微调/后训练）、libero（评测）、simplerenv（评测）、behavior-1k（评测）
- **待核验事项：** OpenGalaxea/GalaxeaVLA 是否包含 G0.5 代码或权重

### 49. RL$^2$-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling for Vision-Language-Action Models — 👀 值得关注

- **时间：** 2026-07-29（[arXiv](https://arxiv.org/abs/2607.26991)）
- **评分：** C3（将离线 RL 潜变量引导与失败触发的自适应测试时扩展结合，是推理期改进 VLA 的扎实方法增量。） / E4（覆盖 SIMPLER 域内/分布外、PolaRiS 与真机，三种 VLA 与两类验证器，含消融与缩放分析。） / O3（官方仓库已含 SIMPLER 评测与数据准备脚本（Apache-2.0），PolaRiS 部分仍在待办，权重可用性未核实。） / T4（通讯作者 Sartoretti 课题组在多机器人学习与机器人 RL 方向有可核实积累。） = **68/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** National University of Singapore；University of Toronto；Singapore Technologies Engineering
- **分类：** `vla` · 核心 · method
- **核心内容：** 为缓解测试时扩展方法中候选动作都来自同一 VLA、继承相关失败模式，且对每一步都施加同样干预的问题，作者提出 RL²：先在 BridgeV2、DROID 上提取 VLA 动作专家潜变量，训练轻量离线 RL 流匹配策略（QAM，OpenVLA 场景用 V-GPS 的 CQL 策略），推理时把其速度场与冻结 VLA 的速度场加权组合以增加动作多样性；并基于“引导在失败状态有益、在成功状态有害”的缩放分析，用 SAFE 失败检测器仅在预测失败时启用引导，再由 RoboMonkey/CoVer 验证器选动作。作者报告：SIMPLER 域内任务上 OpenVLA 平均比重复采样基线高 7.5%；π0 在 SIMPLER 分布外指令下平均高 10.1%、分布外环境高 8.5%；π0.5 在 PolaRiS 分布外指令三任务平均成功率由 31.8% 提至 42.7%；PiperX 真机四任务平均比改写基线高 17.5%，消融支持潜变量与 RL 训练的作用。该结果提示“何时引导”与“如何引导”可模块化叠加于现有 VLA，但依赖外部验证器与按任务训练的失败检测器，计算开销与对新任务的迁移仍需评估。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 部分开放，[仓库](https://github.com/marmotlab/RL2-VLA)；权重 unknown，数据 n/a，许可 Apache-2.0。探测漏掉了项目页链接的官方仓库；README 显示已发布 SIMPLER 评测与 SAFE/QAM 数据准备脚本，PolaRiS 版本在待办列表中。
- **数据/基准关系：** simplerenv（评测）、bridgedata-v2（微调/后训练）、droid（微调/后训练）
- **待核验事项：** HuggingFace rl2-vla 组织下的模型权重是否实际可下载

### 50. Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System — 👀 值得关注

- **时间：** 2026-06-16（[arXiv](https://arxiv.org/abs/2606.18112)）
- **评分：** C4（将多任务导航重构为可配置观测上下文建模并面向智能体调用，覆盖室内导航到自动驾驶，对导航基础模型子方向有明确增量。） / E4（覆盖 VLN-CE、VLNVerse、VLN-PE、HM3D/OVON、EVT-Bench、EQA、NAVSIM、AlpaSim 等多基准并有消融、扩展曲线与 Go2 真机部署。） / O2（官方仓库仅 4 个文件、无代码，权重与训练数据未公开。） / T4（Qwen 团队及作者中 NaVid/NavFoM 系列作者在 VLM 与具身导航方向积累可核实。） = **68/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Qwen Team
- **分类：** `navigation` · 核心 · model
- **核心内容：** 为让同一导航模型在指令跟随、目标搜索、目标跟踪和自动驾驶间按需切换观测策略，Qwen 团队提出 Qwen-RobotNav：在 Qwen3-VL 上加轻量 MLP 轨迹头，以统一航点预测形式建模所有任务，并开放任务模式与 token 预算、时间衰减、相机权重、帧采样方式等参数，训练时对这些参数全部随机化；训练数据 15.6M 样本，含仿真轨迹、文生视频自动合成的导航数据与约 15% 视觉语言数据。作者报告在 VLN-CE RxR、EVT-Bench、NAVSIM 等基准取得最优或可比结果，作为上层规划器调用模块时在 HM-EQA 与 EXPRESS-Bench 上比此前最好方法分别提升 10.8% 与 15.4% 且导航步数减少 77%，并在 Unitree Go2 上做了零样本真机部署和 2B→8B 扩展分析。该结果提示“可配置观测上下文”是多任务导航基础模型的有效接口，但目前仓库仅有 README，权重与数据未开放，跨基准数字条件各异不宜横比。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 找到仓库但未发现实质相关代码，[仓库](https://github.com/QwenLM/Qwen-RobotNav)；权重 none，数据 none，许可 none-found。仓库仅含 README 等 4 个文件，无代码。
- **待核验事项：** 论文未在 HTML 中列出具体机构，需核对 PDF 署名（Qwen Team 之外是否有合作单位）；仓库是否后续发布模型权重

### 51. Qwen-VLA: Alibaba's Embodied Foundation Model — 👀 值得关注

- **时间：** 2026-05-28（[arXiv](https://arxiv.org/abs/2605.30280)）
- **评分：** C4（把操作、导航、轨迹预测统一到一个 VLA 并给出完整分阶段训练配方，属基础模型级工作，但架构组件多为已有技术组合。） / E4（覆盖 6+ 个仿真基准、真机 ALOHA、OOD 测试与多项消融；基线数字多引自原文，真机平台单一。） / O2（官方仓库仅 README 与图片，未见代码、权重或许可证。） / T4（Qwen 团队在多模态基础模型上产出显著，具身方向的可核实积累相对较新。） = **68/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Qwen Team
- **分类：** `vla` · 核心 · model
- **核心内容：** 为缓解具身模型按任务（操作、导航）和本体各自训练导致能力割裂、跨本体泛化差的问题，Qwen 团队提出 Qwen-VLA：以 Qwen3.5-4B 原生多模态模型为骨干，接约 1.15B 参数的 DiT flow-matching 动作专家，用“本体感知提示词”声明机器人平台与控制约定，把操作、视觉语言导航和人类第一视角轨迹统一为动作/轨迹预测。训练分四阶段：仅文本到动作预训练、联合持续预训练（真实机器人数据约占 74%，含 AgiBot World、DROID、BridgeData V2 等）、多任务 SFT 和基于仿真回报的 PPO 强化学习。作者报告单一 Instruct 模型在 LIBERO 97.9%、Simpler-WidowX 73.7%、RoboCasa-GR1 56.7%、RoboTwin 2.0 Easy/Hard 86.1/87.2%，R2R OSR 69.0%、RxR SR 59.6%，ALOHA 真机 OOD 平均 76.9%，DOMINO 零样本 26.6%，并有 T2A、视觉语言共训练等消融。结果提示统一的多任务多本体预训练可在多个基准上与专用模型相当或更好，但对比基线多为各自报告数字，真机只覆盖 ALOHA，且目前仓库无代码和权重。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 找到仓库但未发现实质相关代码，[仓库](https://github.com/QwenLM/Qwen-VLA)；权重 none，数据 none，许可 none-found。2026-10-22 核对：仓库仅 README 与 assets 图片，无代码和权重链接。
- **数据/基准关系：** agibot-world（预训练）、droid（预训练）、bridgedata-v2（预训练）、libero（评测）、simplerenv（评测）
- **待核验事项：** 是否发布模型权重与训练/推理代码及其许可证；论文署名完整单位（arXiv HTML 仅显示 Qwen Team）

### 52. BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action Framework for 3D Manipulation — 👀 值得关注

- **时间：** 2026-08-05（[arXiv](https://arxiv.org/abs/2608.05042)）
- **评分：** C3（在已有 BridgeVLA 上增加时空记忆，增量明确但属于前作扩展。） / E5（RLBench、COLOSSEUM、GemBench、RMBench、MemoryBench 五个基准加两种真机平台与记忆消融，覆盖面广。） / O2（论文仅给出项目页，未找到 BridgeVLA++ 的代码或权重。） / T4（中科院自动化所与字节 Seed 团队在 3D 操作与 VLA 方向有多项可核实成果。） = **67/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** New Laboratory of Pattern Recognition (NLPR), Institute of Automation, Chinese Academy of Sciences；School of Artificial Intelligence, University of Chinese Academy of Sciences；FiveAges；ByteDance Seed
- **分类：** `vla` · 核心 · method
- **核心内容：** 为解决 3D VLA 数据需求大、分布偏移下泛化弱、且缺少对历史观测记忆的问题，作者在前作 BridgeVLA（点云投影为三视图正交图像、以 2D 热力图预测动作并用 RoboPoint 检测数据做热力图预训练）基础上提出 BridgeVLA++：粗阶段加入由初始锚视图、近邻关键帧和自适应选择的子目标关键帧构成的时序记忆，细阶段保存初始点云并按当前缩放区域重渲染作为抗遮挡空间记忆，二者以轻量注意力模块注入，并可共享给双臂各自的动作头。作者报告：在 RLBench 18 任务、COLOSSEUM 扰动和 GemBench 四级泛化上保持强表现；在记忆依赖的双臂 RMBench 九任务与 MemoryBench 上取得表中最优；Franka 真机 13 任务每任务 10 条演示即可学习并在多种视觉扰动下保持优势，Dobot 平台上记忆任务明显优于无记忆版本，消融显示两种记忆互补。该结果提示热力图对齐与显式记忆可兼得，但方法仍基于关键帧与运动规划器，增量主要是对前作的扩展，代码是否发布尚未确认。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 未找到官方仓库链接，无仓库链接；权重 unknown，数据 n/a，许可 unknown。仅有项目页 https://bridgevla-plus.github.io/；前作 BridgeVLA 的开源情况不计入本文。
- **数据/基准关系：** rlbench（微调/后训练）、rlbench（评测）
- **待核验事项：** BridgeVLA++ 代码与权重是否会并入前作仓库发布

### 53. Pre-training Visual Dexterity in Simulation — 👀 值得关注

- **时间：** 2026-08-16（[arXiv](https://arxiv.org/abs/2608.15917)）
- **评分：** C4（以本体一致的仿真 VR 遥操作数据为灵巧手预训练源，并系统研究历史条件与动作块长度，对灵巧操作数据扩展有明确增量。） / E3（5 项真机任务、每项 20 次试验并有历史/动作块消融，但只与从零训练比较，缺少与其他预训练数据源的对照，泛化测试有限。） / O2（仅见项目页 spd.bot；探测到的 mink 仓库是依赖库而非本文代码，数据集与权重是否公开未确认。） / T5（Chelsea Finn、Phillip Isola、C. Karen Liu 团队在机器人学习与灵巧操作方向有多项标志性成果。） = **66/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Stanford University；MIT；Scale AI
- **分类：** `manipulation` · 核心 · method
- **核心内容：** 为缓解多指灵巧手真机遥操作数据昂贵、人手视频存在本体差异和重定向误差的问题，作者提出 SPD：操作者戴 VR 头显在 MuJoCo 中直接操控与真机对齐的双臂 + 双 22 自由度灵巧手（相机布局、物体相近），5 名操作者一周采集约 75 小时、1,930 条多任务示教（spd-75h），用于预训练一个 2.22 亿参数、以视觉-本体历史为条件的因果扩散 Transformer，再在每个真机任务上用 1–2 小时示教全量微调。在挂盘、挂杯、Jenga、叠杯、投瓶 5 项真机任务（每检查点 20 次试验）上，作者报告预训练模型在各阶段完成率和平均任务进度上都高于同架构从零训练的 BC；消融显示 32 步历史窗口配合 8 步短动作块最佳，且该配置从预训练中获益最大（平均进度约 +18 点）。该结果提示仿真遥操作可作为灵巧手预训练的可扩展数据源，但对照只有从零训练，未与真机/人手视频预训练比较；评测物体与仿真中相近，仿真物理调参质量和场景多样性仍是限制。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 未找到官方仓库链接，无仓库链接；权重 unknown，数据 unknown，许可 unknown。探测到的 kevinzakka/mink 是论文使用的 IK 依赖库，非官方代码；缓存中项目页字段（gigabrain0）亦有误，官方项目页为 https://spd.bot
- **待核验事项：** 项目页 spd.bot 是否发布 spd-75h 数据集、spd-vr 采集系统代码或预训练权重

### 54. ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World Models — 👀 值得关注

- **时间：** 2026-08-14（[arXiv](https://arxiv.org/abs/2608.14022)）
- **评分：** C3（少步因果世界模型训练配方扎实，但组合了已有因果蒸馏技术，且仅面向游戏而非具身任务。） / E3（单一Minecraft定量基准对比两个基线并有人评与阶段消融，FPS迁移仅定性/单独报告。） / O4（Apache-2.0实质代码，HuggingFace有权重与数据；复现说明完整度未核验。） / T3（港中文林伟团队与腾讯PCG、上海AI实验室合作，在世界模型方向积累有限可核实。） = **66/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** CUHK；Tencent PCG；FDU；Shanghai AI Laboratory；HKUST
- **分类：** `world-model` · 核心 · method
- **核心内容：** 为解决交互式动作条件视频世界模型在因果化与少步蒸馏时，键盘离散动作与鼠标连续动作难以与压缩潜块对齐、误差随自回归累积的问题，作者提出ForgeWM：从Matrix-Game 2.0出发，依次进行双向领域适配、教师强制因果训练、因果一致性蒸馏和基于自生成历史的分布匹配（DMD），得到稳态1/2/4步去噪的学生模型，并提出交互后对保存草稿再加噪精修的回放细化。在GF-Minecraft 77帧配对轨迹上，作者报告其在成像质量、运动轮廓、动作符号准确率与鼠标控制准确率上优于Matrix-Game 2.0和HY-WorldPlay，1步模型延迟168ms、约72 FPS；41人盲测中偏好率60.7%；同一配方迁移到手柄控制的FPS游戏。该工作对需要低延迟交互仿真的世界模型有参考意义，但实验全部在游戏场景，未涉及机器人或物理控制任务，与具身决策的关联需进一步验证，长时程仍有结构退化。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/asdfo123/ForgeWM)；权重 open，数据 open，许可 Apache-2.0。探针发现 HF 权重 ForgeWM/ForgeWM 与数据集 ForgeWM/ForgeWM-data。
- **待核验事项：** 仓库README是否包含完整训练与评测复现说明

### 55. Real-World Cooperative Bimanual Dexterous Grasp of Large Objects from Single-View Observations — 👀 值得关注

- **时间：** 2026-08-11（[arXiv](https://arxiv.org/abs/2608.10383)）
- **评分：** C3（把扩散抓取生成、真机数据和执行期力反馈组合起来，解决双臂大物体抓取的真机落地问题，属于扎实但有限的增量） / E3（全部为真机实验，有 4 个基线和逐模块消融，但测试物体只有 7 个、每个 15 次试验，场景条件单一） / O4（论文给出的 GitHub 仓库包含遥操作、数据和 DDPM 训练/推理代码，代码为 Apache-2.0；完整数据集（约 40GB）放在百度网盘，仅限非商业研究） / T3（奥克兰大学与重庆大学团队，在该方向的积累难以核实，按默认给 3） = **66/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** School of Computer Science, The University of Auckland；College of Computer Science, Chongqing University；College of Electronic and Information Engineering, Southwest University
- **分类：** `manipulation` · 核心 · method
- **核心内容：** 双臂灵巧手协同抓取大物体的研究多停留在仿真，并且依赖完整的物体网格，也不考虑真机上的可达性与接触稳定性。为此作者提出一个真机框架：先在 Unitree H1-2 加 Inspire 灵巧手上用 Apple Vision Pro 遥操作，采集 33 个大物体、353 次抓取的多模态数据（关节角、RGB-D、关节力矩、触觉）；再用 SAM 分割出物体，经 PointNet++ 编码后由 DDPM 生成双臂关节构型；执行时先做带中间路点的运动规划，再进行“手臂内收直到受阻、手指弯曲直到接触”的力引导微调。在按物体划分的测试集上（7 个未见物体，每个 5 种位姿、每种 3 次），作者报告总成功率 61.90%，高于 BimanGrasp-DDPM（28.57%）、ViSiL-HD（37.14%）以及单手方法 GraspNet 和 DexGraspAnything；去掉运动规划、力微调或 DDPM 后成功率都明显下降。这提示真机数据加上执行期反馈对大物体协同抓取很关键，但物体数量少、场景单一（统一背景的桌面），基线需要改造才能跨本体对比，而且模型只预测静态构型，没有把触觉纳入学习。
- **发表状态（核验：2026-10-22）：** IROS 2026
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/zhangdana483/real_bi_dex_grasp)；权重 unknown，数据 open，许可 Apache-2.0。探测漏掉了论文正文给出的仓库；README 写明包含遥操作、数据集和 DDPM 训练/推理代码。数据只附了样例，完整数据在百度网盘，限非商业研究使用
- **待核验事项：** 仓库代码的完整性（只看了目录和 README）；团队在灵巧操作方向的过往成果

### 56. ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU — 👀 值得关注

- **时间：** 2026-07-21（[arXiv](https://arxiv.org/abs/2607.19191)）
- **评分：** C3（数据管线、LongForcing 与部署栈的系统整合扎实，但面向游戏/漫游的键盘控制，对具身控制的直接增量有限。） / E3（有 WorldRoamBench 对比、系统级消融与 LongForcing 对照，但长程效果多为定性展示，无具身下游任务。） / O4（仓库含实质代码（Apache-2.0），HF 已放出 5B 权重与两个数据子集；README 仍有部分 coming soon。） / T3（论文署名为 ABot-World Team，未列单位；信息不足按默认 3 分。） = **66/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Jiang, Fan et al.
- **分类：** `world-model` · 核心 · model
- **核心内容：** 为解决交互式世界模型在数据、控制接口、长程漂移和实时部署上相互制约的问题，ABot-World-0 构建了融合 AAA 游戏、仿真引擎与互联网视频的数据基础设施（WorldExplorer 智能体采集、14 项确定性质检、VLM 评估与动作/文本标注），以 Wan2.2 为基座训练键盘动作条件的双向教师，再经 teacher forcing、ODE 蒸馏和 LongForcing（用更长时域教师对齐学生自回归 rollout）得到因果学生，并配合轻量 VAE 解码、低比特 DiT 等推理栈。作者报告在单张 RTX 5090 上以 720P 最高 16 FPS 流式生成、峰值显存约 19 GiB，在 WorldRoamBench 的动作、视觉、物理、记忆子维度上有竞争力，并展示小时级到天级 rollout 及 OOD 场景控制。该结果提示消费级 GPU 上的长时交互世界模拟已可行，但控制空间仅为 8 键键盘动作，场景以游戏和街景漫游为主，未涉及机器人动作或下游策略学习，长程一致性主要靠定性展示。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/amap-cvlab/ABot-World)；权重 open，数据 partial，许可 Apache-2.0。HF 有 acvlab/ABot-World-0-5B-LF 权重与 ABot-World-Explorer-4D/500h 数据集；README 仍提示部分内容待发布。
- **待核验事项：** 论文未列作者单位，需从 PDF 或项目页确认（仓库组织为 amap-cvlab）；README 标注部分内容 coming soon，需确认训练代码与完整数据是否开放

### 57. DreamX-World 1.0: A General-Purpose Interactive World Model — 👀 值得关注

- **时间：** 2026-06-15（[arXiv](https://arxiv.org/abs/2606.16993)）
- **评分：** C3（整合相机控制、记忆、事件与蒸馏的完整系统，单项技术多为已有思路的组合，且与具身控制关联间接。） / E3（有基础、长时、记忆一致性与人类偏好多项评测，但基准为自建、仅两个对照模型。） / O4（推理代码 Apache-2.0 开源，HF 上公开 5B 权重；训练数据未公开。） / T3（署名仅为 DreamX Team（仓库属 AMAP-ML），团队相关积累信息不足，默认 3。） = **66/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** DreamX Team
- **分类：** `world-model` · 核心 · model
- **核心内容：** 为让视频世界模型在多种画风下响应相机控制、回访时保持场景一致并支持提示事件，作者发布 DreamX-World 1.0：数据上结合 Unreal Engine 渲染（含精确相机位姿与按键动作）、游戏录像与恢复相机几何的真实视频；方法上提出只在空间降采样 token 上做投影位置编码的 E-PRoPE 相机控制、基于相机几何检索历史帧的场景记忆与残差回收、可组合事件的指令微调，再经 causal forcing、DMD 蒸馏与长 rollout 训练转为少步自回归模型，最后用强化学习恢复相机控制与画质。作者报告在自建 5 秒基础评测上相机控制 73.75、总分 84.76，高于 HY-WorldPlay 1.5（80.79）与 LingBot-World（80.45），并给出 30 秒长时、回访一致性评测和盲测人类偏好；推理优化后 8 张 RTX 5090 最高 16 FPS。该结果显示交互式世界模型工程上的进展，但评测套件为作者自建，对照仅两个模型，且面向游戏与相机漫游而非机器人动作条件，具身应用价值尚待验证。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/AMAP-ML/DreamX-World)；权重 open，数据 none，许可 Apache-2.0。权重见 https://huggingface.co/GD-ML/DreamX-World-5B 与 DreamX-World-5B-Cam。
- **待核验事项：** 论文 PDF 中的具体机构署名；仓库是否包含训练代码

### 58. Mana: Dexterous Manipulation of Articulated Tools — 👀 值得关注

- **时间：** 2026-06-11（[arXiv](https://arxiv.org/abs/2606.13677)）
- **评分：** C4（将铰接工具灵巧操作系统化为关键帧+规划+RL 的数据生成框架并实现零样本迁移，对灵巧操作子方向有明确增量。） / E3（有真机多工具多实例评测与数据规模消融，但每格仅 10 次试验，基线只有开环与遥操作。） / O2（仅有项目页，未见代码、数据或模型发布。） / T5（Pieter Abbeel、C. Karen Liu、Guanya Shi 在灵巧操作与 sim-to-real 方向有多项标志性成果。） = **66/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** UC Berkeley；CMU；Stanford University；Amazon FAR
- **分类：** `sim2real` · 核心 · method
- **核心内容：** 为解决多指手操作钳子、夹子、镊子、注射器等铰接工具时需同时稳定抓握与施加功能性力、而位置式遥操作难以提供足够力的问题，作者提出 Mana：用户只需不到一分钟点选功能区域，系统基于改进的碰撞感知 Lightning Grasp+ 生成大量抓取与驱动关键帧，再用 GPU RRT-Connect 规划非接触段、用 IsaacLab PPO（含力相关域随机化）学习接触段，产出仿真轨迹后蒸馏为点云条件扩散策略，部署在 xArm7+Allegro 手（定制柔性指尖）上。作者报告四类工具、各两个实例、每项 10 次试验中，抓取与开合成功率约 70%，明显高于开环回放与 GeoRT 遥操作基线（遥操作在夹子上几乎为零）；消融显示真机性能随轨迹数、关键帧多样性和力扰动强度提升；组合技能的工具使用任务成功率 5/10–7/10，但对准阶段借助人工腕部遥操作。该结果提示面向接触的仿真数据生成可以零样本迁移到薄小铰接工具，但受限于手的力矩、缺少触觉滑移检测，且长任务尚未完全自主。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 未找到官方仓库链接，无仓库链接；权重 none，数据 none，许可 unknown。仅项目页 https://zhaohengyin.github.io/mana
- **数据/基准关系：** isaac-lab（预训练）
- **待核验事项：** 项目页是否发布代码或生成数据

### 59. LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction — 👀 值得关注

- **时间：** 2025-06-16（[arXiv](https://arxiv.org/abs/2506.13751)）
- **评分：** C4（首个面向人形全身控制的视觉-语言闭环基准与潜动作分层框架，为人形 VLA 提供新接口思路。） / E3（自建仿真基准上的系统消融，真机仅开环回放演示，缺少外部方法对照。） / O2（仅确认有项目页；探测到的 big_vision 为 SigLIP 依赖仓库而非本文代码，未找到官方代码或基准下载。） / T5（UC Berkeley（Sreenath、Darrell、Sastry、Peng）与 CMU 石冠亚等团队，在人形控制与 VLM 方向有多项标志性成果。） = **66/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** University of California Berkeley；Norwegian University of Science and Technology；Simon Fraser University；Carnegie Mellon University
- **分类：** `vla` · 核心 · model
- **核心内容：** 多数 VLA 依赖末端位姿、底盘速度等手工设计的低层动作接口，难以表达敏捷的人形全身行为。为此作者先构建 LeVERB-Bench：在 IsaacSim 中用光线追踪回放重定向后的动捕运动，随机化场景、物体、视角并由 VLM 标注指令，得到约 17.1 小时视觉-语言数据和 2.7 小时纯语言数据，覆盖 150 余个任务、10 个类别。随后提出 LeVERB：高层 LeVERB-VL 以残差 CVAE 从合成运动学示范中学习潜在「动作词表」，并用判别器对齐两类数据；低层 LeVERB-A 先用 PPO 训练跟踪教师，再用 DAgger 蒸馏为以潜变量为条件的 Transformer 全身控制策略。在基准的闭环评测中（每类 20 个未见组合场景），作者报告简单视觉导航成功率 80%、总体 58.5%，约为去掉采样的朴素分层 VLA 的 7.8 倍，并在多数类别优于各消融变体；在 Unitree G1 上展示了潜动作开环回放的零样本 sim-to-real。局限：对照仅为自身消融，真机未做闭环视觉评测，长时程规划能力有限。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 未找到官方仓库链接，无仓库链接；权重 unknown，数据 unknown，许可 unknown。原探测命中的 google-research/big_vision 是 SigLIP 所在仓库，非本文代码，已更正为 no-repo。
- **数据/基准关系：** isaac-sim（评测）
- **待核验事项：** 官方代码与 LeVERB-Bench 数据是否发布（项目页链接返回 404，未能核实）

### 60. UniReflex: Plug-and-Play Force Control for Pretrained Generative Policies via Fast-Slow Reflex — 👀 值得关注

- **时间：** 2026-08-18（[arXiv](https://arxiv.org/abs/2608.17432)）
- **评分：** C4（以非侵入方式给冻结的生成式策略加入变阻抗力控，适配多种骨干，对接触丰富操作有明确的实用增量。） / E4（5 项真机任务、3 种骨干、3 个力感知基线、组件消融与扰动恢复，但每项仅 10 次试验。） / O2（仅有项目页 unireflex.github.io，未见代码仓库。） / T3（清华深研院丁文伯团队在触觉与接触操作方向有一定可核实积累，按 3 计。） = **65/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Tsinghua University Shenzhen International Graduate School；Nanyang Technological University；X Square Robot；Xspark AI
- **分类：** `manipulation` · 核心 · method
- **核心内容：** 生成式模仿策略擅长轨迹规划却缺少闭环力调节，而把力模态并入网络通常需要重新设计或重训大骨干。UniReflex 保持慢速生成策略冻结，只读截取其动作头最后投影前的时序隐表示作为"慢意图"，结合本体与腕部力反馈驱动一个 GRU 快速反射网络，逐步输出参考力与各向异性刚度方向，并用接触触发的门控在位置主导与力主导之间切换；监督信号来自遥操作主从误差推得的力意图。在擦拭曲面/斜面、插充电器、撕便签、翻芯片盒 5 项双臂真机任务（每项 10 次）上，作者报告接入后接触阶段成功率较原骨干提升 20–60 个百分点，非接触阶段变化不超过 10 个百分点，且多数任务不低于 RDP、ForceVLA、TA-VLA；消融显示刚度预测和门控必不可少；反向传播延迟比联合训练低 25–66 倍。但短时高冲击的插接任务无明显提升，对长动作块的世界动作模型增益较小，未公开代码。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 未找到官方仓库链接，无仓库链接；权重 none，数据 unknown，许可 unknown。项目页 https://unireflex.github.io/
- **待核验事项：** 项目页是否发布代码

### 61. GigaBrain-WBC-0.5: A Behavior World Model for Robust Whole-Body Control with Environment Interaction — 👀 值得关注

- **时间：** 2026-08-18（[arXiv](https://arxiv.org/abs/2608.18234)）
- **评分：** C4（将行为世界模型目标与自动地形标注引入通用全身跟踪，统一交互与鲁棒性，对人形控制子方向有明确增量。） / E4（四类sim-to-sim基准对比三个强基线并有组件消融，真机为多场景定性对比，缺少真机定量统计。） / O2（仅有技术报告与项目页，未见代码或权重。） / T3（HTML与缓存未列出作者单位，无法核实，按信息不足默认3。） = **65/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Cheng, Ziyang et al.
- **分类：** `locomotion` · 核心 · method
- **核心内容：** 为解决通用人形动作跟踪器只在平地训练、无法利用地形与物体交互的问题，作者提出GigaBrain-WBC-0.5（初版名InterTrack）：因果Transformer在输出动作的同时预测下一本体状态与下一行为指令的混合分布，以学习环境条件下的动力学；用自动标注管线从重定向动作中重建3D支撑几何以扩充交互训练数据；部署时用预测分布过滤不可行指令实现“尽力而为”执行，并结合倒地初始化训练恢复。在MuJoCo sim-to-sim评测中（AMASS标准集、Bones-Seed地形集、MotionMillion不可行指令集、摔倒集），对比SONIC、HoloMotion-1、Humanoid-GPT官方权重，作者报告地形成功率81.3%、摔倒恢复99.3%、标准集MPKPE 76.6mm，消融显示两项核心组件贡献明显；G1真机演示了跨地形遥操作与倒地恢复。结果提示预测式目标有助于交互感知的全身控制，但真机证据以定性为主，命令过滤识别的是陌生行为而非物理风险。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 未找到官方仓库链接，无仓库链接；权重 none，数据 none，许可 unknown。项目页 https://shepherd1226.github.io/gigabrain-wbc-0.5/ ；未见代码仓库。
- **数据/基准关系：** amass（评测）
- **待核验事项：** 作者单位需从PDF核实（HTML未列出）；是否计划开源代码/权重

### 62. MemoryWAM: Efficient World Action Modeling with Persistent Memory — 👀 值得关注

- **时间：** 2026-06-18（[arXiv](https://arxiv.org/abs/2606.20562)）
- **评分：** C4（面向 WAM 的记忆-效率矛盾给出完整的混合记忆设计，对长时程记忆依赖操作有明确增量。） / E4（RMBench 九任务、强 VLA/WAM 基线、记忆机制效率对比、组件消融及两项真机任务，较完整。） / O1（仅有项目页，未找到代码或权重。） / T5（许华哲、庞江淼、林达华团队在机器人学习与具身基础模型方向有多项标志性成果。） = **65/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** The Chinese University of Hong Kong；Tsinghua University；Zhejiang University
- **分类：** `world-model` · 核心 · model
- **核心内容：** 为解决世界-动作模型在“只看有限近期窗口”（非马尔可夫任务失败）与“缓存全部历史”（时延与显存随长度增长）之间的取舍，作者提出 MemoryWAM：基于 Wan2.2-TI2V-5B 视频 DiT 与约 1B 动作 DiT 的 MoT 结构，推理时不生成视频，只用视频分支维护 KV 缓存；记忆由滑动窗口近期帧、任务起始等事件边界锚帧和压缩长程历史的 gist token 组成，并设计相应注意力掩码。在 RMBench 九项记忆依赖双臂任务（每任务 50 条示范、100 次评测）上，作者报告平均成功率比保留全历史的 LingBot-VA 高 4.8 个百分点、各任务均不低于对手，而短窗口的 π 系列 VLA 基线与 FastWAM 仅约 10% 与 6%；ARX 双臂真机 Shell Game 与 Look and Press 任务上也优于两者，并在单层效率对比中显示延迟与显存低于全注意力、TTT 与 RNN。消融显示去掉 gist token 下降最大，全注意力反而更差。该结果提示紧凑混合记忆可兼顾效率与长时依赖，但部分任务使用了额外预训练或动作历史以对齐基线，真机任务少，语义推理能力受视频扩散骨干限制。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 未找到官方仓库链接，无仓库链接；权重 none，数据 none，许可 unknown。论文仅给出项目页 yangsizhe.github.io/MemoryWAM。
- **待核验事项：** 是否发布代码与权重

### 63. M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking — 👀 值得关注

- **时间：** 2026-06-03（[arXiv](https://arxiv.org/abs/2606.04829)）
- **评分：** C3（多模态参考统一编码的单阶段全身控制器是有用的工程化改进，增量主要在架构组织。） / E4（四个强基线、OOD 测试集、课程/数据/网络规模消融与真机遥操作定量结果，较完整。） / O3（仓库有实质代码，但未见许可证与权重。） / T3（清华李升波、东南大学孙长银等在 RL 与控制方向有积累，人形方向相关成果相对有限。） = **65/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** School of Automation, Southeast University；School of Vehicle and Mobility, Tsinghua University；Department of Robotics, Mohamed Bin Zayed University of Artificial Intelligence
- **分类：** `locomotion` · 核心 · method
- **核心内容：** 为解决人形全身控制中稠密关节角参考与稀疏末端位姿参考的表示失配——以往要么部署时额外做 IK 转换，要么拼接多模态指令再经多阶段师生蒸馏——作者提出 M3imic：为关节角、人体姿态、末端位姿三种参考分别设计编码器，映射到共享潜空间，在 Isaac Sim 中以单阶段大规模 RL 训练一个策略，并配合按片段失败率 EMA 的自适应课程采样与域随机化实现零样本 sim-to-real。作者在 LAFAN1 与 100STYLE 上训练，报告训练集上成功率 99.54%、关键点误差 46.05 mm，优于 HOVER、ExBody2、OmniH2O、TWIST2；在未见的 OMOMO 测试集上，关节角策略跟踪误差最低，末端位姿策略成功率最高（98.42%），体现保真度与鲁棒性的权衡；消融显示数据规模比网络规模影响更大。真机上 G1 跟踪舞蹈、跑步等动作，并用光学动捕做末端位姿遥操作，误差与关节角策略接近。该结果提示共享潜空间可统一多源参考，但真机评测以少量动作为主，基线均按原设置复现，仓库未声明许可证。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/Renforce-Dynamics/MultiModalWBC)；权重 unknown，数据 n/a，许可 none-found。探测到 87 个代码文件，未找到 LICENSE
- **待核验事项：** 仓库许可证与是否发布训练好的策略权重

### 64. ALOHA Unleashed: A Simple Recipe for Robot Dexterity — 👀 值得关注

- **时间：** 2024-10-17（[arXiv](https://arxiv.org/abs/2410.13126)）
- **评分：** C4（证明规模化示范 + 扩散策略可完成系鞋带等此前难以实现的灵巧双臂任务，对灵巧模仿学习有明确参考价值。） / E4（5 项真机任务各 20 次试验，含数据量、数据过滤、扩散 vs L1 消融和仿真多种子实验；基线主要为 ACT 变体。） / O1（未见官方代码、权重或数据发布；探测到的 mujoco_menagerie 只是 ALOHA 2 仿真模型库。） / T5（Google DeepMind 机器人团队（Tony Zhao、Chelsea Finn 等）在 ALOHA 系列与模仿学习方向有多项标志性成果。） = **65/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Google DeepMind
- **分类：** `manipulation` · 核心 · method
- **核心内容：** 模仿学习的成功多集中于抓放、推动等非灵巧任务，单纯扩大模仿学习能否解决可形变物体、接触丰富的双臂灵巧操作尚不清楚。ALOHA Unleashed 给出一个简单配方：在 ALOHA 2 机群上由多名操作员采集超过 2.6 万条真机示范（5 项任务）和 2000 余条仿真示范，训练以多视角图像与本体感知为条件、带动作分块的 Transformer 编码器-解码器扩散策略（DDIM 采样，每任务单独训练）。在挂衬衫、系鞋带、更换机械手指、齿轮插装和随机厨具堆叠 5 项真机任务上每项 20 次试验，作者报告取得较高成功率，并称首次实现端到端策略自主系鞋带与挂 T 恤；消融显示数据量对困难变体（ShirtMessy）影响大、按时长适度过滤数据有益，同规模下扩散损失明显优于 ACT 式 L1 回归，3 项 MuJoCo 仿真任务中扩散在多数任务上更好。该结果提示「大规模高质量示范 + 表达力强的策略」可推进灵巧操作；但每个任务需数千条示范、策略为单任务且 1 秒重规划，代码与数据未公开。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 未找到官方仓库链接，无仓库链接；权重 none，数据 none，许可 unknown。原探测命中的 google-deepmind/mujoco_menagerie 并非本文代码仓库（仅为仿真用 ALOHA 2 模型），已更正为 no-repo。
- **待核验事项：** 作者单位仅提取到 Google DeepMind，需核对 PDF 是否还列有其他单位（如 Stanford）

## 相邻路线（数据 / 基准 / 基础设施 / 分析）

### 65. 3D Gaussian Splatting for Real-Time Radiance Field Rendering — 🔥 重点阅读

- **时间：** 2023-08-08（[arXiv](https://arxiv.org/abs/2308.04079)）
- **评分：** C5（新的显式场景表示范式，已成为机器人 3D 场景重建与 real2sim 管线的基础组件（对具身方向属间接贡献）。） / E5（三个真实数据集 13 个场景与合成数据，对比 Mip-NeRF360、InstantNGP、Plenoxels，含系统消融与速度/显存报告。） / O4（代码完整公开，但许可为 Inria 自定义的非商业研究许可；评测数据为公开数据集。） / T5（Inria GraphDeco（Drettakis）团队在基于点与图像的渲染方向长期领先。） = **94/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** Inria, Université Côte d’Azur, France；Max-Planck-Institut für Informatik, Germany
- **分类：** `scene` · 相邻路线 · method
- **核心内容：** 辐射场方法要么画质高但训练与渲染昂贵，要么速度快但牺牲质量，无法在完整无界场景中以 1080p 实时渲染。3D Gaussian Splatting 从 SfM 稀疏点云初始化一组 3D 高斯，优化其位置、不透明度、各向异性协方差与球谐颜色；在优化中交替执行克隆与分裂的自适应致密化；并实现支持各向异性 splatting 的可见性感知分块光栅化器，使训练与渲染都很快。在 Mip-NeRF360、Tanks&Temples、Deep Blending 共 13 个真实场景及 Blender 合成数据上，作者报告 PSNR/SSIM/LPIPS 与 Mip-NeRF360 相当或更好，训练时间与 InstantNGP、Plenoxels 等快速方法相当，并实现实时渲染；消融验证了 SfM 初始化、致密化策略、各向异性和不限制梯度高斯数量的作用。该表示已广泛用于机器人 real2sim、场景重建与仿真资产生成；但论文本身是图形学工作，不涉及具身决策，且存在欠观测区域伪影、显存占用较大等局限。
- **发表状态（核验：2026-10-22）：** ACM TOG 2023
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/graphdeco-inria/gaussian-splatting)；权重 n/a，数据 open，许可 custom。Inria/MPII 自定义非商业许可；作者在项目页提供场景数据与预训练模型。

### 66. GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors — 🔥 重点阅读

- **时间：** 2026-06-03（[arXiv](https://arxiv.org/abs/2606.05160)）
- **评分：** C4（把视频世界模型约束在已知 3D 配置中生成可执行人形交互数据，是可扩展数据来源的明确新路径。） / E4（HOI 生成对比、跟踪消融、重建损失消融、用户研究与真机拾取/爬楼部署，证据较全；真机试验次数偏少。） / O4（NVlabs 仓库含大量实质代码（自定义许可），生成数据集已在 HF 发布；策略权重未核实。） / T5（NVIDIA GEAR/多伦多实验室（朱玉可、范麟熙、罗正宜、Fidler、Kautz）是人形与世界模型方向公认领先团队。） = **83/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** NVIDIA；UCLA
- **分类：** `locomotion` · 相邻路线 · data
- **核心内容：** 为解决人形 loco-manipulation 演示依赖遥操作与动捕、难以在物体与场景上扩展的问题，作者提出 GRAIL：先在 Infinigen 生成的仿真就绪场景中摆放物体与按 G1 体型预拟合的人物，渲染首帧交给视频基础模型（Kling 2.5）生成交互视频；由于相机参数、度量尺度、物体几何与环境深度已知，可用 GENMO、WiLoR、FoundationPose 与交互感知联合优化重建度量 4D 人-物轨迹，经 GMR 重定向到 Unitree G1；再在预训练全身控制器 SONIC 上训练物体感知潜变量适配器与地形感知跟踪器，转化为机器人动作数据。作者用 1000 个物体资产和 1000 种地形生成超过 2 万条序列（拾取、全身操作、坐下、地形穿越）；在 20 物体评测集上，生成的 HOI 在接触、穿透与可跟踪性上优于 CHOIS、HOIDiff、DAViD；仅用 GRAIL 数据蒸馏的第一视角视觉策略在真机上拾取成功率 84%（未见物体 80%，各 10 次）、爬楼 90%。该结果提示 3D 先验约束下的视频生成可补充遥操作数据，但依赖物体资产与商业视频 API，生成失败需过滤，真机任务仍较简单。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/NVlabs/GRAIL)；权重 unknown，数据 open，许可 custom。HF 数据集 nvidia/PhysicalAI-Robotics-Locomanipulation-GRAIL；v2 标题改为 Generating Humanoid Loco-Manipulation from World Models
- **待核验事项：** 自定义许可的使用限制与策略权重是否发布

### 67. Mobile ALOHA: Learning Bimanual Mobile Manipulation — 🔥 重点阅读

- **时间：** 2024-01-04（[arXiv](https://arxiv.org/abs/2401.02117)）
- **评分：** C4（低成本全身遥操作移动操作平台 + 协同训练方案，推动了双臂移动操作的数据采集与研究普及。） / E4（7 项复杂真机任务、3 种模仿学习方法、协同训练消融与用户研究；为单任务策略且无外部系统对照。） / O4（MIT 代码与硬件说明公开，任务数据可下载；无预训练策略权重。） / T5（Stanford Chelsea Finn 团队在模仿学习与 ALOHA 系列方向有多项标志性成果。） = **83/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** Stanford University
- **分类：** `teleoperation` · 相邻路线 · system
- **核心内容：** 模仿学习成果多局限于桌面操作，缺少可负担的双臂移动操作硬件和全身遥操作接口。Mobile ALOHA 在 ALOHA 基础上加装 AgileX Tracer 移动底盘，操作者通过与底盘绑定的主从臂同时控制双臂和底盘，系统自带电源与算力，总成本低于 3.2 万美元，软硬件开源。策略方面，作者把 Mobile ALOHA 任务数据与 825 条静态 ALOHA 数据协同训练，不做特殊处理。在擦红酒、炒虾、开柜放锅、呼叫并进入电梯、冲洗锅、推椅子、击掌 7 项真机任务上（多数 20 次试验），作者报告用 ACT 协同训练时多数任务成功率达 80–95%，在 7 项中的 5 项提升 20–95 个百分点；Diffusion Policy 与 VINN 同样受益；消融显示协同训练提高数据效率、对混合比例不敏感且优于先预训练再微调；用户研究显示新手很快接近专家速度。局限：策略为单任务、示范由两名专家采集，底盘与固定臂高限制可达范围。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/MarkFzp/mobile-aloha)；权重 none，数据 open，许可 MIT。硬件教程与训练代码（ACT/协同训练）公开；Mobile ALOHA 任务数据集已公开（亦被 LeRobot 收录为 aloha_mobile_* 数据集）。

### 68. RynnWorld-Teleop: An Action-Conditioned World Model for Digital Teleoperation — 🔥 重点阅读

- **时间：** 2026-07-07（[arXiv](https://arxiv.org/abs/2607.06558)）
- **评分：** C4（用实时动作条件世界模型替代真机完成遥操作采集，是数据采集方式上的明确新思路。） / E4（真机 4 任务×35 次、三种策略、纯生成与混合数据、颜色增强与 H2R 对照及预训练消融，证据较完整。） / O4（代码实质开源（Apache-2.0）并发布模型权重，采集的真机数据未公开。） / T4（达摩院具身团队与港中文合作，在 VLA、具身世界模型方向有连续成果。） = **80/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** Hong Kong Embodied AI Lab；CUHK；Alibaba Group；Ant Group；DAMO Academy, Alibaba Group；Hupan Lab
- **分类：** `teleoperation` · 相邻路线 · system
- **核心内容：** 为摆脱物理遥操作对真机硬件与固定工作空间的依赖，作者提出数字遥操作范式：操作者的手部位姿流驱动以机器人为中心的生成式世界模型，从单张参考图合成机器人第一视角视频，而记录的位姿经 IK 重定向后即为动作标签，从而得到可直接用于模仿学习的轨迹。RynnWorld-Teleop 基于 Wan2.2-TI2V-5B，以深度感知骨架渲染作为控制信号，先在 EgoDex、VITRA 人类视频上预训练，再用 1800 条人-机配对数据适配机器人域，并蒸馏为因果自回归学生模型。在 TIANJI M6 双臂+WUJI 灵巧手平台的 4 个任务上（每任务 35 次），作者报告仅用 300 条生成数据训练的 DP/π0/π0.5 平均成功率为 54–64%，低于 300 条真机数据（77–83%）；而真机数据加 300 条生成数据可稳定提升，优于颜色增强与 H2R 对照，加 600 条时 π0 约 92.8%。结果提示生成数据可作有效增广，但单独使用仍不及真机数据，任务均为短程桌面操作，生成视频的物理一致性未做独立检验。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/alibaba-damo-academy/RynnWorld-Teleop)；权重 open，数据 none，许可 Apache-2.0。HF 发布 RynnWorld-Teleop 与因果蒸馏版权重。
- **待核验事项：** 1800 条人-机配对数据与生成数据是否发布

### 69. VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training — 🔥 重点阅读

- **时间：** 2026-06-03（[arXiv](https://arxiv.org/abs/2606.04708)）
- **评分：** C4（系统化解决 UMI 数据进入 VLA 训练的视觉与物理两类缺口，并提供大规模鱼眼 VQA 与校验工具，对手持采集数据利用有明确增量。） / E4（诊断实验、得分-部署相关性、跨本体部署、仿真与 20 个真机任务及组件消融，较完整；仿真为改造的鱼眼基准。） / O4（Apache-2.0 仓库含训练与物理校验代码，权重与数据经 HF collection 发布；UMI-VQA 与轨迹数据的具体条目未逐一核实。） / T4（TeleAI（李学龙、白辰甲）在具身智能与 RL 方向有多项可核实成果。） = **80/100**；**优先级：** 🔥 重点阅读
- **作者/团队单位：** Institute of AI (TeleAI), China Telecom；University of Science and Technology of China；Northwestern Polytechnical University；Shanghai Jiao Tong University；East China University of Science and Technology；Harbin Engineering University；Lumos Robotics；Fudan University
- **分类：** `teleoperation` · 相邻路线 · data
- **核心内容：** 为解决用 UMI 手持夹爪数据训练大规模 VLA 时的两类失配——腕部鱼眼视角对预训练 VLM 属分布外、人工采集轨迹常违反目标机器人运动学或引发自碰撞——作者提出 VISTA：（1）构建约 800 万样本的 UMI-VQA（含约 300 万真实鱼眼帧问答），在联合训练中对齐视觉表征；（2）基于 MuJoCo 与 Mink 的跨本体轨迹回放，对每条轨迹做完整性预检并按连续性、自碰撞风险、执行保真度打分，预训练用宽松阈值、下游微调对目标机器人收紧；（3）先做 VQA 与 FAST 离散动作自回归联合训练，再训练知识隔离的流匹配动作专家。作者先诊断性地报告鱼眼输入使 π0.5、LingBot-VLA 在 LIBERO/RoboTwin 上平均下降 13–16 点、VLM 空间推理平均相对下降 8.6%；高分与低分轨迹子集训练的策略在 RealMan 等三种本体上部署成功率差异明显；在鱼眼版仿真基准和 20 个真机任务上 VISTA 优于 π0.5、LingBot-VLA、Wall-X。该结果提示数据层面的视觉对齐与物理过滤对 UMI→VLA 很关键，但仿真基准为作者改造的鱼眼版本，UMI-VQA 的具体发布形式待核实。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/TeleHuman/umi-vista)；权重 open，数据 partial，许可 Apache-2.0。README 含微调与物理校验回放打分代码；权重与数据统一指向 huggingface.co/collections/TeleEmbodied/vista，未逐项列出数据
- **数据/基准关系：** libero（评测）
- **待核验事项：** HF collection TeleEmbodied/vista 中是否包含完整 UMI-VQA 与校验后轨迹数据

### 70. PhysX-Omni: Unified Simulation-Ready Physical 3D Generation for Rigid, Deformable, and Articulated Objects — 👀 值得关注

- **时间：** 2026-05-20（[arXiv](https://arxiv.org/abs/2605.21572)）
- **评分：** C4（首个覆盖三类资产的统一仿真就绪生成框架并配数据集与基准，对具身仿真资产供给有明确增量。） / E3（两个数据集上多基线定量对比与消融较完整，但具身下游（策略学习）仅定性展示，基准为自建且依赖 VLM 评判。） / O4（实质代码、HF 权重与三个 HF 数据集均已公开，但许可证为自定义条款。） / T5（NTU S-Lab（刘子纬组）在 3D 生成方向有多项标志性成果与资源。） = **78/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** S-Lab, Nanyang Technological University；ACE Robotics
- **分类：** `scene` · 相邻路线 · model
- **核心内容：** 为解决现有 3D 生成忽视物理属性、或只针对刚体/铰接/可形变某一类资产，且缺少大规模标注数据和真实场景评测基准的问题，作者提出 PhysX-Omni：基于 Qwen2.5-VL-7B，以无需压缩的 VLM 友好几何表示直接编码高分辨率 3D 结构，先全局推断类别、尺度、部件层级和物理属性，再逐部件生成几何与属性，并用 TRELLIS 解码为网格。同时发布 PhysXVerse（8.7K 资产、2.9K 类别，GPT 预标注+人工校验）和用 Qwen3.5 评判渲染视频的六维基准 PhysX-Bench。在 PhysXVerse 与 PhysX-Mobility 上，作者报告 PSNR、CD、F-score 及尺度、材质、可供性、运动学指标大多优于 Articulate-Anything、MonoArt、PhysXGen、PhysX-Anything（如 PhysXVerse 尺度误差 2.79 对 298.19），PhysX-Bench 评分与人工标注一致性较高。结果提示统一的仿真就绪资产生成可降低机器人仿真建模成本，但机器人策略学习与场景生成仅为定性演示，基准依赖 VLM 评判，物理属性真实性仍需下游实测验证。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/physx-omni/PhysX-Omni)；权重 open，数据 open，许可 custom。权重 HF PhysX-Omni/PhysX-Omni；数据 HF PhysX-Omni/PhysXVerse、Caoza/PhysX-3D、Caoza/PhysX-Mobility。
- **数据/基准关系：** physxverse（提出）、physx-bench（提出）
- **待核验事项：** 自定义许可证是否允许商用/再分发

### 71. Revisiting Open-Loop Execution in Robotics: Toward Reactive, Higher-Performing Policies — 👀 值得关注

- **时间：** 2026-08-16（[arXiv](https://arxiv.org/abs/2608.15938)）
- **评分：** C4（对动作分块这一普遍做法给出可检验的机理解释与实践建议，可能影响 IL 策略设计） / E4（4 个仿真 + 2 个真机任务，专家类型、数据量、DAgger、上下文长度多组受控对照） / O3（代码仓库仅占位，但脚本专家与示教数据已在 HuggingFace 公开） / T5（MIT Tedrake 组是扩散策略等标志性工作的来源团队） = **77/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Massachusetts Institute of Technology；Mundane Systems Inc.；University of California, Berkeley
- **分类：** `rl-il` · 相邻路线 · method
- **核心内容：** 为厘清动作分块中长开环执行为何有效，作者在扩散策略上做系统受控实验：用有限状态机构造马尔可夫与注入历史依赖行为的非马尔可夫脚本专家，并比较人类示教。在 FurnitureSim 单腿装配、PushT、齿轮插装与 Kitchen 四个仿真任务上，作者报告示教的非马尔可夫性主导「成功率-执行步长」曲线：马尔可夫专家数据下曲线近乎单调下降、最优步长接近 1；而扩大数据量、HG-DAgger 等针对累积误差的干预只带来较小偏移（仅在 100 条示教时累积误差作用明显）。进一步把上下文长度提高到 16–20 帧并采用「双编码器」后，最优步长左移，1000 条示教时长上下文、短步长策略显著优于短上下文最佳配置；两个真机任务（倒单粒药片、塞纸条入袋）也呈相同趋势。该结果提示应优先发展长上下文、高反应性策略，但结论局限于扩散策略和中等数据规模，代码仓库目前为空。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 找到仓库但未发现实质相关代码，[仓库](https://github.com/Michaelszeng/Revisiting-Open-Loop-Execution-in-Robotics)；权重 none，数据 open，许可 MIT。仓库仅 2 个文件无代码；HuggingFace 公开 FurnitureSim one_leg 与 ManiSkill PlanarPushT 遥操作数据

### 72. XPolicyLab: A Unified Standard and Open Ecosystem for Robot Policy Evaluation and Deployment — 👀 值得关注

- **时间：** 2026-08-10（[arXiv](https://arxiv.org/abs/2608.09892)）
- **评分：** C4（把策略侧接口标准化为可复用的生态，覆盖 42 个策略和仿真/真机多个评测平台，对复现与公平比较有实际价值） / E3（证据主要是接入覆盖面、adapter 代码量统计、小规模集成耗时对照和排行榜快照，属于系统可用性证据，而非严格的对照实验） / O4（Apache-2.0 仓库含大量实质代码；仓库 README 仍有部分 coming soon 字样，各策略权重依赖上游发布） / T4（由 HKU MMLab 与清华牵头，与 RoboTwin 等基准团队有可核实的积累） = **75/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** MMLab@HKU；THU
- **分类：** `vla` · 相邻路线 · infra
- **核心内容：** 机器人策略的评测和部署被各自的软件依赖、数据格式和运行接口割裂：把 N 个策略接到 M 个环境，需要 O(NM) 次单独集成，预处理约定也在反复重写中悄悄改变，导致结果难以横向比较。为此作者发布 XPolicyLab：定义统一的观测、动作和轨迹 schema，以及只有 update_obs / get_action / reset 和批量接口的最小 adapter 协议；再通过 WebSocket + MessagePack 的依赖隔离服务，把策略推理与环境执行分在不同进程甚至不同机器上。配套的分级一致性检查和可供编码 agent 执行的 skills 用来规范接入流程。作者报告：截至 2026 年 8 月已接入 42 个策略（VLA、WAM、扩散策略等）；各 adapter 的模型侧代码量差异达一个数量级，而面向环境的循环保持在固定参考的几行以内；在小规模对照实验中，接入一个代表性策略的时间从 5 小时以上降到 2 小时，使用 agent skills 后降到约 30 分钟；同一套 adapter 驱动了 RoboTwin、RoboDojo 仿真和 RoboDojo-RealEval（三种双臂本体、18 个真机任务）的排行榜。这提示统一接口能降低复现和比较的成本，但它本身不评测算法，集成工作量研究的参与者人数有限，也无法消除真机评测中的物理方差。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/XPolicyLab/XPolicyLab)；权重 n/a，数据 n/a，许可 Apache-2.0。基础设施项目；策略权重来自各上游仓库，不由本项目发布
- **数据/基准关系：** robotwin（评测）
- **待核验事项：** README 中标为 coming soon 的部分具体是什么

### 73. HumanCLAW: Can Vision-Language Models Act Through a Body? — 👀 值得关注

- **时间：** 2026-07-29（[arXiv](https://arxiv.org/abs/2607.27180)）
- **评分：** C4（决策与执行解耦、同时保留物理后果的评测设定较新，可能影响 VLM 具身代理的评测方式。） / E3（9 个 VLM、组件消融与分阶段错误分析较充分，但为单一仿真基准且交互类型单一。） / O4（实质代码（Apache-2.0）、HF 运动模型权重与 HSSD 场景数据均已发布；复现说明完整度未核实。） / T4（Meta 与 NTU（刘子纬）、UW（Ranjay Krishna）、Northwestern（Manling Li）在多模态与人体运动方向有可核实积累。） = **75/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Meta；Nanyang Technological University；University of Washington；Brown University；Northwestern University
- **分类：** `navigation` · 相邻路线 · benchmark
- **核心内容：** 为解决评测 VLM 能否通过身体行动时，决策失误与运动控制失败（如失衡跌倒）相互混淆的问题，HumanCLAW 让带推理脚手架的现成 VLM 每步根据第一人称图像输出一个参数化原子技能，再由在 AMASS/BABEL 上训练、按技能接入 ControlNet 的运动扩散模型生成亚秒级全身动作，在保留重力与碰撞、但剔除平衡和跟踪误差的“半物理”仿真中执行。在此基础上构建 HumanCLAW-Bench：基于 HSSD 的 41 个室内场景、1,218 个“寻找—导航—坐下”长程 episode，并把可移动物体设为动态。作者评测 9 个 VLM，报告最好的 Gemini-3.1 端到端成功率仅 16.8%，失败主要来自身体自我感知（不知自身位置、是否到达或碰撞），而非目标识别；消融显示验证器和中层目标是关键，更长文本或图像历史无益。该结果提示通用 VLM 的“行动智能”仍明显不足，但交互仅限坐下，人形在仿真中执行，结论不能直接外推到真实机器人控制。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/Human-CLAW/HumanCLAW)；权重 open，数据 open，许可 Apache-2.0。HF 有 HumanCLAW/HumanCLAW 权重与 HumanCLAW-HSSD 数据集。
- **数据/基准关系：** amass（预训练）
- **待核验事项：** 核实仓库的复现说明与评测脚本完整性

### 74. OpenTeleVision: Open-source Immersive Teleoperation with Stereo Visual Feedback — 👀 值得关注

- **时间：** 2024-07-01（[arXiv](https://arxiv.org/abs/2407.01512)）
- **评分：** C4（把主动立体视觉反馈引入人形遥操作并开源，成为人形数据采集常用参考方案。） / E3（两款人形真机 4 项任务 + 设计消融 + 用户研究，但试验次数少、对照仅为自身变体。） / O4（Apache-2.0 代码公开，README 提供数据集下载链接；无训练好的策略权重。） / T4（UCSD 王小龙团队在人形遥操作与灵巧操作方向有可核实的持续积累。） = **75/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** UC San Diego；MIT
- **分类：** `teleoperation` · 相邻路线 · system
- **核心内容：** 遥操作是采集机器人示范的主要手段，但现有系统常因操作者视线被遮挡、缺乏深度感知而难以完成精细任务。Open-TeleVision 用 VR 头显（文中为 Apple Vision Pro）采集操作者手、腕、头部位姿，经 IK 与重定向控制双臂和多指手或夹爪，同时在机器人头部装 2–3 自由度主动颈部与 ZED Mini 立体相机，相机随操作者头部运动，以 60Hz 回传立体视频，实现「所见即机器人所见」，并支持跨城市远程操作。作者在 Unitree H1（灵巧手）与 Fourier GR-1（夹爪）上采集 Can Sorting、Can Insertion、Folding、Unloading 四项任务数据，训练以 DINOv2 为骨干、立体图像为输入的 ACT 策略，报告其成功率高于 ResNet18 骨干和单目输入的对照，用户研究显示立体显示缩短完成时间、提高成功率。该系统为人形数据采集提供了开源参考实现；但策略评测每项仅 5 个完整回合，对照均为自身消融，系统缺少触觉/力反馈，也只使用上半身自由度。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/OpenTeleVision/TeleVision)；权重 none，数据 open，许可 Apache-2.0。README 提供 Google Drive 数据集下载；未提供训练好的检查点（需自行训练 ACT）。

### 75. PAWBench: How Far Are We from Probabilistically Aligned World Modeling? — 👀 值得关注

- **时间：** 2026-08-27（[arXiv](https://arxiv.org/abs/2608.27345)）
- **评分：** C3（分布层面评测视角新颖，但面向通用视频生成，对具身方向属间接支撑） / E4（11 个模型、采样预算敏感性、蒙特卡洛基线与人工一致性检验，评测设计较严谨） / O4（评测代码 Apache-2.0 与 HuggingFace 数据集均已公开） / T4（上海 AI Lab 等团队在视频生成与评测方向有较多可核实成果） = **74/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Shanghai Jiao Tong University；Shanghai AI Laboratory；Krea AI；Hugging Face；Shanghai Innovation Institute；Tongyi Lab；The University of Hong Kong
- **分类：** `world-model` · 相邻路线 · benchmark
- **核心内容：** 为弥补现有世界模型评测只看单条视频是否合理、不检验重复生成能否复现正确未来分布的缺口，作者提出「概率对齐」准则并发布 PAWBench：50 个人工整理场景分 8 类机制，其中 PAW-Calibration（掷硬币、转盘等 25 个有解析参考分布的场景）用总变差距离衡量概率质量是否对齐，PAW-Coverage（碰撞、稳定性等 25 个场景）衡量合理结果的覆盖率；配套 PAWEval 用 Gemini 按场景规则把每条视频映射为终局结果。对 Veo3.1、Kling 3、Cosmos 3、Wan2.2 等 11 个模型每场景采样 50 次，作者报告没有模型同时做到低 TVD、高覆盖与高可判读率，平均 TVD 远高于有限样本基线；PAWEval 与人工判断一致率 81.3%。提示词、初始噪声耦合与 LoRA 数据配比实验显示只有改变训练数据能实质重塑分布。该基准为评估用于规划的世界模型提供了分布层面的视角，但场景为非机器人的通用物理过程、源图像为生成图，与具身决策的直接关联有待验证。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/Andrew0613/PAWBench)；权重 n/a，数据 open，许可 Apache-2.0。探测到的 Wan2.2 仓库非官方；项目页给出官方仓库（含评测器与测试）与 HuggingFace 数据集 Andrew613/PAWBench
- **待核验事项：** 核实 HuggingFace 上 PAWBench 数据的许可条款

### 76. SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deformable-Object Manipulation — 👀 值得关注

- **时间：** 2026-08-19（[arXiv](https://arxiv.org/abs/2608.18701)）
- **评分：** C4（引入策略不可见的物理真值与DSR指标，把交互质量纳入操作评估，可能影响触觉与可变形操作评测。） / E3（三类策略、分布内外与刚柔孪生、感知/控制交叉消融设计严谨，但仅仿真单一技能。） / O4（Apache-2.0代码仓库为实质代码，HuggingFace上有数据集；策略权重未确认。） / T3（拓竞智能与多所高校合作，含罗平、赵鼎等有相关积累的作者，但该团队方向积累难以统一评估。） = **72/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Tuojing Intelligence；Tsinghua University；King’s College London；Southeast University；Stevens Institute of Technology；The Hong Kong University of Science and Technology (Guangzhou)；University of Manchester；Simple AI；Imperial College London；Carnegie Mellon University；Zhejiang University；Beihang University；The University of Hong Kong
- **分类：** `manipulation` · 相邻路线 · benchmark
- **核心内容：** 为解决可变形物体操作只以任务成功评估、无法识别打滑或过度挤压的问题，作者在Isaac Sim/Isaac Lab中构建SoftVTBench：4个诊断套件、40个任务、4000条脚本示范，含体积可变形物体及外观质量匹配的刚体孪生，每回合以20Hz同步多视角RGB、双指触觉图像与标记位移、本体、语言及二值/连续夹爪动作，并另行记录策略不可见的FEM节点状态；基于逐物体标定的形变容限定义DSR（完成任务且峰值形变不超限）。对Diffusion Policy、π0.5与FastWAM的视觉/视触觉变体评测，作者报告12个分布内配置的成功回合中有0.7%–24%超出形变容限；在光照、质量、刚度九种分布外条件下，视触觉变体在六组对比中任务成功率均更高、五组DSR更高，而分布内收益不一致；感知与夹爪控制粒度交叉消融显示触觉增益需与控制粒度匹配才能识别。结果提示过程级评估能暴露成功率掩盖的问题，但全部为仿真、仅抓放技能，触觉为渲染模拟，真机对应性未验证。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/TuojingAI/SoftVTBench)；权重 unknown，数据 open，许可 Apache-2.0。探针发现HF数据集 Arthur12137/SoftVTBench。
- **待核验事项：** 基线策略权重是否随仓库发布

### 77. stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation — 👀 值得关注

- **时间：** 2026-05-20（[arXiv](https://arxiv.org/abs/2605.21800)）
- **评分：** C3（统一数据、基线、规划器与扰动评测的基础设施，对世界模型研究有实用价值，但方法层面无新增。） / E3（以 Push-T/OGB-Cube 复现基线并做分布偏移与扰动分析，均为仿真案例研究。） / O4（MIT 许可的实质代码（350+ 文件）及 HF 上的 Push-T 数据集，未见基线权重发布。） / T5（LeCun 与 Balestriero 团队在 JEPA/世界模型方向有多项标志性成果。） = **72/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Mila & Université de Montréal；New York University；Universidade Federal de Minas Gerais；Independent Researcher；LanceDB；University of Oxford；Brown University
- **分类：** `world-model` · 相邻路线 · infra
- **核心内容：** 为解决世界模型研究代码各自为政、视频数据加载慢、缺少标准化泛化评测的问题，作者发布开源平台 stable-worldmodel（swm）：基于 Lance 列式格式的数据层（支持 MP4、HDF5、LeRobot 转换，本地读取吞吐约为 HDF5 的 3 倍并支持 S3 流式读取）；经测试的世界模型基线（DINO-WM、LeWorldModel、PLDM、TD-MPC2、GCBC 等）与规划求解器（CEM、MPPI、梯度法等）；以及覆盖经典控制、MuJoCo、Atari、OGBench 机器人与 Craftax 的环境套件，可在线施加颜色、纹理、遮挡、质量、摩擦等可控扰动。案例研究中，作者在 Push-T 上用统一配置复现各基线（如 DINO-WM 92%、LeWM 94%），并报告预测误差与规划成败相关性弱、轻微视觉扰动或增加干扰物即导致成功率显著下降。该平台有望降低复现与公平比较成本，但目前评测主要在仿真低维/桌面任务上，真实机器人与 sim-to-real 支持仍是未来工作，平台价值有待社区采用检验。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/galilai-group/stable-worldmodel)；权重 unknown，数据 partial，许可 MIT。HF 数据集 galilai-group/lewm-pusht。
- **待核验事项：** 是否提供基线预训练检查点

### 78. What Matters for Latent Actions in Robot Learning — 👀 值得关注

- **时间：** 2026-08-20（[arXiv](https://arxiv.org/abs/2608.19613)）
- **评分：** C3（系统化实证比较为潜动作方向提供可操作结论，但不提出新模型，增量有限。） / E4（三个基准、多种设计与多种子、代理指标相关分析并有真机验证，覆盖较广。） / O4（MIT许可实质代码，HF上有LAM权重与一份Franka数据。） / T3（复旦、小米汽车等多单位合作，在潜动作与VLA方向有一定相关成果。） = **71/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** College of Intelligent Robotics and Advanced Manufacturing, Fudan University；Xiaomi EV；Tsinghua Shenzhen International Graduate School, Tsinghua University；Research Center for Intelligent Robotics, School of Astronautics, Northwestern Polytechnical University；School of Artificial Intelligence, Wuhan University；Morphi Intelligence Technology Co., Ltd.
- **分类：** `vla` · 相邻路线 · method
- **核心内容：** 为解决潜动作模型（LAM）研究设定不一致、难以判断哪些设计真正影响下游操作的问题，作者把代表性方法统一到预训练LAM、用潜动作微调VLM骨干（Qwen3-VL-4B，OpenVLA-OFT式）、少量动作数据后训练的三阶段流程中，系统比较7种建模范式、21种正则设置和15种集成策略共41种设计，并检验4个代理指标与下游成功率的相关性；Stage II使用约5900万帧无动作视频语料。在LIBERO、LIBERO-Plus与RoboTwin2.0（3个种子平均）上，作者报告LAPO综合最好、DINO特征差分接近，光流类方法最差；正则强度比正则类型更关键，VQ-VAE在LIBERO-Plus零样本扰动下最稳健；仅有视频时LAP优于DAP；潜动作维度存在较优取值；加入OXE扩充Stage II语料在LIBERO-Plus上最多提升9个百分点；Franka真机四任务上潜动作微调版收敛更快。结果为LAM设计提供了实用参考，但结论基于单一骨干与有限基准，真机规模小，扩展规律仅在两档语料上观察。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/XizoB/What-Matters-for-Latent-Actions-in-Robot-Learning)；权重 open，数据 partial，许可 MIT。HF权重 XizoB/LAM；HF数据集 XizoB/franka_20260617_lerobotv2.1（仅真机数据，非完整训练语料）。
- **数据/基准关系：** libero（评测）、open-x-embodiment（预训练）

### 79. Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention for Video Generation and World Models — 👀 值得关注

- **时间：** 2026-08-19（[arXiv](https://arxiv.org/abs/2608.18484)）
- **评分：** C3（免训练稀疏注意力的扎实改进，对具身方向属间接支撑） / E4（四个模型、多种稀疏注意力基线、密度扫描与组件消融，但无具身下游验证） / O4（实质代码 Apache-2.0 公开；方法免训练，无需额外权重） / T3（德州农工团队，相关积累信息有限，按默认值） = **71/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Texas A&M University
- **分类：** `world-model` · 相邻路线 · infra
- **核心内容：** 为解决块稀疏注意力加速视频 Transformer 时，同组查询偏好的键集合不重合、保留注意力质量也不等于保留输出的问题，作者提出免训练的 SparsePR：先按键对采样查询的响应对 K/V 分组，再按查询对键组中心的响应对查询分组以共享路由；随后对少量探针查询计算精确注意力，用加权岭回归拟合稀疏输出到残差的仿射映射并补偿其余查询。在 HunyuanVideo、Wan2.2 与两个物理世界模型 Cosmos-Predict2.5、Cosmos3-Nano 上，作者报告在约 22% 执行对密度下未探针查询的注意力输出误差比语义分组无校正降低 61.6–90.5%，端到端加速 1.48–2.61 倍，与稠密参考的 PSNR 为 24.42–31.84 dB，VBench/PBench 质量接近稠密，并对分组、探针选择与校正形式做了消融。该结果提示这类加速可降低视频世界模型推理成本，但它是通用视频生成基础设施，未在机器人规划或策略评估等下游任务上验证。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/PardisTaghavi/SparsePR)；权重 n/a，数据 n/a，许可 Apache-2.0。免训练方法，仓库含实现代码

### 80. KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding — 👀 值得关注

- **时间：** 2026-07-22（[arXiv](https://arxiv.org/abs/2607.19876)）
- **评分：** C3（去除 IDM 混淆的闭环评测思路清晰，补充了世界模型物理可执行性评测，属扎实的基准增量。） / E3（有与 IDM 的鲁棒性对比、深度敏感性分析和多模型多套件评测，但全部在 ManiSkill3 仿真且模型池较小。） / O4（代码仓库为 MIT 许可且含实质代码，HF 提供 KineBench 数据集。） / T4（TeleAI（李学龙、白辰甲）等团队在具身智能方向有可核实的持续产出。） = **69/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Institute of Artificial Intelligence (TeleAI), China Telecom, China；National University of Singapore, Singapore；Fudan University, China；Shenzhen Research Institute of Northwestern Polytechnical University, China；Tsinghua University, China
- **分类：** `world-model` · 相邻路线 · benchmark
- **核心内容：** 为解决闭环评测具身世界模型时依赖逆动力学模型（IDM）提取动作、导致无法区分世界模型错误与提取器错误的问题，KineBench 用微调 YOLO 分割、MoGeV2 度量深度与 FoundationPose 6D 跟踪组成显式运动学 grounding 管线，从生成视频逐帧提取末端位姿后在 ManiSkill3 中执行，并引入 SPARC 平滑度与 Maruyama 可操作度两项 3D 运动学指标。基准包含 20 个操作任务和基础执行、任务迁移、视觉 OOD、复杂度缩放四个套件。作者报告该管线在未见任务轨迹上的位姿误差低于 Dino3DFlowIDM；评测 Wan2.1/2.2、CogVideoX 及 LoRA 变体发现，接触丰富任务掉点明显，视觉 OOD 下精细可供性定位退化，数据/训练量的收益随任务复杂度呈非线性甚至为负。该结果提示显式几何 grounding 更易诊断，但管线本身仍含学习模块，且仅在仿真、单一夹爪本体和有限模型池上验证。
- **发表状态（核验：2026-10-22）：** ECCV 2026
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/minecraft-zzz/KineBench)；权重 n/a，数据 open，许可 MIT。数据集见 huggingface.co/datasets/Zorkzak/KineBenchDatasets。
- **数据/基准关系：** maniskill-3（评测）

### 81. Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models — 👀 值得关注

- **时间：** 2026-05-29（[arXiv](https://arxiv.org/abs/2605.31158)）
- **评分：** C3（针对交互式视频世界模型的系统级推理加速，工程价值明确，但与具身控制关联间接、方法为已有加速技术的自适应组合。） / E3（两个开源世界模型、三个基线与组件消融，但仅有视觉质量/效率指标，无下游具身任务验证。） / O4（有 MIT 许可的实质代码仓库；方法免训练，无需额外权重或数据。） / T4（浙大与 NVIDIA（含谢恩泽）在视频生成与高效模型方向有可核实积累。） = **69/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Zhejiang University；NVIDIA
- **分类：** `world-model` · 相邻路线 · infra
- **核心内容：** 为解决交互式视频世界模型在长轨迹生成时因上下文增长、二次注意力和多步去噪导致推理昂贵（HY-WorldPlay 单张 A100 生成 10 秒视频超 200 秒）的问题，作者提出免训练加速框架 Light Interaction：利用相机位姿感知的检索相似度判断"新探索"还是"回访"，新探索时丢弃检索到的空间记忆、按局部潜变量动态调整时间窗；回访时复用早期去噪步输出近似中间步；并把 3D 块稀疏注意力适配到自回归设置，仅对历史视觉 KV 稀疏化，以 Triton 融合算子消除 gather/scatter 开销。在 HY-WorldPlay（8B）与 Matrix-Game-3.0（5B）上、基于 VBench 200 个图文对，作者报告 HY-WorldPlay 加速 2.59×、对原模型 PSNR 24.81、峰值显存降约 22 GB、VBench 0.8220；Matrix-Game-3.0 加速 1.61×，但自一致性指标不及 TeaCache。对照为 SVG、LongCat BSA、TeaCache，并有单组件与留一消融。结果提示交互轨迹信息可用于自适应算力分配，但评测仅限视觉质量与延迟，未验证对具身决策或策略训练的下游影响，且依赖可用的相机位姿信号。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/2843721358l-del/Light-Interaction-Project)；权重 n/a，数据 n/a，许可 MIT。免训练方法，使用 HY-WorldPlay 与 Matrix-Game-3.0 公开权重。

### 82. Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data — 👀 值得关注

- **时间：** 2026-08-03（[arXiv](https://arxiv.org/abs/2608.02580)）
- **评分：** C4（首次在万小时级规模检验人到机器人合成数据对 VLA 预训练的价值，并给出可解耦的泛化评测，资源性增量明确。） / E4（控制样本量的配比实验、11 轴扰动分解、EBench、流水线消融与真机五任务，但仅单一模型架构。） / O2（仅有项目博客，探测到的 mink 仓库是第三方依赖而非官方代码，数据未发布。） / T4（人大 AIM3、通义 Qwen 团队与 BIGAI 在多模态与具身方向有可核实积累。） = **68/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** AIM3 Lab, Renmin University of China；Qwen Team, Alibaba Inc.；ShanghaiTech University；Beijing Institute for General Artificial Intelligence (BIGAI)；Beijing University of Aeronautics and Astronautics
- **分类：** `manipulation` · 相邻路线 · data
- **核心内容：** 为弥补真机演示数据昂贵、多样性受限的缺口，作者构建 Ego2Robot 流水线：把手部位姿重定向为末端执行器轨迹，用 SAM 3 分割、ProPainter 去除人手并经基座位姿搜索与 IK 做深度感知的机械臂渲染，再在轨迹、帧、片段三级做质量筛选；既支持带手部标注的数据集，也支持经 WiLoR/DynHaMR 估计手部的野外视频，由约 1,940 小时视频生成覆盖 15 种机械臂形态的 18,561 小时数据。评测上把 RoboTwin 2.0 扩展为外观、布局、本体、任务语义 11 个独立扰动轴，并补充 EBench。以 Qwen3.5-4B+DiT 的 VLA 在相同样本量下对比，作者报告：Ego2R 与真机数据（DROID+AgiBot World+InternData）1:1 混合预训练使 RoboTwin 随机化设置由 50.9% 升至 53.5%，未见物体与相机偏移等轴提升明显，EBench 3:1 混合提升 12.1 分；ARX ACone 真机五任务中加入转换后的人手 play 数据效果最好。该结果提示合成数据主要提升视觉与语义泛化，但重定向只到平行夹爪、渲染存在伪影，Franka 等大运动学差异本体仍接近失败，数据与代码尚未公开。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 未找到官方仓库链接，无仓库链接；权重 none，数据 none，许可 unknown。探测命中 kevinzakka/mink（IK 库，第三方依赖），并非本文官方仓库；论文只给出项目博客。
- **数据/基准关系：** ego2robot-data（提出）、droid（预训练）、agibot-world（预训练）
- **待核验事项：** 18,561 小时合成数据与流水线代码是否会公开

### 83. ORCA: A Platform for Open-Source Dexterity Research — 👀 值得关注

- **时间：** 2026-06-12（[arXiv](https://arxiv.org/abs/2606.14561)）
- **评分：** C3（把开源灵巧手软硬件整合进 LeRobot 生态是实用的基础设施贡献，但技术新意有限。） / E2（仅展示单一任务的端到端工作流，缺少定量评测与基线对比。） / O5（GitHub 组织下 orca_core、orca_retargeter、orcahand_description 等实质代码与 CAD/打印文件公开，MIT 许可，附安装与教程。） / T3（团队与 ETH 及初创公司 Orca Dexterity 相关，在开源灵巧手硬件上有一定积累。） = **67/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** University of Oxford；ETH Zurich；Orca Dexterity
- **分类：** `teleoperation` · 相邻路线 · infra
- **核心内容：** 为解决灵巧手研究中控制、仿真、遥操作和重定向代码分散、与主流机器人学习生态脱节的问题，作者发布 orca 学习栈：基于开源、可 3D 打印、肌腱驱动的 17 自由度 Orcahand，拆分为 orca_core（真机与仿真共用的关节空间接口、标定与张紧）、orca_sim（MuJoCo 手与 Gymnasium 任务环境）、orca_arm（OpenArm 双臂与 Franka 平台描述文件）和 orca_teleop（支持摄像头、VR 头显、动捕手套的 MANO 关键点重定向与遥操作），并原生对接 LeRobot 的数据、训练与评测流程。论文以 Meta Quest 3 遥操作采集手内重定向示教、用 LeRobot 训练行为克隆策略并评测的端到端流程作为演示。该工作降低了灵巧手进入通用机器人学习管线的门槛，但论文主要是系统描述，缺少系统性定量实验与对比；作者也承认肌腱耦合与软指接触仿真仍很粗略，软件分为四个子包可能增加使用摩擦。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/orcahand/orca_core)；权重 n/a，数据 unknown，许可 MIT。探测未发现仓库；核对 GitHub 组织 orcahand，含 orca_core（MIT）、orca_sim、orca_teleop、orca_retargeter、硬件 CAD 等仓库。
- **待核验事项：** orca_sim 与 orca_teleop 仓库的许可证文件

### 84. AlayaWorld: Interactive Long-Horizon World Modeling -- Full Technical Report — 👀 值得关注

- **时间：** 2026-07-20（[arXiv](https://arxiv.org/abs/2607.18367)）
- **评分：** C3（全栈开源的交互式视频世界模型，工程整合扎实，但方法多为已有技术组合，具身相关性有限。） / E3（单一 iWorld-Bench 上与多个开源世界模型对比并有人工盲评，缺少组件消融与具身下游验证。） / O4（代码、多阶段权重与训练数据均已发布，但为自定义许可，条款未核对。） / T3（Alaya Lab 在交互式世界模型方向有一定成果，信息有限，默认 3。） = **66/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Alaya Lab
- **分类：** `world-model` · 相邻路线 · model
- **核心内容：** 为让视频世界模型同时具备交互控制、空间一致、长时稳定与低延迟，Alaya Lab 提出 AlayaWorld：在 LTX-2.3 视频 DiT 上分三阶段训练——双向全参微调适配领域；自回归阶段加入历史压缩模块、基于深度重投影的空间记忆缓存、AdaLN 相机控制与 next forcing 头，并用受损历史与自身 rollout 残差做防漂移训练；最后结合 DMD、self-forcing++ 与一致性蒸馏把每块采样步数从约 30 降到 4。训练数据混合 Sekai-Real、SpatialVid、RealEstate10K、DL3DV 等真实视频与自有游戏录像、生成事件视频，并以 VLM 做分轨时间段标注。在 iWorld-Bench（480p、4 步）上，作者报告亮度一致性、轨迹精度、记忆对称性等多数指标优于 Cosmos、HunyuanVideo-1.5、Yume 1.5、Matrix-Game 2.0、HY-World 1.5，图像质量略低于部分基线；另参与 WorldMark 竞技场人工盲评。框架代码、权重与数据已开源，但应用主要是游戏与场景漫游，动作限于相机轨迹与文本提示，未验证对具身决策或机器人控制的作用，也缺少组件消融。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/AlayaLab/AlayaWorld)；权重 open，数据 open，许可 custom。HF 发布多阶段权重与 AlayaWorld-v1.1-data 数据集。
- **待核验事项：** 自定义许可证是否允许研究/商业使用；以 PDF 核对作者单位

### 85. Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots — 👀 值得关注

- **时间：** 2026-07-02（[arXiv](https://arxiv.org/abs/2607.02501)）
- **评分：** C3（把 llama.cpp 式运行时扩展到 VLA 与 WAM，工程价值明确但方法增量有限。） / E3（覆盖 5 个模型与多种量化配置，但只与各自 Python 基线归一化比较，任务与硬件设置披露较少。） / O4（仓库含实质代码（Apache-2.0），HF 提供转换后权重。） / T3（东南大学、南京大学、微软研究院与清华 AIR 在系统/边缘推理方向有一定积累。） = **66/100**；**优先级：** 👀 值得关注
- **作者/团队单位：** Southeast University；Nanjing University；Microsoft Research；Institute for AI Industry Research (AIR), Tsinghua University
- **分类：** `vla` · 相邻路线 · infra
- **核心内容：** 为解决具身模型部署依赖各自的 Python 栈、后端假设和机器人侧胶水代码，难以在异构边缘设备上闭环运行的问题，Embodied.cpp 在分析代表性 VLA 与世界-动作模型（WAM）架构后，把共享执行路径组织为输入适配、序列构建、骨干执行、头插件和部署适配五层，提供模块化多速率执行、面向批大小 1 的时延优先融合推理，以及可扩展的算子与 I/O 接口。作者在 pi0.5、GR00T N1.7、HY-VLA 三个 VLA 与 Cosmos3、LingBot-VA 两个 WAM 上与 Python 实现对比，报告归一化推理时延降低（HY-VLA 降至约 0.37–0.48）、8/6/4 比特配置显存显著下降，成功率多数保持在基线的 0.9 以上，但 pi0.5 的 4 比特配置降至 0.70；LingBot-VA 成功率 98% 对 100%、显存从 24.75 GB 降至 16.44 GB。该结果提示统一运行时可降低部署门槛，但评测以归一化指标为主，任务环境与硬件细节披露有限，真机多平台验证不足。
- **发表状态（核验：2026-10-22）：** arXiv 预印本；未检索到正式录用记录
- **开源状态（首次核查：2026-10-22；last_check：2026-10-22）：** 已公开实质相关代码，[仓库](https://github.com/SEU-PAISys/Embodied.cpp)；权重 open，数据 n/a，许可 Apache-2.0。HF 有 SEU-PAISys/Embodied.cpp 模型文件。
- **待核验事项：** 确认闭环成功率评测所用的仿真环境/真机与硬件平台

## 观察中 / 暂不评级

| 论文 | 日期 | 类别 | 总分 | 代码 | 备注 |
|---|---|---|---|---|---|
| [EmbodiedSkills: A Unified Framework for Orchestrating, Training, and Deploying VLA Agents](https://arxiv.org/abs/2609.01281) | 2026-09-01 | `vla` | 63 | 已公开实质相关代码 | 核实仓库是否提供训练好的世界动作模型权重与分支训练数据，以及许可证 |
| [RoboGesture: Real-Time Semantic-aligned Co-Speech Gestures Generation for Humanoid Interaction](https://arxiv.org/abs/2608.28693) | 2026-08-27 | `sim2real` | 63 | 部分开放 |  |
| [RoboEdit: Turning Human Manipulation Videos into Scalable Robot Experience](https://arxiv.org/abs/2608.18948) | 2026-08-19 | `manipulation` | 63 | 未找到官方仓库链接 | RoboEdit-14M数据集与模型是否计划公开 |
| [RoboStriker: Latent-Space Strategic Games for Autonomous Humanoid Boxing](https://arxiv.org/abs/2608.16195) | 2026-08-17 | `rl-il` | 63 | 未找到官方仓库链接 | 摘要所称 RoboStriker 代码/项目页的实际链接与内容 |
| [Learning How the World Evolves: Extrapolative Video World Models via Latent Dynamics Reasoning](https://arxiv.org/abs/2608.09926) | 2026-08-10 | `world-model` | 63 | 部分开放 | 仓库是否包含训练代码（探测只有 7 个代码文件） |
| [Orca: The World is in Your Mind](https://arxiv.org/abs/2606.30534) | 2026-06-29 | `foundation-general` | 63 | 部分开放 | 真机 5 个任务的试验次数与具体成功率（附录 Table E3）；仓库许可证与训练代码发布情况 |
| [Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models](https://arxiv.org/abs/2606.25473) | 2026-06-24 | `world-model` | 63 | 已公开实质相关代码 | 确认 Causal-rCM 检查点（Wan2.1 蒸馏模型、交互式 Cosmos 3）是否公开下载 |
| [World Value Models for Robotic Manipulation](https://arxiv.org/abs/2606.24742) | 2026-06-23 | `world-model` | 63 | 找到仓库但未发现实质相关代码 | 阅读 PDF 核对策略学习（AWR / Filtered BC）在仿真与真机上的具体成功率与试验次数；核对项目页 VOC 表的列序与基线对应关系，以及所用视频  |
| [Sensorimotor World Models: Perception for Action via Inverse Dynamics](https://arxiv.org/abs/2606.20104) | 2026-06-18 | `world-model` | 63 | 已公开实质相关代码 | 是否提供训练好的模型权重 |
| [HumanScale: Egocentric Human Video Can Outperform Real-Robot Data for Embodied Pretraining](https://arxiv.org/abs/2606.20521) | 2026-06-18 | `foundation-general` | 63 | 找到仓库但未发现实质相关代码 | 机器人数据预训练模型的真机成功率未报告，需核对 PDF 是否另有对照；HumanNet 语料与本文后训练验证代码的发布情况 |
| [World Action Models: A Survey](https://arxiv.org/abs/2606.20781) | 2026-06-18 | `tutorials` | 63 | 找到仓库但未发现实质相关代码 |  |
| [Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation](https://arxiv.org/abs/2606.17030) | 2026-06-15 | `world-model` | 63 | 未找到官方仓库链接 | 是否发布模型权重或 EWK 数据；是否有消融与下游策略训练实验 |
| [WorldOlympiad: Can Your World Model Survive a Triathlon?](https://arxiv.org/abs/2606.11129) | 2026-06-09 | `world-model` | 63 | 已公开实质相关代码 | 仓库与数据集的许可证 |
| [Latent Spatial Memory for Video World Models](https://arxiv.org/abs/2606.09828) | 2026-06-08 | `world-model` | 63 | 已公开实质相关代码 | 仓库是否提供训练好的权重与训练脚本 |
| [Tactile Sim2Real without Tactile Simulation via Bottlenecked Latent Reconstruction](https://arxiv.org/abs/2608.15897) | 2026-08-16 | `sim2real` | 62 | 未找到官方仓库链接 |  |
| [MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.09215) | 2026-06-08 | `world-model` | 62 | 未找到官方仓库链接 | 是否有官方项目页或代码发布计划 |
| [Video2Sim2Real: Full-Stack Autonomous Dexterous Skill Acquisition from a Single Human Video](https://arxiv.org/abs/2606.08828) | 2026-06-07 | `sim2real` | 62 | 未找到官方仓库链接 | 项目网站是否计划发布代码 |
| [ActionMap: Robot Policy Learning via Voxel Action Heatmap](https://arxiv.org/abs/2606.06904) | 2026-06-05 | `vla` | 62 | 未找到官方仓库链接 | 项目页是否给出代码或权重 |
| [Dreaming when Necessary: Advancing World Action Models with Adaptive Multi-Modal Reasoning](https://arxiv.org/abs/2606.07089) | 2026-06-05 | `world-model` | 62 | 未找到官方仓库链接 | 代码是否已公开发布 |
| [TAGA: Terrain-aware Active Gaze Learning for Generalizable Agile Humanoid Locomotion](https://arxiv.org/abs/2606.05880) | 2026-06-04 | `locomotion` | 62 | 未找到官方仓库链接 | 是否发布代码 |
| [GeoAlign: Beyond Semantics with State-Guided Spatial Alignment in VLA Models](https://arxiv.org/abs/2606.03240) | 2026-06-02 | `vla` | 62 | 未找到官方仓库链接 | 项目页 chenyizhi123.github.io/geoalign-project 是否提供代码与权重 |
| [Affordance2Action: Task-Conditioned Scene-level Affordance Grounding for Real-Time Manipulation](https://arxiv.org/abs/2606.04172) | 2026-06-02 | `manipulation` | 62 | 未找到官方仓库链接 | A2A-Bench 数据与代码是否已在项目页 arc-l.github.io/a2a 公开 |
| [Intercepting the Future: Latent-Space Predictive World Model for Dynamic VLA Manipulation](https://arxiv.org/abs/2606.02486) | 2026-06-01 | `vla` | 62 | 未找到官方仓库链接 | 是否会发布代码与世界模型权重；预训练所用六个公开视频数据源的具体名单（Table 7） |
| [Hide-and-Seek in Trajectories: Discovering Failure Signals for VLA Runtime Monitoring](https://arxiv.org/abs/2605.30834) | 2026-05-29 | `vla` | 62 | 找到仓库但未发现实质相关代码 | 仓库何时放出训练代码与采集的 rollout 数据 |
| [Reinforcing VLAs in Task-Agnostic World Models](https://arxiv.org/abs/2605.12334) | 2026-05-12 | `world-model` | 62 | 未找到官方仓库链接 | 是否开源世界模型与训练代码；真机四项任务的具体成功率（缓存未含 Table 4 数值） |
| [GOAG: Generative and Object-Agnostic Grasp Planner for Dexterous Robotic Manipulation](https://arxiv.org/abs/2608.19759) | 2026-08-20 | `manipulation` | 60 | 已公开实质相关代码 | 仓库许可证 |
| [CoToGrasp: Contact-Topology-Conditioned Dexterous Grasp Synthesis via Canonical Workspace Learning](https://arxiv.org/abs/2608.19776) | 2026-08-20 | `manipulation` | 60 | 已公开实质相关代码 | 仓库许可证 |
| [PRISM: Precision and contact-rich Real-world Industrial Skill dataset with Multimodal sensing](https://arxiv.org/abs/2608.17962) | 2026-08-18 | `manipulation` | 60 | 找到仓库但未发现实质相关代码 | ModelScope数据集是否完整可下载（5000条轨迹、全部模态）及许可证 |
| [Zetta $\zeta$: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence](https://arxiv.org/abs/2608.16590) | 2026-08-17 | `vla` | 60 | 未找到官方仓库链接 | 项目页是否发布 Zetta / Z-Infra 代码；是否有真机实验（缓存文本未见） |
| [Does VLA Even Know the Basics? Measuring Commonsense and World Knowledge Retention in Vision-Language-Action Models](https://arxiv.org/abs/2606.19297) | 2026-06-17 | `vla` | 60 | 已公开实质相关代码 | 项目页称已被 EMNLP 2026 主会录用，需以官方录用页或 arXiv comment 确认；HuggingFace 任务资产是否发布 |
| [MonoDuo: Using One Robot Arm to Learn Bimanual Policies](https://arxiv.org/abs/2605.29298) | 2026-05-28 | `teleoperation` | 60 | 未找到官方仓库链接 | 项目页 bimanual-monoduo.github.io 是否提供代码或数据 |
| [GesVLA: Pointing Gesture Grounding for Vision-Language-Action Models](https://arxiv.org/abs/2605.22812) | 2026-05-21 | `vla` | 60 | 已公开实质相关代码 | 仓库是否包含训练代码与数据生成管线、是否发布权重；仓库许可证 |
| [SparkVLA: Stop-Aware Hierarchical VLA with Adaptive Action Chunking for Long-Horizon Manipulation](https://arxiv.org/abs/2608.16172) | 2026-08-17 | `vla` | 59 | 未找到官方仓库链接 | 项目页是否后续放出代码与权重；真机对比表中 48.0% 基线的具体模型名称（缓存文本缺失） |
| [DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for Cross-Embodiment Manipulation](https://arxiv.org/abs/2608.06374) | 2026-08-06 | `vla` | 59 | 未找到官方仓库链接 | 代码与权重是否发布；作者团队在跨本体操作方向的既往成果 |
| [World-to-Wrist: Task-Conditioned Future Wrist Modeling for Fine-Grained Robot Manipulation](https://arxiv.org/abs/2608.05369) | 2026-08-05 | `vla` | 59 | 未找到官方仓库链接 | 代码、权重与 W2-CoT 标注是否发布；通讯作者团队在机器人操作方向的既往成果 |
| [SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space](https://arxiv.org/abs/2608.01397) | 2026-08-02 | `world-model` | 59 | 找到仓库但未发现实质相关代码 | 作者单位（需查 PDF）；代码与权重是否按承诺发布 |
| [StairMaster: Learning to Conquer Risky Hollow Stairs for Agile Quadrupedal Robots](https://arxiv.org/abs/2606.25765) | 2026-06-24 | `locomotion` | 59 | 未找到官方仓库链接 | 以 PDF 核对全部作者单位（HTML 仅显示上海交通大学）；项目页是否后续放出代码 |
| [SkyJEPA: Learning Long-Horizon World Models for Zero-Shot Sim-to-Real Control of Quadrotors](https://arxiv.org/abs/2606.23444) | 2026-06-22 | `sim2real` | 59 | 未找到官方仓库链接 | 是否发布代码与仿真数据生成管线 |
| [SWAP: Symmetric Equivariant World-Model for Agile Robot Parkour](https://arxiv.org/abs/2606.19928) | 2026-06-18 | `locomotion` | 59 | 未找到官方仓库链接 | 是否发布代码 |
| [ContactWorld: What Matters in Vision-Tactile World Models for Contact-Rich Manipulation](https://arxiv.org/abs/2606.13877) | 2026-06-11 | `world-model` | 59 | 未找到官方仓库链接 | 项目网站是否发布基准代码、仿真环境与数据；仿真任务所用的仿真器 |
| [3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training](https://arxiv.org/abs/2606.04436) | 2026-06-03 | `vla` | 59 | 未找到官方仓库链接 | 代码与权重是否已公开；通讯作者团队在 VLA 方向的已有成果 |
| [Gaze2Act: Gaze-Conditioned Vision-Language-Action Policies for Interactive Robot Manipulation](https://arxiv.org/abs/2605.30282) | 2026-05-28 | `vla` | 59 | 未找到官方仓库链接 | 项目页 zuo-kuangji.github.io/Gaze2Act 是否提供代码 |
| [Spatial Memory for Out-of-Vision Manipulation in Vision-Language-Action](https://arxiv.org/abs/2605.22283) | 2026-05-21 | `vla` | 59 | 未找到官方仓库链接 | 代码是否已按承诺发布 |
| [HapTile: A Haptic-Informed Vision-Tactile-Language-Action Dataset for Contact-Rich Imitation Learning](https://arxiv.org/abs/2606.04825) | 2026-06-03 | `teleoperation` | 58 | 找到仓库但未发现实质相关代码 | 数据集许可证；采集与训练代码何时开放 |
| [PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration](https://arxiv.org/abs/2608.21031) | 2026-08-21 | `manipulation` | 57 | 未找到官方仓库链接 |  |
| [H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models](https://arxiv.org/abs/2608.13049) | 2026-08-13 | `world-model` | 57 | 找到仓库但未发现实质相关代码 | 评测代码与 240 个案例标注是否发布 |
| [WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reactivity](https://arxiv.org/abs/2608.02603) | 2026-08-03 | `world-model` | 57 | 找到仓库但未发现实质相关代码 | 基准用例与评测代码是否发布 |
| [Wonder: Video World Model Done Better](https://arxiv.org/abs/2607.26037) | 2026-07-28 | `world-model` | 57 | 未找到官方仓库链接 | 确认各组件（坐标场、稀疏记忆、蒸馏改进）的消融结果 |
| [MemLearner: Learning to Query Context memory for Video World Models](https://arxiv.org/abs/2606.31734) | 2026-06-30 | `world-model` | 57 | 未找到官方仓库链接 | 项目页是否后续发布代码或 Unreal Engine 数据集 |
| [ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning](https://arxiv.org/abs/2606.17011) | 2026-06-15 | `rl-il` | 57 | 未找到官方仓库链接 | 每项任务的评测试验次数 |
| [Targeting World Models to Compromise Robot Learning Pipelines](https://arxiv.org/abs/2606.09499) | 2026-06-08 | `world-model` | 57 | 未找到官方仓库链接 | 录用年份（arXiv 注释仅写 CoRL Spotlight）；微调的 Cosmos LIBERO 模型是否已上传 |
| [MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation](https://arxiv.org/abs/2606.06139) | 2026-06-04 | `locomotion` | 57 | 未找到官方仓库链接 | 真机平台型号与是否开源代码 |
| [DexFuture: Hierarchical Future-State Visuomotor Targeting for Bimanual Dexterous Tool Use](https://arxiv.org/abs/2606.05699) | 2026-06-04 | `manipulation` | 57 | 未找到官方仓库链接 | 项目网站是否提供代码或数据链接 |
| [HomeWorld: A Unified Floorplan-to-Furnished Framework for Generating Controllable, Densely Interactive Whole-Home Scenes](https://arxiv.org/abs/2606.06390) | 2026-06-04 | `scene` | 57 | 找到仓库但未发现实质相关代码 | 30 万户型数据集与 5K 场景是否已发布及其许可 |
| [Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum](https://arxiv.org/abs/2605.21133) | 2026-05-20 | `manipulation` | 57 | 未找到官方仓库链接 | 是否开源代码；表 1 第二个数据驱动基线的确切名称（缓存文本缺失） |
| [Hand-in-the-Loop: Improving VLA Policies for Dexterous Manipulation via Seamless Hand-Arm Intervention](https://arxiv.org/abs/2605.15157) | 2026-05-14 | `teleoperation` | 57 | 未找到官方仓库链接 | 是否开源介入系统代码与纠错数据 |
| [Towards Human-Like Manipulation through RL-Augmented Teleoperation and Mixture-of-Dexterous-Experts VLA](https://arxiv.org/abs/2603.08122) | 2026-03-09 | `vla` | 57 | 未找到官方仓库链接 |  |
| [H2R-Grounder: A Paired-Data-Free Paradigm for Translating Human Interaction Videos into Physically Grounded Robot Videos](https://arxiv.org/abs/2512.09406) | 2025-12-10 | `manipulation` | 57 | 找到仓库但未发现实质相关代码 |  |
| [Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents](https://arxiv.org/abs/2606.23085) | 2026-06-22 | `manipulation` | 56 | 未找到官方仓库链接 | 是否发布代码与采集的 rollout 数据 |
| [Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement](https://arxiv.org/abs/2606.18953) | 2026-06-17 | `sim2real` | 56 | 未找到官方仓库链接 | 正文表格数值在缓存中缺失，42%/76% 取自摘要 |
| [MAD: Mapping-Aware World Models for Agile Quadrotor Flight](https://arxiv.org/abs/2606.04534) | 2026-06-03 | `navigation` | 56 | 未找到官方仓库链接 | 是否有代码或 DiffAero 扩展模块的开源计划 |
| [BORA: Bridging Offline Reinforcement Learning and Online Residual Adaptation for Real-World Dexterous VLA Models](https://arxiv.org/abs/2605.30226) | 2026-05-28 | `vla` | 56 | 未找到官方仓库链接 | 是否发布代码或数据 |
| [Progress Reward Modeling for Robotic Learning: A Comprehensive Survey](https://arxiv.org/abs/2607.21655) | 2026-07-22 | `tutorials` | 55 | 找到仓库但未发现实质相关代码 |  |
| [EXIMO: VLM Guided Exploration of VLA Policies](https://arxiv.org/abs/2608.19891) | 2026-08-20 | `vla` | 54 | 未找到官方仓库链接 |  |
| [LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories](https://arxiv.org/abs/2608.18618) | 2026-08-19 | `manipulation` | 54 | 未找到官方仓库链接 | 数据集主页 https://zhipeng-tang.github.io/LabDex/ 是否提供数据下载与评测代码 |
| [PartialBiGrasp: Inferring Hidden Local Geometry for Bimanual Grasping from Partial Views](https://arxiv.org/abs/2608.19188) | 2026-08-19 | `manipulation` | 54 | 未找到官方仓库链接 |  |
| [Tac4Loco: Learning Spatiotemporal Plantar Pressure Representations for Humanoid Locomotion](https://arxiv.org/abs/2608.15766) | 2026-08-16 | `locomotion` | 54 | 未找到官方仓库链接 | 官方代码仓库是否发布 |
| [HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments](https://arxiv.org/abs/2608.12860) | 2026-08-13 | `navigation` | 54 | 未找到官方仓库链接 | 录用后是否实际发布代码、场景与回合数据 |
| [DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation](https://arxiv.org/abs/2608.13489) | 2026-08-13 | `world-model` | 54 | 找到仓库但未发现实质相关代码 | 作者单位（论文只署名 DreamX Team；GitHub 组织为 AMAP-ML）；挑战赛结束后权重与推理代码是否发布 |
| [WorldCycle: Self-Verifiable Reinforcement Learning for Long-Horizon Video World Models](https://arxiv.org/abs/2608.04964) | 2026-08-05 | `world-model` | 54 | 未找到官方仓库链接 | CycleBench 与训练代码是否发布；作者团队在世界模型方向的既往成果 |
| [NavVerse: Benchmarking Indoor-to-Outdoor Embodied Navigation in Continuous Robot Simulation](https://arxiv.org/abs/2607.19695) | 2026-07-22 | `navigation` | 54 | 未找到官方仓库链接 | 确认 NavVerse 场景、episode 与评测代码的官方仓库及开放情况 |
| [ERQA-Plus: A Diagnostic Benchmark for Reasoning in Embodied AI](https://arxiv.org/abs/2606.17639) | 2026-06-16 | `scene` | 54 | 未找到官方仓库链接 | GitHub 仓库 LUNAProject22/erqa-plus 是否存在及内容；数据集许可证 |
| [NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation](https://arxiv.org/abs/2606.13494) | 2026-06-11 | `navigation` | 54 | 未找到官方仓库链接 | 项目页是否后续发布代码与模型 |
| [STRIPS-WM: Learning Grounded Propositional STRIPS-style World Models from Images](https://arxiv.org/abs/2606.06832) | 2026-06-05 | `world-model` | 54 | 未找到官方仓库链接 | 项目网站是否提供代码 |
| [PiL-World: A Chunk-Wise World Model for VLA Policy-in-the-Loop Evaluation](https://arxiv.org/abs/2606.05773) | 2026-06-04 | `world-model` | 54 | 未找到官方仓库链接 | 项目页是否提供代码或模型 |
| [CoRe-MoE: Contrastive Reweighted Mixture of Experts for Multi-Terrain Humanoid Locomotion with Gait Adaptation](https://arxiv.org/abs/2606.04718) | 2026-06-03 | `locomotion` | 54 | 未找到官方仓库链接 | 项目主页地址与是否开放代码 |
| [Learning to Evolve: Multi-modal Interactive Fields for Robust Humanoid Navigation in Dynamic Environments](https://arxiv.org/abs/2605.21935) | 2026-05-21 | `navigation` | 54 | 未找到官方仓库链接 | 项目页 ziya-jiang.github.io/MIF-homepage 是否已链接实质代码仓库 |
| [HiTac-WAM: A Hierarchical Tactile World Action Model for Contact-Rich Robot Manipulation](https://arxiv.org/abs/2608.19574) | 2026-08-20 | `manipulation` | 53 | 未找到官方仓库链接 |  |
| [MILD: Tractable Terrain Modeling for Learning Improved Bipedal Locomotion on Deformable Surfaces](https://arxiv.org/abs/2608.19955) | 2026-08-20 | `locomotion` | 53 | 未找到官方仓库链接 |  |
| [DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation](https://arxiv.org/abs/2608.20114) | 2026-08-20 | `world-model` | 53 | 未找到官方仓库链接 | 核实 ARMDOG 数据集与 DECOWAM 代码是否有公开发布计划或链接 |
| [Dream2Reward: Transition-Alignment Reward Models from Positive Demonstrations for Robotic Manipulation](https://arxiv.org/abs/2608.18787) | 2026-08-19 | `rl-il` | 53 | 未找到官方仓库链接 |  |
| [Prism-GRPO: Faster VLA Policy Optimization via Splitting Same-outcome Groups](https://arxiv.org/abs/2608.17423) | 2026-08-18 | `rl-il` | 53 | 未找到官方仓库链接 |  |
| [EATR-Stereo: Embodiment-Aware Routing of Paired Stereo Evidence for Humanoid Vision-Language-Action Control](https://arxiv.org/abs/2608.17453) | 2026-08-18 | `vla` | 53 | 未找到官方仓库链接 |  |
| [StellaVLA: In-Context Structured Demonstration for Generalizable Vision-Language-Action Models](https://arxiv.org/abs/2608.11671) | 2026-08-12 | `vla` | 53 | 未找到官方仓库链接 | 作者单位（HTML 未列出，需查 PDF；首页指向 stelledge.com 博客）；是否计划发布代码与检查点 |
| [Hidden in Plain Sight: Diffusion-Based Unrestricted Robotic Attacks on Vision-Language-Action Models](https://arxiv.org/abs/2608.10393) | 2026-08-11 | `vla` | 53 | 未找到官方仓库链接 | 是否会发布代码或贴片；真机实验的试验次数和定量结果 |
| [AtlasVLA: Persistent World-Ego State Modeling for Vision-Language-Action Models](https://arxiv.org/abs/2608.06729) | 2026-08-07 | `vla` | 53 | 未找到官方仓库链接 | 是否计划开源代码与权重 |
| [Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation](https://arxiv.org/abs/2606.18960) | 2026-06-17 | `world-model` | 53 | 未找到官方仓库链接 | 是否发布代码与模型 |
| [Discrete-WAM: Unified Discrete Vision-Action Token Editing for World-Policy Learning](https://arxiv.org/abs/2606.05645) | 2026-06-04 | `world-model` | 53 | 未找到官方仓库链接 | 完整作者单位列表（正文仅署 Xiaomi EV）；是否开源代码或模型 |
| [GeoSem-WAM: Geometry- and Semantic-Aware World Action Models](https://arxiv.org/abs/2606.03188) | 2026-06-02 | `world-model` | 53 | 未找到官方仓库链接 | 是否发布代码与权重 |
| [ElegantVLA: Learning When to Think for Efficient Vision-Language-Action Models](https://arxiv.org/abs/2605.29438) | 2026-05-28 | `vla` | 53 | 未找到官方仓库链接 | 是否计划开源调度器代码 |
| [SPRINT: Efficient Spectral Priors for Humanoid Athletic Sprints](https://arxiv.org/abs/2605.28549) | 2026-05-27 | `locomotion` | 53 | 未找到官方仓库链接 | 是否开源代码与谱先验模型；团队在人形运动控制方向的既往成果 |
| [Learning-Based Behavior Planning for Automated Driving: Real-World Integration and Deployment](https://arxiv.org/abs/2608.12198) | 2026-08-12 | `navigation` | 52 | 部分开放 | OpenADS 中是否包含行为规划网络与训练代码 |
| [Robust Brachiation on a Life-Sized Dual-Arm Robot Using Waypoint-Guided Reinforcement Learning](https://arxiv.org/abs/2608.17320) | 2026-08-18 | `locomotion` | 51 | 未找到官方仓库链接 |  |
| [ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models](https://arxiv.org/abs/2608.13438) | 2026-08-13 | `world-model` | 51 | 未找到官方仓库链接 |  |
| [Lost in Reconstruction: Aligning Action Representations with Language in Vision-Language-Action Models](https://arxiv.org/abs/2608.10484) | 2026-08-11 | `vla` | 51 | 未找到官方仓库链接 | 是否发布 SALT 的 tokenizer 代码与权重 |
| [Toward the Cognitive--Physical Limits of Embodied Intelligence through a World-Model-Centric Autonomous Racing Agent](https://arxiv.org/abs/2608.10618) | 2026-08-11 | `world-model` | 51 | 未找到官方仓库链接 | 是否有真车闭环对抗比赛的定量结果；与已有赛车栈（如 Indy Autonomous Challenge 队伍）的对比 |
| [Self-Evolving Embodied Agents via Skill-Harness Evolution](https://arxiv.org/abs/2608.11350) | 2026-08-11 | `foundation-general` | 51 | 未找到官方仓库链接 |  |
| [Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control](https://arxiv.org/abs/2607.25337) | 2026-07-28 | `world-model` | 51 | 未找到官方仓库链接 | 论文所列仓库 HKBU-KnowComp/Temporal-Distance-JEPA 无法访问，需复查是否公开 |
| [TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies](https://arxiv.org/abs/2606.06491) | 2026-06-04 | `vla` | 51 | 未找到官方仓库链接 | 真机实验的具体成功率数值（缓存中数字缺失） |
| [TTT-VLA: Test-Time Latent Prompt Optimization for Vision-Language-Action Models](https://arxiv.org/abs/2606.03127) | 2026-06-02 | `vla` | 51 | 未找到官方仓库链接 | 是否发布代码与训练好的提示/权重 |
| [CLAW: Learning Continuous Latent Action World Models via Adversarial Latent Regularization](https://arxiv.org/abs/2606.04130) | 2026-06-02 | `world-model` | 51 | 未找到官方仓库链接 | 对抗正则的消融结果（缓存中未见）；是否发布代码 |
| [Imagine2Real: Towards Zero-shot Humanoid-Object Interaction via Video Generative Priors](https://arxiv.org/abs/2605.22272) | 2026-05-21 | `locomotion` | 51 | 未找到官方仓库链接 | 官方代码与预训练检查点是否公开 |
| [Safe and Steerable Geometric Motion Policies for Robotic Dexterous Manipulation](https://arxiv.org/abs/2605.21811) | 2026-05-20 | `manipulation` | 51 | 未找到官方仓库链接 | 项目页 tml.stanford.edu/safe-pbds 是否提供代码；真机抓取是否与学习型或优化型抓取基线做了定量对比 |
| [LIBERO-VIFO: Benchmarking the Capability and Safety of Visual Cue Following in Vision-Language-Action Models](https://arxiv.org/abs/2608.17600) | 2026-08-18 | `vla` | 48 | 未找到官方仓库链接 | 作者单位（HTML 未给出，需查 PDF）；基准资产与评测代码是否公开 |
| [NebulaVLA: A Dual-Frequency Vision-Language-Action Model With Guide Action for Robotic Manipulation](https://arxiv.org/abs/2608.16503) | 2026-08-17 | `vla` | 48 | 未找到官方仓库链接 | 真机评测每项任务的试验次数 |
| [Temporal GRPO: Beyond Trajectory-Level Credit in Vision-Language-Action Reinforcement Learning](https://arxiv.org/abs/2608.13026) | 2026-08-13 | `vla` | 48 | 未找到官方仓库链接 |  |
| [NestDex: Nested Policy Learning with Copilot Assisted Teleoperation for Dexterous Manipulation](https://arxiv.org/abs/2608.13362) | 2026-08-13 | `teleoperation` | 48 | 未找到官方仓库链接 |  |
| [One Future, Every Robot: Label-Efficient Collective-State Prediction with Decentralized JEPA](https://arxiv.org/abs/2607.28443) | 2026-07-30 | `world-model` | 48 | 未找到官方仓库链接 | 作者团队在群体机器人学习方向的既往成果 |
| [DynaWM: Dynamics-Aware Distillation with World Model and Momentum Targets for Smooth Locomotion over Continuous Stairs](https://arxiv.org/abs/2606.24089) | 2026-06-23 | `locomotion` | 48 | 未找到官方仓库链接 | 是否发布代码 |
| [NavWM: A Unified Navigation World Model for Foresight-Driven Planning](https://arxiv.org/abs/2606.24101) | 2026-06-23 | `navigation` | 48 | 未找到官方仓库链接 | 是否发布代码与模型 |
| [DREAM-Chunk: Reactive Action Chunking with Latent World Model](https://arxiv.org/abs/2606.18589) | 2026-06-17 | `vla` | 48 | 未找到官方仓库链接 | 是否发布代码 |
| [T-GMP: Terrain-conditioned Generative Motion Priors for Versatile and Natural Humanoid Locomotion](https://arxiv.org/abs/2606.06944) | 2026-06-05 | `locomotion` | 48 | 未找到官方仓库链接 | 地形配对动捕数据集是否计划公开 |
| [Can VLA Models Learn from Real-World Data Continually without Forgetting?](https://arxiv.org/abs/2605.26820) | 2026-05-26 | `vla` | 48 | 未找到官方仓库链接 | 所用基础 VLA 的确切版本（文中引用 [3]）；数据集是否会以 LeRobot 格式公开 |
| [WAM-RL: World-Action Model Reinforcement Learning with Reconstruction Rewards and Online Video SFT](https://arxiv.org/abs/2606.17906) | 2026-06-16 | `world-model` | 46 | 未找到官方仓库链接 | 是否会发布代码与微调权重 |
| [Neural Introspection Gating for Adaptive KV-Cache Reuse in Vision-Language-Action Models](https://arxiv.org/abs/2608.10824) | 2026-08-11 | `vla` | 45 | 未找到官方仓库链接 | 项目页是否链接了代码 |
| [VISA: VLM-Guided Instance Semantic Auditing for 3D Occupancy World Models](https://arxiv.org/abs/2606.13460) | 2026-06-11 | `scene` | 45 | 未找到官方仓库链接 |  |
| [Koala Gripper: Co-designing Robotic Grippers and Data-Capture Devices for Scaling Dexterous Manipulation Learning](https://arxiv.org/abs/2608.20546) | 2026-08-20 | `teleoperation` | 43 | 未找到官方仓库链接 | 核实论文署名单位（项目页域名为 rai-inst.com，PDF 首页需确认） |
| [The Embodiment Gap in Robot Foundation Models](https://arxiv.org/abs/2608.18433) | 2026-08-19 | `tutorials` | 43 | 未找到官方仓库链接 |  |
| [Throwing a Tight Spiral American Football by a Humanoid Robot](https://arxiv.org/abs/2608.16642) | 2026-08-17 | `manipulation` | 43 | 未找到官方仓库链接 |  |
| [Weights or Skills? A Survey of Robot-Learning Techniques: from Action-Predicting Weights to Robots that Write their Own Skills](https://arxiv.org/abs/2608.01851) | 2026-08-03 | `tutorials` | 43 | 未找到官方仓库链接 | 作者团队在机器人学习方向的既往成果 |
| [Towards Robotic Dexterous Hand Intelligence: A Survey](https://arxiv.org/abs/2605.13925) | 2026-05-13 | `tutorials` | 43 | 未找到官方仓库链接 | 是否有配套的 awesome 列表或持续维护的资源页 |
| [PhysiFlow: Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent Flow Matching and Robust Tracking](https://arxiv.org/abs/2603.05410) | 2026-03-05 | `vla` | 42 | 未找到官方仓库链接 |  |
| [WorldDiT: A Unified Diffusion Architecture for World and Action Modeling](https://arxiv.org/abs/2607.23909) | 2026-07-27 | `world-model` | 37 | 未找到官方仓库链接 | 核实 Bagel Labs 在机器人学习方向的相关成果 |
| [EaDex: A Cross-Embodiment Dexterous Manipulation Framework from Low-Cost Demonstrations](https://arxiv.org/abs/2606.03268) | 2026-06-02 | `manipulation` | 37 | 未找到官方仓库链接 | 自建低成本示范数据集是否公开 |
| [HODAgent: Towards On-Demand, Responsive Humanoids for Physical World Human Interaction](https://arxiv.org/abs/2608.17584) | 2026-08-18 | `vla` | — | 未找到官方仓库链接 | 论文已被撤回（公司内部审查要求），确认是否有重新公开的版本；若无，建议从列表移除；作者单位、基线设置与真机试验次数（无 HTML 全文） |
| [Attention from Action, for Action: Emergent Visual Bottlenecks for Policy Learning](https://arxiv.org/abs/2608.13422) | 2026-08-13 | `manipulation` | — | 已公开实质相关代码 | arXiv 无 HTML 版本，需阅读 PDF 的实验部分（仿真任务数、演示数量、真机任务与试次、消融）后再评分；核实论文署名单位（当前取自仓库 README） |
| [Action with Visual Primitives](https://arxiv.org/abs/2605.22183) | 2026-05-21 | `vla` | — | 未找到官方仓库链接 | 论文已于 2026-09-20 撤稿（v4），需确认是否有修订版重新发布；若长期无新版本，应考虑移出列表；正文（v1–v3 PDF）中的实验设置、基线与试验次数 |
| [World Action Models: The Next Frontier in Embodied AI](https://arxiv.org/abs/2605.12090) | 2026-05-12 | `tutorials` | — | 部分开放 | arXiv 无 HTML 版本，需阅读 PDF 正文后再评分（分类体系、数据与评测章节）；作者单位需从 PDF 首页核对（缓存中未提取到） |

## 移出列表

- [VLM3: Vision Language Models Are Native 3D Learners](https://arxiv.org/abs/2605.30561) — 超出范围：纯 VLM 的 3D 视觉理解（深度、对应、相机位姿、物体级空间问答），无机器人或具身决策实验
- [Looped World Models](https://arxiv.org/abs/2606.18208) — 超出范围：在 ScienceWorld/ALFWorld 文本环境中做状态描述预测，以 EM/BLEU 对比 LLM API，无视觉感知或物理控制成分
- [Qwen-AgentWorld: Language World Models for General Agents](https://arxiv.org/abs/2606.24597) — 超出范围：面向 LLM 智能体（终端、GUI、工具调用、搜索）的语言世界模型，无物理/具身成分
- [BlockPilot: Instance-Adaptive Policy Learning for Diffusion-based Speculative Decoding](https://arxiv.org/abs/2606.31315) — 超出范围：LLM 扩散式推测解码的块大小自适应选择，与具身/物理 AI 无关
- [AlayaWorld: Long-Horizon and Playable Video World Generation](https://arxiv.org/abs/2607.06291) — 重复：同一项目的完整技术报告 2607.18367 已覆盖本版内容，本版仅有定性结果
- [SceneActBench: Can Agents Act on the 3D Scenes They See?](https://arxiv.org/abs/2607.22393) — 超出范围：VLM 代理通过 Blender 工具编辑 3D 场景（布局、相机、关节、重建、动画）的基准，无机器人/具身身体或物理控制成分
- [Mental World Modeling](https://arxiv.org/abs/2607.27201) — 超出范围：基于 LLM 的心智/社会情境决策预测框架与多选基准，无具身感知或控制实验
- [DAPD: Dual-Anchored Policy Distillation](https://arxiv.org/abs/2608.01735) — 超出范围：纯语言模型后训练（在线自蒸馏）方法，评测为数学/代码/指令遵循基准，与具身无关
- [EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinforcement Learning](https://arxiv.org/abs/2608.06197) — 超出范围：LLM 工具调用智能体的强化学习方法，评测为 BFCL、tau2-Bench 等文本工具基准，无具身环境
- [Beyond Pixels: From Video Priors to 4D Worlds](https://arxiv.org/abs/2608.10744) — 超出范围：通用文本/图像到 4D 场景生成，与决策和控制无关，具身相关内容只有操作/导航隐变量的定性兼容性演示
- [VIScore: Diagnosing Planning-Relevant Quality in Latent World Models](https://arxiv.org/abs/2608.11174) — 材料不足：arXiv 上两个版本都已被移除或撤回（管理员注明许可证问题，后续版本由作者撤回），没有可核查的全文
- [Poor Man's Agentic Modeling: Simulating Large LLM-Agent Societies on a Laptop](https://arxiv.org/abs/2608.11215) — 超出范围：用低参数代理模型替代 LLM 智能体来模拟社会/经济系统，属于多智能体与统计物理研究，与具身或物理世界交互无关
- [AutoWorldModel-Bench: A State-Centric Benchmark for Automated World-Model Research](https://arxiv.org/abs/2608.11216) — 超出范围：评测编码智能体在游戏结构化状态上自主改进世界模型的能力，不涉及具身感知、机器人或物理控制

## 类别调整

- Imagine2Real: Towards Zero-shot Humanoid-Object Interaction via Video Generative Priors：category sim2real → locomotion
- stable-worldmodel: A Platform for Reproducible World Modeling Research and Evaluation：category foundation-models → world-model
- Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum：category vla → manipulation
- Hand-in-the-Loop: Improving VLA Policies for Dexterous Manipulation via Seamless Hand-Arm Intervention：category manipulation → teleoperation
- Towards Robotic Dexterous Hand Intelligence: A Survey：category manipulation → tutorials
- Reinforcing VLAs in Task-Agnostic World Models：category foundation-models → world-model
- World Action Models: The Next Frontier in Embodied AI：category foundation-models → tutorials
- HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation：category foundation-models → vla
- Cosmos World Foundation Model Platform for Physical AI：category foundation-models → world-model
- LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction：category sim2real → vla
- Towards Human-Like Manipulation through RL-Augmented Teleoperation and Mixture-of-Dexterous-Experts VLA：category teleoperation → vla
- Learning to Evolve: Multi-modal Interactive Fields for Robust Humanoid Navigation in Dynamic Environments：category locomotion → navigation
- Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models：category foundation-models → world-model
- GeoSem-WAM: Geometry- and Semantic-Aware World Action Models：category scene → world-model
- Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking：category vla → locomotion
- CLAW: Learning Continuous Latent Action World Models via Adversarial Latent Regularization：category foundation-models → world-model
- 3DThinkVLA: Endowing Vision-Language-Action Models with Latent 3D Priors via 3D-Thinking-Guided Co-training：category foundation-models → vla
- OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics：category foundation-models → world-model
- MAD: Mapping-Aware World Models for Agile Quadrotor Flight：category foundation-models → navigation
- GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors：category teleoperation → locomotion
- Discrete-WAM: Unified Discrete Vision-Action Token Editing for World-Policy Learning：category foundation-models → world-model
- PiL-World: A Chunk-Wise World Model for VLA Policy-in-the-Loop Evaluation：category teleoperation → world-model
- LadderMan: Learning Humanoid Perceptive Ladder Climbing：category teleoperation → locomotion
- World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis：category foundation-models → vla
- MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation：category teleoperation → locomotion
- DexFuture: Hierarchical Future-State Visuomotor Targeting for Bimanual Dexterous Tool Use：category foundation-models → manipulation
- HomeWorld: A Unified Floorplan-to-Furnished Framework for Generating Controllable, Densely Interactive Whole-Home Scenes：category vla → scene
- STRIPS-WM: Learning Grounded Propositional STRIPS-style World Models from Images：category foundation-models → world-model
- Dreaming when Necessary: Advancing World Action Models with Adaptive Multi-Modal Reasoning：category manipulation → world-model
- MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation：category locomotion → world-model
- Targeting World Models to Compromise Robot Learning Pipelines：category teleoperation → world-model
- iMaC: Translating Actions into Motion and Contact Images for Embodied World Models：category foundation-models → world-model
- Latent Spatial Memory for Video World Models：category foundation-models → world-model
- WorldOlympiad: Can Your World Model Survive a Triathlon?：category scene → world-model
- VISA: VLM-Guided Instance Semantic Auditing for 3D Occupancy World Models：category foundation-models → scene
- NavWAM: A Navigation World Action Model for Goal-Conditioned Visual Navigation：category foundation-models → navigation
- $\texttt{WEAVER}$, Better, Faster, Longer: An Effective World Model for Robotic Manipulation：category foundation-models → world-model
- $\mu_0$: A Scalable 3D Interaction-Trace World Model：category foundation-models → world-model
- ContactWorld: What Matters in Vision-Tactile World Models for Contact-Rich Manipulation：category foundation-models → world-model
- DreamX-World 1.0: A General-Purpose Interactive World Model：category foundation-models → world-model
- ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning：category vla → rl-il
- Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation：category foundation-models → world-model
- Geometric Action Model for Robot Policy Learning：category foundation-models → vla
- ERQA-Plus: A Diagnostic Benchmark for Reasoning in Embodied AI：category navigation → scene
- WAM-RL: World-Action Model Reinforcement Learning with Reconstruction Rewards and Online Video SFT：category foundation-models → world-model
- DREAM-Chunk: Reactive Action Chunking with Latent World Model：category foundation-models → vla
- Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement：category teleoperation → sim2real
- Mem-World: Memory-Augmented Action-Conditioned World Models for Persistent Robot Manipulation：category foundation-models → world-model
- Sensorimotor World Models: Perception for Action via Inverse Dynamics：category foundation-models → world-model
- HumanScale: Egocentric Human Video Can Outperform Real-Robot Data for Embodied Pretraining：category teleoperation → foundation-general
- MemoryWAM: Efficient World Action Modeling with Persistent Memory：category vla → world-model
- World Action Models: A Survey：category foundation-models → tutorials
- Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents：category foundation-models → manipulation
- NavWM: A Unified Navigation World Model for Foresight-Driven Planning：category foundation-models → navigation
- World Value Models for Robotic Manipulation：category foundation-models → world-model
- Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models：category foundation-models → world-model
- Orca: The World is in Your Mind：category foundation-models → foundation-general
- MemLearner: Learning to Query Context memory for Video World Models：category foundation-models → world-model
- From Foundation to Application: Improving VLA Models in Practice：category foundation-models → vla
- RynnWorld-4D: 4D Embodied World Models for Robotic Manipulation：category foundation-models → world-model
- DriftWorld: Fast World Modeling through Drifting：category foundation-models → world-model
- AlayaWorld: Interactive Long-Horizon World Modeling -- Full Technical Report：category foundation-models → world-model
- ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU：category foundation-models → world-model
- Masked Visual Actions for Unified World Modeling：category foundation-models → world-model
- NavVerse: Benchmarking Indoor-to-Outdoor Embodied Navigation in Continuous Robot Simulation：category vla → navigation
- KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding：category foundation-models → world-model
- Kairos: A Regret-Aware Native World-Action Model Stack for Physical AI：category foundation-models → world-model
- Progress Reward Modeling for Robotic Learning: A Comprehensive Survey：category foundation-models → tutorials
- WorldDiT: A Unified Diffusion Architecture for World and Action Modeling：category foundation-models → world-model
- Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control：category foundation-models → world-model
- Wonder: Video World Model Done Better：category foundation-models → world-model
- HumanCLAW: Can Vision-Language Models Act Through a Body?：category vla → navigation
- $N_0$-VTLA: Scaling Vision-Tactile-Language-Action Model with Latent Tactile Tokens：category foundation-models → vla
- $N_0$-TWAM: Scaling Tactile-Native World-Action Model for Contact-Rich Manipulation：category manipulation → world-model
- One Future, Every Robot: Label-Efficient Collective-State Prediction with Decentralized JEPA：category vla → world-model
- SG-WAM: Self-Guided World Modeling in Geometry-Aware Policy Space：category foundation-models → world-model
- WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reactivity：category foundation-models → world-model
- Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data：category vla → manipulation
- WorldCycle: Self-Verifiable Reinforcement Learning for Long-Horizon Video World Models：category foundation-models → world-model
- Weights or Skills? A Survey of Robot-Learning Techniques: from Action-Predicting Weights to Robots that Write their Own Skills：category foundation-models → tutorials
- World Tokens: Enhancing Embodied Policies with Training-Time World Modeling：category foundation-models → vla
- SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation：category foundation-models → vla
- RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance：category foundation-models → foundation-general
- Toward the Cognitive--Physical Limits of Embodied Intelligence through a World-Model-Centric Autonomous Racing Agent：category foundation-models → world-model
- Flex-$\pi$: A Multi-Stream World-Action Model with Compute Flexibility：category locomotion → world-model
- Learning How the World Evolves: Extrapolative Video World Models via Latent Dynamics Reasoning：category locomotion → world-model
- Self-Evolving Embodied Agents via Skill-Harness Evolution：category foundation-models → foundation-general
- Keep the Future, Drop the Rollout: RIFT for World Action Models：category vla → world-model
- Learning-Based Behavior Planning for Automated Driving: Real-World Integration and Deployment：category vla → navigation
- HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments：category locomotion → navigation
- H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models：category foundation-models → world-model
- ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models：category foundation-models → world-model
- DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation：category foundation-models → world-model
- GigaBrain-0.7: Scaling Embodied Foundation Models to Emergent Capabilities with a Three-System Architecture：category foundation-models → vla
- Pre-training Visual Dexterity in Simulation：category teleoperation → manipulation
- Throwing a Tight Spiral American Football by a Humanoid Robot：category vla → manipulation
- HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent RL：category locomotion → vla
- $\tau_0$-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time Computation：category foundation-models → vla
- Prism-GRPO: Faster VLA Policy Optimization via Splitting Same-outcome Groups：category vla → rl-il
- PRISM: Precision and contact-rich Real-world Industrial Skill dataset with Multimodal sensing：category teleoperation → manipulation
- Hydra-0: Action Flow for Generalist World Modeling and Control：category foundation-models → world-model
- GigaBrain-WBC-0.5: A Behavior World Model for Robust Whole-Body Control with Environment Interaction：category teleoperation → locomotion
- The Embodiment Gap in Robot Foundation Models：category foundation-models → tutorials
- Dream2Reward: Transition-Alignment Reward Models from Positive Demonstrations for Robotic Manipulation：category manipulation → rl-il
- ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World Models：category foundation-models → world-model
- What Matters for Latent Actions in Robot Learning：category manipulation → vla
- EXIMO: VLM Guided Exploration of VLA Policies：category teleoperation → vla
- DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation：category locomotion → world-model
- Attention from Action, for Action: Emergent Visual Bottlenecks for Policy Learning：category vla → manipulation
- Revisiting Open-Loop Execution in Robotics: Toward Reactive, Higher-Performing Policies：category manipulation → rl-il
- Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention for Video Generation and World Models：category foundation-models → world-model
- Koala Gripper: Co-designing Robotic Grippers and Data-Capture Devices for Scaling Dexterous Manipulation Learning：category manipulation → teleoperation
- PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration：category vla → manipulation
- WALL-SS: Scaling Long-horizon World Models via Next-Scale Autoregression：category foundation-models → world-model
- PAWBench: How Far Are We from Probabilistically Aligned World Modeling?：category foundation-models → world-model
- CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators：category foundation-models → world-model
