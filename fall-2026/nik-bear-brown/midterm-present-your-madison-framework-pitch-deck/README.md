# Midterm — Present Your Madison Framework (Pitch Deck)

## Executive summary

**What this is.** A first draft of the Canvas midterm (100 points): the outline, speaker notes and timing for a 10-slide, 8-minute video pitch to non-technical investors, with a PDF of the slides.

**Why read it.** The content slides (problem, solution, proof of concept) can be drafted from the real project. The **business model, go-to-market and the ask are the hard part**: the tool exists to serve one person's job search, so any revenue story is a hypothesis, and this draft says so on the slide instead of presenting invented numbers.

**What it found.** Two things about the Canvas text. Its dates are leftovers from a summer term (it says July 10, 2026, mentions July 3–4 holidays, and tells students to send the video by July 10); Canvas itself shows October 30. And "non-technical investors" is a harder audience than the tool was built for.

| | |
|---|---|
| **Due** | Canvas shows October 30, 2026; the brief's own text says July 10. Unpublished. |
| **Points** | 100 (delivery 30 · problem/solution 15 · business viability 15 · proof of concept 10 · presentation 10 · excellence 20) |
| **Rules** | Max 10 slides, 8 minutes, 30-point minimum font; face on camera at some point |
| **Submit** | `YourName_MadisonPitch.mp4` (or a shared link) and `YourName_MadisonPitch.pdf` |
| **State** | DRAFT outline. No slides, no recording. Judgment unless marked record. |

---

## The 10 slides (target timings from the brief)

| # | Slide | Time | Draft content |
|---|---|---:|---|
| 1 | Title | 15 s | **Lectern** `[TODO: DEFINE]` (final name from Assignment 7). "Find the companies that pay for teaching." Professor Bear. |
| 2 | Problem | 75 s | Companies hire people to teach their products, but those jobs are scattered across dozens of company websites and rarely offer flexible terms. Checking by hand is slow and gets skipped. Cost: a missed role, and about an hour a week by his untimed estimate. `[TODO: DEFINE]` any cited market figure; none is used here. |
| 3 | Solution | 75 s | "It watches eighteen company job boards for you and tells you which companies are serious about teaching, and why." No jargon: not "API", not "ATS." |
| 4 | The magic, simplified | 45 s | "We read every job posting, keep the ones about teaching, and show you the reason for each." (No language model is in the loop today: `../scale-your-thing-and-add-intelligence/` describes the "intelligence" as a classifier, a ranker and audits. Do not say the tool uses AI in the chatbot sense. `[TODO: DEFINE]`) |
| 5 | Business model | 50 s | **Hypothesis, not data.** Options to test: a subscription for educators and career centers; a paid company-ranking report for university career offices; free for individuals. `[TODO: DEFINE]` he picks; no revenue projection is made because none is supportable. |
| 6 | Go-to-market | 50 s | First ten users: faculty and instructors he already knows who teach with these tools; career offices. `[TODO: DEFINE]` real names stay private. |
| 7 | Competition | 45 s | Job boards and alerts show postings; none shows why a posting matched or ranks companies. Source: `../the-conductor-brief/conductor-brief.md`, whose competitor notes are web research with first-hand trials still owed. Do not present them as tested. |
| 8 | Development plan | 40 s | Status: **working prototype of the data half** (collector and audits ran on 2026-09-26). Still to do, per the sibling folders: deploy the interface (`../wrap-your-tool/`, built locally, no public URL yet) and run real user tests. `[TODO: DEFINE]` dates. |
| 9 | Proof of concept | 75 s | Show the real files: 18 boards → 3,446 postings → 97 kept; the company ranking where Anthropic shows five kinds of evidence; the Replit one-word miss. All record. |
| 10 | The ask | 30 s | `[TODO: DEFINE]` what he needs — introductions to education and advocacy teams, early users, a design partner. |

**Total:** the brief's own timings (15+75+75+45+50+50+45+40+75+30) add up to 500 seconds, 8:20, which is **20 seconds over its own 8-minute cap.** Trim slide 2 and slide 3 by 10 seconds each.

## Translation guide applied

| Instead of | Say |
|---|---|
| job-board API | "the company's public hiring page" |
| keyword filter | "reads the posting for teaching work" |
| phase gates, audit | "checks its own work and shows you" |

## Production

- **Low effort:** Zoom screen-share with the PDF, camera on.
- **Quality points:** a polished video tool; his film toolkit (not part of this repo) could produce it, which is a choice, not a requirement. `[TODO: DEFINE]`
- Test on a non-technical listener; zero jargon. Slides at 30 pt or larger.

## Pre-submission checklist (from the brief)

☐ Recording under 8:00 · ☐ zero jargon · ☐ proof of concept visible · ☐ problem in the first minute · ☐ business model explained · ☐ specific ask · ☐ face visible · ☐ audio tested · ☐ PDF exported · ☐ file names correct.

## What is still his

1. Slides, recording and the PDF.
2. Every business decision on slides 5, 6 and 10.
3. Whether the investor framing fits a tool built for a job search.
