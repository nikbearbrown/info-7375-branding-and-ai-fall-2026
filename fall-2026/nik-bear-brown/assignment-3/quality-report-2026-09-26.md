# Lectern run — 2026-09-26

## Executive summary

**What ran.** Lectern fetched **18 job boards across three applicant-tracking systems**, read **3,446 postings**, and kept **88** whose titles or text are about teaching, advocacy, or education. Both data files are in this folder: [`all-jobs-2026-09-26.json`](all-jobs-2026-09-26.json) — every posting, kept or rejected, with the reason — and [`jobs-of-interest-2026-09-26.json`](jobs-of-interest-2026-09-26.json), the 88 kept with the words that matched and the full text.

**Six roles are both remote and genuinely advocacy** — the actual answer to the question this tool exists to ask:

| Company | Role | Where |
|---|---|---|
| **GitLab** | Senior Developer Advocate | Remote, Canada **and Remote, United States** |
| **Supabase** | Developer Relations Engineer (×3) | Remote + SF · Remote + New York · Remote + London |
| **Webflow** | Senior Developer Educator | U.S. Remote (1 week/month in SF) |
| **HubSpot** | Academy Professor, French & Portuguese | Remote — Ireland |

**Three findings from widening the list.**

1. **Vercel went from zero to one.** It matched nothing in the morning run and by the afternoon had a *DevRel Engineer, Agentic Infrastructure*. That is the whole argument for P5 — watch the company, not the current opening — proving itself inside one day.
2. **The two biggest AI labs are hiring educators.** Anthropic: 23 matches, including *Developer Education Lead (Claude Platform)*, *Lead Technical Instructor*, *Head of Technical Training*. OpenAI: 17, including *Tech Lead Manager, Education*.
3. **One keyword had to be cut for being noise, and the cut is recorded.** `developer experience` was added as an advocacy synonym, fired on 11 postings, and **10 of them were backend or platform software-engineering jobs**. It names an engineering discipline, not a role. Removed in `keywords.json` v0.2.1, along with `advocacy` (1 hit, a customer-marketing programme). `devrel` was kept — it is what found Vercel's role.

**The quality number that matters.** Every kept record has a title, a URL, and a parseable date, because a record missing any of the three is never written. Completeness on the fields that can vary — location, department, date — is **3,446 / 3,446 (100%)** across every posting fetched. No duplicates.

**The honest caveat.** **"Enablement" is the most common matched word by a wide margin — 34 of the 88 — and at Stripe and GitLab it usually means sales enablement, not teaching.** Those records are in the file because the filter is honest about what it matched, not because they are jobs worth reading.

---

## Counts

| | |
|---|---:|
| Boards requested | 18 |
| Boards that answered | 18 |
| Postings fetched | 3,446 |
| Unique postings | 3,446 |
| **Kept** | **88** |
| Rejected | 3,358 |
| Duplicates collapsed | 0 |

### Rejections, by reason

| Reason | Count |
|---|---:|
| No keyword match at all | 2,345 |
| Only 1 topic word, no role word in the title | 950 |
| Only 2 topic words, no role word in the title | 63 |
| Missing title / URL / unparseable date | 0 |

The rule keeps a posting on **one role word in the title** or **three or more topic words in the body**. That threshold is the most consequential number in `keywords.json`: the two "only N topic words" rows are 1,013 postings that mentioned teaching once or twice in passing.

## Per board

| Company | Source | Postings | Kept |
|---|---|---:|---:|
| OpenAI | ashby | 830 | 17 |
| Stripe | greenhouse | 702 | 10 |
| Anthropic | greenhouse | 618 | 23 |
| GitLab | greenhouse | 199 | 3 |
| Canva | smartrecruiters | 197 | 10 |
| Figma | greenhouse | 163 | 9 |
| Twilio | greenhouse | 138 | **0** |
| HubSpot | greenhouse | 133 | 1 |
| Notion | ashby | 128 | 5 |
| Vercel | greenhouse | 88 | 1 |
| Replit | ashby | 75 | 2 |
| Supabase | ashby | 56 | 4 |
| Writer | ashby | 51 | 1 |
| Miro | greenhouse | 28 | **0** |
| Webflow | greenhouse | 27 | 1 |
| Jasper AI | ashby | 6 | **0** |
| Netlify | greenhouse | 4 | 1 |
| Airtable | greenhouse | 3 | **0** |

Boards that matched nothing today — and stay on the watch list (P5): Twilio, Miro, Jasper AI, Airtable.

## Completeness

| Field | Present | Of |
|---|---:|---:|
| title | 3,446 | 3,446 |
| url | 3,446 | 3,446 |
| date_posted (parsed to `YYYY-MM-DD`) | 3,446 | 3,446 |
| location_text | 3,446 | 3,446 |
| department | 3,446 | 3,446 |

100% on every field. That is a fact about these three APIs being well-formed, not a claim about Lectern's cleaning, which did nothing because nothing needed it.

## What this run does not tell you

- **Nothing here says a job is good.** 88 records matched words. `enablement` alone accounts for 34 of them and is usually a sales function.
- **The watch list is incomplete.** Five companies from the target list cannot be read at all — Adobe, Salesforce, GitHub, Google, Shopify — and four are Tier 1 education players. Four more named as advocacy employers were also unreachable on all four APIs tried: **Hugging Face, Framer, Sketch, InVision**. See [`ATS.md`](ATS.md).
- **This is one day.** Figma had 152 postings on 2026-09-19 and 163 today; Canva 248 then, 197 now. The counts are a snapshot.
- **False negatives are still unmeasured.** `VERIFICATION.md` requires reading 20 rejects by hand to classify what the filter misses. Not done, so no accuracy figure is claimed in either direction.

## Reproduce it

```bash
python3 collect.py                      # fetch all 18 boards, filter, write both files
python3 collect.py --from-raw raw/      # no network; re-filter the saved responses
python3 collect.py --only ashby         # one provider
```

`raw/` holds each response exactly as it arrived — about 45 MB for this run, so it is **not committed**. The two data files are, which is the point: open `all-jobs-2026-09-26.json`, find a posting Lectern rejected, and disagree.
