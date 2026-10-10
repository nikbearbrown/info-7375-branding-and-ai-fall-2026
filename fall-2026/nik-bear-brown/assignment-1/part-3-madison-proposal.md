# Part 2 — Madison Framework exploration & project proposal

## Executive summary

**What this is.** Notes from exploring the Madison Framework repository (Humanitariansai/Madison) and the 150–200 word semester project proposal: extend Madison's Intelligence Agents layer with an evidence-first demand-signal agent built on the Lectern pattern.

**Why read it.** It shows how to pick a component honestly — by matching the framework's actual structure (five agent layers, the Popper validation integration) to work already in progress, rather than inventing a project from the README's marketing copy.

## What the repository contains

Madison is an open-source, agent-based AI marketing intelligence framework. Five agent layers collaborate under an orchestration layer: **Intelligence** (market dynamics, reputation monitoring, trend analysis), **Content** (brand-voice-consistent material across channels), **Research** (survey analysis, synthetic personas), **Experience** (AI concierge, customer journeys), and **Performance** (multi-armed bandit optimization, predictive analytics). Key projects include Brand Voice Personalization, Multi-Armed Bandit Optimization, AI Concierge Systems, and MarketMind Research. The Popper integration brings computational skepticism to the framework: evidence-based claims, bias detection, falsification testing, and causal validation of marketing assertions.

## Semester project proposal (150–200 words)

I will extend Madison's Intelligence Agents layer with a demand-signal agent built on the Lectern pattern: it reads public job boards as buying-signal data and reports which companies are staffing education-related roles, with every verdict traceable to the raw board response it came from. The agent adds three things the layer doesn't have today: source-native record keeping (no renamed fields, so any row can be checked against the live posting), a published reject list with reasons (so misses are findable, not silent), and a human gate — it ranks companies by demand evidence and never scores a person's fit or applies anywhere. This is valuable to the framework because marketing intelligence is only as good as its audit trail: Popper's falsification testing needs claims attached to checkable evidence, and most job-market agents hand you a score you're asked to trust. Building it will teach me agent orchestration under a real validation discipline, plus how to design intelligence outputs a skeptic can verify. In real marketing work, the same pattern turns hiring data into partnership timing — knowing which companies are building education teams tells you who to talk to and when.

*Word count: 176.*