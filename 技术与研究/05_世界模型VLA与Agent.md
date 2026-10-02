# 世界模型、VLA与Agent

> 视觉语言理解、未来预测与任务决策，汇总相关论文、方法与项目。

当前收录 **173** 篇论文／技术报告、**166** 个项目。

## 本页导航

[三种核心范式](#三种核心范式) · [世界模型与未来预测](#世界模型与未来预测) · [VLA与通用操作策略](#vla与通用操作策略) · [世界动作模型（WAM）](#世界动作模型wam) · [仿真生成与数据引擎](#仿真生成与数据引擎) · [具身理解与Agent规划](#具身理解与agent规划) · [训练、部署与评测工具](#训练部署与评测工具) · [相关资料](#相关资料)

## 三种核心范式

| 范式 | 输入 → 输出 | 用途与代表方法 |
| --- | --- | --- |
| **世界模型** | 观测／状态、历史、候选动作 → 未来状态、视频或奖励 | 预测执行动作后的环境变化；Dreamer、Ctrl-World、Cosmos Predict、Qwen-RobotWorld |
| **VLA / 操作策略** | 观测、任务指令、本体状态 → 动作、动作块或末端目标 | 根据任务与当前环境决定动作；π0.5、OpenVLA、GR00T、Qwen-RobotManip |
| **世界动作模型（WAM）** | 观测、任务指令、本体状态 → 动作及未来世界，或由世界表征支持的动作 | 联合学习动作与环境演化；DreamZero、LingBot-VA、Cosmos Policy |

分类围绕模型学习什么、输出什么及怎样参与执行。语言可以描述世界模型的动作条件；视频主干也可以服务直接动作策略。WAM的未来分支可能只在训练中提供监督，部署时输出动作即可。具身理解、仿真生成和工程工具另设入口。

### 未来信息怎样进入动作学习

| 路径 | 训练与执行流程 | 阅读重点 |
| --- | --- | --- |
| 视频规划与逆动力学 | 生成目标视频，再由逆动力学恢复动作 | 视频计划怎样变成可执行控制量 |
| 未来预测辅助动作学习 | 用未来视觉或隐表示提供训练信号，动作头在部署时直接输出动作 | 哪些模块参与训练，哪些模块参与实际执行 |
| 视觉与动作联合建模 | 联合学习未来世界与动作，按条件生成动作、视觉或二者 | 动作与视觉的信息交互、去噪方式及闭环反馈 |
| 隐空间未来学习 | 训练时利用未来观测形成监督，执行时从当前上下文推断隐表示 | 未来信息怎样被压缩进当前决策 |

这几条路径可以交叉组合。比较方法时，沿着观测、历史、任务条件、未来监督、动作输出与真实反馈阅读，能更清楚地理解训练目标与控制流程之间的关系。

建议按[UniPi](论文逐篇解读/P316.md)、[GR-1](论文逐篇解读/P317.md)、[VPP](论文逐篇解读/P318.md)、[UWM](论文逐篇解读/P319.md)、[DreamZero](论文逐篇解读/P113.md)串联方法演进，再比较[Being-H0.7](论文逐篇解读/P314.md)与[FastWAM](论文逐篇解读/P198.md)怎样组织训练期未来信息和执行期动作计算。

## 世界模型与未来预测

根据观测、历史和动作条件预测未来状态、视频或奖励，用于想象学习、规划和策略评估。动作条件也可用语言或潜变量表达。

**24** 篇论文／报告 · **20** 个项目

#### 论文与技术报告

| 论文／报告 | 主要方法与用途 | 原文／代码 |
| --- | --- | --- |
| [ABot-PhysWorld：物理对齐的可控操控世界模型](论文逐篇解读/P279.md) | 以Wan2.1-I2V-14B为视频扩散主干，用物理检查表偏好与Diffusion-DPO强化接触及状态变化真实性，并把结构化机械臂动作投影成空间动作图，经并行上下文分支控制未来视频。 | [原文](https://arxiv.org/abs/2603.23376) · [代码](https://github.com/amap-cvlab/ABot-PhysWorld) |
| [ABot-World-0：以键盘动作驱动桌面实时交互世界](论文逐篇解读/P272.md) | ABot-World-0把历史视频、多模态提示和逐帧8维键盘动作映射为因果未来视频rollout；Wan2.2双向教师、因果学生蒸馏与LongForcing提升动作可控及长程稳定，叠加轻量解码与低比特推理在单张RTX5090实现高分辨率交互。 | [原文](https://arxiv.org/abs/2607.19191) · [代码](https://github.com/amap-cvlab/ABot-World) · [项目页](https://amap-cvlab.github.io/ABot-World/) |
| [LingBot-World 1.0：可交互的长时程视频世界模型](论文逐篇解读/P297.md) | LingBot-World 根据初始视频、相机轨迹及离散/连续用户控制自回归生成交互式未来画面，以空间记忆、动作条件扩散和因果分块推理支持长时程视觉模拟。 | [原文](https://arxiv.org/abs/2601.20540) · [代码](https://github.com/robbyant/lingbot-world) |
| [CLAW：少量交互下的世界模型低秩适配](论文逐篇解读/P345.md) | CLAW用少量测试转移生成覆盖世界模型各层的低秩适配器，并与TD-MPC2基础模型联合预训练；在运动和操作仿真环境家族中比较在线适配、数据稀缺和上下文条件化。 | [原文](https://arxiv.org/abs/2609.12278) |
| [Cosmos 3：统一理解、预测与动作生成的全模态世界模型](论文逐篇解读/P253.md) | 通过共享跨模态MoT支持多模态理解、内容生成、动作条件视觉动力学、逆动力学和机器人策略接口。 | [原文](https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf) · [代码](https://github.com/NVIDIA/cosmos) · [项目页](https://research.nvidia.com/labs/cosmos-lab/cosmos3/) |
| [DreamDojo：基于大规模人类视频的通用机器人世界模型](论文逐篇解读/P114.md) | 从大规模人类视频学习潜在交互动力学，再经机器人后训练与蒸馏用于操作预测和规划。 | [原文](https://arxiv.org/abs/2602.06949) · [代码](https://github.com/NVIDIA/DreamDojo) · [项目页](https://dreamdojo-world.github.io/) |
| [GE-Sim 2.0：让动作条件视频预测接入操作闭环](论文逐篇解读/P261.md) | 以双臂末端动作条件预测多视角未来视频，并联合预测关节状态与逐帧任务成功信号，形成可闭环评估和筛选策略轨迹的世界模型。 | [原文](https://arxiv.org/abs/2605.27491) · [代码](https://github.com/AgibotTech/GE-Sim-V2) · [项目页](https://ge-sim-v2.github.io/) |
| [GigaWorld-1：以动作条件长程预测支持策略评测](论文逐篇解读/P271.md) | GigaWorld-1以历史观测、显式空间动作控制和任务条件自回归预测未来多视角视频；Wan初始化、层级历史记忆、相机几何控制和DMD2蒸馏服务长程rollout，并由WMBench评估其与真实策略结果的对齐。 | [原文](https://arxiv.org/abs/2607.02642) · [代码](https://github.com/open-gigaai/giga-world-1) · [项目页](https://open-gigaai.github.io/giga-world-1/) |
| [LingBot-World 2.0：以相机与事件指令驱动长时程交互世界](论文逐篇解读/P266.md) | LingBot-World 2.0以初始画面、相机位姿和分块文本事件作为条件，自回归预测未来交互视频；MoBA因果注意力、少步蒸馏及Pilot/Director调度支持长时程实时世界交互。 | [原文](https://arxiv.org/abs/2607.07534) · [代码](https://github.com/Robbyant/lingbot-world-v2) · [项目页](https://technology.robbyant.com/lingbot-world-v2) |
| [Qwen-RobotWorld：语言条件的具身未来视频预测](论文逐篇解读/P259.md) | 以自然语言动作意图统一描述不同机器人操作，并预测对应的未来视频状态，供生成评测与下游世界模型研究使用。 | [原文](https://arxiv.org/abs/2606.17030) · [项目页](https://qwen.ai/blog?id=qwen-robotworld) |
| [RynnWorld-4D：协同预测外观、几何与运动的具身世界模型](论文逐篇解读/P281.md) | 从RGB-D观察与任务文本协同生成未来RGB、深度和光流，通过逐帧跨模态注意力形成可还原3D场景流的4D表征；独立训练的RynnWorld-4D-Policy再用冻结预测表征产生动作。 | [原文](https://arxiv.org/abs/2607.06559) · [代码](https://github.com/alibaba-damo-academy/RynnWorld-4D) · [项目页](https://alibaba-damo-academy.github.io/RynnWorld-4D.github.io) |
| [WALL-SS：让动作条件世界模型持续推演，并用于筛选机器人策略](论文逐篇解读/P187.md) | 以尺度对齐动作条件和时间尺度记忆进行长程视频推演，评估机器人世界模型及策略。 | [原文](https://x2robot-open.oss-cn-shenzhen.aliyuncs.com/ARWM%20OPEN/WALL-SS.pdf) · [代码](https://github.com/X-Square-Robot/wall-ss) · [项目页](https://x2robot.com/pages/ss) |
| [μ₀：以三维交互轨迹学习可迁移运动先验](论文逐篇解读/P382.md) | 从人类与机器人视频提取三维交互轨迹，以视觉、语言目标和查询点预测未来运动；冻结轨迹模型后训练目标机器人动作专家，将交互运动先验用于真实操作。 | [原文](https://arxiv.org/abs/2606.13769) · [代码](https://github.com/Yoonkyo/mu0) · [项目页](https://mu0-wm.github.io/) |
| [Embodied World Model Survey：具身智能世界模型综合综述](论文逐篇解读/P072.md) | 从功能、时间建模和空间表示整理具身世界模型，涵盖状态估计、预测、生成与规划。 | [原文](https://arxiv.org/abs/2510.16732) · [代码](https://github.com/Li-Zn-H/AwesomeWorldModels) |
| [Cosmos平台：面向Physical AI的视频世界基础模型](论文逐篇解读/P252.md) | 从通用视频生成先验构建物理AI世界模型平台，覆盖视频数据处理、未来状态生成、目标领域后训练和条件安全评估。 | [原文](https://arxiv.org/pdf/2501.03575) · [代码](https://github.com/nvidia-cosmos/cosmos-predict1) · [项目页](https://research.nvidia.com/labs/dir/cosmos1/) |
| [Ctrl-World：动作条件世界预测与策略评估](论文逐篇解读/P257.md) | 根据外部策略动作生成后续相机视觉状态，为候选操作策略的闭环评测和合成轨迹筛选提供可控视频环境。 | [原文](https://arxiv.org/abs/2510.10125) · [代码](https://github.com/Robert-gyj/Ctrl-World) · [项目页](https://ctrl-world.github.io/) |
| [EnerVerse-AC：动作条件的多视角未来视频模型](论文逐篇解读/P284.md) | 以末端位姿动作图、Delta Action Attention和多视角ray-map条件控制潜空间视频扩散，输入历史观察与外部动作轨迹并生成未来RGB观察；用生成视频做策略评估和示范轨迹数据扩增。 | [原文](https://arxiv.org/abs/2505.09723) · [代码](https://github.com/AgibotTech/EnerVerse-AC) · [项目页](https://annaj2178.github.io/EnerverseAC.github.io) |
| [Genie Envisioner：视频世界模型、动作策略与闭环仿真平台](论文逐篇解读/P283.md) | 以GE-Base生成语言条件多视角未来视频，GE-Act从视觉潜变量生成动作轨迹，GE-Sim以外部动作条件合成执行后视频并反馈策略闭环评测，EWMBench统一测量视频世界模型与动作对齐。 | [原文](https://arxiv.org/abs/2508.05635) · [代码](https://github.com/AgibotTech/Genie-Envisioner-V1) · [项目页](https://genie-envisioner.github.io) |
| [V-JEPA 2：面向理解、预测与规划的自监督视频模型](论文逐篇解读/P067.md) | 先以掩码潜在预测学习视频表征，再用少量机器人数据训练动作条件世界模型和操控规划。 | [原文](https://arxiv.org/abs/2506.09985) · [代码](https://github.com/facebookresearch/vjepa2) · [项目页](https://ai.meta.com/vjepa/) |
| [VideoWorld：从无动作标注视频学习动态与规划](论文逐篇解读/P295.md) | 以VQ-VAE视频自回归生成和LDM多步视觉变化压缩学习任务动态，再由逆动力学模块从生成帧与潜代码恢复动作，在围棋、CALVIN和RLBench验证规划能力。 | [原文](https://arxiv.org/abs/2501.09781) · [代码](https://github.com/ByteDance-Seed/VideoWorld) · [项目页](https://seed.bytedance.com/en/public_papers/videoworld) |
| [UniSim：交互式真实世界模拟器学习](论文逐篇解读/P066.md) | 融合机器人、驾驶和互联网视频训练动作条件生成模型，用于交互式未来画面模拟与规划研究。 | [原文](https://arxiv.org/abs/2310.06114) · [项目页](https://universal-simulator.github.io/) |
| [DreamerV3：基于世界模型的跨领域通用控制](论文逐篇解读/P065.md) | 以离散潜变量、symlog和two-hot回归统一世界模型训练尺度，用于多域控制与泛化。 | [原文](https://arxiv.org/abs/2301.04104) · [代码](https://github.com/danijar/dreamerv3) |
| [Dreamer：基于潜在想象的行为学习](论文逐篇解读/P064.md) | 从交互数据学习潜在世界模型，在想象轨迹中训练Actor-Critic，再回到真实观测闭环控制。 | [原文](https://arxiv.org/abs/1912.01603) · [代码](https://github.com/danijar/dreamer) · [项目页](https://dreamrl.github.io/) |
| [PlaNet：基于像素输入的潜在动力学规划](论文逐篇解读/P063.md) | 以RSSM从像素学习潜在动力学，并用CEM搜索动作序列执行基于模型的控制与规划。 | [原文](https://arxiv.org/abs/1811.04551) · [项目页](https://planetrl.github.io/) |

#### 相关项目

| 项目 | 主要用途 | 功能与特点 |
| --- | --- | --- |
| [1xgpt](https://github.com/1x-technologies/1xgpt) | 世界模型与仿真生成 | 以当前观测和动作条件生成未来状态、视频或交互结果，为策略训练、评测和规划提供数据。 |
| [ABot-PhysWorld](https://github.com/amap-cvlab/ABot-PhysWorld) | 世界模型与未来预测 | 以Wan2.1-I2V-14B为视频扩散主干，用物理检查表偏好与Diffusion-DPO强化接触及状态变化真实性，并把结构化机械臂动作投影成空间动作图，经并行上下文分支控制未来视频。 |
| [ABot-World](https://github.com/amap-cvlab/ABot-World) | 世界模型与未来预测 | ABot-World-0把历史视频、多模态提示和逐帧8维键盘动作映射为因果未来视频rollout；Wan2.2双向教师、因果学生蒸馏与LongForcing提升动作可控及长程稳定，叠加轻量解码与低比特推理在单张RTX5090实现高分辨率交互。 |
| [AgiBotWorldChallengeICRA2026-WorldModelBaseline](https://github.com/AgibotTech/AgiBotWorldChallengeICRA2026-WorldModelBaseline) | 世界模型与仿真生成 | 根据当前观测和动作条件预测未来状态或视频，为策略训练、评测及规划提供世界模型基线。 |
| [CLAW](https://arxiv.org/abs/2609.12278) | 世界模型与未来预测 | CLAW用少量测试转移生成覆盖世界模型各层的低秩适配器，并与TD-MPC2基础模型联合预训练；在运动和操作仿真环境家族中比较在线适配、数据稀缺和上下文条件化。 |
| [Cosmos 3](https://research.nvidia.com/labs/cosmos-lab/cosmos3/) | 多模态物理AI模型家族 | 通过共享跨模态MoT支持多模态理解、内容生成、动作条件视觉动力学、逆动力学和机器人策略接口。 |
| [Cosmos Predict1](https://github.com/nvidia-cosmos/cosmos-predict1) | 世界基础模型平台 | 从通用视频生成先验构建物理AI世界模型平台，覆盖视频数据处理、未来状态生成、目标领域后训练和条件安全评估。 |
| [Ctrl-World](https://github.com/Robert-gyj/Ctrl-World) | 操作世界模型与策略数据引擎 | 根据外部策略动作生成后续相机视觉状态，为候选操作策略的闭环评测和合成轨迹筛选提供可控视频环境。 |
| [DreamDojo](https://github.com/NVIDIA/DreamDojo) | 机器人世界模型项目 | 先以大规模第一视角视频学习潜在动作，再用机器人数据后训练交互策略并蒸馏为实时模型。 |
| [EnerVerse-AC](https://github.com/AgibotTech/EnerVerse-AC) | 世界模型与未来预测 | 以末端位姿动作图、Delta Action Attention和多视角ray-map条件控制潜空间视频扩散，输入历史观察与外部动作轨迹并生成未来RGB观察；用生成视频做策略评估和示范轨迹数据扩增。 |
| [GE-Sim 2.0](https://github.com/AgibotTech/GE-Sim-V2) | 世界模型与未来预测 | 以双臂末端动作条件预测多视角未来视频，并联合预测关节状态与逐帧任务成功信号，形成可闭环评估和筛选策略轨迹的世界模型。 |
| [Genie-Envisioner-V1](https://github.com/AgibotTech/Genie-Envisioner-V1) | 世界模型与未来预测 | 以GE-Base生成语言条件多视角未来视频，GE-Act从视觉潜变量生成动作轨迹，GE-Sim以外部动作条件合成执行后视频并反馈策略闭环评测，EWMBench统一测量视频世界模型与动作对齐。 |
| [GigaWorld-1](https://github.com/open-gigaai/giga-world-1) | 世界模型与未来预测 | GigaWorld-1以历史观测、显式空间动作控制和任务条件自回归预测未来多视角视频；Wan初始化、层级历史记忆、相机几何控制和DMD2蒸馏服务长程rollout，并由WMBench评估其与真实策略结果的对齐。 |
| [LingBot-World 1.0](https://github.com/Robbyant/lingbot-world) | 世界模型与未来预测 | LingBot-World 根据初始视频、相机轨迹及离散/连续用户控制自回归生成交互式未来画面，以空间记忆、动作条件扩散和因果分块推理支持长时程视觉模拟。 |
| [LingBot-World 2.0](https://github.com/Robbyant/lingbot-world-v2) | 世界模型与未来预测 | LingBot-World 2.0以初始画面、相机位姿和分块文本事件作为条件，自回归预测未来交互视频；MoBA因果注意力、少步蒸馏及Pilot/Director调度支持长时程实时世界交互。 |
| [Qwen-RobotWorld](https://qwen.ai/blog?id=qwen-robotworld) | 语言条件视频世界模型 | 以自然语言动作意图统一描述不同机器人操作，并预测对应的未来视频状态，供生成评测与下游世界模型研究使用。 |
| [RynnWorld-4D](https://github.com/alibaba-damo-academy/RynnWorld-4D) | 世界模型与未来预测 | 从RGB-D观察与任务文本协同生成未来RGB、深度和光流，通过逐帧跨模态注意力形成可还原3D场景流的4D表征；独立训练的RynnWorld-4D-Policy再用冻结预测表征产生动作。 |
| [VideoWorld](https://github.com/ByteDance-Seed/VideoWorld) | 世界模型与未来预测 | 以VQ-VAE视频自回归生成和LDM多步视觉变化压缩学习任务动态，再由逆动力学模块从生成帧与潜代码恢复动作，在围棋、CALVIN和RLBench验证规划能力。 |
| [WALL-SS](https://github.com/X-Square-Robot/wall-ss) | 长时世界模型项目页 | 以长时世界模型对齐动作与视觉动态，并利用记忆和视觉动力学奖励评估机器人策略。 |
| [μ₀](https://github.com/Yoonkyo/mu0) | 世界模型与未来预测 | 从人类与机器人视频提取三维交互轨迹，以视觉、语言目标和查询点预测未来运动；冻结轨迹模型后训练目标机器人动作专家，将交互运动先验用于真实操作。 |

[返回本页导航](#本页导航)

## VLA与通用操作策略

根据观测、任务指令和本体状态生成可执行动作或动作块，涵盖VLA、视觉运动模仿学习、跨本体策略与后训练。

**71** 篇论文／报告 · **56** 个项目

#### 论文与技术报告

| 论文／报告 | 主要方法与用途 | 原文／代码 |
| --- | --- | --- |
| [LingBot-VLA 1.0：以大规模真实数据训练跨本体动作策略](论文逐篇解读/P268.md) | LingBot-VLA 1.0基于约2万小时、9种双臂机器人构型的真实遥操作数据，使用Qwen2.5-VL与连续动作专家联合预测50步动作块，并通过深度表征蒸馏提升空间操作。 | [原文](https://arxiv.org/abs/2601.18692v1) · [代码](https://github.com/Robbyant/lingbot-vla) · [项目页](https://technology.robbyant.com/lingbot-vla) |
| [ABot-M0：以动作流形学习强化操作VLA](论文逐篇解读/P276.md) | 将六个公开数据源清洗统一为双臂末端增量动作接口，以Qwen3-VL视觉语言主干、DiT直接动作预测AML和可插拔3D特征构建多任务VLA。 | [原文](https://arxiv.org/abs/2602.11236) · [代码](https://github.com/amap-cvlab/ABot-Manipulation) · [项目页](https://amap-cvlab.github.io/ABot-Manipulation) |
| [ABot-N1：慢速推理与快速控制的通用导航策略](论文逐篇解读/P280.md) | 把点目标、语言指令、物体目标、POI与行人跟随统一为自然语言条件导航；慢速Qwen视觉语言推理输出CoT及可通行/目标像素，快速动作专家解码连续SE(2)航点并异步闭环执行。 | [原文](https://arxiv.org/abs/2607.10383) · [代码](https://github.com/amap-cvlab/ABot-Navigation) · [项目页](https://amap-cvlab.github.io/ABot-Navigation) |
| [ACoT-VLA：动作链式思维引导的视觉语言动作模型](论文逐篇解读/P304.md) | 以显式粗参考轨迹和VLM层内隐式动作先验构成动作链式推理，条件化flow-matching动作头，提升长时程操作及扰动迁移表现。 | [原文](https://arxiv.org/abs/2601.11404) · [代码](https://github.com/AgibotTech/ACoT-VLA) |
| [ALOE：混合轨迹中的动作级离策略评估](论文逐篇解读/P185.md) | 以动作块为单位进行离策略价值估计，为稀疏奖励下的视觉语言动作模型后训练提供评估。 | [原文](https://arxiv.org/abs/2602.12691) · [项目页](https://github.com/AgibotTech/aloe) |
| [Being-H0.5：用共享动作语言连接人手与不同机器人本体](论文逐篇解读/P166.md) | 以统一动作槽位和分路专家共训人类与多种机器人数据，保留跨本体操作输出差异。 | [原文](https://arxiv.org/abs/2601.12993) · [代码](https://github.com/BeingBeyond/Being-H) · [项目页](https://research.beingbeyond.com/being-h05) |
| [Being-H0：以第一视角人类视频预训练视觉语言动作表征](论文逐篇解读/P165.md) | 先从人类视频预训练视觉、语言与手部运动表征，再用机器人示范适配灵巧操作动作空间。 | [原文](https://arxiv.org/abs/2507.15597) · [代码](https://github.com/BeingBeyond/Being-H) · [项目页](https://research.beingbeyond.com/being-h0) |
| [BridgeVLA++：让三维操作策略记住已经发生的交互](论文逐篇解读/P204.md) | 以二维热图生成粗到细动作，并用时间和空间记忆恢复遮挡目标几何以完成三维操作。 | [原文](https://arxiv.org/abs/2608.05042) · [代码](https://github.com/npucvr/BridgeVLA-Seq) · [项目页](https://bridgevla-plus.github.io/) |
| [CLIFT：用真机奖励闭环适配人形 VLA](论文逐篇解读/P242.md) | 把部署后的真机轨迹转成优势标注的监督样本，经托管SFT接口迭代VLA，缓解权重封闭模型在接触操作中的任务适配不足。 | [原文](https://arxiv.org/abs/2607.29172) · [项目页](https://thomaschen98.github.io/clift/) |
| [POT-VLA：用持久三维物体Token闭环验证人形移动操作](论文逐篇解读/P241.md) | 将RGB-D观测更新为带任务角色的持久三维物体记录，把同一物体记忆用于VLA动作条件和动作后几何谓词验证，支持失败后的局部恢复。 | [原文](https://arxiv.org/abs/2607.18016) |
| [DriftingVLA：按动作维度漂移的原生单步 VLA](论文逐篇解读/P325.md) | 从噪声一次生成完整动作块，以PDTD对每个动作维的完整时序轨迹分别建立漂移几何，保留联合动作输出，在LIBERO、RoboTwin与双UR5真机验证精度和时延。 | [原文](https://arxiv.org/abs/2608.29749) |
| [DualManip：语义推理与几何适应协同的动态操作](论文逐篇解读/P355.md) | DualManip用较慢的语义路径拆解任务并初始化交互点，再用实时RGB-D几何路径在物体移动或形变时更新模板对应关系和抓取接触位置；信息交互模块校验几何更新，必要时触发语义重规划。论文在六项真实操作任务中评估静态、单次变化和连续变化场景。 | [原文](https://arxiv.org/abs/2609.31112) · [项目页](https://lichengxi1.github.io/Dualmanip) |
| [EATR-Stereo：让人形VLA按身体状态使用双目辅助证据](论文逐篇解读/P181.md) | 保留主视角Token并路由双目辅助特征，按身体历史调节视觉证据以支持遮挡下长程操作。 | [原文](https://arxiv.org/abs/2608.17453) |
| [EgoVLA：用手腕位姿和MANO手部参数连接人类视频与机器人动作](论文逐篇解读/P168.md) | 将第一视角人手恢复为腕部与MANO动作并结合机器人样本训练跨域操作模型。 | [原文](https://arxiv.org/abs/2507.12440) · [代码](https://github.com/catburgg/EgoVLA) · [项目页](https://rchalyang.github.io/EgoVLA/) |
| [LingBot-VLA 2.0：扩展本体覆盖并引入未来特征蒸馏](论文逐篇解读/P265.md) | LingBot-VLA 2.0以跨本体稀疏MoE、55维全身统一动作接口和当前/未来几何及因果视频特征蒸馏，训练生成机器人动作的VLA策略。 | [原文](https://arxiv.org/abs/2607.06403) · [代码](https://github.com/Robbyant/lingbot-vla-v2) · [项目页](https://technology.robbyant.com/lingbot-vla-v2) |
| [G0.5：让推理与动作回到同一条自回归序列](论文逐篇解读/P162.md) | 以ActionCodec压缩异构动作，让单一自回归模型从视觉语言推理直接生成机器人动作token。 | [原文](https://arxiv.org/abs/2608.11739) · [代码](https://github.com/OpenGalaxea/GalaxeaVLA) · [项目页](https://opengalaxea.github.io/G05/) |
| [GigaBrain-0.7：以三系统协同生成跨本体机器人动作](论文逐篇解读/P269.md) | GigaBrain-0.7以VLA为最终动作策略，将场景理解与子任务规划、未来视频/进度预测、MoT连续动作生成协同起来，使用异构轨迹和VLM数据预训练，并支持世界模型条件微调及经验强化。 | [原文](https://arxiv.org/abs/2608.15875) · [代码](https://github.com/open-gigaai/giga-brain-0) · [项目页](https://gigaai.cc/blog/gigabrain07) |
| [GVLA：夹爪条件化的视觉语言动作策略](论文逐篇解读/P326.md) | MiGA覆盖五类夹爪的多视角示范与策略标签，GVLA以三级夹爪提示和平台/夹爪双MoA条件化π0.5动作生成，提升四类抓取表现并支持UR5少样本迁移。 | [原文](https://arxiv.org/abs/2608.24603) · [项目页](https://airvlab.github.io/G-VLA/) |
| [HEX：以预测本体动力学支撑人形全身操作](论文逐篇解读/P262.md) | HEX 用规范身体部位状态和形态感知 MoE 跨本体预测未来本体动力学，再以视觉语言条件和预测状态生成高层全身操作动作，由低层强化学习控制器保持平衡。 | [原文](https://arxiv.org/abs/2604.07993) · [代码](https://github.com/Open-X-Humanoid/HEX) · [项目页](https://hex-humanoid.github.io/) |
| [HumanEgo：从数分钟人类第一视角视频学习双臂操作策略](论文逐篇解读/P378.md) | 从人类第一视角视频恢复手物交互几何，以流匹配预测双臂末端动作块，并用三类未来状态目标强化少样本学习；四项WidowX实机任务平均成功率为92.5%，并测试跨相机与机械臂迁移。 | [原文](https://arxiv.org/abs/2605.24934) · [代码](https://github.com/TX-Leo/HumanEgo) · [项目页](https://humanego-ai.github.io/) |
| [Hy-Embodied-0.5-VLA：从VLA策略到真机学习执行栈](论文逐篇解读/P291.md) | 以Hy-Embodied MoT骨干和连续流匹配Action Expert输出相对末端delta动作块，结合10K小时UMI预训练、跨本体部署、异步轨迹拼接及FlowPRO真实失败偏好优化。 | [原文](https://arxiv.org/abs/2606.14409) · [代码](https://github.com/Tencent-Hunyuan/Hy-Embodied-0.5-VLA) |
| [IronMind：以第一视角预训练扩展人形灵巧操作](论文逐篇解读/P366.md) | 以相机坐标动作统一第一视角人类与异构机器人示范，预训练可共同优化动作流匹配及深度、语义、未来帧目标；推理仅输出动作，在IRON-R01上开展闭环实机评测。 | [原文](https://arxiv.org/abs/2609.39403) · [项目页](https://xpeng-robotics.github.io/ironmind/) |
| [JALA：联合对齐潜动作的开放域 VLA 预训练](论文逐篇解读/P307.md) | 以起止帧逆动力学提取latent action，与VLA遮蔽动作块的预测嵌入联合对齐，使7.5M实验室及野外人类视频参与动作预训练。 | [原文](https://arxiv.org/abs/2602.21736) · [代码](https://github.com/BeingBeyond/JALA) · [项目页](https://research.beingbeyond.com/jala) |
| [LayerRoute：面向视觉语言动作策略的动作条件多层路由](论文逐篇解读/P359.md) | LayerRoute按当前动作token状态对多个视觉语言主干层的特征动态加权，并令后续动作块直接读取早期动作表示；系统集成到StarVLA-π与π0.5。在LIBERO Long上分别提升7.2和3.6个百分点，Franka三项任务亦报告成功率提升。 | [原文](https://arxiv.org/abs/2609.06079) |
| [N0-Foundation：面向触觉智能的视触觉操作基座](论文逐篇解读/P322.md) | N0-Foundation将视触觉采集、力场标定、OpenNeoData、NeoForce时序表征与NeoReal/NeoSim评测连接起来，使操作策略能够使用跨传感器一致的三轴接触力信息。 | [原文](https://arxiv.org/abs/2608.29601) · [代码](https://github.com/neoteai/N0-Foundation) · [项目页](https://research.neoteai.com/n0-foundation/) |
| [UCAG-P：相机中心动作几何统一异构操作策略](论文逐篇解读/P324.md) | 以相机坐标中的腕部/末端和抓取中心轨迹作为跨本体共享动作，再结合标定、Jacobian和本体状态翻译为执行命令，统一训练人类、单臂、双臂和人形数据。 | [原文](https://arxiv.org/abs/2608.26058) · [代码](https://github.com/Public-BOTs/ucag-p) · [项目页](https://public-bots.github.io/UCAG-P/) |
| [Pelican-VLA 0.5：以动作前的视觉瓶颈形成任务相关注意](论文逐篇解读/P264.md) | 单一Qwen3-VL主干以BotTokens作为感知到动作的窄接口，并联合预测动作、未来图像潜变量和语言任务表示；动作输出是策略目标，未来帧为训练辅助监督。 | [原文](https://arxiv.org/abs/2607.06655) · [代码](https://github.com/Open-X-Humanoid/Pelican-VLA05) |
| [Qwen-RobotManip：对齐异构数据的操作基础模型](论文逐篇解读/P258.md) | 对齐异构本体的状态动作接口和示范数据，训练视觉语言条件连续动作块策略并迁移人类第一视角操作信息。 | [原文](https://arxiv.org/abs/2606.17846) · [代码](https://github.com/QwenLM/Qwen-RobotManip) · [项目页](https://qwen.ai/blog?id=qwen-robotmanip) |
| [Qwen-RobotNav：面向Agent导航的可配置航点策略](论文逐篇解读/P260.md) | 从图像历史和自然语言目标预测移动机器人航点，并由上层导航Agent组织记忆、子目标和执行循环。 | [原文](https://arxiv.org/abs/2606.18112) · [代码](https://github.com/QwenLM/Qwen-RobotNav) · [项目页](https://qwen.ai/blog?id=qwen-robotnav) |
| [Rethink-VLA：异构机器人数据缩放中的物理对齐与训练实证](论文逐篇解读/P308.md) | 以受控MoT与flow-matching VLA实验比较四类末端坐标、异构本体数据累积配比、感觉dropout和分阶段优化，并提出真机匿名盲测协议。 | [原文](https://arxiv.org/abs/2602.09722) · [代码](https://github.com/BeingBeyond/Rethink_VLA) · [项目页](https://research.beingbeyond.com/rethink_vla) |
| [RynnBrain 1.1：增强具身理解与跨本体动作策略](论文逐篇解读/P275.md) | 在具身时空基础模型中加入显式3D物体框和接触点监督，并以81维分组遮罩与RTC构建G1、Astribot、Tianji-Wuji跨本体flow-matching动作策略。 | [原文](https://arxiv.org/abs/2607.17977) · [代码](https://github.com/alibaba-damo-academy/RynnBrain) · [项目页](https://alibaba-damo-academy.github.io/RynnBrain.github.io) |
| [ABC：开放数据驱动的规模化行为克隆](论文逐篇解读/P321.md) | ABC发布双臂YAM的ABC-130K真实操作数据，并配套扩散Transformer与VLM扩散动作头、H200训练流程、MuJoCo遥操作及真机任务评估，形成规模化行为克隆实验栈。 | [原文](https://arxiv.org/abs/2606.27375) · [代码](https://github.com/amazon-far/abc) · [项目页](https://abc.bot/) |
| [VINE：生成式控制策略的价值梯度后训练](论文逐篇解读/P184.md) | 重构流匹配去噪插值状态，使价值梯度可稳定优化生成策略，用于离线强化学习后训练。 | [原文](https://arxiv.org/abs/2607.10369) · [项目页](https://github.com/AgibotTech/vine) |
| [TANGO：从语言和第一视角图像预测人形全身导航动作](论文逐篇解读/P228.md) | 以仿真Plan–Edit–Track数据训练全身导航VLA，从语言和RGB历史预测人形关节动作，零样本部署到G1。 | [原文](https://arxiv.org/abs/2609.09158) |
| [TemporalFlow-VLA：用物理时序监督学习长时操作历史](论文逐篇解读/P240.md) | 从机器人状态和几何构造仅用于训练的表面时序流监督，以短、长时间查询压缩执行历史并送入VLA动作专家，部署时无需几何重建。 | [原文](https://arxiv.org/abs/2608.26821) |
| [The Gaussian Is Enough：大行为模型微调中的动作先验比较](论文逐篇解读/P351.md) | 该研究对七种动作先验、五档微调数据比例和三个行为模型开展仿真与硬件对照，发现通常高斯先验已足够，约5%示教数据时嵌入扰动先验可提高成功率。 | [原文](https://arxiv.org/abs/2609.27070) · [项目页](https://cxu-tri.github.io/non_gaussian_FT/) |
| [TurboVLA：把视觉语言直接送入低延迟动作解码器](论文逐篇解读/P208.md) | 以紧凑视觉语言编码和动作解码器直接从视觉、语言与本体状态生成低延迟操作动作。 | [原文](https://arxiv.org/abs/2607.27205) · [代码](https://github.com/H-EmbodVis/TurboVLA) · [项目页](https://h-embodvis.github.io/TurboVLA/) |
| [VITRA：把无标注人类活动视频加工成VLA预训练片段](论文逐篇解读/P167.md) | 从日常视频提取手物运动轨迹作为中间表示，再用机器人数据适配操作动作空间。 | [原文](https://arxiv.org/abs/2510.21571) · [代码](https://github.com/microsoft/VITRA) |
| [WALL-X：梯度桥接预训练的多本体部署VLA](论文逐篇解读/P299.md) | 以 Mixture-of-Transformers 路由视觉语言与动作专家，通过离散动作 token 梯度桥接预训练主干，再用连续流匹配动作专家形成多本体部署策略。 | [原文](https://arxiv.org/abs/2605.30877) · [代码](https://github.com/X-Square-Robot/wall-x) · [项目页](https://x2robot.com/en/oss) |
| [X-Tokenizer：将动作语义接入VLA预训练的分层编码器](论文逐篇解读/P293.md) | 用语义残差量化将跨本体连续delta动作分层为离散意图码和执行残差，并以动作掩码预测、冻结VLM对齐和下一帧特征预测塑造VLA表征。 | [原文](https://arxiv.org/abs/2606.14752) · [代码](https://github.com/X-Square-Robot/X-Tokenizer) · [项目页](https://x-square-robot.github.io/X-Tokenizer_projectPage/) |
| [Xiaomi-Robotics-0：面向实时执行的双臂操作VLA](论文逐篇解读/P286.md) | 从图像、语言和本体状态生成双臂连续动作块，以流匹配和延迟前缀条件的异步拼接维持实时执行，并在仿真及LEGO分拣、毛巾折叠真机任务评测。 | [原文](https://arxiv.org/abs/2602.12684) · [代码](https://github.com/XiaomiRobotics/Xiaomi-Robotics-0) · [项目页](https://xiaomi-robotics-0.github.io/) |
| [Xiaomi-Robotics-1：以十万小时真实轨迹扩展VLA](论文逐篇解读/P287.md) | 以超过10万小时UMI第一视角真实操作轨迹和自动状态变化标注预训练VLM—DiT连续动作策略，再通过跨本体后训练适配机器人操作。 | [原文](https://arxiv.org/abs/2607.15330) · [代码](https://github.com/XiaomiRobotics/Xiaomi-Robotics-1) · [项目页](https://robotics.xiaomi.com/xiaomi-robotics-1.html) |
| [τ₀-VLA：用世界模型搜索组织长任务与低层动作](论文逐篇解读/P201.md) | 结合执行记忆、世界模型引导测试时搜索和反思策略，处理长程家庭移动操作任务。 | [原文](https://arxiv.org/abs/2608.16885) · [代码](https://github.com/sii-research/tau-0-vla) · [项目页](https://tau0-vla.github.io/) |
| [DeepThinkVLA：因果对齐推理与并行动作解码的 VLA](论文逐篇解读/P306.md) | 因果自回归生成具身CoT，再以双向并行动作槽输出动作块，并用任务成败稀疏奖励强化思维链与执行结果的因果联系。 | [原文](https://arxiv.org/abs/2511.15669) · [代码](https://github.com/OpenBMB/DeepThinkVLA) |
| [OpenVLA-OFT：以并行解码优化 VLA 微调与控制](论文逐篇解读/P302.md) | 通过并行解码、动作分块、连续动作L1回归及可选腕部图像/本体状态微调OpenVLA，并在ALOHA扩展FiLM语言调制，使策略兼顾LIBERO成功率、动作生成吞吐与双臂实机执行。 | [原文](https://arxiv.org/abs/2502.19645) · [代码](https://github.com/moojink/openvla-oft) · [项目页](https://openvla-oft.github.io/) |
| [Gemini Robotics：面向物理世界的通用机器人智能模型](论文逐篇解读/P061.md) | 将具身推理与视觉动作模型分级运行，并以少量本体数据适配机器人操作、规划和工具使用。 | [原文](https://deepmind.google/models/gemini-robotics/) |
| [GEN-0：跨本体真实操作数据驱动的通用机器人策略](论文逐篇解读/P172.md) | 统一多自由度机器人操作数据进行大规模预训练，再用少量目标任务数据后训练策略。 | [原文](https://generalistai.com/blog/gen-0) |
| [GR00T N1：面向通用人形机器人的基础模型](论文逐篇解读/P060.md) | 以视觉语言主干和扩散动作Transformer整合异构人形数据，并用本体专用编码接入身体控制接口。 | [原文](https://arxiv.org/abs/2503.14734) · [代码](https://github.com/NVIDIA/Isaac-GR00T) · [项目页](https://developer.nvidia.com/isaac/gr00t) |
| [GraspVLA：十亿帧合成数据驱动的开放类别抓取](论文逐篇解读/P301.md) | 在SynGrasp-1B合成抓取轨迹与互联网目标定位数据上联合训练VLM和流匹配动作专家，以PAG逐步预测二维目标框、三维抓取姿态和连续末端动作，并验证真机开放类别抓取及LIBERO零样本迁移。 | [原文](https://arxiv.org/abs/2505.03233) · [代码](https://github.com/PKU-EPIC/GraspVLA) |
| [LeVERB：基于潜在视觉语言指令的人形全身控制](论文逐篇解读/P062.md) | 从视频与动作学习视觉语言潜指令，由高层选取技能并让冻结低层策略执行人形全身动作。 | [原文](https://arxiv.org/abs/2506.13751) |
| [Phantom：先把人类示范改造成目标机器人看到的训练画面](论文逐篇解读/P169.md) | 将人手动作重定向至机器人并替换训练图像中的人臂外观，用于无机器人操作数据训练。 | [原文](https://arxiv.org/abs/2503.00779) · [代码](https://github.com/MarionLepert/phantom) · [项目页](https://phantom-human-videos.github.io/) |
| [RynnVLA-001：人类演示预训练的机器人操作VLA](论文逐篇解读/P296.md) | 将第一视角人类操作视频的未来帧预测、手腕轨迹与机器人动作潜码逐阶段对齐，最终由视觉语言策略生成 ActionVAE 解码的连续机器人动作块。 | [原文](https://arxiv.org/abs/2509.15212) · [代码](https://github.com/alibaba-damo-academy/RynnVLA-001) |
| [SmolVLA：轻量视觉语言动作模型与异步执行](论文逐篇解读/P303.md) | 以SmolVLM2和流匹配Action Expert构建0.45B轻量VLA，在481个社区数据集上预训练，通过视觉token压缩、层跳过和异步动作队列降低推理等待，并评估LIBERO、Meta-World及SO100/SO101真机任务。 | [原文](https://arxiv.org/abs/2506.01844) · [代码](https://github.com/huggingface/lerobot) · [项目页](https://huggingface.co/blog/smolvla) |
| [VIPA-VLA：人类视频视觉—物理对齐的空间感知 VLA 预训练](论文逐篇解读/P309.md) | 用人手与物体米制空间标注、三维关系问答及离散腕部轨迹预训练双编码器VLA，再以flow-matching DiT适配机器人动作块。 | [原文](https://arxiv.org/abs/2512.13080) · [代码](https://github.com/BeingBeyond/VIPA-VLA) · [项目页](https://beingbeyond.github.io/VIPA-VLA) |
| [VPP：从视频预测表征直接生成通用机器人动作](论文逐篇解读/P318.md) | 冻结视频预测主干提取预测中间特征，由VideoFormer和扩散动作头直接生成动作块；评测覆盖CALVIN、Meta-World、Franka与灵巧手。 | [原文](https://arxiv.org/abs/2412.14803) · [代码](https://github.com/roboterax/video-prediction-policy) · [项目页](https://video-prediction-policy.github.io/) |
| [WALL-X：从视觉语言理解到连续机器人操作](论文逐篇解读/P298.md) | 基于 Qwen2.5-VL-3B 以具身问答、FAST 离散动作和连续流匹配动作分阶段训练，将场景理解、子任务推理与机器人操作策略接入统一模型。 | [原文](https://arxiv.org/abs/2509.11766) · [代码](https://github.com/X-Square-Robot/wall-x) · [项目页](https://x2robot.com/en/oss) |
| [WholeBodyVLA：面向全身移动操作控制的统一潜在VLA](论文逐篇解读/P097.md) | 从第一视角视频学习潜在动作token，由VLA预测双臂动作和移动命令，低层策略负责平衡执行。 | [原文](https://arxiv.org/abs/2512.11047) · [项目页](https://opendrivelab.com/WholeBodyVLA/) |
| [XR-1：用统一视觉—运动码支撑跨本体动作策略](论文逐篇解读/P263.md) | 以视觉动态分支和机器人运动分支联合训练离散 UVMC，再将联合码作为 VLA 辅助预测目标，分三阶段完成跨本体预训练、动作学习和目标任务微调。 | [原文](https://arxiv.org/abs/2511.02776) · [代码](https://github.com/Open-X-Humanoid/XR-1) · [项目页](https://xr-1-vla.github.io/) |
| [π0.5：具备开放世界泛化能力的视觉语言动作模型](论文逐篇解读/P059.md) | 分阶段对齐网页语义、多源机器人数据与长程移动操作，再训练连续动作头用于开放家庭任务。 | [原文](https://arxiv.org/abs/2504.16054) · [代码](https://github.com/Physical-Intelligence/openpi) · [项目页](https://www.physicalintelligence.company/blog/pi05) |
| [VLA Survey：具身智能视觉语言动作模型综述](论文逐篇解读/P071.md) | 按感知编码、语言推理、动作表示和部署组件分类视觉语言动作模型及其操作规划任务。 | [原文](https://arxiv.org/abs/2405.14093) |
| [EgoMimic：以共享姿态监督联合人类视频与机器人示范](论文逐篇解读/P170.md) | 人类和机器人数据共享姿态预测，仅在机器人样本训练动作头以扩展模仿学习和真机操作。 | [原文](https://arxiv.org/abs/2410.24221) · [代码](https://github.com/SimarKareer/EgoMimic) · [项目页](https://egomimic.github.io/) |
| [Octo：通用机器人策略](论文逐篇解读/P056.md) | 用块状注意力Transformer学习通用操作表示，以独立读出头适配新机器人的观测和动作。 | [原文](https://arxiv.org/abs/2405.12213) · [代码](https://github.com/octo-models/octo) · [项目页](https://octo-models.github.io/) |
| [OpenVLA：视觉语言动作模型](论文逐篇解读/P057.md) | 以双视觉编码器、离散动作token和LoRA微调构建视觉语言动作操作模型。 | [原文](https://arxiv.org/abs/2406.09246) · [代码](https://github.com/openvla/openvla) · [项目页](https://openvla.github.io/) |
| [GR-1：以大规模视频生成预训练增强视觉机器人操作](论文逐篇解读/P317.md) | 以Ego4D下一帧预测预训练共享时序模型，联合监督动作和未来图像，在CALVIN长程操作及Kinova Gen2真机上评测。 | [原文](https://arxiv.org/abs/2312.13139) · [代码](https://github.com/bytedance/GR-1) · [项目页](https://gr1-manipulation.github.io/) |
| [π0：面向通用机器人控制的视觉语言动作流模型](论文逐篇解读/P058.md) | 由视觉语言主干提供语义条件、Flow Matching动作专家生成连续动作块，面向跨本体机器人操作。 | [原文](https://arxiv.org/abs/2410.24164) · [代码](https://github.com/Physical-Intelligence/openpi) · [项目页](https://www.physicalintelligence.company/blog/pi0) |
| [Diffusion Policy：基于动作扩散的视觉运动策略学习](论文逐篇解读/P050.md) | 以条件扩散生成连续操作动作块，滚动执行前缀并根据新视觉观测重规划，构成操作闭环。 | [原文](https://arxiv.org/abs/2303.04137) · [代码](https://github.com/real-stanford/diffusion_policy) · [项目页](https://diffusion-policy.cs.columbia.edu/) |
| [ACT / ALOHA：基于低成本硬件的精细双臂操作学习](论文逐篇解读/P051.md) | 用条件VAE与Transformer生成双臂操作动作块，并以时间集成平滑重叠预测。 | [原文](https://arxiv.org/abs/2304.13705) · [代码](https://github.com/tonyzhaozh/act) · [项目页](https://tonyzhaozh.github.io/aloha/) |
| [UniPi：用文本引导视频生成构造通用操作计划](论文逐篇解读/P316.md) | 由任务文本和当前帧生成未来视觉计划，再以独立逆动力学模型将计划帧变化解码为动作；评测覆盖模拟操作与Bridge计划视频迁移。 | [原文](https://arxiv.org/abs/2302.00111) · [项目页](https://universal-policy.github.io/) |
| [Open X-Embodiment：跨本体机器人学习数据集与RT-X模型](论文逐篇解读/P055.md) | 以统一协议保留本体差异并混合多机器人轨迹，训练和评估跨本体机器人操作策略。 | [原文](https://arxiv.org/abs/2310.08864) · [代码](https://github.com/google-deepmind/open_x_embodiment) · [项目页](https://robotics-transformer-x.github.io/) |
| [RT-2：将网络知识迁移到机器人控制的视觉语言动作模型](论文逐篇解读/P054.md) | 共同微调视觉语言任务与机器人轨迹，并将连续控制离散为动作token以研究语义迁移操作。 | [原文](https://arxiv.org/abs/2307.15818) · [项目页](https://robotics-transformer2.github.io/) |
| [RT-1：面向大规模真实世界控制的机器人Transformer](论文逐篇解读/P052.md) | 以TokenLearner压缩图像、Transformer预测离散动作token，学习真实机器人多任务操作策略。 | [原文](https://arxiv.org/abs/2212.06817) · [项目页](https://robotics-transformer1.github.io/) |

#### 相关项目

| 项目 | 主要用途 | 功能与特点 |
| --- | --- | --- |
| [ABC](https://github.com/amazon-far/abc) | VLA与通用操作策略 | ABC发布双臂YAM的ABC-130K真实操作数据，并配套扩散Transformer与VLM扩散动作头、H200训练流程、MuJoCo遥操作及真机任务评估，形成规模化行为克隆实验栈。 |
| [ABot-Navigation](https://github.com/amap-cvlab/ABot-Navigation) | VLA与通用操作策略 | 把点目标、语言指令、物体目标、POI与行人跟随统一为自然语言条件导航；慢速Qwen视觉语言推理输出CoT及可通行/目标像素，快速动作专家解码连续SE(2)航点并异步闭环执行。 |
| [ACoT-VLA](https://github.com/AgibotTech/ACoT-VLA) | VLA与通用操作策略 | 以显式粗参考轨迹和VLM层内隐式动作先验构成动作链式推理，条件化flow-matching动作头，提升长时程操作及扰动迁移表现。 |
| [ACT](https://github.com/tonyzhaozh/act) | 模仿学习 | 以条件VAE和Transformer预测动作块，并通过时间集成平滑控制，连接双臂示范采集与策略部署流程。 |
| [Being-H0](https://github.com/BeingBeyond/Being-H0) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [BridgeVLA++](https://github.com/npucvr/BridgeVLA-Seq) | 带时空双记忆的操作策略 | 为BridgeVLA加入空间信息和时间记忆，提供预训练、真实机器人微调与评测，用于历史状态条件下的操作策略。 |
| [CLIFT](https://thomaschen98.github.io/clift/) | VLA与通用操作策略 | 把部署后的真机轨迹转成优势标注的监督样本，经托管SFT接口迭代VLA，缓解权重封闭模型在接触操作中的任务适配不足。 |
| [DeepThinkVLA](https://github.com/OpenBMB/DeepThinkVLA) | VLA与通用操作策略 | 因果自回归生成具身CoT，再以双向并行动作槽输出动作块，并用任务成败稀疏奖励强化思维链与执行结果的因果联系。 |
| [Diffusion Policy](https://github.com/real-stanford/diffusion_policy) | 机器人策略 | 以条件扩散生成未来动作轨迹，由视觉和本体观测引导去噪，并通过滚动动作窗口执行闭环控制。 |
| [DriftingVLA](https://arxiv.org/abs/2608.29749) | VLA与通用操作策略 | 从噪声一次生成完整动作块，以PDTD对每个动作维的完整时序轨迹分别建立漂移几何，保留联合动作输出，在LIBERO、RoboTwin与双UR5真机验证精度和时延。 |
| [DualManip](https://lichengxi1.github.io/Dualmanip) | VLA与通用操作策略 | DualManip用较慢的语义路径拆解任务并初始化交互点，再用实时RGB-D几何路径在物体移动或形变时更新模板对应关系和抓取接触位置；信息交互模块校验几何更新，必要时触发语义重规划。论文在六项真实操作任务中评估静态、单次变化和连续变化场景。 |
| [GalaxeaDP](https://github.com/OpenGalaxea/GalaxeaDP) | 星海图双臂移动操作扩散策略 | 以相机观测、机器人状态和任务条件生成连续动作块，提供双臂及移动操作扩散策略。 |
| [GalaxeaVLA](https://github.com/OpenGalaxea/GalaxeaVLA) | 星海图移动操作视觉语言动作模型 | 将视觉、语言和本体状态转为Galaxea机器人动作，并以Action Codec连接自回归推理与连续控制。 |
| [GigaBrain-0](https://github.com/open-gigaai/giga-brain-0) | VLA与通用操作策略 | GigaBrain-0.7以VLA为最终动作策略，将场景理解与子任务规划、未来视频/进度预测、MoT连续动作生成协同起来，使用异构轨迹和VLM数据预训练，并支持世界模型条件微调及经验强化。 |
| [GR-1](https://github.com/bytedance/GR-1) | 视频生成预训练与多任务机器人操作 | 使用大规模第一人称视频预训练，并以联合动作与未来帧监督学习CALVIN及Kinova操作策略。 |
| [GraspVLA](https://github.com/PKU-EPIC/GraspVLA) | VLA与通用操作策略 | 在SynGrasp-1B合成抓取轨迹与互联网目标定位数据上联合训练VLM和流匹配动作专家，以PAG逐步预测二维目标框、三维抓取姿态和连续末端动作，并验证真机开放类别抓取及LIBERO零样本迁移。 |
| [GVLA](https://airvlab.github.io/G-VLA/) | VLA与通用操作策略 | MiGA覆盖五类夹爪的多视角示范与策略标签，GVLA以三级夹爪提示和平台/夹爪双MoA条件化π0.5动作生成，提升四类抓取表现并支持UR5少样本迁移。 |
| [HEX](https://github.com/Open-X-Humanoid/HEX) | VLA与通用操作策略 | HEX 用规范身体部位状态和形态感知 MoE 跨本体预测未来本体动力学，再以视觉语言条件和预测状态生成高层全身操作动作，由低层强化学习控制器保持平衡。 |
| [HumanEgo](https://github.com/TX-Leo/HumanEgo) | VLA与通用操作策略 | 从人类第一视角视频恢复手物交互几何，以流匹配预测双臂末端动作块，并用三类未来状态目标强化少样本学习；四项WidowX实机任务平均成功率为92.5%，并测试跨相机与机械臂迁移。 |
| [HY-Embodied-0.5-VLA](https://github.com/Tencent-Hunyuan/Hy-Embodied-0.5-VLA) | VLA与通用操作策略 | 以Hy-Embodied MoT骨干和连续流匹配Action Expert输出相对末端delta动作块，结合10K小时UMI预训练、跨本体部署、异步轨迹拼接及FlowPRO真实失败偏好优化。 |
| [HY-Embodied-0.5-X](https://github.com/Tencent-Hunyuan/HY-Embodied-0.5-X) | 跨本体具身动作模型 | 以共享多模态表征和统一动作接口学习不同机器人数据，支持跨本体训练与适配。 |
| [IronMind](https://xpeng-robotics.github.io/ironmind/) | VLA与通用操作策略 | 以相机坐标动作统一第一视角人类与异构机器人示范，预训练可共同优化动作流匹配及深度、语义、未来帧目标；推理仅输出动作，在IRON-R01上开展闭环实机评测。 |
| [Isaac-GR00T / GR00T N1.7](https://github.com/NVIDIA/Isaac-GR00T) | 人形基础模型 | GR00T N1.7以视觉语言主干和扩散动作头生成机器人动作，提供LeRobot后训练、推理及ONNX/TensorRT导出。 |
| [JALA](https://github.com/BeingBeyond/JALA) | VLA与通用操作策略 | 以起止帧逆动力学提取latent action，与VLA遮蔽动作块的预测嵌入联合对齐，使7.5M实验室及野外人类视频参与动作预训练。 |
| [LayerRoute](https://arxiv.org/abs/2609.06079) | VLA与通用操作策略 | LayerRoute按当前动作token状态对多个视觉语言主干层的特征动态加权，并令后续动作块直接读取早期动作表示；系统集成到StarVLA-π与π0.5。在LIBERO Long上分别提升7.2和3.6个百分点，Franka三项任务亦报告成功率提升。 |
| [LingBot-VLA 1.0](https://github.com/Robbyant/lingbot-vla) | VLA与通用操作策略 | LingBot-VLA 1.0基于约2万小时、9种双臂机器人构型的真实遥操作数据，使用Qwen2.5-VL与连续动作专家联合预测50步动作块，并通过深度表征蒸馏提升空间操作。 |
| [LingBot-VLA 2.0](https://github.com/Robbyant/lingbot-vla-v2) | VLA与通用操作策略 | LingBot-VLA 2.0以跨本体稀疏MoE、55维全身统一动作接口和当前/未来几何及因果视频特征蒸馏，训练生成机器人动作的VLA策略。 |
| [Mind-1](https://www.mindon.tech/blog/mind-1/index.html) | 跨本体高速操作模型 | 以人类自然速度示范、分层多模态策略、连续动作意图和全身控制完成跨本体高速操作；官方报告推理32 ms、端到端77.5 ms，打包/分拣各3秒、叠衣服25秒。 |
| [N0-Foundation](https://github.com/neoteai/N0-Foundation) | VLA与通用操作策略 | N0-Foundation将视触觉采集、力场标定、OpenNeoData、NeoForce时序表征与NeoReal/NeoSim评测连接起来，使操作策略能够使用跨传感器一致的三轴接触力信息。 |
| [Octo](https://github.com/octo-models/octo) | 通用策略 | 以Transformer和扩散动作头从多机器人数据学习通用策略，支持图像、语言、目标图像和模块化观测。 |
| [OpenDM](https://github.com/dexmal/opendm) | 开放世界机器人控制VLA | 根据语言、图像和机器人状态生成动作序列，支持开放指令、长时操作与动态干扰，并适配仿真和指定本体后训练。 |
| [openpi](https://github.com/Physical-Intelligence/openpi) | VLA | 提供流匹配π0、快速自回归π0-FAST和π0.5的检查点、数据配置、微调与推理服务。 |
| [OpenVLA](https://github.com/openvla/openvla) | VLA | 视觉语言模型根据图像和指令生成机器人动作，并连接RLDS数据混合、策略微调、推理与部署流程。 |
| [OpenVLA-OFT](https://github.com/moojink/openvla-oft) | VLA与通用操作策略 | 通过并行解码、动作分块、连续动作L1回归及可选腕部图像/本体状态微调OpenVLA，并在ALOHA扩展FiLM语言调制，使策略兼顾LIBERO成功率、动作生成吞吐与双臂实机执行。 |
| [Pelican-VLA 0.5](https://github.com/Open-X-Humanoid/Pelican-VLA05) | VLA与通用操作策略 | 单一Qwen3-VL主干以BotTokens作为感知到动作的窄接口，并联合预测动作、未来图像潜变量和语言任务表示；动作输出是策略目标，未来帧为训练辅助监督。 |
| [Qwen-RobotManip](https://github.com/QwenLM/Qwen-RobotManip) | 机器人操作基础模型 | 对齐异构本体的状态动作接口和示范数据，训练视觉语言条件连续动作块策略并迁移人类第一视角操作信息。 |
| [Qwen-RobotNav](https://github.com/QwenLM/Qwen-RobotNav) | 具身导航策略模型 | 从图像历史和自然语言目标预测移动机器人航点，并由上层导航Agent组织记忆、子目标和执行循环。 |
| [Rethink_VLA](https://github.com/BeingBeyond/Rethink_VLA) | VLA与通用操作策略 | 以受控MoT与flow-matching VLA实验比较四类末端坐标、异构本体数据累积配比、感觉dropout和分阶段优化，并提出真机匿名盲测协议。 |
| [RynnBrain](https://github.com/alibaba-damo-academy/RynnBrain) | VLA与通用操作策略 | 在具身时空基础模型中加入显式3D物体框和接触点监督，并以81维分组遮罩与RTC构建G1、Astribot、Tianji-Wuji跨本体flow-matching动作策略。 |
| [RynnVLA-001](https://github.com/alibaba-damo-academy/RynnVLA-001) | VLA与通用操作策略 | 将第一视角人类操作视频的未来帧预测、手腕轨迹与机器人动作潜码逐阶段对齐，最终由视觉语言策略生成 ActionVAE 解码的连续机器人动作块。 |
| [SmolVLA](https://huggingface.co/blog/smolvla) | VLA与通用操作策略 | 以SmolVLM2和流匹配Action Expert构建0.45B轻量VLA，在481个社区数据集上预训练，通过视觉token压缩、层跳过和异步动作队列降低推理等待，并评估LIBERO、Meta-World及SO100/SO101真机任务。 |
| [Spirit-v1.5](https://github.com/Spirit-AI-Team/spirit-v1.5) | 千寻智能具身操作基础模型 | 根据视觉、语言和机器人状态生成操作动作，面向多任务及真实场景泛化研究。 |
| [The Gaussian Is Enough](https://cxu-tri.github.io/non_gaussian_FT/) | VLA与通用操作策略 | 该研究对七种动作先验、五档微调数据比例和三个行为模型开展仿真与硬件对照，发现通常高斯先验已足够，约5%示教数据时嵌入扰动先验可提高成功率。 |
| [TurboVLA](https://github.com/H-EmbodVis/TurboVLA) | 不经大型语言模型中枢的动作生成 | 将视觉语言条件直接连接轻量动作策略，提供训练、评测和模型入口，面向无需大型语言模型中枢的动作生成。 |
| [UCAG-P](https://github.com/Public-BOTs/ucag-p) | VLA与通用操作策略 | 以相机坐标中的腕部/末端和抓取中心轨迹作为跨本体共享动作，再结合标定、Jacobian和本体状态翻译为执行命令，统一训练人类、单臂、双臂和人形数据。 |
| [UnifoLM-VLA-0](https://github.com/unitreerobotics/unifolm-vla) | 宇树视觉语言动作训练与部署框架 | 将LeRobot数据转换为HDF5和RLDS，连接多数据集训练、LIBERO评测、服务推理与G1部署。 |
| [UniPi](https://universal-policy.github.io/) | 文本引导视频规划与动作解码 | 从任务语言与当前图像生成未来视觉计划，再由独立逆动力学模型解码可执行动作。 |
| [video-prediction-policy](https://github.com/roboterax/video-prediction-policy) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [VIPA-VLA](https://github.com/BeingBeyond/VIPA-VLA) | VLA与通用操作策略 | 用人手与物体米制空间标注、三维关系问答及离散腕部轨迹预训练双编码器VLA，再以flow-matching DiT适配机器人动作块。 |
| [WALL-X](https://github.com/X-Square-Robot/WALL-X) | VLA与通用操作策略 | 以 Mixture-of-Transformers 路由视觉语言与动作专家，通过离散动作 token 梯度桥接预训练主干，再用连续流匹配动作专家形成多本体部署策略。 |
| [WholeBodyVLA](https://github.com/OpenDriveLab/WholebodyVLA) | 人形VLA | 从无动作标注的第一视角视频学习潜在动作，将视觉语言条件解码为双臂动作和运动命令，用于视频驱动的机器人动作生成。 |
| [X-Tokenizer](https://github.com/X-Square-Robot/X-Tokenizer) | VLA与通用操作策略 | 用语义残差量化将跨本体连续delta动作分层为离散意图码和执行残差，并以动作掩码预测、冻结VLM对齐和下一帧特征预测塑造VLA表征。 |
| [Xiaomi-Robotics-0](https://github.com/XiaomiRobotics/Xiaomi-Robotics-0) | VLA与通用操作策略 | 从图像、语言和本体状态生成双臂连续动作块，以流匹配和延迟前缀条件的异步拼接维持实时执行，并在仿真及LEGO分拣、毛巾折叠真机任务评测。 |
| [Xiaomi-Robotics-1](https://github.com/XiaomiRobotics/Xiaomi-Robotics-1) | VLA与通用操作策略 | 以超过10万小时UMI第一视角真实操作轨迹和自动状态变化标注预训练VLM—DiT连续动作策略，再通过跨本体后训练适配机器人操作。 |
| [XR-1](https://github.com/Open-X-Humanoid/XR-1) | VLA与通用操作策略 | 以视觉动态分支和机器人运动分支联合训练离散 UVMC，再将联合码作为 VLA 辅助预测目标，分三阶段完成跨本体预训练、动作学习和目标任务微调。 |
| [τ0-VLA](https://github.com/sii-research/tau-0-vla) | 分层任务规划体系的低层策略实现 | 面向τ0-VLA低层策略训练与推理并输出低层动作；高层提案、世界模型与价值规划需由外部模块完成。 |

[返回本页导航](#本页导航)

## 世界动作模型（WAM）

在观测和任务条件下联合学习动作与未来世界，通过世界预测支持动作生成、候选评估或闭环规划；部分方法部署时仅运行动作分支。

**43** 篇论文／报告 · **36** 个项目

#### 论文与技术报告

| 论文／报告 | 主要方法与用途 | 原文／代码 |
| --- | --- | --- |
| [ABot-M0.5：统一移动与操作的世界动作模型](论文逐篇解读/P277.md) | 以未来视频潜变量、帧级视觉latent action、移动/操作可执行动作构成三级WAM级联；双层MoT解耦模态与异构动作，Dream Forcing使用模型自生成未来训练逆动力学。 | [原文](https://arxiv.org/abs/2607.00678) · [代码](https://github.com/amap-cvlab/ABot-Manipulation) |
| [AR-WAM：视觉条件与Agent协作的世界动作策略](论文逐篇解读/P349.md) | AR-WAM以目标框和原子操作token取代策略端自然语言，联合输出可监督的目标理解、压缩未来场景latent与动作块；Agent通过detect/execute/query接口提供高层指令并管理长程记忆。 | [原文](https://arxiv.org/abs/2609.23578) |
| [Being-H0.7：第一视角视频预训练的潜在世界动作模型](论文逐篇解读/P314.md) | 通过训练期未来观测后验与当前上下文先验的潜在表示对齐，学习未来感知动作推理；部署时先验分支直接生成动作块，支持多本体操作。 | [原文](https://arxiv.org/abs/2605.00078) · [代码](https://github.com/BeingBeyond/Being-H) · [项目页](https://research.beingbeyond.com/being-h07) |
| [LingBot-VA 1.0：因果视频—动作联合建模与机器人控制](论文逐篇解读/P255.md) | 视频潜变量流与机器人动作流在双流Transformer中交替建模，模型既预测动作也预测动作条件下的未来画面；仓库开放权重、RoboTwin与LIBERO后训练数据、训练和推理脚本，可检查世界预测怎样与策略输出共享表示但保持独立输出。 | [原文](https://arxiv.org/abs/2601.21998) · [代码](https://github.com/Robbyant/lingbot-va) · [项目页](https://technology.robbyant.com/lingbot-va) |
| [Cosmos Policy：基于视频扩散的机器人策略与规划](论文逐篇解读/P254.md) | 将Cosmos视频生成主干后训练为 visuomotor policy，并扩展未来观测和值预测以支持候选动作规划。 | [原文](https://arxiv.org/pdf/2601.16163) · [代码](https://github.com/NVlabs/cosmos-policy) · [项目页](https://research.nvidia.com/labs/dir/cosmos-policy/) |
| [DELE-w0.5：用未来状态辅助训练，部署时直接生成动作](论文逐篇解读/P193.md) | 训练时联合动作与未来视觉潜变量，部署时移除未来分支以直接生成双臂操作动作。 | [原文](https://arxiv.org/abs/2608.22067) · [项目页](https://deepleap-x.com/research/dele-w0.5) |
| [Delta-0：世界动作模型驱动的全身移动操作](论文逐篇解读/P249.md) | 将潜在世界动作模型与学习型全身控制器连接，以人体数据预训练、仿真评测和实机RL后训练完成家庭移动操作。 | [原文](https://deltai.com/en/blog/delta-0) |
| [DIAL：潜在世界建模解耦意图与动作](论文逐篇解读/P310.md) | System-2以VLM query预测未来ViT视觉latent，System-1以当前-未来latent差异和本体状态驱动DiT flow matching生成动作，并经warmup后端到端联合优化。 | [原文](https://arxiv.org/abs/2603.29844) · [代码](https://github.com/xpeng-robotics/DIAL) · [项目页](https://xpeng-robotics.github.io/dial) |
| [DiT4DiT：联合视频动力学与动作生成的泛化机器人控制](论文逐篇解读/P313.md) | 联合flow matching生成未来视频latent与机器人动作，并抽取视频DiT去噪中间特征条件化动作DiT，在LIBERO、RoboCasa-GR1和Unitree G1评测空间操作及分布变化泛化。 | [原文](https://arxiv.org/abs/2603.10448) · [代码](https://github.com/Mondo-Robotics/DiT4DiT) |
| [DualWAM：异步全局规划与局部闭环修正](论文逐篇解读/P346.md) | DualWAM用高噪声System 2异步生成长时程全局世界动作计划，并让低噪声腕部System 1基于新观测精修时间对齐局部视频与动作窗口，在真实双本体任务上评测成功率和时延。 | [原文](https://arxiv.org/abs/2609.24868) · [项目页](https://steveouo.github.io/DualWAM-Web/) |
| [Dyna-2：百万小时人类视频预训练的世界动作模型](论文逐篇解读/P361.md) | 以百万小时第一视角人类视频共同训练未来视频与动作预测，研究数据规模对跨本体迁移的影响；动作策略经机器人示范后训练执行双臂、灵巧手和半人形操作。 | [原文](https://www.dyna.co/dyna-2) |
| [Fast-WAM：保留视频共训练，部署时跳过未来想象](论文逐篇解读/P198.md) | 保留训练期视频动作共训并在测试时跳过未来视频生成，比较世界动作模型直接控制与想象推演。 | [原文](https://arxiv.org/abs/2603.16666) · [代码](https://github.com/yuantianyuan01/FastWAM) · [项目页](https://yuantianyuan01.github.io/FastWAM/) |
| [Flex-π：让同一个世界动作模型按计算预算选择输出流](论文逐篇解读/P206.md) | 联合去噪RGB、三维、语义和动作流，并以流丢弃支持不同计算配置下的机器人操作推理。 | [原文](https://arxiv.org/abs/2608.10860) · [代码](https://github.com/geyan21/flex-pi) · [项目页](https://flex-pi.github.io/) |
| [GE-Act 2.0：用单步未来状态和行为兼容性训练WAM](论文逐篇解读/P195.md) | 结合控制导向表征、未来视觉规划和逆动力学利用异构数据，研究世界动作模型预训练与规模化。 | [原文](https://arxiv.org/abs/2609.05588) · [项目页](https://ge-act-v2.github.io/) |
| [GigaWorld-Policy-0.5：将未来视觉监督留在训练、动作留给部署](论文逐篇解读/P270.md) | GigaWorld-Policy-0.5在训练期以动作块和动作条件未来视觉联合学习WAM，在推理期仅解码动作；MoT拆分视觉专家和轻量动作专家，配合KV缓存、编译运行时与AutoResearch优化延迟和训练配置。 | [原文](https://arxiv.org/abs/2607.13960) · [代码](https://github.com/open-gigaai/giga-world-policy) · [项目页](https://open-gigaai.github.io/giga-world-policy/) |
| [Hydra-0：以图像动作流连接世界预测与机器人控制](论文逐篇解读/P202.md) | 以Action Flow连接视频预测与控制，并对齐人手、夹爪和不同机器人本体的视觉运动接口。 | [原文](https://arxiv.org/abs/2608.18077) · [代码](https://github.com/nvidia-isaac/video_to_data) · [项目页](https://nvidia-isaac.github.io/video_to_data/hydra-0/) |
| [Kairos：面向物理AI的遗憾感知世界动作栈](论文逐篇解读/P285.md) | 以控制充分状态统一VLM理解、未来视频生成和动作轨迹预测，并用局部/中程/全局混合时间记忆与分阶段人类、机器人数据训练世界动作策略。 | [原文](https://arxiv.org/abs/2606.16533) · [代码](https://github.com/DAXIAORobotics/kairos) |
| [LDA-1B：让不同质量的具身数据共同训练视觉预测与机器人动作](论文逐篇解读/P174.md) | 按数据监督字段组合策略、正逆动力学和视觉预测任务，学习潜在动力学并生成机器人动作块。 | [原文](https://arxiv.org/abs/2602.12215) · [代码](https://github.com/jiangranlv/LDA-1B) · [项目页](https://pku-epic.github.io/LDA/) |
| [MachEmbodied-U0：协同任务理解、未来预测与动作生成](论文逐篇解读/P233.md) | ME-U0以理解专家预测子任务和交互区域，再与生成专家联合预测未来视觉状态及机器人动作，用多模态预训练支持操作策略。 | [原文](https://arxiv.org/abs/2609.25627) · [代码](https://github.com/MachEmbodied/ME-U0) · [项目页](https://machembodied.com/ME-U/ME-U0.html) |
| [ME-Dex 1.0：让世界动作模型联合预测视觉、触觉与动作](论文逐篇解读/P234.md) | ME-Dex把异构触觉映射到统一手部表示，并用视频、触觉和动作专家联合预测未来接触与动作，扩展世界动作模型的物理反馈。 | [原文](https://arxiv.org/abs/2609.21449) · [代码](https://github.com/MachEmbodied/ME-Dex-1.0) · [项目页](https://machembodied.com/ME-Dex/ME-Dex1.0.html) |
| [MotionWAM：面向实时人形移动操作的基座世界动作模型](论文逐篇解读/P081.md) | 以双DiT联合建模未来视觉和全身动作序列，面向实时人形移动操作与长程控制。 | [原文](https://arxiv.org/abs/2606.09215) |
| [MotuBrain：联合预测未来视觉与机器人动作](论文逐篇解读/P250.md) | 用三流Transformer联合生成未来视觉与相对末端动作，经异构数据预训练和异步动作块执行完成跨本体及长程操作。 | [原文](https://arxiv.org/abs/2604.27792) · [项目页](https://www.genspi.com/en/motubrain/) |
| [Motus2：把策略、动作条件世界模型和价值评估放进一个闭环](论文逐篇解读/P197.md) | 共享策略、视觉模拟器和评估器，利用成功与失败交互支持灵巧操作候选规划和模型式学习。 | [原文](https://arxiv.org/abs/2608.30237v2) · [项目页](https://motus-robotics.github.io/motus2/) |
| [LingBot-VA 2.0：原生因果视频—动作预训练](论文逐篇解读/P256.md) | 以原生因果视频—动作预训练和高层任务规划处理跨本体机器人操作，通过异步动作块执行提升闭环响应。 | [原文](https://arxiv.org/abs/2607.08639) · [代码](https://github.com/Robbyant/lingbot-va) · [项目页](https://technology.robbyant.com/lingbot-va-v2) |
| [OpenWAM：把世界动作模型拆成可控的预训练实验](论文逐篇解读/P194.md) | 将视频骨干、动作专家、注意力和数据配方模块化，系统比较跨本体世界动作模型预训练设计。 | [原文](https://arxiv.org/abs/2609.07398) · [代码](https://github.com/OpenWAM-Official/OpenWAM) · [项目页](https://openwam-official.github.io/) |
| [TempoWAM：按任务进度调整动作块执行](论文逐篇解读/P347.md) | TempoWAM以轻量GRU监测器估计动作前缀带来的任务进度，并比较当前与所需进度速率，在线决定继续执行或提前重规划；冻结主干，在模拟基准及真实双臂任务评测效率和成功率。 | [原文](https://arxiv.org/abs/2608.09492) |
| [Riemann-1.0：在同一因果模型中学习机器人动作与未来视觉](论文逐篇解读/P177.md) | 以因果Action/Video DiT共同建模未来视觉与机器人动作，并用本体专属头执行长程操作。 | [原文](https://riemann-dynamics.github.io/Riemann-1.0-Website/paper/Riemann-1.0.pdf) · [项目页](https://riemann-dynamics.github.io/Riemann-1.0-Website/) |
| [Rolling-WAM：跨重规划周期滚动细化世界与动作预测](论文逐篇解读/P227.md) | 在滑动窗口内跨重规划周期复用视频—动作去噪状态，以滚动想象降低WAM推理延迟并保持闭环操作表现。 | [原文](https://arxiv.org/abs/2609.30247) · [代码](https://github.com/zyinghua/Rolling-WAM) · [项目页](https://rolling-wam.github.io/) |
| [SimpleWAM：面向端侧部署的时序世界动作模型](论文逐篇解读/P251.md) | 用训练期未来RGB、深度和语义监督增强表征，以早期历史融合、目标定位和进度感知动作块执行实现两步去噪的端侧机器人控制。 | [公司研究入口](https://www.simplexityrobotics.com/research) |
| [Lumo-2：对齐潜在世界动力学与机器人动作](论文逐篇解读/P328.md) | Lumo-2 通过三阶段训练将潜在世界动力学、视觉语言语义与机器人动作逐步对齐，在统一多模态Transformer中基于历史观测生成未来条件化动作块。 | [原文](https://arxiv.org/abs/2607.11270) · [项目页](https://www.astribot.com/research/Lumo2) |
| [X-WAM：异步去噪的统一四维世界动作建模](论文逐篇解读/P305.md) | 以Wan2.2视频先验联合生成多视角未来RGB、深度、状态与动作，并用轻量深度支路和异步噪声采样兼顾几何精度与动作响应速度。 | [原文](https://arxiv.org/abs/2604.26694) · [代码](https://github.com/sharinka0715/X-WAM) · [项目页](https://sharinka0715.github.io/X-WAM/) |
| [UniT：跨本体统一物理语言与世界建模](论文逐篇解读/P311.md) | 以共享RQ-VAE离散动作词汇对齐人类与机器人，通过跨重建支撑VLA动作生成和动作条件未来视频预测，并在RoboCasa、DROID及IRON人形机器人评测迁移效果。 | [原文](https://arxiv.org/abs/2604.19734) · [代码](https://github.com/xpeng-robotics/UniT) · [项目页](https://xpeng-robotics.github.io/unit/) |
| [WALL-WM：事件对齐的视频—动作世界模型](论文逐篇解读/P300.md) | 以可变时长语义事件为单位联合去噪生成多视角未来视频与末端动作，通过Wan视频塔、动作DiT、跨视角几何交互及Staircase潜在推理支持事件式和定长VLA两种执行，并在双臂真机与RoboTwin评测。 | [原文](https://arxiv.org/abs/2606.01955) · [代码](https://github.com/X-Square-Robot/wall-wm) · [项目页](https://github.com/X-Square-Robot/WALL-X) |
| [WAM-TTT：用无标注人类视频在部署前调整世界动作模型](论文逐篇解读/P173.md) | 通过观看无标注人类视频更新轻量快速记忆，条件化冻结世界动作模型执行跨本体操作。 | [原文](https://arxiv.org/abs/2607.06988) |
| [WholeBodyWAM：以统一全身控制语义扩展世界动作模型](论文逐篇解读/P226.md) | 保留预训练WAM视觉—操作先验，以56维统一全身控制语义和可操作性门控协调不同人形全身控制器。 | [原文](https://arxiv.org/abs/2609.16644) · [项目页](https://wholebodywam.github.io/) |
| [DreamZero：作为零样本策略的世界动作模型](论文逐篇解读/P113.md) | 联合自回归生成未来视觉与机器人动作，并以新观测滚动校正，用作零样本操作策略。 | [原文](https://arxiv.org/abs/2602.15922) · [代码](https://github.com/dreamzero0/dreamzero) · [项目页](https://dreamzero0.github.io/) |
| [World-Action Models 综述：从预测世界到生成可执行动作](论文逐篇解读/P211.md) | 从表示、转移建模、动作接口、架构、训练、数据和规模化整理机器人世界动作模型研究。 | [原文](https://arxiv.org/abs/2609.16074) · [项目页](https://rcl-robotics.github.io/Awesome-World-Action-Models/) |
| [Zero-WAM：让人类视频成为未见任务的上下文指令](论文逐篇解读/P186.md) | 把人类示范视频作为上下文任务条件，联合预测机器人未来视觉与动作而不更新模型参数。 | [原文](https://arxiv.org/abs/2608.26103) · [项目页](https://robbyant-research.github.io/Zero-WAM/) |
| [ZimaBlue：让大规模无动作视频进入可部署的WAM](论文逐篇解读/P196.md) | 以因果视频预训练、视频动作中训练和目标机器人后训练，把第一视角视频用于通用操作策略。 | [原文](https://arxiv.org/abs/2609.00188) · [项目页](https://github.com/ZimaBlue-WAM/ZimaBlue) |
| [ω-0：以潜在未来表征驱动人形全身移动操作](论文逐篇解读/P327.md) | ω-0 以任务语言、视觉和本体状态为条件，联合预测动作潜变量及未来观测嵌入，输出 SONIC 兼容的全身动作块用于人形机器人同步移动与操作。 | [原文](https://arxiv.org/abs/2608.06375) · [代码](https://github.com/gentlefress/Omega-0) · [项目页](https://gentlefress.github.io/OMEGA-0_page/) |
| [Motus：以视觉运动潜变量统一世界模型与机器人动作](论文逐篇解读/P294.md) | 以MoT专家和统一扩散调度共同建模VLA、世界预测、逆动力学与视频生成，并从互联网/人类视频光流压缩潜动作以预训练跨本体运动先验。 | [原文](https://arxiv.org/abs/2512.13030) · [代码](https://github.com/thu-ml/Motus) |
| [RynnVLA-002：统一视觉语言动作与世界模型](论文逐篇解读/P273.md) | 共享自回归多模态主干分别支持任务条件动作块生成与图像—动作条件下一帧预测，并用连续Action Transformer改善真机轨迹平滑度。 | [原文](https://arxiv.org/abs/2511.17502) · [代码](https://github.com/alibaba-damo-academy/RynnVLA-002) |
| [UWM：耦合视频与动作扩散的统一世界模型](论文逐篇解读/P319.md) | 联合扩散动作块和未来观察，支持动作条件预测、策略与视频-only预训练；在LIBERO和Franka真机任务验证。 | [原文](https://arxiv.org/abs/2504.02792) · [代码](https://github.com/WEIRDLabUW/unified-world-model) · [项目页](https://weirdlabuw.github.io/uwm/) |

#### 相关项目

| 项目 | 主要用途 | 功能与特点 |
| --- | --- | --- |
| [ABot-Manipulation](https://github.com/amap-cvlab/ABot-Manipulation) | 世界动作模型（WAM） | 以未来视频潜变量、帧级视觉latent action、移动/操作可执行动作构成三级WAM级联；双层MoT解耦模态与异构动作，Dream Forcing使用模型自生成未来训练逆动力学。 |
| [AR-WAM](https://arxiv.org/abs/2609.23578) | 世界动作模型（WAM） | AR-WAM以目标框和原子操作token取代策略端自然语言，联合输出可监督的目标理解、压缩未来场景latent与动作块；Agent通过detect/execute/query接口提供高层指令并管理长程记忆。 |
| [Being-H0.7](https://research.beingbeyond.com/being-h07) | 潜变量世界动作模型 | 通过训练期未来观测后验与当前上下文先验的潜在表示对齐，学习未来感知动作推理；部署时先验分支直接生成动作块，支持多本体操作。 |
| [Cosmos Policy](https://github.com/NVlabs/cosmos-policy) | 视频模型机器人策略后训练 | 将Cosmos视频生成主干后训练为 visuomotor policy，并扩展未来观测和值预测以支持候选动作规划。 |
| [DIAL](https://github.com/xpeng-robotics/DIAL) | 世界动作模型（WAM） | System-2以VLM query预测未来ViT视觉latent，System-1以当前-未来latent差异和本体状态驱动DiT flow matching生成动作，并经warmup后端到端联合优化。 |
| [DiT4DiT](https://github.com/Mondo-Robotics/DiT4DiT) | 世界动作模型（WAM） | 联合flow matching生成未来视频latent与机器人动作，并抽取视频DiT去噪中间特征条件化动作DiT，在LIBERO、RoboCasa-GR1和Unitree G1评测空间操作及分布变化泛化。 |
| [DreamZero](https://github.com/dreamzero0/dreamzero) | 世界动作模型项目 | 联合预测未来视觉和机器人动作，结合DROID与AgiBot数据进行训练和后训练，并通过WebSocket服务执行推理。 |
| [DualWAM](https://steveouo.github.io/DualWAM-Web/) | 世界动作模型（WAM） | DualWAM用高噪声System 2异步生成长时程全局世界动作计划，并让低噪声腕部System 1基于新观测精修时间对齐局部视频与动作窗口，在真实双本体任务上评测成功率和时延。 |
| [Dyna-2](https://www.dyna.co/dyna-2) | 世界动作模型（WAM） | 以百万小时第一视角人类视频共同训练未来视频与动作预测，研究数据规模对跨本体迁移的影响；动作策略经机器人示范后训练执行双臂、灵巧手和半人形操作。 |
| [Fast-WAM](https://github.com/yuantianyuan01/FastWAM) | 视频先验迁移的动作模型训练 | 训练时联合视频与动作，推理时直接输出动作块；提供数据准备、训练脚本、模型及LIBERO和RoboTwin评测。 |
| [Flex-π](https://github.com/geyan21/flex-pi) | 支持多种观测组合的操作策略 | 组合RGB、几何和语义观测，通过冻结视频编码器与模态训练策略生成动作，提供训练、评测和部署实现。 |
| [GigaWorld-Policy](https://github.com/open-gigaai/giga-world-policy) | 世界动作模型（WAM） | GigaWorld-Policy-0.5在训练期以动作块和动作条件未来视觉联合学习WAM，在推理期仅解码动作；MoT拆分视觉专家和轻量动作专家，配合KV缓存、编译运行时与AutoResearch优化延迟和训练配置。 |
| [Kairos](https://github.com/DAXIAORobotics/kairos) | 世界动作模型（WAM） | 以控制充分状态统一VLM理解、未来视频生成和动作轨迹预测，并用局部/中程/全局混合时间记忆与分阶段人类、机器人数据训练世界动作策略。 |
| [LDA-1B](https://github.com/jiangranlv/LDA-1B) | 世界动作模型官方实现 | 以多模态扩散Transformer联合建模动作块与未来视觉潜变量，用于动作生成和视觉预测评测。 |
| [LingBot-VA 1.0](https://github.com/Robbyant/lingbot-va) | 视频与动作联合世界模型 | 视频潜变量流与机器人动作流在双流Transformer中交替建模，模型既预测动作也预测动作条件下的未来画面；仓库开放权重、RoboTwin与LIBERO后训练数据、训练和推理脚本，可检查世界预测怎样与策略输出共享表示但保持独立输出。 |
| [LingBot-VA 2.0](https://technology.robbyant.com/lingbot-va-v2) | 视频—动作机器人控制模型 | 以原生因果视频—动作预训练和高层任务规划处理跨本体机器人操作，通过异步动作块执行提升闭环响应。 |
| [Lumo-2](https://www.astribot.com/research/Lumo2) | 世界动作模型（WAM） | Lumo-2 通过三阶段训练将潜在世界动力学、视觉语言语义与机器人动作逐步对齐，在统一多模态Transformer中基于历史观测生成未来条件化动作块。 |
| [MachEmbodied-U0 (ME-U0)](https://github.com/MachEmbodied/ME-U0) | 世界动作模型（WAM） | ME-U0以理解专家预测子任务和交互区域，再与生成专家联合预测未来视觉状态及机器人动作，用多模态预训练支持操作策略。 |
| [ME-Dex 1.0](https://github.com/MachEmbodied/ME-Dex-1.0) | 世界动作模型（WAM） | ME-Dex把异构触觉映射到统一手部表示，并用视频、触觉和动作专家联合预测未来接触与动作，扩展世界动作模型的物理反馈。 |
| [MotuBrain](https://github.com/shengshu-ai/MotuBrain) | 面向真实机器人的世界动作模型技术报告 | 以视频、动作和语言联合建模，面向多本体适配、长程机器人任务与实时闭环控制。 |
| [Motus](https://github.com/thu-ml/Motus) | 世界动作模型（WAM） | 以MoT专家和统一扩散调度共同建模VLA、世界预测、逆动力学与视频生成，并从互联网/人类视频光流压缩潜动作以预训练跨本体运动先验。 |
| [OpenDW](https://github.com/dexmal/opendw) | 世界动作模型（WAM） | 以图像、语言、机器人状态和动作联合预测未来视频、动作与价值，用于动作条件回放和策略评估。 |
| [OpenWAM](https://github.com/OpenWAM-Official/OpenWAM) | 可配置的世界动作模型训练框架 | 以共享配置比较视觉编码、动作表示、注意力掩码和联合预测任务，提供世界动作模型训练、微调与部署入口。 |
| [Riemann-1.0](https://riemann-dynamics.github.io/Riemann-1.0-Website/) | 机器人世界动作模型技术报告与演示 | 在策略模式下由视觉和本体状态生成动作，在模拟模式下预测动作条件未来视觉，逐阶段对齐视频与机器人数据。 |
| [Rolling-WAM](https://github.com/zyinghua/Rolling-WAM) | 世界动作模型（WAM） | 在滑动窗口内跨重规划周期复用视频—动作去噪状态，以滚动想象降低WAM推理延迟并保持闭环操作表现。 |
| [RynnVLA-002](https://github.com/alibaba-damo-academy/RynnVLA-002) | 世界动作模型（WAM） | 共享自回归多模态主干分别支持任务条件动作块生成与图像—动作条件下一帧预测，并用连续Action Transformer改善真机轨迹平滑度。 |
| [SimpleWAM](https://www.simplexityrobotics.com/research) | 世界动作模型（WAM） | 用训练期未来RGB、深度和语义监督增强表征，以早期历史融合、目标定位和进度感知动作块执行实现两步去噪的端侧机器人控制。 |
| [TempoWAM](https://arxiv.org/abs/2608.09492) | 世界动作模型（WAM） | TempoWAM以轻量GRU监测器估计动作前缀带来的任务进度，并比较当前与所需进度速率，在线决定继续执行或提前重规划；冻结主干，在模拟基准及真实双臂任务评测效率和成功率。 |
| [Unified World Models (UWM)](https://github.com/WEIRDLabUW/unified-world-model) | 动作条件世界建模与机器人策略预训练 | 在同一扩散模型中学习动作块及其未来视觉后果，为策略、前向动力学、逆动力学和视频-only训练提供接口。 |
| [UnifoLM-WMA-0](https://github.com/unitreerobotics/unifolm-world-model-action) | 宇树世界模型与动作框架 | 联合预测未来状态与动作序列，连接数据处理、训练、推理流程并适配G1部署。 |
| [UniT](https://github.com/xpeng-robotics/UniT) | 世界动作模型（WAM） | 以共享RQ-VAE离散动作词汇对齐人类与机器人，通过跨重建支撑VLA动作生成和动作条件未来视频预测，并在RoboCasa、DROID及IRON人形机器人评测迁移效果。 |
| [WALL-WM](https://github.com/X-Square-Robot/WALL-WM) | 世界动作模型（WAM） | 以可变时长语义事件为单位联合去噪生成多视角未来视频与末端动作，通过Wan视频塔、动作DiT、跨视角几何交互及Staircase潜在推理支持事件式和定长VLA两种执行，并在双臂真机与RoboTwin评测。 |
| [WholeBodyWAM](https://wholebodywam.github.io/) | 世界动作模型（WAM） | 保留预训练WAM视觉—操作先验，以56维统一全身控制语义和可操作性门控协调不同人形全身控制器。 |
| [X-WAM](https://github.com/sharinka0715/X-WAM) | 世界动作模型（WAM） | 以Wan2.2视频先验联合生成多视角未来RGB、深度、状态与动作，并用轻量深度支路和异步噪声采样兼顾几何精度与动作响应速度。 |
| [Zero-WAM](https://github.com/robbyant-research/Zero-WAM) | 世界动作模型项目页 | 以人类示范视频作为上下文任务指令，联合建模未来视觉与机器人动作，并通过人机配对数据迁移到未见操作任务。 |
| [ω-0](https://github.com/gentlefress/Omega-0) | 世界动作模型（WAM） | ω-0 以任务语言、视觉和本体状态为条件，联合预测动作潜变量及未来观测嵌入，输出 SONIC 兼容的全身动作块用于人形机器人同步移动与操作。 |

[返回本页导航](#本页导航)

## 仿真生成与数据引擎

生成、编辑或扩增交互视频、场景与训练轨迹，连接动作恢复、数据合成和虚拟评测环境。

**7** 篇论文／报告 · **7** 个项目

#### 论文与技术报告

| 论文／报告 | 主要方法与用途 | 原文／代码 |
| --- | --- | --- |
| [Matrix-Game 3.5：用三维Patch记忆维持长时交互视频的一致性](论文逐篇解读/P178.md) | 以三维回投历史Patch和参考Token维持相机可控视频生成中的场景记忆与动态主体。 | [原文](https://matrix-game-v3-5.github.io/paper/Matrix-Game-3.5.pdf) · [代码](https://github.com/Riemann-Dynamics/Matrix-Game-3.5) · [项目页](https://matrix-game-v3-5.github.io/) |
| [LingBot-Video：以稀疏专家视频预训练承载具身物理先验](论文逐篇解读/P267.md) | LingBot-Video以文字、图像和视频条件生成图像或视频，通过稀疏MoE扩展单流扩散骨干、具身视频剖析与多阶段训练构建面向机器人数据扩增的生成基础模型；另以GR-1轨迹后训练动作条件A2V分支预测未来视频。 | [原文](https://arxiv.org/abs/2607.07675) · [代码](https://github.com/Robbyant/lingbot-video) · [项目页](https://technology.robbyant.com/lingbot-video) |
| [TableVerse：从真实桌面图像生成可操作仿真数据](论文逐篇解读/P323.md) | TableVerse从真实单视图桌面照片重建带米制尺度、碰撞校正和物理稳定性的MuJoCo场景，再按语言任务生成无碰撞抓取放置轨迹，构成TableVerse-100K仿真训练数据。 | [原文](https://arxiv.org/abs/2607.21017) · [代码](https://github.com/bytedance/TableVerse) · [项目页](https://bytedance.github.io/TableVerse/) |
| [Uranus：动作条件自回归机器人视频仿真](论文逐篇解读/P348.md) | Uranus接收相机参考帧、标定和在线未来关节位置，以因果自回归扩散生成多视角RGB后果；使用逾3382小时真实机器人轨迹训练，并评估WorldOlympiad、真实轨迹一致性和闭环策略排序。 | [原文](https://arxiv.org/abs/2609.24815) · [代码](https://github.com/D-Robotics-AI-Lab/Uranus-OSS) · [项目页](https://d-robotics-ai-lab.github.io/large-model-team/blog/uranus/) |
| [Xiaomi-Robotics-U0：统一具身合成世界模型与数据引擎](论文逐篇解读/P288.md) | 以动作渲染机器人掩码、场景文本和观察为条件合成具身场景及未来交互视频，并生成跨视角数据扩充专家演示；模型输出视觉内容供下游策略训练。 | [原文](https://arxiv.org/abs/2607.11643) · [代码](https://github.com/XiaomiRobotics/Xiaomi-Robotics-U0) · [项目页](https://robotics.xiaomi.com/xiaomi-robotics-u0.html) |
| [GigaWorld-0：作为具身智能数据引擎的世界模型](论文逐篇解读/P115.md) | 结合视频生成、三维场景、视角迁移和物理验证，构建具身合成轨迹及VLA训练数据。 | [原文](https://arxiv.org/abs/2511.19861) · [代码](https://github.com/open-gigaai/giga-world-0) · [项目页](https://giga-world-0.github.io/) |
| [GR00T-Dreams：面向人形机器人学习的合成轨迹生成](论文逐篇解读/P068.md) | 生成任务变化与未来视觉，再用逆动力学补充动作并经仿真或策略筛选人形合成轨迹。 | [原文](https://developer.nvidia.com/blog/enhance-robot-learning-with-synthetic-trajectory-data-generated-by-world-foundation-models/) |

#### 相关项目

| 项目 | 主要用途 | 功能与特点 |
| --- | --- | --- |
| [GigaWorld-0](https://github.com/open-gigaai/giga-world-0) | 合成数据引擎项目 | 结合视频生成、三维高斯场景、系统辨识和规划模块，构建用于VLA训练的数据生成引擎。 |
| [LingBot-Video](https://github.com/Robbyant/lingbot-video) | 仿真生成与数据引擎 | LingBot-Video以文字、图像和视频条件生成图像或视频，通过稀疏MoE扩展单流扩散骨干、具身视频剖析与多阶段训练构建面向机器人数据扩增的生成基础模型；另以GR-1轨迹后训练动作条件A2V分支预测未来视频。 |
| [Matrix-Game 3.5](https://github.com/Riemann-Dynamics/Matrix-Game-3.5) | 相机可控长时交互视频世界模型 | 根据文本、初始画面、主体参考图和相机轨迹生成长时交互视频，结合场景记忆与渐进蒸馏。 |
| [RoboTransfer](https://github.com/HorizonRobotics/RoboTransfer) | 世界模型与仿真生成 | 以当前观测和动作条件生成未来状态、视频或交互结果，为策略训练、评测和规划提供数据。 |
| [TableVerse](https://github.com/bytedance/TableVerse) | 仿真生成与数据引擎 | TableVerse从真实单视图桌面照片重建带米制尺度、碰撞校正和物理稳定性的MuJoCo场景，再按语言任务生成无碰撞抓取放置轨迹，构成TableVerse-100K仿真训练数据。 |
| [Uranus](https://github.com/D-Robotics-AI-Lab/Uranus-OSS) | 仿真生成与数据引擎 | Uranus接收相机参考帧、标定和在线未来关节位置，以因果自回归扩散生成多视角RGB后果；使用逾3382小时真实机器人轨迹训练，并评估WorldOlympiad、真实轨迹一致性和闭环策略排序。 |
| [Xiaomi-Robotics-U0](https://github.com/XiaomiRobotics/Xiaomi-Robotics-U0) | 仿真生成与数据引擎 | 以动作渲染机器人掩码、场景文本和观察为条件合成具身场景及未来交互视频，并生成跨视角数据扩充专家演示；模型输出视觉内容供下游策略训练。 |

[返回本页导航](#本页导航)

## 具身理解与Agent规划

理解场景与任务，组织空间记忆、任务分解、技能调用和导航决策。

**19** 篇论文／报告 · **26** 个项目

#### 论文与技术报告

| 论文／报告 | 主要方法与用途 | 原文／代码 |
| --- | --- | --- |
| [ASENA：通过可复用程序与技能积累导航经验的具身Agent](论文逐篇解读/P373.md) | 编码Agent从执行记录中修订笔记和程序技能，固定模型权重下重复任务表现提升；可选4B单目导航器输出机体航点，并在受监督G1任务中支持无预建地图的搜索与交互。 | [原文](https://arxiv.org/abs/2609.39207) · [项目页](https://asena-bot.github.io/) |
| [BrickCraft-Duo：双臂积木组装的技能学习与长程组合](论文逐篇解读/P354.md) | BrickCraft-Duo先用装配约束组织长程积木任务，再学习可复用单臂与双臂扩散技能，并通过双臂对称映射共享示范。系统把技能组合用于最多九步的真实装配，并以人在回路的针对性修正提高困难结构完成率。 | [原文](https://arxiv.org/abs/2609.28281) · [项目页](https://jichuan-yu.github.io/BrickCraft-Duo/) |
| [HoloAgent-0：具备三维空间记忆的统一具身智能体框架](论文逐篇解读/P082.md) | 以三维空间记忆、技能图和运行监控组织搜索、导航与移动操作，不直接控制关节。 | [原文](https://arxiv.org/abs/2606.23565) · [代码](https://github.com/HorizonRobotics/HoloAgent) · [项目页](https://horizonrobotics.github.io/robot_lab/holoagent) |
| [HY-Embodied-0.5：面向具身任务的空间理解底座](论文逐篇解读/P289.md) | 以模态自适应MoT及视觉潜变量token构建空间感知VLM，训练覆盖定位、深度、分割和具身推理，并在扩展Action Expert的下游版本上验证双臂真机操作。 | [原文](https://arxiv.org/abs/2604.07430) · [代码](https://github.com/Tencent-Hunyuan/HY-Embodied) |
| [Hy-Embodied-VLM-1.0：面向物理环境任务的视觉语言Agent](论文逐篇解读/P290.md) | 沿用HY-Embodied VLM骨干并按状态理解、状态转移、序列自适应推理组织监督，以可验证推理后训练驱动视觉语言导航和仿真Agent决策。 | [原文](https://arxiv.org/abs/2607.12894) · [代码](https://github.com/Tencent-Hunyuan/HY-Embodied) |
| [LT-Mem：为反复访问的场景保存对象状态与变化历史](论文逐篇解读/P375.md) | 将多次单目观察对齐到统一三维场景，以对象身份和变化频率维护当前状态、事件历史与统计记忆，支持物品移动、出现和消失等时序场景问答。 | [原文](https://arxiv.org/abs/2608.19059) · [项目页](https://lt-mem.github.io/) |
| [ME-Brain 1.0：用记忆、认知与动作积累可复用经验](论文逐篇解读/P231.md) | ME-Brain把机器人执行记录整理为分层记忆，由认知核心抽取可迁移技能，并让动作模型按事件检索经验完成后续操作。 | [原文](https://arxiv.org/abs/2609.24271) · [代码](https://github.com/MachEmbodied/ME-Brain-1.0) · [项目页](https://machembodied.com/ME-Brain/ME-Brain-1.0.html) |
| [ME-VLM：统一具身认知与多模态Agent协作](论文逐篇解读/P232.md) | ME-VLM把物理场景理解、空间与时序推理、Agent任务规划和执行结果检查统一训练，并提供适配端侧部署的4B版本。 | [原文](https://arxiv.org/abs/2609.24526) · [代码](https://github.com/MachEmbodied/ME-VLM) · [项目页](https://machembodied.com/ME-Brain/ME-VLM.html) |
| [Counterfactual Memory Audit：反事实检验历史是否引导决策](论文逐篇解读/P350.md) | CMA把不同任务历史配对到相同当前输入，用同随机数查询冻结策略并将保存动作交叉放入两种评估世界，分别统计记忆敏感性、正确分支、匹配世界价值和配对可靠性。 | [原文](https://arxiv.org/abs/2609.27247) |
| [NavProbe：基于主动记忆检索的证据约束零样本导航](论文逐篇解读/P360.md) | NavProbe以动态子目标议程、拓扑情景记忆和实体索引管理导航历史，在推理缺少证据时按需检索图像或几何记录，核实后修订议程并输出航点、垂直移动、回退或停止技能。论文在R2R-CE、RxR-CE、HM3D-v2上报告仿真结果，并展示Galaxea R1Pro实机部署流程。 | [原文](https://arxiv.org/abs/2609.27526) |
| [iFlax：面向长程任务的规划反馈式对象重要性学习](论文逐篇解读/P380.md) | 以PDDL任务关系图预测对象重要性，令规划器在逐步扩张的裁剪空间中搜索，并用所得计划生成训练伪标签；3R并行恢复补回关键对象、重建精简集合或谨慎回退扩张，输出高层计划并在Spot上调用技能执行。 | [原文](https://arxiv.org/abs/2606.06877) · [项目页](https://sairlab.org/iflax/) |
| [RoboAssist：长程手术辅助中的人形机器人交互规划](论文逐篇解读/P371.md) | 把人的部分可观测流程与机器人技能任务分轨维护，以证据门控和仅重规划受影响后缀应对请求变化，并用导航、交接与运行时监督三层机制约束G1执行；实验为非临床模拟手术辅助流程。 | [原文](https://arxiv.org/abs/2609.39384) · [项目页](https://roboassist.github.io/) |
| [VAP-TAMP：以主动视觉核验恢复动态环境中的机器人任务执行](论文逐篇解读/P381.md) | 从RGB-D和语言目标构建动态场景图及PDDL问题，以动作前提和效果组成VLM谓词核验；问法分歧或视野不足时主动换视角，确认状态偏差后更新场景图并重规划，输出由参数化运动技能执行的任务计划。 | [原文](https://arxiv.org/abs/2604.26988) · [代码](https://github.com/aoloo-r/VAP-TAMP) · [项目页](https://vap-tamp.github.io/vap-tamp/) |
| [RxBrain：联合语言推理与视觉想象的具身认知模型](论文逐篇解读/P292.md) | 以交错语言推理和图像子目标表达具身计划，通过视频状态预测、联合子目标想象与自动任务视频标注训练认知模型，并扩展连续动作头完成真机操作。 | [原文](https://arxiv.org/abs/2607.14187) · [代码](https://github.com/Tencent-Hunyuan/Hy-Embodied-RxBrain-1.0) · [项目页](https://huggingface.co/tencent/Hy-Embodied-RxBrain-1.0) |
| [RynnBrain：面向具身任务的时空基础模型](论文逐篇解读/P274.md) | 以Qwen3-VL为底座进行时空具身预训练，再分别后训练CoP空间推理、Nav导航、Plan高层规划与VLA动作策略分支。 | [原文](https://arxiv.org/abs/2602.14979v1) · [代码](https://github.com/alibaba-damo-academy/RynnBrain) · [项目页](https://alibaba-damo-academy.github.io/RynnBrain.github.io) |
| [RynnValue：以时间距离学习机器人任务价值](论文逐篇解读/P282.md) | 以任务语言、本体元数据和多帧观察估计逐帧剩余完成时间及相邻帧有符号时间位移，并辅助输出任务描述/匹配/成功判断；将时间距离势函数接入在线离线RL、价值筛选和冻结策略候选动作重排。 | [原文](https://arxiv.org/abs/2608.09853) · [代码](https://github.com/alibaba-damo-academy/RynnValue) · [项目页](https://alibaba-damo-academy.github.io/RynnValue.github.io) |
| [Show-Harness：用语义动作接口让 VLM 闭环操作机械臂](论文逐篇解读/P210.md) | 以离散语义动作连接视觉语言模型和本体专用解释器，执行跨任务机械臂抓取放置。 | [原文](https://arxiv.org/abs/2609.10522) · [代码](https://github.com/showlab/Show-Harness) · [项目页](https://showlab.github.io/Show-Harness/) |
| [RynnEC：面向具身视频的区域认知模型](论文逐篇解读/P278.md) | 以视频区域编码器和SAM2掩码解码器增强具身视频认知，输入第一人称视频、问题及可选区域提示，输出物体/空间文字答案或跨帧实例掩码，并以四阶段训练整合对象、空间与指代分割能力。 | [原文](https://arxiv.org/abs/2508.14160) · [代码](https://github.com/alibaba-damo-academy/RynnEC) |
| [PaLM-E：具身多模态语言模型](论文逐篇解读/P053.md) | 将视觉与机器人状态嵌入语言模型上下文，用于具身规划、操作和导航，输出仍为语言层。 | [原文](https://arxiv.org/abs/2303.03378) · [项目页](https://palm-e.github.io/) |

#### 相关项目

| 项目 | 主要用途 | 功能与特点 |
| --- | --- | --- |
| [ASENA](https://asena-bot.github.io/) | 具身理解与Agent规划 | 编码Agent从执行记录中修订笔记和程序技能，固定模型权重下重复任务表现提升；可选4B单目导航器输出机体航点，并在受监督G1任务中支持无预建地图的搜索与交互。 |
| [Being-VL-0.5](https://github.com/BeingBeyond/Being-VL-0.5) | 视觉语言理解模型 | 以视觉字节对编码（vBPE）合并重复视觉Token，并与文本Token统一建模，用于图文问答和多模态理解。 |
| [BrickCraft-Duo](https://jichuan-yu.github.io/BrickCraft-Duo/) | 具身理解与Agent规划 | BrickCraft-Duo先用装配约束组织长程积木任务，再学习可复用单臂与双臂扩散技能，并通过双臂对称映射共享示范。系统把技能组合用于最多九步的真实装配，并以人在回路的针对性修正提高困难结构完成率。 |
| [Counterfactual Memory Audit](https://arxiv.org/abs/2609.27247) | 具身理解与Agent规划 | CMA把不同任务历史配对到相同当前输入，用同随机数查询冻结策略并将保存动作交叉放入两种评估世界，分别统计记忆敏感性、正确分支、匹配世界价值和配对可靠性。 |
| [embodied-skill-kit](https://github.com/Open-X-Humanoid/embodied-skill-kit) | 机器人Agent与任务规划 | 根据语言任务与多模态环境状态生成技能调用或导航操作步骤，并结合执行反馈调整任务计划。 |
| [Fast-in-Slow](https://github.com/CHEN-H01/Fast-in-Slow) | VLA与机器人策略 | 以慢速系统规划任务并由快速策略执行操作，研究长时决策与实时动作的分层接口。 |
| [genisom_vln](https://github.com/zsibot/genisom_vln) | 机器人Agent与任务规划 | 根据语言任务与多模态环境状态生成技能调用或导航操作步骤，并结合执行反馈调整任务计划。 |
| [GO-2](https://www.agibot.com/article/231/detail/56.html) | 具身规划与执行模型 | 以Action CoT生成宏观动作意图，再由低频语义规划和高频动作跟随器逐级细化执行。 |
| [HoloAgent](https://github.com/HorizonRobotics/HoloAgent) | 具身Agent与机器人系统栈 | 以AgentOS技能图、空间记忆和执行反馈组织机器人任务，并通过ROS 2连接导航、感知节点及多本体适配工具。 |
| [HY-Embodied](https://github.com/Tencent-Hunyuan/HY-Embodied) | 具身理解与Agent规划 | 沿用HY-Embodied VLM骨干并按状态理解、状态转移、序列自适应推理组织监督，以可验证推理后训练驱动视觉语言导航和仿真Agent决策。 |
| [iFlax](https://sairlab.org/iflax/) | 具身理解与Agent规划 | 以PDDL任务关系图预测对象重要性，令规划器在逐步扩张的裁剪空间中搜索，并用所得计划生成训练伪标签；3R并行恢复补回关键对象、重建精简集合或谨慎回退扩张，输出高层计划并在Spot上调用技能执行。 |
| [LT-Mem](https://lt-mem.github.io/) | 具身理解与Agent规划 | 将多次单目观察对齐到统一三维场景，以对象身份和变化频率维护当前状态、事件历史与统计记忆，支持物品移动、出现和消失等时序场景问答。 |
| [ME-Brain 1.0](https://github.com/MachEmbodied/ME-Brain-1.0) | 具身理解与Agent规划 | ME-Brain把机器人执行记录整理为分层记忆，由认知核心抽取可迁移技能，并让动作模型按事件检索经验完成后续操作。 |
| [ME-VLM](https://github.com/MachEmbodied/ME-VLM) | 具身理解与Agent规划 | ME-VLM把物理场景理解、空间与时序推理、Agent任务规划和执行结果检查统一训练，并提供适配端侧部署的4B版本。 |
| [MiniCPM-Robot](https://github.com/OpenBMB/MiniCPM-Robot) | 端侧机器人感知与决策工具集 | 提供端侧多模态模型的视觉跟踪、目标理解和动作决策接口，支持Jetson、ROS 2及机器人SDK集成。 |
| [NavProbe](https://arxiv.org/abs/2609.27526) | 具身理解与Agent规划 | NavProbe以动态子目标议程、拓扑情景记忆和实体索引管理导航历史，在推理缺少证据时按需检索图像或几何记录，核实后修订议程并输出航点、垂直移动、回退或停止技能。论文在R2R-CE、RxR-CE、HM3D-v2上报告仿真结果，并展示Galaxea R1Pro实机部署流程。 |
| [OpenLoong-Brain](https://github.com/loongOpen/OpenLoong-Brain) | 任务规划与技能系统 | 将人形任务指令映射到可执行技能和机器人接口，提供技能调度、调用与执行框架。 |
| [Pelican-VL](https://github.com/Open-X-Humanoid/pelican-vl) | 人形机器人多模态具身大脑 | 从视觉语言输入形成空间理解、任务推理和高层动作目标，为下层策略或运动控制提供计划。 |
| [RoboAssist](https://roboassist.github.io/) | 具身理解与Agent规划 | 把人的部分可观测流程与机器人技能任务分轨维护，以证据门控和仅重规划受影响后缀应对请求变化，并用导航、交接与运行时监督三层机制约束G1执行；实验为非临床模拟手术辅助流程。 |
| [robocup_demo](https://github.com/BoosterRobotics/robocup_demo) | 机器人Agent与任务规划 | 根据语言任务与多模态环境状态生成技能调用或导航操作步骤，并结合执行反馈调整任务计划。 |
| [RxBrain-1.0](https://github.com/Tencent-Hunyuan/Hy-Embodied-RxBrain-1.0) | 具身理解与Agent规划 | 以交错语言推理和图像子目标表达具身计划，通过视频状态预测、联合子目标想象与自动任务视频标注训练认知模型，并扩展连续动作头完成真机操作。 |
| [RynnEC](https://github.com/alibaba-damo-academy/RynnEC) | 具身理解与Agent规划 | 以视频区域编码器和SAM2掩码解码器增强具身视频认知，输入第一人称视频、问题及可选区域提示，输出物体/空间文字答案或跨帧实例掩码，并以四阶段训练整合对象、空间与指代分割能力。 |
| [RynnValue](https://github.com/alibaba-damo-academy/RynnValue) | 具身理解与Agent规划 | 以任务语言、本体元数据和多帧观察估计逐帧剩余完成时间及相邻帧有符号时间位移，并辅助输出任务描述/匹配/成功判断；将时间距离势函数接入在线离线RL、价值筛选和冻结策略候选动作重排。 |
| [tron1-agent](https://github.com/limxdynamics/tron1-agent) | 机器人Agent与任务规划 | 根据语言任务与多模态环境状态生成技能调用或导航操作步骤，并结合执行反馈调整任务计划。 |
| [UrbanVLA](https://github.com/GalaxyGeneralRobotics/UrbanVLA) | 城市开放环境视觉语言导航模型 | 根据第一视角视觉与语言指令生成移动决策，面向室外及半开放城市环境导航。 |
| [VAP-TAMP](https://github.com/aoloo-r/VAP-TAMP) | 具身理解与Agent规划 | 从RGB-D和语言目标构建动态场景图及PDDL问题，以动作前提和效果组成VLM谓词核验；问法分歧或视野不足时主动换视角，确认状态偏差后更新场景图并重规划，输出由参数化运动技能执行的任务计划。 |

[返回本页导航](#本页导航)

## 训练、部署与评测工具

综合训练平台、本体适配、推理部署、数据处理与模型评测工具。

**9** 篇论文／报告 · **21** 个项目

#### 论文与技术报告

| 论文／报告 | 主要方法与用途 | 原文／代码 |
| --- | --- | --- |
| [FluxVLA Engine：把策略实验接到真机闭环的工程平台](论文逐篇解读/P212.md) | 以配置化流程统一数据、模型、仿真评测、推理优化和机器人部署接口，支撑具身策略流程。 | [原文](https://arxiv.org/abs/2609.17210) · [代码](https://github.com/FluxVLA/FluxVLA) |
| [FoldQuantVLA：一致折叠驱动的视觉语言动作模型原生低比特量化](论文逐篇解读/P357.md) | FoldQuantVLA在无需策略再训练的后训练量化中，为共享激活位置固定一致变换坐标，将其逆变换折叠进各消费者权重，并在原生整数路径执行W4A4；对语言主干敏感输出投影可采用选择性W8A8。Orin实机评估显示四项任务合计成功率为92.5%，均匀W4A4为80.0%。 | [原文](https://arxiv.org/abs/2609.24433) · [代码](https://github.com/cair-vinuni/FoldQuantVLA) · [项目页](https://review-artifact-27f4.github.io/foldquantvla/) |
| [GAUGE：用真实测量诊断仿真与视频世界模型](论文逐篇解读/P320.md) | GAUGE以22类真实运动捕捉实验、校准物理参数和重复试验误差为共同参照，分别比较数值物理引擎的轨迹保真度与视频世界模型的物理定律拟合、参数准确度。 | [原文](https://arxiv.org/abs/2608.05948) · [代码](https://github.com/InternRobotics/GAUGE) · [项目页](https://internrobotics.github.io/GAUGE/) |
| [HIL-UMI：在UMI示教流上进行人机协同VLA后训练](论文逐篇解读/P352.md) | HIL-UMI在UMI人类演示流中并行比较π0.5动作分布并采集策略盲区，另以低优势进度片段修正价值估计，再用混合历史/新增数据做优势条件克隆。 | [原文](https://arxiv.org/abs/2609.20659) · [项目页](https://hil-umi.github.io/) |
| [Action-JND：按动作可容忍扰动压缩视觉语言动作模型 Token](论文逐篇解读/P358.md) | Action-JND训练轻量逐Token容忍度估计器，预测视觉特征扰动在多大程度内仍能维持VLA动作响应；推理时将容忍度分数用于时序KV复用或直接剪枝。LIBERO上的OpenVLA实验在87.5%剪枝时报告42.00%平均成功率与30.16 ms延迟。 | [原文](https://arxiv.org/abs/2608.21247) |
| [RTR：潜空间高频连续动作块与异步执行连续性](论文逐篇解读/P312.md) | 以连续VAE压缩60Hz高频动作块，并用Reuse-then-Refine重整异步推理后的拼接轨迹，改善xArm接触操作的动作平滑性、块间连续和执行时长。 | [原文](https://arxiv.org/abs/2605.24931) · [代码](https://github.com/tars-robotics/RTR) |
| [GPT-as-Policy：大模型数值动作能力的六域评测](论文逐篇解读/P374.md) | 跨夹爪、灵巧手、移动操作、导航、行走和人形移动操作比较GPT-6 Astra直接数值控制与混合控制的接口和结果；混合模式由低层策略或全身控制器执行动作，13/30是回报超过基线的任务数而非成功率。 | [原文](https://arxiv.org/abs/2609.38537) · [代码](https://github.com/anonymous-report-421/GPT-as-Policy) · [项目页](https://galaxygeneralrobotics.github.io/astra-policy/) |
| [EffVLA：由动作头初始化、规模与延迟共同决定的高效 VLA](论文逐篇解读/P356.md) | EffVLA固定SigLIP2/Qwen2.5骨干与训练流程，系统比较动作头结构、损失、初始化、规模和推理轮数，并配对测量设备延迟。论文发现从语言主干复制末层初始化是跨规模最稳定的性能因素，并在LIBERO扰动集和SO-ARM101分拣任务验证迁移。 | [原文](https://arxiv.org/abs/2609.13984) · [代码](https://github.com/MindVLA-Team/EFFVLA) · [项目页](https://mindvla-team.github.io/EFFVLA) |
| [WorldArena：具身世界模型感知与功能效用统一评测基准](论文逐篇解读/P116.md) | 以视觉指标和数据生成、策略评价、动作规划任务共同评估具身世界模型的感知与功能效用。 | [原文](https://arxiv.org/abs/2602.08971) · [代码](https://github.com/tsinghua-fib-lab/WorldArena) · [项目页](https://world-arena.ai/) |

#### 相关项目

| 项目 | 主要用途 | 功能与特点 |
| --- | --- | --- |
| [Action-JND](https://arxiv.org/abs/2608.21247) | 训练、部署与评测工具 | Action-JND训练轻量逐Token容忍度估计器，预测视觉特征扰动在多大程度内仍能维持VLA动作响应；推理时将容忍度分数用于时序KV复用或直接剪枝。LIBERO上的OpenVLA实验在87.5%剪枝时报告42.00%平均成功率与30.16 ms延迟。 |
| [DROID Policy Learning](https://github.com/droid-dataset/droid_policy_learning) | 真实数据学习 | 在robomimic上扩展DROID的RLDS数据读取、策略训练和评测流程，并提供可选真实机器人控制接口。 |
| [EffVLA](https://github.com/MindVLA-Team/EFFVLA) | 训练、部署与评测工具 | EffVLA固定SigLIP2/Qwen2.5骨干与训练流程，系统比较动作头结构、损失、初始化、规模和推理轮数，并配对测量设备延迟。论文发现从语言主干复制末层初始化是跨规模最稳定的性能因素，并在LIBERO扰动集和SO-ARM101分拣任务验证迁移。 |
| [flexiv_trainer](https://github.com/flexivrobotics/flexiv_trainer) | 机器人学习训练平台 | 面向非夕机器人组织数据、训练与Physical AI技能开发流程，连接硬件接口和策略验证。 |
| [FluxVLA Engine](https://github.com/FluxVLA/FluxVLA) | VLA全链路工程平台 | 以统一配置连接LeRobot数据、策略训练、仿真评测和机器人接口，集成Fast-WAM、DiT4DiT及GR00T配方。 |
| [FoldQuantVLA](https://github.com/cair-vinuni/FoldQuantVLA) | 训练、部署与评测工具 | FoldQuantVLA在无需策略再训练的后训练量化中，为共享激活位置固定一致变换坐标，将其逆变换折叠进各消费者权重，并在原生整数路径执行W4A4；对语言主干敏感输出投影可采用选择性W8A8。Orin实机评估显示四项任务合计成功率为92.5%，均匀W4A4为80.0%。 |
| [fourier-lerobot](https://github.com/FFTAI/fourier-lerobot) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [GAUGE](https://github.com/InternRobotics/GAUGE) | 训练、部署与评测工具 | GAUGE以22类真实运动捕捉实验、校准物理参数和重复试验误差为共同参照，分别比较数值物理引擎的轨迹保真度与视频世界模型的物理定律拟合、参数准确度。 |
| [GPT-as-Policy](https://github.com/anonymous-report-421/GPT-as-Policy) | 训练、部署与评测工具 | 跨夹爪、灵巧手、移动操作、导航、行走和人形移动操作比较GPT-6 Astra直接数值控制与混合控制的接口和结果；混合模式由低层策略或全身控制器执行动作，13/30是回报超过基线的任务数而非成功率。 |
| [gr00t-agilex](https://github.com/agilexrobotics/gr00t-agilex) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [HIL-UMI](https://hil-umi.github.io/) | 训练、部署与评测工具 | HIL-UMI在UMI人类演示流中并行比较π0.5动作分布并采集策略盲区，另以低优势进度片段修正价值估计，再用混合历史/新增数据做优势条件克隆。 |
| [lerobot-agilex](https://github.com/agilexrobotics/lerobot-agilex) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [magicbot-gen1_pi0_demo](https://github.com/MagiclabRobotics/magicbot-gen1_pi0_demo) | VLA与机器人策略 | 展示pi0类视觉语言策略接入MagicBot Gen1的模型、观测和机器人执行接口。 |
| [openpi-agilex](https://github.com/agilexrobotics/openpi-agilex) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [real-time-chunking-kinetix](https://github.com/Physical-Intelligence/real-time-chunking-kinetix) | VLA训练与部署 | 将实时动作分块与策略接口连接，接收视觉、语言和机器人状态并输出连续动作序列。 |
| [robotera_vla](https://github.com/roboterax/robotera_vla) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [RTR](https://github.com/tars-robotics/RTR) | 训练、部署与评测工具 | 以连续VAE压缩60Hz高频动作块，并用Reuse-then-Refine重整异步推理后的拼接轨迹，改善xArm接触操作的动作平滑性、块间连续和执行时长。 |
| [tron2_openpi](https://github.com/limxdynamics/tron2_openpi) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [unitree_lerobot](https://github.com/unitreerobotics/unitree_lerobot) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [WorldArena](https://github.com/tsinghua-fib-lab/WorldArena) | 世界模型功能评测 | 以感知指标和任务评测衡量世界模型能力，并在仿真与真实机器人上检查视频质量能否转化为策略收益。 |
| [wuji-openpi](https://github.com/wuji-technology/wuji-openpi) | VLA训练与部署 | 扩展OpenPI以支持双臂和双Wuji Hand，连接ROS 2示范、LeRobot转换、微调、策略服务及真机推理。 |

[返回本页导航](#本页导航)

## 相关资料

- [技术与研究](README.md) · [书籍与课程](../强化学习开发者必备开源资料/书籍与课程.md)
