#!/usr/bin/env python3
"""Lectern demo interface (Assignment 5A, Path A — worked example).

Wraps the Lectern demand data (Assignment 3's 2026-09-26 run: 97 kept
postings of 3,446) in a Gradio UI for the Part 2 user: the independent
AI-education consultant deciding which companies are worth approaching.

Run:  python3 app.py   ->  http://127.0.0.1:7860
Data: lectern_app_data.json (compact extract of the real run file;
      the full file is assignment-3/jobs-of-interest-2026-09-26.json).

NOTE (VM quirk): the egress proxy's NO_PROXY entries crash httpx at
import time inside gradio. Launch with proxy vars unset — the app only
touches localhost and local files, so it needs no proxy:
    env -u https_proxy -u HTTPS_PROXY -u http_proxy -u HTTP_PROXY \
        -u no_proxy -u NO_PROXY python3 app.py
"""
import json
import os

DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "lectern_app_data.json")

try:
    with open(DATA_PATH) as f:
        DATA = json.load(f)
    RECORDS = DATA["records"]
    DATA_ERROR = None
except Exception as e:  # missing/corrupt data file -> plain-English error
    RECORDS, DATA_ERROR = [], f"Could not load the demand data ({e})."

COMPANIES = sorted({r["company"] for r in RECORDS})


def check_demand(company, keyword):
    """Build the demand report for one company, optionally filtered."""
    if DATA_ERROR:
        return f"### Something's wrong on our end\n\n{DATA_ERROR}\n\nThe data file is missing — the interface can't run without it."
    if not company:
        return ("### Pick a company first\n\n"
                "Choose a company from the list above, then press "
                "**Check demand signals**.")
    kw = (keyword or "").strip().lower()
    hits = [r for r in RECORDS if r["company"] == company]
    if kw:
        hits = [r for r in hits if kw in r["title"].lower()]
        if not hits:
            return (f"### No matches for \u201c{keyword.strip()}\u201d at {company}\n\n"
                    f"{company} has teaching-related postings in this run, but none "
                    f"with that word in the title. Try a broader word (e.g. "
                    f"\u201ceducation\u201d, \u201ctraining\u201d), or clear the box "
                    f"to see everything we kept for {company}.")
    if not hits:
        return (f"### No teaching-related postings at {company} in this run\n\n"
                "That doesn't mean no interest — it means nothing matched the "
                "filter on 2026-09-26. Check the full run file for the raw picture.")

    lines = [f"### {company} — demand signals (run of 2026-09-26)",
             f"**{len(hits)} teaching-related posting(s) kept.**",
             "",
             "What this means: these are the roles where the company is "
             "publicly staffing teaching, enablement, or advocacy work — "
             "the evidence you'd cite when deciding whether to approach them.",
             ""]
    for r in hits:
        words = ", ".join(r["words"]) if r["words"] else "—"
        lines.append(f"- **[{r['title']}]({r['url']})** — {r['location']}")
        lines.append(f"  Kept because: *{r['kept_because']}* "
                     f"(matched: {words})")
    lines += ["",
              "_Every posting links to the live ad, and every keep names the "
              "rule that fired — check any claim in two clicks._"]
    return "\n".join(lines)


def build_ui():
    import gradio as gr
    with gr.Blocks(title="Lectern — teaching-demand signals") as ui:
        gr.Markdown(
            "# Lectern\n"
            "Which companies selling AI to universities are showing real "
            "interest in how their tools are used in teaching?\n\n"
            "_Pick a company. Read the evidence. Decide who is worth "
            "approaching._")
        with gr.Row():
            company = gr.Dropdown(choices=COMPANIES, label="Company",
                                  info="One of the watched boards from the "
                                       "2026-09-26 run.")
            keyword = gr.Textbox(label="Filter by keyword (optional)",
                                 placeholder="e.g. education, training, advocate",
                                 info="Matches against posting titles only.")
        btn = gr.Button("Check demand signals", variant="primary")
        out = gr.Markdown(label="Demand report")
        btn.click(check_demand, inputs=[company, keyword], outputs=out)
        gr.Markdown(
            "_Data: 97 kept postings of 3,446 (2026-09-26 run). "
            "Worked example for INFO 7375 Assignment 5A._")
    return ui


if __name__ == "__main__":
    build_ui().launch(server_name="127.0.0.1", server_port=7860)
