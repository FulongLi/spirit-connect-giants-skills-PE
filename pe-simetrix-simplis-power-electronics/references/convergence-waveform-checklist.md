# Convergence And Waveform Credibility Checklist

## Simulation Setup

- Record whether the run uses SIMetrix SPICE, SIMPLIS, or mixed analysis.
- Record transient stop time, maximum time step, initial conditions, model libraries, and temperature assumptions.
- Confirm the converter is at the intended operating point before measuring load-step, loop, or switching-loss results.
- For double-pulse tests, record pulse timing, initial current, integration windows, and probe locations.

## Convergence Debugging

- Start with an idealized circuit and add nonlinear device models, parasitics, snubbers, and protection blocks gradually.
- Avoid ideal voltage-source/capacitor and current-source/inductor conflicts without damping or realistic parasitics.
- Add small ESR/DCR and physically reasonable leakage paths where necessary.
- If a convergence option fixes the run but changes the waveform, treat the result as suspect until the model is simplified and verified.

## Waveform Credibility

- Check whether key conclusions change with maximum time step.
- Compare ringing frequency with estimated L-C values from package, layout, and device capacitance.
- Probe at physically meaningful points: device pins, current-sense node, DC-link terminals, and controller input.
- Separate numerical spikes from physical overshoot by checking probe reference, time step, parasitics, and device model.

## Red Flags

- Switching energy reported without integration windows or device-pin voltage/current waveforms.
- Overshoot conclusion made without loop inductance or package parasitics.
- Control-loop conclusion made while current limit, soft-start, or saturation is active.
- SIMPLIS fast transient result used to claim detailed semiconductor stress without SPICE-level confirmation.

## Minimum Verdict

Every review should state:

- What waveform or metric is trustworthy.
- What assumption dominates uncertainty.
- What check would make the result credible enough for design use.
