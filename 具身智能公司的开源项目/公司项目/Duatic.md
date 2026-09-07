# Duatic

> 本页集中展示能够核验为Duatic官方发布或维护、具有公开代码托管入口的项目。公开仓库不等于训练、权重、数据和部署链路已经完整开放。

## 主体信息

- **国家或地区**：瑞士
- **项目数量**：4
- **公司与产品记录**：[查看主体主表](../../公司与产业/公司与产品主表.md#c154)

## 官方公开项目

| 项目 | 技术位置 | 解决的问题 | 来源 |
| --- | --- | --- | --- |
| [duatic_dynaarm](https://github.com/Duatic/duatic_dynaarm) | 工程基础与工具 | 在ros2_control硬件抽象上连接DynaArm驱动、机器人描述和Demo，使运动命令与实际关节状态进入统一ROS 2接口。适合开发机械臂控制与规划集成，硬件版本和工作空间约束仍需独立验证。 | [官方入口](https://github.com/Duatic/duatic_dynaarm)<br>[归属证据](https://github.com/Duatic/duatic_dynaarm) |
| [duatic_ros2control](https://github.com/Duatic/duatic_ros2control) | 工程基础与工具 | 将DuaDrives封装为ros2_control硬件接口，连接驱动状态与控制命令，作为机械臂或机器人控制器的底层适配。应先检查状态接口、命令模式、EtherCAT与故障处理，再接入上层学习策略。 | [官方入口](https://github.com/Duatic/duatic_ros2control)<br>[归属证据](https://github.com/Duatic/duatic_ros2control) |
| [duatic_teleop](https://github.com/Duatic/duatic_teleop) | LocoManip与物理交互 / 全身协同与技能接口 | 把人类输入设备接入模块化ROS 2遥操作流程，供机器人控制与示范采集使用。任务空间输入到关节执行仍依赖对应本体与控制接口；跨设备映射、同步与录制格式需按实际配置检查。 | [官方入口](https://github.com/Duatic/duatic_teleop)<br>[归属证据](https://github.com/Duatic/duatic_teleop) |
| [duatic_gazebo](https://github.com/Duatic/duatic_gazebo) | 工程基础与工具 | 提供Duatic机器人开发使用的Gazebo配套资源，与机械臂描述和控制接口组成仿真测试入口。适合验证接口与场景配置，不将仿真包存在视为已公开RL任务或经过Sim2Real验证。 | [官方入口](https://github.com/Duatic/duatic_gazebo)<br>[归属证据](https://github.com/Duatic/duatic_gazebo) |

## 使用边界

- 官方发布或维护只能证明项目归属，不能自动证明完整开源、完整复现、持续维护或量产使用。
- 代码许可证不自动覆盖模型权重、训练数据、机器人资产、视频和硬件设计。
- 真机支持表示公开材料存在接口或部署证据，不代表所有机器人版本和控制参数都能直接运行。

## 导航

[返回公司开源项目总览](../README.md) · [查看全部公司与产品](../../公司与产业/公司与产品主表.md) · [查看全部开源项目](../../论文与项目/开源项目主表.md)
