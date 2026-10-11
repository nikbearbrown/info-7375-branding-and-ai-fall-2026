# Assignment 5A — Interface, User Testing, and Market Positioning (Path A)

**Due:** October 23, 2026, 11:59 PM · **Points:** 100 · **Submit:** `LastName_FirstName_A5A_WrapYourTool.pdf`

## Status (2026-10-11)

| Piece | State |
|---|---|
| Gradio interface (`app.py` + `lectern_app_data.json`) | ✅ Built and logic-tested locally (real data, real outputs) |
| Public deployment URL | ⬜ TODO — needs Bear's Hugging Face or Streamlit account |
| Interface walkthrough | ✅ Drafted (`part-1-interface.md`) |
| Three screenshots | ⏳ Verifying via local run; re-capture on the public URL for the PDF |
| Three user test sessions | ⬜ TODO — needs three real humans (protocol ready in `part-2-user-testing.md`) |
| Positioning matrix | ✅ Drafted (`part-3-positioning.md`) |
| Revised one-thing | ⬜ Drafted as provisional — can only be finalized after real user tests |

## Files

- `app.py` — the working Gradio interface. Run: `python3 app.py` → http://127.0.0.1:7860
- `lectern_app_data.json` — compact extract (97 kept postings, 2026-09-26 run) the app reads.
  Full file: `assignment-3/jobs-of-interest-2026-09-26.json`.
- `part-1-interface.md` — walkthrough (URL, fields, output, design decision, error handling).
- `part-2-user-testing.md` — test protocol, note template, tester criteria. Sessions are TODO.
- `part-3-positioning.md` — 2×2 matrix, placements, white space, revised one-thing (provisional).

## What this wraps

Assignments 1–5 built Lectern, the demand-signal reader: it watches the hiring
boards of companies selling AI to universities and keeps the postings that are
evidence of interest in teaching (Assignment 3's collector, Assignment 4's
intelligence). Assignment 5A puts a usable front end on it for the Part 2 user —
the independent AI-education consultant from the Conductor Brief — and tests
whether the strategy survived contact with real users.

## For Bear (the TODOs only you can do)

1. **Deploy** `app.py` to Hugging Face Spaces or Streamlit Community Cloud and
   paste the public URL into `part-1-interface.md`.
2. **Run three user tests** with the protocol in `part-2-user-testing.md`
   (not classmates, not yourself — closest match to the Part 2 user, noting the gap).
3. **Re-capture the three screenshots** on the public URL for the submission PDF.
4. **Finalize the revised one-thing** in `part-3-positioning.md` from what the tests reveal.
5. **Generate the PDF** as `Brown_Nik_A5A_WrapYourTool.pdf` and submit on Canvas.

Nothing here invents user feedback. Every test-shaped section is a labeled
template until real sessions happen — the brief is explicit that faked tests
are detectable, and the repo rule is explicit that invented interviews stay out.
