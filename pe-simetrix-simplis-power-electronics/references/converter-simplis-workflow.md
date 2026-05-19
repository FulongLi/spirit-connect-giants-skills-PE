# Converter And SIMPLIS Transient Workflow

## Choose SIMetrix Or SIMPLIS Deliberately

- Use SIMPLIS when the priority is fast switching-converter transient behavior, startup, load step, line step, loop response, and control iteration.
- Use SIMetrix SPICE when semiconductor switching detail, gate-drive shape, reverse recovery, parasitic ringing, or analog circuit fidelity matters.
- Use both when needed: SIMPLIS for system behavior and SIMetrix for detailed stress or waveform validation at selected operating points.

## Converter Model Setup

- Start with a minimal converter model: source, switch network, magnetic element, output filter, load, feedback path, and essential protection.
- Add parasitics only after the idealized converter reaches the expected operating point.
- Keep control saturation, current limit, soft-start, dead time, and pulse-skipping behavior explicit when they affect the target waveform.
- For resonant converters, confirm operating region, magnetizing current, resonant tank current, frequency limit, and synchronous rectifier timing before tuning the controller.

## Transient Test Sequence

1. Run open-loop or fixed-command operation at a safe operating point.
2. Enable closed loop and check startup without load-step disturbance.
3. Apply a small load step, then increase step amplitude after the basic response is understood.
4. Sweep input voltage, load, compensation parameters, current-limit threshold, and dead time.
5. Compare key operating points with a SPICE-level SIMetrix model if device stress or parasitic ringing matters.

## Key Waveforms

- Input voltage/current, output voltage/current, and inductor or transformer current.
- Switch-node voltage, gate-drive signal, diode or synchronous FET current, and clamp/snubber current.
- Feedback signal, error amplifier output, controller command, limit flags, and soft-start state.
- For resonant or multi-mode converters, frequency command, tank current, magnetizing current, and mode-transition flags.

## Common Interpretation Risks

- A fast SIMPLIS model may hide device-level switching details that dominate stress or EMI.
- A detailed SPICE model may be too slow or convergence-sensitive for wide control sweeps.
- Startup behavior can be mistaken for load-step response if the converter is not settled first.
- A control loop may appear unstable because current limit, soft-start, or saturation is active.
