# Assignment 3, Part 3 — Data quality (worked example)

## Executive summary

**What this is.** The Part 3 quality checklist, answered with the real numbers from the 2026-09-26 run and its two audits — plus what was done about what the audits found.

**Why read it.** "Clean data" here isn't asserted; it was measured twice, by two different audits, and both audits found real problems that got fixed. The numbers below are the after picture, with the before picture stated honestly.

---

## Quality checklist

- [x] **80%+ of records complete.** 3,446 / 3,446 records carry title, URL, date, location, and department — 100%. A posting missing any of the three critical fields (title, link, date) is not written out at all.
- [x] **Essential information present in every record.** Title, date, and source are asserted per record by the reader; the run's counts table confirms 3,446/3,446.
- [x] **Duplicates removed.** 0 duplicates in the final pass — collapsed on source + native job id (the same job on two boards, or one board fetched twice, counts once).
- [x] **Dates in a standard format.** `first_published` / `updated_at` normalized to YYYY-MM-DD throughout; the raw source strings are preserved in the raw files, not in the working data.
- [x] **Relevant to the problem.** 97 kept of 3,446 (2.8%) — and relevance was *audited*, not assumed (see below).

## Quality numbers documented

| Measure | Result | Evidence in this folder |
|---|---|---|
| Records fetched | 3,446 | `all-jobs-2026-09-26.json` |
| Records complete (title/URL/date/location/department) | 3,446 (100%) | `quality-report-2026-09-26.md` |
| Kept as education-related | 97 (2.8%) | `jobs-of-interest-2026-09-26.json` |
| Duplicates | 0 | quality report |
| Title audit: false positives found | 45, fixed | `title-audit-2026-09-26.md` |
| Title audit: candidate misses | 2, under review | title audit |
| Reject audit sample | 100 random + 63 closest calls | `reject-audit-2026-09-26.md` |
| Teaching-materials rule, v1 precision | ~1 in 10 (101 extra kept) → cut to 5 kept, 4 right | quality report |

## What the audits found (and what changed)

**The title audit** read kept postings by job function and found 45 false positives — the largest group was 15 Anthropic *Applied AI Architects* kept on the phrase *technical content* plus *our users*, and four IT Support Engineers kept on *how-to guides*. Nine phrase groups were cut from the materials rule; it now contributes 5 postings, 4 of them right. Two candidate misses are still open, including Replit's *Learning Experiences Creator* — missed on the single word *experiences* vs. *designer*.

**The reject audit** sampled 100 random rejects plus the 63 closest calls (the ones the rules nearly kept) and re-judged them by hand. Its standing finding: 13 sales-enablement postings first called errors are *not* errors — building curriculum and running training for a company's own staff is the work, and `SALES_ENABLEMENT` now expects *keep*.

## Built-in checks (excellence: data quality & care)

- The reader **asserts field positions** per ATS and fails loudly on layout change — a silent schema drift can't produce blank titles.
- The **reject list ships with reasons** — every one of the 3,349 rejects says why, so a miss is a searchable row, not a suspicion.
- **Native IDs are never renamed** — any kept posting checks against the live board in one click.
- Dated files never overwrite — a re-run is a new file pair, so quality numbers are always recomputable from the raw.

## What "standing out" looks like here

Not the 3,446 — that's the haystack. What stands out is the 97: every kept posting names the rule that fired and the words that matched, every reject names its reason, and two audits measured the filter instead of trusting it. Open the kept file and you can read *why* each row is there; open the audit and you can read what was wrong. That is the whole assignment.