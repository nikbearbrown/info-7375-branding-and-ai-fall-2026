#!/usr/bin/env python3
"""run_recipe.py — the conductor script for recipe_brown.md (Assignment 6B, Part 4).

    python3 run_recipe.py --raw <dir of saved responses> --raw-date 2026-09-26

What it does, layer by layer (the recipe's four layers):
  1. Replays the saved raw responses of one earlier run (no network) under today's date,
     because collect.py names its raw files by date. Gate 1 machine check.
  2. Runs ../build-your-data-pipeline/collect.py --from-raw on the replay. Gate 2 machine check,
     including a re-derivation check against the committed run files of the same date.
  3. Runs ../build-your-data-pipeline/demand_report.py and checks the report: every claim has a
     link, every link is a posting in the run, every board total matches. Gate 3 machine check.
  4. Writes logs/reports/demand-<today>.md (marked DRAFT), appends logs/reports/run-log.md and
     writes logs/lectern-<today>.json (the recipe's agent-output contract).

What it does NOT do: it never records a human approval. The recipe's gates carry human judgment
types (IJ, TO); the script reports the machine check and marks each human decision PENDING.
It also does not fetch live data: this is a replay, and the log says so.

Stdlib only. Exit 0 = ran to the stop at Gate 4; 1 = a machine check failed; 2 = bad input.
"""
import argparse, datetime as dt, json, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PIPE = os.path.normpath(os.path.join(HERE, "..", "build-your-data-pipeline"))
REQUIRED = ("title", "url", "date_posted", "location_text", "department")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def raw_name(provider, slug, date):
    return f"{provider}-{slug.replace(' ', '_').lower()}-{date}.json"


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--raw", required=True, help="directory of saved raw responses")
    ap.add_argument("--raw-date", required=True, help="date in the saved filenames, YYYY-MM-DD")
    ap.add_argument("--out", default=os.path.join(HERE, "logs"))
    a = ap.parse_args(argv)
    if not DATE_RE.match(a.raw_date) or not os.path.isdir(a.raw):
        print("INPUT ERROR: --raw must be a directory and --raw-date YYYY-MM-DD", file=sys.stderr)
        return 2

    today = dt.date.today().isoformat()
    stamp = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    cfg = json.load(open(os.path.join(PIPE, "sources.json"), encoding="utf-8"))
    boards = [(s["provider"], b["company"], b["slug"]) for s in cfg["sources"] for b in s["boards"]]
    work = tempfile.mkdtemp(prefix="lectern-run-")
    replay, out1 = os.path.join(work, "raw"), os.path.join(work, "out")
    os.makedirs(replay)
    os.makedirs(out1)
    flags, steps, gates = [], [], {}

    # ---- Layer 1: replay saved responses -------------------------------------------------
    missing, empty = [], []
    for provider, company, slug in boards:
        src = os.path.join(a.raw, raw_name(provider, slug, a.raw_date))
        if not os.path.exists(src):
            missing.append(company)
            continue
        try:
            payload = json.load(open(src, encoding="utf-8"))
        except ValueError:
            empty.append(company)
            continue
        if not payload:
            empty.append(company)
            continue
        shutil.copyfile(src, os.path.join(replay, raw_name(provider, slug, today)))
    steps.append("layer1-replay")
    g1 = not missing and not empty
    gates["gate1_ingest"] = {
        "judgment_type": "IJ",
        "machine_check": "PASS" if g1 else "FAIL",
        "detail": f"{len(boards) - len(missing) - len(empty)} of {len(boards)} watched boards had a non-empty saved response",
        "not_exercised": "count-drift against a previous trusted run, because a replay has no live total to compare",
        "human_decision": "PENDING",
    }
    if missing:
        flags.append(f"missing saved response: {', '.join(missing)}")
    if empty:
        flags.append(f"empty saved response: {', '.join(empty)}")

    # ---- Layer 2: collect.py --from-raw ---------------------------------------------------
    rc, so, se = run([sys.executable, os.path.join(PIPE, "collect.py"), "--from-raw", replay, "--out", out1])
    steps.append("layer2-collect")
    if rc != 0:
        gates["gate2_gigo"] = {"judgment_type": "IJ", "machine_check": "FAIL",
                               "detail": f"collect.py exited {rc}: {se.strip()[-200:]}", "human_decision": "PENDING"}
        flags.append("collect.py failed")
        return finish(a, today, stamp, steps, gates, flags, None, None, None, work, stopped="collect.py failed")
    allj = json.load(open(os.path.join(out1, f"all-jobs-{today}.json"), encoding="utf-8"))
    kept = json.load(open(os.path.join(out1, f"jobs-of-interest-{today}.json"), encoding="utf-8"))
    all_recs, kept_recs = allj["records"], kept["records"]
    incomplete = [r for r in all_recs if any(not r.get(k) for k in REQUIRED)]
    bad_dates = [r for r in all_recs if not DATE_RE.match(r.get("date_posted") or "")]
    keys = [(r["source"], r["source_id"]) for r in kept_recs]
    dupes = len(keys) - len(set(keys))
    untraced = [r for r in kept_recs if not r.get("matched")]
    ref_path = os.path.join(PIPE, f"jobs-of-interest-{a.raw_date}.json")
    rederived = None
    if os.path.exists(ref_path):
        ref = json.load(open(ref_path, encoding="utf-8"))["records"]
        rederived = {(r["source"], r["source_id"]) for r in ref} == set(keys)
    g2 = not incomplete and not bad_dates and dupes == 0 and not untraced and rederived is not False
    gates["gate2_gigo"] = {
        "judgment_type": "IJ",
        "machine_check": "PASS" if g2 else "FAIL",
        "detail": (f"{len(all_recs)} postings fetched, {len(kept_recs)} kept; {len(incomplete)} missing a required field; "
                   f"{len(bad_dates)} non-YYYY-MM-DD dates; {dupes} duplicate kept records; {len(untraced)} kept records "
                   f"with no matched-words trace; kept set identical to the committed run of {a.raw_date}: {rederived}"),
        "not_exercised": "trusted-run thresholds (>=90% of source-reported total, >=70% of previous trusted run)",
        "human_decision": "PENDING",
    }

    # ---- Layer 3: demand report + claim trace ---------------------------------------------
    report_path = os.path.join(work, "demand.md")
    rc, so, se = run([sys.executable, os.path.join(PIPE, "demand_report.py"), "--all-jobs",
                      os.path.join(out1, f"all-jobs-{today}.json"), "--kept",
                      os.path.join(out1, f"jobs-of-interest-{today}.json"), "--out", report_path])
    steps.append("layer3-demand-report")
    if rc != 0:
        gates["gate3_traceable"] = {"judgment_type": "TO", "machine_check": "FAIL",
                                    "detail": f"demand_report.py exited {rc}", "human_decision": "PENDING"}
        flags.append("demand_report.py failed")
        return finish(a, today, stamp, steps, gates, flags, allj, kept, None, work, stopped="demand_report.py failed")
    report = open(report_path, encoding="utf-8").read()
    urls = {r["url"] for r in all_recs}
    claims = [l for l in report.splitlines() if re.match(r"- \*\*(BUILDS|TEACHES|ADVOCATES|SELLS|ENABLES)\*\*", l)]
    unlinked = [l for l in claims if "](http" not in l]
    linked = [re.search(r"\]\((https?://[^)]+)\)", l).group(1) for l in claims if "](http" in l]
    dangling = [u for u in linked if u not in urls]
    per_company = {}
    for r in all_recs:
        per_company[r["company"]] = per_company.get(r["company"], 0) + 1
    table = re.findall(r"^\| \*\*([^*]+)\*\* \| (\d+) \|", report, re.M)
    mismatched = [c for c, n in table if per_company.get(c) != int(n)]
    g3 = bool(claims) and not unlinked and not dangling and not mismatched
    gates["gate3_traceable"] = {
        "judgment_type": "TO",
        "machine_check": "PASS" if g3 else "FAIL",
        "detail": (f"{len(claims)} claims in the report, {len(unlinked)} without a link, {len(dangling)} links not found in "
                   f"the run's postings; {len(table)} ranked companies, {len(mismatched)} whose board total differs from the run"),
        "not_exercised": "recomputing the per-company signal-role counts; only links and board totals were checked",
        "human_decision": "PENDING",
    }

    # ---- Layer 4: write outputs, stop at Gate 4 -------------------------------------------
    gates["gate4_shippable"] = {
        "judgment_type": "TO",
        "machine_check": "NOT RUN",
        "detail": "Gate 4 is a human read: could a non-technical reader answer which companies, what roles, what is new?",
        "not_exercised": "the new/gone diff against a previous trusted run (TODO: DEV in the recipe), and the human top-line label",
        "human_decision": "PENDING - the recipe stops here every run",
    }
    steps.append("layer4-report")
    return finish(a, today, stamp, steps, gates, flags, allj, kept, report, work,
                  stopped="Phase Gate 4: awaiting Professor Bear's approval", dupes=dupes, g=(g1, g2, g3))


