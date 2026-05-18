# DSP/MCU Digital Control Implementation Workflow

## Map The Timing Path

- Document the full path: PWM event, ADC trigger, sampling window, conversion complete, interrupt entry, control calculation, PWM shadow-load, and gate update.
- Measure or estimate total control delay in switching cycles. Include ADC acquisition, conversion, ISR latency, computation time, and PWM update delay.
- Confirm whether PWM compare values are loaded immediately, at period boundary, or at zero/period events.
- For multi-loop systems, record the update rate of each loop and the phase relationship between loops.

## Peripheral Setup Checks

- ADC: trigger source, acquisition window, channel order, conversion timing, offset calibration, scaling, and sample location relative to switching noise.
- PWM: counting mode, dead time, shadow-load mode, compare update event, synchronization, trip-zone behavior, and complementary output polarity.
- Interrupts: priority, nesting, jitter, missed deadlines, watchdog, DMA conflicts, and background task interference.
- Protection: comparator threshold, digital filter, blanking window, latch behavior, clearing sequence, and interaction with soft-start.

## Algorithm Porting Checks

- Compare C output against the simulation model using the same input samples and coefficients.
- Log intermediate values: error, proportional term, integral term, feedforward term, saturation flag, and duty command.
- Confirm coefficient units, per-unit normalization, sample period, sign convention, and feedback polarity.
- Check anti-windup and output limits before tuning gains on hardware.

## Minimum Hardware Test Sequence

1. Run open loop or fixed duty/frequency at a safe operating point.
2. Validate ADC scaling and offset against external measurements.
3. Enable control at reduced voltage/current limits.
4. Apply a small load step and log internal control variables.
5. Increase operating range only after timing, scaling, and protection behavior are understood.
