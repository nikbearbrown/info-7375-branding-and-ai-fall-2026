# Assignment 2, Part 3 — PRD: the demand-signal agent (worked example)

## Executive summary

**What this is.** The Product Requirements Document for the Madison semester project from Part 1 of Assignment 1: a demand-signal agent for Madison's Intelligence Agents layer, built on the Lectern evidence pattern. Problem, solution, three user stories, success metrics — plus edge cases.

**Why read it.** It is written so someone could build from it: the problem names who bleeds and what it costs, the solution says why Madison instead of anything else, and the metrics are measured the way the project already measures itself (the title audit), not invented.

---

## Problem statement

**Who experiences it.** Design and developer advocates, DevRel leads, and independent education consultants — anyone whose job is knowing where teaching demand is forming.

**The problem.** Nobody can see where education hiring demand is forming. Which design-tool companies are staffing customer-education teams? What roles are they actually hiring — curriculum, enablement, advocacy, video? The information is public — it's sitting in job-board feeds — but reading seven boards across three applicant-tracking systems is hours of manual work, so decisions get made on anecdote: advocates build teaching material for roles that may not exist, and consultants pitch partnerships with no timing evidence.

**Cost of not solving it.** Misbuilt material and mistimed pitches. Figma's Advocacy team is three Designer Advocate postings; the seven-board sweep found the real title is often "Educator," not "Advocate" — a team working from anecdote searches the wrong word. For the consultant, the cost is sharper: the role you want is almost never posted, so without demand evidence you're pitching blind.

## Proposed solution

A Madison **Intelligence Agent** — the demand-signal agent — that watches public job-board feeds on a schedule, extracts education-related demand signals, and publishes a digest where **every claim links to the raw posting it came from**. Three mechanisms, all from the Lectern pattern: source-native record keeping (no renamed fields, any row checkable against the live posting), a published reject list with reasons (misses are findable, not silent), and a human gate — it ranks companies by demand evidence and never scores a person's fit.

**Why Madison vs. other solutions.** Job alerts (LinkedIn, HiringCafe) treat listings as openings to apply to, not evidence to read. Sales-intelligence tools treat hiring as a buying signal but hide their reasoning. Madison is the only frame with both the agent layers to do the work (Intelligence to watch, Research to classify, Content to report) and the Popper integration to keep it honest: evidence-based claims, falsification testing of the classifier, bias detection in what's counted.

**What makes it technically interesting.** The trust problem is the interesting part, not the scraping. A monitor that cries "new role!" on every reposted listing is noise; the two-run confirmation rule (a posting counts as closed only after missing from two consecutive trusted runs) and the fail-loud board assertions are what make the signal worth acting on.

## User stories

1. **As a** Designer Advocate, **I want** a weekly digest of new education-related postings at design-tool companies **so that** I build teaching material for roles that are actually being hired.
2. **As a** DevRel lead, **I want** every demand claim linked to the raw posting it came from **so that** I can verify the signal before I act on it.
3. **As an** independent education consultant, **I want** to see which companies are staffing customer-education teams **so that** I can pitch partnership work with timing evidence instead of a cold email.

## Success metrics

| What improves | By how much | How measured |
|---|---|---|
| Classification precision (kept postings that are truly education-related) | ≥ 90% on a 100-posting audit sample | The title-audit method, re-run monthly — the same method that already found 45 false positives and 2 candidate misses by job function, and fixed them |
| Time to produce a demand sweep | From ~4 hours of manual board-reading to under 15 minutes of review | Timed run: the Canva SmartRecruiters sweep took 3h38m of API work for one board; the agent runs it on a schedule |
| Claim traceability | 100% of digest claims link to a raw record | Spot-check 20 claims against live postings; any unlinked claim is a bug |
| Miss rate on known education roles | < 5% | The reject list is published with reasons, so misses are countable — the audit's 2 candidate misses are the baseline to beat |

## Edge cases and failure modes

- **Board layout changes.** Greenhouse/Ashby/SmartRecruiters change their feeds; the collector asserts field positions and fails loudly instead of returning blank titles.
- **Reposted listings.** Same role, new ID — the two-run rule and native-ID diffing keep reposts from reading as new demand.
- **Unreachable companies.** Adobe (Workday), Framer (hand-built pages) have no public feed; the digest says so explicitly rather than silently omitting them — absence is labeled as a measurement gap, not as no demand.
- **Rate limits.** SmartRecruiters paginates 100 at a time with no ad text; the agent budgets one polite request per second and caches raw responses.
- **The human gate holds.** The agent never applies, never scores a person, never contacts a company. Rankings are evidence for a human's decision.