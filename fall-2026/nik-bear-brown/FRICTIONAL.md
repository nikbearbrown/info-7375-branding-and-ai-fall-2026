# FRICTIONAL — Professor Bear's process log

## Executive summary

**What this is.** The honest process log for the work in this folder, written the way the course asks students to write theirs: what was tried, what went wrong, what changed, and who did what — the human or the AI.

**Why read it.** It is a real example of the log, not a constructed one. It shows the instructor's own work run through the same record students keep, including the parts that did not go smoothly.

**What it records so far.** One session, 2026-09-26, during a live class demo: setting this folder up, bringing the Figma dream-job recipe over from the Prompt Engineering class, and consolidating everything of the instructor's into this one folder. No Assignment 3 work has started yet — that folder is a place to work, not a result. Two findings were about the repository rather than the assignment: `fall-2026/` was blocked by a `.gitignore` rule, so anything put there would have pushed nothing with no error; and the instructor's work existed in two places at once, which is not how the other two classes are laid out.

Every push to GitHub is listed at the bottom with its date and commit note.

---

## Entries

### 2026-09-26 — Setting up the Fall 2026 submission folder for a live class demo

- **Date and what I was working on:** Picking up the Figma advocate thread from last week, then setting up the folder the class demo would push to.

- **I tried / expected:** I asked where we were, and said: *"I think we were working on looking at developer advocate positions at Figma. And related companies."* I expected to find my own subfolder already on GitHub. Then: *"While you're looking, see if there's a frictional log on the uh, GitHub. I want to create a new folder on the GitHub under the Nick Bear Brown subfolder. Called assignment three."*

- **What happened:**
  - **Last week's work was all pushed.** The Figma advocate search (seven company job boards, three applicant-tracking systems) is on GitHub in this repo under `assignments/nik-bear-brown/`, and the machinery is in the Reallocation Engine. Nothing was left dangling.
  - **There was no Frictional log for this course's example work.** This repo has the `frictional/` teaching module and a blank `templates/FRICTIONAL.md`, but no filled log for my own work. The Prompt Engineering and Computational Skepticism repos each have one; this one did not. So the honest answer to "is there a frictional log on the GitHub" was: for the other two classes yes, for this class no.
  - **My work was in the wrong folder.** I looked at `https://github.com/nikbearbrown/info-7375-branding-and-ai-fall-2026/tree/main/fall-2026` and said: *"I don't see uh, either my name Nick Bear Brown or uh, [assignment] Three subfolder there. Create one."* The Assignment 2 work had been put under `assignments/nik-bear-brown/`, which is not where the course tells students to submit. The course's own instruction, in `fall-2026/README.md`, is `fall-2026/first-name-last-initial/assignment-XX/`.
  - **`.gitignore` would have silently swallowed the demo.** The rule `/fall-2026/*` ignores everything in `fall-2026/` except its README. Anything created there for the live demo would have been invisible to `git add` with no error — the class would have watched a push that contained nothing.

- **What I did:**
  - Pointed at the Computational Skepticism repo's `fall-2026/nik-bear-brown` as the model: *"look at this as a model how to set up subfolders and frictional logs."*
  - Said where the demo runs: *"I'm doing a live demo in class and this is the folder we're going to push to and work in,"* and how the folder is named: *"nik-bear-brown My subfolder should be named like this."*
  - Had the `.gitignore` rule added that makes this one folder public (`!/fall-2026/nik-bear-brown/`), matching the line the Computational Skepticism repo already uses. Student folders under `fall-2026/` stay untracked.
  - Created `fall-2026/nik-bear-brown/` with the three files the model folder has — `README.md`, `CLAUDE.md`, `FRICTIONAL.md` — and an empty `assignment-3/` to work in.
  - Decided what Assignment 3 is for beyond the grade: the visual identity system closes the exact gap Assignment 2 found in my own CV against the Figma Designer Advocate posting — *never shipped a design system with tokens*. The tokens file and specimen become portfolio evidence, not a throwaway.

