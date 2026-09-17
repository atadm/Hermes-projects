# Enterprise PO Operating Model — Design

**Status:** Draft v0.1 · **Last updated:** 2026-09-17

## Purpose

Operating model for the new Enterprise Product Owner team: process + instrument list for leading complex internal automation and digital transformation projects.

## Architecture truth

- **`playbook.md` is the single source of truth** for the process (6 phases, 5 gates), instrument list, governance skeleton, and measurement standards.
- Templates live in `templates/` (markdown + Excel; spec JSON files are build sources for the workbooks).

## Key design decisions

| Decision | Rationale |
|---|---|
| Gate-based lifecycle (6 phases, 5 gates) | Enterprise automation involves money, procurement, compliance — decisions need gates, not just sprints |
| Adoption & change is its own phase with its own gate | Most internal automation failure is adoption, not technology |
| Baselines captured **before** deployment | No baseline = no credible ROI claim (org standard) |
| Measure outcomes, not activity | Hours saved, cycle time, error rate — not logins/messages |
| ROI conventions: 1 FTE = 2,080 h/yr; $36k/yr fully loaded | Org standard; drives every business case |
| Minimal viable instrument set first (~8), others added on demand | Instruments must earn their place; used within a month or cut |
| Product over project | Value continues after launch; handover ≠ end of accountability |

## Open decisions (team workshops)

- Decision rights table (who approves each gate)
- Template storage / single source of truth
- Whether EPOs own platform components or only use-case products
- ROI convention confirmation with Finance
