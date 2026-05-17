---
name: md-analysis-skills
description: Literature-first molecular dynamics research workflow for keyword-driven literature review, 5-year latest-paper coverage, pre-5-year classic-paper synthesis, research-gap discovery, five-direction proposal and confirmation, then MD experimental/simulation method design, model structure planning, LAMMPS input generation, sanity checks, and MD data analysis. Use when Codex is asked to plan MD studies, generate research ideas from literature, build molecular dynamics models, generate LAMMPS code, debug LAMMPS setup, or analyze MD outputs such as logs, dumps, RDF, MSD, diffusion, density profiles, stress-strain, adsorption, or interfacial behavior.
---

# MD Analysis Skills

## Core Workflow

Use this skill to convert a molecular dynamics research question into a defensible, executable simulation workflow. Always run the literature-first stage before designing models or LAMMPS inputs:

```text
keywords -> literature map -> gaps -> five directions -> user confirms one direction
-> experimental/simulation method -> model structure -> force field plan
-> LAMMPS inputs -> run checks -> trajectory/log analysis -> research report
```

Keep every proposed idea tied to a measurable observable. Reject ideas that cannot be reduced to a model, force field, simulation protocol, and analysis plan.

## Operating Rules

1. Require user-provided search keywords before literature research. If keywords are missing, ask for keywords and stop.
2. During literature research, cover both the latest five years and classic papers older than five years. Treat "latest five years" relative to the current date.
3. Do not proceed to experimental method, model structure, force field, or LAMMPS generation until the user selects one of five proposed research directions.
4. Treat literature claims as evidence that must be traceable to papers, DOIs, or database records.
5. Separate scientific novelty from simulation feasibility.
6. Do not invent force-field parameters. If parameters are unavailable, state the gap and propose a parameterization route.
7. Prefer established tools for structure and topology generation: Packmol, Moltemplate, VMD/TopoTools, RDKit, Open Babel, ASE, pymatgen, mBuild, foyer, AmberTools, LigParGen, CGenFF, or domain-specific generators.
8. Generate LAMMPS scripts as starting points with explicit assumptions, not as guaranteed production inputs.
9. Before analysis, verify equilibration, timestep stability, temperature/pressure behavior, and whether sampling is sufficient.

## Mandatory Stage Gate

For any new research-planning request:

1. Ask for keywords if the user has not provided them.
2. Search and synthesize recent papers from the latest five years and classic papers older than five years.
3. Summarize the literature landscape, unresolved gaps, contradictions, and methodological weaknesses.
4. Propose exactly five research directions.
5. Ask the user to choose one direction and stop.
6. Only after the user confirms a direction, discuss experimental/simulation methods, MD model structure, force field, and LAMMPS implementation.

## Workflow Decision Tree

- **Literature-to-idea request**: Read `references/research_ideation.md`, require keywords, survey latest-five-year and pre-five-year classic papers, summarize gaps, propose exactly five directions, ask the user to select one, and stop.
- **Model-building request**: Read `references/model_building.md`, then produce structure, force field, boundary condition, ensemble, and equilibration plans.
- **LAMMPS-code request**: Read `references/lammps_generation.md`; use `scripts/generate_lammps_template.py` when a baseline input deck is useful.
- **Simulation-output analysis request**: Read `references/analysis_methods.md`; use `scripts/parse_lammps_log.py` for log summaries when a LAMMPS log is available.
- **End-to-end request**: Follow the full workflow and load only the reference files needed for the current stage.

## Required Outputs

For the initial literature stage, include:

- user keywords and any expanded search terms
- databases or sources searched
- latest-five-year literature synthesis
- classic pre-five-year literature synthesis
- research gaps and methodological weaknesses
- exactly five candidate directions
- a question asking the user to choose one direction

For each candidate research direction, include:

- scientific question
- literature gap
- hypothesis
- candidate system
- observables
- analysis method
- novelty score and feasibility score
- risks and fallback plan

After the user confirms one direction, include:

- experimental or simulation route
- model structure design
- force-field strategy
- simulation protocol
- validation plan

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
