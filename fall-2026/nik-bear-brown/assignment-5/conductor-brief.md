# The Conductor Brief: Lectern

**Course:** INFO 7375 Branding and AI, Fall 2026 — Assignment 5
**Author:** Nik Bear Brown (worked example)
**Status:** Draft 2026-10-10 (rev. 2). Numbers marked [VERIFIED] trace to committed run files; numbers marked [UNVERIFIED] come from an agent's uncommitted run log. Competitor notes are web research (product pages, independent reviews); first-hand trials are still owed. Incorporates the 2026-10-10 research files on Meta's education product (resolved: keep), training-failure cases, and the Scoutify/sales-intel check.

---

## Part 1: The Tool in One Sentence

**Lectern helps an independent AI-education consultant find which companies selling AI to universities are showing real interest in how their tools are used in teaching, so they can pitch a role that hasn't been posted yet.**

Why this sentence: it names a real user (not "marketers"), a specific action (find which companies are showing real interest), and a human outcome (pitch the unposted role). No tech stack, no agent names, no "leverages."

---

## Part 2: The User and the Problem

### A. The user and their situation

- **Primary user:** An independent AI-education consultant — typically a working professor or former educator selling teaching expertise to software vendors.
- **Their situation:** They want an education-advocate role (flexible, part-time, or consulting) with a company whose tools they already teach. That role is almost never posted. So the real job is figuring out *which companies are worth approaching, and when* — where is genuine interest in teaching forming?
- **What they are doing right now instead:** Scrolling careers pages by hand (an hour a week, first thing to get skipped), LinkedIn job alerts on titles like "advocate," and conference chatter.
- **Why that is not good enough:** Alerts match *titles*, not interest — and the title search itself was wrong: a seven-board sweep found the real word is often "Educator," not "Advocate." Hand-checking doesn't scale across 18 boards and three applicant-tracking systems, and anecdote can't tell you what's *new* this month versus always there. The cost: mistimed pitches, missed timing windows (a newly posted Designer Advocate in Berlin is a trigger, not trivia), and pitching blind.

### B. Three user stories

**Story 1 — the core job:**
As an independent AI-education consultant, I want a ranked view of which companies selling AI to universities are staffing education-related roles, so that I can pitch an unposted advocate role with timing evidence instead of a cold email.

**Story 2 — a secondary use case:**
As a developer-relations lead at a design-tool company, I want to see which competitors are building education teams, so that I can time our own teaching-material investments instead of guessing.

**Story 3 — the edge case / power user:**
As a skeptical consultant, I want every demand claim linked to the raw posting it came from, so that I can verify the signal myself before I stake a pitch on it.

---

## Part 3: The Data Contract

Every source below is a public, keyless JSON feed (the Assignment 3 collection). The contract is a promise: what goes in, what it means, and how we know it's good enough.

### Data Source 1 — Greenhouse public boards API
- **What it is:** JSON feed, one call per board with full ad text inline. The 2026-09-26 run [VERIFIED]: the majority of 3,446 postings across 18 boards.
- **What it represents:** What design-tool and AI-lab companies are hiring for, in their own words — the demand signal itself. A new "Designer Advocate" posting is a company saying, in public, that teaching its tool matters enough to staff.
- **How we know it is good:** Every record has a title, URL, date, location, and department (3,446/3,446 [VERIFIED]); field positions are asserted per board so a layout change fails loudly instead of writing blank titles; raw responses are saved untouched and dated.
- **Local path:** `data/verified/lectern/all-jobs-YYYY-MM-DD.json` (convention; current files: `assignment-3/all-jobs-2026-09-26.json`, `lectern/runs/2026-10-08/all-jobs-2026-10-08.json`)

### Data Source 2 — Ashby posting API
- **What it is:** JSON feed, one call per job board (board names URL-encoded). Part of the 3,446 postings [VERIFIED].
- **What it represents:** The AI-lab half of the market — OpenAI, Anthropic, Writer, Notion, and others. Same demand signal, different company set.
- **How we know it is good:** Same record standard as Source 1; same raw-save rule.
- **Local path:** `data/verified/lectern/` (same convention; same run files)

