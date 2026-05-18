#!/usr/bin/env python3
"""Generate README.md from skill metadata."""

from __future__ import annotations

import datetime as _dt
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

PLANNED_SKILLS = [
    {
        "name": "pe-ansys-electromagnetic-thermal",
        "status": "planned",
        "focus": "ANSYS Maxwell/Icepak/Mechanical 电磁、损耗与热仿真工作流",
    },
    {
        "name": "pe-comsol-electromagnetic-thermal",
        "status": "planned",
        "focus": "COMSOL 电磁场、热场、多物理场耦合建模与可信度检查",
    },
]


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise ValueError(f"Missing frontmatter: {path}")

    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def first_heading(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.parent.name


def skill_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for skill_md in sorted(ROOT.glob("*/SKILL.md")):
        if skill_md.parts[-2].startswith("."):
            continue
        meta = parse_frontmatter(skill_md)
        references = sorted((skill_md.parent / "references").glob("*.md"))
        agents = skill_md.parent / "agents" / "openai.yaml"
        rows.append(
            {
                "folder": skill_md.parent.name,
                "name": meta.get("name", skill_md.parent.name),
                "title": first_heading(skill_md),
                "description": meta.get("description", ""),
                "references": str(len(references)),
                "status": "active" if agents.exists() else "draft",
            }
        )
    return rows


def generate() -> str:
    today = _dt.date.today().isoformat()
    rows = skill_rows()

    active_table = "\n".join(
        [
            "| Skill | Status | Focus | References |",
            "| --- | --- | --- | ---: |",
            *[
                f"| [`{row['name']}`](./{row['folder']}/SKILL.md) | {row['status']} | {row['title']} | {row['references']} |"
                for row in rows
            ],
        ]
    )

    planned_table = "\n".join(
        [
            "| Planned Skill | Status | Focus |",
            "| --- | --- | --- |",
            *[
                f"| `{item['name']}` | {item['status']} | {item['focus']} |"
                for item in PLANNED_SKILLS
            ],
        ]
    )

    return f"""# Spirit Connect Giants Skills PE

这是一个面向电力电子研发的 Codex Skills 仓库。目标是把项目经验、仿真流程、调试判断和工程 checklist 沉淀成可复用的 AI 工作流，帮助更多人在电力电子设计、仿真和问题定位中少走弯路。

当前第一阶段聚焦仿真与调试：控制环路、PLECS、LTspice、MATLAB/Simulink。后续会扩展到 ANSYS 和 COMSOL 的电磁仿真、热仿真和多物理场耦合。

Generated on: {today}

## Active Skills

{active_table}

## Planned Skills

{planned_table}

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
"""


def main() -> None:
    README.write_text(generate(), encoding="utf-8")


if __name__ == "__main__":
    main()
