# Assignment 3, Part 2 — Data inventory, setup guide, and demo plan (worked example)

## Executive summary

**What this is.** The Part 2 deliverables: the data inventory in the assignment's template, the setup guide, and the demo plan — all describing the real 2026-09-26 collection run whose files sit in this folder.

**Why read it.** A peer could replicate the run from the setup guide alone, and every number in the inventory traces to a file in this folder. The demo plan is honest about format: the Canvas submission is video or annotated screenshots; the repo holds everything the demo would show.

---

## Data inventory

## Project: Lectern — the demand-signal agent
## Problem: Nobody can see where education hiring demand is forming; the agent reads public job boards as demand evidence so advocates build the right material and consultants pitch with timing.

### Data collected

**Source 1: Greenhouse public boards API**
- Type: Full job postings (title, ad text, location, department, dates) — one call per board, complete ad text inline
- Amount: the majority of the 3,446 postings (Figma, Webflow, Miro, Anthropic, and others)
- Purpose: the primary demand signal — Greenhouse boards carry the design-tool companies at the center of the search
- Collection method: `GET boards-api.greenhouse.io/v1/boards/<slug>/jobs?content=true` via `collect.py`; raw response saved untouched and dated
- Quality: every record carries title, URL, date, location, department — the required fields are asserted, not assumed

**Source 2: Ashby posting API**
- Type: Full job postings via the public posting API (board names URL-encoded)
- Amount: part of the 3,446 (Writer, Notion, Jasper, OpenAI, and others)
- Purpose: covers the AI-lab companies — the other half of the demand picture
- Collection method: `GET api.ashbyhq.com/posting-api/job-board/<name>` via `collect.py`; raw response saved untouched and dated
- Quality: same required-field assertions as Source 1

**Source 3: SmartRecruiters public postings API**
- Type: Posting listings (title, location, type) — **no ad text**; one extra call per posting fetches the description
- Amount: 248 postings (Canva); 251 requests; 3 minutes 38 seconds
- Purpose: Canva is unreachable any other way — the one extra call per posting is the documented cost of the third source
- Collection method: paged `GET api.smartrecruiters.com/v1/companies/<Company>/postings` (100/page) via `collect.py`; raw responses saved untouched and dated
- Quality: same required-field assertions; the paging loop verifies no duplicates across pages

### Statistics

- Total records: **3,446**
- Clean records: **3,446 / 3,446** complete on (title, URL, date, location, department) — 100%
- Kept as education-related: **97** (2.8%)
- Duplicates: **0** (collapsed on source + native id)
- Sources: **3** (three ATS APIs, 18 boards)
- Ready for: Assignment 4 — the demand digest, the company ranking, and the Conductor Brief's evidence base

## Setup guide

**Install first:** Python 3. Nothing else — `collect.py` is stdlib only. (The n8n form needs `npm install -g n8n` and a browser at `localhost:5678`.)

**Steps:**
1. Clone the repo; `cd` into this folder.
2. Check `sources.json` — the 18 boards across the three ATSs.
3. Run `python3 collect.py`.
4. Find the dated outputs: `all-jobs-YYYY-MM-DD.json` / `.csv`, `jobs-of-interest-YYYY-MM-DD.json` / `.csv`.

**Passwords / access codes:** none. All three feeds are public and keyless — that is the point of the source choice.

**Common errors and fixes:**
- *A board returns nothing / times out* → logged as unavailable; the other two sources keep going. Re-run later; dated files never overwrite.
- *A board changes its feed shape* → the reader asserts field positions and fails loudly instead of writing blank titles. Fix the reader, don't patch the data.
- *SmartRecruiters is slow* → expected: ~250 requests for one board at one request per second. Let it run.
- *Zero kept postings* → check `keywords.json` version against the run file header before assuming the market went quiet.

## Demo plan (Option B: screenshot walkthrough)

The Canvas demo is 5–8 annotated screenshots; this is what they show, in order:

1. **Workflow overview** — the six pipeline steps, one diagram.
2. **Source 1 config** — the Greenhouse HTTP call: URL, the `?content=true` parameter, the raw-save step.
3. **Sources 2 & 3 configs** — the Ashby board-name encoding; the SmartRecruiters paging loop and per-posting description call.
4. **The classifier** — the three rules and the `matched` key, with one kept posting highlighted.
5. **A run in progress** — terminal output: boards fetched, counts ticking up.
6. **Sample output: kept** — three rows of `jobs-of-interest-2026-09-26.csv`: title, company, rule that fired.
7. **Sample output: rejects** — three rows of the all-jobs file showing reject reasons (misses are findable).
8. **Quality numbers** — the counts table and the audit findings, one slide.

Each screenshot gets a caption and arrows on the fields that matter. The video option (3 min max) would walk the same eight beats on camera.