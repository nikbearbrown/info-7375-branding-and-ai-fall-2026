# Assignment 4, Part 4 — Professional package (worked example)

## Executive summary

**What this is.** The interview-ready materials: the one-page executive summary, the technical architecture diagram, and the demo walkthrough plan.

**Why read it.** This is the page you'd hand a hiring manager. Problem in two sentences, what was built, what it proved, what it's worth — then the diagram and the demo that back it up.

---

## Executive summary (one page)

**Problem solved.** Education hiring demand is invisible: the signal sits in public job-board feeds, but reading 18 boards across three applicant-tracking systems is hours of manual work, so advocates build the wrong material and consultants pitch blind. (2 sentences.)

**Solution approach.**
- Three public, keyless ATS feeds (Greenhouse, Ashby, SmartRecruiters) read on a polite schedule; raw responses saved untouched and dated.
- A three-rule classifier keeps education-related postings — every verdict explained, every reject reasoned.
- A demand ranker turns 97 kept postings into a one-page ranked company report.
- A time differ tracks what's new and what's gone per board.
- Two audits measured the filter and changed the rules (45 false positives fixed).

**Sample outputs / results.** `company-demand-2026-09-26.md` (18 companies, 5 kinds, 57 signal roles); `jobs-of-interest-2026-09-26.csv` (97 kept, human-readable); the Figma 23-new/32-gone diff that surfaced a Designer Advocate posting in Berlin.

**Performance metrics.** 3,446 postings per unattended run; 100% record completeness; 0 duplicates; classifier precision improved from ~1-in-10 to 4-of-5 on the materials rule after the audit; monthly operating cost $0.

**Business value.** An advocate team gets weekly demand evidence for what teaching material to build next; a consultant gets timing evidence for partnership pitches. The same pattern generalizes: any "where is the hiring demand?" question becomes a scheduled, checkable report.

**Built with:** Python stdlib collectors + the n8n four-node form (Schedule Trigger → HTTP Request → Code → Google Sheets).

## Technical architecture

```
                    ┌──────────────┐
                    │ sources.json │
                    │ 18 boards,   │
                    │ 3 ATSs       │
                    └──────┬───────┘
                           │ schedule / on demand
              ┌────────────┼────────────┐
              ▼            ▼            ▼
     ┌─────────────┐ ┌──────────┐ ┌──────────────┐
     │ Greenhouse  │ │  Ashby   │ │SmartRecruiters│
     │ 1 call,     │ │ 1 call,  │ │ paged 100,   │
     │ full text   │ │ full text│ │ +1 call/post │
     └──────┬──────┘ └────┬─────┘ └──────┬───────┘
            │  fail-loud field asserts   │
            ▼             ▼              ▼
     ┌────────────────────────────────────────┐
     │  RAW STORE (raw/, dated, untouched)     │
     └──────────────────┬─────────────────────┘
                        ▼
     ┌────────────────────────────────────────┐
     │  CLASSIFIER (collect.py + keywords +   │
     │  title_families): 3 rules → kept (97)  │
     │  + rejects (3,349) WITH REASONS        │
     └──────┬───────────────────┬─────────────┘
            ▼                   ▼
   ┌────────────────┐  ┌──────────────────┐
   │ DEMAND RANKER  │  │  DIFFER (native  │
   │ demand_report  │  │  IDs, two dates) │
   │ → ranked co.   │  │  → new / gone    │
   │   report       │  │                  │
   └───────┬────────┘  └────────┬─────────┘
           └──────────┬────────┘
                      ▼
     ┌────────────────────────────────────────┐
     │  HUMAN GATE — digest, CSV, reports.    │
     │  No applying. No outreach. No scoring  │
     │  of people. Rankings are evidence for  │
     │  a human's decision.                   │
     └────────────────────────────────────────┘

  FAILURE PATHS (dotted):
  ··· board timeout → logged unavailable, others continue
  ··· layout change → assert raises, nothing blank written
  ··· 429 → backoff, retry
  ··· incomplete run → untrusted: diffs frozen, alert
```

**AI components labeled:** the classifier (decision + reasons), the demand ranker (pattern → ranking), the differ (trend detection), the audit loop (measurement → rule changes). **Integration points:** the three ATS feeds in, the CSV/report/digest out. **Failure paths:** dotted above.

## Demo walkthrough (3–5 minutes)

1. **The problem** (30s): 18 boards, hours by hand, decisions on anecdote.
2. **The run** (60s): one command; watch the counts; the raw files land dated.
3. **The intelligence** (60s): open the kept CSV — every row names its rule; open the reject sample — every row names its reason; the demand report's ranked page.
4. **The learning** (45s): the audit's before/after — 101 sloppy keeps → 5, 4 right; the sales-enablement correction.
5. **The scale honesty** (45s): the numbers table, what breaks first, what it costs ($0), what it can't do yet.

**Backup plan if the demo fails:** never run live. The demo runs against the committed 2026-09-26 files — the outputs already exist, so a dead network changes nothing. If asked for "live," re-run one Greenhouse board (one call, seconds) and diff against the saved raw.