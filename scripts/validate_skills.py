#!/usr/bin/env python3
"""Validate skill folder structure and README freshness."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import update_readme


ROOT = Path(__file__).resolve().parents[1]


def parse_frontmatter(path: Path) -> dict[str, str]:
    return update_readme.parse_frontmatter(path)


def validate_skill(skill_md: Path) -> list[str]:
    errors: list[str] = []
    folder = skill_md.parent
    meta = parse_frontmatter(skill_md)
    name = meta.get("name", "")
    description = meta.get("description", "")

    if not name:
        errors.append(f"{skill_md}: missing frontmatter name")
    if name and name != folder.name:
        errors.append(f"{skill_md}: name '{name}' does not match folder '{folder.name}'")
    if len(description) < 60:
        errors.append(f"{skill_md}: description is too short for reliable skill triggering")

    agents = folder / "agents" / "openai.yaml"
    if not agents.exists():
        errors.append(f"{folder}: missing agents/openai.yaml")
    else:
        agents_text = agents.read_text(encoding="utf-8")
        if f"${name}" not in agents_text:
            errors.append(f"{agents}: default_prompt should mention ${name}")
        for field in ("display_name:", "short_description:", "default_prompt:"):
            if field not in agents_text:
                errors.append(f"{agents}: missing {field}")

    text = skill_md.read_text(encoding="utf-8")
    for ref in sorted(set(re.findall(r"`(references/[^`]+\.md)`", text))):
        ref_path = folder / ref
        if not ref_path.exists():
            errors.append(f"{skill_md}: referenced file does not exist: {ref}")

    return errors


def main() -> int:
    errors: list[str] = []
    skill_files = sorted(ROOT.glob("*/SKILL.md"))
    if not skill_files:
        errors.append("No skills found. Expected at least one */SKILL.md file.")

    for skill_md in skill_files:
        errors.extend(validate_skill(skill_md))

    expected_readme = update_readme.generate()
    current_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if current_readme != expected_readme:
        errors.append("README.md is stale. Run: python3 scripts/update_readme.py")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_files)} skills and README.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
