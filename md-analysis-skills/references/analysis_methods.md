# MD Analysis Methods Reference

## First Checks

Before interpreting trajectories:

- parse thermo output
- check temperature, pressure, total energy, density, and volume stability
- identify equilibration window
- discard unstable or unequilibrated frames
- use block averaging for uncertainty when reporting scalar properties

## Method Selection

- RDF: local structure, coordination, ion pairing, solvation shell.
- MSD: diffusion coefficient; fit only the linear regime.
- Density profile: interfaces, confinement, adsorption layers.
- Hydrogen bonding: network structure and lifetime.
- Coordination number: metal-ion, solvent-ion, or surface binding environment.
- Cluster analysis: aggregation, phase separation, ion clusters.
- Stress-strain: mechanical response; verify deformation protocol.
- Viscosity: Green-Kubo or non-equilibrium methods; needs long sampling.
- Adsorption energy: compare bound and reference states with consistent model definitions.
- Interfacial energy: requires carefully defined thermodynamic path and finite-size checks.

## Reporting Standard

Every plot or metric should state:

- trajectory files used
- equilibration cutoff
- atom selections
- bin size or fit range
- unit conversion
- uncertainty estimate
- interpretation relative to the hypothesis
