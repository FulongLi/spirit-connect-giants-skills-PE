# Device Model, Gate-Drive, And Parasitic Checklist

## Device Model Checks

- Confirm whether the model is intended for switching transient, conduction loss, reverse recovery, avalanche, thermal behavior, or only typical application simulation.
- Check the modeled voltage rating, current rating, capacitance curves, gate charge, threshold, body diode, reverse recovery, and temperature assumptions.
- For IGBT models, inspect tail current, diode behavior, gate resistance assumptions, and switching energy fit range.
- For SiC/GaN models, inspect gate voltage limits, package parasitics, output capacitance behavior, and recommended simulation time step.

## Gate-Drive Checks

- Model driver output voltage, source/sink current, external gate resistor, split gate resistor, Miller clamp, negative gate bias, and driver propagation delay when relevant.
- Probe gate voltage at the power-device pins and at the driver output to separate driver behavior from gate-loop parasitics.
- Check turn-on and turn-off thresholds against actual gate waveform, not just ideal pulse command.
- Include dead time and shoot-through protection for half-bridge or synchronous topologies.

## Parasitic Checks

- DC-link loop inductance controls voltage overshoot and ringing.
- Common source/emitter inductance couples power current into gate voltage and can cause false turn-on or oscillation.
- Gate-loop inductance and resistance affect ringing, dv/dt sensitivity, and switching loss.
- Snubber, clamp, PCB capacitance, transformer leakage, and diode capacitance can dominate high-frequency ringing.

## Sensitivity Experiments

- Sweep gate resistance, loop inductance, snubber values, and device capacitance scaling where appropriate.
- Replace the device model with an ideal switch plus capacitances to separate topology/parasitic issues from model-specific behavior.
- Compare ideal layout and estimated layout parasitics to bound the expected stress.
