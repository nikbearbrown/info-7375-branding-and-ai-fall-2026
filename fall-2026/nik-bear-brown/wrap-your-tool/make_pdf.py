#!/usr/bin/env python3
"""Build Brown_Nik_A5A_WrapYourTool.pdf from the assignment-5a markdown files."""
import re, os
from fpdf import FPDF

BASE = "/tmp/branding/a5a"
OUT = os.path.join(BASE, "Brown_Nik_A5A_WrapYourTool.pdf")

class PDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(120, 120, 120)
            self.cell(0, 8, clean("INFO 7375 -- Assignment 5A (Path A) -- Nik Bear Brown"), align="R", new_x="LMARGIN", new_y="NEXT")
            self.set_text_color(0, 0, 0)
    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

def clean(t):
    t = t.replace("\u201c", '"').replace("\u201d", '"').replace("\u2014", "--").replace("\u2013", "-")
    t = t.replace("\u2192", "->").replace("\u00d7", "x").replace("\u2714", "[x]").replace("\u2b1c", "[ ]")
    t = t.replace("\u23f3", "").replace("\u2018", "'").replace("\u2019", "'").replace("\u2026", "...")
    return t

def mc(pdf, h, text, style="", size=10):
    """multi_cell that leaves the cursor at the left margin (fpdf2 defaults to RIGHT)."""
    pdf.set_font("Helvetica", style, size)
    pdf.multi_cell(0, h, text, new_x="LMARGIN", new_y="NEXT")

def add_md(pdf, path, title):
    with open(path) as f:
        text = f.read()
    # skip the file's own h1 (we add our own section title)
    text = re.sub(r"^# .*\n+", "", text, count=1)
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
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
        elif re.match(r"^\d+\. ", line):
            mc(pdf, 5.5, line)
        else:
            # bold inline markers: strip markdown ** for body text
            body = re.sub(r"\*\*(.+?)\*\*", r"\1", line)
            body = re.sub(r"\*(.+?)\*", r"\1", body)
            mc(pdf, 5.5, body)

pdf = PDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(True, 20)

# Cover
pdf.add_page()
pdf.ln(40)
pdf.set_font("Helvetica", "B", 24)
pdf.cell(0, 12, clean("Assignment 5A -- Path A"), new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 16)
pdf.cell(0, 10, clean("Interface, User Testing, and Market Positioning"), new_x="LMARGIN", new_y="NEXT")
pdf.ln(8)
pdf.set_font("Helvetica", "", 12)
pdf.multi_cell(0, 8, clean("Lectern: which companies selling AI to universities are showing real interest in how their tools are used in teaching?"))
pdf.ln(12)
pdf.set_font("Helvetica", "", 11)
pdf.multi_cell(0, 7, clean("Nik Bear Brown\nINFO 7375 Branding and AI -- Fall 2026\nDue October 23, 2026"))
pdf.ln(12)
pdf.set_font("Helvetica", "I", 10)
pdf.set_text_color(100, 100, 100)
pdf.multi_cell(0, 6, clean("Worked example -- drafted 2026-10-11.\nDeployment URL and user-test sessions are TODO (see README)."))
pdf.set_text_color(0, 0, 0)

add_md(pdf, f"{BASE}/part-1-interface.md", "Part 1 — The Interface (30 pts)")
add_md(pdf, f"{BASE}/part-2-user-testing.md", "Part 2 — User Testing (25 pts)")
add_md(pdf, f"{BASE}/part-3-positioning.md", "Part 3 — Competitive Positioning (25 pts)")

pdf.output(OUT)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
