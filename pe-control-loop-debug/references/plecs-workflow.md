# PLECS Control-Loop Simulation Workflow

## Model Credibility Checks

- Identify the model level first: averaged model, switching model, or thermal/loss model. Do not transfer conclusions blindly between model levels.
- Model control saturation explicitly: error-amplifier output, duty command, peak-current reference, soft-start, current limit, and anti-windup can all reshape the transient response.
- Cover worst-case power-stage parameters: input voltage range, load range, L/C/ESR tolerance, sampling delay, and PWM update behavior.
- For LLC, resonant, or multi-mode topologies, confirm the operating region before drawing loop conclusions.

## Bode And Loop Injection

- Inject a small perturbation at the steady operating point. Keep the amplitude small enough to avoid saturation, mode changes, or protection events.
- Place the injection source where loop gain is well defined, and confirm the return-ratio direction.
- Record the operating condition for every Bode result: Vin, Vout, load, switching frequency, operating mode, and model type.
- If the curve is not smooth near crossover, suspect nonlinear behavior, excessive perturbation amplitude, or time-step issues before trusting the margin.
- For digital control, include sampling, computation delay, PWM zero-order hold, and filtering in the loop.

## Transient Checks

- Run load-step tests before input perturbation tests. Increase step size gradually to avoid triggering protection before the loop behavior is understood.
- Observe output voltage, output current, inductor or transformer current, error signal, compensator output, duty command, and limit flags together.
- If ringing is near the LC or sampling-related frequency, check phase margin, ESR zero placement, and sampling delay.
- If the response is slow but not oscillatory, check low bandwidth, weak zero placement, integral limiting, or soft-start state.
- If recovery is slow after overshoot, check integrator windup, anti-windup, and command saturation.

## Sweep Suggestions

- Minimum sweep set: Vin min/max, load min/max, L/C/ESR tolerance, key compensation zeros/poles, and sampling delay.
- Change one main variable at a time and record the threshold where the abnormal behavior starts.
- Compare averaged and switching models at the same operating point. If the averaged model is stable but the switching model oscillates, inspect sampling, PWM behavior, saturation, and subharmonic oscillation.
- If the power stage is suspected, hold or simplify the controller and observe the natural frequency and damping.

## Common PLECS Pitfalls

- Stability conclusions from ideal devices can be invalidated by ESR, dead time, delay, or saturation.
- A coarse time step can hide switching ripple, sample-point mistakes, and high-frequency oscillation.
- Automatic initialization may not match the real startup path; separate initialization artifacts from control-loop behavior.
- In multi-rate controllers, explicitly document each module's sample time, PWM period, and update instant.
