# Verification of the shipped candidate — Assignment 3

**Nothing has been verified yet.** This file is the plan for the checks, with the acceptance criteria fixed **before** anything is rendered, as the assignment requires. Every field below is filled in from an actual run, never from an expectation.

**Candidate version or content identifier:** _pending — the commit hash of the shipped specimen goes here and in Canvas._

**Input sources and fixture/simulation/live labels:** `tokens.json` (input, written by hand); the specimen is generated output. No live service is involved, so there is nothing to label live.

**Environment and exact commands:** _pending — `python3 generate_specimen.py …` and the test command, recorded as actually run, with the Python version._

**Acceptance criteria fixed before checking:**
1. The generator reproduces `specimen.svg` byte-identically from `tokens.json` on a second run.
2. Every token in `tokens.json` appears in the specimen; nothing in the specimen is hard-coded.
3. Malformed hex (`#GGG`, `red`, empty), zero and negative sizes, and a missing required key each **fail loudly** with a message naming the offending token — not a silent default.
4. No text clips its box and no two text levels collide, checked by eye on the rendered SVG.
5. Contrast ratios computed for every foreground/background pair actually used, reported as numbers.

**Expected result from independent source or calculation:** Contrast computed by hand for at least two pairs using the WCAG relative-luminance formula, and compared against the script's numbers — the script checking itself is not a check.

**Observed result and evidence path:** _pending._

**Checks that failed and subsequent revision:** _pending. A finite passing suite is evidence only about those probes — if nothing fails, that is reported as a possibly weak suite, not as a clean bill._

**Shared assumptions or possible common errors:** The generator and its tests were written in the same session, likely by the same agent, so they can share a wrong assumption about what the tokens mean. The hand-computed contrast pairs exist to break that.

**Remaining limits:** Contrast arithmetic and my own reading of one SVG are not an accessibility audit; no screen reader, no colour-vision simulation, no user testing. Nothing here certifies accessibility.

**Actual reviewer or automated checker:** _pending — name who or what actually ran the checks._

**Final handoff decision and owner:** _pending — Professor Bear._

Put the final Git commit hash in Canvas after committing this file. Do not invent a human signature or claim checks that were not run.