### Data Source 3 — SmartRecruiters postings API
- **What it is:** JSON feed, paged 100 at a time, **no ad text** — one extra call per posting fetches the description. The Canva board: 248 postings, 251 requests, 3m38s [VERIFIED from the run notes].
- **What it represents:** Companies unreachable any other way (Canva). The per-posting call is the documented price of the third source.
- **How we know it is good:** Same record standard; the paging loop is verified to emit no duplicates across pages.
- **Local path:** `data/verified/lectern/` (same convention; same run files)

**What the contract does not cover (honest limits):** Adobe (Workday) and Framer (hand-built pages) have no public feed — absence from the data is labeled a measurement gap, never read as "no demand." Amazon's API reports a round `hits: 10000` that the collector trusts but cannot verify [UNVERIFIED whether it's a cap]. Big-four collector runs (Google/Amazon/Microsoft) exist only in uncommitted run logs [UNVERIFIED]. Meta stays on the watch list: Meta for Education (VR program, generally available) plus the AI Academy Kenya and the AI Learning Alliance give it a real education footprint — though its play is VR-first, so the signal to watch there is enablement/training/academy roles, not AI-assistant roles.

---

## Part 4: What Good Looks Like

Phase-gate criteria — what the human checks at each step before the pipeline continues.

**Step 1 — Data ingestion.**
Good looks like: every source returned its expected board count; raw responses are saved untouched, dated, per source; fetch counts are recorded next to the source-reported totals. (A run that fetched 151 Figma postings against a 160-posting snapshot is *expected* — boards change; a run that fetched 12 is not.)

**Step 2 — Data validation (GIGO gate).**
Good looks like: 100% of records carry title, URL, date, location, department; duplicates are collapsed on source + native ID (0 remaining); the field assertions passed (no silent schema drift). The run is *trusted* only at ≥90% of the source-reported total and ≥70% of the previous trusted run — otherwise nothing downstream may treat anything as "closed."

**Step 3 — Intelligence layer.**
Good looks like: every kept posting names the rule that fired and the words that matched; every rejected posting names its reason; the demand ranking links each company claim to its signal roles; the new/gone diff compares native IDs across two *trusted* runs. Trust test: pick any claim at random — you can reach the raw posting in two clicks.

**Step 4 — Final report.**
Good looks like: a non-technical reader can answer "which companies, what roles, what's new this month" from page one; every number is recomputable from the committed files; the report states its limits (unreadable companies, unverified totals) instead of hiding them.

---

## Part 5: What Bad Looks Like

