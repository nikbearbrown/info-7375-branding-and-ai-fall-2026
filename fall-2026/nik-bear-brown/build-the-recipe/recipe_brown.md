# RECIPE: Lectern — teaching-demand pipeline

Version: 1.0 | Last run: 2026-09-26 | Run frequency: Weekly (on demand for a pitch push)

--- EXECUTIVE SUMMARY ---

This recipe runs Lectern's weekly demand scan: it fetches job postings from
three public ATS feeds (Greenhouse, Ashby, SmartRecruiters), validates every
record against the GIGO gate, keeps the postings that are evidence of teaching
interest (with the rule that fired on each), and produces a company demand
report the conductor's user — the independent AI-education consultant — reads
to decide who is worth approaching about unposted work. The conductor is
whoever runs it (Claude Code, a colleague, future-you); a successful run
produces `logs/reports/demand-YYYY-MM-DD.md` with every claim traceable to a
raw posting in two clicks, plus a reject log with reasons.

--- LAYER 1: EXTERNAL SOURCES → data/raw/ ---

Step 1.1  Greenhouse public boards API
  Action:  One keyless JSON call per watched board (18 boards in the 2026-09-26
           run); save each raw response untouched, dated, per board.
  Output:  data/raw/greenhouse/YYYY-MM-DD/<board>.json
  TODO:    RESOLVED — collector exists (build-your-data-pipeline/collect.py);
           field positions asserted per board so layout changes fail loudly.

Step 1.2  Ashby posting API
  Action:  One keyless JSON call per board (board names URL-encoded); same
           raw-save rule as 1.1.
  Output:  data/raw/ashby/YYYY-MM-DD/<board>.json
  TODO:    RESOLVED — same collector, same assertions.

Step 1.3  SmartRecruiters postings API
  Action:  Paged fetch (100/page), then one extra call per posting for the
           description (Canva: 248 postings, 251 requests, ~3.5 min).
  Output:  data/raw/smartrecruiters/YYYY-MM-DD/<board>.json
  TODO:    TODO: DATA SOURCE — only one SmartRecruiters board (Canva) is wired
           up; 10 verified records in the last run, below the 25-record bar.
           Resolve by wiring more boards or accepting a two-source recipe.

PHASE GATE 1 | Judgment type: IJ (Ingest Judgment)
  Good looks like: Every source returned its expected board count; raw
    responses saved untouched, dated, per source; fetch counts recorded next
    to the source-reported totals. (Figma 151 vs a 160-posting snapshot is
    expected drift; 12 is not.)
  Bad looks like:  A whole ATS returns nothing, or a board that had 248
    postings returns 12.
  Response:        Log and continue — record the source as unavailable and let
    the other sources finish. Flag for review if an entire ATS is dark across
    two consecutive runs.

--- LAYER 2: data/raw/ → data/verified/ ---

Step 2.1  Record validation (GIGO gate)
  Action:  Assert every record carries title, URL, date, location,
           department; collapse duplicates on source + native ID; run the
           field-position assertions per board.
  Output:  data/verified/<source>/verified-YYYY-MM-DD.json
  Rejects: data/raw/rejected/<source>/ with the failed assertion logged per
           record. Nothing blank is ever written downstream.
  TODO:    TODO: DEFINE — the trusted-run thresholds (≥90% of source-reported
           total, ≥70% of previous trusted run) are set from the 2026-09-26
           run; confirm they still fit once two more weekly runs exist.

Step 2.2  Teaching-interest filter
  Action:  Apply the rule set (role words in title, topic words in text,
           materials rule as currently tuned); every kept record stores
           kept_because + matched words; every rejected record stores its
           reason.
  Output:  data/verified/<source>/verified-YYYY-MM-DD.json (kept records only)
  TODO:    RESOLVED — rules + the audit loop that cut nine phrase groups after
           the materials rule failed at ~1-in-10 (now 5 kept, 4 right).

PHASE GATE 2 | Judgment type: IJ (Ingest Judgment)
  Good looks like: 100% of records carry the five fields; 0 duplicates remain;
    field assertions passed; the run clears the trusted-run thresholds.
  Bad looks like:  Field assertions raise (board layout changed), or the run
    lands under 90% of the reported total.
  Response:        Hard stop for that source's downstream. An untrusted run
    freezes the closed-job logic — it may update "seen" timestamps, but it
    closes nothing. This is the most important gate: a bad run must not
    declare jobs dead.

--- LAYER 3: TOOL / AI PROCESSING ---

Step 3.1  Demand ranking
  Action:  Aggregate kept postings per company; rank by signal-role count;
           diff native IDs against the previous trusted run for new/gone.
  Model:   No LLM in the loop — deterministic rules + audit loop. (Deliberate:
           the differentiator is verifiability, and a model in this step would
           make claims uncheckable.)
  Output:  logs/reports/demand-YYYY-MM-DD.md (draft)
  TODO:    TODO: DEV — the new/gone diff currently runs by hand from the run
           files; script it so the conductor gets it automatically.

Step 3.2  Claim trace check
  Action:  Automated pass: every company claim in the draft must resolve to ≥1
           kept record with a live URL; any unlinked claim is removed or
           flagged before the gate.
  Output:  Same draft, trace-checked.
  TODO:    RESOLVED — the two-click trust test (brief Part 4, Step 3).

