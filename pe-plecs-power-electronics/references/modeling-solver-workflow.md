# PLECS Modeling And Solver Workflow

## Choose The Model Level

- Use a switching model when PWM timing, current ripple, device stress, protection, dead time, or nonlinear controller behavior matters.
- Use an averaged model when the goal is fast control design, wide operating sweeps, loop trends, or system-level studies.
- Use a thermal or loss model only after the electrical operating point and switching behavior are credible.
- For large systems, start with averaged subsystems and replace only the critical converter with a switching model.

## Build The Electrical Model

- Start with a minimal power stage, verified source/load conditions, and simple control before adding protection, parasitics, or thermal coupling.
- Add ESR, DCR, dead time, current-sense filtering, and delay only when they affect the target question.
- Keep measurement points aligned with the real design: sensed current, feedback divider output, PWM compare signal, gate command, and protection flags.
- Record parameter source and units, especially when values come from datasheets, measurements, or derating assumptions.

## Solver And Step Size

- Switching models need time resolution fine enough for PWM events, dead time, protection trips, and sample instants.
- Averaged models can use larger steps, but should still represent controller sampling and saturation if those are part of the question.
- If changing solver settings or step size changes the conclusion, treat the result as not yet credible.
- Event-heavy models should be simplified when debugging: remove unrelated state machines and confirm the minimum reproduction first.

## Initialization

- Decide whether the target experiment is startup, initialized steady state, or disturbance from steady state.
- For load steps and input perturbations, confirm the model is settled before applying the disturbance.
- Capture controller state, soft-start state, integrator state, and protection flags at the start of each test.
