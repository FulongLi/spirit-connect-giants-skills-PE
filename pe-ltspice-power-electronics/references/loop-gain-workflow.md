# LTspice Loop-Gain Injection And Compensation Validation

## Prefer Averaged Models

- For loop-gain and compensation validation, prefer an averaged power-stage model or controlled-source representation.
- Explicitly model modulator gain, sample-and-hold behavior, output LC, ESR zero, and load equivalent.
- Tie every AC conclusion to an operating condition: Vin, Vout, load, duty ratio, and mode.

## Injection Method Checks

- The injection point should preserve DC bias and avoid breaking the operating point.
- Confirm measurement polarity so phase margin is not interpreted backward.
- Keep perturbation amplitude small enough to avoid saturation or mode changes.
- If measuring loop gain on a switching model, verify cycle averaging, steady-state time, and perturbation method.

## Compensation Validation

- Check crossover frequency, phase margin, gain margin, and low-frequency gain.
- For RHP-zero topologies, keep bandwidth below the phase-limited region.
- For current-mode control, include current-sense gain, slope compensation, and sample delay.
- For digital or sampled control, include ZOH, computation delay, and PWM update delay.

## When Results Look Wrong

- Spikes or rough curves: check nonlinear limiting, excessive perturbation, insufficient settling time, or incorrect injection point.
- Abnormal phase jump: check measurement direction, reference node, and transfer-function definition.
- AC stable but transient oscillates: inspect sampling, saturation, delay, and subharmonic behavior in the switching model.
