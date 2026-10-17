# Assignment 6B, Part 4 — The Pipeline Run (10 pts)

## Executive summary

**What this is.** The Canvas Part 4 write-up for Path B: a run of the Lectern recipe through its four layers, with the phase gates checked and an output report in `logs/reports/`. The run was made on 2026-10-17 by `run_recipe.py`, a new conductor script in this folder.

**Why read it.** Part 4 asks for proof that the recipe executes and not just a document. This is that proof, with its limits stated: it is a **replay** of the responses saved on 2026-09-26, not a live fetch, and **every human gate is still pending**. The script checks what a machine can check and never records an approval.

**What it found.** The machine checks for Gates 1–3 pass: 18 of 18 boards, 3,446 postings, 97 kept, no duplicates, no missing fields, and 57 report claims that each link to a posting in the run. The replay reproduced the 2026-09-26 outputs exactly: the same 97 postings with the same matched words, and a demand report identical apart from its date. It also exposed three problems in the earlier docs and the collector (below).

---

## Fill-in, as the Canvas brief asks

**Run date:** 2026-10-17.

**How it was run:** Claude Code as conductor, running `python3 run_recipe.py --raw ../assignment-3/raw --raw-date 2026-09-26`. The raw responses are the ones the collector saved on 2026-09-26; they are git-ignored, so they exist only on the machine that fetched them. No network was used.

**What happened at each phase gate** (machine check is the script's; the decision column is his):

| Gate | Judgment type | Machine check | What it checked | Human decision |
|---|---|---|---|---|
| 1 Ingest | IJ | PASS | 18 of 18 watched boards had a non-empty saved response | `[TODO: APPROVE]` |
| 2 GIGO | IJ | PASS | 3,446 postings, 97 kept; 0 missing a required field; 0 non-`YYYY-MM-DD` dates; 0 duplicates; 0 kept records without matched words; kept set identical to the committed 2026-09-26 run | `[TODO: APPROVE]` |
| 3 Traceable | TO | PASS | 57 claims in the report, 0 without a link, 0 links absent from the run's postings; 18 ranked companies, 0 board totals that differ | `[TODO: APPROVE]` |
| 4 Shippable | TO | NOT RUN | A human read; the recipe stops here every run | `[TODO: APPROVE]` and `[TODO: REPORT FIELD]` the top-line takeaway |

**Not exercised, and said so in the log:** the trusted-run thresholds (at least 90% of a source-reported total, at least 70% of the previous trusted run), because a replay has neither; the new/gone diff against a previous trusted run, which is still unscripted; and the per-company signal-role counts, which the script did not recompute (it checked links and board totals only).

**Output produced:** `logs/reports/demand-2026-10-17.md`, marked DRAFT, ranking 18 companies with 57 signal roles, each a link to the live posting. Plus `logs/lectern-2026-10-17.json` (the recipe's agent-output contract) and the run block in `logs/reports/run-log.md`.

**What surprised the run:**

1. **The collector's replay only works on the day it ran.** `collect.py --from-raw` looks for files named with *today's* date, so on any other day it finds nothing and reports "every source failed." The script works around it by copying the saved files under today's name. The collector should accept the date. `[TODO: DEV]`
2. **The collector does not write the quality report its docstring promises.** It wrote four files (all-jobs and jobs-of-interest, as JSON and CSV). The dated quality report on file was produced outside it. This matches the gap the design document already recorded. `[TODO: DEV]`
3. **Two facts in the earlier 6B files were wrong about the 2026-09-26 run, and are fixed in this folder:** that run fetched **197** Canva postings, not 248 (the 248 figure appears in the 2026-09-19 sweep notes), and **Anthropic is on Greenhouse**, not Ashby. The Conductor Brief still ties 248 to Canva (`../the-conductor-brief/conductor-brief.md`, Part 3); it is not edited here. The "Figma 151" drift example was left alone: it is consistent with the 160-posting snapshot minus 32 gone plus 23 new that Assignment 4 reports, but that run's files are not in this repo, so it is unverified here.
4. **`brand_config.json` was a single minified line.** It is now indented; the data is unchanged (checked by parsing both).

**Did the recipe change because of the run?** Yes, in two places: the Canva figure in Step 1.3 and the open-TODO note that Gates 1–3 and the agent-output JSON are now scripted.

## Negative test

Run with a wrong `--raw-date`, the script reports Gate 1 FAIL and Gate 2 FAIL and stops, instead of passing quietly (run into a scratch folder, not this one).

## To make this a live run

```
python3 ../build-your-data-pipeline/collect.py --out <fresh folder>      # fetches all 18 boards live
python3 run_recipe.py --raw <fresh folder>/raw --raw-date <today>
```

The first command hits eighteen public job-board APIs (SmartRecruiters needs one extra call per posting, about three and a half minutes for Canva). It was not run for this write-up. `[TODO: APPROVE]` He decides whether a live run is wanted before the submission.

## What the Canvas brief still needs from him

1. The decision at each gate, in his words, under the table above.
2. A screenshot of `logs/reports/` after the run.
3. The PDF rebuilt with this section as an appendix (see the README: the existing PDF predates it).
