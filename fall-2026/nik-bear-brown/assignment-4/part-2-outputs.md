# Assignment 4, Part 2 — Complete the loop: show your output (worked example)

## Executive summary

**What this is.** Proof the pipeline produces things a human can use: one end-to-end run documented input → processing → output → proof, plus a gallery of 15 real artifacts.

**Why read it.** The brief's test is "could a non-technical person use this?" Every output below is a file a person can open and read — a ranked report, a spreadsheet, an audit — not JSON in a console. Nothing here is "it would create X."

---

## Complete workflow run

**Input data:**
- 3,446 postings from 18 boards across three ATS APIs (Greenhouse, Ashby, SmartRecruiters), fetched 2026-09-26, raw responses saved untouched

**Processing:**
- Classified by three rules (title role-word, topic words, teaching-materials) → 97 kept, 3,349 rejected with reasons
- Duplicates collapsed on source + native id → 0 remaining
- Demand ranker scored all 18 companies on five signal kinds → ranked table, 57 signal roles
- Title audit measured the filter → 45 false positives found and fixed; reject audit re-judged 163 borderline calls

**Final output:**
- `company-demand-2026-09-26.md` — the one-page ranked demand report
- `jobs-of-interest-2026-09-26.csv` — the 97 kept as a spreadsheet a human can sort and filter
- `quality-report-2026-09-26.md` — counts, completeness, and what the audits changed
- `title-audit-2026-09-26.md` + `reject-audit-2026-09-26.md` — the measurement, published

**Proof output exists:** all four files are in `assignment-3/` in this repo, committed and readable on GitHub. Open the CSV in any spreadsheet app — no n8n, no JSON parsing, no technical skill required.

## Output gallery

### 1. The demand report
**Produced:** `company-demand-2026-09-26.md` — 18 companies ranked on five demand kinds, 57 signal roles, with a plain-language section on why Google's absence is a measurement gap, not a finding.
**Where:** `assignment-3/` in this repo.
**Quality check:** a non-technical reader gets the answer ("which companies are hiring for education work?") on page one.

### 2. The kept-postings spreadsheet
**Produced:** `jobs-of-interest-2026-09-26.csv` — 97 rows: company, title, location, URL, rule that fired, words that matched.
**Where:** `assignment-3/`.
**Quality check:** opens in Excel/Sheets; every row links to the live posting.

### 3. The quality report
**Produced:** `quality-report-2026-09-26.md` — counts (3,446 fetched, 97 kept, 0 duplicates, 100% complete), how the 97 were kept, what the audits changed.
**Where:** `assignment-3/`.

### 4. The title audit
**Produced:** `title-audit-2026-09-26.md` — kept postings read by job function; 45 false positives named, 2 candidate misses flagged.
**Where:** `assignment-3/`.

### 5. The reject audit
**Produced:** `reject-audit-2026-09-26.md` — 100 random rejects + 63 closest calls re-judged by hand; the sales-enablement correction.
**Where:** `assignment-3/`.

### 6. The Figma time-diff
**Produced:** 23 new native IDs (including Designer Advocate, Berlin) and 32 gone, 2026-09-23 → 2026-10-08, computed from the snapshot and the run file.
**Where:** verified in `lectern-state-check.md`; inputs are `greenhouse-watch-demo/snapshots/figma-2026-09-23.json` and `lectern/runs/2026-10-08/all-jobs-2026-10-08.json`.
**Quality check:** recomputable by anyone from the two files.

### 7. The six-board run
**Produced:** `lectern/runs/2026-10-08/` — 1,891 postings, 58 kept, JSON + CSV.
**Where:** the Computational Skepticism master folder (canonical for Lectern).

### 8. The job-search recipe
**Produced:** `advocate/README.md` — the "how to run your own search" document: method, scheme, the human override.
**Where:** the master folder's shared job-search files.

### 9. The sources watch list
**Produced:** `sources.json` — 18 boards, three ATSs, five unreachable companies with reasons.
**Where:** `assignment-3/` and `lectern/`.

### 10. The keyword rules
**Produced:** `keywords.json` + `title_families.json` — the classifier's actual rules, versioned.
**Where:** `assignment-3/` and `lectern/`.

### 11. The ATS field guide
**Produced:** `ATS.md` — which system each company uses, how to spot it, the feed URL pattern.
**Where:** `assignment-3/` and `lectern/`.

### 12. The software design document
**Produced:** `SDD-job-search-project.md` — sixteen sections on what was built, plus a seventeenth: where the design and the built code disagree.
**Where:** `assignment-3/` and the master folder.

### 13. The demand-report script
**Produced:** `demand_report.py` — the ranker itself, runnable.
**Where:** `assignment-3/` and `lectern/`.

### 14. The audit scripts
**Produced:** `audit_titles.py`, `audit_rejects.py` — the measurement tools, runnable.
**Where:** `assignment-3/` and `lectern/`.

### 15. The collector
**Produced:** `collect.py` — the six-step pipeline, stdlib only.
**Where:** `assignment-3/` and `lectern/`.