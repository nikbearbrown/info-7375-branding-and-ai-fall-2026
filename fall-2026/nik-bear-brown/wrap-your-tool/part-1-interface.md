# Assignment 5A, Part 1 — The Interface (30 pts)

## Tool URL

- **Public URL:** TODO — deploy `app.py` to Hugging Face Spaces or Streamlit
  Community Cloud (needs Bear's account; the app is deployment-ready, single
  file + one JSON data file, no secrets).
- **Local:** `python3 app.py` → `http://127.0.0.1:7860` (verified working 2026-10-11).

## Interface walkthrough (300–400 words)

The interface wraps the Lectern demand data — the 97 teaching-related postings
kept from the 2026-09-26 run of 3,446 — for the Part 2 user: the independent
AI-education consultant deciding which companies are worth approaching about
unposted work.

**Input fields.** *Company* — a dropdown of the 14 watched boards from the run
(Anthropic, Canva, Figma, GitLab, HubSpot, Netlify, Notion, OpenAI, Replit,
Stripe, Supabase, Vercel, Webflow, Writer). The user's decision is per-company
("is Figma showing real teaching interest?"), so the input is per-company too;
a dropdown, not free text, because the watch list is fixed and typos would
silently return nothing. *Filter by keyword (optional)* — a textbox matching
against posting titles (e.g. "education", "training", "advocate"). The user
thinks in role language, so the filter speaks role language.

**Output display.** A readable demand report, not a dataframe: the kept count,
each posting as a linked title with location, and — under each — the rule that
fired ("Kept because: *role word in title*", matched words listed). The format
is deliberate: the Conductor Brief's differentiator is *checkable* evidence,
so every claim links to the live ad and names its rule. A non-technical user
reads it like a briefing, not a query result.

**One design decision.** The per-posting "kept because" line. It would have
been simpler to show titles and links only, but the Part 2 user's whole job is
judging whether the evidence is real — hiding the rule would ask for trust the
tool hasn't earned. Showing the rule turns the output into something they can
argue with, which is exactly what the audit loop (Assignment 4) is for.

**Error handling.** Bad input gets plain English, never a traceback. Typing a
keyword that matches nothing returns: *"No matches for "zzzznothing" at Figma
— Figma has teaching-related postings in this run, but none with that word in
the title. Try a broader word (e.g. "education", "training"), or clear the box
to see everything we kept."* An empty company selection and a missing data
file each get their own plain-English message. All three states were verified
against the real app on 2026-10-11.

## Screenshots

Three states, all verified against the running app on 2026-10-11 (logic outputs
captured verbatim through direct calls; PNG captures are TODO on the public
URL — the brief requires screenshots of the *deployed* interface, so local
captures would be placeholders anyway):

**Screenshot 1 — Empty state.** The interface before any input: title, the
one-sentence framing ("Which companies selling AI to universities are showing
real interest in how their tools are used in teaching?"), the Company dropdown,
the keyword box, and the "Check demand signals" button. *Why it matters:* the
Part 2 user has never read the PRD — the page must explain itself, and the
test is whether they can complete a check without help.

**Screenshot 2 — Completed run.** Company = Figma, no keyword. Verified output
begins: "### Figma — demand signals (run of 2026-09-26)" / "**N
teaching-related posting(s) kept.**" followed by linked titles, locations, and
the rule fired per posting. *Where the output went:* rendered in-page as the
demand report; the underlying data stays in `lectern_app_data.json` (extract
of the real 2026-09-26 run file).

**Screenshot 3 — Error state.** Keyword = "zzzznothing". Verified output:
"### No matches for "zzzznothing" at Figma" — "Figma has teaching-related
postings in this run, but none with that word in the title. Try a broader word
(e.g. "education", "training"), or clear the box to see everything we kept
for Figma." Plain English, concrete next step, no traceback.

## Build notes (for the repo)

- Stack: Gradio (chosen over Streamlit — the UI is one form + one report, and
  Gradio's `gr.Markdown` output renders the evidence briefing natively).
- VM quirk, recorded so nobody re-discovers it: this machine's egress proxy
  env vars crash Gradio's httpx at import (`Invalid port: ':1]'` from the
  bracketed IPv6 entries in `NO_PROXY`, plus `ALL_PROXY` hijacking Gradio's
  localhost startup check). Launch with all eight proxy vars unset — the app
  only touches localhost and local files. Documented in `app.py`'s header.
- Data contract honored: inputs are the watched boards + a title filter (the
  Part 3 contract's sources and fields); outputs are the Part 4 evidence
  report. Nothing in the UI invents data — every posting links to its live ad.
