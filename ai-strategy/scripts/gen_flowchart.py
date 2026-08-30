#!/usr/bin/env python3
"""
Generate a self-explaining Mermaid flowchart DERIVED from the project's source
of truth (build-plan.md workstreams). Because the chart is generated from the
real definition, it cannot drift from reality while the source is maintained.

Automate the re-run:
  - cron:  `python3 scripts/gen_flowchart.py && git add docs/flowchart.md && git commit`
  - hook:  run on commit of build-plan.md

Usage:
    python3 gen_flowchart.py [--out docs/flowchart.md] [--dry-run]
"""

import argparse
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # project root


def slug(text: str) -> str:
    """Short safe node id from step text."""
    words = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-").split("-")
    return "-".join(words[:5])


def parse_build_plan(text: str) -> list[dict]:
    """Extract workstreams: {id, title, internal:[], external:[], generic:[], exit}."""
    section = re.search(
        r"## 4\. Workstreams & timeline.*?\n(.*?)(?=\n## 5\.)",
        text,
        re.DOTALL,
    )
    if not section:
        raise SystemExit("Could not find '## 4. Workstreams & timeline'")
    body = section.group(1)

    ws_list = []
    # Split on ### WS<n> headings, keeping id + title
    chunks = re.split(r"\n### (WS\d+) — ([^\n]+)\n", body)
    for i in range(1, len(chunks), 3):
        ws_id, title = chunks[i], chunks[i + 1].strip()
        block = chunks[i + 2]

        internal, external, generic = [], [], []
        current = generic
        for line in block.splitlines():
            line = line.strip()
            if line.startswith("**Internal"):
                current = internal
            elif line.startswith("**External"):
                current = external
            elif line.startswith("- "):
                current.append(line[2:].strip())
        # Remove the exit-criteria pseudo-step if it landed in lists
        exit_m = re.search(r"\*\*Exit criteria:\*\*\s*(.+)", block)

        ws_list.append(
            {
                "id": ws_id,
                "title": title,
                "internal": internal,
                "external": external,
                "generic": generic,
                "exit": exit_m.group(1).strip() if exit_m else "",
            }
        )
    return ws_list


def build_mermaid(ws: list[dict], project: str) -> str:
    L = ["```mermaid", "flowchart TD", f'    P["📦 {project}"] --> {ws[0]["id"]}', ""]

    # One subgraph per workstream
    for w in ws:
        L.append(f'    subgraph {w["id"]}["{w["title"]}"]')
        L.append("        direction TB")
        nid = 0

        def node(text, cls=""):
            nonlocal nid
            nid += 1
            n = f'{w["id"]}n{nid}'
            label = text.replace('"', "'")
            L.append(f'        {n}{cls}["{label}"]')
            return n

        prev = None
        for grp, name in ((w["external"], "🔎 External (start now)"),
                          (w["internal"], "🏢 Internal (needs company input)"),
                          (w["generic"], "")):
            for s in grp:
                n = node(f'{name + " · " if name else ""}{s}')
                if prev:
                    L.append(f"        {prev} --> {n}")
                prev = n
        # Exit gate
        x = f'{w["id"]}X'
        L.append(f'        {x}{{"✅ exit: {w["exit"].replace(chr(34), "")}"}}')
        if prev:
            L.append(f"        {prev} --> {x}")
        L.append("    end")
        L.append("")

    # Chaining + retry loops
    for a, b in zip(ws, ws[1:]):
        L.append(f'    {a["id"]}X -- "pass" --> {b["id"]}')
    for w in ws:
        retry_target = f'{w["id"]}n1'
        L.append(f'    {w["id"]}X -- "fail: revise" --> {retry_target}')

    L.append("```")
    L.append("")
    L.append(
        f"_Auto-generated {date.today().isoformat()} from build-plan.md by "
        "scripts/gen_flowchart.py — re-run to refresh, commit the change._"
    )
    return "\n".join(L)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="docs/flowchart.md")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    plan = (ROOT / "build-plan.md").read_text(encoding="utf-8")
    ws = parse_build_plan(plan)
    for w in ws:
        print(
            f"{w['id']}: {w['title']} | ext={len(w['external'])} "
            f"int={len(w['internal'])} | exit: {w['exit'][:50]}"
        )

    md = build_mermaid(ws, "ai-strategy")
    if args.dry_run:
        print(md)
        return
    out = ROOT / args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8")
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
