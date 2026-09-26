# 具身智能数据集

> 汇总具身智能训练与评测相关的数据集、训练数据配方及仿真资产，涵盖人体动作、人类操作视频、机器人示范、重定向轨迹与合成数据，按数据来源与内容整理。

当前收录：**40项数据集与相关数据资源**。

## 分类导航

[人体动作与语言](#human-motion) · [人类视频与操作示范](#human-demonstration) · [重定向与目标本体动作](#retargeted-motion) · [真实机器人示范与运行数据](#robot-demonstration) · [仿真合成与生成式数据](#synthetic-data) · [跨来源训练集合与配方](#training-mixtures) · [数字资产与感知评测资源](#assets-perception)

点击名称进入原始来源，各分类下可展开规模、格式与获取方式。规模和访问说明沿用既有记录，不代表当前下载状态；使用前请核对来源的数据卡和授权条款。

<a id="human-motion"></a>

## 人体动作与语言

| 数据集 | 数据内容 | 本体／对象 | 训练用途 |
| --- | --- | --- | --- |
| <a id="d001"></a>[AMASS](https://amass.is.tue.mpg.de/) | 统一格式的人体运动捕捉与SMPL动作 | 人体 | 恢复、重定向人体动作，构建机器人动作跟踪参考 |
| <a id="d002"></a>[CMU Motion Capture Database](http://mocap.cs.cmu.edu/) | 多类人体运动捕捉序列 | 人体 | 建立动作参考库，研究动作跟踪与动画生成 |
| <a id="d003"></a>[HumanML3D](https://github.com/EricGuo5513/HumanML3D) | 文本与三维人体动作配对 | 人体 | 训练文本到动作生成，研究语言驱动的动作接口 |
| <a id="d004"></a>[KIT Motion-Language Dataset](https://motion-annotation.humanoids.kit.edu/) | 文本描述与运动捕捉动作配对 | 人体 | 训练语言条件动作生成 |
| <a id="d005"></a>[AIST++](https://google.github.io/aistplusplus_dataset/) | 舞蹈视频、三维动作与音乐 | 人体 | 研究音乐条件动作生成与动作跟踪 |
| <a id="d006"></a>[Motion-X](https://motion-x-dataset.github.io/) | 全身三维动作与文本描述 | 人体 | 训练全身动作生成，构建动作跟踪参考 |
| <a id="d008"></a>[Human3.6M](http://vision.imar.ro/human3.6m/description.php) | 室内人体视频与三维姿态 | 人体 | 训练姿态估计，为动作重定向提供人体表示 |
| <a id="d009"></a>[LaFAN1](https://github.com/ubisoft/ubisoft-laforge-animation-dataset) | 运动捕捉序列与动作过渡片段 | 人体 | 研究动作补间、动作生成与跟踪参考 |
| <a id="d023"></a>[OMOMO](https://github.com/lijiaman/omomo_release) | 人体与物体动作、物体三维几何 | 人体／物体 | 学习人-物交互动作，研究重定向与移动操作 |

<details>
<summary>规模、格式与获取方式</summary>

### [AMASS](https://amass.is.tue.mpg.de/)

- **规模与版本**：多数据集统一，规模见官网
- **模态与表示**：MoCap/SMPL
- **具体本体／对象**：Human
- **获取方式**：申请访问；[数据卡／项目来源](https://amass.is.tue.mpg.de/)
- **许可与访问说明**：既有记录按研究用途收录，具体授权以来源条款为准
- **补充说明**：人体动作基座；许可范围：研究许可；访问方式：申请下载

### [CMU Motion Capture Database](http://mocap.cs.cmu.edu/)

- **规模与版本**：多类动作序列
- **模态与表示**：MoCap
- **具体本体／对象**：Human
- **获取方式**：直接下载；[数据卡／项目来源](http://mocap.cs.cmu.edu/)
- **许可与访问说明**：既有记录按研究用途收录，具体授权以来源条款为准
- **补充说明**：经典动作数据；许可范围：公开研究使用

### [HumanML3D](https://github.com/EricGuo5513/HumanML3D)

- **规模与版本**：文本动作对
- **模态与表示**：Text + Motion
- **具体本体／对象**：Human
- **获取方式**：按说明；[数据卡／项目来源](https://github.com/EricGuo5513/HumanML3D)
- **许可与访问说明**：既有记录按研究用途收录，具体授权以来源条款为准
- **补充说明**：语言动作数据；许可范围：研究许可；访问方式：按项目说明

### [KIT Motion-Language Dataset](https://motion-annotation.humanoids.kit.edu/)

- **规模与版本**：文本描述动作
- **模态与表示**：Text + MoCap
- **具体本体／对象**：Human
- **获取方式**：申请访问；[数据卡／项目来源](https://motion-annotation.humanoids.kit.edu/)
- **许可与访问说明**：既有记录按研究用途收录，具体授权以来源条款为准
- **补充说明**：动作语义；许可范围：研究许可；访问方式：申请/下载

### [AIST++](https://google.github.io/aistplusplus_dataset/)

- **规模与版本**：舞蹈动作
- **模态与表示**：Video + 3D Motion + Music
- **具体本体／对象**：Human
- **获取方式**：申请访问；[数据卡／项目来源](https://google.github.io/aistplusplus_dataset/)
- **许可与访问说明**：既有记录按研究用途收录，具体授权以来源条款为准
- **补充说明**：表达性动作；许可范围：研究许可；访问方式：申请/下载

### [Motion-X](https://motion-x-dataset.github.io/)

- **规模与版本**：大规模全身动作
- **模态与表示**：3D Motion + Text
- **具体本体／对象**：Human
- **获取方式**：项目页；[数据卡／项目来源](https://motion-x-dataset.github.io/)
- **许可与访问说明**：既有记录按研究用途收录，具体授权以来源条款为准
- **补充说明**：全身/手部动作；许可范围：研究许可

### [Human3.6M](http://vision.imar.ro/human3.6m/description.php)

- **规模与版本**：室内动作
- **模态与表示**：Video + 3D Pose
- **具体本体／对象**：Human
- **获取方式**：申请访问；[数据卡／项目来源](http://vision.imar.ro/human3.6m/description.php)
- **许可与访问说明**：既有记录按研究用途收录，具体授权以来源条款为准
- **补充说明**：人体姿态基础；许可范围：研究许可；访问方式：申请下载

### [LaFAN1](https://github.com/ubisoft/ubisoft-laforge-animation-dataset)

- **规模与版本**：动作过渡片段
- **模态与表示**：Motion Sequences
- **具体本体／对象**：Human
- **获取方式**：直接下载；[数据卡／项目来源](https://github.com/ubisoft/ubisoft-laforge-animation-dataset)
- **许可与访问说明**：既有记录按研究用途收录，具体授权以来源条款为准
- **补充说明**：动作过渡；许可范围：研究许可

### [OMOMO](https://github.com/lijiaman/omomo_release)

- **规模与版本**：15种物体，约10小时人-物交互动作
- **模态与表示**：3D Object Geometry;Object Motion;Human Motion
- **具体本体／对象**：Human;Object
- **获取方式**：平台下载；[数据卡／项目来源](https://github.com/lijiaman/omomo_release)
- **许可与访问说明**：许可信息待核实
- **补充说明**：官方项目同时发布数据入口与两阶段扩散基线。；许可范围：数据条款见下载入口；代码MIT；访问方式：GitHub/Google Drive

</details>

<a id="human-demonstration"></a>

## 人类视频与操作示范

| 数据集 | 数据内容 | 本体／对象 | 训练用途 |
| --- | --- | --- | --- |
| <a id="d007"></a>[Ego-Exo4D](https://ego-exo4d-data.org/) | 第一／第三视角视频、姿态与音频 | 人体 | 学习第一视角技能表征，研究视频模仿 |
| <a id="d035"></a>[RealOmni-Open](https://cn.genrobot.com/data/open-dataset) | 双手操作影像、末端位姿与夹爪状态 | 人体＋GenDAS采集器 | 预训练操作表征，经本体映射构建机器人示范 |
| <a id="d036"></a>[Open-AoE-2000H](https://github.com/ant-research/Open-AoE) | 手机视频、手部与相机轨迹、动作标注 | 人体＋手机 | 研究人类操作预训练、跨本体重定向与VLA/WAM |
| <a id="d038"></a>[World In Your Hands](https://wiyh.tars-ai.com/) | 多视角、手部动作及部分触觉与语义 | 人体／灵巧操作 | 研究跨本体操作预训练、重定向与世界建模 |
| <a id="d039"></a>[KAI Ego Data Minibatch](https://huggingface.co/datasets/Kinetix-AI/kai-data-minibatch) | 第一视角视频、相机参数与跟踪标注 | 人体 | 评估第一视角手物交互数据与机器人学习管线 |

<details>
<summary>规模、格式与获取方式</summary>

### [Ego-Exo4D](https://ego-exo4d-data.org/)

- **规模与版本**：多视角技能视频
- **模态与表示**：Ego/Exo Video + Pose + Audio
- **具体本体／对象**：Human
- **获取方式**：申请访问；[数据卡／项目来源](https://ego-exo4d-data.org/)
- **许可与访问说明**：既有记录按研究用途收录，具体授权以来源条款为准
- **补充说明**：第一/第三视角；许可范围：研究许可；访问方式：申请下载

### [RealOmni-Open](https://cn.genrobot.com/data/open-dataset)

- **规模与版本**：发布方报告13000+小时与500万+片段；Hugging Face当前展示约36.9 TB
- **模态与表示**：Fisheye RGB;Camera Calibration;IMU;End-Effector Pose;Gripper State;Optional Depth;Optional Tactile
- **具体本体／对象**：Human + GenDAS Gripper;No Target Robot
- **获取方式**：平台注册；[数据卡／项目来源](https://cn.genrobot.com/data/open-dataset)
- **许可与访问说明**：既有记录按研究用途收录，具体授权以来源条款为准
- **补充说明**：由简智机器人使用GenDAS采集设备在真实家庭场景采集并通过Hugging Face、ModelScope和百度百舸等入口分发；MCAP记录鱼眼视频、标定、IMU、夹爪开合和末端位姿，部分批次包含深度或触觉。它不是目标机器人关节轨迹，进入具体本体训练前仍需完成坐标、动作空间和控制接口转换。官网限定非商业使用，而Hugging Face元数据标为CC BY-SA 4.0，授权口径冲突，按更严格的研究用途记录。13000小时、500万片段与210秒中位时长不是同一粒度的统计，使用时需区分回合、片段和训练窗口。

### [Open-AoE-2000H](https://github.com/ant-research/Open-AoE)

- **规模与版本**：约2000小时；500+采集者；400+智能手机
- **模态与表示**：Calibrated RGB;MANO Hand Pose;Camera Trajectory;Validity Mask;Bilingual Atomic Action
- **具体本体／对象**：Human + Consumer Smartphone;No Target Robot
- **获取方式**：平台下载；[数据卡／项目来源](https://github.com/ant-research/Open-AoE)
- **许可与访问说明**：不同子集、上游数据或配套资源适用不同条款
- **补充说明**：使用消费级智能手机采集自然环境中的第一视角操作视频，并提供相机轨迹、MANO手部恢复、有效性掩码和带时间范围的双语原子动作。它不是目标机器人的关节、力矩或低层控制日志；进入机器人训练仍需动作表示转换、重定向、少量目标本体数据和闭环验证。仓库原创代码为Apache-2.0，但数据分发条款、MANO文件、模型权重、机器人资产与第三方组件分别适用各自许可，因此需要分别核对许可。

### [World In Your Hands](https://wiyh.tars-ai.com/)

- **规模与版本**：1045小时RGB与标定；800小时深度；500小时动作；400小时指令；320小时推理；240小时掩码；10小时触觉
- **模态与表示**：Multi-View RGB;Calibration;Depth;3D Wrist Pose;Hand Skeleton;Tactile;Mask;Instruction;Reasoning
- **具体本体／对象**：Human;Cross-Embodiment;Dexterous Hand
- **获取方式**：项目页；[数据卡／项目来源](https://wiyh.tars-ai.com/)
- **许可与访问说明**：CC-BY-NC-SA-4.0
- **补充说明**：由它石智航TARS Robotics使用Oracle Suite在办公室、物流、洗衣、餐饮、酒店、公寓、超市等自然工作流中采集，并提供样例数据、HDF5解析、可视化和LeRobot转换。各模态覆盖时长不同，只有部分数据含触觉、动作、指令或推理标注；人体动作进入机器人仍需重定向或跨本体预训练和目标本体后训练。

### [KAI Ego Data Minibatch](https://huggingface.co/datasets/Kinetix-AI/kai-data-minibatch)

- **规模与版本**：约3小时完整处理数据包；数据卡显示63.7 GB
- **模态与表示**：Ego Video;Camera Parameters;Tracking;Semantic Segments;Quality Inspection
- **具体本体／对象**：Human;No Target Robot
- **获取方式**：申请访问；[数据卡／项目来源](https://huggingface.co/datasets/Kinetix-AI/kai-data-minibatch)
- **许可与访问说明**：既有记录按研究用途收录，具体授权以来源条款为准
- **补充说明**：由超维动力Kinetix AI发布，保留元数据、相机参数、质检输出、片段元信息、语义分段与跟踪结果。须签署非商业受控访问协议并经人工审核；公司总体采集量不是此样例开放规模。不是目标机器人关节与低层动作日志，下游训练仍需验证坐标、时间和动作转换。

</details>

<a id="retargeted-motion"></a>

## 重定向与目标本体动作

本组包括人类动作与目标机器人动作的配对或转换资源；AMS为直接合成的本体参考，不是MoCap重定向。

| 数据集 | 数据内容 | 本体／对象 | 训练用途 |
| --- | --- | --- | --- |
| <a id="d010"></a>[Humanoid-X](https://huggingface.co/datasets/USC-PSI-Lab/Humanoid-X) | 人类视频与人形动作数据 | 人体／人形机器人 | 研究视频模仿及人体到机器人动作转换 |
| <a id="d011"></a>[PHUMA](https://github.com/DAVIAN-Robotics/PHUMA) | 人体动作与目标机器人重定向动作 | G1、H1-2等 | 构建物理可行动作参考，研究重定向与动作跟踪 |
| <a id="d026"></a>[OmniContact Dataset](https://huggingface.co/datasets/lightcone02/OmniContact-Dataset) | 人体-物体动作、G1轨迹与接触标签 | 人体／G1／物体 | 学习接触感知参考与全身移动操作 |
| <a id="d031"></a>[LAFAN1 Retargeting Dataset](https://huggingface.co/datasets/lvhaidong/LAFAN1_Retargeting_Dataset) | 由LaFAN1转换的关节与根节点轨迹 | H1、H1-2、G1 | 训练目标本体动作跟踪与运动模仿 |
| <a id="d040"></a>[AMS Synthetic Balance Motions](https://github.com/OpenDriveLab/AMS/blob/main/MotionGen/README.md) | 目标本体根节点、关节与支撑腿参考 | G1 29自由度 | 扩展平衡动作参考，研究动作跟踪与参考质量 |

<details>
<summary>规模、格式与获取方式</summary>

### [Humanoid-X](https://huggingface.co/datasets/USC-PSI-Lab/Humanoid-X)

- **规模与版本**：规模见项目页
- **模态与表示**：Human Video + Humanoid Motion
- **具体本体／对象**：Human/Humanoid
- **获取方式**：项目页；[数据卡／项目来源](https://huggingface.co/datasets/USC-PSI-Lab/Humanoid-X)
- **许可与访问说明**：许可信息待核实
- **补充说明**：官方Hugging Face数据仓库发布文本描述、人形关键点、动作与部分人体姿态；许可范围仍需核验

### [PHUMA](https://github.com/DAVIAN-Robotics/PHUMA)

- **规模与版本**：预构建G1/H1-2动作库，规模见官方数据卡
- **模态与表示**：SMPL-X Human Motion;Retargeted Robot Motion
- **具体本体／对象**：Unitree G1;Unitree H1-2;Custom Humanoid
- **获取方式**：平台下载；[数据卡／项目来源](https://github.com/DAVIAN-Robotics/PHUMA)
- **许可与访问说明**：不同子集、上游数据或配套资源适用不同条款
- **补充说明**：提供物理筛选、PhySINK重定向与自定义本体流程；原始人体动作并非全部可再分发。；许可范围：Apache-2.0；源人体动作受上游许可约束；访问方式：下载脚本/Hugging Face

### [OmniContact Dataset](https://huggingface.co/datasets/lightcone02/OmniContact-Dataset)

- **规模与版本**：公开仓库当前列出700条处理轨迹；项目页汇总1274条有效序列与22.29小时配对采集
- **模态与表示**：BVH;G1 Joint Trajectory;Object Pose;Contact Label
- **具体本体／对象**：Human;Unitree G1;Object
- **获取方式**：平台注册；[数据卡／项目来源](https://huggingface.co/datasets/lightcone02/OmniContact-Dataset)
- **许可与访问说明**：CC-BY-4.0
- **补充说明**：处理NPZ含29维关节、39个body位姿、物体6DoF及腕踝接触标签；90 Hz项目全集与当前公开子集口径分开记录。；许可范围：CC BY 4.0；访问方式：需登录并同意共享联系信息

### [LAFAN1 Retargeting Dataset](https://huggingface.co/datasets/lvhaidong/LAFAN1_Retargeting_Dataset)

- **规模与版本**：314 MB；由LAFAN1逐帧重定向到3种人形本体
- **模态与表示**：Root Pose;Joint Configuration;30 FPS
- **具体本体／对象**：Unitree H1;H1_2;G1
- **获取方式**：平台下载；[数据卡／项目来源](https://huggingface.co/datasets/lvhaidong/LAFAN1_Retargeting_Dataset)
- **许可与访问说明**：不同子集、上游数据或配套资源适用不同条款
- **补充说明**：社区发布而非宇树官方数据；只考虑运动学、末端位姿及关节位置速度约束，未处理动力学与执行器限制；上游LAFAN1为CC BY-NC-ND 4.0，使用与再分发前必须单独核对衍生数据权利。

### [AMS Synthetic Balance Motions](https://github.com/OpenDriveLab/AMS/blob/main/MotionGen/README.md)

- **规模与版本**：约10000条合成平衡序列
- **模态与表示**：Root Position;Quaternion;Joint Position;Axis-Angle Pose;FPS;Stance Leg
- **具体本体／对象**：Unitree G1 29-DoF
- **获取方式**：按说明；[数据卡／项目来源](https://github.com/OpenDriveLab/AMS/blob/main/MotionGen/README.md)
- **许可与访问说明**：Apache-2.0
- **补充说明**：使用Pyroki采样平衡姿态和序列，经MuJoCo自碰撞与地面穿透检测后筛选合并；README提供Hugging Face及Git LFS入口并声明Apache-2.0。不是人类MoCap重定向，也不是策略执行成功率或完整训练控制器；参考可行性仍需在目标动力学与控制器下验证。

</details>

<a id="robot-demonstration"></a>

## 真实机器人示范与运行数据

| 数据集 | 数据内容 | 本体／对象 | 训练用途 |
| --- | --- | --- | --- |
| <a id="d013"></a>[DROID](https://droid-dataset.github.io/) | 多视角操作视频、本体状态与动作 | 机械臂 | 训练视觉模仿学习与VLA操作策略 |
| <a id="d014"></a>[BridgeData V2](https://rail-berkeley.github.io/bridgedata/) | 操作视频、动作与语言 | 机械臂 | 训练语言条件操作策略，进行模仿学习实验 |
| <a id="d015"></a>[RoboNet](https://www.robonet.wiki/) | 跨机器人操作视频与动作 | 多种机械臂 | 研究动作条件视频预测与跨机器人策略学习 |
| <a id="d016"></a>[RH20T](https://rh20t.github.io/) | 多模态传感器记录与操作动作 | 多种机械臂 | 训练多模态操作策略与示范模仿 |
| <a id="d017"></a>[RoboMIND](https://huggingface.co/datasets/x-humanoid-robomind/RoboMIND) | 多视角、状态、语言及部分触觉数据 | 多种机器人／人形 | 训练通用操作策略，研究跨本体与触觉融合 |
| <a id="d018"></a>[AGIBOT WORLD 2026](https://huggingface.co/datasets/agibot-world/AgiBotWorld2026) | 全身操作、多模态交互及策略运行记录 | G2及配套末端 | 研究模仿学习、世界模型、真机RL与失败恢复 |
| <a id="d024"></a>[Humanoid Everyday](https://humanoideveryday.github.io/) | 真机多传感器、关节动作与任务语言 | G1、H1 | 训练全身操作策略，评测开放世界任务 |
| <a id="d027"></a>[OpenHLM-data](https://huggingface.co/datasets/OpenHLM/OpenHLM-data) | 相机、语言与全身关节动作 | 人形机器人 | 训练全身VLA与移动操作策略 |

<details>
<summary>规模、格式与获取方式</summary>

### [DROID](https://droid-dataset.github.io/)

- **规模与版本**：规模见项目页
- **模态与表示**：Multi-view Video + Proprioception + Actions
- **具体本体／对象**：多机械臂
- **获取方式**：申请访问；[数据卡／项目来源](https://droid-dataset.github.io/)
- **许可与访问说明**：既有记录按研究用途收录，具体授权以来源条款为准
- **补充说明**：多场景真实操作；许可范围：研究许可；访问方式：申请/下载

### [BridgeData V2](https://rail-berkeley.github.io/bridgedata/)

- **规模与版本**：规模见项目页
- **模态与表示**：Video + Actions + Language
- **具体本体／对象**：机械臂
- **获取方式**：直接下载；[数据卡／项目来源](https://rail-berkeley.github.io/bridgedata/)
- **许可与访问说明**：既有记录按研究用途收录，具体授权以来源条款为准
- **补充说明**：跨场景操作；许可范围：研究许可；访问方式：下载

### [RoboNet](https://www.robonet.wiki/)

- **规模与版本**：规模见项目页
- **模态与表示**：Video + Actions
- **具体本体／对象**：多机械臂
- **获取方式**：直接下载；[数据卡／项目来源](https://www.robonet.wiki/)
- **许可与访问说明**：既有记录按研究用途收录，具体授权以来源条款为准
- **补充说明**：早期跨机器人数据；许可范围：研究许可；访问方式：下载

### [RH20T](https://rh20t.github.io/)

- **规模与版本**：规模见项目页
- **模态与表示**：Multi-modal Sensor + Actions
- **具体本体／对象**：多机械臂
- **获取方式**：申请访问；[数据卡／项目来源](https://rh20t.github.io/)
- **许可与访问说明**：既有记录按研究用途收录，具体授权以来源条款为准
- **补充说明**：多模态真实操作；许可范围：研究许可；访问方式：申请/下载

### [RoboMIND](https://huggingface.co/datasets/x-humanoid-robomind/RoboMIND)

- **规模与版本**：V1.2 107k轨迹/479任务/96物体类/4本体；V2.0官方集合称新增300k+双臂轨迹/6本体/739任务/129技能/12k+触觉数据
- **模态与表示**：Multi-view + Proprioception + Language + Tactile
- **具体本体／对象**：多机器人/人形
- **获取方式**：平台注册；[数据卡／项目来源](https://huggingface.co/datasets/x-humanoid-robomind/RoboMIND)
- **许可与访问说明**：不同子集、上游数据或配套资源适用不同条款
- **补充说明**：V1.2 Hugging Face数据卡标注Apache-2.0且需登录同意共享联系信息；V2.0完整集合位于https://modelscope.cn/datasets/X-Humanoid/RoboMIND2.0，其具体文件许可与下载条件应按ModelScope逐项核验。

### [AGIBOT WORLD 2026](https://huggingface.co/datasets/agibot-world/AgiBotWorld2026)

- **规模与版本**：持续分主题发布；当前覆盖模仿学习、物理交互与世界模型、真机强化学习数据，具体规模按各期数据卡
- **模态与表示**：RGB;Depth;Tactile;LiDAR;IMU;Whole-Body State;Force/Torque;Language;Policy Rollout;Human Intervention
- **具体本体／对象**：AGIBOT G2;OmniPicker;OmniHand
- **获取方式**：平台下载；[数据卡／项目来源](https://huggingface.co/datasets/agibot-world/AgiBotWorld2026)
- **许可与访问说明**：CC-BY-NC-SA-4.0
- **补充说明**：首期包含真实场景示范、任务步骤、原子技能、物体标注和错误恢复；后续增加接触与物理交互信号、策略执行、人类干预和真机强化学习数据。小时、轨迹、任务和技能属于不同统计粒度，使用时应回到对应版本数据卡；代码、数据与仿真资产许可分别核对。；访问方式：Hugging Face

### [Humanoid Everyday](https://humanoideveryday.github.io/)

- **规模与版本**：10.3k轨迹；300万余帧；260任务；7类别；30 Hz
- **模态与表示**：RGB;Depth;LiDAR;Tactile;IMU;Joint State;Action;Language
- **具体本体／对象**：Unitree G1;Unitree H1
- **获取方式**：平台下载；[数据卡／项目来源](https://humanoideveryday.github.io/)
- **许可与访问说明**：不同子集、上游数据或配套资源适用不同条款
- **补充说明**：包含真实G1/H1示范与多模态同步数据；云评测状态以项目页为准。；许可范围：数据Apache-2.0；加载代码MIT；访问方式：Hugging Face/任务下载清单

### [OpenHLM-data](https://huggingface.co/datasets/OpenHLM/OpenHLM-data)

- **规模与版本**：约298 GB；轨迹数量与字段说明待官方数据卡补充
- **模态与表示**：Camera;Language;Whole-Body Joint Action
- **具体本体／对象**：Humanoid
- **获取方式**：平台下载；[数据卡／项目来源](https://huggingface.co/datasets/OpenHLM/OpenHLM-data)
- **许可与访问说明**：MIT
- **补充说明**：Hugging Face仓库已发布但README当前为空；不根据论文演示推测下载文件的具体结构。；访问方式：Hugging Face

</details>

<a id="synthetic-data"></a>

## 仿真合成与生成式数据

| 数据集 | 数据内容 | 本体／对象 | 训练用途 |
| --- | --- | --- | --- |
| <a id="d020"></a>[RoboCasa365](https://robocasa.ai/) | 厨房仿真任务、示范与场景资产 | 机械臂／移动操作 | 生成家庭操作示范，训练和评测操作策略 |
| <a id="d021"></a>[MimicGen Datasets](https://mimicgen.github.io/) | 仿真生成的多任务操作示范 | 机械臂 | 扩展示范数据，训练模仿学习策略 |
| <a id="d022"></a>[DexMimicGen Datasets](https://dexmimicgen.github.io/) | 双臂与灵巧操作仿真示范 | 双臂／灵巧手 | 训练灵巧操作和长程模仿策略 |
| <a id="d025"></a>[GRAIL Generated Loco-Manipulation Dataset](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-Locomanipulation-GRAIL) | 合成视频、人-物交互与G1轨迹 | G1／人体／物体 | 构建移动操作参考，研究动作跟踪与仿真迁移 |
| <a id="d030"></a>[NVIDIA GR00T X-Embodiment Sim](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-GR00T-X-Embodiment-Sim) | 跨本体仿真操作轨迹 | Panda、GR1、G1 | 生成操作训练数据，开展GR00T后训练 |
| <a id="d037"></a>[HumanGen](https://github.com/robbyant-research/Zero-WAM) | 生成式人机视频、动作及任务配对 | 人体＋多种机器人 | 研究上下文机器人学习与跨任务泛化 |

<details>
<summary>规模、格式与获取方式</summary>

### [RoboCasa365](https://robocasa.ai/)

- **规模与版本**：365类任务/多厨房
- **模态与表示**：Simulation + Demonstrations + Assets
- **具体本体／对象**：机械臂/移动操作
- **获取方式**：项目页；[数据卡／项目来源](https://robocasa.ai/)
- **许可与访问说明**：不同子集、上游数据或配套资源适用不同条款
- **补充说明**：厨房任务扩展；许可范围：MIT/资产许可分项

### [MimicGen Datasets](https://mimicgen.github.io/)

- **规模与版本**：多任务/多版本
- **模态与表示**：Simulation Demonstrations
- **具体本体／对象**：机械臂
- **获取方式**：项目页；[数据卡／项目来源](https://mimicgen.github.io/)
- **许可与访问说明**：既有记录按研究用途收录，具体授权以来源条款为准
- **补充说明**：自动数据扩增；许可范围：研究许可

### [DexMimicGen Datasets](https://dexmimicgen.github.io/)

- **规模与版本**：规模见项目页
- **模态与表示**：Simulation Demonstrations
- **具体本体／对象**：双臂/灵巧手
- **获取方式**：项目页；[数据卡／项目来源](https://dexmimicgen.github.io/)
- **许可与访问说明**：既有记录按研究用途收录，具体授权以来源条款为准
- **补充说明**：复杂操作扩增；许可范围：研究许可

### [GRAIL Generated Loco-Manipulation Dataset](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-Locomanipulation-GRAIL)

- **规模与版本**：20,000余条序列；约250 GB；多类拾取、坐下与地形动作
- **模态与表示**：Synthetic Video;4D HOI;G1 Trajectory;Object 6DoF;USD Asset
- **具体本体／对象**：Unitree G1;SMPL-X;Object
- **获取方式**：平台下载；[数据卡／项目来源](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-Locomanipulation-GRAIL)
- **许可与访问说明**：不同子集、上游数据或配套资源适用不同条款
- **补充说明**：每条可含源视频、SMPL-X/物体重建、G1与物体物理rollout及USD资产。；许可范围：主体Apache-2.0；第三方资产与权重保留上游许可；访问方式：Hugging Face

### [NVIDIA GR00T X-Embodiment Sim](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-GR00T-X-Embodiment-Sim)

- **规模与版本**：跨本体双臂9k轨迹；GR1人形桌面操作240k轨迹；另有单臂与G1 LocoManip子集
- **模态与表示**：Simulation Trajectory;Robot State;Action;Task
- **具体本体／对象**：Panda Gripper/Hand;Fourier GR1;Unitree G1
- **获取方式**：平台下载；[数据卡／项目来源](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-GR00T-X-Embodiment-Sim)
- **许可与访问说明**：CC-BY-4.0
- **补充说明**：官方数据卡说明这些轨迹用于GR00T N1后训练；不同本体与任务以独立子集组织，不能假定动作空间可直接互换。

### [HumanGen](https://github.com/robbyant-research/Zero-WAM)

- **规模与版本**：7.42万对人机上下文样本；8600个任务
- **模态与表示**：Generated Human Video;Robot Video;Executable Action;Language;Task Metadata
- **具体本体／对象**：Human + 45+ Robot Embodiments
- **获取方式**：项目页；[数据卡／项目来源](https://github.com/robbyant-research/Zero-WAM)
- **许可与访问说明**：许可信息待核实
- **补充说明**：既有记录仅确认论文报告的规模与数据构造流程，尚未核实实际下载文件和数据协议；此条保留为跟踪资源，不表示数据已可获取。

</details>

<a id="training-mixtures"></a>

## 跨来源训练集合与配方

合集和训练配方可能包含其他条目中的数据；40项资源的规模不能简单相加。

| 数据集 | 数据内容 | 本体／对象 | 训练用途 |
| --- | --- | --- | --- |
| <a id="d012"></a>[Open X-Embodiment](https://robotics-transformer-x.github.io/) | 跨机构、跨机器人的操作数据合集 | 多种机器人 | 统一观测与动作字段，训练跨本体通用策略 |
| <a id="d028"></a>[MolmoAct Dataset与训练数据配方](https://github.com/allenai/molmoact) | 自采示范与多源动作推理训练配方 | Franka、WidowX等 | 开展VLA预训练、中期训练与动作推理学习 |
| <a id="d029"></a>[MolmoAct2训练集合与策略Rollout](https://github.com/allenai/molmoact2) | 跨本体训练集合与策略执行轨迹 | SO-100/101、Franka等 | 研究VLA微调、失败标注及奖励建模 |
| <a id="d033"></a>[ARIO Dataset](https://imaei.github.io/project_pages/ario/) | 统一格式的真实、仿真及转换数据 | 多种机器人 | 统一多源数据，研究跨机器人操作与导航 |

<details>
<summary>规模、格式与获取方式</summary>

### [Open X-Embodiment](https://robotics-transformer-x.github.io/)

- **规模与版本**：跨机构数据集合集
- **模态与表示**：Images + States + Actions + Language
- **具体本体／对象**：多机器人
- **获取方式**：平台下载；[数据卡／项目来源](https://robotics-transformer-x.github.io/)
- **许可与访问说明**：不同子集、上游数据或配套资源适用不同条款
- **补充说明**：跨本体数据核心；许可范围：各子集不同；访问方式：TensorFlow Datasets/项目页

### [MolmoAct Dataset与训练数据配方](https://github.com/allenai/molmoact)

- **规模与版本**：自采约10k轨迹/93任务；原始表约111万帧行；预训练混合约2410万样本
- **模态与表示**：Multi-View RGB;Robot State;Action;Language;Depth Token;Visual Trace
- **具体本体／对象**：Franka;Google Robot;WidowX;Mixed
- **获取方式**：平台下载；[数据卡／项目来源](https://github.com/allenai/molmoact)
- **许可与访问说明**：不同子集、上游数据或配套资源适用不同条款
- **补充说明**：自采MolmoAct Dataset采用CC BY 4.0；预训练混合包含Open X-Embodiment转换数据并受上游许可约束；训练数据配方不能当作单一原始数据集。

### [MolmoAct2训练集合与策略Rollout](https://github.com/allenai/molmoact2)

- **规模与版本**：多个训练集合；评测Rollout覆盖多任务与ID/OOD设置，规模按子数据卡
- **模态与表示**：LeRobot v3.0;RGB;Robot State;Action;Language;Policy Rollout
- **具体本体／对象**：SO-100/101;Franka;Bimanual YAM;Mixed
- **获取方式**：平台下载；[数据卡／项目来源](https://github.com/allenai/molmoact2)
- **许可与访问说明**：不同子集、上游数据或配套资源适用不同条款
- **补充说明**：训练集合包含DROID、BC-Z、Bridge、RT-1及Ai2数据并分别继承上游条款；策略Rollout用于失败标注与奖励模型训练，不能与成功示范混为一类。

### [ARIO Dataset](https://imaei.github.io/project_pages/ario/)

- **规模与版本**：项目页报告约300万回合、258个系列和321064项任务
- **模态与表示**：Real;Simulation;Multi-Modal;Robot State;Action
- **具体本体／对象**：Multi-Robot;Manipulation;Navigation
- **获取方式**：项目页；[数据卡／项目来源](https://imaei.github.io/project_pages/ario/)
- **许可与访问说明**：不同子集、上游数据或配套资源适用不同条款
- **补充说明**：数据来自开源转换、团队仿真和真实机器人采集；团队自采或自建仿真材料采用CC BY 4.0或MIT，第三方转换数据继续遵循各自上游许可。

</details>

<a id="assets-perception"></a>

## 数字资产与感知评测资源

任务定义、场景资产与感知日志各有用途，不等同于可直接模仿的机器人动作轨迹。

| 数据集 | 数据内容 | 本体／对象 | 训练用途 |
| --- | --- | --- | --- |
| <a id="d019"></a>[BEHAVIOR-1K](https://behavior.stanford.edu/) | 日常任务定义、场景资产与示范资源 | 家庭移动操作 | 构建长程家庭任务和训练评测环境 |
| <a id="d032"></a>[ArtVIP](https://huggingface.co/datasets/X-Humanoid/ArtVIP) | 关节物体、场景及物理属性资产 | 仿真物体／场景 | 搭建交互场景，生成操作示范与合成数据 |
| <a id="d034"></a>[GrandTour Dataset](https://grandtour.leggedrobotics.com/) | 雷达、图像、IMU及本体感知记录 | ANYmal D | 研究状态估计、定位与复杂环境感知 |

<details>
<summary>规模、格式与获取方式</summary>

### [BEHAVIOR-1K](https://behavior.stanford.edu/)

- **规模与版本**：1000日常任务
- **模态与表示**：Task Definitions + Assets + Demonstrations
- **具体本体／对象**：移动操作
- **获取方式**：项目页；[数据卡／项目来源](https://behavior.stanford.edu/)
- **许可与访问说明**：不同子集、上游数据或配套资源适用不同条款
- **补充说明**：家庭任务体系；许可范围：BSD/数据许可分项

### [ArtVIP](https://huggingface.co/datasets/X-Humanoid/ArtVIP)

- **规模与版本**：476个关节物体；6个预配置交互场景；6个用户场景；约9.69 GB
- **模态与表示**：USD;3D Geometry;PBR Texture;Physical Parameter;Affordance
- **具体本体／对象**：Simulation;Articulated Object
- **获取方式**：平台下载；[数据卡／项目来源](https://huggingface.co/datasets/X-Humanoid/ArtVIP)
- **许可与访问说明**：Apache-2.0
- **补充说明**：核心产物是带关节、材质、物理参数和可供性的数字孪生资产，不是状态—动作示范轨迹；当前数据卡标注Apache-2.0，使用具体资产时仍应检查版本说明。

### [GrandTour Dataset](https://grandtour.leggedrobotics.com/)

- **规模与版本**：49+环境；5万步；15万图像；4万LiDAR点云
- **模态与表示**：LiDAR;RGB;Depth;IMU;Proprioception;RTK-GPS
- **具体本体／对象**：ANYmal D
- **获取方式**：按说明；[数据卡／项目来源](https://grandtour.leggedrobotics.com/)
- **许可与访问说明**：CC-BY-SA-4.0
- **补充说明**：数据许可为CC BY-SA 4.0、配套软件为MIT；多传感器时间同步精度标称1 ms，主要用于感知定位与状态估计而非动作模仿。

</details>

## 选用提示

- 人体动作、人类视频与采集器记录通常仍需动作恢复、重定向或本体映射，不能直接作为机器人电机命令。
- 先核对观测、动作、坐标、时钟与回合边界，再判断数据能否接入训练；仿真数据还需检查动力学与控制接口。
- 时长、帧数、片段与完整轨迹不是同一种统计口径；训练混合、转换版和镜像也不应重复计算。

## 专题阅读

| 专题 | 内容 |
| --- | --- |
| [具身训练数据来源与本体依赖](具身训练数据来源与本体依赖.md) | 数据如何进入训练、动作映射、数据卡检查与世界模型数据需求 |
| [Ego第一人称数据采集设备选型](Ego第一人称数据采集设备选型.md) | 采集设备、操作终端与数据平台的选型 |
| [RealOmni-Open](RealOmni-Open.md) | 从采集设备、记录格式与解析工具到数据分发和训练 |
| [Open-AoE](Open-AoE.md) | 从手机视频、手部恢复与动作标注到机器人训练转换 |
