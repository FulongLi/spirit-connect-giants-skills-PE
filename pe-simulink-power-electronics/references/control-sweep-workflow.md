# Control Co-Simulation And Sweep Workflow

## Controller Implementation Checks

- Identify whether the controller is continuous-domain, discrete-domain, or code-identical to the target implementation.
- Record sample time, PWM update period, computation delay, filter delay, and saturation limits.
- Check anti-windup, saturation, mode transition, and protection state-machine paths.
- For digital controllers, inspect quantization, data types, normalization, and fixed-point range.

## Baseline Experiment Order

1. Fix the command and verify that the power stage works at the target condition.
2. Close the loop with an averaged power stage to confirm compensation parameters and loop trend.
3. Switch to the switching model and compare steady-state error, ripple, transient response, and command signal.
4. Add parasitics, delay, and saturation to see which factor introduces the abnormal behavior.
5. Sweep Vin, load, L/C/ESR tolerance, and sampling delay to find the worst case.

## Sweep Output

- Each sweep result should record the operating condition, model level, solver settings, key metrics, and failure reason.
- Key metrics include overshoot, recovery time, steady-state error, peak current, duty/frequency saturation, and protection events.
- Save the minimum reproduction model or parameter set for any abnormal point.

## Cross-Checking With PLECS Or LTspice

- Loop conclusions can be cross-checked with PLECS sweeps or LTspice small circuits.
- If Simulink and circuit-level tools disagree, inspect model level, injection point, delays, and parameter units first.
