# Confirmed Direction Protocol Design

## Purpose

Use this reference only after the user has selected one of the five literature-derived research directions. Build a complete executable experiment/simulation plan from the first software operation to final data analysis.

## Protocol Standard

Do not write only conceptual meaning. Every step must tell the user what to do.

For each step, specify:

- step objective
- software name and version if known
- exact menu path, button, panel, command, or script to use
- files to download, create, save, or export
- parameters to type
- expected screen/output/file
- success check
- common failure and fix
- beginner followability check

If a step says "build model", "run simulation", "analyze data", or "plot result" without concrete software operations, rewrite it.

## Software-Level Guidance Examples

Use concrete instructions like:

- VMD: `File > New Molecule > Browse > Load`, then `Extensions > Tk Console`.
- OVITO: `File > Load File`, then `Add modification > Coordination analysis`.
- Materials Studio: `File > Import`, then choose the CIF or molecular file; use `Build > Symmetry > Supercell` when needed.
- Packmol: create `packmol.inp`, then run `packmol < packmol.inp`.
- Moltemplate: prepare `.lt` files, then run `moltemplate.sh system.lt`.
- LAMMPS: run `lmp -in in.minimize`, then check `log.lammps`.
- Python/Jupyter: open the notebook, run cells from top to bottom, and verify plots and CSV outputs.

Adapt software choices to the user's operating system, license availability, and target system.

## Step-by-Step Expansion Rule

After drafting one step, perform this check:

```text
Can a careful 10-year-old follow this with no hidden assumptions?
```

If no, add:

- where to click
- what file name to use
- what value to type
- what the output should look like
- how to know it worked

Only then continue to the next step.

## Required Protocol Sections

1. Research direction and hypothesis
2. Literature rationale and gap
3. Overall workflow
4. Software and environment preparation
5. Structure/model construction
6. Force-field and parameter preparation
7. LAMMPS data/input generation
8. Energy minimization
9. Equilibration
10. Production simulation
11. Trajectory visualization and sanity checks
12. Quantitative analysis
13. Plot/table generation
14. Interpretation against the hypothesis
15. Failure diagnosis and fallback plan

## Analysis Specificity

For each analysis, state:

- exact input file
- software or Python package
- command or notebook cell purpose
- atom selection
- parameter choices such as cutoff, bin width, lag time, or fit window
- output file name
- interpretation rule
