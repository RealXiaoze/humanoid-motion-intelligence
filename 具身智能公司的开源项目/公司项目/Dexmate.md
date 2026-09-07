# Dexmate

> 本页集中展示能够核验为Dexmate官方发布或维护、具有公开代码托管入口的项目。公开仓库不等于训练、权重、数据和部署链路已经完整开放。

## 主体信息

- **国家或地区**：美国
- **项目数量**：5
- **公司与产品记录**：[查看主体主表](../../公司与产业/公司与产品主表.md#c155)

## 官方公开项目

| 项目 | 技术位置 | 解决的问题 | 来源 |
| --- | --- | --- | --- |
| [dexcontrol](https://github.com/dexmate-ai/dexcontrol) | 工程基础与工具 | 为Dexmate机器人提供运动命令、传感读取、遥操作与故障诊断示例，是策略或采集程序接入Vega的接口层。SDK与机器人固件按次版本配套，先检查版本与状态再执行动作，不能直接跨固件复用配置。 | [官方入口](https://github.com/dexmate-ai/dexcontrol)<br>[归属证据](https://github.com/dexmate-ai/dexcontrol) |
| [dexmate-urdf](https://github.com/dexmate-ai/dexmate-urdf) | 工程基础与工具 | 公开Dexmate本体描述，供可视化、运动学、逆运动学与仿真接入使用。需要与dexcontrol实际关节名称、零位和限制对齐，URDF可用不等于碰撞和惯量已经完成任务级标定。 | [官方入口](https://github.com/dexmate-ai/dexmate-urdf)<br>[归属证据](https://github.com/dexmate-ai/dexmate-urdf) |
| [omniteleop](https://github.com/dexmate-ai/omniteleop) | LocoManip与物理交互 / 全身协同与技能接口 | 支持JoyCon、Dynamixel外骨骼与VR相对位姿输入，经命令处理器、急停和关节限制进入机器人控制；提供MDP录制、轨迹回放、关节遥测及Web界面。适合把人类遥操作接到Vega示范采集，但设备映射和时间同步仍需实测，自主策略要另行训练。 | [官方入口](https://github.com/dexmate-ai/omniteleop)<br>[归属证据](https://github.com/dexmate-ai/omniteleop) |
| [dexdata](https://github.com/dexmate-ai/dexdata) | 动作数据入口与重定向 / 人形训练数据构建 | 用Protobuf和MCAP记录或回放机器人状态、动作、RGB与深度，回合由state_action.mcap、相机文件和info.json组成；可导出NumPy字典、视频与Rerun可视化。适合检查观测动作对齐并建立学习输入，不应把记录工具当成已有规模化训练数据集。 | [官方入口](https://github.com/dexmate-ai/dexdata)<br>[归属证据](https://github.com/dexmate-ai/dexdata) |
| [dexcontrol-rosbridge](https://github.com/dexmate-ai/dexcontrol-rosbridge) | 工程基础与工具 | 在dexcontrol与ROS生态之间提供桥接，使现有机器人节点能够接入Dexmate控制与状态流。它解决通信集成问题，不替代动作规划、低层保护或学习算法；时序和异常处理需在目标系统中复核。 | [官方入口](https://github.com/dexmate-ai/dexcontrol-rosbridge)<br>[归属证据](https://github.com/dexmate-ai/dexcontrol-rosbridge) |

## 使用边界

- 官方发布或维护只能证明项目归属，不能自动证明完整开源、完整复现、持续维护或量产使用。
- 代码许可证不自动覆盖模型权重、训练数据、机器人资产、视频和硬件设计。
- 真机支持表示公开材料存在接口或部署证据，不代表所有机器人版本和控制参数都能直接运行。

## 导航

[返回公司开源项目总览](../README.md) · [查看全部公司与产品](../../公司与产业/公司与产品主表.md) · [查看全部开源项目](../../论文与项目/开源项目主表.md)
