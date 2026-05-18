# Simulink Power Electronics Simulation Credibility Checklist

## Required Settings

- Confirm the model level matches the question: do not mix conclusions from switching detail, averaged loop design, and system-level behavior.
- Check solver, maximum step size, sample time, and PWM frequency alignment.
- Confirm controller discretization matches the target implementation.
- Record initial conditions, soft-start state, and protection state.
- Identify the load model: resistor, constant-current load, constant-power load, or downstream converter.

## Required Waveforms

- Input voltage, inductor or transformer current, output voltage, and output current.
- Error signal, compensator output, duty command, or frequency command.
- Current limit, over-voltage, under-voltage, mode transition, and soft-start status.
- ADC sample point, PWM carrier, comparator output, or digital control update instant.

## Signals That May Be Untrustworthy

- The conclusion changes strongly when maximum step size changes.
- The averaged model is stable, but the switching model oscillates at a fixed condition.
- Load-step response includes startup behavior.
- The controller output remains saturated while the analysis uses only linear loop-margin language.
- The sample point lands near a switching spike or dead-time transition.

## Minimum Reproduction

- Remove system-level modules unrelated to the abnormal behavior.
- Fix input and load so only one abnormal operating condition remains.
- Fix the command to validate the power stage, then restore closed loop.
- Save the parameter snapshot and simulation settings, not only waveform screenshots.
