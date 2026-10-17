# Deploying the 6A interface, and where a website fits

## Executive summary

**What this is.** The steps to put the Lectern interface at a public URL, and an answer to whether showing it on a website such as bearbrown.co satisfies Canvas Assignment 6A ("Wrap Your Tool").

**Why read it.** The one thing 6A's worked example is missing is a public URL, and the deployment needs Professor Bear's accounts, so Claude cannot do it. This lays out the shortest path and the one choice in it.

**What it found.** A page on bearbrown.co that shows the tool and its search output **does satisfy the public-URL requirement**. What it cannot do alone is run the tool: the interface is a Python Gradio app, and bearbrown.co is a site on Vercel (repo `bearbrown_co`), which does not run a Python server like this one. So the app runs on a free Hugging Face Space and bearbrown.co embeds it. The Canvas brief names Gradio or Streamlit as the framework, so a hand-built web page in place of the Gradio app would be a departure from the brief that only he can allow.

| | |
|---|---|
| **State** | Not deployed. The app has not been run on this Mac (Gradio is not installed here); the earlier worked example logged it as verified in a different environment. |
| **Needs from him** | A Hugging Face account (or Streamlit Community Cloud); permission to add a page to the site repo. |

---

## What the Canvas brief requires

From the 6A brief: "Build a working **Gradio or Streamlit** interface," "**Deployed and accessible via a public URL** (Hugging Face Spaces, Streamlit Community Cloud, or equivalent)," usable by someone who has not read the PRD, with plain-English errors. Then three screenshots (empty, completed run, error) and three structured user tests.

So the **hosting** has flexibility ("or equivalent") and the **framework** does not.

## Does a bearbrown.co page count?

| Option | Meets the brief? | Notes |
|---|---|---|
| The Gradio app on a Hugging Face Space, with bearbrown.co linking to it | Yes | The Space URL is the public URL. The site adds a home for it. |
| The Gradio app on a Hugging Face Space, **embedded** in a bearbrown.co page | Yes | The page URL can be the one submitted, and the Space URL goes alongside it. Screenshots are of the embedded app. |
| A page built in the site's own code that reads the same JSON file and shows the same output | The URL is public, but it is not Gradio or Streamlit | A real interface, and arguably in the spirit of 6A, but he would be allowing a departure from his own rubric. For a worked example for students, follow the brief. |
| The Gradio app running *on* bearbrown.co | No | Vercel does not host a Python server for this. |

**Recommendation:** Space plus embed. It follows the brief, costs nothing, and gives the tool a page on his own site, which also serves Assignments 7–9 (a portfolio piece).

## Steps

1. **Create the Space** (his account): New Space → SDK Gradio → public.
2. **Upload four files** from this folder: `app.py`, `lectern_app_data.json`, `requirements.txt`, and `SPACE_README.md` renamed to `README.md` (its header tells the Space which file to run).
3. **Wait for the build**, open the Space, and run the three states: empty, a company such as Figma, and a keyword that matches nothing.
4. **Paste the Space URL** into `part-1-interface.md` ("Public URL: TODO").
5. **Re-take the three screenshots on the public URL.** The brief wants the deployed interface, not a local run.
6. **Optional: add the website page.** On bearbrown.co, a page that embeds the Space:
   ```html
   <iframe src="https://YOUR-USERNAME-lectern.hf.space" width="100%" height="800" style="border:0"></iframe>
   ```
   The exact address is under the Space's "Embed this Space" menu.
7. **Then run the three user tests** from `part-2-user-testing.md`. Those need three real people; nothing here replaces them.

## Why `app.py` changed

The old launch line fixed the address to `127.0.0.1`. Hugging Face sets its own address through environment variables, and a fixed value would override it and leave the Space unreachable. The app now reads those variables and falls back to `127.0.0.1:7860` locally. The proxy note in the file's header applies only to the earlier environment.

## Not done, and why

- **No deployment, no account, no screenshots:** they need his accounts, and the brief wants screenshots of the deployed app.
- **The app has not been run since this change.** `python3 -c "import ast; ast.parse(open('app.py').read())"` passes, but Gradio is not installed on this Mac, so the interface itself has not been started. Run it once locally before deploying: `pip install gradio` then `python3 app.py`.
- **The site repo was not touched.** Adding a page to bearbrown.co is a change to a live site; that is his call.
