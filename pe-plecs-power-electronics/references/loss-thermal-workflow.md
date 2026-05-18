# PLECS Loss And Thermal Simulation Workflow

## Electrical First

- Confirm the electrical switching waveform before trusting loss or temperature predictions.
- Check current direction, device conduction intervals, dead time, reverse recovery, and switching-node behavior.
- Loss models inherit any electrical modeling error, so do not tune thermal results to compensate for an incorrect electrical waveform.

## Semiconductor Losses

- Confirm device model source, temperature assumptions, gate resistance, switching energy curves, and conduction characteristics.
- Check whether switching losses are evaluated at the right voltage, current, temperature, and gate-drive condition.
- Separate conduction loss, switching loss, diode or body-diode loss, and reverse-recovery related loss when diagnosing hot devices.
- Run loss sweeps across load, input voltage, switching frequency, and modulation index or duty ratio.

## Magnetic And Passive Losses

- For inductors and transformers, separate copper loss, core loss, AC winding loss, and saturation margin where the model supports it.
- Confirm ripple current and flux swing before using core-loss conclusions.
- Capacitor RMS current and ESR loss should be checked at the actual ripple frequency content, not only average current.

## Thermal Network

- Keep thermal boundary conditions explicit: ambient temperature, heatsink, airflow, interface material, and thermal resistance network.
- Start with a simple thermal network and add detail only when the result requires it.
- Verify thermal time constants against the experiment being simulated. Do not infer steady-state temperature from a short transient unless the model supports it.
- Record final junction, case, heatsink, and ambient temperatures with the operating condition that produced them.

## Credibility Checks

- Compare total input/output power balance against summed losses.
- Check whether the hottest device matches the expected current path and switching stress.
- Repeat the loss/thermal run at at least one known or hand-calculable operating point.
