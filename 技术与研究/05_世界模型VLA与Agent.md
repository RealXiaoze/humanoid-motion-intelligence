# 世界模型、VLA与Agent

> 视觉语言理解、未来预测与任务决策，汇总相关论文、方法与项目。

当前收录 **69** 篇论文／技术报告、**116** 个项目。

## 本页导航

[VLA与通用操作策略](#vla与通用操作策略) · [世界动作模型（WAM）](#世界动作模型（wam）) · [世界模型与仿真生成](#世界模型与仿真生成) · [具身理解与Agent规划](#具身理解与agent规划) · [训练、部署与评测工具](#训练部署与评测工具) · [相关资料](#相关资料)

## VLA与通用操作策略

根据视觉、语言或机器人状态生成动作，涵盖模仿学习、跨本体策略与后训练方法。

#### 论文与技术报告

| 论文／报告 | 主要方法与用途 | 原文／代码 |
| --- | --- | --- |
| [ALOE：混合轨迹中的动作级离策略评估](论文逐篇解读/P185.md) | 以动作块为单位进行离策略价值估计，为稀疏奖励下的视觉语言动作模型后训练提供评估。 | [原文](https://arxiv.org/abs/2602.12691) · [项目页](https://github.com/AgibotTech/aloe) |
| [Being-H0.5：用共享动作语言连接人手与不同机器人本体](论文逐篇解读/P166.md) | 以统一动作槽位和分路专家共训人类与多种机器人数据，保留跨本体操作输出差异。 | [原文](https://arxiv.org/abs/2601.12993) · [代码](https://github.com/BeingBeyond/Being-H) · [项目页](https://research.beingbeyond.com/being-h05) |
| [Being-H0：以第一视角人类视频预训练视觉语言动作表征](论文逐篇解读/P165.md) | 先从人类视频预训练视觉、语言与手部运动表征，再用机器人示范适配灵巧操作动作空间。 | [原文](https://arxiv.org/abs/2507.15597) · [代码](https://github.com/BeingBeyond/Being-H) · [项目页](https://research.beingbeyond.com/being-h0) |
| [BridgeVLA++：让三维操作策略记住已经发生的交互](论文逐篇解读/P204.md) | 以二维热图生成粗到细动作，并用时间和空间记忆恢复遮挡目标几何以完成三维操作。 | [原文](https://arxiv.org/abs/2608.05042) · [代码](https://github.com/npucvr/BridgeVLA-Seq) · [项目页](https://bridgevla-plus.github.io/) |
| [CLIFT：用真机奖励闭环适配人形 VLA](论文逐篇解读/P242.md) | 把部署后的真机轨迹转成优势标注的监督样本，经托管SFT接口迭代VLA，缓解权重封闭模型在接触操作中的任务适配不足。 | [原文](https://arxiv.org/abs/2607.29172) · [项目页](https://thomaschen98.github.io/clift/) |
| [POT-VLA：用持久三维物体Token闭环验证人形移动操作](论文逐篇解读/P241.md) | 将RGB-D观测更新为带任务角色的持久三维物体记录，把同一物体记忆用于VLA动作条件和动作后几何谓词验证，支持失败后的局部恢复。 | [原文](https://arxiv.org/abs/2607.18016) |
| [EATR-Stereo：让人形VLA按身体状态使用双目辅助证据](论文逐篇解读/P181.md) | 保留主视角Token并路由双目辅助特征，按身体历史调节视觉证据以支持遮挡下长程操作。 | [原文](https://arxiv.org/abs/2608.17453) |
| [EgoVLA：用手腕位姿和MANO手部参数连接人类视频与机器人动作](论文逐篇解读/P168.md) | 将第一视角人手恢复为腕部与MANO动作并结合机器人样本训练跨域操作模型。 | [原文](https://arxiv.org/abs/2507.12440) · [代码](https://github.com/catburgg/EgoVLA) · [项目页](https://rchalyang.github.io/EgoVLA/) |
| [G0.5：让推理与动作回到同一条自回归序列](论文逐篇解读/P162.md) | 以ActionCodec压缩异构动作，让单一自回归模型从视觉语言推理直接生成机器人动作token。 | [原文](https://arxiv.org/abs/2608.11739) · [代码](https://github.com/OpenGalaxea/GalaxeaVLA) · [项目页](https://opengalaxea.github.io/G05/) |
| [VINE：生成式控制策略的价值梯度后训练](论文逐篇解读/P184.md) | 重构流匹配去噪插值状态，使价值梯度可稳定优化生成策略，用于离线强化学习后训练。 | [原文](https://arxiv.org/abs/2607.10369) · [项目页](https://github.com/AgibotTech/vine) |
| [TANGO：从语言和第一视角图像预测人形全身导航动作](论文逐篇解读/P228.md) | 以仿真Plan–Edit–Track数据训练全身导航VLA，从语言和RGB历史预测人形关节动作，零样本部署到G1。 | [原文](https://arxiv.org/abs/2609.09158) |
| [TemporalFlow-VLA：用物理时序监督学习长时操作历史](论文逐篇解读/P240.md) | 从机器人状态和几何构造仅用于训练的表面时序流监督，以短、长时间查询压缩执行历史并送入VLA动作专家，部署时无需几何重建。 | [原文](https://arxiv.org/abs/2608.26821) |
| [TurboVLA：把视觉语言直接送入低延迟动作解码器](论文逐篇解读/P208.md) | 以紧凑视觉语言编码和动作解码器直接从视觉、语言与本体状态生成低延迟操作动作。 | [原文](https://arxiv.org/abs/2607.27205) · [代码](https://github.com/H-EmbodVis/TurboVLA) · [项目页](https://h-embodvis.github.io/TurboVLA/) |
| [VITRA：把无标注人类活动视频加工成VLA预训练片段](论文逐篇解读/P167.md) | 从日常视频提取手物运动轨迹作为中间表示，再用机器人数据适配操作动作空间。 | [原文](https://arxiv.org/abs/2510.21571) · [代码](https://github.com/microsoft/VITRA) |
| [Gemini Robotics：面向物理世界的通用机器人智能模型](论文逐篇解读/P061.md) | 将具身推理与视觉动作模型分级运行，并以少量本体数据适配机器人操作、规划和工具使用。 | [原文](https://deepmind.google/models/gemini-robotics/) |
| [GEN-0：跨本体真实操作数据驱动的通用机器人策略](论文逐篇解读/P172.md) | 统一多自由度机器人操作数据进行大规模预训练，再用少量目标任务数据后训练策略。 | [原文](https://generalistai.com/blog/gen-0) |
| [GR00T N1：面向通用人形机器人的基础模型](论文逐篇解读/P060.md) | 以视觉语言主干和扩散动作Transformer整合异构人形数据，并用本体专用编码接入身体控制接口。 | [原文](https://arxiv.org/abs/2503.14734) · [代码](https://github.com/NVIDIA/Isaac-GR00T) · [项目页](https://developer.nvidia.com/isaac/gr00t) |
| [LeVERB：基于潜在视觉语言指令的人形全身控制](论文逐篇解读/P062.md) | 从视频与动作学习视觉语言潜指令，由高层选取技能并让冻结低层策略执行人形全身动作。 | [原文](https://arxiv.org/abs/2506.13751) |
| [Phantom：先把人类示范改造成目标机器人看到的训练画面](论文逐篇解读/P169.md) | 将人手动作重定向至机器人并替换训练图像中的人臂外观，用于无机器人操作数据训练。 | [原文](https://arxiv.org/abs/2503.00779) · [代码](https://github.com/MarionLepert/phantom) · [项目页](https://phantom-human-videos.github.io/) |
| [WholeBodyVLA：面向全身移动操作控制的统一潜在VLA](论文逐篇解读/P097.md) | 从第一视角视频学习潜在动作token，由VLA预测双臂动作和移动命令，低层策略负责平衡执行。 | [原文](https://arxiv.org/abs/2512.11047) · [项目页](https://opendrivelab.com/WholeBodyVLA/) |
| [π0.5：具备开放世界泛化能力的视觉语言动作模型](论文逐篇解读/P059.md) | 分阶段对齐网页语义、多源机器人数据与长程移动操作，再训练连续动作头用于开放家庭任务。 | [原文](https://arxiv.org/abs/2504.16054) · [代码](https://github.com/Physical-Intelligence/openpi) · [项目页](https://www.physicalintelligence.company/blog/pi05) |
| [VLA Survey：具身智能视觉语言动作模型综述](论文逐篇解读/P071.md) | 按感知编码、语言推理、动作表示和部署组件分类视觉语言动作模型及其操作规划任务。 | [原文](https://arxiv.org/abs/2405.14093) |
| [EgoMimic：以共享姿态监督联合人类视频与机器人示范](论文逐篇解读/P170.md) | 人类和机器人数据共享姿态预测，仅在机器人样本训练动作头以扩展模仿学习和真机操作。 | [原文](https://arxiv.org/abs/2410.24221) · [代码](https://github.com/SimarKareer/EgoMimic) · [项目页](https://egomimic.github.io/) |
| [Octo：通用机器人策略](论文逐篇解读/P056.md) | 用块状注意力Transformer学习通用操作表示，以独立读出头适配新机器人的观测和动作。 | [原文](https://arxiv.org/abs/2405.12213) · [代码](https://github.com/octo-models/octo) · [项目页](https://octo-models.github.io/) |
| [OpenVLA：视觉语言动作模型](论文逐篇解读/P057.md) | 以双视觉编码器、离散动作token和LoRA微调构建视觉语言动作操作模型。 | [原文](https://arxiv.org/abs/2406.09246) · [代码](https://github.com/openvla/openvla) · [项目页](https://openvla.github.io/) |
| [π0：面向通用机器人控制的视觉语言动作流模型](论文逐篇解读/P058.md) | 由视觉语言主干提供语义条件、Flow Matching动作专家生成连续动作块，面向跨本体机器人操作。 | [原文](https://arxiv.org/abs/2410.24164) · [代码](https://github.com/Physical-Intelligence/openpi) · [项目页](https://www.physicalintelligence.company/blog/pi0) |
| [Diffusion Policy：基于动作扩散的视觉运动策略学习](论文逐篇解读/P050.md) | 以条件扩散生成连续操作动作块，滚动执行前缀并根据新视觉观测重规划，构成操作闭环。 | [原文](https://arxiv.org/abs/2303.04137) · [代码](https://github.com/real-stanford/diffusion_policy) · [项目页](https://diffusion-policy.cs.columbia.edu/) |
| [ACT / ALOHA：基于低成本硬件的精细双臂操作学习](论文逐篇解读/P051.md) | 用条件VAE与Transformer生成双臂操作动作块，并以时间集成平滑重叠预测。 | [原文](https://arxiv.org/abs/2304.13705) · [代码](https://github.com/tonyzhaozh/act) · [项目页](https://tonyzhaozh.github.io/aloha/) |
| [Open X-Embodiment：跨本体机器人学习数据集与RT-X模型](论文逐篇解读/P055.md) | 以统一协议保留本体差异并混合多机器人轨迹，训练和评估跨本体机器人操作策略。 | [原文](https://arxiv.org/abs/2310.08864) · [代码](https://github.com/google-deepmind/open_x_embodiment) · [项目页](https://robotics-transformer-x.github.io/) |
| [RT-2：将网络知识迁移到机器人控制的视觉语言动作模型](论文逐篇解读/P054.md) | 共同微调视觉语言任务与机器人轨迹，并将连续控制离散为动作token以研究语义迁移操作。 | [原文](https://arxiv.org/abs/2307.15818) · [项目页](https://robotics-transformer2.github.io/) |
| [RT-1：面向大规模真实世界控制的机器人Transformer](论文逐篇解读/P052.md) | 以TokenLearner压缩图像、Transformer预测离散动作token，学习真实机器人多任务操作策略。 | [原文](https://arxiv.org/abs/2212.06817) · [项目页](https://robotics-transformer1.github.io/) |

#### 相关项目

| 项目 | 主要用途 | 功能与特点 |
| --- | --- | --- |
| [ACoT-VLA](https://github.com/AgibotTech/ACoT-VLA) | 显式动作推理视觉语言动作模型 | 在视觉语言条件与动作输出之间加入任务相关的中间推理，组织长程操作目标和动作序列。 |
| [ACT](https://github.com/tonyzhaozh/act) | 模仿学习 | 以条件VAE和Transformer预测动作块，并通过时间集成平滑控制，连接双臂示范采集与策略部署流程。 |
| [Being-H0](https://github.com/BeingBeyond/Being-H0) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [BridgeVLA++](https://github.com/npucvr/BridgeVLA-Seq) | 带时空双记忆的操作策略 | 为BridgeVLA加入空间信息和时间记忆，提供预训练、真实机器人微调与评测，用于历史状态条件下的操作策略。 |
| [CLIFT](https://thomaschen98.github.io/clift/) | VLA与通用操作策略 | 把部署后的真机轨迹转成优势标注的监督样本，经托管SFT接口迭代VLA，缓解权重封闭模型在接触操作中的任务适配不足。 |
| [DeepThinkVLA](https://github.com/OpenBMB/DeepThinkVLA) | 强化动作推理的视觉语言动作模型 | 在视觉语言输入到动作输出间加入任务相关推理，关联复杂操作中的目标、状态与动作序列。 |
| [DIAL](https://github.com/xpeng-robotics/DIAL) | VLA与机器人策略 | 围绕多模态输入与机器人任务执行开展机器人学习研究。 |
| [Diffusion Policy](https://github.com/real-stanford/diffusion_policy) | 机器人策略 | 以条件扩散生成未来动作轨迹，由视觉和本体观测引导去噪，并通过滚动动作窗口执行闭环控制。 |
| [DiT4DiT](https://github.com/Mondo-Robotics/DiT4DiT) | VLA与机器人策略 | 联合视频DiT特征和流匹配动作头训练策略，提供LIBERO、RoboCasa-GR1配方及G1遥操作训练部署示例。 |
| [GalaxeaDP](https://github.com/OpenGalaxea/GalaxeaDP) | 星海图双臂移动操作扩散策略 | 以相机观测、机器人状态和任务条件生成连续动作块，提供双臂及移动操作扩散策略。 |
| [GalaxeaVLA](https://github.com/OpenGalaxea/GalaxeaVLA) | 星海图移动操作视觉语言动作模型 | 将视觉、语言和本体状态转为Galaxea机器人动作，并以Action Codec连接自回归推理与连续控制。 |
| [GraspVLA](https://github.com/PKU-EPIC/GraspVLA) | 开放场景六自由度抓取视觉语言动作模型 | 将视觉语言目标转为开放场景中的六自由度末端抓取动作，连接场景理解、抓取候选与机器人执行。 |
| [HEX](https://github.com/Open-X-Humanoid/HEX) | 跨本体人形全身VLA框架 | 对齐不同人形的身体状态槽位，以统一本体预测器和视觉语言条件生成动作，并由低层全身控制执行腿部命令。 |
| [HY-Embodied-0.5-VLA](https://github.com/Tencent-Hunyuan/Hy-Embodied-0.5-VLA) | 腾讯混元视觉语言动作模型 | 根据视觉、语言和机器人状态生成操作动作，提供HY-Embodied视觉语言策略模型与推理入口。 |
| [HY-Embodied-0.5-X](https://github.com/Tencent-Hunyuan/HY-Embodied-0.5-X) | 跨本体具身动作模型 | 以共享多模态表征和统一动作接口学习不同机器人数据，支持跨本体训练与适配。 |
| [Isaac-GR00T / GR00T N1.7](https://github.com/NVIDIA/Isaac-GR00T) | 人形基础模型 | GR00T N1.7以视觉语言主干和扩散动作头生成机器人动作，提供LeRobot后训练、推理及ONNX/TensorRT导出。 |
| [JALA](https://github.com/BeingBeyond/JALA) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [LingBot-VLA 1.0](https://github.com/Robbyant/lingbot-vla) | 早期跨本体视觉语言动作模型 | 早期跨本体视觉语言动作模型，提供训练、后训练、评测和部署入口，用于追踪LingBot-VLA版本演进。 |
| [LingBot-VLA 2.0](https://github.com/Robbyant/lingbot-vla-v2) | 跨本体视觉语言动作基础模型 | 将多类机器人和第一视角数据映射到统一状态动作向量，以稀疏专家学习跨本体策略并进行泛化评测。 |
| [Octo](https://github.com/octo-models/octo) | 通用策略 | 以Transformer和扩散动作头从多机器人数据学习通用策略，支持图像、语言、目标图像和模块化观测。 |
| [OpenDM](https://github.com/dexmal/opendm) | 开放世界机器人控制VLA | 根据语言、图像和机器人状态生成动作序列，支持开放指令、长时操作与动态干扰，并适配仿真和指定本体后训练。 |
| [openpi](https://github.com/Physical-Intelligence/openpi) | VLA | 提供流匹配π0、快速自回归π0-FAST和π0.5的检查点、数据配置、微调与推理服务。 |
| [OpenVLA](https://github.com/openvla/openvla) | VLA | 视觉语言模型根据图像和指令生成机器人动作，并连接RLDS数据混合、策略微调、推理与部署流程。 |
| [Pelican-VLA 0.5](https://github.com/Open-X-Humanoid/Pelican-VLA05) | 操作VLA中间版本 | 以共享视觉语言主干预测未来帧和动作，并用接触相关瓶颈Token连接感知与动作，研究跨场景和跨本体泛化。 |
| [Rethink_VLA](https://github.com/BeingBeyond/Rethink_VLA) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [RTR](https://github.com/tars-robotics/RTR) | VLA与机器人策略 | 在连续潜空间学习高频动作块，并以Reuse-then-Refine处理异步推理时动作块切换，维持接触操作连续性。 |
| [RynnVLA-001](https://github.com/alibaba-damo-academy/RynnVLA-001) | 第一代Rynn视觉语言动作模型 | 将语言任务、视觉观测和机器人状态映射为动作序列，构成Rynn系列早期通用操作基线。 |
| [RynnVLA-002](https://github.com/alibaba-damo-academy/RynnVLA-002) | 第二代通用机器人VLA | 根据视觉、语言和机器人状态预测操作动作，面向跨任务与跨本体泛化能力研究。 |
| [Spirit-v1.5](https://github.com/Spirit-AI-Team/spirit-v1.5) | 千寻智能具身操作基础模型 | 根据视觉、语言和机器人状态生成操作动作，面向多任务及真实场景泛化研究。 |
| [TurboVLA](https://github.com/H-EmbodVis/TurboVLA) | 不经大型语言模型中枢的动作生成 | 将视觉语言条件直接连接轻量动作策略，提供训练、评测和模型入口，面向无需大型语言模型中枢的动作生成。 |
| [UnifoLM-VLA-0](https://github.com/unitreerobotics/unifolm-vla) | 宇树视觉语言动作训练与部署框架 | 将LeRobot数据转换为HDF5和RLDS，连接多数据集训练、LIBERO评测、服务推理与G1部署。 |
| [UniT](https://github.com/xpeng-robotics/UniT) | VLA与机器人策略 | 小鹏机器人统一机器人学习研究项目，连接多模态观测与不同机器人任务输出。 |
| [video-prediction-policy](https://github.com/roboterax/video-prediction-policy) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [VIPA-VLA](https://github.com/BeingBeyond/VIPA-VLA) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [WALL-X](https://github.com/X-Square-Robot/WALL-X) | 通用机器人操作基础模型 | 以语言、视觉和机器人状态生成多任务操作动作，构成X Square通用机器人操作模型主线。 |
| [WholeBodyVLA](https://github.com/OpenDriveLab/WholebodyVLA) | 人形VLA | 从无动作标注的第一视角视频学习潜在动作，将视觉语言条件解码为双臂动作和运动命令，用于视频驱动的机器人动作生成。 |
| [X-Tokenizer](https://github.com/X-Square-Robot/X-Tokenizer) | 机器人动作统一离散表示 | 将不同机器人和任务的连续动作编码为序列Token并解码执行，为WALL系列提供统一动作表示。 |
| [Xiaomi-Robotics-0](https://github.com/XiaomiRobotics/Xiaomi-Robotics-0) | 小米机器人通用操作模型首版 | 以视觉、语言和本体状态生成操作动作，构成小米机器人通用操作模型首版基线。 |
| [Xiaomi-Robotics-1](https://github.com/XiaomiRobotics/Xiaomi-Robotics-1) | 小米机器人通用操作模型迭代版 | 扩展小米机器人模型的数据、操作任务与泛化评测，持续生成多任务机器人动作序列。 |
| [Xiaomi-Robotics-U0](https://github.com/XiaomiRobotics/Xiaomi-Robotics-U0) | 统一机器人动作基础模型 | 统一机器人观测和动作接口，吸收多任务、多本体数据并支持操作策略迁移与适配。 |
| [XR-1](https://github.com/Open-X-Humanoid/XR-1) | 统一视觉运动表征VLA框架 | 分阶段学习统一视觉运动离散表示、异构数据预训练和本体微调，提供LeRobot训练及多类机器人部署入口。 |
| [τ0-VLA](https://github.com/sii-research/tau-0-vla) | 分层任务规划体系的低层策略实现 | 面向τ0-VLA低层策略训练与推理并输出低层动作；高层提案、世界模型与价值规划需由外部模块完成。 |

## 世界动作模型（WAM）

结合未来世界预测与动作学习，用于机器人动作生成、规划和闭环控制。

#### 论文与技术报告

| 论文／报告 | 主要方法与用途 | 原文／代码 |
| --- | --- | --- |
| [DELE-w0.5：用未来状态辅助训练，部署时直接生成动作](论文逐篇解读/P193.md) | 训练时联合动作与未来视觉潜变量，部署时移除未来分支以直接生成双臂操作动作。 | [原文](https://arxiv.org/abs/2608.22067) · [项目页](https://deepleap-x.com/research/dele-w0.5) |
| [Fast-WAM：保留视频共训练，部署时跳过未来想象](论文逐篇解读/P198.md) | 保留训练期视频动作共训并在测试时跳过未来视频生成，比较世界动作模型直接控制与想象推演。 | [原文](https://arxiv.org/abs/2603.16666) · [代码](https://github.com/yuantianyuan01/FastWAM) · [项目页](https://yuantianyuan01.github.io/FastWAM/) |
| [Flex-π：让同一个世界动作模型按计算预算选择输出流](论文逐篇解读/P206.md) | 联合去噪RGB、三维、语义和动作流，并以流丢弃支持不同计算配置下的机器人操作推理。 | [原文](https://arxiv.org/abs/2608.10860) · [代码](https://github.com/geyan21/flex-pi) · [项目页](https://flex-pi.github.io/) |
| [GE-Act 2.0：用单步未来状态和行为兼容性训练WAM](论文逐篇解读/P195.md) | 结合控制导向表征、未来视觉规划和逆动力学利用异构数据，研究世界动作模型预训练与规模化。 | [原文](https://arxiv.org/abs/2609.05588) · [项目页](https://ge-act-v2.github.io/) |
| [Hydra-0：以图像动作流连接世界预测与机器人控制](论文逐篇解读/P202.md) | 以Action Flow连接视频预测与控制，并对齐人手、夹爪和不同机器人本体的视觉运动接口。 | [原文](https://arxiv.org/abs/2608.18077) · [代码](https://github.com/nvidia-isaac/video_to_data) · [项目页](https://nvidia-isaac.github.io/video_to_data/hydra-0/) |
| [LDA-1B：让不同质量的具身数据共同训练视觉预测与机器人动作](论文逐篇解读/P174.md) | 按数据监督字段组合策略、正逆动力学和视觉预测任务，学习潜在动力学并生成机器人动作块。 | [原文](https://arxiv.org/abs/2602.12215) · [代码](https://github.com/jiangranlv/LDA-1B) · [项目页](https://pku-epic.github.io/LDA/) |
| [ME-Dex 1.0：让世界动作模型联合预测视觉、触觉与动作](论文逐篇解读/P234.md) | ME-Dex把异构触觉映射到统一手部表示，并用视频、触觉和动作专家联合预测未来接触与动作，扩展世界动作模型的物理反馈。 | [原文](https://arxiv.org/abs/2609.21449) · [代码](https://github.com/MachEmbodied/ME-Dex-1.0) · [项目页](https://machembodied.com/ME-Dex/ME-Dex1.0.html) |
| [MotionWAM：面向实时人形移动操作的基座世界动作模型](论文逐篇解读/P081.md) | 以双DiT联合建模未来视觉和全身动作序列，面向实时人形移动操作与长程控制。 | [原文](https://arxiv.org/abs/2606.09215) |
| [Motus2：把策略、动作条件世界模型和价值评估放进一个闭环](论文逐篇解读/P197.md) | 共享策略、视觉模拟器和评估器，利用成功与失败交互支持灵巧操作候选规划和模型式学习。 | [原文](https://arxiv.org/abs/2608.30237v2) · [项目页](https://motus-robotics.github.io/motus2/) |
| [OpenWAM：把世界动作模型拆成可控的预训练实验](论文逐篇解读/P194.md) | 将视频骨干、动作专家、注意力和数据配方模块化，系统比较跨本体世界动作模型预训练设计。 | [原文](https://arxiv.org/abs/2609.07398) · [代码](https://github.com/OpenWAM-Official/OpenWAM) · [项目页](https://openwam-official.github.io/) |
| [Riemann-1.0：在同一因果模型中学习机器人动作与未来视觉](论文逐篇解读/P177.md) | 以因果Action/Video DiT共同建模未来视觉与机器人动作，并用本体专属头执行长程操作。 | [原文](https://riemann-dynamics.github.io/Riemann-1.0-Website/paper/Riemann-1.0.pdf) · [项目页](https://riemann-dynamics.github.io/Riemann-1.0-Website/) |
| [Rolling-WAM：跨重规划周期滚动细化世界与动作预测](论文逐篇解读/P227.md) | 在滑动窗口内跨重规划周期复用视频—动作去噪状态，以滚动想象降低WAM推理延迟并保持闭环操作表现。 | [原文](https://arxiv.org/abs/2609.30247) · [代码](https://github.com/zyinghua/Rolling-WAM) · [项目页](https://rolling-wam.github.io/) |
| [WAM-TTT：用无标注人类视频在部署前调整世界动作模型](论文逐篇解读/P173.md) | 通过观看无标注人类视频更新轻量快速记忆，条件化冻结世界动作模型执行跨本体操作。 | [原文](https://arxiv.org/abs/2607.06988) |
| [WholeBodyWAM：以统一全身控制语义扩展世界动作模型](论文逐篇解读/P226.md) | 保留预训练WAM视觉—操作先验，以56维统一全身控制语义和可操作性门控协调不同人形全身控制器。 | [原文](https://arxiv.org/abs/2609.16644) · [项目页](https://wholebodywam.github.io/) |
| [DreamZero：作为零样本策略的世界动作模型](论文逐篇解读/P113.md) | 联合自回归生成未来视觉与机器人动作，并以新观测滚动校正，用作零样本操作策略。 | [原文](https://arxiv.org/abs/2602.15922) · [代码](https://github.com/dreamzero0/dreamzero) · [项目页](https://dreamzero0.github.io/) |
| [World-Action Models 综述：从预测世界到生成可执行动作](论文逐篇解读/P211.md) | 从表示、转移建模、动作接口、架构、训练、数据和规模化整理机器人世界动作模型研究。 | [原文](https://arxiv.org/abs/2609.16074) · [项目页](https://rcl-robotics.github.io/Awesome-World-Action-Models/) |
| [Zero-WAM：让人类视频成为未见任务的上下文指令](论文逐篇解读/P186.md) | 把人类示范视频作为上下文任务条件，联合预测机器人未来视觉与动作而不更新模型参数。 | [原文](https://arxiv.org/abs/2608.26103) · [项目页](https://robbyant-research.github.io/Zero-WAM/) |
| [ZimaBlue：让大规模无动作视频进入可部署的WAM](论文逐篇解读/P196.md) | 以因果视频预训练、视频动作中训练和目标机器人后训练，把第一视角视频用于通用操作策略。 | [原文](https://arxiv.org/abs/2609.00188) · [项目页](https://github.com/ZimaBlue-WAM/ZimaBlue) |

#### 相关项目

| 项目 | 主要用途 | 功能与特点 |
| --- | --- | --- |
| [ABot-Manipulation](https://github.com/amap-cvlab/ABot-Manipulation) | 移动操作世界动作模型 | 联合建模移动操作中的世界表征、动作预测和评测，提供模型、推理与评测入口。 |
| [DreamZero](https://github.com/dreamzero0/dreamzero) | 世界动作模型项目 | 联合预测未来视觉和机器人动作，结合DROID与AgiBot数据进行训练和后训练，并通过WebSocket服务执行推理。 |
| [Fast-WAM](https://github.com/yuantianyuan01/FastWAM) | 视频先验迁移的动作模型训练 | 训练时联合视频与动作，推理时直接输出动作块；提供数据准备、训练脚本、模型及LIBERO和RoboTwin评测。 |
| [Flex-π](https://github.com/geyan21/flex-pi) | 支持多种观测组合的操作策略 | 组合RGB、几何和语义观测，通过冻结视频编码器与模态训练策略生成动作，提供训练、评测和部署实现。 |
| [GigaWorld-Policy](https://github.com/open-gigaai/giga-world-policy) | 动作中心世界模型策略 | 联合学习动作与环境变化表征，使世界模型表征直接服务动作选择与机器人策略训练。 |
| [Kairos](https://github.com/kairos-agi/kairos) | 跨本体世界动作模型 | 结合视频、人类行为和真实交互数据训练世界表征，联合预测未来视觉状态与机器人动作。 |
| [LDA-1B](https://github.com/jiangranlv/LDA-1B) | 世界动作模型官方实现 | 以多模态扩散Transformer联合建模动作块与未来视觉潜变量，用于动作生成和视觉预测评测。 |
| [LingBot-VA](https://github.com/Robbyant/lingbot-va) | 视频与动作联合世界模型 | 以双流Transformer联合建模视频潜变量和机器人动作，用于动作生成与未来视觉预测。 |
| [ME-Dex 1.0](https://github.com/MachEmbodied/ME-Dex-1.0) | 世界动作模型（WAM） | ME-Dex把异构触觉映射到统一手部表示，并用视频、触觉和动作专家联合预测未来接触与动作，扩展世界动作模型的物理反馈。 |
| [MotuBrain](https://github.com/shengshu-ai/MotuBrain) | 面向真实机器人的世界动作模型技术报告 | 以视频、动作和语言联合建模，面向多本体适配、长程机器人任务与实时闭环控制。 |
| [Motus](https://github.com/thu-ml/Motus) | 统一视频与动作的世界模型 | 在统一架构中学习视频动态、语言条件和机器人动作，兼顾未来环境表征与动作预测。 |
| [OpenWAM](https://github.com/OpenWAM-Official/OpenWAM) | 可配置的世界动作模型训练框架 | 以共享配置比较视觉编码、动作表示、注意力掩码和联合预测任务，提供世界动作模型训练、微调与部署入口。 |
| [Riemann-1.0](https://riemann-dynamics.github.io/Riemann-1.0-Website/) | 机器人世界动作模型技术报告与演示 | 在策略模式下由视觉和本体状态生成动作，在模拟模式下预测动作条件未来视觉，逐阶段对齐视频与机器人数据。 |
| [Rolling-WAM](https://github.com/zyinghua/Rolling-WAM) | 世界动作模型（WAM） | 在滑动窗口内跨重规划周期复用视频—动作去噪状态，以滚动想象降低WAM推理延迟并保持闭环操作表现。 |
| [UnifoLM-WMA-0](https://github.com/unitreerobotics/unifolm-world-model-action) | 宇树世界模型与动作框架 | 联合预测未来状态与动作序列，连接数据处理、训练、推理流程并适配G1部署。 |
| [WholeBodyWAM](https://wholebodywam.github.io/) | 世界动作模型（WAM） | 保留预训练WAM视觉—操作先验，以56维统一全身控制语义和可操作性门控协调不同人形全身控制器。 |
| [X-WAM](https://github.com/sharinka0715/X-WAM) | 跨本体世界动作模型 | 联合学习视频世界变化与机器人动作，在共享表征中支持跨本体操作和未来预测。 |
| [Zero-WAM](https://github.com/robbyant-research/Zero-WAM) | 世界动作模型项目页 | 以人类示范视频作为上下文任务指令，联合建模未来视觉与机器人动作，并通过人机配对数据迁移到未见操作任务。 |

## 世界模型与仿真生成

学习环境动态，进行未来预测、想象规划、交互模拟与合成数据生成。

#### 论文与技术报告

| 论文／报告 | 主要方法与用途 | 原文／代码 |
| --- | --- | --- |
| [DreamDojo：基于大规模人类视频的通用机器人世界模型](论文逐篇解读/P114.md) | 从大规模人类视频学习潜在交互动力学，再经机器人后训练与蒸馏用于操作预测和规划。 | [原文](https://arxiv.org/abs/2602.06949) · [代码](https://github.com/NVIDIA/DreamDojo) · [项目页](https://dreamdojo-world.github.io/) |
| [MachEmbodied-U0：协同任务理解、未来预测与动作生成](论文逐篇解读/P233.md) | ME-U0以理解专家预测子任务和交互区域，再与生成专家联合预测未来视觉状态及机器人动作，用多模态预训练支持操作策略。 | [原文](https://arxiv.org/abs/2609.25627) · [代码](https://github.com/MachEmbodied/ME-U0) · [项目页](https://machembodied.com/ME-U/ME-U0.html) |
| [Matrix-Game 3.5：用三维Patch记忆维持长时交互视频的一致性](论文逐篇解读/P178.md) | 以三维回投历史Patch和参考Token维持相机可控视频生成中的场景记忆与动态主体。 | [原文](https://matrix-game-v3-5.github.io/paper/Matrix-Game-3.5.pdf) · [代码](https://github.com/Riemann-Dynamics/Matrix-Game-3.5) · [项目页](https://matrix-game-v3-5.github.io/) |
| [WALL-SS：让动作条件世界模型持续推演，并用于筛选机器人策略](论文逐篇解读/P187.md) | 以尺度对齐动作条件和时间尺度记忆进行长程视频推演，评估机器人世界模型及策略。 | [原文](https://x2robot-open.oss-cn-shenzhen.aliyuncs.com/ARWM%20OPEN/WALL-SS.pdf) · [代码](https://github.com/X-Square-Robot/wall-ss) · [项目页](https://x2robot.com/pages/ss) |
| [Embodied World Model Survey：具身智能世界模型综合综述](论文逐篇解读/P072.md) | 从功能、时间建模和空间表示整理具身世界模型，涵盖状态估计、预测、生成与规划。 | [原文](https://arxiv.org/abs/2510.16732) · [代码](https://github.com/Li-Zn-H/AwesomeWorldModels) |
| [GigaWorld-0：作为具身智能数据引擎的世界模型](论文逐篇解读/P115.md) | 结合视频生成、三维场景、视角迁移和物理验证，构建具身合成轨迹及VLA训练数据。 | [原文](https://arxiv.org/abs/2511.19861) · [代码](https://github.com/open-gigaai/giga-world-0) · [项目页](https://giga-world-0.github.io/) |
| [GR00T-Dreams：面向人形机器人学习的合成轨迹生成](论文逐篇解读/P068.md) | 生成任务变化与未来视觉，再用逆动力学补充动作并经仿真或策略筛选人形合成轨迹。 | [原文](https://developer.nvidia.com/blog/enhance-robot-learning-with-synthetic-trajectory-data-generated-by-world-foundation-models/) |
| [V-JEPA 2：面向理解、预测与规划的自监督视频模型](论文逐篇解读/P067.md) | 先以掩码潜在预测学习视频表征，再用少量机器人数据训练动作条件世界模型和操控规划。 | [原文](https://arxiv.org/abs/2506.09985) · [代码](https://github.com/facebookresearch/vjepa2) · [项目页](https://ai.meta.com/vjepa/) |
| [UniSim：交互式真实世界模拟器学习](论文逐篇解读/P066.md) | 融合机器人、驾驶和互联网视频训练动作条件生成模型，用于交互式未来画面模拟与规划研究。 | [原文](https://arxiv.org/abs/2310.06114) · [项目页](https://universal-simulator.github.io/) |
| [DreamerV3：基于世界模型的跨领域通用控制](论文逐篇解读/P065.md) | 以离散潜变量、symlog和two-hot回归统一世界模型训练尺度，用于多域控制与泛化。 | [原文](https://arxiv.org/abs/2301.04104) · [代码](https://github.com/danijar/dreamerv3) |
| [Dreamer：基于潜在想象的行为学习](论文逐篇解读/P064.md) | 从交互数据学习潜在世界模型，在想象轨迹中训练Actor-Critic，再回到真实观测闭环控制。 | [原文](https://arxiv.org/abs/1912.01603) · [代码](https://github.com/danijar/dreamer) · [项目页](https://dreamrl.github.io/) |
| [PlaNet：基于像素输入的潜在动力学规划](论文逐篇解读/P063.md) | 以RSSM从像素学习潜在动力学，并用CEM搜索动作序列执行基于模型的控制与规划。 | [原文](https://arxiv.org/abs/1811.04551) · [项目页](https://planetrl.github.io/) |

#### 相关项目

| 项目 | 主要用途 | 功能与特点 |
| --- | --- | --- |
| [1xgpt](https://github.com/1x-technologies/1xgpt) | 世界模型与仿真生成 | 以当前观测和动作条件生成未来状态、视频或交互结果，为策略训练、评测和规划提供数据。 |
| [ABot-PhysWorld](https://github.com/amap-cvlab/ABot-PhysWorld) | 面向机器人交互的物理世界模型 | 联合视频、动作和状态建模接触与环境变化，连接合成数据、未来预测和机器人动作学习。 |
| [ABot-World](https://github.com/amap-cvlab/ABot-World) | 可持续交互的机器人世界模型 | 根据场景和交互输入持续生成未来世界，用于策略反复交互的视觉环境模拟。 |
| [AgiBotWorldChallengeICRA2026-WorldModelBaseline](https://github.com/AgibotTech/AgiBotWorldChallengeICRA2026-WorldModelBaseline) | 世界模型与仿真生成 | 根据当前观测和动作条件预测未来状态或视频，为策略训练、评测及规划提供世界模型基线。 |
| [Being-VL-0.5](https://github.com/BeingBeyond/Being-VL-0.5) | 世界模型与仿真生成 | 以当前观测和动作条件生成未来状态、视频或交互结果，为策略训练、评测和规划提供数据。 |
| [DreamDojo](https://github.com/NVIDIA/DreamDojo) | 机器人世界模型项目 | 先以大规模第一视角视频学习潜在动作，再用机器人数据后训练交互策略并蒸馏为实时模型。 |
| [EnerVerse-AC](https://github.com/AgibotTech/EnerVerse-AC) | 早期动作条件具身世界模型 | 根据机器人场景和动作条件生成未来视觉变化，是动作条件具身世界模型的早期实现。 |
| [GE-Sim 2.0](https://github.com/AgibotTech/GE-Sim-V2) | 具身世界模拟器 | 根据图像、本体状态和候选动作滚动预测未来视频与状态，并由独立策略服务开展闭环仿真评测。 |
| [Genie-Envisioner-V1](https://github.com/AgibotTech/Genie-Envisioner-V1) | 面向机器人学习的生成式世界模型 | 根据场景和动作条件生成机器人交互视频，为策略训练、数据扩增和未来状态预测提供环境样本。 |
| [GigaWorld-0](https://github.com/open-gigaai/giga-world-0) | 合成数据引擎项目 | 结合视频生成、三维高斯场景、系统辨识和规划模块，构建用于VLA训练的数据生成引擎。 |
| [GigaWorld-1](https://github.com/open-gigaai/giga-world-1) | 新一代具身世界模型 | 研究机器人动作条件下的未来环境生成与交互评测，为具身数据生成和策略训练提供可控世界变化。 |
| [LingBot-Video](https://github.com/Robbyant/lingbot-video) | 具身视频生成预训练模型 | 从文本或图像生成未来视频，支持稠密与MoE模型推理及提示词重写，用于具身视频预训练。 |
| [LingBot-World 1.0](https://github.com/Robbyant/lingbot-world) | 早期具身视频世界模型 | 根据文本、初始画面或动作生成未来视频，是LingBot长时交互世界模型的早期版本。 |
| [LingBot-World 2.0](https://github.com/Robbyant/lingbot-world-v2) | 长时交互视频世界模型 | 根据画面、文本和交互控制持续生成未来视频，并以Pilot和Director组织角色行为与环境事件。 |
| [MachEmbodied-U0 (ME-U0)](https://github.com/MachEmbodied/ME-U0) | 世界模型与仿真生成 | ME-U0以理解专家预测子任务和交互区域，再与生成专家联合预测未来视觉状态及机器人动作，用多模态预训练支持操作策略。 |
| [Matrix-Game 3.5](https://github.com/Riemann-Dynamics/Matrix-Game-3.5) | 相机可控长时交互视频世界模型 | 根据文本、初始画面、主体参考图和相机轨迹生成长时交互视频，结合场景记忆与渐进蒸馏。 |
| [OpenDW](https://github.com/dexmal/opendw) | 动作条件具身世界模型 | 以图像、语言、机器人状态和动作联合预测未来视频、动作与价值，用于动作条件回放和策略评估。 |
| [RoboTransfer](https://github.com/HorizonRobotics/RoboTransfer) | 世界模型与仿真生成 | 以当前观测和动作条件生成未来状态、视频或交互结果，为策略训练、评测和规划提供数据。 |
| [RynnWorld-4D](https://github.com/alibaba-damo-academy/RynnWorld-4D) | 时空一致的机器人世界模型 | 联合表示三维空间结构与时间演化，预测机器人动作后的场景变化及对象运动。 |
| [VideoWorld](https://github.com/ByteDance-Seed/VideoWorld) | 世界模型与视频预测 | 从无标注视频学习潜在动态与行为表示，为视觉运动规律和动作先验研究提供模型案例。 |
| [WALL-SS](https://github.com/X-Square-Robot/wall-ss) | 长时世界模型项目页 | 以长时世界模型对齐动作与视觉动态，并利用记忆和视觉动力学奖励评估机器人策略。 |
| [WALL-WM](https://github.com/X-Square-Robot/WALL-WM) | 面向机器人操作的世界模型 | 联合建模场景视频、机器人状态与动作，预测执行后的环境变化以支持操作策略训练。 |

## 具身理解与Agent规划

理解场景与任务，组织空间记忆、任务分解、技能调用和导航决策。

#### 论文与技术报告

| 论文／报告 | 主要方法与用途 | 原文／代码 |
| --- | --- | --- |
| [HoloAgent-0：具备三维空间记忆的统一具身智能体框架](论文逐篇解读/P082.md) | 以三维空间记忆、技能图和运行监控组织搜索、导航与移动操作，不直接控制关节。 | [原文](https://arxiv.org/abs/2606.23565) · [代码](https://github.com/HorizonRobotics/HoloAgent) · [项目页](https://horizonrobotics.github.io/robot_lab/holoagent) |
| [ME-Brain 1.0：用记忆、认知与动作积累可复用经验](论文逐篇解读/P231.md) | ME-Brain把机器人执行记录整理为分层记忆，由认知核心抽取可迁移技能，并让动作模型按事件检索经验完成后续操作。 | [原文](https://arxiv.org/abs/2609.24271) · [代码](https://github.com/MachEmbodied/ME-Brain-1.0) · [项目页](https://machembodied.com/ME-Brain/ME-Brain-1.0.html) |
| [ME-VLM：统一具身认知与多模态Agent协作](论文逐篇解读/P232.md) | ME-VLM把物理场景理解、空间与时序推理、Agent任务规划和执行结果检查统一训练，并提供适配端侧部署的4B版本。 | [原文](https://arxiv.org/abs/2609.24526) · [代码](https://github.com/MachEmbodied/ME-VLM) · [项目页](https://machembodied.com/ME-Brain/ME-VLM.html) |
| [Show-Harness：用语义动作接口让 VLM 闭环操作机械臂](论文逐篇解读/P210.md) | 以离散语义动作连接视觉语言模型和本体专用解释器，执行跨任务机械臂抓取放置。 | [原文](https://arxiv.org/abs/2609.10522) · [代码](https://github.com/showlab/Show-Harness) · [项目页](https://showlab.github.io/Show-Harness/) |
| [τ₀-VLA：用世界模型搜索组织长任务与低层动作](论文逐篇解读/P201.md) | 结合执行记忆、世界模型引导测试时搜索和反思策略，处理长程家庭移动操作任务。 | [原文](https://arxiv.org/abs/2608.16885) · [代码](https://github.com/sii-research/tau-0-vla) · [项目页](https://tau0-vla.github.io/) |
| [PaLM-E：具身多模态语言模型](论文逐篇解读/P053.md) | 将视觉与机器人状态嵌入语言模型上下文，用于具身规划、操作和导航，输出仍为语言层。 | [原文](https://arxiv.org/abs/2303.03378) · [项目页](https://palm-e.github.io/) |

#### 相关项目

| 项目 | 主要用途 | 功能与特点 |
| --- | --- | --- |
| [ABot-Navigation](https://github.com/amap-cvlab/ABot-Navigation) | 语言条件机器人导航系统 | 将语言目标和视觉场景转为导航决策，提供机器人底盘移动与目标到达的基准评测入口。 |
| [embodied-skill-kit](https://github.com/Open-X-Humanoid/embodied-skill-kit) | 机器人Agent与任务规划 | 根据语言任务与多模态环境状态生成技能调用或导航操作步骤，并结合执行反馈调整任务计划。 |
| [Fast-in-Slow](https://github.com/CHEN-H01/Fast-in-Slow) | VLA与机器人策略 | 以慢速系统规划任务并由快速策略执行操作，研究长时决策与实时动作的分层接口。 |
| [genisom_vln](https://github.com/zsibot/genisom_vln) | 机器人Agent与任务规划 | 根据语言任务与多模态环境状态生成技能调用或导航操作步骤，并结合执行反馈调整任务计划。 |
| [GigaBrain-0](https://github.com/open-gigaai/giga-brain-0) | 通用具身大脑模型 | 融合图像、点云、文本和本体状态，输出结构化任务规划与运动规划，连接生成数据和机器人执行。 |
| [GO-2](https://www.agibot.com/article/231/detail/56.html) | 具身规划与执行模型 | 以Action CoT生成宏观动作意图，再由低频语义规划和高频动作跟随器逐级细化执行。 |
| [HoloAgent](https://github.com/HorizonRobotics/HoloAgent) | 具身Agent与机器人系统栈 | 以AgentOS技能图、空间记忆和执行反馈组织机器人任务，并通过ROS 2连接导航、感知节点及多本体适配工具。 |
| [ME-Brain 1.0](https://github.com/MachEmbodied/ME-Brain-1.0) | 具身理解与Agent规划 | ME-Brain把机器人执行记录整理为分层记忆，由认知核心抽取可迁移技能，并让动作模型按事件检索经验完成后续操作。 |
| [ME-VLM](https://github.com/MachEmbodied/ME-VLM) | 具身理解与Agent规划 | ME-VLM把物理场景理解、空间与时序推理、Agent任务规划和执行结果检查统一训练，并提供适配端侧部署的4B版本。 |
| [MiniCPM-Robot](https://github.com/OpenBMB/MiniCPM-Robot) | 端侧机器人感知与决策工具集 | 提供端侧多模态模型的视觉跟踪、目标理解和动作决策接口，支持Jetson、ROS 2及机器人SDK集成。 |
| [OpenLoong-Brain](https://github.com/loongOpen/OpenLoong-Brain) | 任务规划与技能系统 | 将人形任务指令映射到可执行技能和机器人接口，提供技能调度、调用与执行框架。 |
| [Pelican-VL](https://github.com/Open-X-Humanoid/pelican-vl) | 人形机器人多模态具身大脑 | 从视觉语言输入形成空间理解、任务推理和高层动作目标，为下层策略或运动控制提供计划。 |
| [robocup_demo](https://github.com/BoosterRobotics/robocup_demo) | 机器人Agent与任务规划 | 根据语言任务与多模态环境状态生成技能调用或导航操作步骤，并结合执行反馈调整任务计划。 |
| [RxBrain-1.0](https://github.com/Tencent-Hunyuan/Hy-Embodied-RxBrain-1.0) | 机器人高层理解与任务决策模型 | 从视觉与语言形成场景理解和任务计划，为下层导航或机器人操作策略提供执行目标。 |
| [RynnBrain](https://github.com/alibaba-damo-academy/RynnBrain) | 机器人任务理解与规划模型 | 从视觉和语言形成场景理解与任务步骤，为VLA、导航和操作策略提供高层目标。 |
| [RynnEC](https://github.com/alibaba-damo-academy/RynnEC) | 具身认知与任务决策模型 | 研究多模态观测到环境理解、任务分解和行动决策的映射，连接认知规划与导航操作模块。 |
| [tron1-agent](https://github.com/limxdynamics/tron1-agent) | 机器人Agent与任务规划 | 根据语言任务与多模态环境状态生成技能调用或导航操作步骤，并结合执行反馈调整任务计划。 |
| [UrbanVLA](https://github.com/GalaxyGeneralRobotics/UrbanVLA) | 城市开放环境视觉语言导航模型 | 根据第一视角视觉与语言指令生成移动决策，面向室外及半开放城市环境导航。 |

## 训练、部署与评测工具

综合训练平台、本体适配、推理部署、数据处理与模型评测工具。

#### 论文与技术报告

| 论文／报告 | 主要方法与用途 | 原文／代码 |
| --- | --- | --- |
| [FluxVLA Engine：把策略实验接到真机闭环的工程平台](论文逐篇解读/P212.md) | 以配置化流程统一数据、模型、仿真评测、推理优化和机器人部署接口，支撑具身策略流程。 | [原文](https://arxiv.org/abs/2609.17210) · [代码](https://github.com/FluxVLA/FluxVLA) |
| [WorldArena：具身世界模型感知与功能效用统一评测基准](论文逐篇解读/P116.md) | 以视觉指标和数据生成、策略评价、动作规划任务共同评估具身世界模型的感知与功能效用。 | [原文](https://arxiv.org/abs/2602.08971) · [代码](https://github.com/tsinghua-fib-lab/WorldArena) · [项目页](https://world-arena.ai/) |

#### 相关项目

| 项目 | 主要用途 | 功能与特点 |
| --- | --- | --- |
| [DROID Policy Learning](https://github.com/droid-dataset/droid_policy_learning) | 真实数据学习 | 在robomimic上扩展DROID的RLDS数据读取、策略训练和评测流程，并提供可选真实机器人控制接口。 |
| [flexiv_trainer](https://github.com/flexivrobotics/flexiv_trainer) | 机器人学习训练平台 | 面向非夕机器人组织数据、训练与Physical AI技能开发流程，连接硬件接口和策略验证。 |
| [FluxVLA Engine](https://github.com/FluxVLA/FluxVLA) | VLA全链路工程平台 | 以统一配置连接LeRobot数据、策略训练、仿真评测和机器人接口，集成Fast-WAM、DiT4DiT及GR00T配方。 |
| [fourier-lerobot](https://github.com/FFTAI/fourier-lerobot) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [gr00t-agilex](https://github.com/agilexrobotics/gr00t-agilex) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [HY-Embodied](https://github.com/Tencent-Hunyuan/HY-Embodied) | 腾讯混元具身模型总入口 | 汇总HY-Embodied系列模型、数据、训练与评测入口，连接VLA、世界模型及跨本体项目。 |
| [lerobot-agilex](https://github.com/agilexrobotics/lerobot-agilex) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [magicbot-gen1_pi0_demo](https://github.com/MagiclabRobotics/magicbot-gen1_pi0_demo) | VLA与机器人策略 | 展示pi0类视觉语言策略接入MagicBot Gen1的模型、观测和机器人执行接口。 |
| [openpi-agilex](https://github.com/agilexrobotics/openpi-agilex) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [real-time-chunking-kinetix](https://github.com/Physical-Intelligence/real-time-chunking-kinetix) | VLA训练与部署 | 将实时动作分块与策略接口连接，接收视觉、语言和机器人状态并输出连续动作序列。 |
| [robotera_vla](https://github.com/roboterax/robotera_vla) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [RynnValue](https://github.com/alibaba-damo-academy/RynnValue) | 机器人轨迹价值评估模型 | 评估候选机器人动作或执行轨迹的价值，为策略选择、失败筛选和后训练提供反馈信号。 |
| [tron2_openpi](https://github.com/limxdynamics/tron2_openpi) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [unitree_lerobot](https://github.com/unitreerobotics/unitree_lerobot) | VLA训练与部署 | 将相机、语言和机器人状态输入策略生成动作块，再连接本体接口执行并回收任务结果。 |
| [WorldArena](https://github.com/tsinghua-fib-lab/WorldArena) | 世界模型功能评测 | 以感知指标和任务评测衡量世界模型能力，并在仿真与真实机器人上检查视频质量能否转化为策略收益。 |
| [wuji-openpi](https://github.com/wuji-technology/wuji-openpi) | VLA训练与部署 | 扩展OpenPI以支持双臂和双Wuji Hand，连接ROS 2示范、LeRobot转换、微调、策略服务及真机推理。 |

## 相关资料

- [技术与研究](README.md) · [书籍与课程](../强化学习开发者必备开源资料/书籍与课程.md)
