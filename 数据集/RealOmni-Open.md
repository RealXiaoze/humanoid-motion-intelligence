# RealOmni-Open：真实家庭双手操作数据

> 简智机器人使用GenDAS双手采集设备记录家庭操作示范，将视觉、末端运动和夹爪状态用于机器人操作模仿、VLA预训练与双手协作研究。

## 数据内容

| 内容 | 记录或提供什么 |
|---|---|
| 视觉与标定 | 鱼眼相机视频、相机内外参 |
| 设备运动 | IMU、VIO估计的左右末端位姿、线速度与角速度 |
| 操作状态 | 左右采集端的夹爪开合状态 |
| 深度与触觉 | 部分采集批次提供的附加观测 |
| 回合与任务 | 按操作回合组织的多模态时间序列与任务记录 |

## 主要用途

| 训练方向 | 数据怎样使用 |
|---|---|
| 操作表征预训练 | 联合学习家庭场景视频与末端动作 |
| 模仿学习与VLA | 构建视觉、任务与动作序列样本 |
| 双手协作与长时任务 | 学习双手配合、连续操作和家庭任务过程 |
| 跨本体动作适配 | 将采集端的末端轨迹和夹爪状态映射到目标机器人 |

## 规模与格式

| 项目 | 说明 |
|---|---|
| 发布方报告规模 | 13000+小时、500万+片段；按发布方统计口径记录 |
| 百度百舸早期上传批次 | 950小时、39761段、约3.45 TB |
| 原始格式 | MCAP多模态时间序列；`robot0`与`robot1`表示左右采集端 |
| 处理工具 | das-datakit支持数据读取和MCAP转H5 |

## 工具与官方链接

| 入口 | 用途 |
|---|---|
| [简智机器人官方页面](https://cn.genrobot.com/data/open-dataset) | 数据介绍与发布信息 |
| [Hugging Face](https://huggingface.co/datasets/genrobot2025/10Kh-RealOmin-OpenData) | 数据卡与文件访问 |
| [ModelScope](https://modelscope.cn/datasets/GenRobot.AI/10Kh-RealOmin-OpenData) | 数据分发 |
| [das-datakit](https://github.com/genrobot-ai/das-datakit) | 读取相机、深度、触觉与设备状态，转换训练文件 |
| [百度百舸](https://cloud.baidu.com/doc/AIHC/s/xmk22jsl8) | 数据挂载与云端训练说明 |
| [LoongForge](https://github.com/baidu-baige/LoongForge) | 配套参考：VLA等模型的分布式训练框架 |

[返回具身智能数据集](README.md) · [Open-AoE手机操作数据](Open-AoE.md) · [Ego采集设备与数据平台](Ego第一人称数据采集设备选型.md)
