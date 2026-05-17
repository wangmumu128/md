# Literature-Guided MD Research Ideation

## Purpose

Use this reference when turning literature into molecular dynamics research ideas. The goal is not to summarize papers; it is to identify simulation-answerable gaps.

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
Idea:
Literature gap:
Hypothesis:
System:
Model:
Force field:
Simulation protocol:
Observable(s):
Analysis:
Expected result:
Novelty / Feasibility:
Main risk:
Fallback:
```
