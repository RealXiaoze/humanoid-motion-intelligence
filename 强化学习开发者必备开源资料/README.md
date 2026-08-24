# 强化学习开发者必备开源资料

这份页面不追求收集最多的强化学习仓库，而是回答开发时应该先选哪一层工具：环境接口、算法实现、实验框架、机器人仿真，还是腿式训练与部署。原始清单中的项目跨越十多年，其中一部分已经归档或被接替；它们仍可用于理解技术演进，但不应与当前新项目的首选工具混在一起。

## 本目录包含什么

| 入口 | 适合解决的问题 |
|---|---|
| 本页 | 选择环境接口、算法实现、实验框架、机器人仿真和腿式训练项目，并识别已归档工具 |
| [强化学习书籍与课程](强化学习书籍与课程.md) | 按“概念入门、代码实践、机器人训练与调参”选择开源教材、课程和书目信息 |
| [基础书籍与学习资料](../技术路线/基础书籍与学习资料.md) | 回查坐标、运动学、刚体动力学、状态估计、规划和反馈控制等机器人基础 |

## 先按任务选择

| 当前目标 | 建议入口 | 选择理由 |
|---|---|---|
| 理解环境与算法怎样交互 | [Gymnasium](https://github.com/Farama-Foundation/Gymnasium) | 当前维护的标准单智能体环境接口，适合检查`reset`、`step`、终止、截断、空间和随机种子 |
| 阅读一份可以逐行追踪的算法实现 | [CleanRL](../论文与项目/开源项目主表.md#r032) | 单文件实现便于沿采样、优势估计、损失、更新和日志读完整训练循环 |
| 快速建立可靠算法基线 | [Stable-Baselines3](../论文与项目/开源项目主表.md#r031) | 经过测试的常见算法和统一API适合做对照，不必先搭完整训练框架 |
| 研究模块化或分布式训练系统 | [DI-engine](https://github.com/opendilab/DI-engine) | 把环境、策略、模型、任务和中间件拆开，适合研究大规模实验组织，而不是强化学习第一课 |
| 构建自定义三维交互环境 | [Unity ML-Agents](https://github.com/Unity-Technologies/ml-agents) | Unity场景可以作为深度强化学习和模仿学习环境，但结果不能直接替代机器人动力学仿真和Sim2Real验证 |
| 使用JAX研究可批量化环境 | [Jumanji](https://github.com/instadeepai/jumanji) | 提供JAX原生、可扩展的环境集合，适合研究并行环境与组合优化任务 |
| 研究第一视角视觉决策 | [ViZDoom](https://github.com/Farama-Foundation/ViZDoom) | 视觉输入、快速仿真和自定义场景适合做感知决策实验，但与真实机器人接触控制仍有明显距离 |
| 训练腿式或人形机器人 | [Isaac Lab](../论文与项目/开源项目主表.md#r001) + [RSL-RL](../论文与项目/开源项目主表.md#r026) | 前者组织机器人、场景和MDP，后者负责PPO等策略优化；两者的职责需要分开理解 |

## 当前训练栈怎样分工

一套最小强化学习实验可以按下面的信号流理解：

```text
环境状态与传感器模拟
        ↓
环境接口生成观测、奖励、终止和附加信息
        ↓
策略根据观测产生动作
        ↓
环境执行动作并推进动力学
        ↓
采样缓冲区计算回报和优势
        ↓
优化器更新Actor、Critic或其他学习模块
        ↓
固定测试条件评估新策略
```

`Gymnasium`规定环境和算法怎样交换数据；`CleanRL`、`Stable-Baselines3`或`DI-engine`实现采样与更新；`Isaac Lab`进一步加入机器人模型、物理场景、接触、传感器、域随机化和并行环境；`RSL-RL`接收这些环境产生的批量观测与奖励并训练策略。缺少这种分层意识时，很容易把环境配置、算法改动和机器人控制效果混成同一个结论。

## 机器人强化学习实践

| 资源 | 适合解决的问题 | 使用边界 |
|---|---|---|
| [Isaac Lab](../论文与项目/开源项目主表.md#r001) | 用Manager-Based或Direct工作流定义机器人场景、观测、动作、奖励、终止和随机化 | 它是环境与仿真基础设施，不会自动给出合理奖励、控制接口或Sim2Real结果 |
| [RSL-RL](../论文与项目/开源项目主表.md#r026) | 追踪向量化PPO、非对称Actor-Critic、经验存储、归一化、蒸馏和策略导出 | 它不负责机器人资产、传感器或低层硬件通信，需要与环境和部署工程配合 |
| [legged_gym](../论文与项目/开源项目主表.md#r027) | 理解Isaac Gym时代的GPU并行地形、关节位置动作、奖励、噪声和动力学随机化最小闭环 | 官方已经把相关环境迁移到Isaac Lab，并说明该仓库只接受有限更新；新项目应优先评估Isaac Lab |
| [IsaacGymEnvs](../论文与项目/开源项目主表.md#r028) | 复现Isaac Gym时代的官方GPU并行任务和多算法接入方式 | 适合旧实验复现和迁移对照，不是新机器人任务的默认起点 |
| [Unitree RL Lab](../论文与项目/开源项目主表.md#r036) | 检查Unitree本体从Isaac Lab训练、策略导出、MuJoCo验证到实机SDK的接口 | 平台支持范围和控制安全以官方仓库及机器人版本为准 |
| [IsaacGym二阶倒立摆示例](https://github.com/ZzzzzzS/legged_gym/releases) | 用较小任务理解观测、动作、奖励和训练入口，再进入多关节机器人 | 属于社区教程和旧Isaac Gym栈，应锁定版本；不能把倒立摆跑通等同于掌握腿式控制 |

Isaac Lab的安装、兼容矩阵和API以[官方文档](https://isaac-sim.github.io/IsaacLab/)为准。中文镜像或社区教程可以降低阅读成本，但版本冲突时必须回到官方文档和仓库提交定位。

## 历史项目与替代关系

下面这些项目有历史价值，但不建议在新工程中不加判断地直接采用。

| 原项目 | 当前判断 | 更合适的入口 |
|---|---|---|
| [OpenAI Gym](https://github.com/openai/gym) | 已归档，官方README明确说明后续开发转移到Gymnasium | [Gymnasium](https://github.com/Farama-Foundation/Gymnasium)；旧代码可通过兼容层逐步迁移 |
| [OpenAI Universe](https://github.com/openai/universe) | 2018年已归档，依赖旧Python、VNC和容器体系；只适合研究通用程序怎样被包装成环境 | 根据任务选择Gymnasium、现代浏览器环境或专用仿真平台 |
| [Retro Learning Environment](https://github.com/nadavbh12/Retro-Learning-Environment) | README已说明被后续项目取代，不应作为新Atari实验入口 | [Arcade Learning Environment](https://github.com/Farama-Foundation/Arcade-Learning-Environment)与Gymnasium Atari接口 |
| [Project Malmo](https://github.com/microsoft/malmo) | 已归档；Minecraft任务和多智能体实验仍有参考价值，但依赖与运行链较旧 | 仅在复现Malmo论文或确有Minecraft任务需求时使用 |
| [DeepMind Lab](https://github.com/google-deepmind/lab) | 仍可读取源码和任务设计，但构建、图形栈与依赖偏旧 | 新项目先确认是否真的需要Quake III式第一视角环境 |
| [MAgent](https://github.com/geek-ai/MAgent) | 原仓库明确停止维护 | [MAgent2](https://github.com/Farama-Foundation/MAgent2) |
| [keras-rl](https://github.com/keras-rl/keras-rl)、[OpenAI Lab](https://github.com/kengz/openai_lab)、[SLM-Lab](https://github.com/kengz/SLM-Lab) | 可以研究早期Keras或模块化RL框架设计，但依赖和接口不适合作为当前默认栈 | 入门用CleanRL或Stable-Baselines3；复杂实验再评估DI-engine、Tianshou或RLlib |
| [Torch-TWRL](https://github.com/twitter-archive/torch-twrl)、[UETorch](https://github.com/facebookarchive/UETorch)、[Coach](https://github.com/IntelLabs/coach) | 组织或仓库已进入历史维护状态，主要用于理解Lua/Torch、UE4插件和早期框架设计 | 选择当前维护且与现有Python、PyTorch和仿真器兼容的工具 |
| [TRFL](https://github.com/google-deepmind/trfl)、[Tensorforce](https://github.com/tensorforce/tensorforce)、[garage](https://github.com/rlworkgroup/garage) | 仍可查TensorFlow损失组件、应用框架和可复现实验设计，但不应只凭功能数量决定采用 | 先检查依赖版本、最近发行版、测试状态和团队是否能长期维护 |

## 最小实践顺序

1. **跑通接口**：使用Gymnasium的CartPole，打印每一步观测、动作、奖励、`terminated`和`truncated`，确认随机种子能够复现实验。
2. **读通算法**：选择CleanRL的一份PPO实现，沿采样、GAE、mini-batch、裁剪损失、价值损失和参数更新读完一次迭代。
3. **建立对照**：用Stable-Baselines3在同一环境、同一训练步数和相同评估种子下建立PPO基线，再只修改一个变量。
4. **进入机器人环境**：在Isaac Lab中先完成一个低自由度任务，确认动作缩放、PD接口、奖励、终止和并行环境，再进入四足或人形。
5. **形成工程闭环**：固定模型、配置、随机种子和测试集，保存训练曲线、评估指标、失败视频与策略文件；只有进入真机时，才继续增加模型导出、控制频率、延迟、关节映射和安全状态机检查。

最终产物不应该只是“安装成功”或“奖励上涨”，而应能够回答：环境给了策略什么信息，策略输出如何作用于系统，奖励究竟训练了哪种行为，改动相对基线带来了什么收益，以及更换随机种子、任务参数或机器人以后是否仍然成立。
