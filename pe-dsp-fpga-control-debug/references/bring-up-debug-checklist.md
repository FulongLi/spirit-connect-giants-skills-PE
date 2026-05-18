# Hardware Bring-Up And Waveform Diagnosis Checklist

## First Measurements

- Probe PWM output, gate signal, switch node, current-sense signal, voltage feedback, ADC trigger, and protection output.
- Log internal variables if possible: raw ADC code, scaled feedback, error, controller terms, duty command, saturation flag, and trip status.
- Compare probe timing with the expected digital timing path, not only waveform amplitude.
- Keep initial tests at reduced input voltage, current limit, and conservative duty/frequency limits.

## Common Root Causes

- ADC sample point lands on switching noise, diode recovery, dead time, or current-sense blanking interval.
- PWM shadow register updates one cycle later than expected.
- Feedback polarity or current-sense sign is inverted.
- Fixed-point scaling overflows or silently clips the integrator.
- Protection comparator trips and latches before the control loop can respond.
- FPGA pipeline valid signals are misaligned with the corresponding data.

## Isolation Experiments

- Replace ADC input with a known test value or DAC-injected signal.
- Freeze the controller output and validate the power stage open loop.
- Bypass one filter or limiter at a time in a safe test build.
- Replay captured ADC samples through the C or HDL implementation offline.
- Reduce loop bandwidth and observe whether the symptom follows phase delay.

## Evidence To Capture

- Operating condition, topology, switching frequency, sample rate, and controller version.
- Oscilloscope capture with ADC trigger, PWM output, current sense, voltage feedback, and gate signal.
- Logged internal control variables around the event.
- Fault flags, protection thresholds, and latch clear sequence.
- The smallest test condition that reproduces the issue.
