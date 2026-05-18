# Control-Loop Debugging Checklist

## Start From The Symptom

- Oscillation near the LC resonance: check phase margin, ESR zero, compensation zero placement, and effective output capacitance.
- Oscillation near half the switching frequency: check slope compensation, sample timing, and subharmonic oscillation in peak-current-mode control.
- Large load-step overshoot: check bandwidth, phase margin, integrator windup, current limit, output capacitance, and load model.
- Slow recovery without oscillation: check low crossover frequency, misplaced compensation zero, integral limiting, and soft-start state.
- Abnormal behavior only at one Vin or load range: check mode transition, duty-cycle limit, RHP zero, resonant operating region, or sampling-delay ratio.

## Controller And Compensation

- Identify the compensation form: Type II, Type III, PI, PID, digital IIR/FIR, or state-machine control.
- Do not set crossover only at a typical condition; cover Vin, load, L/C/ESR tolerance, and mode transitions.
- For voltage-mode Boost, flyback, and other RHP-zero topologies, keep bandwidth below the phase-limited region.
- For current-mode control, inspect current-sense gain, slope compensation, peak current limit, and current-sense filter delay.
- For digital control, include sampling delay, computation delay, PWM update, and quantization in the phase-margin estimate.

## Power Stage And Load

- Output capacitor ESR, MLCC DC bias, temperature, and parallel combinations move zeros and damping.
- Inductor DCR, saturation, core loss, and current ripple change effective power-stage dynamics.
- Distinguish resistive load, constant-current load, constant-power load, and downstream converter load.
- For LLC and other frequency-controlled topologies, confirm gain-curve slope, operating region, and frequency limits.

## Sampling, PWM, And Saturation

- Check whether the sampling point avoids switching spikes and diode-recovery noise.
- Match PWM update instant with controller computation timing to avoid an extra-cycle delay.
- Inspect whether the error amplifier output, duty command, current reference, or frequency command is saturated.
- Once a loop enters saturation, do not explain the full response using linear loop margin only.

## Simulation Credibility

- Cross-check averaged and switching models at the same operating condition.
- Verify Bode injection point, perturbation amplitude, measurement direction, and steady operating point.
- Build a minimum reproduction by reducing unrelated control blocks, fixing the command, and simplifying the model.
- Record the simulation settings behind each conclusion: step size, solver, initial condition, model version, and parameter table.

## Minimum Diagnostic Output

Every conclusion should include:

- The most likely root cause.
- The waveform or simulation evidence supporting it.
- The fastest validation action.
- The next hypothesis if that validation fails.
