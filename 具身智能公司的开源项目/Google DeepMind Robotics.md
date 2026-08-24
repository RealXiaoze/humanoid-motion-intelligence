# Google DeepMind Robotics

> 本页集中展示能够核验为Google DeepMind Robotics官方发布或维护、具有代码入口和明确许可证的项目。

## 主体信息

- **稳定编号**：`C030`
- **国家或地区**：英国
- **项目数量**：4
- **公司与产品记录**：[查看主体主表](../公司与产业/公司与产品主表.md#c030)

## 官方开源项目

| 项目 | 技术位置 | 解决的问题 | 开放与维护 | 来源 |
| --- | --- | --- | --- | --- |
| [R003 MuJoCo](../论文与项目/开源项目主表.md#r003) | 工程基础与工具 | MJCF把关节、执行器、肌腱、传感器和接触参数放进可读模型，前向与逆动力学接口可直接服务控制器。作为Sim2Sim第二后端时，它能暴露策略对引擎接触细节的依赖。 | Apache-2.0<br>持续维护<br>真机：是 | [官方入口](https://github.com/google-deepmind/mujoco)<br>[归属证据](https://github.com/google-deepmind/mujoco) |
| [R004 MJX](../论文与项目/开源项目主表.md#r004) | 工程基础与工具 | MJX沿用MuJoCo模型语义，同时把批量动力学放进JAX编译和自动微分链。大规模rollout与可微优化可以共用同一模型，实验仍应报告其与CPU MuJoCo的接触差异和吞吐边界。 | Apache-2.0<br>持续维护<br>真机：部分 | [官方入口](https://github.com/google-deepmind/mujoco/tree/main/mjx)<br>[归属证据](https://github.com/google-deepmind/mujoco/tree/main/mjx) |
| [R005 MuJoCo Menagerie](../论文与项目/开源项目主表.md#r005) | 工程基础与工具 | 仓库为常见机器人维护可直接运行的MJCF资产，网格、执行器、传感器、默认姿态和关键参数已经过人工整理。算法对照复用同一资产，可减少模型适配差异对实验结论的干扰。 | Apache-2.0<br>持续维护<br>真机：否 | [官方入口](https://github.com/google-deepmind/mujoco_menagerie)<br>[归属证据](https://github.com/google-deepmind/mujoco_menagerie) |
| [R010 Brax](../论文与项目/开源项目主表.md#r010) | 工程基础与工具 | 当前活跃部分主要保留JAX强化学习训练算法，可与MJX或MuJoCo Warp等物理后端配合进行加速器并行实验；旧版弹性动力学环境仍可复现历史基线，但不宜再作为持续维护的仿真主线。 | Apache-2.0<br>持续维护<br>真机：否 | [官方入口](https://github.com/google/brax)<br>[归属证据](https://github.com/google/brax) |

## 使用边界

- 官方发布或维护只能证明项目归属，不能自动证明完整复现、持续维护或量产使用。
- 代码许可证不自动覆盖模型权重、训练数据、机器人资产、视频和硬件设计。
- 真机支持表示公开材料存在接口或部署证据，不代表所有机器人版本和控制参数都能直接运行。

## 导航

[返回公司开源项目索引](README.md) · [查看全部开源项目](../论文与项目/开源项目主表.md)