def finish(a, today, stamp, steps, gates, flags, allj, kept, report, work, stopped, dupes=0, g=None):
    out = a.out
    os.makedirs(os.path.join(out, "reports"), exist_ok=True)
    fetch_counts = {}
    if allj:
        for r in allj["records"]:
            fetch_counts[r["company"]] = fetch_counts.get(r["company"], 0) + 1
    agent = {
        "workflow": "lectern",
        "run_id": f"lectern-{today}",
        "mode": f"replay of saved responses dated {a.raw_date} (no live fetch)",
        "steps_completed": steps,
        "records_seen": len(allj["records"]) if allj else 0,
        "records_kept": len(kept["records"]) if kept else 0,
        "rejects": kept["counts"]["rejected"] if kept else None,
        "duplicates": dupes,
        "flags": flags,
        "stop_conditions": [stopped],
        "generated_at": stamp,
        "fetch_counts": dict(sorted(fetch_counts.items())),
        "trusted_run": {"verdict": None,
                        "reason": "not determined: a replay has no source-reported total and no previous trusted run to compare"},
        "gates": gates,
    }
    with open(os.path.join(out, f"lectern-{today}.json"), "w", encoding="utf-8") as f:
        json.dump(agent, f, indent=2, ensure_ascii=False)
        f.write("\n")
    if report:
        head = (f"> **DRAFT, not approved.** Run of {today}: a replay of the responses saved {a.raw_date}, not a live fetch. "
                f"Machine checks for Gates 1-3 are in `../lectern-{today}.json`. Phase Gate 4 (a human read) is pending; "
                f"the \"what's new\" takeaway is not written.\n\n")
        with open(os.path.join(out, "reports", f"demand-{today}.md"), "w", encoding="utf-8") as f:
            f.write(head + report)
    log = os.path.join(out, "reports", "run-log.md")
    new = not os.path.exists(log)
    with open(log, "a", encoding="utf-8") as f:
        if new:
            f.write("# Lectern run log\n\nOne block per run, newest last. Machine checks are the script's; every human "
                    "decision is recorded only when a person makes it.\n")
        f.write(f"\n## {today} - replay of the {a.raw_date} responses\n\n")
        f.write(f"- Mode: replay of saved responses, no live fetch. Generated {stamp}.\n")
        f.write(f"- Postings seen {agent['records_seen']}, kept {agent['records_kept']}, duplicates {dupes}.\n")
        for name, gate in gates.items():
            f.write(f"- {name} ({gate['judgment_type']}): machine check {gate['machine_check']}. {gate['detail']}. "
                    f"Human decision: {gate['human_decision']}.\n")
        for fl in flags:
            f.write(f"- FLAG: {fl}\n")
        f.write(f"- Stopped: {stopped}.\n")
    shutil.rmtree(work, ignore_errors=True)
    for name, gate in gates.items():
        print(f"{name:18} {gate['judgment_type']}  machine check: {gate['machine_check']}")
    print(f"stopped: {stopped}")
    failed = any(g_["machine_check"] == "FAIL" for g_ in gates.values())
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
