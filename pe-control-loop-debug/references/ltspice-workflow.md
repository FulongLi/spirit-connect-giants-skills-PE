# LTspice Control-Loop Simulation Workflow

## Transient Credibility

- Confirm the circuit reaches the intended operating condition before drawing conclusions about loop response.
- Observe the error signal, compensation node, PWM comparator signal, switching node, inductor current, output voltage, and load current.
- If results are highly sensitive to maximum time step, reduce the maximum step and inspect switching edges, diode reverse recovery, parasitic inductance, and ideal sources.
- For startup issues, separate soft-start parameters, initial conditions, integrator windup, and numerical convergence problems.

## Loop Injection And AC Analysis

- If using an averaged model, confirm the power-stage transfer function, operating point, duty constraint, and modulator gain.
- If measuring loop behavior on a switching model, use a stable operating point, small-signal injection, and enough cycle averaging.
- Choose an injection point that preserves DC bias. Confirm return-ratio polarity, otherwise phase margin can be misread.
- AC analysis is reliable only for a linearized model. Models containing comparators, limiters, and switching behavior usually need averaging or a dedicated sampled-data method.

## Convergence And Numerical Issues

- For convergence failures, first inspect ideal voltage sources in parallel with capacitors, ideal current sources in series with inductors, floating nodes, and overly stiff switching models.
- Add reasonable ESR/DCR to key components to avoid ideal LC tanks and infinitely sharp switching edges.
- Do not treat `.options` as root-cause repair. Improve model physicality first, then tune tolerances or integration method if needed.
- If non-physical spikes appear, inspect probe reference, grounding, inductor series resistance, diode model, and MOSFET parasitics.

## Comparison Experiments

- Fixed command: force duty ratio or frequency and confirm the power stage can operate at the target condition.
- Simplified controller: keep only proportional or low-order compensation to see whether higher-order compensation causes the issue.
- Model swap: run the same condition with ideal and realistic devices to separate control, parasitic, and device-model effects.
- Vin/load sweep: record the critical load, Vin, and duty range where oscillation begins.

## Common LTspice Pitfalls

- Running small-signal AC directly on a switching model can produce precise-looking but unreliable loop curves.
- Measuring transient metrics before steady state can confuse startup with load-step response.
- `startup`, initial conditions, and capacitor precharge strongly affect controller state and must be recorded.
- Idealized op amp and comparator models can hide delay, slew rate, output saturation, and common-mode limitations.
