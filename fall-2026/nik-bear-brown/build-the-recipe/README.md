# Assignment 6B — Build the Recipe (Path B)

**Due:** October 23, 2026, 11:59 PM · **Points:** 100
**Canvas submissions:** `LastName_FirstName_A5B_BuildTheRecipe.pdf` +
`brand_config.json` + `recipe_[LastName].md`

## Status (2026-10-11; Part 4 and corrections added 2026-10-17)

| Piece | State |
|---|---|
| `brand_config.json` | ✅ Valid JSON, all fields from the Conductor Brief, judgment types named |
| `data/verified/` | ✅ 3 sources: greenhouse (53), ashby (34), smartrecruiters (10) + README |
| `recipe_brown.md` | ✅ Four layers, typed phase gates, typed TODOs, standardization appendix |
| Part 4 /snickerdoodle | ✅ Manual audit documented; **Gru `/claude` confirmation needs Bear** |
| Part 4 — the pipeline run | ✅ `part-4-pipeline-run.md`; run by `run_recipe.py` on 2026-10-17 as a **replay** of the 2026-09-26 responses; Gates 1–3 machine checks PASS; every human decision still **pending** |
| `logs/` | ✅ `logs/reports/demand-2026-10-17.md` (DRAFT), `logs/reports/run-log.md`, `logs/lectern-2026-10-17.json` |
| PDF | ⚠️ `Brown_Nik_A5B_BuildTheRecipe.pdf` predates the run and the corrections listed in `part-4-pipeline-run.md`; rebuild with `part-4-pipeline-run.md` as an appendix. Canvas names the file `…_A6B_…`; `make_pdf.py` hard-codes a `/tmp` path and needs `fpdf2`. |

## Files

- `brand_config.json` — machine-readable Conductor Brief (submit separately).
- `recipe_brown.md` — the conductor's recipe (submit separately).
- `data/verified/{greenhouse,ashby,smartrecruiters}/` — verified records + README.
- `part-4-snickerdoodle.md` — pipeline description, audit TODOs, resolutions.
- `run_recipe.py` — the conductor script: replays saved responses, runs Gates 1–3 as machine checks, writes the report and run log, stops at Gate 4. Never records an approval.
- `part-4-pipeline-run.md` — the Canvas Part 4 write-up of that run.
- `logs/` — the run's outputs.
- `make_pdf.py` — PDF build script.

## Honest limits (what needs Bear)

1. **SmartRecruiters is thin** — 10 verified records vs the 25-record bar.
   TODO: DATA SOURCE in the recipe (wire more boards or accept two sources).
2. **Gru steps** — `/snickerdoodle` and `/claude` need Gru; the audit here is
   manual and labeled as such. No confirmation is fabricated.
3. **Two TODOs need time** — trusted-run thresholds want two more weekly runs.
4. Nothing here invents data: every verified record traces to the real
   2026-09-26 run; rejections are documented, not hidden.
