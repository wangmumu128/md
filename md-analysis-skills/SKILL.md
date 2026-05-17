---
name: md-analysis-skills
description: Literature-guided molecular dynamics research workflow for generating scientific ideas, designing MD simulation models, producing LAMMPS input scripts, running sanity checks, and analyzing LAMMPS trajectories/logs. Use when Codex is asked to plan MD studies, build molecular dynamics models, generate LAMMPS code, debug LAMMPS setup, or analyze MD outputs such as log files, dumps, RDF, MSD, diffusion, density profiles, stress-strain, adsorption, or interfacial behavior.
---

# MD Analysis Skills

## Core Workflow

Use this skill to convert a molecular dynamics research question into a defensible, executable simulation workflow:

```text
research goal -> literature map -> hypotheses -> model plan -> force field plan
-> LAMMPS inputs -> run checks -> trajectory/log analysis -> research report
```

Keep every proposed idea tied to a measurable observable. Reject ideas that cannot be reduced to a model, force field, simulation protocol, and analysis plan.

## Operating Rules

1. Start by clarifying the target material system, scale, method, and desired observable if they are missing.
2. Treat literature claims as evidence that must be traceable to papers, DOIs, or database records.
3. Separate scientific novelty from simulation feasibility.
4. Do not invent force-field parameters. If parameters are unavailable, state the gap and propose a parameterization route.
5. Prefer established tools for structure and topology generation: Packmol, Moltemplate, VMD/TopoTools, RDKit, Open Babel, ASE, pymatgen, mBuild, foyer, AmberTools, LigParGen, CGenFF, or domain-specific generators.
6. Generate LAMMPS scripts as starting points with explicit assumptions, not as guaranteed production inputs.
7. Before analysis, verify equilibration, timestep stability, temperature/pressure behavior, and whether sampling is sufficient.

## Workflow Decision Tree

- **Literature-to-idea request**: Read `references/research_ideation.md`, then produce ranked hypotheses with evidence, novelty, feasibility, observables, and risks.
- **Model-building request**: Read `references/model_building.md`, then produce structure, force field, boundary condition, ensemble, and equilibration plans.
- **LAMMPS-code request**: Read `references/lammps_generation.md`; use `scripts/generate_lammps_template.py` when a baseline input deck is useful.
- **Simulation-output analysis request**: Read `references/analysis_methods.md`; use `scripts/parse_lammps_log.py` for log summaries when a LAMMPS log is available.
- **End-to-end request**: Follow the full workflow and load only the reference files needed for the current stage.

## Required Outputs

For a research idea, include:

- scientific question
- literature gap
- hypothesis
- candidate system
- force-field strategy
- simulation protocol
- observables
- analysis method
- novelty score and feasibility score
- risks and fallback plan

For a LAMMPS setup, include:

- assumed units and atom style
- expected data file/topology source
- pair, bond, angle, dihedral, improper, and kspace styles as applicable
- minimization, equilibration, and production stages
- timestep, temperature, pressure, ensemble, boundary conditions
- thermo and dump outputs
- post-run analysis plan

For analysis, include:

- files used
- equilibration judgment
- computed metrics
- uncertainty or block-averaging method when applicable
- plots or tables requested by the user
- interpretation tied back to the hypothesis

## Bundled Tools

Use `scripts/generate_lammps_template.py` to create a minimal three-stage LAMMPS input set:

```bash
python scripts/generate_lammps_template.py --system polymer-electrolyte --units real --atom-style full --output ./case
```

Use `scripts/parse_lammps_log.py` to extract thermo columns and summary statistics:

```bash
python scripts/parse_lammps_log.py log.lammps --csv thermo.csv --summary summary.json
```

## Quality Gates

Before finalizing any MD workflow, check:

- The proposed observable answers the hypothesis directly.
- The model size and simulation time are realistic for the available compute.
- The force field matches the chemistry and target properties.
- Long-range electrostatics, constraints, and boundary conditions are stated.
- Equilibration and production are separated.
- Analysis scripts match the actual LAMMPS outputs.
- The report distinguishes simulated evidence from literature evidence.
