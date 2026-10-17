# Assignment 11 — Show Your Work: Substack as a Brand Platform

## Executive summary

**What this is.** A first draft of Canvas Assignment 11 (100 points): a Substack publication (name, tagline, About page), a brand-consistency audit, a 600–800 word thought-leadership article, a LinkedIn promotion post and a 300-word reflection.

**Why read it.** The publication copy and the article can be drafted from events on record. The audit needs screenshots of live pages that do not exist yet. The **reflection cannot be drafted**: it asks what he chose and what he would do differently, which only he knows.

**A decision to make first.** `[TODO: DEFINE]` He may already have Substack publications; this draft could not check. If so, this assignment may be answered with an existing publication instead of a new one. The brief wants a brand-aligned publication; `[TODO: DATA SOURCE]` nobody has checked what exists.

| | |
|---|---|
| **Due** | Canvas shows no date ("TBD"). Unpublished. |
| **Points** | 100 (Substack setup 10 · audit 10 · article 50 · promotion 10 · reflection 20) |
| **Path** | A (personal brand) |
| **Submit** | Live publication link; one-page audit PDF; live article link; LinkedIn post screenshot; reflection inside the PDF |
| **State** | DRAFT. Not published anywhere. |

---

## Part 1 — Launch the publication (20 pts)

- **Publication name:** `[TODO: DEFINE]` candidates (judgment): *Show Your Work*; *The Receipts*; *Lectern Notes*. Depends on the tool name chosen in Assignment 7.
- **Tagline (judgment):** "Teaching AI tools well, with the evidence."
- **About page, 150–200 words (draft):**

> I am an associate teaching professor of AI and machine learning at Northeastern University. I build AI course assistants for classes I do not teach, taught a course on working with Claude to more than seven hundred learners, and co-developed a public Coursera course on algorithms. This publication is where I show the work behind the work: the tools I build, the places they went wrong, and how I checked them. Right now I am building a job-board tool that searches for teaching and advocacy roles at the companies whose products I teach. It keeps every raw response, shows every reason it kept a posting, and logs its own mistakes. I write about what it found, what it got wrong, and what I would do differently. If you teach, build or evaluate AI, you will find methods here you can reuse and failures you can avoid. Subscribe for one piece at a time. Reply with anything I got wrong; I will correct it in public.

(About 165 words; the facts are in the attested CV file. The last two sentences are a promise he has to be willing to keep. `[TODO: DEFINE]`)

- **Logo or header, custom URL:** `[TODO: DEFINE]` from Assignment 8; the subdomain is not registered.
- **Brand consistency audit (10):** `[TODO: DEFINE]` one-page PDF of the Substack header, the LinkedIn header and the website hero, with 3–5 sentences on why they feel like one family. Needs all three to exist.

## Part 2 — The article (60 pts)

**Angle:** a counterintuitive truth (Path A option). **Headline (draft):** "The list looked right. That was the problem."

**Draft, about 650 words (counted below, headings included):**

> ## The most dangerous output is the one that looks fine
>
> I built a program to find me teaching jobs. It read the open postings from eighteen company job boards, kept the ones about teaching, and showed me each one with the words that made it qualify. It looked professional. Every row made sense. I nearly trusted it.
>
> ## What reading the rejects showed
>
> Then I did the thing I tell students to do: I read what the program threw away. Replit's Learning Experiences Creator, almost exactly the job I wanted, was in the reject pile. My keyword list had "learning designer." The posting said "learning experiences." One word, and the best match in three thousand four hundred forty-six postings was invisible.
>
> The first version of one of my rules was worse. It kept a hundred and one extra postings and was right about roughly one in ten. If I had only counted what it kept, I would have been pleased with how much it found.
>
> ## The audit was wrong too
>
> So I wrote a second script that sorts every posting by what kind of job its title names and shows me only the places where the filter and the job type disagree. The first run reported twenty-seven "education" jobs the filter had rejected, a serious problem. They were Pre-training, Post-Training and Training Runtime roles. At an AI company, "training" means training a model. The filter was right. My audit was wrong.
>
> ## Three habits that came out of it
>
> **Save the raw response before you parse it.** Every board's answer is written to disk, dated, before anything reads it, so any verdict can be re-run and checked.
>
> **Show the reason for every decision.** Each kept posting lists the words that matched and where. A match you cannot explain is a guess.
>
> **Audit the audit.** The checker is a program too, and it fails in its own ways. Write down the failure.
>
> ## What I still do not know
>
> I should be plain about the limits. A random sample of the rejects has been drawn, but I have not yet read it, so I cannot give you an error rate for the filter. I can tell you how many postings it kept, and I can tell you which mistakes I found. Those are different numbers, and only one of them measures whether the list is any good. Five companies I care about use hiring systems the program cannot read at all, so they are missing from every count, not counted as empty. Anyone who quotes my totals without those two sentences is quoting a number that sounds more certain than it is.
>
> ## Why this is not only about job hunting
>
> The same shape shows up wherever a machine hands you a clean summary. A chatbot's answer, a dashboard, a model's grade on a benchmark: each arrives fluent and organized, and the fluency tells you nothing about whether it is right. What separates a result you can use from one you merely admire is whether someone can retrace it. That is why I keep the raw files, print the reasons, and publish the mistakes. It is more work than trusting the list. It is also the only version of this I would put my name on.
>
> ## Where this goes
>
> I built this to look for a particular kind of work: teaching and advocacy roles at the companies whose tools I teach, on flexible terms. The postings alone will not hand me that, because those roles are rarely posted. What the data can do is rank the companies that have decided teaching is worth paying for, which gives me a list of people to talk to. That list is the product; the tool is how I check it.
>
> If you evaluate or teach AI, try this on whatever your own tool produces: read the rejects before you read the results. Tell me where it breaks for you. I'll write about the best failure.

- **Word count:** checked below. **Custom visual:** `[TODO: DEFINE]` e.g. a before/after of the title audit's first and corrected counts, made in Canva or Figma.
- **Mentions the tool naturally:** yes ("a program to find me teaching jobs"); `[TODO: DEFINE]` use the final tool name once chosen.
- **Events (record):** 18 boards and 3,446 postings (`../build-your-data-pipeline/quality-report-2026-09-26.md`); the one-word miss and the 101-extra-postings first rule (same file); the 27 "training" jobs and the `ML_TRAINING` fix (`../build-your-data-pipeline/title-audit-2026-09-26.md`).
- **Call to action:** subscribe or reply, as the draft ends.

## Promotion post (10 pts)

Caption draft (judgment): "My job-search program produced a list that looked right. It had missed the best match because of one word, and my audit of it had its own error. Here is what I do now: read the rejects before the results." Add the article link and a graphic from it. `[TODO: DEFINE]` screenshot after posting.

## Part 3 — Reflection, 300 words (20 pts)

`[TODO: DEFINE]` **Not drafted, deliberately.** The brief asks for the strategic choices he made, how the piece positions him differently, what he would do differently, and the next piece. Those are his decisions. A reflection written in advance would be a fabricated understanding.

## What is still his

1. Check whether a Substack already exists; create or update; publish.
2. The reflection, the audit PDF and the graphics.
3. Whether to promise "I will correct it in public" in the About text.
