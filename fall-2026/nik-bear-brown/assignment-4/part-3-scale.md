# Assignment 4, Part 3 — Prove it can scale (worked example)

## Executive summary

**What this is.** Honest stress numbers: what was actually run, what broke first, what it costs, and whether this could run 24/7.

**Why read it.** The brief deducts 20 points for fake scale testing, so there is none here — every number below is from a run that happened, and the breaking points are the ones actually hit.

---

## Scale testing results

| Test | What ran | Result |
|---|---|---|
| Single board, one call | Figma's Greenhouse feed (`?content=true`) | ~152 postings, seconds |
| One slow board, full paging | Canva's SmartRecruiters feed (no ad text → one call per posting) | 248 postings, **251 requests, 3m38s** |
| Full 18-board sweep | Three ATS APIs, polite 1 req/sec | **3,446 postings**, one unattended run |
| Big-board paging | Google careers, 20 per page | 3,345 postings ≈ 168 requests ≈ **~3 minutes** at 1 req/sec |
| Big-board paging | Amazon search.json, 100 per page | 9,993 of 10,000 reported ≈ 100 requests |
| Hostile API | Microsoft PCSX, 10 per page, throttles hard | **HTTP 429s**; slowed to ~1 req/5–6s → ~1,700 postings ≈ **15+ minutes**; latest full run never completed trusted |

## What breaks first

- **Rate limits, not memory.** Microsoft's API throttles at roughly one request per 5+ seconds and returns 429 under sustained pull — the run slows to a crawl before anything else breaks. Nothing in the pipeline has ever hit a memory limit; the largest single artifact is under 3 MB of JSON.
- **Paging cost.** SmartRecruiters' missing ad text multiplies one board into 251 requests. That's the most expensive source per posting by far.
- **The reported-total question.** Amazon's API reports `hits: 10000` — a round number the collector trusts but can't verify. If it's a result cap rather than the true total, the trust rule (≥90% of reported) passes while postings go unseen. Documented as an open question, not hand-waved.
- **Timeout errors** appear past ~30s on slow boards; the per-source try/except isolates them.

## Production readiness

- **Could this run 24/7?** Not as built — and that's honest. The "daily recipe" runs on Professor Bear's command, not on a schedule. The pipeline itself is stateless and idempotent (dated files, never overwrite), so scheduling it is a cron line, not a redesign. What's missing for true 24/7: the Microsoft throttle handling (checkpoint resume — the collector re-fetches from zero today) and alerting on untrusted runs.
- **Estimated monthly cost at 1,000 requests/day:** **$0.** Public feeds, no keys, stdlib Python, files on disk. The only real cost is time: ~17 minutes a day at current politeness settings.
- **Required monitoring:** (1) trusted/untrusted per source per run — an untrusted run must page someone, because it silently freezes the closed-job logic; (2) feed-shape assertions — a layout change fails loud today but nobody is listening; (3) the Amazon `hits` question — a periodic category-split count to check whether 10,000 is real.

## The honest summary

It scales to the boards it was built for — 3,446 postings in one unattended run — and the breaking points are known, named, and mostly about other people's rate limits rather than the pipeline. What it can't do yet: run itself, survive Microsoft's throttle without babysitting, or prove Amazon's total. All three are written down as the next work, which is what "production readiness" actually means at this stage.