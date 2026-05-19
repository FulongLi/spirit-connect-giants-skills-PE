# ANSYS Validation And Reporting Checklist

## Minimum Validation

- Compare inductance, resistance, impedance, or loss against hand calculations or measurement where available.
- Compare thermal result against at least one thermal measurement, thermal camera image, thermocouple point, or known thermal resistance when possible.
- Run sensitivity checks for mesh, material, boundary condition, and operating point.
- Confirm that the simulated current or flux waveform matches the real converter operating condition.

## Reporting Outputs

- Geometry version, simplifications, material sources, solver type, mesh settings, and boundary conditions.
- Operating point: current waveform, frequency spectrum, ambient, airflow, duty cycle, and thermal assumptions.
- Loss breakdown by component and region.
- Temperature map, hot-spot location, thermal path, and thermal resistance estimate.
- Validation comparison and known limitations.

## Red Flags

- A single colorful field plot is presented without mesh, material, or boundary-condition context.
- Loss or temperature is reported with high precision but no validation or sensitivity check.
- Thermal hot spot does not align with the dominant loss source.
- Simulation matches one measurement only after hidden tuning of material or convection values.
- The model predicts safe temperature while a key thermal interface or contact resistance is missing.

## Expert Verdict Format

When reviewing a model, state:

- What result is currently trustworthy.
- What result is directional only.
- What assumption dominates uncertainty.
- What minimum validation action should be done next.