PHASE GATE 3 | Judgment type: TO (Tool Output Review)
  Good looks like: Every kept posting names its rule and matched words; every
    rejected posting names its reason; the ranking links each claim to signal
    roles; the diff compares native IDs across two trusted runs.
  Bad looks like:  A rule keeps postings at ~1-in-10 precision, or a claim
    appears with no raw link behind it.
  Response:        Flag for review, then fix and re-audit. An unlinked claim
    is a hard stop until traced or removed.

--- LAYER 4: logs/reports/ → USER ---

Step 4.1  Report delivery
  Action:  Render the final demand report (companies, signal roles, what's new
           this month, stated limits); commit it under logs/reports/.
  Output:  logs/reports/demand-YYYY-MM-DD.md
  TODO:    TODO: REPORT FIELD — the "what's new this month" section needs a
           human label for the top-line takeaway before it is user-facing
           (e.g. "Figma is staffing education faster than any watched
           company").

Step 4.2  Run log
  Action:  Append fetch counts, keep/reject counts, gate outcomes, and any
           flags to the run log.
  Output:  logs/reports/run-log.md (append)

PHASE GATE 4 | Judgment type: TO (Tool Output Review)
  Good looks like: A non-technical reader answers "which companies, what
    roles, what's new" from page one; every number recomputable from committed
    files; limits stated, not hidden.
  Bad looks like:  Numbers that can't be recomputed, or an unreadable company
    presented as "no demand."
  Response:        Flag for review — a human reads the report before it ships.

--- CONDUCTOR NOTE ---

Watch the calendar, not just the counts. Boards are quieter on weekends and
Mondays — a thin Monday run is usually calendar, not signal; compare against
the source-reported total for that day, never against last week's number
alone. And when a company you expected to see goes silent, check whether the
board moved (Greenhouse → Ashby migrations happen) before reading it as lost
interest: absence from the data is a measurement gap until proven otherwise.
The recipe cannot tell the difference — you can, by opening the board.

--- OPEN TODOs ---
  TODO: DATA SOURCE   Wire up more SmartRecruiters boards (or accept a
                      two-source recipe) — 10 verified records is below the bar.
  TODO: DEFINE        Confirm the trusted-run thresholds (≥90% / ≥70%) after
                      two more weekly runs.
  TODO: DEV           Script the new/gone native-ID diff (currently by hand).
  TODO: APPROVE       Human approves the final demand report before it ships
                      (Phase Gate 4) — the conductor stops here every run.
  TODO: REPORT FIELD  Human writes the top-line "what's new" takeaway label.

--- APPENDIX: STANDARDIZATION (per recipes/cowork_recipe_standardize.md) ---

## Phase-gate test commands

1. Gate 1 — Ingest complete: every source folder under data/raw/<source>/
   holds one dated JSON per watched board; fetch counts logged next to
   source-reported totals.
   Test: `ls data/raw/*/[0-9]*/ | wc -l` equals the watched-board count (18),
   and no board file is empty.
   Human capacity: [IJ].
2. Gate 2 — GIGO gate: all five fields present on 100% of records; zero
   duplicates on source+native ID; trusted-run thresholds cleared.
   Test: `python3 -c "import json,glob; rs=[r for f in glob.glob('data/verified/*/*.json') for r in json.load(open(f))['records']]; assert all(all(k in r for k in ('title','url','date_posted','location','department')) for r in rs); assert len({(r['source'],r['source_id']) for r in rs})==len(rs); print(len(rs),'records, 0 dupes')"`
   Human capacity: [IJ].
3. Gate 3 — Intelligence traceable: every kept record carries kept_because +
   matched_words; every company claim in the draft resolves to a kept record.
   Test: grep the draft report for `](http` — claim count equals link count;
   any claim without a link fails the gate.
   Human capacity: [TO].
4. Gate 4 — Report shippable: page one answers which companies / what roles /
   what's new; every number recomputable from committed files.
   Test: pick any number in the report at random and recompute it from the
   committed run files in under five minutes; if you cannot, the gate fails.
   Human capacity: [TO].

## Output contract

### Agent output
File: `logs/lectern-[DATE].json`
Fields: workflow, run_id, mode, steps_completed, records_seen, rejects,
duplicates, flags, stop_conditions, generated_at, plus per-source
fetch_counts and the trusted_run verdict (true/false with the two threshold
comparisons).

### Human report
File: `logs/reports/demand-[DATE].md`
Reader: the independent AI-education consultant (Part 2 user).
Decision enabled: which companies to approach about unposted education work,
and with what timing evidence.
Sections: ranked company list; signal roles per company (title, link, rule
fired); new/gone vs previous trusted run; stated limits.

## Stop conditions

- Stop if any source's field assertions raise (board layout changed) — the
  conductor fixes the assertions before that source continues; other sources
  are unaffected.
- Stop if the run falls below the trusted-run thresholds — the closed-job
  logic freezes; nothing is declared dead on an untrusted run.
- Stop if a demand claim has no raw link — remove or trace it before the
  report ships.
- Stop at Phase Gate 4 every run — the report never ships without human
  approval.

## Snickerdoodle

Full dialogic run: `snickerdoodle run lectern --mode dialogic`
Sample mode (no live network calls, no writes):
`snickerdoodle run lectern --mode dialogic --sample`
Step: `snickerdoodle run lectern --step ingest-greenhouse --sample --no-write`
Gate: `snickerdoodle gate lectern --gate 2 --decision approve --note "..."`
