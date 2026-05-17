# Visual and Word Output Reference

## Purpose

Use this reference when the confirmed direction requires polished workflow diagrams, model structure schematics, and a Word document.

## Image2 Figure Generation

Use image2/gpt-image-2 image generation when available. If the user provides a reference style, imitate the visual style while preserving scientific accuracy. If no style is provided, use a clean Nature-style scientific schematic: white or light background, restrained colors, clear labels, arrows, and publication-ready composition.

Generate at least two visual assets:

1. Experimental/simulation workflow chart showing the complete route from literature, model construction, LAMMPS run, analysis, to conclusion.
2. Model structure schematic showing molecules/materials, interfaces, simulation box, periodic boundary conditions, important interactions, and measured observables.

Optional assets:

- force-field parameter flow
- data analysis pipeline
- before/after mechanism schematic

## Image Prompt Requirements

Each image prompt must include:

- figure type
- target audience
- scientific system
- visual style
- labeled components
- arrows/process flow
- what must not be shown
- aspect ratio or page placement

Do not generate purely decorative images. Every image must explain a step, model, or mechanism.

## Structure Rationality Explanation

After creating the structure schematic, explain:

- why the selected molecular/material model represents the research question
- why the box size, boundary condition, composition, and phase are reasonable
- why the selected force field or parameterization route is appropriate
- what limitations remain
- which observables validate or challenge the model

## Word Document Assembly

When producing Word output, create a `.docx` that contains:

- title
- selected research direction
- keyword strategy and literature basis
- latest-five-year and classic-literature summary
- research loopholes
- hypothesis
- complete step-by-step protocol
- software/button-level instructions
- generated workflow figure
- generated structure schematic
- model-structure rationality explanation
- LAMMPS input plan or appendix
- analysis plan
- expected results
- failure diagnosis and fallback plan
- references

Use document-generation tooling when available, render the Word document to PDF or page images if possible, and visually check that figures and text are not overlapping.

## Beginner Readability Check

Before finalizing the Word document, audit each procedural section:

- Does each step name the software?
- Does each step say exactly what to click or run?
- Does each step say what output to expect?
- Does each step include a success check?
- Could a careful beginner follow it without asking what to do next?

If any answer is no, revise the section before final delivery.
