# Simulink/Simscape Modeling And Solver Workflow

## Choose The Model Level

- Use switching models for PWM behavior, sampling, device stress, ripple, current limit, and nonlinear state machines.
- Use averaged models for loop design, operating-point sweeps, control-parameter iteration, and system-level stability screening.
- For system-level studies, start with averaged power stages and replace critical operating points with switching models for confirmation.
- Do not expect one model to answer every question. State the engineering question before choosing the model level.

## Simscape Electrical Modeling

- Keep units and parameter sources consistent. Avoid mixing nominal values, tolerance values, and measured values without labels.
- Add capacitor ESR, parasitic inductance, inductor DCR, dead time, and sampling delay only when they are relevant to the target question.
- For aggressive switching models, start with ideal devices, then add real devices and parasitics gradually.
- For control debugging, make sure measurement points match the real sampling points rather than ideal internal nodes only.

## Solver And Step Size

- Switching models usually need discrete or local solver settings aligned with PWM frequency. Maximum step size must resolve switching edges and sample instants.
- Averaged models can use larger steps, but should not hide discrete controller delay or saturation.
- If a conclusion is highly sensitive to maximum step size, treat it as a model credibility issue before explaining the control behavior.
- For convergence issues, inspect ideal sources, pure LC networks, floating nodes, algebraic loops, and overly stiff nonlinear switches.

## Initialization

- Document whether the model uses steady-state initialization, startup from zero, or specified initial conditions.
- Load-step and input-perturbation tests should start after steady state unless startup behavior is the subject.
- Controller integrator state, soft-start state, and protection state machine must match the target experiment.
