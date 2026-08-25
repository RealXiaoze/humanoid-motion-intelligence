# Hugging Face Robotics

> 本页集中展示能够核验为Hugging Face Robotics官方发布或维护、具有公开代码托管入口的项目。公开仓库不等于训练、权重、数据和部署链路已经完整开放。

## 主体信息

- **国家或地区**：美国/法国
- **项目数量**：5
- **公司与产品记录**：[查看主体主表](../../公司与产业/公司与产品主表.md#c033)

## 官方公开项目

| 项目 | 技术位置 | 解决的问题 | 来源 |
| --- | --- | --- | --- |
| [LeRobot](https://github.com/huggingface/lerobot) | 工程基础与工具 | Robot接口、示范采集、Parquet加视频的数据格式、策略训练和部署在同一生态中衔接。开发新本体时，可先实现硬件与数据接口，再复用现成策略，快速判断瓶颈在数据质量还是模型。 | [官方入口](https://github.com/huggingface/lerobot)<br>[归属证据](https://github.com/huggingface/lerobot) |
| [robotics-course](https://github.com/huggingface/robotics-course) | AMP运动先验与Locomotion / 基础Locomotion | 仿真中的机器人模型、观测、奖励和随机化进入并行强化学习训练，输出可供回放和部署的运动策略。 | [官方入口](https://github.com/huggingface/robotics-course)<br>[归属证据](https://github.com/huggingface/robotics-course) |
| [gym-hil](https://github.com/huggingface/gym-hil) | Mimic动作跟踪与全身控制 / 实时人体驱动与遥操作闭环 | 头手、相机或主从设备输入经过坐标标定和动作映射形成机器人目标，同时记录观测、状态与动作供回放和训练。 | [官方入口](https://github.com/huggingface/gym-hil)<br>[归属证据](https://github.com/huggingface/gym-hil) |
| [gym-aloha](https://github.com/huggingface/gym-aloha) | 工程基础与工具 | 机器人模型、场景和控制接口接入仿真器，用于控制器联调、策略回放、Sim2Sim与部署前验证。 | [官方入口](https://github.com/huggingface/gym-aloha)<br>[归属证据](https://github.com/huggingface/gym-aloha) |
| [lerobot-annotate](https://github.com/huggingface/lerobot-annotate) | 动作数据入口与重定向 / 人形训练数据构建 | 相机、机器人状态、动作和任务边界被同步记录、转换或评估，形成可进入LeRobot、RLDS或公司训练栈的数据。 | [官方入口](https://github.com/huggingface/lerobot-annotate)<br>[归属证据](https://github.com/huggingface/lerobot-annotate) |

## 使用边界

- 官方发布或维护只能证明项目归属，不能自动证明完整开源、完整复现、持续维护或量产使用。
- 代码许可证不自动覆盖模型权重、训练数据、机器人资产、视频和硬件设计。
- 真机支持表示公开材料存在接口或部署证据，不代表所有机器人版本和控制参数都能直接运行。

## 导航

[返回公司开源项目总览](../README.md) · [查看全部公司与产品](../../公司与产业/公司与产品主表.md) · [查看全部开源项目](../../论文与项目/开源项目主表.md)
