# Assignment 3 — Collect Data for Your Madison Agent

## Executive summary

**What it does.** `collect.py` fetches every open job posting from three different applicant-tracking systems, keeps the ones about teaching — education, workshops, curriculum, developer advocacy — and writes them to one file of jobs worth my time.

Three steps, once a day:
1. **Download.** For each company on the list, fetch its public job-board JSON and save the response untouched, dated. Greenhouse (`boards-api.greenhouse.io`), Ashby (`api.ashbyhq.com`), SmartRecruiters (`api.smartrecruiters.com`) — three separate APIs with three different shapes and no key required.
2. **Filter.** Scan each posting's title for role words (`advocate, educator, education, enablement, evangelist, developer relations, community, instructor, trainer, curriculum`) and its text for topic words (`university, campus, student, workshop, educate, teach`) and flexible-terms phrases (`part-time, contract role, temporary, fixed-term, freelance, summer, hourly`).
3. **Write.** Save the matches to `jobs-of-interest.json` — **and to `jobs-of-interest.csv`** for the spreadsheet the assignment wants.

**The field names are the source's own.** A kept record carries Greenhouse's `id`, `title`, `absolute_url`, `location`, `content`, `first_published`, `updated_at`, `departments` exactly as Greenhouse wrote them — not renamed, not reshaped. Anything the tool works out for itself goes under one clearly separate key (`matched`), so a reader can always tell what the company said from what my script decided. Ashby's and SmartRecruiters' records keep *their* own names too, which is why the file also records which source each record came from rather than pretending all three are the same.

**What it refuses.** A posting with no title, no link, or no date is not written out — those three fields are what make a record usable, and a record missing them is filler. Duplicates (the same job posted to two boards, or the same board fetched twice in a day) collapse on source + id. A source that times out or returns nothing is logged as unavailable and the other two keep going.

**What it is for.** Figma has no part-time advocate role today. Neither does Writer, Notion, Webflow, Canva, Miro, or Jasper. Checking that by hand, one careers page at a time, costs an hour a week and is the first thing to get skipped. This runs in six steps and tells me only what changed.

**What it does not do.** It never applies to anything, never contacts anyone, and makes no judgment about fit — it matches words and hands me a list. Which of these is worth a day of my life stays my decision.

**Status: not built.** The folder holds the plan, the prediction ([`PREDICTIONS.md`](PREDICTIONS.md)) and the acceptance criteria ([`VERIFICATION.md`](VERIFICATION.md)), all written before any output exists. What *does* exist is the working parts this is assembled from: `greenhouse-watch` in the Reallocation Engine already reads all three ATSs, and [`../figma/find_roles.py`](../figma/find_roles.py) already runs the keyword scan on a saved Figma board.

---

## Which assignment this is

The live Assignment 3 is **"Build Your Data Pipeline — Collect Data for Your Madison Agent"** (due October 2, 2026): an n8n workflow, 3+ data sources, 50–300 clean records, plus documentation, a demo, and quality numbers.

⚠️ **The brief in this repo says something else.** [`assignments/fall-2026/assignment-03.md`](../../../assignments/fall-2026/assignment-03.md) is "Visual identity system" — design tokens and an SVG specimen. That is the same mismatch Assignment 2 had. This folder follows the live assignment; the repo brief needs replacing.

## The Madison project this feeds

**Problem:** I am looking for advocate, educator, or education-adjacent work I can do while remaining a professor — remote, part-time, contract, or workshop-based. The companies whose tools I teach are the obvious place to look, and their job boards are public. Nobody is going to email me when a part-time Developer Educator opens at Webflow.

**From Assignment 2:** the dream job is a Figma Designer Advocate posting, and the gap analysis is [`../assignment-2/`](../assignment-2/). The seven-company sweep is in [`../advocate/`](../advocate/).

## Requirements checklist

Scored against the live brief. **Nothing is checked off yet** — this is the target, not a claim.

### Part 1 — Working data collection workflow (40 pts)

