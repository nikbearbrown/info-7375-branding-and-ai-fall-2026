#!/usr/bin/env python3
"""Build Brown_Nik_A5B_BuildTheRecipe.pdf for Assignment 6B (Path B)."""
import re, os, json
from fpdf import FPDF

BASE = "/tmp/branding/b5/build-the-recipe"
OUT = os.path.join(BASE, "Brown_Nik_A5B_BuildTheRecipe.pdf")

class PDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(120, 120, 120)
            self.cell(0, 8, "INFO 7375 -- Assignment 6B (Path B) -- Nik Bear Brown",
                      align="R", new_x="LMARGIN", new_y="NEXT")
            self.set_text_color(0, 0, 0)
    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

def clean(t):
    for a, b in [("\u201c", '"'), ("\u201d", '"'), ("\u2014", "--"), ("\u2013", "-"),
                 ("\u2192", "->"), ("\u00d7", "x"), ("\u2714", "[x]"), ("\u2b1c", "[ ]"),
                 ("\u23f3", ""), ("\u2018", "'"), ("\u2019", "'"), ("\u2026", "..."),
                 ("\u2265", ">="), ("\u2010", "-"), ("\u2705", "[x]"), ("\u2b1c", "[ ]"),
                 ("\u23f3", "(pending)")]:
        t = t.replace(a, b)
    return t

def mc(pdf, h, text, style="", size=10):
    pdf.set_font("Helvetica", style, size)
    pdf.multi_cell(0, h, text, new_x="LMARGIN", new_y="NEXT")

def add_md(pdf, path, title):
    with open(path) as f:
        text = f.read()
    text = re.sub(r"^# .*\n+", "", text, count=1)
    pdf.add_page()
    mc(pdf, 9, clean(title), "B", 16)
    pdf.ln(3)
    for line in text.split("\n"):
        line = clean(line.rstrip())
        if not line.strip():
            pdf.ln(3); continue
        if line.startswith("### "):
            mc(pdf, 7, line[4:], "B", 12); pdf.ln(1)
        elif line.startswith("## "):
            mc(pdf, 8, line[3:], "B", 13); pdf.ln(1)
        elif line.startswith("- ") or line.startswith("* "):
            mc(pdf, 5.5, "  - " + line[2:])
        elif line.startswith("> "):
            pdf.set_text_color(60, 60, 60)
            mc(pdf, 5.5, line[2:], "I", 10)
            pdf.set_text_color(0, 0, 0)
        elif line.startswith("```"):
            continue
        elif line.startswith("|"):
            mc(pdf, 5, line, "", 8)
        elif re.match(r"^\d+\. ", line):
            mc(pdf, 5.5, line)
        else:
            body = re.sub(r"\*\*(.+?)\*\*", r"\1", line)
            body = re.sub(r"\*(.+?)\*", r"\1", body)
            body = re.sub(r"`(.+?)`", r"\1", body)
            mc(pdf, 5.5, body)

def add_json(pdf, path, title):
    with open(path) as f:
        data = json.load(f)
    pretty = json.dumps(data, indent=1, ensure_ascii=True)
    pdf.add_page()
    mc(pdf, 9, clean(title), "B", 16)
    pdf.ln(3)
    pdf.set_font("Courier", "", 7.5)
    for line in pretty.split("\n"):
        line = clean(line)
        while len(line) > 0:
            chunk, line = line[:105], line[105:]
            pdf.multi_cell(0, 4, chunk, new_x="LMARGIN", new_y="NEXT")

pdf = PDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(True, 20)

# Cover
pdf.add_page()
pdf.ln(40)
mc(pdf, 12, "Assignment 6B -- Path B", "B", 24)
mc(pdf, 10, "Build the Recipe", "", 16)
pdf.ln(8)
mc(pdf, 8, "Lectern teaching-demand pipeline, conductor-ready: config, verified data, recipe, audit.")
pdf.ln(12)
mc(pdf, 7, "Nik Bear Brown\nINFO 7375 Branding and AI -- Fall 2026\nDue October 23, 2026")
pdf.ln(12)
pdf.set_text_color(100, 100, 100)
mc(pdf, 6, "Worked example -- drafted 2026-10-11. Gru /snickerdoodle confirmation is TODO (see Part 4).", "I", 10)
pdf.set_text_color(0, 0, 0)

add_md(pdf, f"{BASE}/README.md", "Overview")
add_json(pdf, f"{BASE}/brand_config.json", "Part 1 -- brand_config.json (25 pts)")
add_md(pdf, f"{BASE}/data/verified/README.md", "Part 2 -- Verified data folder (20 pts)")
add_md(pdf, f"{BASE}/recipe_brown.md", "Part 3 -- Recipe file (25 pts)")
add_md(pdf, f"{BASE}/part-4-snickerdoodle.md", "Part 4 -- The /snickerdoodle run (10 pts)")

pdf.output(OUT)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
