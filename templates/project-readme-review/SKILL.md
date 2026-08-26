---
name: project-readme-review
description: "When user says 'project <name>', report its README status."
version: 1.0.0
author: Tom (adapted for Antonina)
license: MIT
metadata:
  hermes:
    tags: [project, status, readme, documentation]
    related_skills: [obsidian]
---

# Project README Review

## When to Use

Use whenever the user asks "project <name>", "project status", or "what's the status on <name>" — report the project's current state from its README and git history instead of guessing.

## Trigger

Any utterance matching `project <name>` where `<name>` is a project identifier. Also triggered by "project lead", "project status", or "what's the status on [name]".

## Steps

1. **Locate the project folder**
   - Root path: `/opt/data/projects/<name>/` (same as `~/projects/<name>/` since `$HOME=/opt/data`)
   - Verify the directory exists

2. **Read the README.md**
   - Path: `/opt/data/projects/<name>/README.md`
   - This is the canonical source of project status

3. **Supplement with git state**
   - Run `git status --short` and `git log --oneline -5` from the project root
   - Note any uncommitted changes, current branch, recent commits

4. **Check for key project files**
   - `package.json` / `pyproject.toml` / `wrangler.toml` / `dockerfile` — deployment config (varies by stack)
   - `design.md` / `build-plan.md` — architecture and plan docs (adopted convention)
   - Any gap reviews or audit files in the root

5. **Present a concise project lead summary**
   - Current status (from README)
   - Working tree state (uncommitted changes, recent commits)
   - Live URL / deployment targets (only if the project actually has one)
   - Open gaps or known issues
   - Last known activity timestamp

## Conventions

- Every project lives at `/opt/data/projects/<name>/` — one folder per project
- Each project gets its own GitHub repo (`origin` remote)
- Subfolders: `src/`, `docs/`, `scripts/`, `data/`, `reports/`, etc.
- The README is always at the root level
- Do NOT guess project structure — always read the actual files
- If the project folder or README doesn't exist, say so and offer to create it

## Pitfalls

- A project may have uncommitted git changes — always check `git status`
- README may reference a "live" URL that isn't actually deployed — don't assume without verifying
- **README can be stale.** The README is a living dashboard that may not have been kept current. Architecture decisions in `design.md` and build plans in `build-plan.md` are the deeper source of truth. Always cross-reference README claims against these files, especially for provisioning/pipeline/architecture questions. When they conflict, `design.md` wins.
- **Specific subsystems are prone to drift.** Sourcing, provisioning, and integration details change faster than READMEs. If the README describes a subsystem (e.g. a data source, an API integration, a hosting model), verify against the current design docs before repeating it as fact.
- **Obsidian doc-only projects.** Some projects may exist as notes in the Obsidian vault but not as `/opt/data/projects/` code folders — check both if uncertain. Resolve the vault path via `OBSIDIAN_VAULT_PATH` (fallback `~/Documents/Obsidian Vault`); if neither exists, there is no vault.
- **After updating stale docs, commit locally — ask before pushing.** If you discover stale content while doing a project review, update the affected files and commit locally. Do NOT push to GitHub without asking: the user's policy is to push only after a major block of work is finished, and only with confirmation.
- **When the user corrects an answer about project architecture, check `design.md` and `build-plan.md` before assuming the README was enough.** The correction itself is a signal that this project has in-flight changes between the README and the active design docs.
