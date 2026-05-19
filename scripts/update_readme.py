#!/usr/bin/env python3
"""Generate README.md from skill metadata."""

from __future__ import annotations

import datetime as _dt
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

PLANNED_SKILLS: list[dict[str, str]] = []


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

    if PLANNED_SKILLS:
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
    else:
        planned_table = "_No planned skills are listed right now. Add future items to `PLANNED_SKILLS` in `scripts/update_readme.py`._"

    return f"""# Spirit Connect Giants Skills PE

Spirit Connect Giants Skills PE is a Codex Skills repository for power electronics engineering. Its purpose is to turn project experience, simulation workflows, debugging judgment, and engineering checklists into reusable AI workflows that can help more people design, simulate, and diagnose power electronics systems.

The first stage focuses on simulation, debugging, digital control implementation, and electromagnetic/thermal multiphysics workflows for control loops, PLECS, LTspice, SIMetrix/SIMPLIS, MATLAB/Simulink, DSP/MCU targets, FPGA targets, ANSYS, and COMSOL.

Generated on: {today}

## Active Skills

{active_table}

## Planned Skills

{planned_table}

## How To Use These Skills

1. Install or copy the skill folder you want to use into your Codex skills directory.
2. Invoke a skill explicitly by name, for example: `Use $pe-ltspice-power-electronics to debug this LTspice converter simulation`.
3. Provide the engineering context the skill asks for: topology, operating range, control method, simulation tool, abnormal waveform, solver settings, and what you are trying to prove.
4. Let the skill load only the relevant `references/` files. The `SKILL.md` file gives the high-level workflow; the references contain tool-specific procedures and checklists.
5. When capturing project experience, remove customer names, project codenames, product names, exact confidential parameters, internal file paths, and any screenshot metadata that could reveal sensitive information.

## How To Add Or Update A Skill

1. Create or edit a folder named after the skill, for example `pe-new-topic/`.
2. Keep the required workflow instructions in `pe-new-topic/SKILL.md`.
3. Put detailed procedures, checklists, templates, and examples under `pe-new-topic/references/`.
4. Add `pe-new-topic/agents/openai.yaml` with a display name, short description, and default prompt.
5. Run the update and validation commands:

```bash
python3 scripts/update_readme.py
python3 scripts/validate_skills.py
```

`scripts/update_readme.py` scans all `*/SKILL.md` files and regenerates the Active Skills table and generated date. `scripts/validate_skills.py` checks skill metadata, referenced files, UI metadata, and whether README is current.

## Repository Convention

- Each skill lives in a standalone directory and must include `SKILL.md`.
- Detailed tool workflows and checklists live in `references/` and are loaded only when needed.
- UI metadata lives in `agents/openai.yaml`.
- Skill content should be primarily English so the repository can help a broader engineering audience.
- Case studies should be anonymized by default.

## Automation

GitHub Actions runs the same README freshness and skill validation checks on push and pull request. If README is stale after a skill update, the CI check fails and tells the contributor to run `python3 scripts/update_readme.py`.
"""


def main() -> None:
    README.write_text(generate(), encoding="utf-8")


if __name__ == "__main__":
    main()
