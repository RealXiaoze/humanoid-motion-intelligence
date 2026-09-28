# 强化学习开发者必备开源资料

> 汇总强化学习环境、算法框架、机器人仿真与训练工具，按功能介绍项目用途与特点。

## 本页导航

[环境接口与任务环境](#环境接口与任务环境) · [算法实现与训练框架](#算法实现与训练框架) · [机器人仿真与训练](#机器人仿真与训练) · [历史项目与相关入口](#历史项目与相关入口) · [书籍与学习资料](#书籍与学习资料)

## 环境接口与任务环境

| 项目 | 主要用途 | 功能与特点 |
|---|---|---|
| [Gymnasium](https://github.com/Farama-Foundation/Gymnasium) | 统一环境与算法的数据接口 | 定义观测、动作、奖励、终止与截断，提供标准实验环境 |
| [Unity ML-Agents](https://github.com/Unity-Technologies/ml-agents) | 构建三维交互与智能体训练任务 | 使用Unity场景进行强化学习和模仿学习实验 |
| [Jumanji](https://github.com/instadeepai/jumanji) | JAX并行环境与组合优化实验 | JAX原生环境集合，支持批量化计算 |
| [ViZDoom](https://github.com/Farama-Foundation/ViZDoom) | 第一视角视觉决策实验 | 基于Doom提供视觉输入、快速仿真和自定义场景 |

## 算法实现与训练框架

| 项目 | 主要用途 | 功能与特点 |
|---|---|---|
| [CleanRL](https://github.com/vwxyzjn/cleanrl) | 阅读与修改强化学习算法 | 单文件实现，便于追踪采样、优势估计、损失和参数更新 |
| [Stable-Baselines3](https://github.com/DLR-RM/stable-baselines3) | 建立常见算法基线 | 统一API、训练与评估接口，提供常用强化学习算法 |
| [DI-engine](https://github.com/opendilab/DI-engine) | 组织模块化训练与复杂实验 | 分离环境、策略、模型、任务和中间件 |
| [RSL-RL](https://github.com/leggedrobotics/rsl_rl) | 机器人策略优化 | 向量化PPO、非对称Actor-Critic、归一化、蒸馏与策略导出 |

## 机器人仿真与训练

| 项目 | 主要用途 | 功能与特点 |
|---|---|---|
| [Isaac Lab](https://github.com/isaac-sim/IsaacLab) | 构建机器人强化学习与模仿学习任务 | 机器人场景、传感器、观测、动作、奖励、随机化与并行环境；[官方文档](https://isaac-sim.github.io/IsaacLab/) · [中文文档（范子琦译）](https://docs.robotsfan.com/isaaclab/index.html) |
| [Unitree RL Lab](https://github.com/unitreerobotics/unitree_rl_lab) | 宇树机器人训练与部署 | 连接Isaac Lab训练、策略导出、MuJoCo验证和实机SDK |
| [K-Sim](https://github.com/kscalelabs/ksim) | 基于MuJoCo与JAX训练机器人策略 | 提供机器人任务示例与仿真采样、策略训练流程 |
| [K-Scale OS](https://github.com/kscalelabs/kos) | 机器人硬件运行时 | 接入执行器、传感器与机器人运行系统 |
| [EmbodiChain](https://github.com/DexForce/EmbodiChain) | 组织仿真任务、数据生成与策略训练 | 集成GPU仿真、任务环境和RL/IL接口 |
| [DISCOVERSE](https://github.com/discoverse-dev/DISCOVERSE) | 场景重建、操作示范与模仿学习 | 结合MuJoCo与3DGS，支持Real2Sim2Real数据流程 |

## 其他环境与工具

| 项目 | 主要用途 | 技术栈或相关入口 |
|---|---|---|
| [legged_gym](https://github.com/leggedrobotics/legged_gym) | 腿式机器人GPU并行训练 | Isaac Gym向量化仿真与批量训练 |
| [IsaacGymEnvs](https://github.com/isaac-sim/IsaacGymEnvs) | Isaac Gym官方任务与训练示例 | GPU并行物理仿真与多算法接入 |
| [IsaacGym二阶倒立摆示例](https://github.com/ZzzzzzS/legged_gym/releases) | 用低自由度任务学习训练配置 | 社区Isaac Gym教程，包含观测、动作、奖励与训练入口 |
| [OpenAI Gym](https://github.com/openai/gym) | 强化学习标准环境接口 | Gym环境封装与交互协议 |
| [OpenAI Universe](https://github.com/openai/universe) | 将桌面程序与游戏包装为交互环境 | VNC与容器化环境交互 |
| [Retro Learning Environment](https://github.com/nadavbh12/Retro-Learning-Environment) | 复古游戏强化学习环境 | 相关入口：[Arcade Learning Environment](https://github.com/Farama-Foundation/Arcade-Learning-Environment) |
| [Project Malmo](https://github.com/microsoft/malmo) | Minecraft智能体与多智能体实验 | Minecraft任务环境与多智能体接口 |
| [DeepMind Lab](https://github.com/google-deepmind/lab) | 三维第一视角学习任务 | 基于Quake III的视觉导航与交互环境 |
| [MAgent](https://github.com/geek-ai/MAgent) | 大规模多智能体实验 | 后续入口：[MAgent2](https://github.com/Farama-Foundation/MAgent2) |
| [keras-rl](https://github.com/keras-rl/keras-rl) | 使用Keras搭建强化学习算法 | 早期Keras强化学习实现 |
| [OpenAI Lab](https://github.com/kengz/openai_lab) | 组织强化学习实验 | 实验配置与训练流程 |
| [SLM-Lab](https://github.com/kengz/SLM-Lab) | 模块化算法研究与实验管理 | 训练配置、算法组件与实验组织 |
| [Torch-TWRL](https://github.com/twitter-archive/torch-twrl) | Torch强化学习实验 | Lua/Torch技术栈 |
| [UETorch](https://github.com/facebookarchive/UETorch) | 连接游戏引擎与学习系统 | UE4与Torch插件 |
| [Coach](https://github.com/IntelLabs/coach) | 组合强化学习算法与环境 | 早期模块化训练框架 |
| [TRFL](https://github.com/google-deepmind/trfl) | 复用强化学习计算组件 | TensorFlow损失函数与更新算子 |
| [Tensorforce](https://github.com/tensorforce/tensorforce) | 构建应用型强化学习实验 | 基于TensorFlow的训练框架 |
| [garage](https://github.com/rlworkgroup/garage) | 组织可复现强化学习研究 | 算法、环境与实验工具 |

## 书籍与学习资料

| 入口 | 主要内容 |
|---|---|
| [书籍与课程](书籍与课程.md) | 机器人学、动力学、控制、强化学习、大模型与AI基础设施 |
| [技术路线与学习路径](../技术与研究/README.md) | 知识体系、项目路线与实践顺序 |
| [技术与研究](../技术与研究/README.md) | 更多运动控制、仿真、训练与部署项目 |
