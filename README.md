# 人形机器人运动智能知识库

<p align="center">
  <a href="https://github.com/RealXiaoze/humanoid-motion-intelligence/stargazers"><img src="https://img.shields.io/github/stars/RealXiaoze/humanoid-motion-intelligence?style=flat-square&label=Stars&color=0969da" alt="GitHub Stars"></a>
  <a href="https://github.com/RealXiaoze/humanoid-motion-intelligence/forks"><img src="https://img.shields.io/github/forks/RealXiaoze/humanoid-motion-intelligence?style=flat-square&label=Forks&color=0969da" alt="GitHub Forks"></a>
  <a href="LICENSE.md"><img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-2da44e?style=flat-square" alt="CC BY-NC-SA 4.0 License"></a>
  <img src="https://komarev.com/ghpvc/?username=RealXiaoze-humanoid-motion-intelligence&label=Visitors&color=555&style=flat-square" alt="Repository Visitors">
</p>

> 出品：具身智能研究室

这个知识库围绕人形机器人运动智能的完整研发链组织内容，帮助读者把单篇论文、开源项目、公司动态和岗位要求放回同一张问题地图中。

## 🚀 使用方法

将仓库克隆到本地，并在支持读取本地文件的Agent中打开仓库目录：

```bash
git clone https://github.com/RealXiaoze/humanoid-motion-intelligence.git
cd humanoid-motion-intelligence
```

使用时向Agent说明你的背景、目标、机器人本体、开发环境、已有结果和当前问题，再让它按照[Agent使用规则](AGENTS.md)检索技术路线、论文、项目、数据集、产业和岗位信息。

### 这个知识库可以怎样使用

