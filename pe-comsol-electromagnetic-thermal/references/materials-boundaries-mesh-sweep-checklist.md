# COMSOL Materials, Boundaries, Mesh, And Sweep Checklist

## Material Data

- Magnetic material: B-H curve, saturation, loss model, frequency range, temperature dependence, and DC bias validity.
- Conductors: conductivity, temperature coefficient, strand/foil/layer structure, plating, and skin-depth relevance.
- Thermal materials: anisotropy, contact resistance, TIM thickness, insulation, potting, coolant, and airflow assumptions.
- Document whether values are measured, datasheet, estimated, or calibrated.

## Boundary Conditions

- Electromagnetic boundaries should not artificially suppress leakage fields or eddy-current paths.
- Thermal boundaries should match the actual environment: natural convection, forced convection, cold plate, heat sink, enclosure, or test fixture.
- Symmetry boundaries must match geometry, excitation, and thermal environment.
- Avoid claiming predictive accuracy when convection or contact resistance is fitted to one measurement without disclosure.

## Mesh Strategy

- Refine air gaps, conductor edges, skin-depth regions, high-current-density regions, thermal interfaces, and hot spots.
- Use boundary layer, swept, mapped, or local refinement where it matches the physics.
- Run mesh convergence on the decision metric: inductance, loss, hot-spot temperature, thermal resistance, or current sharing.
- Do not accept a mesh only because the solver converged.

## Parameter Sweep Strategy

- Sweep current, frequency, DC bias, air gap, conductor spacing, material grade, convection coefficient, and ambient temperature when relevant.
- Separate design sweeps from uncertainty sweeps. Design sweeps explore choices; uncertainty sweeps expose model risk.
- Save failed or suspicious sweep points with geometry, material, mesh, boundary, and solver settings.
