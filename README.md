# Spirit Connect Giants Skills PE

这是一个面向电力电子研发的 Codex Skills 仓库。目标是把项目经验、仿真流程、调试判断和工程 checklist 沉淀成可复用的 AI 工作流，帮助更多人在电力电子设计、仿真和问题定位中少走弯路。

当前第一阶段聚焦仿真与调试：控制环路、PLECS、LTspice、MATLAB/Simulink。后续会扩展到 ANSYS 和 COMSOL 的电磁仿真、热仿真和多物理场耦合。

Generated on: 2026-05-18

## Active Skills

| Skill | Status | Focus | References |
| --- | --- | --- | ---: |
| [`pe-control-loop-debug`](./pe-control-loop-debug/SKILL.md) | active | 电力电子控制环路仿真与调试 | 4 |
| [`pe-ltspice-power-electronics`](./pe-ltspice-power-electronics/SKILL.md) | active | LTspice 电力电子仿真 | 3 |
| [`pe-simulink-power-electronics`](./pe-simulink-power-electronics/SKILL.md) | active | MATLAB/Simulink 电力电子仿真 | 3 |

## Planned Skills

| Planned Skill | Status | Focus |
| --- | --- | --- |
| `pe-ansys-electromagnetic-thermal` | planned | ANSYS Maxwell/Icepak/Mechanical 电磁、损耗与热仿真工作流 |
| `pe-comsol-electromagnetic-thermal` | planned | COMSOL 电磁场、热场、多物理场耦合建模与可信度检查 |

## Repository Convention

- 每个技能放在独立目录中，必须包含 `SKILL.md`。
- 详细工具流程、检查清单和案例模板放入 `references/`，由 `SKILL.md` 按需引用。
- UI 元数据放入 `agents/openai.yaml`，用于展示名称、简介和默认调用提示。
- 项目复盘默认脱敏：删除客户名、项目代号、产品名、精确商业参数和内部路径。

## README Update

每次新增、重命名或更新技能后，运行：

```bash
python3 scripts/update_readme.py
```

脚本会扫描所有 `*/SKILL.md`，自动更新 Active Skills 表格和生成日期，让 README 反映当前仓库状态。GitHub Actions 会在 push 和 pull request 时检查 README 是否已经同步。未来新增 ANSYS、COMSOL 或其他电力电子技能时，也应同步更新 `scripts/update_readme.py` 中的 planned 列表或将对应技能目录落地。
