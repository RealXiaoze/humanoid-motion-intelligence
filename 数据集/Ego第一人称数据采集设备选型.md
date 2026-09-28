# Ego第一人称采集设备与数据平台

> 汇总第一人称视觉设备、动作采集系统与数据平台，按采集内容和用途整理。

## 研究系统与工具

| 系统 | 采集或输出 | 主要用途 |
|---|---|---|
| [Project Aria Gen 2 Pilot](https://explorer.projectaria.com/gen2pilot/play_0) | RGB、VRS记录、相机标定、设备轨迹、手跟踪、深度与场景派生数据 | 第一视角感知、手物交互、定位与多传感器研究 |
| [EgoKit](https://www.chuange.org/papers/EgoKit.html) | 手机、平板、智能眼镜与XR设备的统一录制和日志；可接腕部相机，XR端提供头部与手部跟踪 | 用多种消费级设备采集第一视角与腕部视觉数据 |
| [DexCap（学术系统）](https://github.com/j96w/DexCap) | 胸前RGB-D、胸部及双手位姿、手部关节；提供处理、数据构建和策略训练代码 | 将可穿戴动作采集接入灵巧手重定向与Diffusion Policy训练 |
| [Tobii Pro Glasses 3](https://www.tobii.com/products/eye-trackers/wearables/tobii-pro-glasses-3) | 第一视角场景视频、眼动及时间对齐接口 | 分析注意力、视线目标与人类操作过程 |

## 第一人称采集设备

| 产品 | 采集或输出 | 主要用途 |
|---|---|---|
| [奥比中光 EGO RGB-D](https://www.orbbec.com.cn/index/News/info.html?cate=31&id=377) | 同步RGB、深度与IMU，提供公制深度与空间对齐 | 记录操作场景几何与手物交互 |
| [简智机器人 DAS Ego](https://cn.genrobot.com/products/ego) | 6路RGB、六轴IMU、空间轨迹与音频 | 采集大视场第一视角视频、惯性与运动轨迹 |
| [鹿明机器人 FastUMI Ego](https://www.news.cn/tech/20260314/e81f7585b7c94e1281f94cd4eb59202e/c.html) | RGB、IMU、ToF、世界坐标定位与双手跟踪，可配合FastUMI操作端 | 同时记录环境、操作者与手部操作轨迹 |
| [Kinetix AI Kai Halo](https://www.kinetixai.tech/zh/KaiEgo) | 多路鱼眼图像，以及场景重建、手部跟踪、全身姿态与动作语义处理 | 构建第一视角人体动作与手物交互数据 |
| [觅蜂科技 MEgo View](https://www.maniformer.net/mego) | 头戴及腕部共7摄RGB、深度、IMU、空间轨迹、音频与人体位姿信息 | 采集多视角人类操作，用于动作重建与操作学习 |
| [OmniEgo](https://omniego.com/) | 头戴双目、三维手姿、点云、SLAM轨迹及清洗标注工具 | 将第一视角采集连接到三维重建与数据处理 |
| [TOBI E2/E6/E8](https://www.tobi.cn/products.html) | RGB、IMU、时间戳、相机内外参与音频，配置按型号区分 | 采集多视角观察与传感器原始数据 |
| [松灵 Pika Pro Ego-centric](https://www.agilex.ai/page/690ac4905e78cfa260412ca1) | Pika Ego、移动计算单元与操作端协同记录视觉、深度、位姿和操作信息 | 采集第一视角与手部示范，连接标注和训练流程 |
| [PIA Primus Ego](https://cn.piagroup.com/news/company2/538.html) | 工业场景第一视角操作记录 | 采集工业任务中的人类操作示范 |
| [京东 JoyEgoCam](https://finance-app.people.cn/n1/2026/0417/c1004-40703454.html) | 第一视角采集终端，接入京东数据处理平台 | 连接数据采集、存储、标注、训练与评测 |

## 动作采集与数据平台

| 产品或平台 | 采集或处理内容 | 主要用途 |
|---|---|---|
| [觅蜂科技 MEgo Gripper](https://www.maniformer.net/mego) | 二指夹爪采集RGB、深度、IMU、空间轨迹、音频、触觉、夹爪角度与开口距离 | 记录抓取和接触操作示范 |
| [觅蜂科技 MEgo Engine](https://www.maniformer.net/mego) | 云端轨迹重建、人体位姿提取、质量检测与智能标注 | 将采集记录处理成结构化操作数据 |
| [觅蜂派](https://www.maniformer.net/mifengpai) | 采集任务分发、设备申领、录制上传、脱敏与有效时长核定 | 组织分布式人类操作数据采集 |
| [Lightwheel EgoSuite](https://lightwheel.ai/egosuite) | 组合VR、外骨骼与UMI式夹爪，处理RGB-D、手臂姿态、触觉、三维轨迹和语义 | 建设多设备协同采集与操作数据处理流程 |
| [DexRobot DexCap（商业外骨骼）](https://www.dex-robot.com/dexCap) | 全身外骨骼记录手、手臂、腰部等动作，提供C++、Python与ROS接口 | 采集全身动作示范，接入遥操作与重定向 |
| [Sunday Robotics Skill Capture Glove](https://www.sunday.ai/) | 手套采集家庭操作示范，供Memo技能学习使用 | 从人类示范学习家庭任务 |

## 相关数据资源

| 资源 | 数据内容与用途 |
|---|---|
| [KAI Ego Data Minibatch](README.md#d039) | 约3小时第一视角交互样例，含相机参数、跟踪与语义分段，用于手物交互和数据处理实验 |
| [RealOmni-Open](RealOmni-Open.md) | 双手操作视频、末端位姿与夹爪状态，用于人类示范学习与本体动作映射 |
| [Open-AoE](Open-AoE.md) | 手机第一视角视频、手部和相机轨迹、动作标注，用于操作表征与机器人学习 |

[数据集总览](README.md) · [动作数据与重定向](../技术与研究/01_动作数据与重定向.md)
