# Physical Intelligence

> 本页集中展示能够核验为Physical Intelligence官方发布或维护、具有公开代码托管入口的项目。公开仓库不等于训练、权重、数据和部署链路已经完整开放。

## 主体信息

- **国家或地区**：美国
- **项目数量**：4
- **公司与产品记录**：[查看主体主表](../公司与产业/公司与产品主表.md#c031)

## 官方公开项目

| 项目 | 技术位置 | 解决的问题 | 来源 |
| --- | --- | --- | --- |
| [R055 openpi](../论文与项目/开源项目主表.md#r055) | 世界模型VLA与Agent / 动作生成与通用策略 | 仓库同时维护流匹配式π0、快速自回归π0-FAST和π0.5，并提供检查点、数据配置、微调与推理服务。接入新机器人时最关键的工作是动作归一化、数据字段映射和推理频率对齐。 | [官方入口](https://github.com/Physical-Intelligence/openpi)<br>[归属证据](https://github.com/Physical-Intelligence/openpi) |
| [R418 openpi-basic-control](../论文与项目/开源项目主表.md#r418) | 工程基础与工具 | 部署端读取机器人状态并构造训练时一致的观测，加载策略或控制器输出关节命令，同时处理频率、通信和安全状态。 | [官方入口](https://github.com/Physical-Intelligence/openpi-basic-control)<br>[归属证据](https://github.com/Physical-Intelligence/openpi-basic-control) |
| [R419 pi-data-sharing](../论文与项目/开源项目主表.md#r419) | 动作数据入口与重定向 / 人形训练数据构建 | 相机、机器人状态、动作和任务边界被同步记录、转换或评估，形成可进入LeRobot、RLDS或公司训练栈的数据。 | [官方入口](https://github.com/Physical-Intelligence/pi-data-sharing)<br>[归属证据](https://github.com/Physical-Intelligence/pi-data-sharing) |
| [R420 real-time-chunking-kinetix](../论文与项目/开源项目主表.md#r420) | 世界模型VLA与Agent / 动作生成与通用策略 | 相机、语言和机器人状态进入策略模型生成动作块，再经本体接口送入真机或仿真执行并回收任务结果。 | [官方入口](https://github.com/Physical-Intelligence/real-time-chunking-kinetix)<br>[归属证据](https://github.com/Physical-Intelligence/real-time-chunking-kinetix) |

## 使用边界

- 官方发布或维护只能证明项目归属，不能自动证明完整开源、完整复现、持续维护或量产使用。
- 代码许可证不自动覆盖模型权重、训练数据、机器人资产、视频和硬件设计。
- 真机支持表示公开材料存在接口或部署证据，不代表所有机器人版本和控制参数都能直接运行。

## 导航

[查看全部公司与产品](../公司与产业/公司与产品主表.md) · [查看全部开源项目](../论文与项目/开源项目主表.md)
