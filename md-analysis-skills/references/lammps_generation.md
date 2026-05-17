# LAMMPS Generation Reference

## Input Deck Structure

Use separate files when possible:

- `in.minimize`: read data, define force field, minimize energy.
- `in.equilibration`: thermalize and density/pressure equilibrate.
- `in.production`: collect trajectory and thermo outputs.
- `submit.slurm`: optional HPC submission script.

## Required LAMMPS Sections

Include:

- `units`
- `atom_style`
- `boundary`
- `read_data`
- force-field styles and coefficients
- neighbor settings
- thermo settings
- minimization
- velocity initialization when appropriate
- fixes for ensemble control
- dump outputs
- restart outputs for long runs

## Common Choices

- Molecular systems with bonds and charges: `units real`, `atom_style full`, `pair_style lj/cut/coul/long`, `kspace_style pppm`.
- Metals: `units metal`, `atom_style atomic`, EAM/MEAM as appropriate.
- Coarse-grained systems: `units lj` or `real`, often `atom_style molecular` or `full`.
- Reactive systems: ReaxFF with charge equilibration when required by the parameter set.

## Failure Patterns

- `Lost atoms`: timestep too large, bad initial structure, unstable pressure coupling, or bad force-field parameters.
- `Non-numeric pressure`: overlaps, bad parameters, or unstable integration.
- `Bond atoms missing`: bad timestep, communication cutoff, or bad topology.
- `All pair coeffs are not set`: missing type interactions or incomplete force-field section.

When debugging, reduce timestep, minimize more carefully, run NVT before NPT, and inspect the initial structure visually.