| Requirement | Plan | Done |
|---|---|---|
| Collects data that directly addresses the Assignment 2 problem | Job postings from the companies whose tools I teach, filtered to advocate/education roles — the exact question Assignment 2 asked | ☐ |
| **At least 3 different data sources** | **Greenhouse API · Ashby API · SmartRecruiters API** — three separate services, three different JSON shapes, three normalisers. *See the note below.* | ☐ |
| Saves in an organized format | `jobs-of-interest.csv` (spreadsheet) and `jobs-of-interest.json` (data file), plus the dated raw responses | ☐ |
| Runs on my computer and is repeatable | One command; a state file makes the second run report only what is new | ☐ |
| 50–300 clean, relevant records | Target **150–300** — reached by widening the company list, not by loosening the filter | ☐ |
| Workflow runs without major errors (15) | A dead source logs "unavailable" and the run continues | ☐ |
| Data relevant to the problem (15) | Every kept record carries the words that matched, so relevance is checkable rather than asserted | ☐ |
| Usable, organized format (10) | Same columns in every row, dates as `YYYY-MM-DD`, source named per record | ☐ |

### Part 2 — Data documentation & demo (24 pts)

| Requirement | Plan | Done |
|---|---|---|
| Data inventory, template followed (8) | `DATA-INVENTORY.md`, one block per source with type, amount, purpose, method, quality, then the statistics block | ☐ |
| Setup guide (8) | `SETUP.md`: install, run, what needs installing first, common errors. **No API keys needed for any of the three** — worth saying explicitly, since that is why these sources were chosen | ☐ |
| Demo (8) | Screenshot walkthrough PDF, 5–8 annotated shots: workflow overview, key node configs, the run, sample output | ☐ |

### Part 3 — Data quality (16 pts)

| Requirement | Plan | Done |
|---|---|---|
| 80%+ records complete (8) | A record without title, link, or date is never written — so completeness on those three is 100% by construction, and the **real** number to report is completeness on the optional fields | ☐ |
| Essential info in every record (8) | title, date, source enforced at write time | ☐ |
| Duplicates removed | Collapse on source + posting id | ☐ |
| Consistent dates | All three sources' dates converted to `YYYY-MM-DD`; the original string kept alongside | ☐ |
| Quality numbers documented | Counted by the script, not by hand: fetched, kept, rejected and why, duplicates collapsed, per-field completeness | ☐ |

### Excellence (20 pts, comparative)

| What they look for | What I intend |
|---|---|
| Clearly structured, easy to read (5) | Every column means one thing; source's own field names preserved so a reader can check any row against the live posting |
| Checks that catch mistakes (3) | Validators: non-empty title, parseable date, well-formed URL, expected record count asserted against what the API said it had |
| Quality numbers documented in detail (2) | A counts table the script writes, including rejects by reason — not just a pass rate |
| Handles problems without crashing (3) | Per-source try/except; unavailable source logged and skipped; the state file is never written on a failed run |
| Sources connected coherently (2) | Not three bolted-on feeds — three ATSs normalised to one record shape, which is the actual engineering problem |
| Thorough, professional documentation (3) | Executive summary first, annotated screenshots, clean layout |
| A peer could replicate it (2) | No keys, public endpoints, one command, the dated raw responses shipped so anyone can re-derive the filtered file |

### Submission

| Item | File | Done |
|---|---|---|
| n8n workflow export | `Brown_Nik_A3_Workflow.json` | ☐ |
| Documentation PDF | inventory + setup + quality numbers | ☐ |
| Data file | `jobs-of-interest.csv` | ☐ |
| Demo | screenshot walkthrough PDF | ☐ |

## On "three data sources" — the thing worth deciding

The brief says **at least 3 different data sources.** Two readings:

- **Three companies on one API** — Figma, Webflow, Miro, all Greenhouse. Simplest, but it is one source three times, and a grader could fairly say so.
- **Three different APIs** — Greenhouse, Ashby, SmartRecruiters. Genuinely three services with three different JSON shapes, three normalisers, three failure modes. **This is the stronger answer, and the work is already done** in the Reallocation Engine's `greenhouse-watch`.

