# Assignment 5B, Part 4 — The /snickerdoodle Run (10 pts)

## Status: documented as a manual audit — Gru step needs Bear

`/snickerdoodle` is a Gru command and the `/claude` confirmation happens in
Gru; neither is available in this environment. What follows is the honest
equivalent: the pipeline description that would be fed to `/snickerdoodle`,
plus a manual audit of the recipe against the standardization rules
(`madison/recipes/cowork_recipe_standardize.md`, read 2026-10-11) that
produced typed TODOs exactly the way the prompt factory would. Nothing is
presented as a Gru run that wasn't one — the `/claude` confirmation is an
explicit TODO for Bear.

## Pipeline description for /snickerdoodle

> Lectern is a weekly teaching-demand pipeline. It fetches job postings from
> three public, keyless ATS feeds (Greenhouse, Ashby, SmartRecruiters — 18
> watched boards), validates every record (title, URL, date, location,
> department; deduplicated on source + native ID), keeps the postings that
> are evidence of teaching interest using a tuned rule set with an audit loop,
> and produces a company demand report with every claim traceable to a raw
> posting in two clicks. The user is an independent AI-education consultant
> deciding which companies to approach about unposted work. Failure handling:
> untrusted runs freeze the closed-job logic, unlinked claims are hard stops,
> and the final report never ships without human approval.

## TODO items from the audit

| # | Type | Item |
|---|------|------|
| 1 | TODO: DATA SOURCE | Only one SmartRecruiters board (Canva) wired; 10 verified records, below the 25-record bar. |
| 2 | TODO: DEFINE | Trusted-run thresholds (≥90% of source-reported total, ≥70% of previous trusted run) set from a single run; confirm after two more weekly runs. |
| 3 | TODO: DEV | New/gone native-ID diff runs by hand; script it. |
| 4 | TODO: APPROVE | Final demand report requires human approval every run (Phase Gate 4). |
| 5 | TODO: REPORT FIELD | "What's new this month" needs a human-written top-line takeaway label. |
| 6 | TODO: DEFINE | "Expected board count" per source is currently the previous run's snapshot; define the canonical board list in `sources.json` so drift is measured, not guessed. (Found in audit — added.) |
| 7 | TODO: DEV | Agent output JSON (`logs/lectern-[DATE].json`) per the output contract is specified but not yet implemented. (Found in audit — added.) |

## TODOs resolved before this submission

- **#6 (DEFINE):** RESOLVED — the canonical board list lives in the existing
  `sources.json` (18 boards, committed in `build-your-data-pipeline/`);
  the recipe now names it as the drift reference instead of "last week's number."
- **#7 (DEV):** RESOLVED as specified-not-built — the output contract in the
  recipe appendix defines the exact fields; implementation is a flagged DEV
  task, not a vague intention.
- **Earlier resolutions carried in:** the collector, the rule set, the audit
  loop, and the two-click trace test were resolved in Assignments 3–4 and are
  marked RESOLVED in the recipe rather than re-audited.

## TODOs still open and why

- **#1 (DATA SOURCE):** blocked on wiring more SmartRecruiters boards (needs
  board discovery work) or an explicit decision to run a two-source recipe.
- **#2 (DEFINE):** blocked on time — needs two more weekly runs of data.
- **#3 (DEV):** blocked on implementation — the diff logic is specified, the
  script isn't written.
- **#4 (APPROVE) / #5 (REPORT FIELD):** open by design — these are per-run
  human judgments, not pre-closable items.

## Gru /claude confirmation

TODO for Bear: paste the recipe into Gru, run `/snickerdoodle` with the
pipeline description above, and run `/claude` once TODOs #1–#3 are closed.
No confirmation is claimed here — the recipe is audit-complete and
rules-conformant to manual inspection, pending Gru's own verdict.
