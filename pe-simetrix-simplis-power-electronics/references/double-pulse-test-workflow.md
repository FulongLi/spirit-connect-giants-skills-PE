# Double-Pulse Test Workflow

## Purpose

Use double-pulse simulation to evaluate switching energy, voltage overshoot, current slew rate, diode reverse recovery, gate-drive behavior, and parasitic sensitivity for MOSFET, IGBT, SiC, or GaN devices.

## Circuit Setup

- Model the DC link, high-side/low-side switch position, freewheel diode or synchronous device, load inductor, gate driver, gate resistance, and measurement points.
- Include package inductance, DC-link loop inductance, gate-loop inductance, source/emitter inductance, and snubber/clamp components when they affect overshoot or ringing.
- Use realistic gate-drive voltage, sink/source strength, negative turn-off if applicable, Miller clamp, and gate resistor split if present.
- Initialize the load current with the first pulse; use the second pulse for turn-on/turn-off energy extraction.

## Measurement Points

- Gate-source or gate-emitter voltage at the device pins, not only at the driver output.
- Drain-source or collector-emitter voltage at the device pins and, separately, at the DC-link terminals if layout inductance matters.
- Switch current, diode current, inductor current, and reverse-recovery current.
- Switching energy integration windows for turn-on and turn-off.

## Sweep Strategy

- Sweep gate resistance, DC-link voltage, load current, junction temperature if the model supports it, and loop inductance.
- Sweep snubber or clamp values when overshoot or ringing is the target.
- For SiC/GaN, check very small time steps around edges and verify model validity at the actual gate-drive condition.
- Keep one baseline condition that matches a bench double-pulse test or datasheet condition.

## Credibility Checks

- Compare simulated switching energy, overshoot, and slew rate with datasheet or measured double-pulse data when possible.
- Check whether ringing frequency matches the expected loop inductance and capacitance.
- If energy changes dramatically with maximum time step, the waveform is not yet trustworthy.
- Do not trust package-stress conclusions without package and layout parasitics.
