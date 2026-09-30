# 具身智能数据集

> 汇总具身智能训练与评测相关的数据集、训练数据配方及仿真资产，涵盖人体动作、人类操作视频、机器人示范、重定向轨迹与合成数据，按数据来源与内容整理。

当前收录：**42项数据集与相关数据资源**。

## 分类导航

[人体动作与语言](#human-motion) · [人类视频与操作示范](#human-demonstration) · [重定向与目标本体动作](#retargeted-motion) · [真实机器人示范与运行数据](#robot-demonstration) · [仿真合成与生成式数据](#synthetic-data) · [跨来源训练集合与配方](#training-mixtures) · [数字资产与感知评测资源](#assets-perception)

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
<summary>规模、格式与官方来源</summary>

### AMASS

- **规模**：多数据集统一，规模见官网
- **模态与格式**：MoCap/SMPL
- **具体本体／对象**：Human
- **官方来源**：[数据卡／项目来源](https://amass.is.tue.mpg.de/)

### CMU Motion Capture Database

- **规模**：多类动作序列
- **模态与格式**：MoCap
- **具体本体／对象**：Human
- **官方来源**：[数据卡／项目来源](http://mocap.cs.cmu.edu/)

### HumanML3D

- **规模**：文本动作对
- **模态与格式**：Text + Motion
- **具体本体／对象**：Human
- **官方来源**：[数据卡／项目来源](https://github.com/EricGuo5513/HumanML3D)

### KIT Motion-Language Dataset

- **规模**：文本描述动作
- **模态与格式**：Text + MoCap
- **具体本体／对象**：Human
- **官方来源**：[数据卡／项目来源](https://motion-annotation.humanoids.kit.edu/)

### AIST++

- **规模**：舞蹈动作
- **模态与格式**：Video + 3D Motion + Music
- **具体本体／对象**：Human
- **官方来源**：[数据卡／项目来源](https://google.github.io/aistplusplus_dataset/)

### Motion-X

- **规模**：大规模全身动作
- **模态与格式**：3D Motion + Text
- **具体本体／对象**：Human
- **官方来源**：[数据卡／项目来源](https://motion-x-dataset.github.io/)

### Human3.6M

- **规模**：室内动作
- **模态与格式**：Video + 3D Pose
- **具体本体／对象**：Human
- **官方来源**：[数据卡／项目来源](http://vision.imar.ro/human3.6m/description.php)

### LaFAN1

- **规模**：动作过渡片段
- **模态与格式**：Motion Sequences
- **具体本体／对象**：Human
- **官方来源**：[数据卡／项目来源](https://github.com/ubisoft/ubisoft-laforge-animation-dataset)

### OMOMO

- **规模**：15种物体，约10小时人-物交互动作
- **模态与格式**：3D Object Geometry;Object Motion;Human Motion
- **具体本体／对象**：Human;Object
- **官方来源**：[数据卡／项目来源](https://github.com/lijiaman/omomo_release)

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
| <a id="d041"></a>[EgoHTR](https://huggingface.co/datasets/leggedrobotics/egohtr) | 复杂地形中的场景对齐4D人体运动序列，包含SMPL-X人体模型、第一视角视频与SLAM轨迹、原始IMU、三维场景网格和点云；部分片段还提供第二视角、固定相机和动捕真值。 | 8名人类被试；下游示范与控制验证包含Unitree G1 | 评测第一视角人体姿态与人体-场景4D重建；为复杂地形人体动作分析、参考动作重定向和基于场景几何的人形感知Locomotion训练提供数据。论文以重定向后的参考动作训练G1专家策略，并测试接触奖励与参考位置误差的影响。 |

<details>
<summary>规模、格式与官方来源</summary>

### Ego-Exo4D

- **规模**：多视角技能视频
- **模态与格式**：Ego/Exo Video + Pose + Audio
- **具体本体／对象**：Human
- **官方来源**：[数据卡／项目来源](https://ego-exo4d-data.org/)

### RealOmni-Open

- **规模**：发布方报告13000+小时与500万+片段；Hugging Face当前展示约36.9 TB
- **模态与格式**：Fisheye RGB;Camera Calibration;IMU;End-Effector Pose;Gripper State;Optional Depth;Optional Tactile
- **具体本体／对象**：Human + GenDAS Gripper;No Target Robot
- **官方来源**：[数据卡／项目来源](https://cn.genrobot.com/data/open-dataset)

### Open-AoE-2000H

- **规模**：约2000小时；500+采集者；400+智能手机
- **模态与格式**：Calibrated RGB;MANO Hand Pose;Camera Trajectory;Validity Mask;Bilingual Atomic Action
- **具体本体／对象**：Human + Consumer Smartphone;No Target Robot
- **官方来源**：[数据卡／项目来源](https://github.com/ant-research/Open-AoE)

### World In Your Hands

- **规模**：1045小时RGB与标定；800小时深度；500小时动作；400小时指令；320小时推理；240小时掩码；10小时触觉
- **模态与格式**：Multi-View RGB;Calibration;Depth;3D Wrist Pose;Hand Skeleton;Tactile;Mask;Instruction;Reasoning
- **具体本体／对象**：Human;Cross-Embodiment;Dexterous Hand
- **官方来源**：[数据卡／项目来源](https://wiyh.tars-ai.com/)

### KAI Ego Data Minibatch

- **规模**：约3小时完整处理数据包；数据卡显示63.7 GB
- **模态与格式**：Ego Video;Camera Parameters;Tracking;Semantic Segments;Quality Inspection
- **具体本体／对象**：Human;No Target Robot
- **官方来源**：[数据卡／项目来源](https://huggingface.co/datasets/Kinetix-AI/kai-data-minibatch)

### EgoHTR

- **规模**：7个场景；55段序列；约1.37小时、约15万帧@30fps；36段多视角序列约0.88小时；约0.7小时动捕真值测试子集
- **模态与格式**：Ego RGB; SLAM trajectory; IMU; SMPL-X; Scene mesh; Point cloud; Optional exocentric video; MoCap ground truth subset
- **具体本体／对象**：8名人类被试；下游示范与控制验证包含Unitree G1
- **官方来源**：[数据卡／项目来源](https://huggingface.co/datasets/leggedrobotics/egohtr)

</details>

<a id="retargeted-motion"></a>

## 重定向与目标本体动作

| 数据集 | 数据内容 | 本体／对象 | 训练用途 |
| --- | --- | --- | --- |
| <a id="d010"></a>[Humanoid-X](https://huggingface.co/datasets/USC-PSI-Lab/Humanoid-X) | 人类视频与人形动作数据 | 人体／人形机器人 | 研究视频模仿及人体到机器人动作转换 |
| <a id="d011"></a>[PHUMA](https://github.com/DAVIAN-Robotics/PHUMA) | 人体动作与目标机器人重定向动作 | G1、H1-2等 | 构建物理可行动作参考，研究重定向与动作跟踪 |
| <a id="d026"></a>[OmniContact Dataset](https://huggingface.co/datasets/lightcone02/OmniContact-Dataset) | 人体-物体动作、G1轨迹与接触标签 | 人体／G1／物体 | 学习接触感知参考与全身移动操作 |
| <a id="d031"></a>[LAFAN1 Retargeting Dataset](https://huggingface.co/datasets/lvhaidong/LAFAN1_Retargeting_Dataset) | 由LaFAN1转换的关节与根节点轨迹 | H1、H1-2、G1 | 训练目标本体动作跟踪与运动模仿 |
| <a id="d040"></a>[AMS Synthetic Balance Motions](https://github.com/OpenDriveLab/AMS/blob/main/MotionGen/README.md) | 目标本体根节点、关节与支撑腿参考 | G1 29自由度 | 扩展平衡动作参考，研究动作跟踪与参考质量 |
| <a id="d042"></a>[Weave reference motions and simulation rollouts](https://huggingface.co/datasets/appolyn/Weave) | 保留人—物交互的机器人参考动作、策略仿真执行轨迹与九种物体资产，包含身体、手部、物体状态及接触标签。 | Unitree G1与双Inspire灵巧手；人—物交互 | 用于人形全身移动操作策略学习、评测，以及带物理接触标注的人—物交互动作建模。 |

<details>
<summary>规模、格式与官方来源</summary>

### Humanoid-X

- **规模**：规模见项目页
- **模态与格式**：Human Video + Humanoid Motion
- **具体本体／对象**：Human/Humanoid
- **官方来源**：[数据卡／项目来源](https://huggingface.co/datasets/USC-PSI-Lab/Humanoid-X)

### PHUMA

- **规模**：预构建G1/H1-2动作库，规模见官方数据卡
- **模态与格式**：SMPL-X Human Motion;Retargeted Robot Motion
- **具体本体／对象**：Unitree G1;Unitree H1-2;Custom Humanoid
- **官方来源**：[数据卡／项目来源](https://github.com/DAVIAN-Robotics/PHUMA)

### OmniContact Dataset

- **规模**：公开仓库当前列出700条处理轨迹；项目页汇总1274条有效序列与22.29小时配对采集
- **模态与格式**：BVH;G1 Joint Trajectory;Object Pose;Contact Label
- **具体本体／对象**：Human;Unitree G1;Object
- **官方来源**：[数据卡／项目来源](https://huggingface.co/datasets/lightcone02/OmniContact-Dataset)

### LAFAN1 Retargeting Dataset

- **规模**：314 MB；由LAFAN1逐帧重定向到3种人形本体
- **模态与格式**：Root Pose;Joint Configuration;30 FPS
- **具体本体／对象**：Unitree H1;H1_2;G1
- **官方来源**：[数据卡／项目来源](https://huggingface.co/datasets/lvhaidong/LAFAN1_Retargeting_Dataset)

### AMS Synthetic Balance Motions

- **规模**：约10000条合成平衡序列
- **模态与格式**：Root Position;Quaternion;Joint Position;Axis-Angle Pose;FPS;Stance Leg
- **具体本体／对象**：Unitree G1 29-DoF
- **官方来源**：[数据卡／项目来源](https://github.com/OpenDriveLab/AMS/blob/main/MotionGen/README.md)

### Weave reference motions and simulation rollouts

- **规模**：参考动作9,474段、23.2小时；仿真执行轨迹8,699段、21.2小时；物体资产9种。
- **模态与格式**：50 Hz关节与刚体状态、物体位姿与速度、接触标签；网格、USD、SDF与表面点
- **具体本体／对象**：Unitree G1与双Inspire灵巧手；人—物交互
- **官方来源**：[数据卡／项目来源](https://huggingface.co/datasets/appolyn/Weave)

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
<summary>规模、格式与官方来源</summary>

### DROID

- **规模**：规模见项目页
- **模态与格式**：Multi-view Video + Proprioception + Actions
- **具体本体／对象**：多机械臂
- **官方来源**：[数据卡／项目来源](https://droid-dataset.github.io/)

### BridgeData V2

- **规模**：规模见项目页
- **模态与格式**：Video + Actions + Language
- **具体本体／对象**：机械臂
- **官方来源**：[数据卡／项目来源](https://rail-berkeley.github.io/bridgedata/)

### RoboNet

- **规模**：规模见项目页
- **模态与格式**：Video + Actions
- **具体本体／对象**：多机械臂
- **官方来源**：[数据卡／项目来源](https://www.robonet.wiki/)

### RH20T

- **规模**：规模见项目页
- **模态与格式**：Multi-modal Sensor + Actions
- **具体本体／对象**：多机械臂
- **官方来源**：[数据卡／项目来源](https://rh20t.github.io/)

### RoboMIND

- **规模**：V1.2 107k轨迹/479任务/96物体类/4本体；V2.0官方集合称新增300k+双臂轨迹/6本体/739任务/129技能/12k+触觉数据
- **模态与格式**：Multi-view + Proprioception + Language + Tactile
- **具体本体／对象**：多机器人/人形
- **官方来源**：[数据卡／项目来源](https://huggingface.co/datasets/x-humanoid-robomind/RoboMIND)

### AGIBOT WORLD 2026

- **规模**：持续分主题发布；当前覆盖模仿学习、物理交互与世界模型、真机强化学习数据，具体规模按各期数据卡
- **模态与格式**：RGB;Depth;Tactile;LiDAR;IMU;Whole-Body State;Force/Torque;Language;Policy Rollout;Human Intervention
- **具体本体／对象**：AGIBOT G2;OmniPicker;OmniHand
- **官方来源**：[数据卡／项目来源](https://huggingface.co/datasets/agibot-world/AgiBotWorld2026)

### Humanoid Everyday

- **规模**：10.3k轨迹；300万余帧；260任务；7类别；30 Hz
- **模态与格式**：RGB;Depth;LiDAR;Tactile;IMU;Joint State;Action;Language
- **具体本体／对象**：Unitree G1;Unitree H1
- **官方来源**：[数据卡／项目来源](https://humanoideveryday.github.io/)

### OpenHLM-data

- **规模**：约298 GB
- **模态与格式**：Camera;Language;Whole-Body Joint Action
- **具体本体／对象**：Humanoid
- **官方来源**：[数据卡／项目来源](https://huggingface.co/datasets/OpenHLM/OpenHLM-data)

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
<summary>规模、格式与官方来源</summary>

### RoboCasa365

- **规模**：365类任务/多厨房
- **模态与格式**：Simulation + Demonstrations + Assets
- **具体本体／对象**：机械臂/移动操作
- **官方来源**：[数据卡／项目来源](https://robocasa.ai/)

### MimicGen Datasets

- **规模**：多任务/多版本
- **模态与格式**：Simulation Demonstrations
- **具体本体／对象**：机械臂
- **官方来源**：[数据卡／项目来源](https://mimicgen.github.io/)

### DexMimicGen Datasets

- **规模**：规模见项目页
- **模态与格式**：Simulation Demonstrations
- **具体本体／对象**：双臂/灵巧手
- **官方来源**：[数据卡／项目来源](https://dexmimicgen.github.io/)

### GRAIL Generated Loco-Manipulation Dataset

- **规模**：20,000余条序列；约250 GB；多类拾取、坐下与地形动作
- **模态与格式**：Synthetic Video;4D HOI;G1 Trajectory;Object 6DoF;USD Asset
- **具体本体／对象**：Unitree G1;SMPL-X;Object
- **官方来源**：[数据卡／项目来源](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-Locomanipulation-GRAIL)

### NVIDIA GR00T X-Embodiment Sim

- **规模**：跨本体双臂9k轨迹；GR1人形桌面操作240k轨迹；另有单臂与G1 LocoManip子集
- **模态与格式**：Simulation Trajectory;Robot State;Action;Task
- **具体本体／对象**：Panda Gripper/Hand;Fourier GR1;Unitree G1
- **官方来源**：[数据卡／项目来源](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-GR00T-X-Embodiment-Sim)

### HumanGen

- **规模**：论文报告：7.42万对人机上下文样本；8600个任务
- **模态与格式**：Generated Human Video;Robot Video;Executable Action;Language;Task Metadata
- **具体本体／对象**：Human + 45+ Robot Embodiments
- **官方来源**：[数据卡／项目来源](https://github.com/robbyant-research/Zero-WAM)

</details>

<a id="training-mixtures"></a>

## 跨来源训练集合与配方

| 数据集 | 数据内容 | 本体／对象 | 训练用途 |
| --- | --- | --- | --- |
| <a id="d012"></a>[Open X-Embodiment](https://robotics-transformer-x.github.io/) | 跨机构、跨机器人的操作数据合集 | 多种机器人 | 统一观测与动作字段，训练跨本体通用策略 |
| <a id="d028"></a>[MolmoAct Dataset与训练数据配方](https://github.com/allenai/molmoact) | 自采示范与多源动作推理训练配方 | Franka、WidowX等 | 开展VLA预训练、中期训练与动作推理学习 |
| <a id="d029"></a>[MolmoAct2训练集合与策略Rollout](https://github.com/allenai/molmoact2) | 跨本体训练集合与策略执行轨迹 | SO-100/101、Franka等 | 研究VLA微调、失败标注及奖励建模 |
| <a id="d033"></a>[ARIO Dataset](https://imaei.github.io/project_pages/ario/) | 统一格式的真实、仿真及转换数据 | 多种机器人 | 统一多源数据，研究跨机器人操作与导航 |

<details>
<summary>规模、格式与官方来源</summary>

### Open X-Embodiment

- **规模**：跨机构数据集合集
- **模态与格式**：Images + States + Actions + Language
- **具体本体／对象**：多机器人
- **官方来源**：[数据卡／项目来源](https://robotics-transformer-x.github.io/)

### MolmoAct Dataset与训练数据配方

- **规模**：自采约10k轨迹/93任务；原始表约111万帧行；预训练混合约2410万样本
- **模态与格式**：Multi-View RGB;Robot State;Action;Language;Depth Token;Visual Trace
- **具体本体／对象**：Franka;Google Robot;WidowX;Mixed
- **官方来源**：[数据卡／项目来源](https://github.com/allenai/molmoact)

### MolmoAct2训练集合与策略Rollout

- **规模**：多个训练集合；评测Rollout覆盖多任务与ID/OOD设置，规模按子数据卡
- **模态与格式**：LeRobot v3.0;RGB;Robot State;Action;Language;Policy Rollout
- **具体本体／对象**：SO-100/101;Franka;Bimanual YAM;Mixed
- **官方来源**：[数据卡／项目来源](https://github.com/allenai/molmoact2)

### ARIO Dataset

- **规模**：项目页报告约300万回合、258个系列和321064项任务
- **模态与格式**：Real;Simulation;Multi-Modal;Robot State;Action
- **具体本体／对象**：Multi-Robot;Manipulation;Navigation
- **官方来源**：[数据卡／项目来源](https://imaei.github.io/project_pages/ario/)

</details>

<a id="assets-perception"></a>

## 数字资产与感知评测资源

| 数据集 | 数据内容 | 本体／对象 | 训练用途 |
| --- | --- | --- | --- |
| <a id="d019"></a>[BEHAVIOR-1K](https://behavior.stanford.edu/) | 日常任务定义、场景资产与示范资源 | 家庭移动操作 | 构建长程家庭任务和训练评测环境 |
| <a id="d032"></a>[ArtVIP](https://huggingface.co/datasets/X-Humanoid/ArtVIP) | 关节物体、场景及物理属性资产 | 仿真物体／场景 | 搭建交互场景，生成操作示范与合成数据 |
| <a id="d034"></a>[GrandTour Dataset](https://grandtour.leggedrobotics.com/) | 雷达、图像、IMU及本体感知记录 | ANYmal D | 研究状态估计、定位与复杂环境感知 |

<details>
<summary>规模、格式与官方来源</summary>

### BEHAVIOR-1K

- **规模**：1000日常任务
- **模态与格式**：Task Definitions + Assets + Demonstrations
- **具体本体／对象**：移动操作
- **官方来源**：[数据卡／项目来源](https://behavior.stanford.edu/)

### ArtVIP

- **规模**：476个关节物体；6个预配置交互场景；6个用户场景；约9.69 GB
- **模态与格式**：USD;3D Geometry;PBR Texture;Physical Parameter;Affordance
- **具体本体／对象**：Simulation;Articulated Object
- **官方来源**：[数据卡／项目来源](https://huggingface.co/datasets/X-Humanoid/ArtVIP)

### GrandTour Dataset

- **规模**：49+环境；5万步；15万图像；4万LiDAR点云
- **模态与格式**：LiDAR;RGB;Depth;IMU;Proprioception;RTK-GPS
- **具体本体／对象**：ANYmal D
- **官方来源**：[数据卡／项目来源](https://grandtour.leggedrobotics.com/)

</details>

## 专题阅读

| 专题 | 内容 |
| --- | --- |
| [具身训练数据来源与用途](具身训练数据来源与本体依赖.md) | 人类视频、动捕、机器人示范与仿真数据的内容和训练用途 |
| [Ego第一人称采集设备与数据平台](Ego第一人称数据采集设备选型.md) | 设备采集哪些信号、平台处理什么数据、用于哪些任务 |
| [RealOmni-Open](RealOmni-Open.md) | 从采集设备、记录格式与解析工具到数据分发和训练 |
| [Open-AoE](Open-AoE.md) | 从手机视频、手部恢复与动作标注到机器人训练转换 |