Going with the second. Companies get added *within* each source to reach the record count:

| Source | Companies | Postings seen 2026-09-19 |
|---|---|---:|
| Greenhouse | Figma, Webflow, Miro (`realtimeboardglobal`) | 209 |
| Ashby | Notion, Writer, Jasper AI | 186 |
| SmartRecruiters | Canva | 248 |

That is 643 postings across three sources, of which the advocate/education filter kept a handful. **643 raw is more than the assignment wants and the filtered set is fewer than 50** — so the records that get shipped are the filtered set *widened by adding companies*, which is the honest way to reach 150–300: more boards, same filter. Companies to add are AI and developer-tool firms that actually hire advocates. `[TODO: DEFINE]` the list.

**A fourth source is available if 150 records proves hard from ATSs alone:** RSS feeds from company engineering and careers blogs, which are Tier 1 in the brief and need no key.

## Planned files

| File | What it will be | Status |
|---|---|---|
| `collect.py` | Fetch → filter → write, one command, three sources | not started |
| `sources.json` | The company list per ATS, so adding a board is a data change not a code change | not started |
| `keywords.json` | Role, topic, and flexible-terms word lists, in one editable place | not started |
| `raw/<source>-<company>-<date>.json` | Each response exactly as the API sent it | not started |
| `jobs-of-interest.json` · `.csv` | The kept records, source field names preserved | not started |
| `quality-report.md` | Counts the script wrote: fetched, kept, rejected by reason, duplicates, completeness | not started |
| `DATA-INVENTORY.md` | The brief's inventory template, filled from real counts | not started |
| `SETUP.md` | Install, run, common errors | not started |
| `workflow.json` | The n8n export: Schedule → 3× HTTP Request → Code (filter) → Write File | not started |
| `test_collect.py` | Offline tests against saved responses: empty board, dead source, missing title, duplicate id, bad date | not started |

## The design document

[`SDD.md`](SDD.md) — the full Software Design Document for **Lectern**, the collector described above, generated by Gru in silent mode (`/g1 silent`) on 2026-09-26. Sixteen sections: problem summary, four architecture principles with a collision test, the three flows, eight needs mapped to components, six components with edge cases, the three API contracts with risk ratings, the data and domain models with six invariants, the CLI and output contracts, three sequence diagrams, a 21-component priority list with an MVS statement, ten out-of-scope decisions, infrastructure, an eight-row risk register, and eight open questions.

Its appendix states what silent mode skipped: no `/v0` gate, no phase gates, no pushback — so the V0 sentence is Gru's, not mine, and the open company list (Q1) would have stopped intake in interactive mode.

**Two findings from writing it.** The P1/CSV collision (source field names versus one header row) forced an explicit decision: the JSON is the evidence, the CSV is declared derived. And exactly one invariant — that a kept record's `original` stays byte-identical to the raw response — has no runtime enforcement, which is now risk R4 with a test instead of a shrug.

## The standard submission files

| File | What it holds | Status |
|---|---|---|
| [`PREDICTIONS.md`](PREDICTIONS.md) | The expectation and its measurable failure condition, dated before the first run | needs rewriting for this assignment |
| [`VERIFICATION.md`](VERIFICATION.md) | Acceptance criteria fixed in advance, and the checks as actually run | needs rewriting for this assignment |
| [`CONTRIBUTIONS.md`](CONTRIBUTIONS.md) | What the human did, what Claude did, what is still unreviewed | current |
| [`FRICTIONAL.md`](FRICTIONAL.md) | This assignment's process log (folder-level: [`../FRICTIONAL.md`](../FRICTIONAL.md)) | current |

## The honest note about scope

The tool matches words. A posting that says "we love teaching" in its culture blurb will match; a Developer Educator role that never uses any of my keywords will be missed. Both errors are real and neither is reported as accuracy. **No number this produces is a measure of how good a job is** — it produces a shorter list to read, and I do the reading.
