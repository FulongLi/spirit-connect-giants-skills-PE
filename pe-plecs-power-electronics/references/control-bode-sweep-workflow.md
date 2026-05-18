# PLECS Control, Bode, And Sweep Workflow

## Control-Loop Setup

- Identify the loop: voltage loop, current loop, PLL, DC-link loop, speed loop, or nested-loop structure.
- Record controller implementation: continuous, discrete, sampled-data, state machine, or code-equivalent block.
- Include sampling delay, computation delay, PWM update timing, filters, saturation, and anti-windup when they affect phase or transient response.
- Check whether the loop enters current limit, duty saturation, frequency limit, or mode transition before interpreting linear margins.

## Bode Workflow

- Use a settled operating point and a perturbation small enough to avoid nonlinear behavior.
- Place the injection point where the loop gain is well defined and the DC operating point is preserved.
- Record Vin, Vout, load, switching frequency, controller parameters, model level, and perturbation amplitude for every Bode plot.
- If the Bode curve is rough near crossover, check settling time, perturbation amplitude, nonlinear saturation, and measurement direction first.

## Transient Workflow

- Run small load steps before large load steps. Increase amplitude only after the loop behavior is understood.
- Observe output voltage, output current, inductor or transformer current, error signal, compensator output, command signal, and limit flags together.
- Compare averaged and switching models at the same operating point. Differences often reveal sampling, PWM, saturation, and ripple effects.

## Sweep Workflow

- Minimum sweep set: input voltage, load, L/C/ESR tolerance, sampling delay, controller gains, and key protection thresholds.
- Change one dominant factor at a time when diagnosing a root cause.
- For each failed sweep point, save the condition, model level, solver settings, key waveforms, and failure reason.
