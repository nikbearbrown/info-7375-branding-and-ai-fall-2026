# Assignment 3 — Visual identity system

## Executive summary

**What this is.** Professor Bear's Assignment 3 for INFO 7375 Branding and AI: design tokens in JSON, a Python generator that turns them into an SVG identity specimen, and a written rationale for the direction chosen. Built live in class on 2026-09-26.

**Why read it.** Two reasons. It is a worked example of the assignment, with the process recorded in [`../FRICTIONAL.md`](../FRICTIONAL.md) rather than smoothed over. And it is doing double duty: Assignment 2 found a real Figma Designer Advocate posting and a real gap in my own CV — *never shipped a design system with tokens and Dev Mode handoff*. This is that gap being closed where anyone can check it.

**Where it stands.** Nothing built yet. This folder is a placeholder created at the start of the demo; the sections below are the plan, not results. Nothing here has been run, and no claim in it has been verified.

---

## What the assignment asks for

From [`assignments/fall-2026/assignment-03.md`](../../../assignments/fall-2026/assignment-03.md), bundling Lesson 5:

| Phase | What it requires |
|---|---|
| **Predict** | Which palette, type, and spacing choices communicate the strategy — and a predicted readability problem, written down *before* the specimen is rendered |
| **Build It** | A Python script that reads JSON design tokens and produces an SVG specimen showing colors, text hierarchy, and spacing; it must validate hex colors, reject non-positive sizes, and report missing required tokens |
| **Use It** | Claude Code implements the specimen from the creative brief; two design directions compared and one chosen against stated audience and strategy criteria |
| **Ship It** | Creative brief, `tokens.json`, generator, SVG specimen, design rationale, tests, inputs, actual outputs, source credits, submission record — here on GitHub and matching on Canvas |
| **Verify** | Inspect the rendered specimen for clipping, legibility, consistency; test malformed colors and zero sizes; document the accessibility checks actually performed — and claim nothing beyond them |

Rubric: 60 implementation + 10 Frictional + 10 GitHub posting + 20 relative quartile.

## Planned files

| File | What it will be | Status |
|---|---|---|
| `creative-brief.md` | Audience, strategy constraints inherited from Assignment 2's positioning, and the prediction with a measurable failure condition | not started |
| `tokens.json` | The design tokens: palette, type scale, spacing scale | not started |
| `generate_specimen.py` | Reads tokens, writes the SVG; validates hex colors, positive sizes, required keys | not started |
| `specimen.svg` | The rendered identity specimen | not started |
| `test_generate_specimen.py` | The failure cases: malformed hex, zero and negative sizes, a missing required token | not started |
| `rationale.md` | The two directions compared, which was chosen, and why — on audience and strategy grounds, not taste | not started |
| `verification.md` | superseded by [`VERIFICATION.md`](VERIFICATION.md) below | — |

## The standard submission files

The course asks every submission to carry the same four records, from [`templates/`](../../../templates/). They are written in this order on purpose: the prediction and the acceptance criteria are fixed *before* there is any output to be impressed by.

| File | What it holds | Status |
|---|---|---|
| [`PREDICTIONS.md`](PREDICTIONS.md) | The expectation and its measurable failure condition, dated before the first render | written, not yet reviewed |
| [`VERIFICATION.md`](VERIFICATION.md) | The acceptance criteria fixed in advance, and the checks as actually run | criteria written; nothing verified |
| [`CONTRIBUTIONS.md`](CONTRIBUTIONS.md) | What the human did, what Claude did, what is still unreviewed | current |
| [`FRICTIONAL.md`](FRICTIONAL.md) | This assignment's process log (the folder-level one is [`../FRICTIONAL.md`](../FRICTIONAL.md)) | current |

## The honest note about scope

The Figma posting asks for design systems *in Figma*, with tokens and Dev Mode handoff. This assignment produces tokens and an SVG specimen from Python — adjacent, not the same thing. It is a real step toward the gap, not a claim to have closed it. Where the gap actually gets closed is the Figma API book in `brutalist-figma-claude/`, and that is a separate, longer piece of work.
