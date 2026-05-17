# MD Model Building Reference

## Model Planning Checklist

Define:

- chemistry and composition
- target phase: gas, liquid, amorphous solid, crystal, surface, interface, nanopore, polymer, electrolyte, biomolecule, or composite
- resolution: all-atom, united-atom, coarse-grained, reactive, polarizable, or hybrid
- box size and boundary conditions
- number of molecules, density, concentration, charge neutrality
- initial structure source
- topology source
- force-field source and citation
- equilibration route

## Structure Generation Routes

- Small organic molecules: RDKit, Open Babel, LigParGen, CGenFF, AmberTools.
- Packed liquids/electrolytes: Packmol followed by topology assignment.
- Polymers: mBuild, foyer, Polymatic, custom chain builders, or Moltemplate.
- Crystals and inorganic solids: pymatgen, ASE, Materials Project structures, crystallographic CIF files.
- Surfaces/interfaces: cleave slab with ASE/pymatgen, add vacuum or liquid layer, equilibrate carefully.
- Biomolecules: PDB plus AmberTools, CHARMM-GUI, or GROMACS conversion if justified.

## Force-Field Decision Guide

- Organic liquids/polymers: OPLS-AA, GAFF, CGenFF, PCFF, COMPASS where appropriate.
- Biomolecules: AMBER, CHARMM, OPLS-AA.
- Inorganic solids: CLAYFF, INTERFACE FF, ReaxFF, COMB, EAM, MEAM, Tersoff, Stillinger-Weber depending on chemistry.
- Electrolytes: verify ion parameters, mixing rules, dielectric behavior, and transport-property validation.
- Reactions/bond breaking: use ReaxFF/COMB only when parameter set covers all elements and target chemistry.

Never claim a force field is valid without checking whether it was parameterized for the relevant chemistry and property.

## Pre-Run Sanity Checks

- no overlapping atoms after packing
- charge neutrality or explicit charged-system rationale
- realistic density
- correct atom types and masses
- all bonds/angles/dihedrals parameterized
- pair coefficients complete
- timestep compatible with fastest motion
- kspace enabled when long-range charges require it
- neighbor settings reasonable
