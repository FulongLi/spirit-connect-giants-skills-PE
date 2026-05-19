# COMSOL Validation And Reporting Checklist

## Minimum Validation

- Compare inductance, impedance, resistance, loss, or temperature rise against hand calculation, datasheet, or measurement.
- Validate at more than one operating point when the model will be used for sweeps or design decisions.
- Run sensitivity checks for mesh, material properties, thermal boundary conditions, and operating point.
- Check power balance before accepting thermal predictions.

## Reporting Outputs

- Physics interfaces, study type, geometry version, simplifications, material sources, mesh settings, and boundary conditions.
- Operating point: waveform, current, frequency, DC bias, ambient, airflow/coolant, duty, and thermal assumptions.
- Electromagnetic outputs: inductance, flux density, current density, loss breakdown, field leakage, and saturation regions.
- Thermal outputs: temperature map, hot-spot location, thermal path, thermal resistance, and time-to-limit if transient.
- Validation comparison, sensitivity results, and limitations.

## Red Flags

- A multiphysics model is trusted before each physics domain is checked independently.
- Loss is spatially averaged while hot-spot temperature is the decision metric.
- Boundary conditions are convenient rather than representative of the real test or product environment.
- Solver convergence is treated as proof of physical correctness.
- Material properties are used outside their frequency, temperature, or bias validity range.

## Expert Verdict Format

When reviewing a COMSOL model, state:

- The result that is currently trustworthy.
- The result that is only directional.
- The dominant uncertainty source.
- The minimum experiment or model refinement needed next.
