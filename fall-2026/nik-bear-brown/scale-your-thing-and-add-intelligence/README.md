# Assignment 4 — "Scale Your Thing & Add Intelligence" (worked example)

## Executive summary

**What this is.** Professor Bear's worked example for Assignment 4 of INFO 7375 Branding and AI (Fall 2026): the intelligence layer on top of Assignment 3's data pipeline, the usable outputs it produces, honest scale numbers, and the interview-ready package — in markdown instead of a Figma board.

**Why read it.** Assignment 3 collected the data; this one makes it smart and proves it. The intelligence here isn't a chatbot bolted on — it's the classifier that decides keep/reject with reasons, the demand ranker that turns postings into company rankings, and the audit loop that measured the filter and fixed it. Every claim below traces to a file in `assignment-3/` or `lectern/`.

**What changed from Assignment 3.** A3 fetched and saved. A4 classifies (three rules, every verdict explained), ranks (five demand kinds per company), diffs over time (the Figma 23-new/32-gone), and measures itself (two audits). The outputs are human-readable reports, not JSON dumps.

## Files

| File | Assignment part | Points |
|---|---|---|
| `part-1-intelligence.md` | Part 1 — Add real intelligence + error handling | 20 |
| `part-2-outputs.md` | Part 2 — Complete the loop: end-to-end + output gallery | 25 |
| `part-3-scale.md` | Part 3 — Prove it can scale | 20 |
| `part-4-package.md` | Part 4 — Professional package | 15 |
| | Excellence | 20 |

**Status.** Drafted 2026-10-10 by Muse from the project record. Professor Bear has not reviewed this draft.