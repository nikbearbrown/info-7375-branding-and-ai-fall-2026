# Assignment 2, Part 4 — Technical architecture (worked example)

## Executive summary

**What this is.** The agent design for the demand-signal agent (three agents, how they communicate) and the honest Week 3 MVP scope: one n8n workflow, 3–5 named nodes, input → process → output, and what won't get built.

**Why read it.** The agents map onto Madison's real layers, the data schema between them is written out (not hand-waved), and the MVP is small enough to ship in a week — the scope section says what it won't do, which is where most student architectures fail.

---

## The Madison agent design

Three agents, each with one job, mapped to Madison's layers:

| Agent | Layer | Job |
|---|---|---|
| **Board Watcher** | Intelligence | Fetches the public ATS feeds on schedule; saves the raw board response untouched, with fetch time and URL |
| **Signal Classifier** | Intelligence → Research | Applies the keyword/title rules to each posting; writes every kept posting to `kept` and every rejected one to the reject list *with its reason* |
| **Evidence Reporter** | Content | Builds the weekly digest: demand ranked by company, every claim hyperlinked to the raw posting record; stops at the human gate — no applying, no outreach |

### How they communicate

```
Board Watcher ── raw/*.json ──▶ Signal Classifier ── kept.json + rejects.json ──▶ Evidence Reporter ── digest.md ──▶ human
      │                              │                                                        │
      └──── feed URL + fetched_at ────┴── native IDs only, never renamed ─────────────────────┘
```

The contract between agents is the **native posting record** — the ATS's own fields, unrenamed — so any downstream claim can be traced back to the exact raw response. The Classifier never invents fields; the Reporter never claims what the raw data doesn't show.

### Data schema between agents

```json
{
  "job_id": "6176134004",
  "company": "Figma",
  "ats": "greenhouse",
  "title": "Designer Advocate",
  "url": "https://boards.greenhouse.io/figma/jobs/6176134004",
  "location": "San Francisco, CA",
  "fetched_at": "2026-09-26T14:00:00Z",
  "verdict": "kept | rejected",
  "verdict_reason": "title rule: role word 'advocate' + topic word 'design systems'",
  "raw_ref": "raw/figma-2026-09-26.json#6176134004"
}
```

## MVP scope (Week 3)

**The ONE workflow:** a scheduled sweep of one board (Figma, Greenhouse) → classify → write the digest file. If it can't do one board end to end, it can't do seven.

**The n8n nodes (4):**

1. **Schedule Trigger** — weekly, Monday 06:00 ET.
2. **HTTP Request** — `GET https://boards-api.greenhouse.io/v1/boards/figma/jobs?content=true`; one call, full ad text. Saves the raw response to a file.
3. **Code** — the classifier: applies the keyword/title rules from `keywords.json`, emits `kept.json` and `rejects.json` in the schema above.
4. **Google Sheets** (or **Slack**) — appends the digest rows: company, new education postings this week, link per claim. The human reads the sheet; the agent stops there.

**Input → process → output:** board feed URL in → raw JSON saved → rules applied → digest rows out. Total moving parts: one schedule, one HTTP call, one rules file, one output table.

**What I WON'T build (honest scope):**

- The closed-job diffing (the two-run confirmation rule) — that needs the SQLite monitor and a second scheduled run; it's Week 4+, not the MVP.
- Multi-ATS support — Ashby and SmartRecruiters have different feed shapes; Greenhouse first, the pattern generalizes later.
- Any UI beyond the sheet — no dashboard, no charts; the digest is a table a human reads.
- Outreach or application logic — the human gate is a design constraint, not a missing feature.