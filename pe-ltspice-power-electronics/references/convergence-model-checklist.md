# LTspice Convergence And Model Credibility Checklist

## Fix Model Physicality First

- Avoid ideal voltage sources directly in parallel with ideal capacitors.
- Avoid ideal current sources directly in series with ideal inductors.
- Add reasonable parasitics to inductors, capacitors, switches, and interconnect.
- Check floating nodes, high-impedance nodes, and control inputs without a DC path.

## Then Tune Simulation Settings

- Reduce maximum time step and check whether the key conclusion changes.
- Use initial conditions only when needed, and record why they are needed so startup issues are not hidden.
- Use `.options` carefully. Do not relax tolerances as a substitute for fixing the model.
- For strongly nonlinear models, enable realistic device behavior incrementally.

## Device Model Checks

- Controller macro-models may only support typical application behavior and may not be valid for AC, startup, or protection-boundary tests.
- Op amp and comparator models should include output swing, input common-mode range, slew rate, delay, and saturation recovery if those effects matter.
- MOSFET models should be checked for body diode behavior, output capacitance, gate charge, and temperature assumptions.
- Diode models should be checked for reverse recovery and junction capacitance when they affect the target waveform.

## Credibility Gate

Before making an engineering conclusion, confirm:

- Key waveforms are not sensitive to maximum time step.
- The model has no obvious non-physical ideal-source conflicts.
- The target condition is at steady state, or the analysis explicitly concerns startup.
- The controller has not entered an unmodeled or incorrectly modeled protection state.
