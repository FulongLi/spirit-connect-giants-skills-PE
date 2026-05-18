# Anonymized Case Template

Use this template to turn project experience into a shareable control-loop debugging case. The goal is to preserve engineering judgment while removing customer, project, product, and commercial-sensitive information.

## Anonymization Rules

- Remove customer names, project codenames, product names, supplier-specific part numbers, and internal version identifiers.
- Keep parameters as engineering ranges or relative relationships, such as "high input voltage condition", "below 10% load", or "crossover near one tenth of switching frequency".
- Do not record complete input/output/power combinations, cost, release timing, or customer use cases if they could identify the product.
- Remove title bars, file paths, customer logos, and sensitive absolute values from waveform screenshots.
- If a detail is not necessary to explain the root cause, remove it by default.

## Case Structure

### Background

- Topology:
- Control method:
- Simulation or debugging tool:
- Operating range:
- Target behavior or metric:

### Symptom

- Condition where the abnormal behavior appears:
- Main waveform behavior:
- Relationship to Vin, load, temperature, startup, current limit, or mode transition:

### Initial Hypotheses

- Hypothesis 1:
- Hypothesis 2:
- Hypothesis 3:

### Diagnosis Path

- Simulations or experiments performed:
- Evidence observed at each step:
- Causes eliminated:
- Most important comparison experiment:

### Root Cause

- Root-cause category: stability / compensation parameters / sampling delay / model setup / power-stage parameters / simulation credibility
- Root-cause description:
- Why it was not exposed earlier:

### Fix

- Change made:
- Waveform or metric change after the fix:
- Side effects and new constraints:
- Other operating conditions that need coverage:

### Reusable Rules

- Check this first next time:
- Key waveforms to record:
- Mistake to avoid:
- Rule that should be added to the checklist:

## Output Requirement

Write cases in engineering facts and diagnosis actions, not personal evaluation. If information is missing, mark it as "not recorded" or "needs follow-up"; do not invent parameters.
