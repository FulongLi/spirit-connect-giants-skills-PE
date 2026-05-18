# FPGA And High-Speed FPGA Control Workflow

## Datapath Architecture

- Draw the pipeline from ADC interface to filtering, control law, limiter, PWM generation, and protection output.
- Count latency in clock cycles and convert it to switching-cycle phase delay.
- Keep word length, binary point, saturation behavior, and rounding mode explicit at every datapath stage.
- Treat clock-domain crossings as design elements, not wiring details. Document synchronizers, FIFOs, valid signals, and reset behavior.

## HDL Verification Checks

- Run testbench vectors from Simulink, PLECS, or a floating-point reference model through the HDL implementation.
- Compare internal signals, not only final duty command: error, filter states, multiply-accumulate output, limiter state, and PWM compare.
- Test startup, saturation, sign changes, zero crossing, current reversal, and protection activation.
- Add assertions for overflow, invalid state, out-of-range duty, stale sample, and unexpected clock-domain crossing behavior.

## PWM And Protection

- Confirm carrier mode, compare update timing, complementary output polarity, dead time, and minimum pulse constraints.
- Protection paths should be deterministic and faster than software paths when hardware safety depends on them.
- Verify trip latch, fault clear, blanking window, and restart sequencing in simulation and on hardware.
- For multi-phase systems, confirm phase offsets, synchronization, and interleaving remain correct after resets.

## Bring-Up Strategy

1. Validate clocks, resets, ADC interface, and PWM output with the power stage disabled.
2. Feed known ADC test patterns into the datapath and compare expected duty command.
3. Enable gate outputs at safe voltage/current and fixed command.
4. Enable closed loop with conservative limits and log internal debug buses.
5. Increase bandwidth only after latency, scaling, and protection behavior are verified.
