---
name: pe-ltspice-power-electronics
description: Use this skill for LTspice power electronics simulation workflows, including switching converter transient analysis, averaged models, loop-gain injection, compensation validation, convergence debugging, device model sanity checks, and waveform-based diagnosis.
---

# LTspice 电力电子仿真

## 使用目标

面向电力电子研发工程师，用于搭建、检查和调试 LTspice 中的电源与功率变换器仿真。重点是让仿真结果可信、可复现，并能支持工程判断。

## 先判断任务类型

- 瞬态开关仿真：检查启动、负载阶跃、开关节点、电感电流、限流和器件应力。
- 平均模型/小信号：检查环路增益、补偿网络、交越频率和相位裕度。
- 收敛问题：检查理想器件、寄生、初始条件、求解器和模型物理性。
- 器件模型问题：检查 MOSFET/二极管/运放/比较器模型是否适合当前目标。
- 波形诊断：根据异常频率、节点和工况判断控制、功率级或数值问题。

## 信息不足时追问

- 拓扑、控制方式、开关频率、输入/输出和负载范围。
- 使用开关模型还是平均模型，目标是瞬态、AC 还是环路测量。
- 异常波形、仿真命令、最大步长、初始条件和报错信息。
- 关键模型来源：控制芯片宏模型、MOSFET/二极管模型、运放或比较器模型。

## 参考资料

按需读取：

- 瞬态与波形诊断：`references/transient-waveform-workflow.md`
- 环路注入与补偿验证：`references/loop-gain-workflow.md`
- 收敛和模型可信度：`references/convergence-model-checklist.md`

## 标准输出结构

1. 目标和症状：说明用户要验证的工况、异常和已有证据。
2. 可信度判断：指出仿真结论当前是否可相信，缺哪些检查。
3. LTspice 操作建议：给出仿真命令、探针、对比实验或模型简化步骤。
4. 关键波形：列出必须同时观察的节点和控制量。
5. 根因假设排序：按控制环路、功率级、器件模型、数值设置分类。
6. 下一步实验：给出最快能排除一个假设的动作。
