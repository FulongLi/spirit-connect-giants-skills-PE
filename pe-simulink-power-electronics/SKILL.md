---
name: pe-simulink-power-electronics
description: Use this skill for MATLAB and Simulink power electronics simulation workflows, including Simscape Electrical modeling, switching and averaged converter models, control-loop co-simulation, solver setup, parameter sweeps, waveform validation, and debugging unreliable simulation results.
---

# MATLAB/Simulink 电力电子仿真

## 使用目标

面向电力电子研发工程师，用于规划、搭建、检查和调试 MATLAB/Simulink/Simscape Electrical 中的电力电子仿真。优先帮助用户把模型变得可验证、可扫参、可复现。

## 先判断仿真类型

收到需求后先分类：

- 功率级开关模型：关注器件、PWM、采样、开关纹波、寄生和求解器稳定性。
- 平均模型：关注控制器、传递函数、工况扫参、环路稳定性和快速迭代。
- 控制联合仿真：关注离散控制、采样周期、PWM 更新、延迟、限幅和 anti-windup。
- 系统级仿真：关注上游/下游源负载、母线、电机/逆变器、保护状态机和工况覆盖。
- 模型可信度问题：关注 solver、步长、初始条件、单位、参数来源和波形测量位置。

## 信息不足时追问

只追问会改变建模方案或诊断结论的信息：

- 拓扑、功率级参数、输入/输出范围和负载类型。
- 使用 Simscape Electrical、Specialized Power Systems 还是纯 Simulink 模型。
- 目标是开关细节、平均控制设计、系统级行为还是代码生成前验证。
- 控制器采样周期、PWM 频率、离散/连续实现方式。
- 当前异常波形、solver 设置、最大步长、是否存在代数环或收敛报错。

## 参考资料

按需读取：

- 建模和 solver 设置：`references/modeling-solver-workflow.md`
- 控制联合仿真与扫参：`references/control-sweep-workflow.md`
- 模型可信度检查清单：`references/simulink-validation-checklist.md`

## 标准输出结构

1. 仿真目标复述：明确用户要验证的是功率级、控制器、系统行为还是故障。
2. 推荐模型层级：说明应使用开关模型、平均模型或两者组合。
3. Simulink/Simscape 设置：给出 solver、步长、初始化、采样周期和测量点建议。
4. 检查实验：给出扫参、负载阶跃、输入扰动、控制器对比或模型简化实验。
5. 关键波形和指标：列出必须记录的信号和合格判据。
6. 下一步：给出最小可执行动作，优先能快速验证模型可信度。
