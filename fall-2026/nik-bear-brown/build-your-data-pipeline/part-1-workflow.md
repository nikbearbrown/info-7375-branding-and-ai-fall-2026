# Assignment 3, Part 1 — Working data collection workflow (worked example)

## Executive summary

**What this is.** The Part 1 deliverable for "Collect Data for Your Madison Agent": the working data pipeline behind the demand-signal agent — three public data sources, the collection steps, what was actually collected, and how to re-run it.

**Why read it.** It follows the assignment's own rules: quality over quantity (97 kept of 3,446, every one checkable), collect once and reuse (the dated run files are the dataset; nothing is re-fetched), and Tier-1-style sources only — three public JSON feeds, no logins, no keys.

**What was collected.** The 2026-09-26 final pass: **3,446 postings from 18 boards across three applicant-tracking systems, 97 kept.** Raw and kept data: `all-jobs-2026-09-26.json` / `.csv`, `jobs-of-interest-2026-09-26.json` / `.csv`.

---

## The three data sources

| # | Source | Feed | Companies | Records (2026-09-26) |
|---|---|---|---|---|
| 1 | **Greenhouse** | `boards-api.greenhouse.io/v1/boards/<slug>/jobs?content=true` — one call, full ad text | Figma, Webflow, Miro, Anthropic, and others | majority of the 3,446 |
| 2 | **Ashby** | `api.ashbyhq.com/posting-api/job-board/<name>` — one call; names URL-encoded (`Jasper AI` → `Jasper%20AI`) | Writer, Notion, Jasper, OpenAI, and others | — |
| 3 | **SmartRecruiters** | `api.smartrecruiters.com/v1/companies/<Company>/postings` — paged, 100 at a time, **no ad text**; one extra call per posting for the description | Canva | 248 postings; 251 requests; 3m38s |

All three are public, keyless JSON feeds — the assignment's Tier 1 in spirit. No logins, no passwords, nothing to get cut off from.

## The pipeline (what runs)

`collect.py`, six steps, stdlib Python only:

1. **Fetch.** For each board in `sources.json`, GET the public feed. Save the raw response untouched, dated, under `raw/`.
2. **Normalize (without renaming).** Kept records carry the source's own field names (`id`, `title`, `absolute_url` for Greenhouse) — never renamed, so any row checks against the live posting.
3. **Classify.** Title rule (role words: advocate, educator, enablement, …), topic-words rule, teaching-materials rule. Every kept posting records which rule fired and which words matched, under one separate `matched` key.
4. **Reject with reasons.** Every rejected posting is written to the all-jobs file *with its reject reason* — misses are findable, not silent.
5. **Dedupe.** Collapse on source + native id.
6. **Write.** `all-jobs-YYYY-MM-DD.json` + `.csv` (everything), `jobs-of-interest-YYYY-MM-DD.json` + `.csv` (the kept).

**Failure handling (excellence: craft).** A source that times out or returns nothing is logged as unavailable and the other two keep going. A board that changes shape fails loudly — the reader asserts field positions instead of returning blank titles. One polite request per second; nothing hammers a host.

## The n8n form

The production pipeline is `collect.py`; its n8n equivalent is the four-node workflow from Assignment 2, Part 4: **Schedule Trigger** (weekly) → **HTTP Request** (the ATS feed) → **Code** (the keyword/title rules) → **Google Sheets** (the digest). Same logic, same schema, same human gate at the end.

## Repeatability

Prerequisites: Python 3, nothing to install (stdlib only). Run: `python3 collect.py`. Outputs are dated; re-running never overwrites — a new date makes a new file pair, which is what makes "collect once, reuse forever" true. The 2026-09-26 files in this folder are the dataset everything downstream works from.