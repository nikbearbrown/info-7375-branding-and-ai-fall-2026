# FRICTIONAL — Professor Bear's process log

## Executive summary

**What this is.** The honest process log for the work in this folder, written the way the course asks students to write theirs: what was tried, what went wrong, what changed, and who did what — the human or the AI.

**Why read it.** It is a real example of the log, not a constructed one. It shows the instructor's own work run through the same record students keep, including the parts that did not go smoothly.

**What it records so far.** One session, 2026-09-26: setting this folder up for a live class demo. The Assignment 3 work itself has not started — the folder is a place to work, not a result yet. The session's finding was about the repository, not the assignment: the instructor's earlier Assignment 2 work was in the wrong place (`assignments/nik-bear-brown/`), and `fall-2026/` was blocked by a `.gitignore` rule, so nothing put there would ever have reached GitHub.

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

---

## GitHub pushes

One line per push to GitHub: the date and the commit note. The commit ID for each push is in `git log`; a commit can't contain its own ID.

| Date | GitHub note |
|---|---|
| 2026-09-26 | feat(fall-2026): add Professor Bear's folder with Frictional log and assignment-3 |
