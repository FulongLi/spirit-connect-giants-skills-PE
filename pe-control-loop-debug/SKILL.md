---
name: pe-control-loop-debug
description: Use this skill for power electronics control-loop simulation and debugging, especially PLECS or LTspice workflows involving loop stability, compensation, transient response, oscillation diagnosis, Bode plots, sampling delay, PWM effects, simulation convergence, and waveform-based root cause analysis.
---

# 电力电子控制环路仿真与调试

## 使用目标

面向已有电力电子基础的研发工程师，帮助定位控制环路仿真和调试问题。优先给出可执行检查步骤、关键波形和下一步实验，而不是泛泛讲理论。

第一版聚焦控制环路，不展开磁件设计、热设计、EMI、器件选型或硬件实测全流程。

## 先判断问题类型

收到拓扑、控制方式、波形、仿真描述或故障现象后，先把问题归入一个或多个类别：

- 稳定性：相位裕度不足、交越频率过高、右半平面零点、谐振峰、次谐波振荡。
- 补偿参数：零极点位置不当、积分太强、带宽过低、负载/输入范围未覆盖。
- 采样和延迟：ADC 采样点、ZOH、计算延迟、PWM 更新、数字滤波造成额外相移。
- 模型设置：平均模型与开关模型不一致、初始条件、寄生参数、控制限幅、软启动。
- 功率级参数：LC 谐振、ESR 零点、输出电容偏差、电感饱和、负载模型。
- 仿真可信度：步长、收敛、探针位置、环路注入方式、扰动幅值、测量脚本。

## 信息不足时只追问关键项

优先继续诊断；只有缺少会改变结论的内容时再追问：

- 拓扑和工作模式：Buck/Boost/LLC/反激/逆变器，以及 CCM/DCM/CRM 等。
- 控制方式：电压模式、电流模式、峰值电流、平均电流、数字控制、PLL 等。
- 关键参数：开关频率、输入/输出范围、L/C/ESR、负载范围、补偿网络或数字控制参数。
- 仿真条件：PLECS/LTspice、平均模型或开关模型、瞬态/Bode/扫参、扰动位置和幅值。
- 异常现象：振荡频率、出现工况、关键波形、是否限流/饱和/占空比打满。

## 参考资料选择

按需要读取，不要一次性加载全部：

- PLECS 建模、扫参、Bode、瞬态检查：`references/plecs-workflow.md`
- LTspice 小信号、瞬态、收敛和环路注入：`references/ltspice-workflow.md`
- 控制环路诊断清单：`references/control-loop-checklist.md`
- 项目经验脱敏复盘：`references/anonymous-case-template.md`

## 标准输出结构

回答控制环路调试问题时，默认使用以下结构：

1. 问题复述：用工程语言重述症状、工况和已知约束。
2. 可能原因排序：按概率和风险排序，说明每个原因的关键证据。
3. 建议仿真检查：给出 PLECS/LTspice 可执行步骤、扫参或对比实验。
4. 关键波形：列出必须观察的电压、电流、误差信号、占空比、限幅和采样点。
5. 参数/补偿建议：说明建议改动、预期影响和不能跨越的约束。
6. 下一步实验：给出最小闭环验证动作，优先能快速排除假设。

## 项目经验沉淀

当用户要求整理项目经验、复盘或案例时，默认使用匿名案例格式。保留拓扑、症状、定位过程、证据、根因和可复用规则；删除客户名、项目代号、产品名、精确商业参数和任何不可公开信息。
