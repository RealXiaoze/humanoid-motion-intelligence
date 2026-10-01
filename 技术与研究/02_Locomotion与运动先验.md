# Locomotion与运动先验

> 自主移动、地形适应与运动先验，汇总相关论文、方法与项目。

当前收录 **55** 篇论文／技术报告、**78** 个项目。

## 本页导航

[基础行走与自然步态](#基础行走与自然步态) · [视觉与地形感知运控](#视觉与地形感知运控) · [技能表示与行为基座](#技能表示与行为基座) · [抗扰与保护性控制](#抗扰与保护性控制) · [训练框架与本体适配](#训练框架与本体适配) · [相关资料](#相关资料)

## 基础行走与自然步态

平衡、速度跟踪、走跑与运动适应，以及利用示范和运动先验学习自然步态。

**17** 篇论文／报告 · **9** 个项目

#### 论文与技术报告

| 论文／报告 | 主要方法与用途 | 原文／代码 |
| --- | --- | --- |
| [GaitSpan：从冻结行走策略扩展连续走跑能力](论文逐篇解读/P147.md) | 冻结行走策略并以动作波、SLIP事件塑形和残差策略扩展人形慢跑、跑步与地形移动。 | [原文](https://arxiv.org/abs/2607.12114) · [项目页](https://gaitspan2026.github.io/) |
| [Fly-Inspired Recurrent Controller：飞虫启发循环网络的人形机器人行走分析](论文逐篇解读/P339.md) | 论文分析固定T_graph检查点的神经状态—身体闭环：82维身体与命令输入经投影进入3,609维循环核心，由135个电机神经元标记状态读出15个关节目标，在MuJoCo G1上以50 Hz运行。控制器完成63项地形、速度和初始偏航组合中的61项；重置循环状态后标称偏航成功从19/21降为0/21。 | [原文](https://arxiv.org/abs/2609.27001) |
| [SMP：把动作扩散模型变成可复用的运动奖励](论文逐篇解读/P137.md) | 复用冻结扩散模型的运动分数作为SDS奖励，训练物理角色移动与风格控制技能。 | [原文](https://arxiv.org/abs/2512.03028) · [代码](https://github.com/xbpeng/MimicKit) · [项目页](https://yxmu.foo/smp-page/) |
| [State-Dependent AMP：基于状态相关对抗运动先验的统一行走、跑步与恢复](论文逐篇解读/P106.md) | 用状态门控选择走、跑和恢复运动先验，由同一PPO策略完成速度跟踪与人形真机控制。 | [原文](https://arxiv.org/abs/2605.18611) |
| [DBHL：基于ZMP奖励的无外部感知窄地形全身运动](论文逐篇解读/P129.md) | 将ZMP与角动量约束写入PPO奖励，以本体历史控制人形窄路、障碍和负载行走。 | [原文](https://arxiv.org/abs/2502.17219) · [项目页](https://whole-body-loco.github.io/) |
| [GMP：用生成式运动先验监督自然人形行走](论文逐篇解读/P136.md) | 由条件VAE生成未来动作参考并转为监督信号，训练可调速度的人形行走策略。 | [原文](https://arxiv.org/abs/2503.09015) · [项目页](https://sites.google.com/view/humanoid-gmp) |
| [Denoising World Model Locomotion：基于去噪世界模型的复杂地形人形运动控制](论文逐篇解读/P017.md) | 循环编码器以特权真值重建去噪潜状态，供PPO直接输出关节目标，用于人形地形行走。 | [原文](https://arxiv.org/abs/2408.14472) |
| [Real-World Humanoid Locomotion：基于强化学习的真实世界人形运动控制](论文逐篇解读/P014.md) | 以特权教师训练、历史Transformer学生适配Digit本体观测，输出关节PD目标用于真机行走与恢复。 | [原文](https://doi.org/10.1126/scirobotics.adi9579) · [项目页](https://learning-humanoid-locomotion.github.io/) |
| [DreamWaQ：基于隐式地形想象的鲁棒四足运动控制](论文逐篇解读/P125.md) | 从本体历史估计四足速度和地形潜变量，以PPO学习粗糙地面、台阶及户外行走。 | [原文](https://arxiv.org/abs/2301.10602) · [代码](https://github.com/Manaro-Alpha/DreamWaQ) · [项目页](https://sites.google.com/view/dreamwaq) |
| [AMP Locomotion：以对抗运动先验替代复杂奖励函数的四足运动控制](论文逐篇解读/P023.md) | 用对抗运动先验提供四足步态风格奖励，并以显式速度任务奖励训练移动策略。 | [原文](https://arxiv.org/abs/2203.15103) |
| [Rapid Locomotion：基于强化学习的高速运动控制](论文逐篇解读/P011.md) | 以二维命令课程扩展高速走跑范围，并从历史状态动作估计动力学潜变量用于真机控制。 | [原文](https://arxiv.org/abs/2205.02824) · [项目页](https://agility.csail.mit.edu/) |
| [AMP：面向风格化物理角色控制的对抗运动先验](论文逐篇解读/P022.md) | 以对抗判别器从动作数据学习短时运动先验，配合PPO控制物理角色的动作风格与移动。 | [原文](https://arxiv.org/abs/2104.02180) · [代码](https://github.com/nv-tlabs/ASE) · [项目页](https://xbpeng.github.io/projects/AMP/) |
| [Learning to Walk in Minutes：基于大规模并行深度强化学习的快速行走训练](论文逐篇解读/P010.md) | 用GPU并行PPO和渐进地形课程训练四足行走、越障与复杂地形适应策略。 | [原文](https://arxiv.org/abs/2109.11978) · [代码](https://github.com/leggedrobotics/legged_gym) |
| [RMA：面向腿式机器人的快速运动适应](论文逐篇解读/P009.md) | 从状态动作历史估计动力学潜变量，使腿式行走策略在部署时快速适应负载与地面变化。 | [原文](https://arxiv.org/abs/2107.04034) · [项目页](https://ashish-kmr.github.io/rma-legged-robots/) |
| [Challenging Terrain Locomotion：复杂地形四足运动控制学习](论文逐篇解读/P008.md) | 以特权教师和本体历史学生学习四足地形行走策略，通过接触反馈适应复杂地面。 | [原文](https://doi.org/10.1126/scirobotics.abc5986) |
| [Agile Motor Skills：面向腿式机器人的敏捷动态运动技能学习](论文逐篇解读/P007.md) | 结合执行器网络与域随机化训练腿式行走、跑步和恢复策略，并处理仿真到真机差异。 | [原文](https://doi.org/10.1126/scirobotics.aau5872) |
| [Sim-to-Real 2018：用执行器辨识与随机化跨越四足仿真差距](论文逐篇解读/P144.md) | 结合直流电机模型、延迟仿真、系统辨识和域随机化，训练四足走跑的Sim2Real策略。 | [原文](https://arxiv.org/abs/1804.10332) |

#### 相关项目

| 项目 | 主要用途 | 功能与特点 |
| --- | --- | --- |
| [AMP_mjlab](https://github.com/ccrpRepo/AMP_mjlab) | AMP人形控制实现 | 在MJLab提供G1地形AMP任务、动作转换、行走跑步与跌倒恢复训练及ONNX导出；实机状态由外部仓库接入。 |
| [DBHL窄地形全身运动](https://whole-body-loco.github.io/) | 本体感知复杂地形运动 | 仅依赖本体感觉在狭窄未知地形行走，以扩展ZMP和全身任务奖励约束落脚、躯干与摆臂。 |
| [DreamWaQ（社区实现）](https://github.com/Manaro-Alpha/DreamWaQ) | 感知运动复现 | 在Isaac Gym和legged_gym复现DreamWaQ式历史编码、速度估计与潜变量辅助盲走训练；未实现全部论文机制且无实机入口。 |
| [Fly-Inspired Recurrent Controller](https://arxiv.org/abs/2609.27001) | 基础行走与自然步态 | 论文分析固定T_graph检查点的神经状态—身体闭环：82维身体与命令输入经投影进入3,609维循环核心，由135个电机神经元标记状态读出15个关节目标，在MuJoCo G1上以50 Hz运行。控制器完成63项地形、速度和初始偏航组合中的61项；重置循环状态后标称偏航成功从19/21降为0/21。 |
| [Generative Motion Prior](https://sites.google.com/view/humanoid-gmp) | 生成式自然行走参考 | 以条件VAE在线生成重定向后的机器人未来参考，并训练速度策略跟踪，用于生成式自然行走控制。 |
| [Legged Lab DWAQ（Unitree G1）](https://gitee.com/chaomingsanhua/legged_lab) | 感知运动复现 | 在Legged Lab为G1复现DreamWaQ式历史VAE速度与环境潜变量估计并训练PPO盲走策略；缺少AdaBoot和实机通信链路。 |
| [ModelBasedFootstepPlanning-IROS2024](https://github.com/hojae-io/ModelBasedFootstepPlanning-IROS2024) | 模型落脚规划与无模型策略结合实现 | 以线性倒立摆模型生成速度目标对应的落脚参考，再训练无模型策略跟踪落脚和全身状态。 |
| [motion_imitation](https://github.com/erwincoumans/motion_imitation) | 四足参考动作模仿经典实现 | 将动物参考动作重定向到四足本体，以任务状态、动作相位和跟踪奖励学习步态与动态技能。 |
| [rl_amp](https://github.com/fan-ziqi/rl_amp) | legged_gym最小改动AMP实现 | 在legged_gym与rsl_rl中加入专家动作、AMP观测、判别器和先验奖励，构成最小改动的AMP实现。 |

[返回本页导航](#本页导航)

## 视觉与地形感知运控

利用视觉与地形信息调整运动，涵盖落脚、越障、跑酷和目标驱动移动。

**22** 篇论文／报告 · **16** 个项目

#### 论文与技术报告

| 论文／报告 | 主要方法与用途 | 原文／代码 |
| --- | --- | --- |
| [DAVIS：深度视觉驱动的人形足球技能](论文逐篇解读/P218.md) | 以头部深度图和本体历史端到端输出全身PD目标，使用可见性几何监督、真值渐进替换与AMP先验训练射门和盘带。 | [原文](https://arxiv.org/abs/2609.28175) · [项目页](https://thusi-lab.github.io/DAVIS/) |
| [Deep Whole-Body Parkour：基于深度强化学习的全身跑酷控制](论文逐篇解读/P020.md) | 将场景扫描与人体示范配对，以参考、本体历史和深度输入修正人形跑酷中的多接触时机。 | [原文](https://arxiv.org/abs/2601.07701) · [代码](https://github.com/project-instinct/InstinctLab/blob/main/source/instinctlab/instinctlab/tasks/shadowing/README.md) · [项目页](https://project-instinct.github.io/deep-whole-body-parkour/) |
| [DODGER：面向动态障碍导航的安全引导强化学习](论文逐篇解读/P367.md) | 把动态抛物CBF约束用作训练引导而非执行时安全过滤，策略在自身动作下采样并通过约束感知回报学习；MuJoCo全身仿真和Unitree G1激光雷达实机验证动态避障。 | [原文](https://arxiv.org/abs/2609.38873) · [代码](https://github.com/psh0823/dodger) · [项目页](https://psh0823.github.io/dodger-homepage/) |
| [DPL：以跨模态地形重建驱动深度感知人形运动](论文逐篇解读/P149.md) | 以深度合成、跨注意力地形重建和教师学生蒸馏，将深度输入映射为人形地形行走动作。 | [原文](https://arxiv.org/abs/2510.07152) |
| [FootQuery：未来落脚点引导的深度历史检索](论文逐篇解读/P216.md) | 根据本体状态预测每只脚的下一触地点，并从深度历史中检索相关区域，与全局视觉记忆融合生成关节动作。 | [原文](https://arxiv.org/abs/2609.21447) |
| [Generate, Track, Improve：强化学习微调的感知多技能人形运动](论文逐篇解读/P215.md) | 以深度条件流匹配生成全身参考、CLF-RL跟踪器执行，并用结构化搜索与AWR微调生成器，改善未见地形通过和技能选择。 | [原文](https://arxiv.org/abs/2609.31577) · [项目页](https://zolkin1.github.io/generate-track-improve/) |
| [Hiking in the Wild：面向真实复杂地形的可扩展感知跑酷](论文逐篇解读/P132.md) | 从深度检测地形边缘并约束足部落点，训练人形在台阶、空隙等复杂地形自主行走。 | [原文](https://arxiv.org/abs/2601.07718) · [代码](https://github.com/project-instinct/InstinctLab/blob/main/source/instinctlab/instinctlab/tasks/parkour/README.md) · [项目页](https://project-instinct.github.io/hiking-in-the-wild/) |
| [Vision-Driven Soccer：把不可靠视觉接入人形机器人反应式全身控制](论文逐篇解读/P182.md) | 将对象中心视觉、本体历史估计和关节控制合入强化学习策略，在仿真训练人形足球技能。 | [原文](https://arxiv.org/abs/2511.03996) · [代码](https://doi.org/10.5281/zenodo.21620490) · [项目页](https://humanoid-kick.github.io/) |
| [Light-Loco-Parkour：多专家蒸馏与无标签切换的视觉全身跑酷](论文逐篇解读/P150.md) | 以多技能专家、DAgger蒸馏和奖励微调训练人形依据深度与速度切换跳跃攀爬动作。 | [原文](https://arxiv.org/abs/2608.02653) · [项目页](https://light-loco-parkour.github.io/) |
| [NEXUS：让人体参考动作适应机器人所在的地形](论文逐篇解读/P362.md) | 生成地形适应参考训练特权教师，再把控制能力蒸馏到读取深度、本体历史与原始人体参考的学生；输出关节位置目标，在G1上执行楼梯、斜坡及全身遥操作。 | [原文](https://arxiv.org/abs/2609.39000) · [项目页](https://nexus-humanoid.github.io/) |
| [Perceptive BFM：面向机器人中心地形的人体运动先验适配](论文逐篇解读/P038.md) | 离线生成地形一致参考并蒸馏学生策略，以局部高度扫描修正人形动作跟踪和地形行走。 | [原文](https://arxiv.org/abs/2606.08059) · [项目页](https://acodedog.github.io/perceptive-bfm/) |
| [PHP：基于运动匹配与多教师蒸馏的感知人形跑酷](论文逐篇解读/P133.md) | 以运动匹配拼接人类跑酷技能并蒸馏跟踪专家，按深度和速度命令衔接障碍动作。 | [原文](https://arxiv.org/abs/2602.15827) · [项目页](https://php-parkour.github.io/) |
| [SOLO：稳定长时全地形感知人形运动](论文逐篇解读/P238.md) | 以查询式地形重建保留落脚相关细节，并用带未来状态分歧信用分配的蒸馏奖励训练仅依赖深度与本体感知的长时运动策略。 | [原文](https://arxiv.org/abs/2608.26583) · [项目页](https://sunpihai-up.github.io/solo/) |
| [WM-LOCO：世界模型增强的受限落足地形运动](论文逐篇解读/P217.md) | 将RSSM循环世界模型与PPO联合训练，以历史状态、动作和深度预测形成供人形运动策略使用的记忆特征。 | [原文](https://arxiv.org/abs/2609.02542) · [项目页](https://m0puppet.github.io/wm-loco/) |
| [X-Loco：基于协同策略蒸馏的视觉通用人形运动控制](论文逐篇解读/P128.md) | 分别训练移动、恢复和协调专家并按场景蒸馏，形成视觉速度条件的人形移动策略。 | [原文](https://arxiv.org/abs/2603.03733) · [项目页](https://x-loco-humanoid.github.io/) |
| [DreamPolicy：面向可扩展人形运动控制的统一世界模型策略](论文逐篇解读/P018.md) | 用地形条件扩散模型生成未来身体状态，并由统一策略跟踪以执行人形行走和地形适应。 | [原文](https://arxiv.org/abs/2505.18780) · [项目页](https://dreampolicy.github.io/) |
| [LEGO-H：面向复杂山径的人形机器人一体化技能学习](论文逐篇解读/P019.md) | 结合时序局部目标、特权运动教师和视觉学生，联合学习复杂山径导航与人形行走技能。 | [原文](https://arxiv.org/abs/2505.06218) · [项目页](https://lego-h-humanoidrobothiking.github.io/) |
| [MoRE：面向复杂地形拟人步态切换的残差专家混合策略](论文逐篇解读/P126.md) | 以基础地形策略配合残差专家和运动判别器，组合复杂地形通行与拟人步态控制策略。 | [原文](https://arxiv.org/abs/2506.08840) · [代码](https://github.com/TeleHuman/MoRE) · [项目页](https://more-humanoid.github.io/) |
| [Humanoid Parkour：人形机器人跑酷技能学习](论文逐篇解读/P016.md) | 以特权全身策略和DAgger视觉学生串联深度感知，用于人形多障碍跑酷。 | [原文](https://arxiv.org/abs/2406.10759) · [代码](https://github.com/ZiwenZhuang/parkour) · [项目页](https://humanoid4parkour.github.io/) |
| [Extreme Parkour：面向腿式机器人的极限跑酷控制](论文逐篇解读/P013.md) | 先用特权教师学习四足跑酷，再以深度视觉学生控制跨越、攀爬等复杂障碍动作技能。 | [原文](https://arxiv.org/abs/2309.14341) · [项目页](https://extreme-parkour.github.io/) |
| [Robot Parkour：基于软硬动力学约束课程的视觉跑酷学习](论文逐篇解读/P130.md) | 以软到硬动力学课程训练四足跑酷专家，再蒸馏为接收深度的多技能视觉策略。 | [原文](https://arxiv.org/abs/2309.05665) · [代码](https://github.com/ZiwenZhuang/parkour) · [项目页](https://robot-parkour.github.io/) |
| [Robust Perceptive Locomotion：面向野外四足机器人的鲁棒感知运动控制](论文逐篇解读/P012.md) | 融合带噪地形图与本体历史的循环策略，用于野外四足感知行走及感知失效时的反馈控制。 | [原文](https://arxiv.org/abs/2201.08117) |

#### 相关项目

| 项目 | 主要用途 | 功能与特点 |
| --- | --- | --- |
| [Click-and-Traverse](https://github.com/GalaxyGeneralRobotics/Click-and-Traverse) | 点击目标驱动的人形复杂地形移动 | 由视觉画面点击目标点，结合地形感知、导航和全身运动策略驱动人形机器人越障到达目标。 |
| [DAVIS](https://thusi-lab.github.io/DAVIS/) | 视觉与地形感知运控 | 以头部深度图和本体历史端到端输出全身PD目标，使用可见性几何监督、真值渐进替换与AMP先验训练射门和盘带。 |
| [Deep Whole-Body Parkour](https://project-instinct.github.io/deep-whole-body-parkour/) | 感知全身动作跟踪 | 将地形感知接入参考动作跟踪，以动作地形配对、深度修正和影子跟踪训练G1全身跑酷策略。 |
| [DODGER](https://github.com/psh0823/dodger) | 视觉与地形感知运控 | 把动态抛物CBF约束用作训练引导而非执行时安全过滤，策略在自身动作下采样并通过约束感知回报学习；MuJoCo全身仿真和Unitree G1激光雷达实机验证动态避障。 |
| [Generate, Track, Improve](https://zolkin1.github.io/generate-track-improve/) | 视觉与地形感知运控 | 以深度条件流匹配生成全身参考、CLF-RL跟踪器执行，并用结构化搜索与AWR微调生成器，改善未见地形通过和技能选择。 |
| [Hiking in the Wild](https://project-instinct.github.io/hiking-in-the-wild/) | 感知人形徒步 | 从原始深度生成G1动作，并以地形边缘、足部安全约束和平坦落脚区采样处理野外徒步。 |
| [Humanoid Parkour Learning](https://humanoid4parkour.github.io/) | 人形感知跑酷 | 以深度图和全身关节动作策略控制人形机器人跨越连续障碍，提供跑酷任务与对照实现。 |
| [MoRE](https://github.com/TeleHuman/MoRE) | 感知拟人Locomotion | 以共享基础策略和地形残差专家处理复杂地形行走，提供深度感知训练与MuJoCo部署。 |
| [NEXUS](https://nexus-humanoid.github.io/) | 视觉与地形感知运控 | 生成地形适应参考训练特权教师，再把控制能力蒸馏到读取深度、本体历史与原始人体参考的学生；输出关节位置目标，在G1上执行楼梯、斜坡及全身遥操作。 |
| [Perceptive Humanoid Parkour](https://php-parkour.github.io/) | 长时感知跑酷 | 拼接长程跑酷参考并训练多个跟踪专家，再蒸馏为接收深度和速度指令的G1策略。 |
| [Robot Parkour Learning](https://robot-parkour.github.io/) | 四足感知跑酷 | 将直接配点跑酷解转成强化学习课程，训练多个四足专家并蒸馏为适配A1与Go1部署的单一深度策略。 |
| [SOLO](https://sunpihai-up.github.io/solo/) | 视觉与地形感知运控 | 以查询式地形重建保留落脚相关细节，并用带未来状态分歧信用分配的蒸馏奖励训练仅依赖深度与本体感知的长时运动策略。 |
| [Vision-Driven Reactive Soccer Skills code and data](https://doi.org/10.5281/zenodo.21620490) | 论文复现代码与实验数据 | 以视觉驱动机器人足球技能，处理遮挡与球状态估计并生成关节轨迹。 |
| [VR-M3 视觉感知爬楼梯](https://vinrobotics.net/blog/perceptive-stair-locomotion) | 视觉运控实机案例 | 利用机载单摄像头感知前方地形、评估落脚点并调整步态；官方演示约60 kg人形携带5 kg载荷攀爬陌生楼梯，报告速度0.6 m/s和零样本仿真迁移。 |
| [WM-LOCO](https://m0puppet.github.io/wm-loco/) | 视觉与地形感知运控 | 将RSSM循环世界模型与PPO联合训练，以历史状态、动作和深度预测形成供人形运动策略使用的记忆特征。 |
| [X-Loco](https://x-loco-humanoid.github.io/) | 通用人形Locomotion | 训练多种地形专家并自适应选择教师，蒸馏为G1深度感知速度跟踪策略。 |

[返回本页导航](#本页导航)

## 技能表示与行为基座

学习可复用的运动表示，通过潜变量、目标或提示调用与组合行为。

**10** 篇论文／报告 · **6** 个项目

#### 论文与技术报告

| 论文／报告 | 主要方法与用途 | 原文／代码 |
| --- | --- | --- |
| [GPC：以离散运动Token预训练可适配的生成式控制器](论文逐篇解读/P159.md) | 将参考动作压成离散Token并训练自回归运动先验，支持角色控制、目标到达和轨迹跟随。 | [原文](https://arxiv.org/abs/2606.29148) · [代码](https://github.com/NVlabs/ProtoMotions) · [项目页](https://yi-shi94.github.io/gpc-page/) |
| [Locomotion-Grounded Humanoid Soccer：任务门控的多向人形踢球技能库](论文逐篇解读/P368.md) | 先训练全向Locomotion基座，再用任务模式门控七个视频重定向踢球技能并蒸馏为单策略；Unitree G1实机验证部分方向，仿真显示多方向覆盖与合并负迁移。 | [原文](https://arxiv.org/abs/2609.38852) |
| [P³：把边缘策略概率接回VAE与PPO之间](论文逐篇解读/P160.md) | 用矩匹配和潜变量采样估计VAE边缘策略概率，稳定PPO潜变量策略的具身行走训练。 | [原文](https://arxiv.org/abs/2607.25541) · [代码](https://github.com/ylyem9x/P3_Open) |
| [SkillX：人形足球统一多技能策略](论文逐篇解读/P219.md) | 以单一命令条件Actor配合技能专属对抗先验、价值头和球物体时序编码器，学习带球、停球、射门及其转换。 | [原文](https://arxiv.org/abs/2609.06718) · [项目页](https://yzc0731.github.io/SkillX/) |
| [BFM Survey：面向下一代人形全身控制的行为基座模型综述](论文逐篇解读/P070.md) | 按预训练监督、统一接口、适配方式和下游任务梳理人形行为基础模型与全身控制路线。 | [原文](https://arxiv.org/abs/2506.20487) |
| [BFM：人形机器人行为基座模型](论文逐篇解读/P036.md) | 以物理代理生成行为数据，再用掩码CVAE与在线蒸馏学习多种目标接口下的人形全身动作。 | [原文](https://arxiv.org/abs/2509.13780) · [项目页](https://bfm4humanoid.github.io/) |
| [BFM-Zero：基于无监督强化学习的可提示人形行为基座模型](论文逐篇解读/P080.md) | 以无监督强化学习构建共享行为潜空间，并用提示和条件运动先验连接跟踪、目标与奖励任务。 | [原文](https://arxiv.org/abs/2511.04131) · [代码](https://github.com/LeCAR-Lab/BFM-Zero) · [项目页](https://lecar-lab.github.io/BFM-Zero/) |
| [CALM：面向可控虚拟角色的条件对抗潜变量模型](论文逐篇解读/P025.md) | 从动作片段学习条件潜变量模型，让虚拟角色按示范运动分布选择并组合动作。 | [原文](https://arxiv.org/abs/2305.02195) · [项目页](https://research.nvidia.com/labs/par/calm/) |
| [PULSE：面向物理控制的通用人形运动表征](论文逐篇解读/P027.md) | 将多个SMPL仿真人跟踪教师蒸馏为状态条件潜策略，供下游复用动作技能。 | [原文](https://arxiv.org/abs/2310.04582) · [代码](https://github.com/ZhengyiLuo/PULSE) · [项目页](https://zhengyiluo.github.io/PULSE-Site/) |
| [ASE：面向物理仿真角色的大规模可复用对抗技能嵌入](论文逐篇解读/P024.md) | 以对抗判别器和潜变量学习可区分的物理角色技能嵌入，供动作跟踪与下游技能组合使用。 | [原文](https://arxiv.org/abs/2205.01906) · [项目页](https://xbpeng.github.io/projects/ASE/) |

#### 相关项目

| 项目 | 主要用途 | 功能与特点 |
| --- | --- | --- |
| [BFM-Zero](https://github.com/LeCAR-Lab/BFM-Zero) | 行为基座 | 以Forward-Backward无监督强化学习学习行为潜空间，再结合行为提示和条件运动先验训练并部署G1策略。 |
| [FLD](https://github.com/mit-biomimetics/fld) | 傅里叶潜在动力学运动表示实现 | 用傅里叶潜变量表示周期动作的频率、幅值和相位，再通过潜变量采样构造策略任务并生成运动。 |
| [Locomotion-Grounded Humanoid Soccer](https://arxiv.org/abs/2609.38852) | 技能表示与行为基座 | 先训练全向Locomotion基座，再用任务模式门控七个视频重定向踢球技能并蒸馏为单策略；Unitree G1实机验证部分方向，仿真显示多方向覆盖与合并负迁移。 |
| [PULSE](https://github.com/ZhengyiLuo/PULSE) | 动作表示 | 在物理人体控制器上学习潜在动作空间，由高层策略组合潜变量完成任务，研究可复用技能表示。 |
| [SkillX](https://yzc0731.github.io/SkillX/) | 技能表示与行为基座 | 以单一命令条件Actor配合技能专属对抗先验、价值头和球物体时序编码器，学习带球、停球、射门及其转换。 |
| [UFO](https://github.com/Roboparty/UFO) | 无监督人形行为框架 | 结合Forward-Backward与TeCH学习可提示的G1行为潜空间，并提供动作导入、目标定义、奖励和跟踪流程。 |

[返回本页导航](#本页导航)

## 抗扰与保护性控制

围绕抗扰稳定、失衡处理和保护性跌倒设计控制方法。

**5** 篇论文／报告 · **4** 个项目

#### 论文与技术报告

| 论文／报告 | 主要方法与用途 | 原文／代码 |
| --- | --- | --- |
| [DDC：支撑脚相对动态质心驱动的人形单腿平衡](论文逐篇解读/P335.md) | DDC 将质心位置与速度变换为支撑脚相对动态 CoM 观测，配合人体姿势控制奖励和 FastSAC 直接训练单腿平衡策略，并通过跨仿真评测选择部署检查点。 | [原文](https://arxiv.org/abs/2608.00500) · [项目页](https://estoil.github.io/DDC/) |
| [ADP：以对抗动力学分布训练人形抗扰运动](论文逐篇解读/P148.md) | 以轨迹优化数据学习对抗动力学先验，训练人形速度跟踪和推扰恢复而非逐帧模仿。 | [原文](https://arxiv.org/abs/2607.03454) · [项目页](https://seokju-lee.github.io/adp/) |
| [LocoWM：世界模型引导的高精度运动残差适应](论文逐篇解读/P365.md) | 动作条件世界模型根据本体历史与基策略动作预测任务状态序列，残差适配器提前修正；Go2-W完成地形调平、加速补偿与抗推实机演示，G1搬盘验证仅在仿真。 | [原文](https://arxiv.org/abs/2609.39179) · [代码](https://github.com/zhaozijie2022/LocoWM) · [项目页](https://zhaozijie2022.github.io/LocoWM/) |
| [PAC-MAN：感知约束下的人形全身安全躲避](论文逐篇解读/P336.md) | PAC-MAN 以分割掩码深度和本体状态驱动全身躲球策略，在训练期用逐连杆 CBF 安全奖励塑形，并以 AMP 人体躲避动作先验协调关节响应。 | [原文](https://arxiv.org/abs/2607.28623) · [代码](https://github.com/lzyang2000/perceptive_cbf_rl) · [项目页](https://lzyang2000.github.io/perceptive_cbf_rl/) |
| [SafeFall：人形机器人的保护性跌倒控制学习](论文逐篇解读/P108.md) | 以GRU预测不可避免跌倒，并由损伤感知保护策略控制落地，用于人形跌倒防护与恢复接口。 | [原文](https://arxiv.org/abs/2511.18509) · [项目页](https://safefall.github.io/) |

#### 相关项目

| 项目 | 主要用途 | 功能与特点 |
| --- | --- | --- |
| [DDC](https://estoil.github.io/DDC/) | 抗扰与保护性控制 | DDC 将质心位置与速度变换为支撑脚相对动态 CoM 观测，配合人体姿势控制奖励和 FastSAC 直接训练单腿平衡策略，并通过跨仿真评测选择部署检查点。 |
| [LocoWM](https://github.com/zhaozijie2022/LocoWM) | 抗扰与保护性控制 | 动作条件世界模型根据本体历史与基策略动作预测任务状态序列，残差适配器提前修正；Go2-W完成地形调平、加速补偿与抗推实机演示，G1搬盘验证仅在仿真。 |
| [PAC-MAN](https://github.com/lzyang2000/perceptive_cbf_rl) | 抗扰与保护性控制 | PAC-MAN 以分割掩码深度和本体状态驱动全身躲球策略，在训练期用逐连杆 CBF 安全奖励塑形，并以 AMP 人体躲避动作先验协调关节响应。 |
| [SafeFall](https://safefall.github.io/) | 保护性跌倒项目 | 用GRU判断跌倒是否不可避免，仅在触发后切换损伤缓解策略。 |

[返回本页导航](#本页导航)

## 训练框架与本体适配

各厂商与社区的训练实现，涵盖人形、四足、双轮足及多本体任务配置。

**1** 篇论文／报告 · **42** 个项目

#### 论文与技术报告

| 论文／报告 | 主要方法与用途 | 原文／代码 |
| --- | --- | --- |
| [Humanoid-Gym：面向人形机器人的零样本Sim2Real强化学习框架](论文逐篇解读/P015.md) | 整合PPO、域随机化、Isaac Gym训练、MuJoCo验证和XBot部署，面向人形行走Sim2Real。 | [原文](https://arxiv.org/abs/2404.05695) · [代码](https://github.com/roboterax/humanoid-gym) · [项目页](https://sites.google.com/view/humanoid-gym/) |

#### 相关项目

| 项目 | 主要用途 | 功能与特点 |
| --- | --- | --- |
| [agibot_x1_train](https://github.com/AgibotTech/agibot_x1_train) | 强化学习训练框架 | 组织仿真本体、观测、奖励和随机化配置，提供强化学习训练及运动策略回放入口。 |
| [AgileX Robot Lab](https://github.com/agilexrobotics/robot_lab) | 强化学习训练框架 | 组织仿真本体、观测、奖励和随机化配置，提供强化学习训练及运动策略回放入口。 |
| [atom-locomotion-training](https://github.com/embodied-dobot/atom-locomotion-training) | 强化学习训练框架 | 提供ATOM人形机器人的Locomotion强化学习训练环境、任务配置与策略训练入口。 |
| [Booster Gym](https://github.com/BoosterRobotics/booster_gym) | 人形RL训练与部署 | Booster T1与K1的训练部署项目，连接Isaac Gym或Isaac Lab、MuJoCo、Webots及机器人接口。 |
| [booster_train](https://github.com/BoosterRobotics/booster_train) | 强化学习训练框架 | 组织仿真本体、观测、奖励和随机化配置，提供强化学习训练及运动策略回放入口。 |
| [DeepRobotics RL Training](https://github.com/DeepRoboticsLab/RL_Training) | 云深处多本体强化学习训练框架 | 在Isaac Lab为Lite3、M20和DR02配置速度跟踪或AMP任务，统一RSL-RL训练、回放与多GPU入口。 |
| [engineai_amp](https://github.com/engineai-robotics/engineai_amp) | 强化学习训练框架 | 组织仿真本体、观测、奖励和随机化配置，提供强化学习训练及运动策略回放入口。 |
| [fourier_lab](https://github.com/FFTAI/fourier_lab) | 强化学习训练框架 | 组织仿真本体、观测、奖励和随机化配置，提供强化学习训练及运动策略回放入口。 |
| [Humanoid-Gym](https://github.com/roboterax/humanoid-gym) | 人形RL | 基于Isaac Gym训练人形速度跟踪策略，并提供MuJoCo仿真迁移与XBot实机接口，覆盖观测、奖励和随机化配置。 |
| [humanoid-lab](https://github.com/roboterax/humanoid-lab) | 强化学习训练框架 | 组织仿真本体、观测、奖励和随机化配置，提供强化学习训练及运动策略回放入口。 |
| [humanoid-rl-isaaclab](https://github.com/limxdynamics/humanoid-rl-isaaclab) | 强化学习训练框架 | 组织仿真本体、观测、奖励和随机化配置，提供强化学习训练及运动策略回放入口。 |
| [InternRobotics运动控制开源生态](https://github.com/InternRobotics) | 研究生态/项目合集 | InternRobotics运动控制项目集合，包含感知行走、全身模仿、遥操作和真机部署等不同仓库。 |
| [Isaac-RL-Two-wheel-Legged-Bot](https://github.com/jaykorea/Isaac-RL-Two-wheel-Legged-Bot) | 双轮足强化学习训练 | 为Flamingo双轮足提供Isaac Lab速度跟踪、PPO与CoRL训练及约束终止管理，可导出ONNX并进行MuJoCo仿真迁移。 |
| [isaac_asimov](https://github.com/menloresearch/isaac_asimov) | Asimov人形行走训练基线 | 提供Asimov 1的Isaac Lab速度行走PPO与AMP任务、分布式训练、检查点回放及ONNX导出。 |
| [legged_gym](https://github.com/leggedrobotics/legged_gym) | 腿式RL | 经典腿式强化学习基线，以并行地形、速度指令和关节位置动作训练步态，并结合噪声与动力学随机化覆盖Sim2Real差异。 |
| [LejuLab-Train](https://github.com/LejuRobotics/LejuLab-Train) | 强化学习训练框架 | 以Isaac Lab构建仿真机器人任务，将观测、奖励和随机化配置接入强化学习训练与策略回放。 |
| [LeTools-Learning](https://github.com/LejuRobotics/LeTools-Learning) | 强化学习训练框架 | 组织仿真本体、观测、奖励和随机化配置，提供强化学习训练及运动策略回放入口。 |
| [livelybot_pi_rl_baseline](https://github.com/HighTorque-Robotics/livelybot_pi_rl_baseline) | 强化学习训练框架 | 组织仿真本体、观测、奖励和随机化配置，提供强化学习训练及运动策略回放入口。 |
| [magiclab_rl_lab](https://github.com/MagiclabRobotics/magiclab_rl_lab) | 强化学习训练框架 | 为魔法原子机器人提供基于Isaac Lab的强化学习训练环境与任务配置。 |
| [Mini Pi Plus AMP](https://github.com/HighTorque-Robotics/Mini-Pi-Plus_AMP) | AMP运动训练框架 | 面向高擎Mini Pi Plus的AMP训练与仿真，连接Isaac Lab训练、MuJoCo验证和策略回放，用于运动策略研究。 |
| [noetix_e1_lab](https://github.com/Noetix-Robotics/noetix_e1_lab) | 强化学习训练框架 | 为E1人形提供Isaac Lab强化学习环境、任务配置和策略训练入口，覆盖仿真运动实验。 |
| [noetix_n2_gym](https://github.com/Noetix-Robotics/noetix_n2_gym) | 强化学习训练框架 | 为N2人形提供Isaac Gym训练环境、动作加载、AMP训练和Sim2Sim工具。 |
| [OpenLoong-Gymloong](https://github.com/loongOpen/OpenLoong-Gymloong) | 强化学习训练框架 | 提供青龙人形Isaac Gym训练环境和任务配置，用于Locomotion策略训练与Sim2Sim验证。 |
| [Project Instinct](https://project-instinct.github.io/) | 全身控制研究生态 | 由环境任务、PPO/AMP训练、G1板载推理和动作编辑工具组成的全身控制研究生态。 |
| [RoboOrchardLab](https://github.com/HorizonRobotics/RoboOrchardLab) | 强化学习训练框架 | 组织仿真本体、观测、奖励和随机化配置，提供强化学习训练及运动策略回放入口。 |
| [roboparty_train](https://github.com/Roboparty/roboparty_train) | 人形运动训练工作区 | 以子模块串联GMR动作准备、AMP与BeyondMimic训练、跑酷任务、ONNX导出及MuJoCo仿真验证。 |
| [Robot_Training_Cases](https://github.com/DeepRoboticsLab/Robot_Training_Cases) | 强化学习训练框架 | 组织仿真本体、观测、奖励和随机化配置，提供强化学习训练及运动策略回放入口。 |
| [TienKung-Lab](https://github.com/Open-X-Humanoid/TienKung-Lab) | 天工运动训练与部署框架 | 连接SMPL-X重定向、动作专家数据、Isaac Lab AMP训练、MuJoCo验证及天工ROS 2实机部署。 |
| [TITA RL](https://github.com/DDTRobot/tita_rl) | TITA强化学习训练与部署链 | 训练TITA四足与轮足策略并导出ONNX/TensorRT，连接Webots、ROS 2及Jetson实机推理接口。 |
| [topstar_rl_lab](https://github.com/MatrixZTlab/topstar_rl_lab) | H2自然步态AMP训练 | 以Isaac Lab和AMP训练H2自然步态，提供动作重定向、训练回放与诊断脚本。 |
| [TRON1 RL Isaac Gym](https://github.com/limxdynamics/tron1-rl-isaacgym) | 逐际动力TRON1强化学习训练框架 | 在legged_gym结构中配置TRON1点足、轮足和双足环境，训练PPO策略并导出模型。 |
| [tron2_rl_lab](https://github.com/limxdynamics/tron2_rl_lab) | 强化学习训练框架 | 组织仿真本体、观测、奖励和随机化配置，提供强化学习训练及运动策略回放入口。 |
| [Unitree RL Gym](https://github.com/unitreerobotics/unitree_rl_gym) | 人形/腿式RL | Unitree官方Isaac Gym时代的人形与腿式训练链，包含本体配置、PPO、MuJoCo验证和实机入口。 |
| [Unitree RL Lab](https://github.com/unitreerobotics/unitree_rl_lab) | 人形/腿式RL | 面向宇树Go2、H1和G1，连接Isaac Lab任务、策略导出、MuJoCo验证及实机SDK，贯通训练与部署流程。 |
| [Unitree RL Mjlab](https://github.com/unitreerobotics/unitree_rl_mjlab) | 人形/腿式RL | 基于MJLab和MuJoCo的轻量训练路线，覆盖速度行走、动作模仿、策略回放与真机接口。 |
| [VinRobotics mjlab](https://github.com/VinRobotics/vinrobotics_mjlab) | 厂商训练与部署 | 基于mjlab、MuJoCo Warp与RSL-RL训练M3.1速度跟踪策略，提供全身及12自由度下肢的平地/粗糙地形任务、多GPU训练、策略回放与ONNX导出。 |
| [VinRobotics mjlab deploy](https://github.com/VinRobotics/vinrobotics_mjlab_deploy) | 厂商训练与部署 | 在MuJoCo中加载M3.1模型与ONNX运动策略，通过Vinverse Connector接入运行流程，提供站立、行走和前后、侧向、转向命令的Sim2Sim验证。 |
| [Wheel-Legged-Gym](https://github.com/clearlab-sustech/Wheel-Legged-Gym) | 双轮足强化学习训练 | 基于legged_gym和rsl_rl训练双轮足，并以VMC适配开链或闭链机构，支持平地与粗糙地形任务。 |
| [Wheel-Legged-Lab](https://github.com/zyicome/Wheel-Legged-Lab) | 双轮足强化学习训练 | 以策略生成虚拟腿角度、腿长和轮速参考，再由VMC转为关节力矩，训练双轮足跳跃、落地与越障。 |
| [wheel_legged_genesis](https://github.com/Albusgive/wheel_legged_genesis) | 双轮足强化学习训练 | 在Genesis训练双轮足速度、转向、腿长和姿态策略，加入地形课程与随机化并提供MuJoCo回放。 |
| [wheelDog_RL](https://github.com/seer-robotics/wheelDog_RL) | 强化学习训练框架 | 仙工智能第一阶段轮足机器人强化学习项目，为轮足平台提供训练环境与策略实验入口。 |
| [Wiki-GRx-Gym](https://github.com/FFTAI/Wiki-GRx-Gym) | 强化学习训练框架 | 组织仿真本体、观测、奖励和随机化配置，提供强化学习训练及运动策略回放入口。 |

[返回本页导航](#本页导航)

## 相关资料

- [双轮足机器人训练开源方案表](双轮足机器人训练开源方案表.md)：训练框架、控制方式与任务能力。
- [Hugging Face Robotics Course](https://github.com/huggingface/robotics-course)：机器人学习课程与实践资料。
- [技术与研究](README.md) · [书籍与课程](../强化学习开发者必备开源资料/书籍与课程.md)
