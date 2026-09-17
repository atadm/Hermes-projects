# Rollout & Hypercare Checklist — <Project>

**Purpose:** Get to go-live (Gate 4) in a controlled way, protect users in the first weeks, and hand over cleanly (Gate 5). Wave-based rollout for anything touching more than ~10 users.

## 1. Pre-launch checklist (Gate 4 conditions)

- [ ] UAT passed with sign-off recorded — owner, date
- [ ] Security/compliance sign-off (incl. EU AI Act transparency/literacy duties if AI is used) — owner, date
- [ ] Architecture review done — owner, date
- [ ] Support model ready: L1/L2/L3 defined, helpdesk briefed — owner, date
- [ ] Training completed (see training-plan.md) — owner, date
- [ ] Comms sent (see comms-plan.md) — owner, date
- [ ] Data migration verified + reconciled — owner, date
- [ ] Rollback plan exists and is understood (what triggers it, who authorizes) — owner, date
- [ ] Performance/volume test at expected load — owner, date
- [ ] Go-live decision recorded in Decision Log — date

## 2. Rollout wave plan

| Wave | Group | Date | Go criteria (what must be true first) | Owner | Notes |
|---|---|---|---|---|---|
| Pilot | <small, low-risk, visible team> | | Wave readiness: UAT done, support ready | EPO | Learn fast, create advocates |
| Wave 2 | <next group> | | Pilot hypercare stable ≥ 1 week, issues fixed | EPO | |
| Full | <everyone> | | Waves 1–2 stable, training done for all | EPO + sponsor | |

## 3. Hypercare (typically 2–4 weeks after each wave)

| Item | Detail | Owner |
|---|---|---|
| Duration | <2–4 weeks> | EPO |
| L1 — helpdesk | Triage + known issues (runbook) | Support |
| L2 — process | Workflow/process issues, training gaps | EPO + process owner |
| L3 — vendor/platform | Escalation to vendor per SLA | Delivery |
| Issue logging | Every contact logged; blockers flagged to RAID | Support |
| Daily triage | 15-min standup during hypercare, issues prioritized | EPO |
| Response targets | L1 < 4 h · L2 < 1 business day · L3 per vendor SLA | — |
| Escalation path | EPO → sponsor if critical issue unresolved 48 h | — |

## 4. Post-hypercare handover (Gate 5)

- [ ] Adoption target met or trajectory confirmed (adoption-tracker.xlsx) — date
- [ ] Support ownership handed to operations (runbook, SLA, contact list) — date
- [ ] Benefit baseline confirmed (benefit-tracker.xlsx) — date
- [ ] Old process officially retired (old tools disabled, instructions removed) — date
- [ ] Lessons learned logged (what worked, what to repeat) — date
- [ ] Quarterly value review scheduled — date
