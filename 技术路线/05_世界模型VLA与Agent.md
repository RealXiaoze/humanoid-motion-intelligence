# 世界模型、VLA与Agent

> **这一页回答什么**：上层模型怎样理解视觉语言、预测环境变化、生成动作或调度技能，并与身体控制器形成闭环？

**这条路线的主要产物：**动作块、世界预测、技能图、空间记忆与重规划指令。

**读完后应该能够**：

- 分清上层模型输出的是关节动作、动作块、轨迹、末端目标还是技能调用。
- 区分严格世界模型、改变决策的世界代理模块和只提供训练资源的相邻基础设施。
- 按环境记忆、后果预测、交互数据、动作选择和安全验证追踪完整闭环。
- 判断证据停留在离线预测、仿真闭环、真机验证还是受控更新，避免把演示混写成持续学习。

## 本页导航

[内部路线](#怎么区分内部路线) · [系统边界](#先判断它在系统中是什么) · [能力闭环](#五类能力怎样形成闭环) · [使用层级](#世界模型怎样进入机器人系统) · [证据阶梯](#证据应该证明到哪一层) · [代表工作](#代表工作) · [完整条目](#完整条目)

## 怎么区分内部路线

- **动作生成与通用策略**：从视觉、语言、机器人状态或任务条件生成动作块、动作Token、连续轨迹或身体技能，并明确下游控制接口。
- **物理世界建模与预测**：学习动作条件下的未来视觉、潜在状态、物体变化或动力学，用于规划、数据生成、策略训练与功能评测。
- **记忆、规划与任务调度**：维护任务与空间上下文，把长程目标分解为技能图或子目标，并根据执行反馈更新记忆、检测失败和重新规划。

## 先判断它在系统中是什么

判断一项工作时，先看它是否使用当前观测或状态与候选动作预测后果，以及预测是否真正改变动作选择。不要仅凭名称中出现`World Model`、生成视频或接入仿真器就判断它已经形成机器人世界模型。

| 层次 | 最低判断条件 | 常见产物 | 不能直接推断什么 |
| --- | --- | --- | --- |
| 严格世界模型 | 输入当前状态/观测与动作，预测未来状态、观测、奖励、代价或分布，并能区分不同动作的后果 | 动力学模型、动作条件视频或潜在状态预测 | 预测准确不等于已经改善真实机器人决策 |
| 世界代理模块 | 不完整生成未来世界，但通过记忆、可供性、技能可行性、价值或风险判断改变决策 | 空间记忆、奖励模型、动作验证器、异常检测器 | 承担一项世界建模职责不等于具备完整世界模型 |
| 相邻基础设施 | 提供资产、任务、数据、仿真或评测，通常不直接参与在线动作选择 | 物理仿真器、数字孪生、数据引擎、Benchmark | 能够生成数据不等于具备动作条件预测或闭环规划 |

## 五类能力怎样形成闭环

```text
当前观测、机器人状态与任务目标
              ↓
环境建图与空间记忆：保存对象、关系、可供性、遮挡和任务状态
              ↓
动力学建模与后果预测：比较候选动作将怎样改变机器人与环境
              ↓
仿真环境与训练数据：提供交互世界、合成轨迹、失败样本与校准
              ↓
任务规划与动作选择：拆分任务、生成或排序动作、必要时重新规划
              ↓
身体控制器与真机执行：Tracker / Locomotion / WBC / MPC / 技能库
              ↓
策略测试与安全验证：成功判断、风险监测、异常检测与安全回退
              ↓
成功、失败、接管和恢复日志 → 数据筛选、训练、回归评测与再部署
```

仿真环境与训练数据也会回接记忆、预测、规划和评测，而不是只能单向向下流动；只有在输出参与动作比较、策略训练或闭环复测时，才产生可核验的决策价值。五类能力可以按任务组合，并非每套系统都必须同时采用生成式世界模型。

## 世界模型怎样进入机器人系统

- **L1：推理阶段指导**。部署时预测候选动作后果、判断技能可行性、选择轨迹或触发重新规划。
- **L2：训练阶段优化**。生成或筛选数据、学习奖励与价值、进行想象Rollout，最终训练独立策略。
- **L3：真实反馈驱动的共同演化**。真机日志经过筛选、训练、回归评测和安全闸门后更新模型或策略，再受控部署。

同一项目可以跨越多个层级，但必须分别提供证据。训练时使用世界模型，不代表部署时仍在线调用；根据新观测重新推理也不等于模型参数已经学习。

## 证据应该证明到哪一层

1. **离线预测**：在固定数据集上验证未来状态、视频、奖励或风险预测，尚未进入控制闭环。
2. **仿真闭环**：预测结果真实参与动作选择、策略训练或重规划，并在统一任务中比较基线。
3. **真机定量验证**：在配对条件下测量任务成功率、规划收益、风险识别、延迟和失败类型。
4. **受控更新闭环**：真实失败进入数据与模型更新，并通过固定回归集、安全检查和版本回退再次部署。

视觉质量、预测误差和演示视频只能支持部分结论。机器人世界模型还应检查动作敏感性、长时漂移、物理一致性、候选排序、不确定性、分布外检测、推理预算以及对下游任务的实际增益。

## 代表工作

### 论文

| 年份 | 论文/报告 | 核心问题 | 开源 |
| --- | --- | --- | --- |
| 2026 | [MotionWAM：面向实时人形移动操作的基座世界动作模型](../论文与项目/论文逐篇解读/P081.md) · [原文](https://arxiv.org/abs/2606.09215) | 视频世界模型通常生成慢且没有可执行动作，人形低层控制又缺少长程语义；Dual-DiT联合建模视觉未来与全身动作，分阶段数据训练后以实时动作序列调用既有身体执行接口。 | 否 |
| 2026 | [HoloAgent-0：具备三维空间记忆的统一具身智能体框架](../论文与项目/论文逐篇解读/P082.md) · [原文](https://arxiv.org/abs/2606.23565) | 长时机器人任务会因空间记忆过期、技能失败和异构本体接口而中断。AgentOS把语言计划转成受监控技能图，三维记忆随执行更新并触发重规划，控制边界落在技能契约而非关节层。 | 部分 · [代码](https://github.com/HorizonRobotics/HoloAgent) |
| 2026 | [DreamDojo：基于大规模人类视频的通用机器人世界模型](../论文与项目/论文逐篇解读/P114.md) · [原文](https://arxiv.org/abs/2602.06949) | 机器人动作标签稀缺，而人类第一视角视频缺少可直接监督的控制量；潜动作模型从四万四千小时视频学习交互动力学，再以后训练和蒸馏接入机器人动作，实现可控长时预测。 | 是 · [代码](https://github.com/NVIDIA/DreamDojo) |
| 2025 | [GR00T N1：面向通用人形机器人的开放基座模型](../论文与项目/论文逐篇解读/P060.md) · [原文](https://arxiv.org/abs/2503.14734) | 人形数据来自视频、仿真和不同本体，原始关节向量无法直接混合。视觉语言主干与扩散动作Transformer分工，Data Pyramid和本体专用动作编码统一监督，低层仍按具体机器人接口执行。 | 是 · [代码](https://github.com/NVIDIA/Isaac-GR00T) |

### 项目

| 项目 | 定位 |
| --- | --- |
| [GE-2 / GE-Sim 2.0](https://github.com/AgibotTech/GE-Sim-V2) | 当前图像、本体状态和候选动作进入生成模型，系统滚动预测未来视频与状态，独立策略服务据此完成闭环评测。它承担学习式策略试验和数据回流，物理接触精度仍由其他验证环节负责。 |
| [GO-2](https://www.agibot.com/article/231/detail/56.html) | Action CoT生成宏观动作意图，低频语义规划器持续细化计划，高频动作跟随器用残差修正现场偏差。公开材料界定了规划到执行的接口，具体控制输出仍缺少代码和权重验证。 |
| [HoloAgent](https://github.com/HorizonRobotics/HoloAgent) | AgentOS把语言任务展开为受监控的技能图，三维空间记忆支撑检索、执行反馈和失败恢复；当前仓库已开放机器人无关ROS 2核心、导航与感知节点、HTTP/ROS桥接、Unitree和HexFellow适配及录制工具，但模型和数据分发、无硬件快速启动与HoloAgent-1仍未完成。 |
| [Isaac-GR00T / GR00T N1.7](https://github.com/NVIDIA/Isaac-GR00T) | N1.7以Cosmos-Reason2-2B视觉语言主干和扩散动作头接收图像、语言与机器人状态，并用跨本体相对末端动作表示连接人类视频和机器人数据。仓库提供LeRobot后训练、推理及ONNX/TensorRT导出，可直接检查VLA适配新本体的工程成本。 |

## 完整条目

本路线当前收录 **42** 篇论文/技术报告、**91** 个项目。

### 动作生成与通用策略

从视觉、语言、机器人状态或任务条件生成动作块、动作Token、连续轨迹或身体技能，并明确下游控制接口。

#### 论文与技术报告

| 年份 | 论文/报告 | 核心问题 | 开源 |
| --- | --- | --- | --- |
| 2026 | [MotionWAM：面向实时人形移动操作的基座世界动作模型](../论文与项目/论文逐篇解读/P081.md) · [原文](https://arxiv.org/abs/2606.09215) | 视频世界模型通常生成慢且没有可执行动作，人形低层控制又缺少长程语义；Dual-DiT联合建模视觉未来与全身动作，分阶段数据训练后以实时动作序列调用既有身体执行接口。 | 否 |
| 2026 | [DreamZero：作为零样本策略的世界动作模型](../论文与项目/论文逐篇解读/P113.md) · [原文](https://arxiv.org/abs/2602.15922) | 视频世界模型通常只预测画面，机器人策略又只预测动作，二者误差无法在闭环中互相约束。联合自回归模型同步生成未来视觉和动作，并用最新观测滚动重置，使预训练模型可直接充当零样本策略。 | 是 · [代码](https://github.com/dreamzero0/dreamzero) |
| 2025 | [GR00T N1：面向通用人形机器人的开放基座模型](../论文与项目/论文逐篇解读/P060.md) · [原文](https://arxiv.org/abs/2503.14734) | 人形数据来自视频、仿真和不同本体，原始关节向量无法直接混合。视觉语言主干与扩散动作Transformer分工，Data Pyramid和本体专用动作编码统一监督，低层仍按具体机器人接口执行。 | 是 · [代码](https://github.com/NVIDIA/Isaac-GR00T) |
| 2025 | [WholeBodyVLA：面向全身移动操作控制的统一潜在VLA](../论文与项目/论文逐篇解读/P097.md) · [原文](https://arxiv.org/abs/2512.11047) | 无动作标注第一视角视频包含移动操作意图，却无法直接监督机器人关节；潜在动作模型从视频提取token，VLA解码为双臂动作和运动命令，独立LMO低层策略承担全身平衡与扰动控制。 | 否 |
| 2024 | [Octo：开源通用机器人策略](../论文与项目/论文逐篇解读/P056.md) · [原文](https://arxiv.org/abs/2405.12213) | 通用策略若把传感器和动作维度写死，迁移新机器人仍需重训主干。块状注意力Transformer学习共享任务表示，独立读出头适配新观测与动作，开源权重支持受控微调比较。 | 是 · [代码](https://github.com/octo-models/octo) |
| 2024 | [OpenVLA：开源视觉语言动作模型](../论文与项目/论文逐篇解读/P057.md) · [原文](https://arxiv.org/abs/2406.09246) | 开放VLA需要同时保留语义视觉与精细空间特征，并把连续动作接入语言模型；双视觉编码器为7B主干提供互补表征，动作离散为token，LoRA与全量微调暴露适配成本。 | 是 · [代码](https://github.com/openvla/openvla) |
| 2024 | [π0：面向通用机器人控制的视觉语言动作流模型](../论文与项目/论文逐篇解读/P058.md) · [原文](https://arxiv.org/abs/2410.24164) | 离散动作token难表达高频连续控制，普通扩散采样又可能过慢。预训练VLM负责语义条件，独立动作专家用Flow Matching生成连续动作块，并按本体归一化接口处理跨机器人数据。 | 部分 · [代码](https://github.com/Physical-Intelligence/openpi) |
| 2023 | [Diffusion Policy：基于动作扩散的视觉运动策略学习](../论文与项目/论文逐篇解读/P050.md) · [原文](https://arxiv.org/abs/2303.04137) | 连续操作动作往往多峰且长序列回归易平均化。条件扩散迭代生成一段动作轨迹，滚动时域只执行前缀再根据新视觉重规划，把多模态动作建模与高频闭环分开。 | 是 · [代码](https://github.com/real-stanford/diffusion_policy) |
| 2023 | [ACT / ALOHA：基于低成本硬件的精细双臂操作学习](../论文与项目/论文逐篇解读/P051.md) · [原文](https://arxiv.org/abs/2304.13705) | 低成本双臂示范数量少，逐步预测又会在长任务中累积误差；条件VAE与Transformer一次生成动作块，时间集成平滑重叠预测，使精细操作的数据效率和执行连续性可分别控制。 | 是 · [代码](https://github.com/tonyzhaozh/act) |
| 2023 | [RT-2：将网络知识迁移到机器人控制的视觉语言动作模型](../论文与项目/论文逐篇解读/P054.md) · [原文](https://arxiv.org/abs/2307.15818) | 机器人数据不足以覆盖开放语义，网页知识又没有动作标签。视觉语言任务与机器人轨迹共同微调同一模型，连续控制被离散为文本token，从而测试语义知识能否迁移到动作选择。 | 否 |
| 2023 | [Open X-Embodiment：跨本体机器人学习数据集与RT-X模型](../论文与项目/论文逐篇解读/P055.md) · [原文](https://arxiv.org/abs/2310.08864) | 不同机构的数据在本体、相机、动作和任务标注上互不兼容；统一数据协议保留本体差异并混合大规模轨迹，RT-X实验检验跨数据训练何时帮助新机器人，而非假设动作空间天然一致。 | 部分 · [代码](https://github.com/google-deepmind/open_x_embodiment) |
| 2022 | [RT-1：面向大规模真实世界控制的机器人Transformer](../论文与项目/论文逐篇解读/P052.md) · [原文](https://arxiv.org/abs/2212.06817) | 真实机器人多任务数据规模增加后，策略仍需在有限推理预算内共享视觉和动作表示。TokenLearner压缩图像，Transformer按历史预测离散动作token，检验任务与对象规模化的收益边界。 | 部分 |
| 2026 | [G0.5：让推理与动作回到同一条自回归序列](../论文与项目/论文逐篇解读/P162.md) · [原文](https://arxiv.org/abs/2608.11739) | VLM加动作专家的双系统VLA在语言理解与电机命令之间插入另一套参数与目标函数。G0.5用ActionCodec把异构本体动作按部位压成短离散码，让同一自回归Decoder在可选CoT后直接生成动作Token，预训练不引入单独动作回归损失。 | 部分 · [代码](https://github.com/OpenGalaxea/GalaxeaVLA) |
| 2026 | [Being-H0：以第一视角人类视频预训练视觉语言动作表征](../论文与项目/论文逐篇解读/P165.md) · [原文](https://arxiv.org/abs/2507.15597) | 机器人动作数据规模有限，而人类视频没有目标机器人的关节监督。Being-H0先学习视觉、语言与手部运动之间的对应关系，再用Action Query和机器人示范把共享表征接到具体动作空间。 | 是 · [代码](https://github.com/BeingBeyond/Being-H) |
| 2026 | [Being-H0.5：用共享动作语言连接人手与不同机器人本体](../论文与项目/论文逐篇解读/P166.md) · [原文](https://arxiv.org/abs/2601.12993) | 人类视频、遥操作与不同机器人动作维度不一致，直接拼接会让模型把本体差异当成任务规律。Being-H0.5用统一动作槽位和分路专家共享任务结构，同时保留各本体的动作输出边界。 | 是 · [代码](https://github.com/BeingBeyond/Being-H) |
| 2026 | [VITRA：把无标注人类活动视频加工成VLA预训练片段](../论文与项目/论文逐篇解读/P167.md) · [原文](https://arxiv.org/abs/2510.21571) | 公开人类视频覆盖大量操作，却缺少机器人控制标签。VITRA从视频中提取手和物体的视觉运动轨迹，把轨迹作为跨人手与机器人末端的中间表示，再用机器人数据完成动作空间适配。 | 是 · [代码](https://github.com/microsoft/VITRA) |
| 2026 | [EgoVLA：用手腕位姿和MANO手部参数连接人类视频与机器人动作](../论文与项目/论文逐篇解读/P168.md) · [原文](https://arxiv.org/abs/2507.12440) | 第一视角人类视频与机器人数据的视觉外观和动作表示不同。EgoVLA把人手运动恢复成统一腕部与MANO动作，再与机器人样本共同训练，使模型先学习任务和手物关系后再输出机器人动作。 | 是 · [代码](https://github.com/catburgg/EgoVLA) |
| 2026 | [Riemann-1.0：在同一因果模型中学习机器人动作与未来视觉](../论文与项目/论文逐篇解读/P177.md) · [原文](https://riemann-dynamics.github.io/Riemann-1.0-Website/paper/Riemann-1.0.pdf) | 第一视角视频、UMI示范和机器人轨迹的数据规模与动作监督不同。Riemann-1.0用同一套因果Action/Video DiT学习未来视觉与可执行动作，并通过本体专属动作头保留不同机器人的动作空间。 | 否 |
| 2025 | [DreamPolicy：面向可扩展人形运动控制的统一世界模型策略](../论文与项目/论文逐篇解读/P018.md) · [原文](https://arxiv.org/abs/2505.18780) | 为每类地形单独训练策略难以扩展，直接混合专家又会产生冲突。地形条件自回归扩散模型从专家数据生成未来身体状态，统一目标条件策略跟踪该状态并用转移判别器维持运动分布。 | 否 |
| 2025 | [π0.5：具备开放世界泛化能力的视觉语言动作模型](../论文与项目/论文逐篇解读/P059.md) · [原文](https://arxiv.org/abs/2504.16054) | 训练场景内的VLA容易依赖固定环境和短技能，进入新家庭后任务分解与执行同时失效；分阶段预训练把网页语义、多源机器人数据和长程移动操作对齐，再后训练连续动作头。 | 部分 · [代码](https://github.com/Physical-Intelligence/openpi) |
| 2025 | [Phantom：先把人类示范改造成目标机器人看到的训练画面](../论文与项目/论文逐篇解读/P169.md) · [原文](https://arxiv.org/abs/2503.00779) | 人类视频中的手臂外观与机器人不同，直接训练会在部署时遇到视觉域差异。Phantom先恢复人手动作并映射到目标机器人，再移除人臂、渲染机器人替身，使训练图像和测试时机器人视角更接近。 | 是 · [代码](https://github.com/MarionLepert/phantom) |
| 2025 | [GEN-0：跨本体真实操作数据驱动的通用机器人策略](../论文与项目/论文逐篇解读/P172.md) · [原文](https://generalistai.com/blog/gen-0) | 单一机器人和单一任务数据难以训练通用操作策略。GEN-0把多种自由度与任务的真实操作数据统一进入通用模型，再以少量目标任务数据后训练，观察模型规模和数据规模对下游成功率的影响。 | 否 |
| 2024 | [EgoMimic：以共享姿态监督联合人类视频与机器人示范](../论文与项目/论文逐篇解读/P170.md) · [原文](https://arxiv.org/abs/2410.24221) | 人类和机器人数据共享任务语义与手部运动，却只有机器人数据包含关节命令。EgoMimic让两类数据共享姿态预测，在机器人样本上额外训练动作头，并通过遮罩与方向标记减少人手和机械臂外观差异。 | 是 · [代码](https://github.com/SimarKareer/EgoMimic) |
| 2025 | [LeVERB：基于潜在视觉语言指令的人形全身控制](../论文与项目/论文逐篇解读/P062.md) · [原文](https://arxiv.org/abs/2506.13751) | 语言指令过于抽象，逐关节参考又不利于复用，人形全身控制缺少中间语义接口。视频与运动共同学习潜在视觉语言词汇，高层选择潜指令，冻结低层策略把它解码为身体动作。 | 否 |
| 2024 | [VLA Survey：具身智能视觉语言动作模型综述](../论文与项目/论文逐篇解读/P071.md) · [原文](https://arxiv.org/abs/2405.14093) | VLA工作在感知编码、语言推理、动作表示与部署层采用不同组合，只按模型名称难以比较；综述按组件、训练数据和动作输出建立分类，帮助识别规划模型与实时控制策略的边界。 | 是 |

#### 相关项目

| 项目 | 定位 |
| --- | --- |
| [ABot-Manipulation](https://github.com/amap-cvlab/ABot-Manipulation) | ABot-M0.5联合处理移动与操作任务，让世界表征、动作预测和评测在同一系统中连接；仓库开放推理、预训练模型和评测入口，用于检查移动操作是否真正形成统一动作接口。 |
| [ACoT-VLA](https://github.com/AgibotTech/ACoT-VLA) | 模型在动作生成前组织与任务执行相关的中间动作推理，使长时操作中的目标、状态变化和动作选择更容易关联；仓库开放模型和实验入口。 |
| [ACT](https://github.com/tonyzhaozh/act) | 以条件变分自编码器和Transformer一次预测动作块，再用时间集成平滑连续控制，减少长任务中的逐步误差累积；低成本双臂数据采集与真实部署代码使其成为模仿学习常用基线。 |
| [Being-H0](https://github.com/BeingBeyond/Being-H0) | 相机、语言和机器人状态进入策略模型生成动作块，再经本体接口送入真机或仿真执行并回收任务结果。 |
| [DeepThinkVLA](https://github.com/OpenBMB/DeepThinkVLA) | 模型在视觉与语言输入到动作输出之间加入与任务执行相关的推理过程，使复杂操作中的目标、状态和动作序列能够显式关联。 |
| [Diffusion Policy](https://github.com/real-stanford/diffusion_policy) | 一段未来动作被表示为条件扩散轨迹，视觉与本体观测引导多步去噪，控制器只执行滚动窗口前端。它为多峰操作动作提供清晰基线，复现时应单独测去噪步数、时域长度和闭环频率。 |
| [DreamZero](https://github.com/dreamzero0/dreamzero) | World Action Model同时预测未来视觉与机器人动作，DROID和AgiBot检查点接入训练、后训练与评测流程，推理由WebSocket服务解耦。这个结构可以单独测量视频预测是否真的改善动作选择，而不是只提升画面质量。 |
| [DROID Policy Learning](https://github.com/droid-dataset/droid_policy_learning) | 在robomimic基础上增加DROID的RLDS数据读取、训练和评测流程，并保留可选真实机器人控制接口；它把大规模异构真实示范转成可训练批次，是复现DROID策略学习的数据层入口。 |
| [FluxVLA Engine](https://github.com/FluxVLA/FluxVLA) | 以统一配置和标准接口连接LeRobot数据、VLA模型组装、分布式训练、仿真评测、推理优化与机器人部署；内置多种VLM或策略适配、LIBERO与RoboCasa数据入口以及真实双臂示例，适合检查同一模型怎样从数据进入真机控制。 |
| [fourier-lerobot](https://github.com/FFTAI/fourier-lerobot) | 相机、语言和机器人状态进入策略模型生成动作块，再经本体接口送入真机或仿真执行并回收任务结果。 |
| [GalaxeaDP](https://github.com/OpenGalaxea/GalaxeaDP) | 把相机观测、机器人状态和任务条件映射为连续动作块，用扩散策略完成双臂或移动操作；项目适合作为GalaxeaVLA之外的模仿学习基线。 |
| [GalaxeaVLA](https://github.com/OpenGalaxea/GalaxeaVLA) | 语言、视觉和机器人状态经过VLA生成移动底盘与双臂动作，用于在星海图本体上执行多步骤移动操作任务；仓库提供模型、数据或部署入口。 |
| [GigaBrain-0](https://github.com/open-gigaai/giga-brain-0) | 图像、点云、文本和本体状态进入统一模型，输出结构化任务规划与运动规划；仓库用于检查GigaWorld生成数据怎样进入GigaBrain训练和机器人任务执行链路。 |
| [GigaWorld-Policy](https://github.com/open-gigaai/giga-world-policy) | 以动作和环境变化的联合表征训练机器人策略，使世界模型不仅生成未来画面，也为动作选择提供表征；适合研究GigaWorld世界生成能力怎样转成可执行控制信号。 |
| [gr00t-agilex](https://github.com/agilexrobotics/gr00t-agilex) | 相机、语言和机器人状态进入策略模型生成动作块，再经本体接口送入真机或仿真执行并回收任务结果。 |
| [GraspVLA](https://github.com/PKU-EPIC/GraspVLA) | 视觉与语言目标经过空间理解和抓取策略生成六自由度末端动作，用于在开放物体与场景中完成抓取；项目连接视觉语言理解、抓取候选与机器人执行。 |
| [HEX](https://github.com/Open-X-Humanoid/HEX) | 不同人形的状态先对齐到共享身体部位槽位，统一本体预测器学习跨本体协调和时序动力学，视觉语言线索再经残差门控与流匹配动作头生成手臂、手和腰动作；腿部由低层RL全身控制器执行高层命令，明确了VLA与运动控制之间的接口。 |
| [HY-Embodied](https://github.com/Tencent-Hunyuan/HY-Embodied) | 仓库汇总HY-Embodied系列模型、数据、训练和评测入口，使读者能够从统一位置追踪VLA、世界模型和跨本体版本之间的关系。 |
| [HY-Embodied-0.5-VLA](https://github.com/Tencent-Hunyuan/Hy-Embodied-0.5-VLA) | 模型接收视觉、语言和机器人状态并生成动作序列，面向多任务操作和后训练；仓库提供模型与推理入口，用于分析HY具身模型的动作接口。 |
| [HY-Embodied-0.5-X](https://github.com/Tencent-Hunyuan/HY-Embodied-0.5-X) | 通过共享多模态表征和统一动作接口学习不同机器人数据，使模型能够在多个本体和任务间迁移；仓库用于检查跨本体训练、适配和评测流程。 |
| [Isaac-GR00T / GR00T N1.7](https://github.com/NVIDIA/Isaac-GR00T) | N1.7以Cosmos-Reason2-2B视觉语言主干和扩散动作头接收图像、语言与机器人状态，并用跨本体相对末端动作表示连接人类视频和机器人数据。仓库提供LeRobot后训练、推理及ONNX/TensorRT导出，可直接检查VLA适配新本体的工程成本。 |
| [JALA](https://github.com/BeingBeyond/JALA) | 相机、语言和机器人状态进入策略模型生成动作块，再经本体接口送入真机或仿真执行并回收任务结果。 |
| [lerobot-agilex](https://github.com/agilexrobotics/lerobot-agilex) | 相机、语言和机器人状态进入策略模型生成动作块，再经本体接口送入真机或仿真执行并回收任务结果。 |
| [LingBot-VLA 1.0](https://github.com/Robbyant/lingbot-vla) | 语言、图像和机器人状态经过具身模型生成动作块，仓库开放训练、后训练、评测和部署入口；它适合追溯LingBot-VLA从首版到2.0的接口变化，而不应再作为当前版本能力的唯一依据。 |
| [LingBot-VLA 2.0](https://github.com/Robbyant/lingbot-vla-v2) | 把单臂、双臂、半人形、人形与第一视角数据映射到统一状态动作向量，稀疏MoE动作专家学习共享与本体特有模式，当前与未来感知查询分别接收深度和视频教师信号；仓库开放预训练权重、训练配置、数据映射、后训练和评测入口。 |
| [Octo](https://github.com/octo-models/octo) | 用Transformer与扩散动作头从多机器人数据学习通用策略，支持RGB、语言和目标图像等条件，并用模块化注意力扩展传感器与动作维度；适合作为跨本体预训练和下游微调的研究基线。 |
| [OpenDM](https://github.com/dexmal/opendm) | DM0.5根据语言、图像和机器人状态生成动作序列，面向开放指令、长时任务、动态干扰和多本体控制；OpenDM开放基础及任务权重、训练和推理脚本、数据注册示例，以及LIBERO、RoboTwin和SO101后训练流程。 |
| [openpi](https://github.com/Physical-Intelligence/openpi) | 仓库同时维护流匹配式π0、快速自回归π0-FAST和π0.5，并提供检查点、数据配置、微调与推理服务。接入新机器人时最关键的工作是动作归一化、数据字段映射和推理频率对齐。 |
| [openpi-agilex](https://github.com/agilexrobotics/openpi-agilex) | 相机、语言和机器人状态进入策略模型生成动作块，再经本体接口送入真机或仿真执行并回收任务结果。 |
| [OpenVLA](https://github.com/openvla/openvla) | 预训练模型以视觉和语言生成机器人动作，仓库同时开放RLDS数据混合、LoRA或全参数微调和推理部署入口。接入新本体时，可以沿相机标定、指令格式和动作空间三处拆开评估适配成本。 |
| [Pelican-VLA 0.5](https://github.com/Open-X-Humanoid/Pelican-VLA05) | 共享Qwen3-VL主干联合视觉语言理解、未来帧和动作预测，固定容量瓶颈Token把与接触相关的视觉信息送入动作通路；当前版本重点验证注意力层面的跨场景与跨本体泛化，并明确承认从表征到可靠动作仍有缺口。 |
| [real-time-chunking-kinetix](https://github.com/Physical-Intelligence/real-time-chunking-kinetix) | 相机、语言和机器人状态进入策略模型生成动作块，再经本体接口送入真机或仿真执行并回收任务结果。 |
| [Rethink_VLA](https://github.com/BeingBeyond/Rethink_VLA) | 相机、语言和机器人状态进入策略模型生成动作块，再经本体接口送入真机或仿真执行并回收任务结果。 |
| [Riemann-1.0](https://riemann-dynamics.github.io/Riemann-1.0-Website/) | 同一因果模型在策略模式下根据真实视觉与本体状态生成动作块，在模拟模式下根据给定动作预测未来视觉；三阶段训练把无动作第一视角视频、UMI与机器人轨迹逐步对齐到目标本体。 |
| [robotera_vla](https://github.com/roboterax/robotera_vla) | 相机、语言和机器人状态进入策略模型生成动作块，再经本体接口送入真机或仿真执行并回收任务结果。 |
| [RynnVLA-001](https://github.com/alibaba-damo-academy/RynnVLA-001) | 把语言任务、视觉观测和机器人状态映射为动作序列，构成Rynn系列早期的通用操作基线；保留该版本有助于比较002在数据、结构和长时任务上的改动。 |
| [RynnVLA-002](https://github.com/alibaba-damo-academy/RynnVLA-002) | RynnVLA-002在视觉、语言和机器人状态条件下预测动作，面向跨任务和跨本体操作；项目用于检查Rynn系列从模型结构、训练数据到策略评测的更新。 |
| [Spirit-v1.5](https://github.com/Spirit-AI-Team/spirit-v1.5) | 模型根据视觉、语言和机器人状态生成操作动作，面向多任务和真实场景泛化；仓库提供Spirit-v1.5的模型与研究入口。 |
| [tron2_openpi](https://github.com/limxdynamics/tron2_openpi) | 相机、语言和机器人状态进入策略模型生成动作块，再经本体接口送入真机或仿真执行并回收任务结果。 |
| [UnifoLM-VLA-0](https://github.com/unitreerobotics/unifolm-vla) | LeRobot数据先转换为HDF5和RLDS，视觉语言主干与机器人状态共同生成动作块；仓库公开多数据集训练、LIBERO评测、服务端推理和G1客户端部署入口，把数据准备、后训练与真机执行连成一条链。 |
| [unitree_lerobot](https://github.com/unitreerobotics/unitree_lerobot) | 相机、语言和机器人状态进入策略模型生成动作块，再经本体接口送入真机或仿真执行并回收任务结果。 |
| [video-prediction-policy](https://github.com/roboterax/video-prediction-policy) | 相机、语言和机器人状态进入策略模型生成动作块，再经本体接口送入真机或仿真执行并回收任务结果。 |
| [VIPA-VLA](https://github.com/BeingBeyond/VIPA-VLA) | 相机、语言和机器人状态进入策略模型生成动作块，再经本体接口送入真机或仿真执行并回收任务结果。 |
| [WALL-X](https://github.com/X-Square-Robot/WALL-X) | 语言、视觉和机器人状态经过统一模型生成操作动作，面向多任务与跨本体执行；仓库开放训练或推理入口，构成X Square具身模型主线。 |
| [WholeBodyVLA](https://github.com/OpenDriveLab/WholebodyVLA) | 从无动作标注的第一视角视频学习统一潜在动作，将视觉和语言解码为双臂关节动作与运动命令，再交给面向移动操作的低层策略执行；当前仓库仅提供论文资源与研究索引。 |
| [X-Tokenizer](https://github.com/X-Square-Robot/X-Tokenizer) | 把不同机器人或任务的连续动作编码为可由序列模型处理的Token，并解码回可执行动作；它为WALL系列跨本体训练提供动作表示基础。 |
| [Xiaomi-Robotics-0](https://github.com/XiaomiRobotics/Xiaomi-Robotics-0) | 视觉、语言和本体状态经过统一模型生成机器人动作，用于建立小米机器人团队的通用操作基线；保留首版便于比较后续版本在数据、结构和任务覆盖上的变化。 |
| [Xiaomi-Robotics-1](https://github.com/XiaomiRobotics/Xiaomi-Robotics-1) | 在首版基础上扩展训练数据、操作任务和泛化评测，使视觉语言模型输出更稳定的机器人动作序列；项目用于追踪同一团队模型迭代而非只看单次演示。 |
| [Xiaomi-Robotics-U0](https://github.com/XiaomiRobotics/Xiaomi-Robotics-U0) | 通过统一观测与动作接口吸收不同任务或本体数据，使单一模型能够在多种机器人操作任务间迁移；项目重点在统一表示和后训练接口。 |
| [XR-1](https://github.com/Open-X-Humanoid/XR-1) | 三阶段流程先学习统一视觉—运动离散表征，再在异构视觉与机器人数据上预训练，最后按具体本体微调动作策略；官方实现统一LeRobot 2.1数据加载、跨数据集训练、权重和Franka/UR/AgileX部署脚本，并给出天工2.0适配入口。 |

### 物理世界建模与预测

学习动作条件下的未来视觉、潜在状态、物体变化或动力学，用于规划、数据生成、策略训练与功能评测。

#### 论文与技术报告

| 年份 | 论文/报告 | 核心问题 | 开源 |
| --- | --- | --- | --- |
| 2026 | [DreamDojo：基于大规模人类视频的通用机器人世界模型](../论文与项目/论文逐篇解读/P114.md) · [原文](https://arxiv.org/abs/2602.06949) | 机器人动作标签稀缺，而人类第一视角视频缺少可直接监督的控制量；潜动作模型从四万四千小时视频学习交互动力学，再以后训练和蒸馏接入机器人动作，实现可控长时预测。 | 是 · [代码](https://github.com/NVIDIA/DreamDojo) |
| 2026 | [WorldArena：具身世界模型感知与功能效用统一评测基准](../论文与项目/论文逐篇解读/P116.md) · [原文](https://arxiv.org/abs/2602.08971) | 世界模型视觉指标高并不代表能支持机器人决策；十六项指标先测感知质量，数据生成、策略评价和动作规划任务再测功能效用，并以人类对比和EWMScore揭示两者脱节。 | 是 · [代码](https://github.com/tsinghua-fib-lab/WorldArena) |
| 2025 | [GigaWorld-0：作为具身智能数据引擎的世界模型](../论文与项目/论文逐篇解读/P115.md) · [原文](https://arxiv.org/abs/2511.19861) | 仅生成外观逼真的视频不足以形成可用机器人数据。视频链控制视角与动作，三维高斯场景补几何一致性，系统辨识和规划模块再校验物理与任务，使世界模型承担数据引擎角色。 | 是 · [代码](https://github.com/open-gigaai/giga-world-0) |
| 2023 | [DreamerV3：基于世界模型的跨领域通用控制](../论文与项目/论文逐篇解读/P065.md) · [原文](https://arxiv.org/abs/2301.04104) | 世界模型跨视觉游戏和控制域时常因奖励尺度、数值范围与超参数变化失稳；离散潜变量、symlog和two-hot回归统一表示与损失尺度，使同一配置可跨域训练，但不消除模型误差。 | 是 · [代码](https://github.com/danijar/dreamerv3) |
| 2019 | [Dreamer：基于潜在想象的行为学习](../论文与项目/论文逐篇解读/P064.md) · [原文](https://arxiv.org/abs/1912.01603) | 在线环境交互昂贵时，策略更新不能依赖每个候选动作都真实试验。世界模型从历史学习潜在转移，Actor-Critic在短时想象轨迹中训练，再回到真实观测闭环校正模型偏差。 | 是 · [代码](https://github.com/danijar/dreamer) |
| 2018 | [PlaNet：基于像素输入的潜在动力学规划](../论文与项目/论文逐篇解读/P063.md) · [原文](https://arxiv.org/abs/1811.04551) | 从像素直接规划需要预测与控制相关的未来而非重建全部图像细节；RSSM结合确定性记忆和随机潜变量，观测模型学习潜在动力学，CEM在模型中搜索动作序列并滚动执行。 | 是 |
| 2026 | [WAM-TTT：用无标注人类视频在部署前调整世界动作模型](../论文与项目/论文逐篇解读/P173.md) · [原文](https://arxiv.org/abs/2607.06988) | 世界动作模型遇到新任务时缺少与机器人动作配对的数据。WAM-TTT用配对人机示范元训练快速记忆，再在部署前只观看无标注人类视频更新轻量权重，以视觉变化引导冻结动作模型生成机器人动作。 | 否 |
| 2026 | [LDA-1B：让不同质量的具身数据共同训练视觉预测与机器人动作](../论文与项目/论文逐篇解读/P174.md) · [原文](https://arxiv.org/abs/2602.12215) | 机器人示范、人类视频和仿真轨迹的监督完整度不同。LDA-1B按数据可用字段分配策略、正向动力学、逆向动力学和视觉预测任务，让无动作视频也能训练世界变化表示，再用目标本体数据生成可执行动作块。 | 部分 · [代码](https://github.com/jiangranlv/LDA-1B) |
| 2026 | [Matrix-Game 3.5：用三维Patch记忆维持长时交互视频的一致性](../论文与项目/论文逐篇解读/P178.md) · [原文](https://matrix-game-v3-5.github.io/paper/Matrix-Game-3.5.pdf) | 相机可控视频模型长时间自回归时容易遗忘离开视野的场景，并在重新观察时产生几何漂移和动态主体重影。Matrix-Game 3.5把历史静态Patch回投三维并重投影到新视角，同时用参考Token单独维持动态主体。 | 部分 · [代码](https://github.com/Riemann-Dynamics/Matrix-Game-3.5) |
| 2025 | [V-JEPA 2：面向理解、预测与规划的自监督视频模型](../论文与项目/论文逐篇解读/P067.md) · [原文](https://arxiv.org/abs/2506.09985) | 海量无动作视频能学到物体和运动规律，却不能直接决定机器人控制；掩码潜在预测先获得视频表征，再用少量机器人数据训练动作条件世界模型，并以模型预测控制选择可执行动作。 | 是 · [代码](https://github.com/facebookresearch/vjepa2) |
| 2025 | [GR00T-Dreams：面向人形机器人学习的合成轨迹生成](../论文与项目/论文逐篇解读/P068.md) · [原文](https://developer.nvidia.com/blog/enhance-robot-learning-with-synthetic-trajectory-data-generated-by-world-foundation-models/) | 人形真实轨迹稀缺，纯视频生成又缺少可靠动作标签。世界基础模型先生成任务变化与未来视觉，逆动力学模型补动作，再经仿真或策略筛选形成训练轨迹，关键瓶颈是标签误差回流。 | 部分 |
| 2024 | [Denoising World Model Locomotion：基于去噪世界模型的复杂地形人形运动控制](../论文与项目/论文逐篇解读/P017.md) · [原文](https://arxiv.org/abs/2408.14472) | 噪声和遮挡使本体历史无法直接提供控制所需状态；循环编码器以特权真值做去噪重建并与PPO联合优化，策略从潜变量立即输出关节目标，属于学习式状态估计而非向前滚动规划的世界模型。 | 部分 |
| 2023 | [UniSim：交互式真实世界模拟器学习](../论文与项目/论文逐篇解读/P066.md) · [原文](https://arxiv.org/abs/2310.06114) | 真实视频数据异构且缺少统一动作标注，传统模拟器又难覆盖外观变化。条件生成模型融合机器人轨迹、驾驶和互联网视频，按动作生成可交互未来画面，但视觉一致性不能替代接触动力学验证。 | 否 |
| 2025 | [Embodied World Model Survey：具身智能世界模型综合综述](../论文与项目/论文逐篇解读/P072.md) · [原文](https://arxiv.org/abs/2510.16732) | 具身世界模型既可做状态估计、未来预测、数据生成或规划，单一“生成质量”指标无法覆盖。综述从功能、时间建模和空间表示三轴组织方法，并强调以决策效用评估。 | 是 · [代码](https://github.com/Li-Zn-H/AwesomeWorldModels) |

#### 相关项目

| 项目 | 定位 |
| --- | --- |
| [1xgpt](https://github.com/1x-technologies/1xgpt) | 当前观测与动作条件进入生成或预测模型，输出未来状态、视频或交互结果，为策略训练、评测或规划提供数据。 |
| [ABot-PhysWorld](https://github.com/amap-cvlab/ABot-PhysWorld) | 通过视频、动作与状态联合训练模型理解接触、位移和环境变化，并提供训练和数据入口；它位于合成数据、未来预测和动作学习之间。 |
| [ABot-World](https://github.com/amap-cvlab/ABot-World) | 模型接收场景条件与交互输入持续滚动生成未来世界，用于建立能够被机器人策略反复交互的视觉环境；仓库开放推理入口和模型资料，可用于分析长序列生成中的一致性与误差积累。 |
| [AgiBotWorldChallengeICRA2026-WorldModelBaseline](https://github.com/AgibotTech/AgiBotWorldChallengeICRA2026-WorldModelBaseline) | 当前观测与动作条件进入生成或预测模型，输出未来状态、视频或交互结果，为策略训练、评测或规划提供数据。 |
| [Being-VL-0.5](https://github.com/BeingBeyond/Being-VL-0.5) | 当前观测与动作条件进入生成或预测模型，输出未来状态、视频或交互结果，为策略训练、评测或规划提供数据。 |
| [DreamDojo](https://github.com/NVIDIA/DreamDojo) | 四万四千小时第一视角视频先建立潜在动作表示，机器人数据后训练再把它转成可交互策略并蒸馏到十帧每秒运行。开放的数据、模型与推理入口让人类视频预训练对机器人控制的增益可以分阶段核对。 |
| [EnerVerse-AC](https://github.com/AgibotTech/EnerVerse-AC) | 根据机器人场景和动作条件生成未来视觉变化，用于构造操作数据和研究动作结果预测；它是Genie-Envisioner与GE-Sim-V2之前的重要历史入口。 |
| [GE-2 / GE-Sim 2.0](https://github.com/AgibotTech/GE-Sim-V2) | 当前图像、本体状态和候选动作进入生成模型，系统滚动预测未来视频与状态，独立策略服务据此完成闭环评测。它承担学习式策略试验和数据回流，物理接触精度仍由其他验证环节负责。 |
| [Genie-Envisioner](https://github.com/AgibotTech/Genie-Envisioner) | 从场景和动作条件生成机器人交互视频，为策略训练、数据扩充和未来预测提供可控环境；仓库连接GE-Sim系列与早期EnerVerse-AC路线。 |
| [GigaWorld-0](https://github.com/open-gigaai/giga-world-0) | 把视频外观、视角和动作建模与三维高斯场景、系统辨识及规划模块连接，形成服务VLA训练的数据生成流程；已开放训练、推理和模型配置，可核查世界建模如何产出机器人可用数据。 |
| [GigaWorld-1](https://github.com/open-gigaai/giga-world-1) | GigaWorld-1继续研究机器人动作条件下的未来环境生成、交互一致性和世界模型评测，为具身数据生成与策略训练提供可控环境变化。 |
| [Kairos](https://github.com/kairos-agi/kairos) | Kairos以通用视频、人类行为和真机交互数据逐级训练持续世界表征，并在统一模型中预测未来视觉状态与可执行动作；仓库开放推理代码和多组模型权重，并提供RoboTwin与LIBERO评测入口。 |
| [LDA-1B](https://github.com/jiangranlv/LDA-1B) | 官方仓库开放LDA-1B模型、部分训练与评测入口、配置和检查点，用同一多模态扩散Transformer联合处理动作块和未来视觉潜变量；适合检查策略、正向动力学、逆向动力学与视觉预测怎样共享主干。 |
| [LingBot-VA](https://github.com/Robbyant/lingbot-va) | 视频潜变量流与机器人动作流在双流Transformer中交替建模，模型既预测动作也预测动作条件下的未来画面；仓库开放权重、RoboTwin与LIBERO后训练数据、训练和推理脚本，可检查世界预测怎样与策略输出共享表示但保持独立输出。 |
| [LingBot-Video](https://github.com/Robbyant/lingbot-video) | 稠密与MoE视频模型从文本或图像条件生成未来视频，并通过大规模视频预训练学习场景变化与运动模式；仓库开放推理代码、模型权重和提示词重写器，可作为世界动态表征或人类视频预训练研究入口。 |
| [LingBot-World 1.0](https://github.com/Robbyant/lingbot-world) | 根据文本、初始画面或动作条件生成未来视频，用视频预训练表达机器人动作后的环境变化；它构成LingBot-World 2.0之前的技术入口，可用于比较离线视频生成与后续长时交互世界模型的差异。 |
| [LingBot-World 2.0](https://github.com/Robbyant/lingbot-world-v2) | 因果视频模型根据初始画面、文本与交互控制持续生成世界演化，KV缓存与蒸馏版本面向实时推理，Pilot和Director两个Agent分别组织角色行为与环境事件；它提供可交互环境模拟能力，不直接输出机器人关节动作。 |
| [Matrix-Game 3.5](https://github.com/Riemann-Dynamics/Matrix-Game-3.5) | 根据文本、初始画面、可选主体参考图和相机轨迹持续生成未来视频；Warped PRoPE编码相机几何，Patch Memory保存静态场景，参考Token维护动态主体，再通过渐进蒸馏获得少步因果生成器。 |
| [MotuBrain](https://github.com/shengshu-ai/MotuBrain) | MotuBrain把视频、动作和语言统一建模，并面向多本体适配、长程任务和实时闭环；公开仓库主要承载技术报告、图示和发布材料，适合了解系统定位。 |
| [Motus](https://github.com/thu-ml/Motus) | Motus在统一架构中学习视频世界变化、语言条件和机器人动作，使同一模型既表达未来环境也支持动作预测；仓库开放模型与实验入口，用于检查世界模型怎样扩展到机器人策略。 |
| [OpenDW](https://github.com/dexmal/opendw) | DW0.5接收语言、图像或视频、机器人类型、状态和动作，用共享骨干及视频、动作、价值专家联合预测未来画面、动作与状态价值；仓库开放权重、推理与训练代码，并给出RoboTwin式数据格式和动作条件回放入口。 |
| [RoboTransfer](https://github.com/HorizonRobotics/RoboTransfer) | 当前观测与动作条件进入生成或预测模型，输出未来状态、视频或交互结果，为策略训练、评测或规划提供数据。 |
| [RynnWorld-4D](https://github.com/alibaba-damo-academy/RynnWorld-4D) | 模型联合表达三维空间结构和时间演化，用于预测机器人动作后的场景变化与对象运动；适合作为空间理解、世界生成和规划之间的研究入口。 |
| [UnifoLM-WMA-0](https://github.com/unitreerobotics/unifolm-world-model-action) | 视觉观测和动作条件进入世界模型预测未来状态，动作模块再把预测与任务条件转成机器人控制序列；官方仓库提供数据处理、训练、推理、权重和G1部署入口，用于检查世界预测怎样接回真实动作闭环。 |
| [WALL-WM](https://github.com/X-Square-Robot/WALL-WM) | 联合建模场景视频、机器人状态与动作，预测执行后的环境变化，为动作选择和策略训练提供世界表征；仓库公开模型结构与训练评测入口。 |
| [WorldArena](https://github.com/tsinghua-fib-lab/WorldArena) | 十六项感知指标与功能任务把“视频生成更像”拆成可测能力，2.0又跨RoboTwin、LIBERO和真实ALOHA检查这些指标能否转化为策略收益。把新模型接入数据引擎、策略排序和动作规划三条路径，可以检验视觉质量是否真正转成控制收益。 |
| [X-WAM](https://github.com/sharinka0715/X-WAM) | 模型联合学习视频世界变化与机器人动作，在共享表征中支持跨本体操作和未来预测；项目用于检查世界模型输出怎样与动作头连接。 |

### 记忆、规划与任务调度

维护任务与空间上下文，把长程目标分解为技能图或子目标，并根据执行反馈更新记忆、检测失败和重新规划。

#### 论文与技术报告

| 年份 | 论文/报告 | 核心问题 | 开源 |
| --- | --- | --- | --- |
| 2026 | [HoloAgent-0：具备三维空间记忆的统一具身智能体框架](../论文与项目/论文逐篇解读/P082.md) · [原文](https://arxiv.org/abs/2606.23565) | 长时机器人任务会因空间记忆过期、技能失败和异构本体接口而中断。AgentOS把语言计划转成受监控技能图，三维记忆随执行更新并触发重规划，控制边界落在技能契约而非关节层。 | 部分 · [代码](https://github.com/HorizonRobotics/HoloAgent) |
| 2023 | [PaLM-E：具身多模态语言模型](../论文与项目/论文逐篇解读/P053.md) · [原文](https://arxiv.org/abs/2303.03378) | 语言模型无法直接消费连续相机和机器人状态；传感器特征被投影成与文本相同的嵌入序列并参与自回归训练，使视觉、状态和语言共享推理上下文，但输出仍是语言层而非电机动作。 | 否 |
| 2025 | [Gemini Robotics：面向物理世界的通用机器人智能模型](../论文与项目/论文逐篇解读/P061.md) · [原文](https://deepmind.google/models/gemini-robotics/) | 多模态模型具备语义和空间推理，却难满足机器人实时动作闭环；高层具身推理与低层视觉动作模型分级运行，并以少量本体数据适配新机器人，语义安全仍不等于物理控制安全。 | 部分 |

#### 相关项目

| 项目 | 定位 |
| --- | --- |
| [ABot-Navigation](https://github.com/amap-cvlab/ABot-Navigation) | 视觉与语言指令经过场景理解和导航策略生成移动决策，仓库提供Benchmark、评测和方法入口；它用于检验高层语言目标怎样接到底盘导航，而不是机械臂操作。 |
| [embodied-skill-kit](https://github.com/Open-X-Humanoid/embodied-skill-kit) | 语言任务和多模态环境状态进入任务规划模块，生成技能调用或导航操作步骤，并根据执行反馈重新组织任务。 |
| [genisom_vln](https://github.com/zsibot/genisom_vln) | 语言任务和多模态环境状态进入任务规划模块，生成技能调用或导航操作步骤，并根据执行反馈重新组织任务。 |
| [GO-2](https://www.agibot.com/article/231/detail/56.html) | Action CoT生成宏观动作意图，低频语义规划器持续细化计划，高频动作跟随器用残差修正现场偏差。公开材料界定了规划到执行的接口，具体控制输出仍缺少代码和权重验证。 |
| [HoloAgent](https://github.com/HorizonRobotics/HoloAgent) | AgentOS把语言任务展开为受监控的技能图，三维空间记忆支撑检索、执行反馈和失败恢复；当前仓库已开放机器人无关ROS 2核心、导航与感知节点、HTTP/ROS桥接、Unitree和HexFellow适配及录制工具，但模型和数据分发、无硬件快速启动与HoloAgent-1仍未完成。 |
| [MiniCPM-Robot](https://github.com/OpenBMB/MiniCPM-Robot) | 将小型多模态模型用于机器人视觉跟踪、目标理解和动作决策，并提供Jetson、ROS 2及机器人SDK集成入口；项目强调本地断网运行和工程部署。 |
| [Pelican-VL](https://github.com/Open-X-Humanoid/pelican-vl) | Pelican-VL从视觉和语言输入形成空间理解、任务推理与高层动作目标，为下层VLA、技能或运动控制模块提供计划；项目开放多尺度模型入口。 |
| [robocup_demo](https://github.com/BoosterRobotics/robocup_demo) | 语言任务和多模态环境状态进入任务规划模块，生成技能调用或导航操作步骤，并根据执行反馈重新组织任务。 |
| [RxBrain-1.0](https://github.com/Tencent-Hunyuan/Hy-Embodied-RxBrain-1.0) | 视觉与语言输入形成场景理解和任务计划，再向下层操作或导航策略发出目标；项目用于区分高层认知、策略动作与低层控制三种职责。 |
| [RynnBrain](https://github.com/alibaba-damo-academy/RynnBrain) | 视觉和语言输入先形成场景与任务表示，再输出任务步骤或技能调用，为下层VLA、导航和操作策略提供高层目标；仓库用于理解Rynn体系中大脑层与动作层的接口。 |
| [RynnEC](https://github.com/alibaba-damo-academy/RynnEC) | 项目研究机器人怎样从多模态观测形成环境理解、任务分解和下一步决策，并把结果交给导航或操作模块执行；适合定位认知规划层与低层策略之间的接口。 |
| [RynnValue](https://github.com/alibaba-damo-academy/RynnValue) | 模型对候选动作或执行轨迹进行价值判断，为策略选择、失败筛选和后训练提供反馈信号；它解决的是动作好坏的评估，不直接生成完整机器人控制命令。 |
| [tron1-agent](https://github.com/limxdynamics/tron1-agent) | 语言任务和多模态环境状态进入任务规划模块，生成技能调用或导航操作步骤，并根据执行反馈重新组织任务。 |
| [UrbanVLA](https://github.com/GalaxyGeneralRobotics/UrbanVLA) | 将第一视角视觉、语言指令与机器人状态映射为移动决策，使机器人在室外或半开放城市环境中完成目标导向导航。 |