**Step 1 — Data ingestion.**
Bad looks like: a whole ATS returns nothing, or a board that had 248 postings returns 12.
**Response: log and continue** — the failure is recorded as unavailable and the other sources keep going (one board's outage must not destroy the run). **Flag for review** if an entire ATS is dark across two runs.

**Step 2 — Data validation (GIGO gate).**
Bad looks like: field assertions raise (the board changed its layout), or a run lands under 90% of the reported total.
**Response: hard stop for that source's downstream** — nothing blank is ever written, and an untrusted run *freezes* the closed-job logic (it may update "seen" timestamps, but it closes nothing). This is the most important gate in the system: a bad run must not be allowed to declare jobs dead.

**Step 3 — AI processing.**
Bad looks like: a rule keeps 101 postings at ~1-in-10 precision (this actually happened with the first teaching-materials rule — 15 Anthropic *Applied AI Architects* kept on *technical content* + *our users*), or a demand claim appears with no raw link behind it.
**Response: flag for review, then fix and re-audit** — nine phrase groups were cut and the rule re-measured (now 5 kept, 4 right). An unlinked claim is a bug, not a judgment call: **hard stop** until it's traced or removed.

---

## Part 6: The One Thing

### A. Competitive evidence

**Competitor 1: LinkedIn Job Alerts**
- **What they do well:** The largest listing pool in the world; free daily/weekly alerts by email and app; every job seeker already lives there.
- **Where they fall short for our user:** Alerts match *titles for applicants*. They can't read company interest, they show no evidence trail, and there's no demand view — just a stream of openings. Our user isn't applying.
- **Source:** Web research — LinkedIn's own alert documentation and an independent 2026 job-alert roundup (scoutify.com). First-hand trial not yet done.

**Competitor 2: HiringCafe**
- **What they do well:** Indexes ~5.7M jobs directly from company career pages (bypassing aggregators), AI-parses each posting into structured facts (salary, tools, clearance), free with an AI Talent Agent that scouts 24/7. Raised $6.8M pre-seed in Sept 2026.
- **Where they fall short for our user:** Built end-to-end for *applicants* — every result terminates at "apply here." It finds openings brilliantly; it never asks what a board *means*, and it shows no reasoning a skeptic could check.
- **Source:** Web research — funding coverage (citybiz.co, pulse2.com) and product pages. First-hand trial not yet done.

**Competitor 3: TrueUp**
- **What they do well:** ~280K tech jobs across 9,000+ companies *plus* company intel — funding, layoffs, trajectory scores, open-role trends. The closest thing to "hiring as signal" in the seeker market.
- **Where they fall short for our user:** The intel answers "where should I work," not "who cares about teaching." No education taxonomy, no per-claim traceability, and the demand lens is tech-wide rather than teaching-specific.
- **Source:** Web research — trueup.io product pages. First-hand trial not yet done.

**Also evaluated (not counted among the three):** *Scoutify* (scoutify.com) — watches 70,000+ company career pages directly (Greenhouse, Lever, Ashby, Workday, SmartRecruiters — the same plumbing Lectern uses) and pushes alerts within ~5–15 minutes; $5/week for alerts, more for auto-apply. The cleanest comparison in the set: it proves the data is reachable, but treats every listing as something to *apply to*, never as evidence of what the company cares about. *HireSignal* (open-source MCP server) — turns postings into B2B buying signals ("which fintechs posted RevOps roles this week?" → in-market for CRM tooling), claiming the signal surfaces 60–90 days before vendor research starts. This is the honest challenge to the "one thing": sales-intel tools *do* read listings as evidence of company interest — but for *purchasing* intent, aimed at sales teams. Lectern reads a subset sales tools don't parse (teaching-related hiring: customer education, enablement, training, academy roles) as evidence of interest in *pedagogy* — a question nobody in that category answers.

**The gap all three share:** Every one of them treats a listing as *an opening to apply to*. None reads the board as *evidence of what the company cares about*, and none shows its work — there is no reject list, no rule trace, no way to verify a claim except to trust the tool.

### B. The one thing

**Lectern is the only job-board reader that turns listings into checkable evidence of a company's interest in teaching, for the independent education consultant, without asking them to pretend to be a job seeker.**

- **Why this matters to our user:** The role they want is almost never posted. A tool that only finds openings is useless to them; a tool that reads *interest* — with the timing to act on it — is the entire pitch strategy. And the interest is real: when one AI-tutoring deployment added structured educator onboarding, student engagement went from 11% to 64% with the same product (vendor-reported case) — the gap is training, not the tool, which is exactly what the consultant is selling.
- **Why this is defensible:** Three things a competitor can't copy in a week: (1) the education-specific taxonomy (title families, the teaching-materials rule) built from 3,446 real postings and two audits; (2) the audit loop that measures the filter and publishes its misses — 45 false positives fixed, on the record; (3) native-ID traceability from every claim back to the raw board response. A filter is a weekend; a *verifiable* filter is a practice.

---

*Prepared 2026-10-10 as the INFO 7375 Branding and AI Assignment 5 worked example. It synthesizes Assignments 1–4 and is the strategic foundation for the recipe (5B), the interface (5A), the brand identity (A6), and the Weeks 7–12 pitch.*
