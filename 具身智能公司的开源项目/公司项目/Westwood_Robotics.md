# Westwood Robotics

> 本页集中展示能够核验为Westwood Robotics官方发布或维护、具有公开代码托管入口的项目。公开仓库不等于训练、权重、数据和部署链路已经完整开放。

## 主体信息

- **国家或地区**：美国
- **项目数量**：4
- **公司与产品记录**：[查看主体主表](../../公司与产业/公司与产品主表.md#c153)

## 官方公开项目

| 项目 | 技术位置 | 解决的问题 | 来源 |
| --- | --- | --- | --- |
| [BRUCE simulation models](https://github.com/Westwood-Robotics/BRUCE_simulation_models) | 工程基础与工具 | 提供BRUCE在Gazebo与MuJoCo中的机器人模型，供几何、关节、碰撞与控制接口对照。它是本体资产入口，不包含完整RL训练流程；另一个BRUCE-OP仓库公开的控制器为二进制，不能混写为完整开源WBC。 | [官方入口](https://github.com/Westwood-Robotics/BRUCE_simulation_models)<br>[归属证据](https://github.com/Westwood-Robotics/BRUCE_simulation_models) |
| [THEMIS Simulation Model](https://github.com/Westwood-Robotics/THEMIS-Simulation-Model) | 工程基础与工具 | 提供THEMIS机器人仿真模型，为运动学、关节与物理资产检查提供入口。接入动作重定向或策略训练时仍需补充任务、观测、动作、奖励与执行器约束，不能只凭仿真模型认定训练栈已开放。 | [官方入口](https://github.com/Westwood-Robotics/THEMIS-Simulation-Model)<br>[归属证据](https://github.com/Westwood-Robotics/THEMIS-Simulation-Model) |
| [PyBEAR](https://github.com/Westwood-Robotics/PyBEAR) | 工程基础与工具 | 通过Python与BEAR系列执行器通信，支持驱动参数与状态访问等开发操作。它位于上层关节命令和执行器之间，适合检查通信及配置链路；控制安全、零位、力矩限制和实时性仍由具体机器人系统负责。 | [官方入口](https://github.com/Westwood-Robotics/PyBEAR)<br>[归属证据](https://github.com/Westwood-Robotics/PyBEAR) |
| [EN02-OP](https://github.com/Westwood-Robotics/EN02-OP) | 工程基础与工具 | 公开三指七自由度末端的STEP结构、打印零件、BOM、电路和装配指南，适合研究低成本末端结构与机械臂安装。执行器采用Dynamixel，仓库明确尚无专用控制软件，因此不是灵巧操作训练框架。 | [官方入口](https://github.com/Westwood-Robotics/EN02-OP)<br>[归属证据](https://github.com/Westwood-Robotics/EN02-OP) |

## 使用边界

- 官方发布或维护只能证明项目归属，不能自动证明完整开源、完整复现、持续维护或量产使用。
- 代码许可证不自动覆盖模型权重、训练数据、机器人资产、视频和硬件设计。
- 真机支持表示公开材料存在接口或部署证据，不代表所有机器人版本和控制参数都能直接运行。

## 导航

[返回公司开源项目总览](../README.md) · [查看全部公司与产品](../../公司与产业/公司与产品主表.md) · [查看全部开源项目](../../论文与项目/开源项目主表.md)
