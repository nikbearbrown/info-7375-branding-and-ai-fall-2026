# Assignment 4, Part 1 — Add real intelligence (worked example)

## Executive summary

**What this is.** The intelligence layer added on top of Assignment 3's collection pipeline: what it decides, what it learns, and how it handles failure.

**Why read it.** The brief asks for "AI doing something clever." The clever thing here isn't generating text — it's making *decisions with reasons* at every step, then measuring those decisions and fixing them. That is the brief's own example list: detecting patterns → triggering actions, making decisions → routing to different outcomes.

**What got smarter.** A3 saved 3,446 postings. A4 reads them: three classification rules (every keep/reject explained), a five-kind demand ranker (postings → company rankings), a time differ (what's new, what's gone), and an audit loop that caught 45 false positives and changed the rules.

---

## The intelligence: four capabilities

**1. The classifier decides — with reasons.** Every posting gets a verdict, and the verdict is never just a label. Three rules: a role word in the title (`advocate, educator, enablement, …`), three teaching-topic words in the body, or the body saying the job *produces teaching materials*. Each kept posting records which rule fired and which words matched; each of the 3,349 rejects records why it was rejected. Implementation: `collect.py` + `keywords.json` + `title_families.json`.

**2. The demand ranker turns postings into rankings.** `demand_report.py` reads the kept postings and scores each company on five kinds of demand signal (direct education roles, advocacy, enablement, materials production, adjacent). Output: `company-demand-2026-09-26.md` — 18 companies, 5 kinds, 57 signal roles, ranked. This is the pattern-detection step: 97 postings become one page a human can act on.

**3. The differ reads change over time.** Same board, two dates, native IDs compared: the Figma 2026-09-23 → 2026-10-08 diff found 23 new postings (including the Designer Advocate in Berlin) and 32 gone. Trend detection, not just a snapshot.

**4. The audit loop learns.** This is what the system "learns." The title audit read kept postings by job function and found 45 false positives — 15 Anthropic *Applied AI Architects* kept on *technical content* + *our users*, four IT Support Engineers kept on *how-to guides*. Nine phrase groups were cut from the materials rule; it went from ~1-in-10 precision (101 extra kept) to 4-of-5 right. The reject audit (100 random + 63 closest calls) re-judged the borderline and corrected a whole category: 13 sales-enablement postings first called errors are *not* errors — internal training is the work. The rules changed because the measurement said so. That is the learning.

## Error handling

**What could go wrong:**
- A board changes its feed shape → blank or mislabeled titles
- An ATS rate-limits or times out (Microsoft's PCSX throttles hard; SmartRecruiters paginates slowly)
- A run fetches far fewer postings than the source reports (incomplete data → false "closed" signals)
- A posting is missing title, link, or date

**How it's handled:**
- **Fail loud, not silent.** The readers assert field positions per ATS; a layout shift raises instead of writing blank titles.
- **One board's failure never kills the run.** Per-source try/except: a timeout is logged as unavailable and the other sources keep going.
- **Polite by default, backoff on 429.** One request per second with jitter; `polite_get` retries rate limits with 30s backoff.
- **Incomplete runs can't close anything.** The trusted-run rule: a run counts only at ≥90% of the source-reported total and ≥70% of the previous trusted run; a job is marked closed only after missing from *two consecutive trusted runs*.
- **Missing critical fields = not written.** No title, link, or date → the record is filler and stays out.

In n8n terms: the Code node wraps the classifier in try/catch (bad record → logged, skipped, next item), the HTTP Request nodes carry retry-with-backoff, and the trusted-run check is the "On Error" branch that quarantines an incomplete run instead of letting it poison the diff.