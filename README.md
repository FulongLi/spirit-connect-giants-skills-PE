# Spirit Connect Giants Skills PE

Spirit Connect Giants Skills PE is a Codex Skills repository for power electronics engineering. Its purpose is to turn project experience, simulation workflows, debugging judgment, and engineering checklists into reusable AI workflows that can help more people design, simulate, and diagnose power electronics systems.

The first stage focuses on simulation and debugging for control loops, PLECS, LTspice, and MATLAB/Simulink. Future skills will cover ANSYS and COMSOL workflows for electromagnetic simulation, thermal simulation, and coupled multiphysics validation.

Generated on: 2026-05-18

## Active Skills

| Skill | Status | Focus | References |
| --- | --- | --- | ---: |
| [`pe-control-loop-debug`](./pe-control-loop-debug/SKILL.md) | active | Power Electronics Control-Loop Simulation And Debugging | 4 |
| [`pe-ltspice-power-electronics`](./pe-ltspice-power-electronics/SKILL.md) | active | LTspice Power Electronics Simulation | 3 |
| [`pe-plecs-power-electronics`](./pe-plecs-power-electronics/SKILL.md) | active | PLECS Power Electronics Simulation | 4 |
| [`pe-simulink-power-electronics`](./pe-simulink-power-electronics/SKILL.md) | active | MATLAB/Simulink Power Electronics Simulation | 3 |

## Planned Skills

| Planned Skill | Status | Focus |
| --- | --- | --- |
| `pe-ansys-electromagnetic-thermal` | planned | ANSYS Maxwell/Icepak/Mechanical workflows for electromagnetic loss, thermal, and coupled-field simulation. |
| `pe-comsol-electromagnetic-thermal` | planned | COMSOL workflows for electromagnetic fields, thermal fields, and multiphysics validation. |

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
