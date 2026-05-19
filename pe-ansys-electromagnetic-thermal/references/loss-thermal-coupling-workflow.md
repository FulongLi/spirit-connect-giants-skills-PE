# ANSYS Loss Extraction And Thermal Coupling Workflow

## Loss Extraction

- Separate copper DC loss, copper AC loss, core loss, eddy loss in shields or busbars, and semiconductor/module losses when possible.
- Confirm whether the excitation waveform is sinusoidal, piecewise current, harmonic spectrum, or transient switching waveform.
- For core loss, check whether the selected model supports the material, frequency range, flux waveform, DC bias, and temperature range.
- For winding loss, check skin depth, proximity effect, strand/foil representation, and temperature-dependent conductivity.

## Preparing Thermal Inputs

- Export loss by physical body or meaningful region, not as a single lumped number when hot-spot prediction matters.
- Preserve coordinate alignment and body names when transferring losses from Maxwell or Q3D to Icepak or Mechanical.
- Check power balance: electrical input/output or expected I2R loss should be consistent with the extracted loss magnitude.
- Do not tune convection coefficients to hide an electromagnetic loss-modeling error.

## Thermal Model Setup

- Define ambient temperature, airflow, heatsink, enclosure, thermal interface material, radiation, and mounting assumptions.
- Use realistic thermal conductivity for anisotropic materials such as PCB, winding packs, insulation, ferrite, and gap fillers.
- Add contact resistance or TIM layers where they dominate thermal impedance.
- Choose steady-state or transient thermal analysis according to the engineering question.

## Electro-Thermal Iteration

- If temperature significantly changes copper resistance, core loss, or semiconductor loss, iterate EM loss and thermal solution.
- Record each iteration's loss, material temperature, and convergence criterion.
- Check whether the hot spot is located where the loss source predicts it. A mismatch often means a boundary condition or loss mapping issue.
