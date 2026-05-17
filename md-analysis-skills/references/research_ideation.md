# Literature-Guided MD Research Ideation

## Purpose

Use this reference when turning literature into molecular dynamics research ideas. The goal is not to summarize papers; it is to identify simulation-answerable gaps.

## Required User Input

Require keywords before starting literature research. If the user has not supplied keywords, ask for:

- core material/system keywords
- method keywords such as molecular dynamics, LAMMPS, ReaxFF, coarse-grained MD, or enhanced sampling
- property keywords such as diffusion, adsorption, interface, mechanical behavior, ion transport, hydration, or thermal transport

Do not perform model design before keyword-based literature synthesis is complete.

## Literature Coverage Requirement

Search two literature windows:

1. Latest literature: all relevant work from the latest five years, relative to the current date.
2. Classic literature: important papers older than five years that established the field, model, force field, mechanism, or analysis method.

Use multiple scholarly sources when available, such as Web of Science, Scopus, PubMed, Crossref, Semantic Scholar, arXiv, Google Scholar, publisher pages, or local PDF libraries. If full coverage is impossible, state the searched sources and the limitation explicitly.

For recent literature, prioritize comprehensive coverage over cherry-picking. For classic literature, prioritize high-citation, method-defining, or frequently reused studies.

## Literature Extraction Schema

For each paper or database record, extract:

- material system
- molecular or atomistic model
- force field and parameter source
- ensemble, timestep, temperature, pressure, simulation length
- observables and analysis methods
- main finding
- stated limitation
- unstated limitation or unexplored variable
- data/code availability
- DOI or stable URL
- whether it belongs to the latest-five-year group or the classic group

## Synthesis Sequence

1. Build and show the keyword strategy, including synonyms and exclusions.
2. Summarize latest-five-year studies by topic, material system, method, and finding.
3. Summarize classic pre-five-year studies by foundational contribution.
4. Compare latest and classic literature to identify what has changed and what remains unsolved.
5. Extract research loopholes: missing variables, weak assumptions, unvalidated force fields, insufficient sampling, unexplored systems, conflicting conclusions, or absent mechanism.
6. Propose exactly five new research directions.
7. Ask the user to choose one direction before discussing experimental/simulation method or model structure.

## Gap Types That Often Produce Good MD Ideas

- composition not explored
- interface not modeled
- temperature, pressure, strain, humidity, pH, salinity, or electric-field condition missing
- mechanism inferred experimentally but not resolved molecularly
- force field comparison absent
- equilibrium property studied but dynamics not studied
- bulk behavior studied but confinement/surface behavior missing
- single-component system studied but multicomponent competition matters
- structure-property trend observed but no molecular descriptor identified

## Idea Scoring

Score each candidate from 1 to 5:

- novelty: low if many direct simulations exist
- feasibility: low if force-field parameters are missing or timescale is unrealistic
- mechanistic value: high if MD can expose a process inaccessible experimentally
- analysis clarity: high if observables map cleanly to the hypothesis
- publication potential: high if the idea links to a current materials or molecular design problem

Prefer ideas with high mechanistic value and analysis clarity even if novelty is moderate.

## Output Template

```text
Keywords:
Expanded search terms:
Sources searched:

Latest five-year literature:
- Paper / DOI:
  Finding:
  Limitation:

Classic pre-five-year literature:
- Paper / DOI:
  Foundational contribution:
  Remaining limitation:

Research loopholes:
1.
2.
3.

Five candidate directions:
1. Direction:
   Scientific question:
   Literature gap:
   Hypothesis:
   Candidate system:
   Observable(s):
   Analysis:
   Novelty / Feasibility:
   Main risk:
   Fallback:

Question:
Please choose one of the five directions. After confirmation, proceed to experimental/simulation method and model structure design.
```
