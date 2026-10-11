# Assignment 5A, Part 2 — User Testing (25 pts)

## Status: protocol ready, sessions TODO

No test sessions have been run. Nothing below invents testers, quotes, or
findings — the brief warns that faked tests are detectable, and this repo does
not carry invented interviews. Run three real sessions with this protocol,
then fill in the templates.

## Who to recruit

The Part 2 user (Conductor Brief): the **independent AI-education consultant**
— someone who sells training, enablement, or teaching-related advisory work to
companies or universities, and who decides where to pitch based on evidence of
interest. Closest matches in Bear's world, in order:

1. An independent consultant who sells AI training/enablement to orgs.
2. A DevRel / education / customer-education lead at an ed-tech or AI company
   (adjacent: they read hiring boards the same way, but from inside).
3. A university teaching-center staffer who vets vendor partnerships.

Per the brief's FAQ: recruit the closest match you can find, run the test, and
**note the gap** in the report. Do not use classmates. Do not use yourself.

## The protocol (verbatim script)

Remote is fine — video call with screen share. Send the URL, then say only:

> "This is a tool I built. I would like to watch you use it and hear your thinking."

- Ask them to **think aloud** as they use it.
- Take notes on where they **pause**, what they **re-read**, what they **ask**.
- Give them one task: *"Pick a company you have an opinion about and decide
  whether they're worth approaching, using only what the tool shows you."*
- At the end, ask exactly:
  1. What did this help you do?
  2. What confused you?
  3. Would you use this again? Why or why not?
- **Do not defend the interface. Listen.** Confusion is data.

## Note template (one per tester)

```markdown
### Tester N
- **Role and background:** [job title + context — why they match (or how far off) the Part 2 user]
- **What they did:** [in order — what actually happened, not what was expected]
- **Where they paused or got confused:** [specific moments, specific inputs/outputs]
- **What they said at the end:** [direct quote or close paraphrase — Q1/Q2/Q3 answers]
```

## What you changed (fill after sessions)

```markdown
- **Change 1:** [what changed] — [which tester feedback drove it]
- **Change 2 (decided NOT to change):** [what was kept] — [why the line was held]
```

Grading note from the brief, kept visible: the score is for running a real
test, listening, and making a real decision — not for testers loving the tool.
Genuine confusion + a reasoned hold-the-line outscores three polite thumbs-ups.

## Candidate things to watch for (hypotheses, not findings)

These are guesses to check in testing, recorded so the test can prove them
wrong — not conclusions:

- Does "kept because: *role word in title*" read as transparency or as jargon?
- Does the 2026-09-26 run date make the data feel stale, and does the user ask
  for a refresh before trusting it?
- Does the per-company dropdown match how they think, or do they want to
  compare companies side by side?
