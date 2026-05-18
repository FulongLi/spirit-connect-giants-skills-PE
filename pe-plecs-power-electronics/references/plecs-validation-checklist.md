# PLECS Simulation Credibility Checklist

## Required Context

- Topology, control method, switching frequency, input/output range, and load range.
- Model level: switching, averaged, thermal, loss-only, or mixed.
- Solver settings, maximum step size, initialization method, and sample times.
- Parameter sources and whether values are nominal, worst-case, measured, or derated.

## Required Waveforms

- Input voltage/current, output voltage/current, and key energy-storage currents.
- Switching node, gate or PWM command, duty or frequency command, and current-sense signal.
- Error signal, compensator output, limit flags, protection states, and mode-transition flags.
- For thermal work: per-device loss, junction/case temperature, heatsink temperature, and ambient condition.

## Red Flags

- The result changes significantly after a step-size or solver-setting change.
- The averaged model and switching model disagree without a clear reason.
- Bode results show rough curves, unexpected phase jumps, or margins that contradict transient response.
- The controller output is saturated while the analysis assumes linear operation.
- Loss or thermal results are accepted before verifying the electrical waveform and power balance.

## Minimum Reproduction

- Reduce the model to the smallest converter, controller, and load condition that reproduces the symptom.
- Fix the control command to validate the power stage, then restore closed loop.
- Remove unrelated state machines and protection blocks until the root cause is isolated.
- Save the parameter set, model level, solver settings, waveforms, and diagnosis conclusion together.