- **What Claude or another person contributed:** Claude Code (Opus 5) checked that last week's commits were pushed, searched both repos for a Frictional log and reported that this one had none, found the `.gitignore` rule that would have blocked the demo folder, read the Computational Skepticism folder as the model, and wrote this folder's README, CLAUDE.md, and the first draft of this entry. I decided the location, the folder name, the model to copy, and that the demo happens here. I have not yet reviewed the Assignment 3 plan, and no Assignment 3 work exists yet.

- **What I understand now / still do not understand:** A submission folder is not a place until `.gitignore` agrees it exists — worth saying out loud in class, because a student who creates `fall-2026/their-name/` in a repo with that rule will push nothing and see no error. Still open: whether to move the Assignment 2 and advocate work from `assignments/nik-bear-brown/` into this folder so everything sits in one place, or leave it and link. Also still open: which running brand Assignment 3's palette and type serve, since that decision comes from Assignment 2's positioning.

- **Evidence and next step:** This folder — `README.md`, `CLAUDE.md`, `assignment-3/` — and the `.gitignore` line that tracks it. Last week's evidence is in `assignments/nik-bear-brown/assignment-2/evidence/` and the engine's `reports/greenhouse-watch/`. Next: the Assignment 3 creative brief and `tokens.json`, built live.

### 2026-09-26 (same session, continued) — Bringing the Figma recipe over from Prompt Engineering, and one folder instead of two

- **Date and what I was working on:** After the first push went live, moving the Figma dream-job work into this class and fixing the folder layout.

- **I tried / expected:** I said: *"copy [the Prompt Engineering fall-2026/nik-bear-brown folder]. We're going to build on the Figma from the other. That's also being done in other class. So it took it the look at this particular folder here and copy it over to branding and AI."* And, so the class could watch: *"When you have something to push to the branding and AI folder, push it. I want to show it while you are working on other things."*

- **What happened:**
  - **The recipe was written in the wrong class.** The Prompt Engineering folder holds an eight-step dream-job recipe whose steps are explicitly mapped onto **Assignment 2, "Plan Your Madison Project Like a Pro"** — which is *this* course's assignment, not that one's. Copying it here puts it where it is graded.
  - **The two folders disagree about which posting to pick.** The recipe suggests **Designer Advocate, Partnerships** (the only Figma role that builds certification and enablement programs and appears at workshops). Last week's write-up picked the **Designer Advocate** US-hubs posting and kept Partnerships as "consider." Both judgments are defensible. The disagreement is now stated in the README instead of one quietly overwriting the other; I have not picked yet.
  - **I thought the folder name was wrong.** I said: *"Looks like you misspelled my name… Look at how it's spelled. And the other directories… you also missed it for twenty twenty-six as fall two two six. Look at the other directories for the proper naming… The same thing is being done both in the computational skepticism class and in the prompt engineering class."* Checked against GitHub: the live folder is `fall-2026/nik-bear-brown/`, character for character the same as the other two repos. The spelling and the year were right.
  - **What was actually wrong was that there were two of them.** This repo had `assignments/nik-bear-brown/` *and* `fall-2026/nik-bear-brown/`. Neither of the other two classes has an `assignments/<name>/` folder at all. Two folders with my name is what I was looking at.

- **What I did:**
  - Copied `figma/`, `facts/`, and `greenhouse-watch-demo/` from the Prompt Engineering folder into this one, unchanged.
  - Rewrote this folder's README around the eight-step recipe, with Assignment 2's four parts mapped to the steps that feed them, and the two candidate picks side by side.
  - Added the Prompt Engineering folder's standing rules to `CLAUDE.md`: every value labeled record / judgment / your input, every JSON file indented so students can read it on GitHub, saved boards and run output never hand-edited, and the facts file attested with a date.
  - **Moved `assignment-2/` and `advocate/` here with `git mv`**, moved the Figma book repo with them, deleted the old `assignments/nik-bear-brown/`, and rewrote every link that pointed at the old location. One folder now, like the other two classes.

