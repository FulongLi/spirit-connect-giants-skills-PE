# ANSYS Maxwell Electromagnetic Modeling Workflow

## Start From The Engineering Question

- Define the trusted output before building the model: inductance, leakage inductance, winding loss, core loss, busbar loss, stray inductance, current sharing, or saturation margin.
- Pick 2D only when geometry and excitation are genuinely invariant along the ignored dimension. Use 3D for fringing, end effects, busbar loops, planar magnetics, and asymmetric current paths.
- Decide whether the study is magnetostatic, eddy-current, transient, or frequency-domain before choosing excitations and material data.

## Geometry Simplification

- Preserve current paths, air gaps, magnetic path lengths, winding placement, shield plates, and busbar loop area.
- Simplify cosmetic features, tiny fillets, screws, and non-current-carrying details only after confirming they do not affect flux or current density.
- For Litz wire, foil, or planar windings, choose whether to model individual conductors, homogenized regions, or equivalent loss data based on the target frequency and accuracy.
- For gapped magnetics, keep gap geometry and fringing region credible; small gap changes can dominate local loss and saturation.

## Excitation Setup

- Use current excitation when current waveform is known and voltage is not the target result.
- Use voltage excitation only when winding impedance, waveform, and external circuit coupling are represented credibly.
- For multi-winding magnetics, confirm winding polarity, turns ratio, leakage path, and load condition.
- For harmonic-rich waveforms, include the frequency components that dominate AC loss and proximity effect.

## Result Checks

- Inspect flux density hot spots, current-density distribution, eddy-current loops, field symmetry, and energy storage.
- Compare inductance or resistance against hand calculation, datasheet, impedance analyzer data, or low-frequency measurement.
- Run at least one mesh refinement check around gaps, corners, skin-depth regions, and conductor edges.
- If loss changes strongly after mesh refinement, do not use the result for thermal coupling yet.
