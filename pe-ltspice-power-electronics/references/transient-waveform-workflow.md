# LTspice Transient And Waveform Diagnosis Workflow

## Pre-Run Checks

- Confirm the input source, load, initial conditions, and controller soft-start path match the target experiment.
- For switching converters, set the maximum time step fine enough to resolve PWM behavior, dead time, switching edges, and sample instants.
- Start with ideal devices to prove the topology and operating point, then add realistic MOSFET, diode, op amp, and controller models step by step.

## Required Waveforms

- Vin, Vout, load current, and input current.
- Switching node, inductor or transformer current, diode current, and synchronous FET current.
- Error signal, compensation node, PWM comparator signal, duty command, or frequency command.
- Current-limit flag, soft-start signal, protection pins, and controller supply pins.

## Diagnosis Sequence

1. Force duty ratio or frequency and confirm the power stage works at the target operating condition.
2. Restore closed loop and inspect whether the error signal or compensation node rails.
3. Sweep load and input voltage to record the boundary where the issue appears.
4. Change maximum time step to confirm the conclusion is not a numerical artifact.
5. Swap ideal and realistic device models to separate circuit, control, and model effects.

## Common Waveform Meanings

- Compensation node railed: check startup, current limit, output target, feedback ratio, and integrator windup.
- Excessive switching-node spike: check parasitic inductance, snubber network, diode recovery, and probe reference.
- Alternating large/small inductor current cycles: check peak-current-mode slope compensation and sampling noise.
- Output ringing near LC resonance: check compensation zero/pole placement, output capacitor ESR, and load model.
