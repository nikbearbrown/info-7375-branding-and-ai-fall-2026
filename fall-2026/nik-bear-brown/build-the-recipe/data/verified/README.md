# data/verified/ — README

Verified inputs for the Lectern recipe (Assignment 5B, Path B). Every record
below passed the GIGO gate from Conductor Brief Part 3. No raw or unvalidated
records live here.

## Folders

- `greenhouse/` — **53 records** | 2026-09-26 | Kept postings from Greenhouse-hosted boards (design-tool companies). File: `verified-2026-09-26.json`.
- `ashby/` — **34 records** | 2026-09-26 | Kept postings from Ashby-hosted boards (AI labs: OpenAI, Anthropic, Writer, Notion, others). File: `verified-2026-09-26.json`.
- `smartrecruiters/` — **10 records** | 2026-09-26 | Kept postings from SmartRecruiters-hosted boards (Canva). File: `verified-2026-09-26.json`. **Below the 25-record bar** — see below.

## Quality gate applied (all three folders)

A record is admitted only if it has all five fields — title, URL, date,
location, department — is deduplicated on source + native ID, and was kept by
the teaching-interest filter with its rule trace intact (`kept_because` +
matched words on every record). Source: the 2026-09-26 run (3,446 postings
fetched, 97 kept, 0 duplicates — see `build-your-data-pipeline/`
for the run files and both audits).

## Records rejected and why

- **Greenhouse:** the run fetched the majority of 3,446 postings; the filter
  kept 53. The rest failed the teaching-interest rules (no role/title/topic
  match) — rejections are logged with reasons in the run files, not here.
- **Ashby:** same — 34 kept of the fetched postings; the rest rejected by rule.
- **SmartRecruiters:** 10 kept. The Canva board fetched 248 postings; only 10
  matched the teaching-interest filter. This is a **thin source**: it clears
  the quality gate but **does not meet the 25-record minimum** for a verified
  source folder. Recorded as TODO: DATA SOURCE in the recipe — either more
  SmartRecruiters boards get wired up, or the recipe runs on two sources with
  the gap labeled.

## What this folder does not cover (honest limits, from Brief Part 3)

Adobe (Workday) and Framer (hand-built pages) have no public feed — absence is
a measurement gap, never "no demand." Amazon's `hits: 10000` is trusted but
unverified as a cap. Big-four runs exist only in uncommitted logs.