| 你的目标 | 主要入口 | 可以让Agent完成什么 |
|---|---|---|
| 从零学习人形机器人运动控制 | [技术路线总览与学习路径](技术路线/README.md) | 根据专业基础、可用硬件和学习周期，在自主运动基座、参考跟踪基座和真机部署闭环中规划阶段任务、阅读材料与验收结果 |
| 查论文、比较方法或确定选题 | [论文总索引](论文与项目/README.md) | 围绕一个技术矛盾比较相邻论文的输入、输出、训练信号、控制接口、实机证据和失败边界，判断已有结论与可研究缺口 |
| 选择开源项目和复现基线 | [开源项目主表](论文与项目/开源项目主表.md) · [小而美的运动控制项目](https://my.feishu.cn/wiki/Q1jaw5rCliWddukCfYfcwjW0nJf) | 根据机器人本体、仿真器、算法方向、代码状态、许可证和真机支持筛选项目，并检查项目实际开放了训练、部署还是只有演示 |
| 按公司查官方开源项目 | [具身智能公司的开源项目](具身智能公司的开源项目/README.md) | 从公司进入其独立页面，查看官方训练、仿真、模型、运行时和部署项目，并核对许可证、维护状态、真机支持与归属证据 |
| 查找训练数据和数据采集方案 | [具身智能数据集](数据集/README.md) | 比较人体动作、人类视频、Ego数据、遥操作、真机示范、仿真轨迹和数字资产的模态、本体依赖、动作表示、许可与下游用途 |
| 建设动作恢复、重定向和数据管线 | [动作数据与重定向](技术路线/01_动作数据与重定向.md) | 梳理视频或MoCap恢复、坐标处理、跨本体重定向、接触约束、时间同步、质量筛选和下游训练接口 |
| 调试或优化运动控制算法 | [Locomotion与运动先验](技术路线/02_Locomotion与运动先验.md) · [动作跟踪与全身控制](技术路线/03_动作跟踪与全身控制.md) | 根据观测、动作、奖励、参考轨迹、PD、控制频率、训练现象和失败日志定位问题，并提出可通过消融实验验证的修改 |
| 构建LocoManip、VLA、世界模型或Agent系统 | [LocoManip](技术路线/04_LocoManip.md) · [世界模型、VLA与Agent](技术路线/05_世界模型VLA与Agent.md) | 明确感知、身体基座、接触控制、动作生成、任务规划和反馈模块的输入输出，判断上层模型怎样调用低层执行能力 |
| 完成Sim2Real和真机部署 | [工程与实机部署](技术路线/06_工程与实机部署.md) | 检查模型导出、关节映射、归一化、PD/WBC、状态估计、控制时序、通信、安全状态机、日志和失败回归 |
| 建立评测和测试体系 | [工程与实机部署](技术路线/06_工程与实机部署.md#数据集benchmark与标准) | 根据Benchmark、标准、任务协议和失败场景建立固定测试矩阵，区分仿真结果、Sim2Sim、硬件在环和真机证据 |
| 补机器人学和强化学习基础 | [基础书籍与学习资料](技术路线/基础书籍与学习资料.md) · [强化学习开发者必备开源资料](强化学习开发者必备开源资料/README.md) | 根据当前故障补坐标、动力学、规划、状态估计、PPO和工程工具，而不是从头顺序读完整份书单 |
| 观察公司、产品与产业变化 | [公司与产业](公司与产业/README.md) | 查询公司成立、产品发布、融资和公开技术路线，并区分公司自述、论文证据、第三方报道与分析推断 |
| 准备实习、校招或社招 | [招聘与内推信息](求职与岗位/README.md) | 对照目标岗位分析能力缺口、项目表达、面试准备和投递渠道；岗位状态、薪资和联系方式仍需回到原始页面确认 |

### 使用要求

要求Agent在结论中注明引用页面、稳定`Pxxx/Rxxx/Dxxx`编号和原始来源，并区分论文结论、项目README声明、公司自述和分析推断。“有代码”“有演示”不等于完整可复现或稳定真机部署。

## 🗺️ 技术路线核心内容

六条路线是知识库的资料分类，不等于六个并列的个人研究方向。对人形机器人运动控制而言，核心是形成通用全身运动控制基座：一条主线根据任务命令、地形和行为提示自主产生运动，另一条主线根据参考动作或人体信号完成全身跟踪。动作数据位于上游，LocoManip与世界模型/VLA/Agent位于下游，工程与实机部署横向支撑所有环节。

### 1. 动作数据与重定向

[动作数据与重定向](技术路线/01_动作数据与重定向.md)回答人体、视频、MoCap或其他本体的运动怎样变成目标机器人可训练、可执行的数据。判断一项工作是否属于这里，要看它的核心产物是不是人体运动、机器人参考轨迹或批量数据，而不是最终控制策略。

| 内部路线 | 需要解决的问题 | 代表工作 |
|---|---|---|
| 视频人体运动恢复 | 从移动相机和野外视频中分离人体局部姿态、相机运动与世界坐标轨迹 | [GVHMR](论文与项目/论文逐篇解读/P075.md)、[TRAM](论文与项目/论文逐篇解读/P076.md)、[WHAM](论文与项目/论文逐篇解读/P121.md) |
| 目标本体动作重定向 | 处理人体与机器人之间的比例、零位、连杆坐标、关节限位、接触和动力学可行性 | [GMR](论文与项目/论文逐篇解读/P077.md)、[NMR](论文与项目/论文逐篇解读/P078.md)、[OmniRetarget](论文与项目/论文逐篇解读/P079.md)、[DDR](论文与项目/论文逐篇解读/P122.md)、[DynaRetarget](论文与项目/论文逐篇解读/P123.md) |
| 人形训练数据构建 | 把少量示范、三维资产、视频先验或无本体采集扩展成可规模化训练的数据 | [GRAIL](论文与项目/论文逐篇解读/P118.md)、[BifrostUMI](论文与项目/论文逐篇解读/P124.md)、[HumanoidMimicGen](论文与项目/论文逐篇解读/P045.md) |

代表项目包括[GMR](https://github.com/YanjieZe/GMR)、[GVHMR](https://github.com/zju3dv/GVHMR)、[OmniRetarget](https://github.com/amazon-far/holosoma)和[HumanoidMimicGen](https://humanoidmimicgen.github.io/)。完整页面收录**14篇论文/技术报告和13个项目**。

### 2. Locomotion与运动先验

[Locomotion与运动先验](技术路线/02_Locomotion与运动先验.md)研究没有完整逐帧参考动作时，机器人怎样根据速度、方向、目标位置、地形或行为提示自主产生运动。视觉感知、复杂地形与AMP不是三个平级能力，而是同一自主运动主线中的不同问题。

| 内部路线 | 需要解决的问题 | 代表工作 |
|---|---|---|
| 基础Locomotion | 速度跟踪、站立、行走、跑跳、抗扰、课程学习、域随机化和基础Sim2Real | [Humanoid-Gym](论文与项目/论文逐篇解读/P015.md)、[Rapid Locomotion](论文与项目/论文逐篇解读/P011.md)、[Real-World Humanoid Locomotion](论文与项目/论文逐篇解读/P014.md) |
| 感知与复杂地形 | 让本体历史、深度图或高度图参与状态估计、落脚选择和全身地形反应 | [DreamWaQ](论文与项目/论文逐篇解读/P125.md)、[Humanoid Parkour](论文与项目/论文逐篇解读/P016.md)、[Hiking in the Wild](论文与项目/论文逐篇解读/P132.md) |
| 对抗先验与行为模型 | 用判别器、生成先验、潜变量或无监督技能表示约束动作分布并形成可提示行为 | [AMP](论文与项目/论文逐篇解读/P022.md)、[ASE](论文与项目/论文逐篇解读/P024.md)、[BFM-Zero](论文与项目/论文逐篇解读/P080.md)、[State-Dependent AMP](论文与项目/论文逐篇解读/P106.md) |

代表项目包括[Humanoid-Gym](https://github.com/roboterax/humanoid-gym)、[BFM-Zero](https://github.com/LeCAR-Lab/BFM-Zero)、[Project Instinct](https://project-instinct.github.io/)和[Legged Lab DWAQ](https://gitee.com/chaomingsanhua/legged_lab)。完整页面收录**38篇论文/技术报告和33个项目**。

### 3. 动作跟踪与全身控制

[动作跟踪与全身控制](技术路线/03_动作跟踪与全身控制.md)研究参考动作、关键点、目标姿态或人体实时信号怎样被稳定转换成机器人全身动作。与自主Locomotion的区别是，这条路线具有明确参考；真正的难点是参考是否可执行、Tracker是否能泛化，以及失配后能否恢复。

| 内部路线 | 需要解决的问题 | 代表工作 |
|---|---|---|
| 基础Tracker与通用运动基座 | 扩展动作库与模型容量，统一速度、关键点、姿态和motion token等控制接口 | [DeepMimic](论文与项目/论文逐篇解读/P021.md)、[HOVER](论文与项目/论文逐篇解读/P031.md)、[SONIC](论文与项目/论文逐篇解读/P035.md)、[HoloMotion-1](论文与项目/论文逐篇解读/P104.md) |
| 跟踪增强与失配恢复 | 修正不可达参考，处理动力学偏差、碰撞扰动、在线适应和偏离参考后的恢复 | [BeyondMimic](论文与项目/论文逐篇解读/P034.md)、[Heracles](论文与项目/论文逐篇解读/P134.md)、[Any2Track](论文与项目/论文逐篇解读/P103.md) |
| 人体驱动与遥操作 | 把人体信号、重定向、因果观测、通信延迟、真机反馈和安全约束组成实时闭环 | [H2O](论文与项目/论文逐篇解读/P029.md)、[OmniH2O](论文与项目/论文逐篇解读/P030.md)、[TWIST](论文与项目/论文逐篇解读/P088.md)、[TWIST2](论文与项目/论文逐篇解读/P089.md) |

代表项目包括[BeyondMimic](https://github.com/HybridRobotics/whole_body_tracking)、[HoloMotion](https://github.com/HorizonRobotics/HoloMotion)、[OmniH2O](https://omni.human2humanoid.com/)、[MimicKit](https://github.com/xbpeng/MimicKit)和[engineai_rl_lab](https://github.com/engineai-robotics/engineai_rl_lab)。完整页面收录**37篇论文/技术报告和27个项目**。

### 4. LocoManip与物理交互

[LocoManip](技术路线/04_LocoManip.md)位于任务能力层。它不只是“边走边抓”，而是要求移动、平衡、视觉、接触、负载和物体动力学进入同一任务闭环，最终改变外部物体或场景状态。现有系统可以串联多个专项技能，也可以训练统一全身策略，或让VLA/WAM生成目标后由身体基座执行。

| 内部路线 | 需要解决的问题 | 代表工作 |
|---|---|---|
| 视觉闭环与交互状态 | 从RGB、深度、场景几何或物体状态判断接触阶段，并处理视觉误差对任务结果的影响 | [DoorMan](论文与项目/论文逐篇解读/P092.md)、[HumanX](论文与项目/论文逐篇解读/P098.md)、[HAIC](论文与项目/论文逐篇解读/P049.md) |
| 接触力控与负载适应 | 处理外力、柔顺响应、接触切换、未知负载和人体安全交互 | [FACET](论文与项目/论文逐篇解读/P084.md)、[Thor](论文与项目/论文逐篇解读/P112.md)、[GentleHumanoid](论文与项目/论文逐篇解读/P083.md) |
| 全身协同与技能接口 | 联合腿、腰、手和物体状态，并向遥操作、规划器或上层模型提供统一身体接口 | [OmniContact](论文与项目/论文逐篇解读/P138.md)、[CoorDex](论文与项目/论文逐篇解读/P139.md)、[OpenHLM](论文与项目/论文逐篇解读/P141.md) |

代表项目包括[DoorMan](https://doorman-humanoid.github.io/)、[OmniContact](https://github.com/Ingrid789/OmniContact_sim2sim)、[CoorDex](https://github.com/Skevinci/coordex)和[Thor](https://baai-aether.github.io/baai-thor/)。完整页面收录**30篇论文/技术报告和24个项目**。

### 5. 世界模型、VLA与Agent

[世界模型、VLA与Agent](技术路线/05_世界模型VLA与Agent.md)关注上层模型怎样理解视觉语言、预测环境变化、生成动作或调度技能，并与身体控制器形成反馈闭环。阅读这类工作时必须先确认输出接口：模型给出的是关节动作、动作块、motion token、轨迹、末端目标还是技能调用。

| 内部路线 | 需要解决的问题 | 代表工作 |
|---|---|---|
| 动作生成与通用策略 | 从视觉、语言、本体状态和任务条件生成可供机器人执行的动作表示 | [GR00T N1](论文与项目/论文逐篇解读/P060.md)、[WholeBodyVLA](论文与项目/论文逐篇解读/P097.md)、[MotionWAM](论文与项目/论文逐篇解读/P081.md) |
| 物理世界建模与预测 | 预测动作条件下的未来视觉、潜在状态、物体变化或动力学，用于规划、训练和评测 | [DreamDojo](论文与项目/论文逐篇解读/P114.md)、[HAIC](论文与项目/论文逐篇解读/P049.md)、[WorldArena](论文与项目/论文逐篇解读/P116.md) |
| 记忆、规划与任务调度 | 维护空间和任务上下文，把长程目标拆成技能图，并依据执行反馈重新规划 | [HoloAgent-0](论文与项目/论文逐篇解读/P082.md)、[SceneBot](论文与项目/论文逐篇解读/P094.md)、[FALCON](论文与项目/论文逐篇解读/P044.md) |

代表项目包括[Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T)、[HoloAgent](https://github.com/HorizonRobotics/HoloAgent)、[GE-2 / GE-Sim 2.0](https://github.com/AgibotTech/GE-Sim-V2)和[GO-2](https://www.agibot.com/article/231/detail/56.html)。完整页面收录**42篇论文/技术报告和23个项目**。

### 6. 工程与实机部署

[工程与实机部署](技术路线/06_工程与实机部署.md)不是杂项目录，而是算法进入真机必须经过的横向底座。这里覆盖机器人模型和接口、状态估计、动力学控制与优化、仿真器、Sim2Real、安全评测、数据集、Benchmark和标准。

| 工程层 | 需要解决的问题 | 代表论文或项目 |
|---|---|---|
| 状态、接触与控制 | 浮基状态怎样估计，任务空间目标怎样转成满足接触和动力学约束的控制量 | [Contact-Aided InEKF](论文与项目/论文逐篇解读/P074.md)、[Crocoddyl](论文与项目/论文逐篇解读/P006.md)、[Pinocchio](https://github.com/stack-of-tasks/pinocchio)、[mc_rtc](https://github.com/jrl-umi3218/mc_rtc) |
| 仿真与训练基础设施 | 怎样统一机器人、环境、观测、动作、奖励、随机化和批量训练接口 | [Isaac Lab](https://github.com/isaac-sim/IsaacLab)、[MuJoCo](https://github.com/google-deepmind/mujoco)、[Genesis](https://github.com/Genesis-Embodied-AI/Genesis) |
| Sim2Real、安全与部署 | 怎样处理动力学偏差、系统辨识、模型导出、控制时序、硬件通信、安全过滤和故障回退 | [PACE](论文与项目/论文逐篇解读/P146.md)、[ASAP](论文与项目/论文逐篇解读/P033.md)、[SafeWBC](论文与项目/论文逐篇解读/P142.md)、[ros2_control](https://github.com/ros-controls/ros2_control) |
| 数据集、Benchmark与标准 | 怎样定义数据来源、本体依赖、许可、任务协议、评价指标和回归测试 | [具身智能数据集](数据集/README.md) · [工程与实机部署完整索引](技术路线/06_工程与实机部署.md#数据集benchmark与标准) |

完整页面收录**17篇论文/技术报告和86个项目**。项目数量较多，是因为本体接口、仿真器、控制库、数据工具和部署工程都在这一层汇合。

## 新手学习顺序

完整学习要求和每阶段通过标准见[技术路线总览与学习路径](技术路线/README.md)。下面保留最关键的顺序与最小产物，避免只读论文却没有形成可验证闭环。[基础书籍与学习资料](技术路线/基础书籍与学习资料.md)是遇到坐标、动力学、规划、状态估计或强化学习问题时的查阅入口，不要在开始项目前按书单从头读到尾。

| 阶段 | 核心任务 | 最小产物 |
|---|---|---|
| 1. 编程、数学与机器人表示 | 掌握Linux、Git、Python/C++、坐标变换、四元数、URDF/MJCF、关节与执行器顺序 | 解析一个机器人模型和一段关节日志，验证坐标、单位与索引 |
| 2. 机器人模型与反馈控制 | 理解FK/IK、雅可比、刚体动力学、接触、PD、阻抗/导纳和控制频率 | 在MuJoCo中完成单关节跟踪和静态姿态保持，并分析增益与时序失稳 |
| 3. 仿真训练闭环 | 追踪任务注册、观测、动作、奖励、Actor、Critic、保存和推理入口 | 跑通Humanoid-Gym或同类基线，保存配置、随机种子、曲线和评估视频 |
| 4. PPO与基础Locomotion | 理解任务奖励、优势估计、PPO裁剪、课程学习、随机化和训练特权信息 | 固定测试条件，只改变一组观测、奖励或随机化并完成受控消融 |
| 5. 选择一条运动基座主线 | 自主运动主线继续研究地形感知、状态估计与AMP/行为先验；参考跟踪主线先完成动作数据与重定向，再进入Tracker、恢复和人体驱动 | 自主运动完成一项受控消融；参考跟踪完成一段动作从重定向到关节目标的闭环，并报告失败片段 |
| 6. 按目标扩展系统 | 根据目标建设规模化动作/交互数据管线，或把运动基座接入LocoManip、VLA/WAM/Agent；这些分别是上游数据、任务层和高层扩展，不是第三条运动基座 | 明确扩展模块的输入输出、上下游接口和独立收益，用端到端任务与失败案例验证 |
| 7. Sim2Real与测试闭环 | 核对关节映射、模型参数、PD、延迟、导出、通信、安全状态机和日志时钟 | 建立覆盖速度、地面、扰动、载荷、延迟与模型偏差的回归测试矩阵 |

最终作品不要求覆盖全部路线，但应包含问题边界、可复现环境、控制闭环、基线与改动、实验与消融、失败分析、部署证据和结果表达。完成标志不是“成功运行作者命令”，而是更换动作、本体、控制参数或测试场景以后，仍能判断应该修改哪一层以及如何验证。

## 📚 重点文件索引

| 文件 | 主要内容 |
|---|---|
| [技术路线总览与学习路径](技术路线/README.md) | 系统能力栈、训练更新闭环、路线关系、七阶段学习顺序、最小作品和通过标准 |
| [强化学习开发者必备开源资料](强化学习开发者必备开源资料/README.md) | 通过开源项目页和书籍课程页，分别解决“开发用什么工具”和“基础怎样补齐” |
| [具身智能数据集](数据集/README.md) | 按数据来源、本体依赖、动作表示和训练用途查找34个具身智能数据集 |
| [论文与技术报告总索引](论文与项目/README.md) | 178篇论文与技术报告按最终系统作用分类，可按稳定`Pxxx`编号进入独立解读 |
| [开源项目主表](论文与项目/开源项目主表.md) | 206个项目的研发位置、关键实现、开源边界与开发价值 |
| [具身智能公司的开源项目](具身智能公司的开源项目/README.md) | 通过公司索引进入独立页面，查看官方归属可核验、代码托管和许可证明确的开源项目 |
| [公司与产品主表](公司与产业/公司与产品主表.md) | 按国家或地区整理的114家公司/机构及其公开产品与平台 |
| [公开信号时间线](公司与产业/公开信号时间线.md) | 只记录带日期的公司成立、产品发布与融资事实 |
| [运动控制面经、谈薪与薪资汇总](求职与岗位/2026-03_运动控制面经_谈薪技巧_薪资汇总.md) | 运动控制面试、项目表达、谈薪与匿名薪资样本入口 |
| [具身秋招运动控制问答](求职与岗位/2026-07_具身秋招运动控制问答.md) | 秋招阶段关于方向选择、项目准备和岗位判断的集中问答 |
| [招聘与内推信息](求职与岗位/2026_招聘与内推信息.md) | 按Base地点整理的公司、岗位、职责、要求和公开投递方式 |

## 阅读与使用

- 技术方法按最终解决的问题分类，AMP、Mimic、Diffusion、Transformer和世界模型等保留为方法标签。
- 公司自述、论文结果和第三方证据不能相互替代；公司目录与事件时间线均不构成强弱排名或投资建议。
- 招聘、薪资和产品信息会变化，使用前请检查页面日期和原始来源。
- 发现错误时，请提供具体页面、稳定ID和原始来源；转载与图片使用请先阅读[许可与版权边界](LICENSE.md)。

## 📬 联系与纠错

- 微信：`yzz010329`
- GitHub：[提交Issue](https://github.com/RealXiaoze/humanoid-motion-intelligence/issues)

![元泽个人名片](求职与岗位/图片/个人名片.png)

纠错时请附上页面名称、稳定ID、错误位置和可核验来源；论文、项目、公司与招聘信息均以原始来源为准。
