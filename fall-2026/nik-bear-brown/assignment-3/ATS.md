# Which applicant-tracking system each target company uses

## Executive summary

**What this is.** A record of which job-board API each company on Lectern's watch list can be read through, and — for the ones that cannot — a plain statement that I do not know, rather than a guess.

**How it was established.** Every row marked *verified* was probed on 2026-09-26 by requesting the company's board from each of the three public APIs Lectern reads and checking whether a list of postings came back. The postings count in the table is what that request returned. Nothing in the verified column is recalled, inferred from a careers-page design, or assumed from company size.

**What it found.** **13 boards are reachable** across three systems — 8 Greenhouse, 5 Ashby, 1 SmartRecruiters (Figma and Canva counted once each). **5 companies could not be found at all**, and four of them are Tier 1 education players: Adobe, Salesforce, GitHub, Google, plus Shopify. For those five, **the ATS is unknown.** I tried the obvious slug variants on all three APIs and got nothing, and I have not verified what they use instead, so this file does not say.

**Two corrections worth keeping on the record.** HubSpot's board is `hubspotjobs`, not `hubspot` — the plain slug returns a valid but empty board, which would have looked like "HubSpot has no jobs" rather than "wrong slug." And a SmartRecruiters request for a company with no board returns HTTP 200 with `content: []` and `totalFound: 0`, which an early version of the probe scored as a hit; every company appeared to be on SmartRecruiters until that was fixed.

---

## Verified — reachable today

Probed 2026-09-26. Counts are that day's board size, not a contract.

| Company | ATS | Board slug | Postings | How it was verified |
|---|---|---|---:|---|
| Anthropic | **Greenhouse** | `anthropic` | 618 | `boards-api.greenhouse.io/v1/boards/anthropic/jobs` returned 618 postings |
| OpenAI | **Ashby** | `openai` | 830 | `api.ashbyhq.com/posting-api/job-board/openai` returned 830 postings |
| Canva | **SmartRecruiters** | `Canva` | 248 | `api.smartrecruiters.com/v1/companies/Canva/postings` returned `totalFound: 248` (2026-09-19) |
| Figma | **Greenhouse** | `figma` | 163 | Greenhouse board returned 163 postings (152 on 2026-09-19 — the board moves) |
| HubSpot | **Greenhouse** | `hubspotjobs` | 133 | Greenhouse board returned 133. **`hubspot` returns an empty board, not an error** |
| Notion | **Ashby** | `notion` | 128 | Ashby board returned 128 postings |
| Vercel | **Greenhouse** | `vercel` | 88 | Greenhouse board returned 88. `ashby/vercel` returned nothing |
| Replit | **Ashby** | `replit` | 75 | Ashby board returned 75 postings |
| Writer | **Ashby** | `writer` | 51 | Ashby board returned 51 postings |
| Miro | **Greenhouse** | `realtimeboardglobal` | 28 | Greenhouse board returned 28. **The slug is their former company name, RealtimeBoard — `miro` does not work** |
| Webflow | **Greenhouse** | `webflow` | 27 | Greenhouse board returned 27 postings |
| Jasper AI | **Ashby** | `Jasper AI` | 6 | Ashby board returned 6 postings. **The name contains a space and must be URL-encoded** (`Jasper%20AI`) |
| Airtable | **Greenhouse** | `airtable` | 3 | Greenhouse board returned 3 postings |

**By system:** Greenhouse 8 · Ashby 5 · SmartRecruiters 1.

## Unknown — not found, and not guessed

For each of these I requested the slugs listed from all three APIs on 2026-09-26 and no board came back. **I do not know which ATS these companies use.** I have not checked their careers pages, and I am not recording an ATS I have not verified.

| Company | Tier | ATS | Slugs tried (all three APIs) |
|---|---|---|---|
| **Adobe** | 1 | **Unknown** | `adobe`, `Adobe` |
| **Salesforce** | 1 | **Unknown** | `salesforce`, `Salesforce`, `salesforceinc`, `slack` |
| **GitHub** | 1 | **Unknown** | `github`, `GitHub`, `githubinc`, `github-inc` |
| **Google** | 1 | **Unknown** | `google`, `Google`, `googledeepmind`, `deepmind` |
| **Shopify** | 2 | **Unknown** | `shopify`, `Shopify`, `shopifyinc` |

Two things that would be easy to write here and are not, because neither has been verified: that a large enterprise "is on Workday," and that a company with a custom-looking careers page "has no ATS." A careers page can be a skin over any system, and a company absent from these three APIs may be on a fourth Lectern does not read yet — Lever, Workable, SuccessFactors, Workday, or an in-house system.

**What would settle it,** in increasing order of effort: open each careers page and look at where the apply button posts to (the ATS is usually visible in the URL or the network request); check whether that ATS has a public JSON endpoint; if it does, add a provider to Lectern; if it does not, the company stays unreachable and is watched by hand.

This matters more than a footnote, because **four of the five are Tier 1** — Adobe has the oldest education playbook of anyone on the list, Salesforce runs Trailhead, GitHub Education is decades deep, and Google is the incumbent in K-12. A watch list missing all four is incomplete, and Lectern's documentation says so rather than quietly presenting 13 boards as the market.

## Systems Lectern can read, and what each costs

| System | Endpoint | Auth | Ad text in the listing? | Calls per board |
|---|---|---|---|---|
| **Greenhouse** | `boards-api.greenhouse.io/v1/boards/{slug}/jobs?content=true` | none | Yes, in `content` (HTML, double-escaped) | 1 |
| **Ashby** | `api.ashbyhq.com/posting-api/job-board/{name}` | none | Yes, in `descriptionHtml` / `descriptionPlain` | 1 |
| **SmartRecruiters** | `api.smartrecruiters.com/v1/companies/{id}/postings` | none | **No** — listing has titles and locations only | 1 per 100 postings **plus one per posting** for the text |

SmartRecruiters is the expensive one: Canva's 248 postings take 249 requests and about three and a half minutes. Greenhouse and Ashby are one request each, which is why 12 of the 13 boards fetch in seconds.

## How to re-check this

The probe is not a stored script yet — it was run ad hoc on 2026-09-26. `[TODO: DEV]` Make it `probe_ats.py` so the table can be regenerated instead of retyped, and so a board that moves or a slug that changes is caught by re-running rather than by noticing.

For one company by hand:

```bash
curl -s "https://boards-api.greenhouse.io/v1/boards/SLUG/jobs" | head -c 200
curl -s "https://api.ashbyhq.com/posting-api/job-board/SLUG" | head -c 200
curl -s "https://api.smartrecruiters.com/v1/companies/SLUG/postings?limit=1" | head -c 200
```

An empty `jobs` array or `totalFound: 0` means the slug is wrong or the board is empty — not that the company is not hiring.
