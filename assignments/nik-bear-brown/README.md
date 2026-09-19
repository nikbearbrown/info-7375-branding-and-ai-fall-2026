# Nik Bear Brown — doing the assignments alongside the class

## Executive summary

**What this is.** The instructor's own copy of the Fall 2026 *Branding and AI* assignments, done for real. I teach this course; this folder is where I do the same work I ask of students, on the same deadlines, with the same rubric — except the job I am hunting is not a first job, it is a **Developer / Designer Advocate or technical educator role I could hold while remaining a professor**: remote, part-time, consulting, or educational-material work at a design-tool or AI company.

**Why read it.** If you are a student: this is what a finished, honest submission looks like, including the parts that went wrong (a scraper that flagged 51 of 51 jobs, a board with no roles in my geography, a dream job that turned out not to be the best fit once I looked wider). If you are a hiring manager who followed a link here: this is my working portfolio for advocate roles — the search, the reasoning, and the materials, in the open. If you are me: this is the to-do list.

**Where it stands (September 19, 2026).** Assignment 2 Part 1 is done and pushed; Parts 2–4 (gap analysis, PRD, architecture) are next. The advocate search has covered seven companies and found six roles worth keeping; the portfolio folder holds the target list and will grow the materials that answer each posting.

---

## The folders

| Folder | What it is | Status |
|---|---|---|
| [`assignment-2/`](assignment-2/) | **Assignment 2 — "Plan Your Madison Project Like a Pro."** Part 1 finds a real job I could apply to in 6–12 months and names the three requirements I will be measured against. My pick: **Designer Advocate at Figma**. The appendix runs the same search on seven companies and three applicant-tracking systems and explains why "Educator" turned out to be the better search word. `evidence/` holds the machine reports the pick was made from — the ranked match list, the run record, the matching rules, and the keep list — with no résumé data. | Part 1 done · Parts 2–4 (gap table, PRD, agents + n8n MVP) pending |
| [`advocate/`](advocate/) | **The advocate-job portfolio.** The cross-company target list (`advocate-roles-2026-09-19.md` — six roles at four companies, only one US-remote), one keep list per company with my reason for each role, and — as they are built — the materials each posting asks for: on-camera samples, a Figma design-systems piece, written and video tutorials, a speaking reel. Everything here is meant to be linkable from an application. | Target list done · materials starting |
| `brutalist-figma-claude/` | **The Figma portfolio piece: a practitioner book,** *The Figma API: From Canvas to Production* — how to make a Figma file the machine-readable source of truth for a design system, audited programmatically, tokens extracted, connected to an AI coding agent over MCP. It is its own repository — `github.com/nikbearbrown/brutalist-figma-claude`, **private for now** (the link will not open for you until it is published), checked out here for convenience and **ignored by this repo's git** — do not commit it from here. It is the "shipped a design system in Figma" gap from Assignment 2 being closed in public. | In progress (13 chapters scaffolded; see its BLUEPRINT.md) |

## How the search works (once, so each folder does not repeat it)

Every posting in these folders was found by the reallocation engine's `greenhouse-watch` skill — a stored script that fetches one company's public job feed (Greenhouse, Ashby, or SmartRecruiters), matches each posting against a JSON version of my CV with a written rule set, and writes a ranked list with the exact words that matched. The list is a filter for my reading, not a judgment; every "keep" in these folders is mine, with the reason written under the card. The engine, the rules, and the per-company reports live at [github.com/nikbearbrown/the-reallocation-engine](https://github.com/nikbearbrown/the-reallocation-engine) under `reports/greenhouse-watch/`. My CV JSON stays local and is never committed anywhere.

## Rules this folder follows

- **Real, not staged.** Real postings, real gaps, real disappointments. Nothing is invented to make the example cleaner.
- **Executive summary first.** Every Markdown file here opens with what it is, why to read it, and what it found — before any table or technical detail.
- **No personal data in git.** Public-CV facts only. The résumé JSON, phone, and address never enter a tracked path.
- **The human decides.** Machines rank words; I pick. Where a file says "TENTATIVE," I have not read the postings yet.
