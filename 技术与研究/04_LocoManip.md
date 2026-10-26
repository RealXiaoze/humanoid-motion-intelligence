# LocoManip

<!-- direction-links:start -->
研究方向入口：[物体交互与全身操作](研究方向_物体交互与全身操作.md)
<!-- direction-links:end -->

> 移动、平衡、接触与操作协同，汇总相关论文、方法与项目。

当前收录 **72** 篇论文／技术报告、**62** 个项目。

## 本页导航

[球类运动与动态接触](#球类运动与动态接触) · [视觉闭环与交互状态建模](#视觉闭环与交互状态建模) · [接触力控与负载适应](#接触力控与负载适应) · [全身协同与技能接口](#全身协同与技能接口) · [相关资料](#相关资料)

## 球类运动与动态接触

围绕来球感知与预测、击球时序、接触模仿和技能组合阅读。下表按实验平台区分机器人实机、物理仿真角色与评测环境；各项工作仍保留在对应方法分类中。

| 场景 | 实验平台 | 相关解读 |
| --- | --- | --- |
| 乒乓球 | 人形机器人实机 | [HITTER](论文逐篇解读/P472.md) · [PACE](论文逐篇解读/P473.md) · [SMASH](论文逐篇解读/P474.md) · [PingpongDuo](论文逐篇解读/P505.md) · [From Hitter to Player](论文逐篇解读/P506.md) |
| 乒乓球 | 机械臂与专用竞技平台 | [SpikePingpong](论文逐篇解读/P480.md) · [DeepMind乒乓球机器人](论文逐篇解读/P481.md) · [Sony Ace](论文逐篇解读/P482.md) |
| 网球 | 人形机器人实机 | [LATENT](论文逐篇解读/P376.md) · [AdaPT](论文逐篇解读/P191.md) · [ATHLETE](论文逐篇解读/P475.md) |
| 网球 | 轮椅底盘与机械臂 | [ESTHER](论文逐篇解读/P484.md) |
| 篮球与多任务交互 | 人形机器人实机 | [HumanX](论文逐篇解读/P098.md) · [HAIC](论文逐篇解读/P049.md) |
| 球类技能与动作组合 | 物理仿真角色 | [PhysHOI](论文逐篇解读/P476.md) · [SkillMimic](论文逐篇解读/P477.md) · [SkillMimic-V2](论文逐篇解读/P478.md) · [Vid2Player3D](论文逐篇解读/P479.md) · [物理乒乓球动画](论文逐篇解读/P483.md) |
| 多运动评测 | 仿真基准 | [SMPLOlympics](论文逐篇解读/P485.md) |

[返回本页导航](#本页导航)

## 视觉闭环与交互状态建模

利用视觉、物体状态与场景信息控制机器人交互。

**18** 篇论文／报告 · **11** 个项目

#### 论文与技术报告

| 论文／报告 | 主要方法与用途 | 原文／代码 |
| --- | --- | --- |
| [Dexterity-BEV：以鸟瞰空间对齐三维世界与操作动作](论文逐篇解读/P405.md) | 以多视角点云/顶点谱融合成共同BEV工作区，将机器人状态与SE(3)末端动作也映射到该坐标系，再由VLM条件下的flow-matching动作专家输出动作块；在LIBERO、RoboTwin 2.0和AgileX、DexForce W1、A1实机上测试。作者项目页是代码与资源入口，本登记不将其误标为DexForce公司GitHub。 | [原文](https://arxiv.org/abs/2606.02274) · [项目页](https://hnuzhy.github.io/projects/Dex-BEV) |
| [EgoHumanoid：基于机器人无关第一视角示范的野外移动操作](论文逐篇解读/P047.md) | 将第一视角示范重投影并转为末端增量和移动原语，再以少量真机数据锚定移动操作策略。 | [原文](https://arxiv.org/abs/2602.10106) · [代码](https://github.com/OpenDriveLab/EgoHumanoid) · [项目页](https://opendrivelab.com/EgoHumanoid) |
| [ForeTime-VLA：把未来动作线索蒸馏进因果抓取策略](论文逐篇解读/P200.md) | 从世界动作模型蒸馏因果未来潜变量与阶段信息，改善传送带抓取和接触时序控制。 | [原文](https://arxiv.org/abs/2608.20735) |
| [HAIC：基于动力学感知世界模型的敏捷人形物体交互控制](论文逐篇解读/P049.md) | 用对象中心世界模型递推物体位姿、速度和占据状态，并将预测作为策略输入执行物体交互。 | [原文](https://arxiv.org/abs/2602.11758) · [代码](https://github.com/ldt29/HAIC) · [项目页](https://haic-humanoid.github.io/) |
| [LadderMan：基于深度视觉的人形爬梯与梯上操作](论文逐篇解读/P330.md) | LadderMan 从单条参考动作学习不同梯具的攀爬专家，再以混合模仿与强化学习蒸馏为深度视觉闭环全身策略，并以双智能体实现梯上操作和平衡。 | [原文](https://arxiv.org/abs/2606.05873) · [代码](https://github.com/amazon-far/LadderMan) · [项目页](https://ladderman-robot.github.io/) |
| [LEGS：在具身高斯泼溅环境中免遥操作微调人形VLA](论文逐篇解读/P332.md) | 组合MuJoCo动态网格、3DGS真实场景背景与程序化全身动作，生成可重渲染的视觉示范，微调VLA并通过SONIC驱动G1移动与操作。 | [原文](https://arxiv.org/abs/2606.01458) · [项目页](https://legsvla.github.io/) |
| [OASIS：从仿真数据采集到真实人形移动操作](论文逐篇解读/P119.md) | 在Isaac Lab采集本体对齐轨迹并扩增视觉外观，训练迁移至真实G1的移动操作策略。 | [原文](https://arxiv.org/abs/2606.08548) · [代码](https://github.com/TeleHuman/OASIS) · [项目页](https://oasis-humanoid.github.io/) |
| [Sony Ace：以事件视觉与强化学习应对高速对抗](论文逐篇解读/P482.md) | 以主动像素相机测位置、事件视觉估旋转，再用仿真训练的非对称Actor-Critic生成短时击球动作，并由约束优化筛除碰撞风险、生成复位轨迹。论文记录了与精英及职业球员的比赛结果，但样本和赛事规则限定了结论范围。 | [原文](https://www.nature.com/articles/s41586-026-10338-5) · [项目页](https://ace.ai.sony/) |
| [Psi0：分阶段学习人形移动操作并接入全身控制](论文逐篇解读/P192.md) | 分阶段训练视觉语言动作模型与动作专家，并由低层控制器执行人形移动和灵巧操作。 | [原文](https://arxiv.org/abs/2603.12263) · [代码](https://github.com/physical-superintelligence-lab/Psi0) · [项目页](https://psi-lab.ai/Psi0/) |
| [Reflex：从机载视觉学习人形反应式接箱](论文逐篇解读/P490.md) | 先学习特权状态接箱控制，再通过潜变量对齐及带相机自运动历史的RGB-D编码实现视觉反应控制。 | [原文](https://arxiv.org/abs/2610.12772) |
| [SceneBot：接触提示的场景交互人形全身跟踪](论文逐篇解读/P094.md) | 从动作恢复场景并生成接触标签，以接触提示条件化人形跟踪器，区分支撑地面与交互对象。 | [原文](https://arxiv.org/abs/2606.27581) · [项目页](https://ericcsr.github.io/scenebot/) |
| [SMASH：机载视觉与可扩展全身动作的人形乒乓球控制](论文逐篇解读/P474.md) | Motion-VAE扩展G1可执行击球动作，双机载相机与自适应滤波估计来球和机器人状态；机载感知真球测试20次回球12次。 | [原文](https://arxiv.org/abs/2604.01158) · [项目页](https://mmlab.hk/Smash/) |
| [TouchGuide：用触觉引导推理时的接触操作](论文逐篇解读/P421.md) | 视觉运动策略先根据视觉观测生成粗略候选动作；任务专属接触物理模型融合视觉、触觉与候选动作，在扩散去噪或流匹配采样后期提供可行性梯度，引导动作贴合当前接触状态，无需重训基础策略。 | [原文](https://arxiv.org/abs/2601.20239) · [项目页](https://martelzhang.github.io/touchguide) |
| [DexGraspVLA：面向泛化灵巧抓取的视觉语言动作框架](论文逐篇解读/P416.md) | 高层视觉语言规划器把开放式指令转为目标物体与框选区域，SAM/Cutie 生成并跟踪掩码，冻结 DINOv2 表征和 diffusion action chunk 策略执行灵巧抓取；以 2,094 条示范训练，并在新物体、背景、照明及长程操作上实测。 | [原文](https://arxiv.org/abs/2502.20900) · [代码](https://github.com/Psi-Robot/DexGraspVLA) · [项目页](https://dexgraspvla.github.io/) |
| [DoorMan：面向人形像素到动作策略Sim2Real迁移的开门系统](论文逐篇解读/P092.md) | 以阶段重置训练特权开门教师，再经DAgger和GRPO优化RGB学生的像素到动作Sim2Real控制。 | [原文](https://arxiv.org/abs/2512.01061) · [代码](https://github.com/NVlabs/GR00T-VisualSim2Real) · [项目页](https://doorman-humanoid.github.io/) |
| [SpikePingpong：用快慢视觉校正高速击球](论文逐篇解读/P480.md) | 将RGB-D物理弹道预测与脉冲相机接触标签监督的快慢校正结合，并以约2,000条示范训练关节修正策略；在ABB机械臂上评估30厘米、20厘米容差内的目标落点与连续回击。 | [原文](https://arxiv.org/abs/2506.06690) · [代码](https://github.com/PKUHaoWang/SpikePingpong) |
| [VIRAL：面向人形移动操作的大规模视觉Sim2Real](论文逐篇解读/P093.md) | 以特权教师、DAgger学生和视觉随机化训练RGB人形策略，面向长程搬运与移动操作Sim2Real。 | [原文](https://arxiv.org/abs/2511.15200) · [代码](https://github.com/NVlabs/GR00T-VisualSim2Real) · [项目页](https://viral-humanoid.github.io/) |
| [VBC：面向腿式移动操作的视觉全身控制](论文逐篇解读/P043.md) | 由特权高层生成任务目标、视觉学生预测目标，再经低层全身控制执行腿式移动操作。 | [原文](https://arxiv.org/abs/2403.16967) · [项目页](https://wholebody-b1.github.io/) |

#### 相关项目

| 项目 | 主要用途 | 功能与特点 |
| --- | --- | --- |
| [#sudo R1](https://www.sudo.ai/) | 仿真训练通用操作系统 | 在仿真中以视觉观测条件策略执行连续物体操作；官方介绍策略每步根据最新观测闭环更新动作，观测条件动作频率为15至25Hz。 |
| [DexGraspVLA](https://github.com/Psi-Robot/DexGraspVLA) | 灵巧抓取视觉语言动作策略 | 高层视觉语言规划器把指令转成目标物体与区域，分割掩码跟踪保持抓取对象对应，冻结DINOv2视觉特征与扩散动作块控制器执行灵巧抓取；项目提供控制器训练、评测和推理记录入口。 |
| [DoorMan](https://doorman-humanoid.github.io/) | 视觉物理交互 | 以分阶段reset和PPO训练特权开门教师，通过DAgger蒸馏为RGB视觉学生，再用GRPO改善部分可观测性下的闭环行为。门体、把手动力学、材质、光照及相机参数随机化覆盖物理与视觉变化，策略在G1上完成开门与穿门。 |
| [LadderMan](https://github.com/amazon-far/LadderMan) | LocoManip | LadderMan 从单条参考动作学习不同梯具的攀爬专家，再以混合模仿与强化学习蒸馏为深度视觉闭环全身策略，并以双智能体实现梯上操作和平衡。 |
| [LEGS](https://legsvla.github.io/) | LocoManip与物理交互 | 组合MuJoCo动态网格、3DGS真实场景背景与程序化全身动作，生成可重渲染的视觉示范，微调VLA并通过SONIC驱动G1移动与操作。 |
| [OASIS](https://github.com/TeleHuman/OASIS) | 仿真数据采集 | 用PICO/XR遥操作在Isaac Lab记录G1移动操作轨迹，并将机器人头部相机画面实时送回操作者。离线回放利用PathTracing随机化纹理、光照和相机外参，生成多外观视觉训练数据；场景资产可由照片重建并导入。 |
| [Psi0](https://github.com/physical-superintelligence-lab/Psi0) | 人形VLA训练与分层执行 | 提供人类第一视角预训练、真机后训练、任务微调和动作块部署，连接SONIC遥操作、LeRobot数据与G1全身执行。 |
| [SceneBot](https://ericcsr.github.io/scenebot/) | 接触物理交互 | 以接触标签和条件提示统一地形、物体、障碍与自由空间交互，展示单一G1策略的场景适应能力。 |
| [SimToolReal](https://github.com/tylerlum/simtoolreal) | 跨工具灵巧操作参考 | 通过程序化工具几何与动力学随机化训练物体中心、目标条件的灵巧操作策略，在KUKA iiwa14与22自由度SHARPA手上跟踪六维工具目标姿态。SAPG训练支持跨未见工具、物体和目标轨迹迁移，视觉估计提供部署时的工具姿态。 |
| [SpikePingpong](https://github.com/PKUHaoWang/SpikePingpong) | 动态物体击球系统 | 官方仓库包含SONIC校正器训练、示范采集、IMPACT训练与部署入口。 |
| [VIRAL](https://viral-humanoid.github.io/) | 视觉物理交互 | 面向托盘搬运等人形交互任务训练RGB视觉策略，结合特权教师、视觉随机化和指尖系统辨识处理真机偏差。 |

[返回本页导航](#本页导航)

## 接触力控与负载适应

协调外力、柔顺控制、接触切换与负载变化。

**18** 篇论文／报告 · **19** 个项目

#### 论文与技术报告

| 论文／报告 | 主要方法与用途 | 原文／代码 |
| --- | --- | --- |
| [CEER2：面向人形移动操作的末端与根部方向可调柔顺](论文逐篇解读/P363.md) | 以固定的全身动作跟踪策略为底座，分层残差策略调节手端三轴刚度与根部抗力/阻尼；Isaac Sim训练后迁移Unitree G1，实机展示写字、负载拖曳和协作搬箱。 | [原文](https://arxiv.org/abs/2609.38709) · [项目页](https://ee-root-compliance.github.io/) |
| [HOIST：面向悬挂负载搬运的人形模仿学习与样本高效微调](论文逐篇解读/P331.md) | 以VR示范训练高层视觉语言动作策略，输出手部、头部与移动目标，由固定全身控制器操控悬挂负载；再从机器人交互学习动作流噪声修正，提高定位与停止精度。 | [原文](https://arxiv.org/abs/2606.00252) |
| [TF-ART：把触觉、力觉学习拆成可核验的闭环](论文逐篇解读/P205.md) | 综述触觉力觉感知、动作生成、动作修正和末端控制，覆盖接触操作与柔顺控制方法。 | [原文](https://arxiv.org/abs/2608.07558) · [项目页](https://lorenzo-0-0.github.io/tactile-force-survey/) |
| [HTD：从解耦身体控制、触觉示范到接触感知策略](论文逐篇解读/P180.md) | 以分离下肢控制维持基座，并用训练期力与触觉潜变量预测改进人形接触操作策略。 | [原文](https://arxiv.org/abs/2604.13015) · [代码](https://github.com/chrisyrniu/humanoid-touch-dream) · [项目页](https://humanoid-touch-dream.github.io/) |
| [SplitAdapter：基于因子化适配的负载感知人形移动操作](论文逐篇解读/P110.md) | 分别编码物体负载与本体动力学，再调制冻结策略层，适配人形搬运和Sim2Real任务。 | [原文](https://arxiv.org/abs/2606.03297) · [项目页](https://splitadapter.github.io/) |
| [SteadyTray：以残差强化学习稳定人形托盘运输](论文逐篇解读/P377.md) | 冻结步态基座训练残差以稳定托盘负载，再蒸馏编码器接入相机物体位姿；G1仿真评估变速、推机器人与推物体，真机展示多类负载运输和扰动恢复。 | [原文](https://arxiv.org/abs/2603.10306) · [代码](https://github.com/AllenHuangGit/steadytray) · [项目页](https://steadytray.github.io/) |
| [VisForce：指尖力视觉对齐与目标条件灵巧操作](论文逐篇解读/P353.md) | VisForce将腕部图像上的当前指尖力线索与示范检索得到的目标力图像送入目标条件交叉注意力，再沿π0.5的动作生成路径输出手臂与手部增量动作。在UR10与RH56F1上评估力条件抓取、插入、倾倒、工具转移和受控滑移任务。 | [原文](https://arxiv.org/abs/2609.25785) |
| [WT-UMI：把接触力纳入全身示范、规划与柔顺执行](论文逐篇解读/P140.md) | 以触觉和力监督修正人体示范的位姿与接触轨迹，再用导纳控制完成柔性及大件操作。 | [原文](https://arxiv.org/abs/2606.13232) · [项目页](https://wt-umi.github.io/WTUMI/) |
| [CHIP：基于后见扰动的人形自适应柔顺控制](论文逐篇解读/P086.md) | 将后见扰动转成条件目标，使全身策略按任务调节末端顺应，支持开门、擦拭和推车。 | [原文](https://arxiv.org/abs/2512.14689) · [项目页](https://nvlabs.github.io/CHIP/) |
| [DexNDM：用真实状态转移学习灵巧手的动力学残差](论文逐篇解读/P175.md) | 以仿真专家蒸馏通用策略，再用真机数据训练逐关节动力学和残差模型补偿手内旋转差异。 | [原文](https://arxiv.org/abs/2510.08556) · [项目页](https://meowuu7.github.io/DexNDM/) |
| [FACET：基于阻抗参考跟踪的腿式机器人力自适应控制](论文逐篇解读/P084.md) | 以质量－弹簧－阻尼参考和策略跟踪实现外力适应，主要面向四足接触与负载交互。 | [原文](https://arxiv.org/abs/2505.06883) · [项目页](https://facet.pages.dev/) |
| [FALCON：力自适应人形移动操作学习](论文逐篇解读/P044.md) | 以双策略共享身体状态并从本体历史适应外力，协调人形搬运、推拉和开门动作。 | [原文](https://arxiv.org/abs/2505.06776) · [代码](https://github.com/LeCAR-Lab/FALCON) · [项目页](https://lecar-lab.github.io/falcon-humanoid/) |
| [GentleHumanoid：面向富接触人机与物体交互的上半身柔顺学习](论文逐篇解读/P083.md) | 以弹簧式交互参考和强化学习调节上身顺应，用于人机接触、物体操作及全身柔顺控制。 | [原文](https://arxiv.org/abs/2511.04679) · [项目页](https://gentle-humanoid.axell.top/) |
| [Hold My Beer / SoFTA：柔和人形运动与末端稳定控制学习](论文逐篇解读/P087.md) | 以低频下肢和高频上肢策略分工稳定基座与末端，面向轻柔行走和手持物稳定。 | [原文](https://arxiv.org/abs/2505.24198) · [代码](https://github.com/LeCAR-Lab/SoFTA) · [项目页](https://lecar-lab.github.io/SoFTA/) |
| [MSDP：用多传感器动态预训练提升接触操作强化学习](论文逐篇解读/P379.md) | 通过多传感器掩码重建和动作条件下一观测预测学习融合表征，再以交叉注意力Critic及池化Actor接入强化学习；在仿真与Franka插销、推块任务及扰动条件下验证。 | [原文](https://arxiv.org/abs/2511.14427) · [项目页](https://msdp-pearl.github.io/) |
| [SoftMimic：从示例学习柔顺全身控制](论文逐篇解读/P085.md) | 从逆运动学生成的受力响应样本学习柔顺全身控制，用于扰动吸收、安全交互和恢复。 | [原文](https://arxiv.org/abs/2510.17792) · [代码](https://github.com/Improbable-AI/softmimic) · [项目页](https://gmargo11.github.io/softmimic/) |
| [Thor：面向强接触环境的人类启发全身反应](论文逐篇解读/P112.md) | 以分区Actor-Critic和力自适应躯干倾斜奖励协调腰腿与手臂，执行强接触人形交互。 | [原文](https://arxiv.org/abs/2510.26280) · [项目页](https://baai-aether.github.io/baai-thor/) |
| [PhysHOI：用接触关系奖励学习全身人—物交互](论文逐篇解读/P476.md) | 以人体、物体运动及二值接触图构造统一交互模仿奖励，用PPO训练物理仿真人形角色完成抓取和篮球交互。 | [原文](https://arxiv.org/abs/2312.04393) · [代码](https://github.com/wyhuai/PhysHOI) · [项目页](https://wyhuai.github.io/physhoi-page/) |

#### 相关项目

| 项目 | 主要用途 | 功能与特点 |
| --- | --- | --- |
| [CEER2](https://ee-root-compliance.github.io/) | 接触力控与负载适应 | 以固定的全身动作跟踪策略为底座，分层残差策略调节手端三轴刚度与根部抗力/阻尼；Isaac Sim训练后迁移Unitree G1，实机展示写字、负载拖曳和协作搬箱。 |
| [CHIP](https://nvlabs.github.io/CHIP/) | 柔顺控制项目 | 利用后见式扰动把外力位移转成跟踪目标，使策略在顺应和姿态恢复间调节刚度。 |
| [dexrobot_ecosystem](https://github.com/DexRobot/dexrobot_ecosystem) | 灵巧手开发与仿真平台 | 整合灵巧手控制、运动学、URDF、Isaac Sim、MuJoCo和ROS兼容层，连接硬件、仿真与算法开发。 |
| [FACET](https://facet.pages.dev/) | 柔顺控制项目 | 把虚拟质量、弹簧和阻尼系统的短时响应作为强化学习目标，研究外力与接触下的可控阻抗行为。 |
| [GentleHumanoid](https://github.com/Axellwppr/gentle-humanoid) | 柔顺控制项目 | 以带上身柔顺和可调力阈值的全身跟踪策略协调肩、肘、腕对外力的响应，处理阻抗接触和人类引导动作。部署工具通过MuJoCo仿真与Unitree SDK2连接G1，支持参考动作切换及运行时力阈值调节。 |
| [HOIST](https://arxiv.org/abs/2606.00252) | LocoManip与物理交互 | 先用VR示范微调高层VLA，输出双手、头部、导航及机身高度目标，由固定全身控制器执行悬挂负载操作；随后冻结VLA，以交互rollout训练actor-critic，按状态选择流匹配动作专家的初始噪声向量，改善负载定位与停止表现。 |
| [humanoid-touch-dream](https://github.com/chrisyrniu/humanoid-touch-dream) | 具身操作策略与数据采集 | 连接解耦身体控制、VR遥操作、多视角触觉数据、HTD行为克隆和真机执行；部署时仅保留动作策略。 |
| [linkerhand-sim](https://github.com/linker-bot/linkerhand-sim) | 灵巧手仿真与操作 | 提供LinkerHand灵巧手仿真环境，用于验证抓取、手部控制和操作策略。 |
| [MSDP](https://msdp-pearl.github.io/) | 接触力控与负载适应 | 通过多传感器掩码重建和动作条件下一观测预测学习融合表征，再以交叉注意力Critic及池化Actor接入强化学习；在仿真与Franka插销、推块任务及扰动条件下验证。 |
| [PhysHOI](https://github.com/wyhuai/PhysHOI) | 物理仿真人形交互技能 | 以接触图奖励驱动物理角色模仿全身抓取和篮球人—物交互。 |
| [RevoLab](https://github.com/BrainCoTech/RevoLab) | 仿真与灵巧手训练 | 为Revo3提供Isaac Lab环境、机器人资产和预训练策略，覆盖手内重定位、姿态调整、物体旋转、抬举与动态交接；训练与部署目录对应RSL-RL、RL Games及HORA/ProprioAdapt等路径。 |
| [SoFTA / Hold My Beer](https://github.com/LeCAR-Lab/SoFTA) | 末端稳定项目 | 将下肢平衡与上肢末端稳定分为不同控制带宽，以协调行走和手持物任务中的基座扰动补偿。 |
| [SoftMimic](https://gmargo11.github.io/softmimic/) | 柔顺控制项目 | 将刚性示范扩增为动力学可行的柔顺响应，再训练策略跟踪响应分布，覆盖数据处理、训练与部署。 |
| [SplitAdapter](https://splitadapter.github.io/) | 负载适配项目 | 分离编码负载变化与机器人动力学变化，并以世界模型和分层FiLM适配G1负载操作。 |
| [SteadyTray/ReST-RL](https://github.com/AllenHuangGit/steadytray) | 接触力控与负载适应 | 冻结步态基座训练残差以稳定托盘负载，再蒸馏编码器接入相机物体位姿；G1仿真评估变速、推机器人与推物体，真机展示多类负载运输和扰动恢复。 |
| [Thor](https://baai-aether.github.io/baai-thor/) | 强接触控制项目 | 协调上肢、腰部和下肢应对强外力与负载变化，利用躯干倾斜目标调节承重和步态。 |
| [VisForce](https://arxiv.org/abs/2609.25785) | 接触力控与负载适应 | VisForce将腕部图像上的当前指尖力线索与示范检索得到的目标力图像送入目标条件交叉注意力，再沿π0.5的动作生成路径输出手臂与手部增量动作。在UR10与RH56F1上评估力条件抓取、插入、倾倒、工具转移和受控滑移任务。 |
| [WT-UMI](https://wt-umi.github.io/WTUMI/) | 触觉示范与柔顺执行 | 以可穿戴触觉接口采集人体示范和机器人接触反馈，力监督规划末端轨迹，再以触觉导纳闭环执行。 |
| [wuji-mjlab](https://github.com/wuji-technology/wuji-mjlab) | 强化学习训练与实机部署 | 基于mjlab训练Wuji Hand手内旋转策略，提供PPO训练与Sim2Real部署入口。 |

[返回本页导航](#本页导航)

## 全身协同与技能接口

联合移动、平衡、上肢与手部完成操作任务。

**36** 篇论文／报告 · **32** 个项目

#### 论文与技术报告

| 论文／报告 | 主要方法与用途 | 原文／代码 |
| --- | --- | --- |
| [MPC-RL：用并行质心动力学优化引导人形全身策略学习](论文逐篇解读/P333.md) | 用并行GPU质心动力学MPC生成结构化奖励训练PPO，关节策略部署时独立执行，在Themis V2上验证行走、抗扰与推箱移动操作。 | [原文](https://arxiv.org/abs/2606.05687) · [代码](https://github.com/junhengl/mpc-rl) |
| [ATHLETE：轨迹引导动作匹配与反应式人形网球策略](论文逐篇解读/P475.md) | TGMM把LAFAN1步态与公开视频恢复的正反手动作拼成可执行参考，再用时限自适应教师、DAgger学生和PPO训练反应式G1策略。 | [原文](https://arxiv.org/abs/2610.13572) · [代码](https://anonymous.4open.science/r/athlete-humanoid-tennis) · [项目页](https://hazintihoa.github.io/athlete.github.io/) |
| [CEER：面向分层人形移动操作的柔顺末端与根部统一控制接口](论文逐篇解读/P095.md) | 以末端位姿、基座速度和根状态构成低维接口，由柔顺全身策略执行接触操作与移动任务。 | [原文](https://arxiv.org/abs/2605.19981) · [代码](https://github.com/stevenryanrobot/ceer_deploy) · [项目页](https://robotproject8.github.io/ceer_page/) |
| [CoorDex：用身体与手部先验降低连续灵巧移动操作难度](论文逐篇解读/P139.md) | 分别蒸馏身体和灵巧手动作先验，再在潜在动作空间学习协同残差以完成连续移动抓取。 | [原文](https://arxiv.org/abs/2606.23680) · [代码](https://github.com/Skevinci/coordex) · [项目页](https://skevinci.github.io/coordex/) |
| [DECOWAM：用未来蒸馏与动作解耦适配腿式移动操作](论文逐篇解读/P199.md) | 以未来瓶颈和底盘－手臂因子分解区分相机自运动与机械臂动作，面向腿式移动操作。 | [原文](https://arxiv.org/abs/2608.20114) |
| [DPC：从视觉语义直接生成可执行全身关节目标](论文逐篇解读/P164.md) | 取消中间运动目标接口，让视觉、语言、本体与执行反馈直接生成关节和手部动作。 | [原文](https://symbiosis-robotics.com/research/dpc/en/) |
| [FARO：面向可行性的机器人运动优化](论文逐篇解读/P239.md) | 围绕候选接触序列构建由便宜到昂贵的运动学与动力学可行性筛选层，并与接触模式树搜索结合以生成可执行的人形全身操作轨迹。 | [原文](https://arxiv.org/abs/2607.18362) · [项目页](https://atarilab.github.io/faro.io/) |
| [From Hitter to Player：用落点命令分开训练击球执行与对抗策略](论文逐篇解读/P506.md) | 以落点坐标连接物理击球规划、29关节全身策略和高层选点；先适应连续回合，再冻结执行层学习对抗策略。 | [原文](https://arxiv.org/abs/2610.14067) · [项目页](https://mufanmufan.github.io/hitter-to-player/) |
| [HANDOFF：基于互补教师蒸馏的人形智能体任务空间全身控制](论文逐篇解读/P111.md) | 将互补移动、操作和恢复教师蒸馏为MoE策略，把低维任务空间命令转成人形全身动作。 | [原文](https://arxiv.org/abs/2606.06493) · [代码](https://github.com/lzyang2000/HANDOFF) · [项目页](https://lzyang2000.github.io/HANDOFF/) |
| [HumanX：基于人类视频的敏捷可泛化人形交互技能](论文逐篇解读/P098.md) | 将人类视频恢复为人－物交互轨迹并扩增，再以统一模仿学习训练球类、搬运和交互技能。 | [原文](https://arxiv.org/abs/2602.02473) · [代码](https://github.com/wyhuai/HumanX) · [项目页](https://wyhuai.github.io/human-x/) |
| [KINO：用关键帧连接视觉语言规划与人形全身控制](论文逐篇解读/P224.md) | 以稀疏语义关键帧连接VLM分阶段规划与PPO全身策略，通过场景重定向和显著性采样完成G1抓取搬运。 | [原文](https://arxiv.org/abs/2609.18869) |
| [MobileWAM：用训练期未来信念支持移动操作](论文逐篇解读/P203.md) | 用前瞻链和移动专家建模底盘视角变化与手臂动作，执行全身移动操作长程任务。 | [原文](https://arxiv.org/abs/2608.04657) |
| [MotionDisco：通过接触计划搜索发现人形全身技能](论文逐篇解读/P329.md) | MotionDisco 以LLM进化搜索生成离散接触计划，通过分层运动学检查与动力学轨迹优化闭环修正，发现长时程人形全身移动操作技能并训练跟踪策略部署。 | [原文](https://arxiv.org/abs/2606.06139) |
| [OmniContact：用接触流组织可组合的人形物理技能](论文逐篇解读/P138.md) | 以身体轨迹和时序接触构成Contact Flow，由生成器与低层策略组合长程移动操作技能。 | [原文](https://arxiv.org/abs/2606.26201) · [代码](https://github.com/Ingrid789/OmniContact_sim2sim) · [项目页](https://omnicontact.github.io/) |
| [OpenHLM：验证全身原生LocoManip的数据与训练配方](论文逐篇解读/P141.md) | 以关节级全身遥操作和异构数据共训练VLA，面向人形全身移动操作控制任务。 | [原文](https://arxiv.org/abs/2606.22174) · [项目页](https://openhlm-project.github.io/) |
| [PanTact：通过可穿戴接触接口教授全身灵巧操作](论文逐篇解读/P496.md) | 从可穿戴贴片示范学习双手动作与身体接触目标，并用全身控制器将接触迁移到机器人可用表面。 | [原文](https://arxiv.org/abs/2610.12558) · [项目页](https://pantact.github.io/) |
| [PingpongDuo：把双人让位与击球串成连续乒乓球双打](论文逐篇解读/P505.md) | 团队规划联合选择站位并筛选碰撞风险，步法与击球交替执行，手臂残差修正回球；两台G1实机连续严格交替击球超过10次。 | [原文](https://arxiv.org/abs/2610.20579) · [项目页](https://www.archon.tech/research/PingpongDuo) |
| [Praxis：从第一视角示范迁移人形机器人的全身灵巧操作](论文逐篇解读/P338.md) | Praxis将移动操作分成视觉语言导航、闭环全身姿态校准和基于一次 egocentric RGB-D 示范的灵巧操作。人体腕部关键帧经机器人坐标变换、物体相对位姿重定位和手指关节映射后执行；在线物体跟踪、五指触觉与视觉结果验证支持跨位姿、跨物体和受扰恢复。五项实机任务平均成功率76.97%。 | [原文](https://arxiv.org/abs/2609.30735) · [项目页](https://edem-ai.github.io/Praxis/) |
| [ResGAC：全身运动中的精确SE(3)末端控制](论文逐篇解读/P489.md) | 以几何SE(3)末端反馈产生名义手臂目标，再用共享关节位置接口上的残差强化学习协调手臂、步态和平衡。 | [原文](https://arxiv.org/abs/2610.09479) · [项目页](https://resgac.github.io/ResGAC-website/) |
| [STRIDER：以精确落脚和多步态协同实现人形移动操作](论文逐篇解读/P225.md) | 融合AMP行走、地形感知迈步和笛卡尔上肢专家，并以LD-PPO蒸馏潜在协调表示实现单策略多步态移动操作。 | [原文](https://arxiv.org/abs/2609.23483) |
| [WEAVE：从人—物交互示范学习全身灵巧移动操作](论文逐篇解读/P223.md) | 从人—物动作重定向与接触优化生成机器人参考，再以几何和接触感知策略联合控制人形身体、灵巧手与物体。 | [原文](https://arxiv.org/abs/2609.16683) · [代码](https://github.com/xiaohu-art/Weave) · [项目页](https://xiaohu-art.github.io/Weave/) |
| [Workhorse：用机器人无关的人体示范学习全身移动操作](论文逐篇解读/P491.md) | 以人体五链动作直接训练视觉动作块规划器和全身强化学习跟踪器，并用漂移增强适配闭环误差。 | [原文](https://arxiv.org/abs/2610.09117) · [项目页](https://hybridrobotics.github.io/workhorse/) |
| [DemoHLM：从单次示范到可泛化人形移动操作](论文逐篇解读/P046.md) | 把单次仿真示范拆为移动、预操作和接触阶段，在新物体布局生成轨迹并训练长程策略。 | [原文](https://arxiv.org/abs/2510.11258) · [项目页](https://beingbeyond.github.io/DemoHLM/) |
| [HDMI：从人类视频学习交互式人形全身控制](论文逐篇解读/P099.md) | 结合对象感知参考、残差控制和物体状态奖励，从单目视频学习人形开门、搬运和推物。 | [原文](https://arxiv.org/abs/2509.16757) · [代码](https://github.com/LeCAR-Lab/HDMI) · [项目页](https://hdmi-humanoid.github.io/) |
| [HITTER：层级规划与强化学习驱动的人形乒乓球控制](论文逐篇解读/P472.md) | 物理模型预测来球并规划球拍目标，PPO全身策略协调G1跑位与正反手击球；动捕实测26球中24次有效回球。 | [原文](https://arxiv.org/abs/2508.21043) · [项目页](https://humanoid-table-tennis.github.io/) |
| [Humanoid Loco-Manipulation Survey：人形运动与操作的控制、规划与学习综述](论文逐篇解读/P069.md) | 综述人形移动、操作的模型控制、强化学习、接触规划与硬件接口，覆盖全身控制任务。 | [原文](https://arxiv.org/abs/2501.02116) |
| [PACE：物理预测增强的端到端人形乒乓球策略](论文逐篇解读/P473.md) | 学习式球路预测增强统一PPO策略的观测，仿真物理预测提供密集奖励与Critic特权信息；T1实机31球中19次有效回球。 | [原文](https://arxiv.org/abs/2509.21690) · [代码](https://github.com/purdue-tracelab/PACE-ICRA2026) · [项目页](https://purdue-tracelab.github.io/ttrobot.github.io/) |
| [SkillBlender：基于技能混合的通用人形全身移动操作](论文逐篇解读/P109.md) | 以目标条件全身技能原语和上层混合器组合推箱、搬运及按键等移动操作任务。 | [原文](https://arxiv.org/abs/2506.09366) · [代码](https://github.com/Humanoid-SkillBlender/SkillBlender) · [项目页](https://usc-gvl.github.io/SkillBlender-web/) |
| [SkillMimic-V2：用轨迹连接和状态历史补足稀疏交互示范](论文逐篇解读/P478.md) | STG连接示范片段，STF扩充邻域转移，ATS重采困难轨迹，并用冻结历史编码器学习稳健交互和技能切换。 | [原文](https://arxiv.org/abs/2505.02094) · [代码](https://github.com/Ingrid789/SkillMimic-V2) · [项目页](https://ingrid789.github.io/SkillMimicV2/) |
| [ULC：面向人形移动操作的统一细粒度控制器](论文逐篇解读/P096.md) | 用单一策略接收根高、躯干、双臂和移动目标，支持连续组合人形移动与全身操作。 | [原文](https://arxiv.org/abs/2507.06905) · [项目页](https://hellod035.github.io/ULC/) |
| [DeepMind乒乓球机器人：技能库与逐球决策](论文逐篇解读/P481.md) | 低层在MuJoCo中以进化策略训练17种击球技能，并利用真实人类球路反复校准；高层按来球、技能回球表现和对手特征逐球选技。真机与29名人类对手比赛，结果支持其达到业余中级水平，不代表职业级表现。 | [原文](https://arxiv.org/abs/2408.03906) · [项目页](https://deepmind.google/research/publications/107741/) |
| [SkillMimic：从篮球示范学习可复用的交互技能](论文逐篇解读/P477.md) | 统一技能条件策略以人体、球和接触关系模仿篮球示范，再由高层控制器组合技能完成运球、投篮和连续得分任务。 | [原文](https://arxiv.org/abs/2408.15270) · [代码](https://github.com/wyhuai/SkillMimic) · [项目页](https://ingrid789.github.io/SkillMimic/) |
| [物理乒乓球动画：分层学习击球技能与战术](论文逐篇解读/P483.md) | 先从动捕训练模仿和单项击球策略，再以Mixer平滑切换技能；策略层用条件VAE和迭代行为克隆，从角色、对手及球状态生成技能与目标落点。论文报告了技能识别、连续回球和VR交互结果，结论限于物理模拟角色。 | [原文](https://arxiv.org/abs/2407.16210) |
| [Vid2Player3D：从网球转播视频学习物理角色控制](论文逐篇解读/P479.md) | 把转播视频动作嵌入、低层物理模仿和高层击球规划结合，控制模拟球员适应来球、目标与不同击球风格。 | [原文](https://doi.org/10.1145/3592408) · [代码](https://github.com/nv-tlabs/vid2player3d) · [项目页](https://research.nvidia.com/labs/toronto-ai/vid2player3d/) |
| [ESTHER：以移动轮椅和机械臂完成网球回击](论文逐篇解读/P484.md) | ESTHER融合六套立体相机、连续时间球路滤波和轮椅定位，规划击球位姿后通过ROS导航与机械臂挥拍闭环回球。论文在标准室内球场和实验室评测；两种环境的成功判据不同，结果应分开解释。 | [原文](https://arxiv.org/abs/2210.02517) · [代码](https://github.com/CORE-Robotics-Lab/Wheelchair-Tennis-Robot) · [项目页](https://core-robotics-lab.github.io/Wheelchair-Tennis-Robot/) |
| [Deep Whole-Body Control：操作与运动统一策略学习](论文逐篇解读/P042.md) | 用优势混合平衡移动与操作训练信号，并以在线适应估计环境变化，训练统一全身策略。 | [原文](https://arxiv.org/abs/2210.10044) · [项目页](https://manipulation-locomotion.github.io/) |

#### 相关项目

| 项目 | 主要用途 | 功能与特点 |
| --- | --- | --- |
| [ATHLETE](https://anonymous.4open.science/r/athlete-humanoid-tennis) | 人形网球策略学习 | 论文作者链接的匿名代码实现 |
| [CEER](https://robotproject8.github.io/ceer_page/) | 层级物理交互 | 将移动操作任务压缩为基座速度、高度和双手目标等命令，由定制G1全身策略执行并进行Sim2Sim验证。 |
| [CoorDex](https://github.com/Skevinci/coordex) | 身体与灵巧手协同回放 | 拆分身体先验、手部先验与协同残差，在Isaac Lab中构造训练任务，用于研究身体与灵巧手联合控制。 |
| [DemoGrasp](https://github.com/BeingBeyond/DemoGrasp) | 灵巧手仿真与操作 | 以单次示范增强灵巧抓取强化学习策略，并研究不同机器人手形态间的迁移。 |
| [DemoHLM](https://github.com/BeingBeyond/DemoHLM) | 移动操作与技能系统 | 从单次仿真示范生成多样化人形移动操作轨迹；高层策略根据关节位置与速度、躯干roll/pitch及相机坐标目标物六维位姿输出运动命令，由全身控制器转为关节位置目标并经PD执行。 |
| [duatic_teleop](https://github.com/Duatic/duatic_teleop) | 模块化ROS 2遥操作 | 将人体输入设备接入模块化ROS 2遥操作流程，用于机器人控制和示范采集。 |
| [ESTHER Wheelchair Tennis Robot](https://github.com/CORE-Robotics-Lab/Wheelchair-Tennis-Robot) | 移动操作机器人系统 | 官方项目提供轮椅网球机器人系统、硬件设计、固件与ROS软件。 |
| [FARO](https://atarilab.github.io/faro.io/) | LocoManip与物理交互 | 围绕候选接触序列构建由便宜到昂贵的运动学与动力学可行性筛选层，并与接触模式树搜索结合以生成可执行的人形全身操作轨迹。 |
| [HANDOFF](https://github.com/lzyang2000/HANDOFF) | Agent到WBC接口项目 | 将上层移动操作意图转为十维全身命令，并蒸馏运动跟踪、行走和恢复教师为MoE策略。 |
| [HDMI](https://github.com/LeCAR-Lab/HDMI) | 人形物体交互项目 | 从单目视频恢复人体物体参考，在Isaac Lab训练残差策略，并通过动作蒸馏和在线适配连接G1部署。 |
| [HumanX](https://github.com/wyhuai/HumanX) | 交互数据与技能项目 | XGen编辑机器人与物体交互并导出HOI NPZ，XMimic将其转换为PKL训练数据，提供篮球接抛与假动作投篮、足球踢球、箱体取放的仿真训练、评测和回放流程。 |
| [I-BFM](https://github.com/Roboparty/I-BFM-Code) | 机器人开发与研究 | 联合表征机器人、物体与接触状态，通过奖励推断选择行为意图，使用同一策略完成搬箱、推箱和踢箱，并在偏离原轨迹后继续交互。 |
| [JAKA_Lumi](https://github.com/JAKARobotics/JAKA_Lumi) | 移动操作与技能系统 | 提供JAKA Lumi机器人平台开发入口，面向机械臂、移动平台与感知任务的系统集成。 |
| [Mobile ALOHA](https://github.com/MarkFzp/mobile-aloha) | 低成本双臂移动操作与示范学习系统 | 以主从双臂遥操作和移动底盘采集示范，再用ACT、Diffusion Policy或VINN学习长程移动操作。 |
| [MotionDisco](https://arxiv.org/abs/2606.06139) | LocoManip | MotionDisco 以LLM进化搜索生成离散接触计划，通过分层运动学检查与动力学轨迹优化闭环修正，发现长时程人形全身移动操作技能并训练跟踪策略部署。 |
| [MPC-RL](https://github.com/junhengl/mpc-rl) | LocoManip与物理交互 | 用并行GPU质心动力学MPC生成结构化奖励训练PPO，关节策略部署时独立执行，在Themis V2上验证行走、抗扰与推箱移动操作。 |
| [MuST](https://www.amazon.science/publications/must-multi-head-skill-transformer-for-long-horizon-dexterous-manipulation-with-skill-progress) | 机器人开发与研究 | 以多头技能Transformer和技能进度信息组织长流程灵巧操作，协调技能执行与阶段切换。 |
| [OmniContact](https://github.com/Ingrid789/OmniContact_sim2sim) | 接触流执行与仿真回放 | 以关键身体轨迹和时序接触统一表示搬运、推拉、滑动和踢球，并提供ONNX策略的MuJoCo回放。 |
| [omniteleop](https://github.com/dexmate-ai/omniteleop) | Dexmate遥操作接口 | 接入JoyCon、Dynamixel外骨骼和VR位姿，经急停与关节限制发送控制，并支持轨迹录制回放和遥测。 |
| [open_manipulator](https://github.com/ROBOTIS-GIT/open_manipulator) | 机器人SDK与通信接口 | OpenMANIPULATOR系列ROS 2软件包，用于机械臂控制、传感器集成和Physical AI开发。 |
| [OpenHLM](https://huggingface.co/OpenHLM) | 全身VLA数据与权重 | 将语言、相机像素和全身关节动作连接为人形VLA训练接口，通过异构共训练学习全身操作。官方数据集页列出约298 GB、1,814,714行数据，模型检查点另设独立仓库；代码包含G1控制采集、HuMI数据处理、训练与推理流程。 |
| [OpenWBT](https://github.com/GalaxyGeneralRobotics/OpenWBT) | 人形全身遥操作系统 | 以头显和手柄提供视角、手部目标与行走命令，结合上肢逆运动学和下肢策略驱动G1遥操作。 |
| [PACE（Humanoid Table Tennis）](https://github.com/purdue-tracelab/PACE-ICRA2026) | 人形乒乓球策略训练 | 端到端全身强化学习训练框架与仿真任务 |
| [Praxis](https://edem-ai.github.io/Praxis/) | 全身协同与技能接口 | Praxis将移动操作分成视觉语言导航、闭环全身姿态校准和基于一次 egocentric RGB-D 示范的灵巧操作。人体腕部关键帧经机器人坐标变换、物体相对位姿重定位和手指关节映射后执行；在线物体跟踪、五指触觉与视觉结果验证支持跨位姿、跨物体和受扰恢复。五项实机任务平均成功率76.97%。 |
| [SkillBlender](https://github.com/Humanoid-SkillBlender/SkillBlender) | 分层技能组合项目 | 以目标条件的低层技能原语和逐关节混合器组合行走、伸手与操作；SkillBench提供H1、G1和H1-2的任务配置、训练、回放与评测流程，支持状态或第一视角视觉作为高层观测。 |
| [SkillMimic](https://github.com/wyhuai/SkillMimic) | 物理仿真篮球技能学习 | 以统一全身交互策略学习篮球技能，并由高层策略复用技能完成目标任务。 |
| [SkillMimic-V2](https://github.com/Ingrid789/SkillMimic-V2) | 鲁棒物理仿真交互技能学习 | 通过轨迹图、邻域转移场和历史编码增强物理仿真人形角色的技能切换与恢复。 |
| [troncamp-mani](https://github.com/limxdynamics/troncamp-mani) | Benchmark与评测平台 | TRON2双臂ACT竞赛的训练与推理基线，围绕竞赛任务完成仿真评估和结果提交。 |
| [UMI on Legs](https://github.com/real-stanford/umi-on-legs) | 操作策略与移动全身控制接口 | 由视觉操作策略输出世界坐标夹爪轨迹，全身控制器协调四足底盘与机械臂执行移动操作。 |
| [UniTacHand](https://github.com/BeingBeyond/UniTacHand) | 灵巧手遥操作与训练系统 | 将人类触觉手套信号与机器人灵巧手信号映射到统一表示，用于触觉技能迁移。 |
| [Vid2Player3D](https://github.com/nv-tlabs/vid2player3d) | 视频驱动物理网球角色控制 | 将视频学习到的动作嵌入、物理模仿策略和高层击球规划组合为多回合角色控制器。 |
| [WEAVE](https://github.com/xiaohu-art/Weave) | 全身协同与技能接口 | 从人—物动作重定向与接触优化生成机器人参考，再以几何和接触感知策略联合控制人形身体、灵巧手与物体。 |

[返回本页导航](#本页导航)

## 相关资料

- [技术与研究](README.md) · [书籍与课程](../强化学习开发者必备开源资料/书籍与课程.md)
