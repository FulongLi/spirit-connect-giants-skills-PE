# ANSYS Materials, Mesh, And Boundary-Condition Checklist

## Material Data

- Magnetic core: B-H curve, saturation behavior, core-loss coefficients, frequency range, temperature dependence, and DC bias validity.
- Copper or aluminum: conductivity, temperature coefficient, plating, strand/foil geometry, and skin-depth relevance.
- Insulation and potting: thermal conductivity, dielectric spacing relevance, and whether anisotropy matters.
- Thermal interfaces: TIM thickness, contact resistance, mounting pressure, and heatsink attachment assumptions.

## Mesh Checks

- Refine air gaps, conductor edges, corners, skin-depth regions, high-current-density regions, and thermal hot spots.
- Use mesh operations that match the physics: skin-depth mesh for high-frequency conductors, local refinement for gaps, and boundary-layer or local thermal mesh near interfaces.
- Perform at least one mesh sensitivity run for the output that will drive decisions.
- Report convergence of the target metric, not only global mesh statistics.

## Boundary Conditions

- Electromagnetic boundaries should be far enough away or use appropriate symmetry/infinite boundary assumptions.
- Symmetry planes must match both geometry and excitation; wrong symmetry can suppress leakage or circulating currents.
- Thermal boundaries should reflect the real environment: natural convection, forced airflow, cold plate, enclosure, or test fixture.
- Avoid mixing measurement-derived convection coefficients with predictive thermal claims unless that calibration is explicitly stated.

## Common Credibility Risks

- Material data copied from a similar grade but used outside its frequency or temperature range.
- Thermal conductivity assumed isotropic for winding packs, PCBs, or laminated structures.
- Mesh looks dense globally but is weak in the air gap, edge, or skin-depth region.
- Loss is mapped to the wrong body or averaged across a region where local hot spots matter.