- **What Claude or another person contributed:** Claude Code did the copy, the README rewrite, the move, and the link fixes, and checked the live GitHub tree to establish that the folder name was already correct rather than agreeing with me. I gave the direction: copy the Prompt Engineering folder, push as you go, and make the naming match the other classes.

- **What I understand now / still do not understand:** The naming was fine; the duplication was the bug, and it was mine — last week's work went into `assignments/` before this folder existed. Resolved: everything of mine is in `fall-2026/nik-bear-brown/`. Still open: which of the two Figma postings is the submission's dream job, the "why this role" sentence, and whether the six-company sweep gets refolded into this folder's per-company shape.

- **Also in this session — the standard submission files.** I asked for *"all of the standard readmes and frictional logs, the other ones have in that as well."* The course's own brief names them, and `templates/` holds blanks for them, so `assignment-3/` now carries `PREDICTIONS.md`, `VERIFICATION.md`, `CONTRIBUTIONS.md`, and its own `FRICTIONAL.md` alongside the README. The prediction (a contrast failure at the smallest caption size on a mid-tone background) and the acceptance criteria are both written **before** anything has been rendered, which is the order the assignment is actually testing. A copied blank template is not evidence, so each one is filled in with what is true today — including "not run yet" where that is the truth. I have not reviewed the drafted prediction.

- **Evidence and next step:** `figma/`, `facts/`, `greenhouse-watch-demo/`, `assignment-2/`, `advocate/`, and `assignment-3/` with its four records, in this folder; the README's recipe and mapping table. Next: pick one of the two Figma postings, then the Assignment 3 creative brief and `tokens.json`.

### 2026-09-26 — This folder stopped being a place to edit shared code

- **Date and what I was working on:** Keeping one live-coded project consistent across three classes.

- **I tried / expected:** I expected the three `nik-bear-brown` folders to be roughly the same.

- **What happened:** They had drifted. Branding had the collector, the watch list, the filter, and the ATS notes; Prompt Engineering had the CV facts and the earlier iterations but not the collector; Computational Skepticism had neither. I named **Computational Skepticism the canonical master**, which meant the master was the folder furthest behind at the moment it was declared.

- **What I did:** The shared spine now lives in the master and is copied here by its `lectern/sync.sh`. This folder gained a `SYNC.md` saying it is **not** the master, and a Rule 0 in `CLAUDE.md` saying the same. The files that are copies are named there. Everything specific to this class — this log, the README, the assignment folders, the dated run outputs — is never copied in either direction, because a log overwritten by another class's log is a destroyed record.

- **What Claude or another person contributed:** Claude Code (Opus 5) inventoried and diffed the three folders, built the sync script, and wrote the notes. I decided which class is master.

- **What I understand now / still do not understand:** Drift is invisible until something diffs it. Still open: the recovery path — a shared file edited in the wrong repo — has not been exercised.

- **Evidence and next step:** `SYNC.md` here, and `./lectern/sync.sh --check` in the master reporting all three in sync.

### 2026-09-26 — Reading the rejects: the audit found a false-positive problem instead

- **Date and what I was working on:** The one check left in my own acceptance criteria. 3,358 postings were rejected in the 2026-09-26 run and nobody had looked at what the filter threw away. I asked for a random sample: *"Give me a hundred or two hundred of the three thousand three hundred postings. Uh, as a random sample. So I can take a quick look at them to see what's being missed."*

- **I tried / expected:** I expected to read 100 rejects and find a handful of missed teaching roles — false negatives.

