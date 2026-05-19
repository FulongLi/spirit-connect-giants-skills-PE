# COMSOL Thermal And Multiphysics Coupling Workflow

## Heat Source Definition

- Separate heat sources by physical origin: copper loss, core loss, busbar loss, PCB loss, semiconductor loss, contact loss, and external heat input.
- Use spatially distributed losses when hot spots matter; use lumped heat only when temperature gradients are not the target.
- Check power balance before coupling losses into thermal simulation.
- Avoid tuning heat sources to force agreement with a temperature measurement.

## Heat Transfer Setup

- Choose conduction, convection, radiation, CFD, or simplified heat-transfer coefficients according to the engineering question.
- Define ambient temperature, airflow, coolant, cold plate, heatsink, enclosure, mounting, and thermal interface material explicitly.
- Use anisotropic thermal conductivity for PCB stacks, winding packs, laminated cores, and composite insulation when it matters.
- Include contact resistance or thin-layer approximations where thermal interfaces dominate.

## Coupling Strategy

- One-way coupling is appropriate when temperature does not significantly affect loss or material behavior.
- Iterative or fully coupled analysis is needed when copper resistance, core loss, semiconductor loss, or permeability changes strongly with temperature.
- Record convergence criteria for electro-thermal iterations: loss change, maximum temperature change, or material-property change.
- Check whether the hot spot aligns with the dominant loss source and expected thermal path.

## Transient Versus Steady State

- Use steady-state thermal analysis for final operating temperature and thermal resistance.
- Use transient analysis for startup, overload, pulse load, thermal protection, and time-to-limit studies.
- Do not infer steady-state safety from a short transient unless the thermal time constant is validated.
