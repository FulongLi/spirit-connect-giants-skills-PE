# COMSOL Electromagnetic Modeling Workflow

## Choose The Physics And Study Type

- Use the physics interface that matches the question: magnetic field, electric current, eddy current, frequency domain, transient, or coupled multiphysics.
- Use 2D/2D axisymmetric only when geometry, excitation, and fields justify it. Use 3D for end effects, busbars, leakage paths, planar magnetics, and asymmetric layouts.
- For high-frequency conductors, decide whether skin and proximity effects require resolved conductors, homogenized material, impedance boundary, or loss correction.
- For nonlinear magnetics, include the B-H curve and operating bias if saturation or inductance shift matters.

## Geometry And Domain Setup

- Preserve air gaps, conductor placement, magnetic path, leakage path, shield plates, PCB copper paths, and thermal interfaces.
- Simplify small mechanical features only after checking they do not affect current density, flux density, or heat flow.
- Define surrounding air or infinite-element domains when field leakage matters.
- Use symmetry only when both geometry and excitation are symmetric.

## Excitation And Waveform

- Use current excitation when current waveform is known and power-stage operation is external to the model.
- Use voltage or circuit coupling only when the external circuit behavior is represented credibly.
- For nonsinusoidal waveforms, include the harmonic components that dominate loss and field distribution.
- For multi-winding magnetics, confirm polarity, turns, load condition, leakage path, and winding connection.

## Result Checks

- Inspect flux-density hot spots, current-density distribution, eddy-current paths, stored energy, and field leakage.
- Compare inductance, resistance, or impedance with hand calculation, datasheet, or measurement.
- Run mesh sensitivity in air gaps, conductor edges, skin-depth regions, and high-field regions.
- If the target output changes materially with mesh refinement, do not use the result for thermal decisions yet.