- **What happened:** The sample has not been read yet. But building it exposed two things first, and the second one is not what I was looking for.

  - **`education` is in 618 of 618 Anthropic postings.** Every Anthropic ad ends with *"Minimum education: Bachelor's degree or an equivalent combination of education, training, and/or experience."* So the topic word carries no information on that board — the same boilerplate problem already found on Writer's board, and most of the reason **950 rejects matched exactly one teaching word**: the word was `education`, in a salary footer.
  - **The topic-word rule is keeping recruiters, not teachers.** 79 of the 88 kept records were kept on a role word in the title. The other 9 were kept on topic words alone, and on inspection most are wrong: three Stripe **University Recruiter** postings, Notion's **Head of Early Career Recruiting**, OpenAI's **Integrated Marketing Manager, Youth Culture**. `university`, `campus`, and `student` are recruiting vocabulary as much as teaching vocabulary. Only Anthropic's **Head of Technical Training** is a clear true positive in that group.

  So an audit aimed at false negatives found a **false-positive** problem instead, in the part of the rule I had paid least attention to.

- **What I did:** Had `lectern/audit_rejects.py` written as a stored script rather than an ad-hoc query, so the sample is reproducible: seed `20260926` recorded in the output, and rerunning reproduces the same 100 rows. Two parts on purpose — a uniform random 100 (the only part that supports a rate: k MISSes means about k × 34 across all rejects) and all 63 of the closest calls, the rejects that matched two teaching words against a bar of three. The 950 one-word rejects are counted, not listed.

  Both findings are written into the sample file as calls for me to make. **Neither has been changed in `keywords.json`** — adding `education` to Anthropic's ignore list would move the flagship company's counts, and demoting `university`/`campus`/`student` would move the kept total, so both are mine to decide rather than something to quietly fix.

- **What Claude or another person contributed:** Claude Code (Opus 5) wrote the sampler, drew the sample, and found both problems while checking the snippets. It also stopped its first attempt: the near-miss tier was 1,013 postings, well past the 100–200 I asked for, so Part 2 was narrowed to the 63 closest calls. It did not change the filter, and it did not mark a verdict on any row — the Verdict column is empty and mine.

- **What I understand now / still do not understand:** The reason to read rejects is not only to find what was missed. Reading them showed what boilerplate looks like from the other side, and that led straight to a false-positive class I would not have found by looking at the 88 keeps. Still open: the actual reading, the two calls above, and whether `university`/`campus`/`student` should require pairing with a real teaching word before they count.

- **Evidence and next step:** `reject-audit-2026-09-26.md` — 100 random rows plus 63 closest calls, Verdict column blank; `lectern/audit_rejects.py` in the master, synced to both other classes. Next: read it, mark the MISSes, multiply, and decide the two calls.

---

## GitHub pushes

One line per push to GitHub: the date and the commit note. The commit ID for each push is in `git log`; a commit can't contain its own ID.

| Date | GitHub note |
|---|---|
| 2026-09-26 | feat(fall-2026): add Professor Bear's folder with Frictional log and assignment-3 |
| 2026-09-26 | feat(fall-2026): bring the Figma dream-job recipe into this class and put all my work in one folder |
| 2026-09-26 | feat(fall-2026): add the standard submission records to assignment-3 (predictions and acceptance criteria before any output) |
| 2026-09-26 | feat(fall-2026): rewrite assignment-3 for the live data-pipeline brief and add the Lectern SDD |
| 2026-09-26 | feat(fall-2026): build Lectern, watch 13 boards across 3 ATSs, publish all 2347 postings and the 69 kept |
| 2026-09-26 | feat(fall-2026): add the advocacy-title companies, cut a keyword that measured as noise |
| 2026-09-26 | docs(fall-2026): note that shared code is canonical in the Computational Skepticism folder |
| 2026-09-26 | feat(fall-2026): add the advocacy-title companies, cut a keyword that measured as noise |
| | ↑ **the row above is the subject this commit actually carries.** The subject intended for it was *"feat(fall-2026): reject audit sample (100 random + 63 closest calls) with two findings to rule on"*; a scripting error reused an earlier commit's subject line. The content is correct; history was not rewritten to fix a label. |
