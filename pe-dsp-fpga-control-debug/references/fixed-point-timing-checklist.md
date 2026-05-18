# Fixed-Point, Scaling, And Timing Checklist

## Fixed-Point Scaling

- Define the Q format or binary point for every signal: ADC value, normalized feedback, error, coefficients, integrator state, and output command.
- Check signed versus unsigned interpretation at ADC inputs, subtractors, multipliers, and PWM compare registers.
- Verify multiplication growth, accumulator width, rounding mode, and saturation at every arithmetic stage.
- Test edge cases: zero input, full-scale input, negative current, current reversal, saturated command, and sign changes.

## Coefficient And Unit Consistency

- Confirm whether gains are in physical units, per-unit, normalized digital units, or register-scaled units.
- Recompute discrete coefficients using the actual sample period, not the nominal simulation step if they differ.
- Check bilinear, backward Euler, forward Euler, or matched pole-zero discretization assumptions.
- Keep feedforward and feedback sign conventions explicit.

## Timing And Delay

- Total delay includes sample placement, ADC conversion, ISR or HDL pipeline, PWM shadow-load, gate-driver delay, and sensing filter delay.
- Convert delay into phase loss near crossover frequency when diagnosing instability.
- In DSP systems, check ISR execution time and jitter against the switching period.
- In FPGA systems, check pipeline latency, clock-domain crossing delay, and valid-signal alignment.

## Failure Signatures

- Works at low bandwidth but oscillates at target bandwidth: suspect delay, sample timing, or discretization mismatch.
- Duty command rails immediately: suspect sign error, scaling error, offset, feedback polarity, or startup state.
- Hardware response is slower than simulation: suspect sample period mismatch, coefficient scaling, or output limiting.
- Noise-sensitive control: suspect ADC sample timing, insufficient filtering, poor current-sense scaling, or quantization.
