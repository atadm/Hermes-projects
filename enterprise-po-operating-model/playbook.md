# Enterprise Product Owner Playbook (Draft v0.1)

**Purpose:** Baseline process and instrument list for Enterprise Product Owners (EPOs) leading complex internal automation and digital transformation projects.

**Status:** Draft for team workshops — to be validated, cut down, and adopted by the team. Every instrument must earn its place; start lean (~20 templates), not exhaustive.

**Alignment notes:** Consistent with the company AI strategy direction (hybrid hub-and-spoke, outcome-based measurement, baselines captured before deployment, EU AI Act literacy duties as deployer). ROI conventions per org standard: 1 FTE = 2,080 h/yr; fully loaded employee cost $36k/yr ($3,000/mo). **Confirm these figures** — they drive every business case.

---

## 1. Role definition

An Enterprise PO is the single accountable owner of **business value** for an internal automation / digital product — not the delivery manager.

| Dimension | Classic Product Owner | Enterprise PO (internal automation/transformation) |
|---|---|---|
| Customer | External users, one market | Internal employees + process owners across functions |
| Value | Revenue / growth | Cost reduction, time saved, risk reduction, capacity freed |
| Stakeholders | Product org | Business units, IT/engineering, vendors, procurement, compliance, security, works council where relevant |
| Governance | Sprint-level | Gate-level (money, procurement, compliance, architecture) |
| Lifecycle | Continuous product | Product with lifecycle, but value continues after launch |

**Core accountabilities:**
1. Opportunity framing and business case (economics first)
2. Stakeholder and sponsor management
3. Requirements and solution ownership (build / buy / configure)
4. Delivery governance (with delivery leads/PMs where they exist)
5. Adoption and change — where most value is won or lost
6. Value measurement and reporting after go-live

**Explicit non-ownership** (align in workshop): security/compliance final approval, architecture decisions, infrastructure ops, procurement contract terms — EPO *drives* these but does not *own* them. Decision rights table needed (see §4).

---

## 2. Process: 6 phases, 5 gates

```
Phase 0 Intake → G1 → Phase 1 Discovery → G2 → Phase 2 Selection → G3
→ Phase 3 Delivery → G4 → Phase 4 Adoption → G5 → Phase 5 Value (recurring)
```

### Phase 0 — Intake & Triage (1–2 weeks)
- **Purpose:** Decide whether an opportunity is worth discovery investment.
- **Activities:** Capture the ask; estimate rough economics; score against portfolio priorities.
- **Instruments:** Intake template; triage scorecard.
- **Gate 1 (Discovery approved):** clear problem + pain owner; rough economics plausible; strategic fit; no obvious blocker (compliance/legal/data).

### Phase 1 — Discovery & Business Case (2–6 weeks)
- **Purpose:** Understand the as-is process, quantify pain, define success, size options.
- **Activities:** Process mapping (as-is/to-be); pain quantification with process owners; stakeholder & change-impact assessment; options identification (do nothing / improve / automate / transform); draft business case.
- **Instruments:** Value stream map; pain quantification sheet; stakeholder map; change impact assessment (draft); business case canvas; ROI model (org conventions).
- **Gate 2 (Business case approved & funded):** quantified baseline captured **before** deployment; ROI model signed by sponsor; option selected; budget allocated.

### Phase 2 — Solution Selection (2–8 weeks incl. procurement)
- **Purpose:** Choose the cheapest sufficient path: build, buy, or configure (incl. no-code / AI agents).
- **Activities:** Build-vs-buy analysis; vendor long-list and scorecard; PoC where needed; TCO over 3–5 years; contract/PO in place.
- **Instruments:** Build-vs-buy decision matrix; vendor scorecard (weighted); RFP checklist; PoC plan & evaluation script; TCO model.
- **Gate 3 (Delivery go-ahead):** solution selected; commercial agreed; security/architecture/compliance reviewed; delivery team identified.

### Phase 3 — Delivery & Governance (1–6 months typical)
- **Purpose:** Build/configure/test the solution in working increments, with enterprise guardrails.
- **Activities:** PRD → backlog; sprint delivery with demo cadence; RAID and risk management; vendor management; decision log; steering updates.
- **Instruments:** PRD; backlog/roadmap; RAID log; risk register; RACI; decision log; steering pack (1-pager); demo/sign-off record; UAT plan.
- **Gate 4 (Go-live):** UAT passed; security/compliance sign-off; support model ready; training & comms ready; rollout plan approved; adoption targets defined.

### Phase 4 — Adoption & Change (1–3 months, may overlap Phase 3)
- **Purpose:** Make the new way of working stick — the phase where internal automation typically fails.
- **Activities:** Executed comms plan; training; rollout wave plan; hypercare; adoption tracking; feedback loops.
- **Instruments:** Comms plan; training plan & materials checklist; rollout/hypercare checklist; adoption tracker.
- **Gate 5 (Value review / handover):** adoption target met or trajectory confirmed; support handed to operations; benefit baseline confirmed.

### Phase 5 — Value Realization & Continuous Improvement (recurring, quarterly)
- **Purpose:** Prove and grow value; decide to scale, adjust, or retire.
- **Activities:** Benefits tracking (planned vs actual); KPI dashboard; quarterly value review with sponsor; backlog of improvements; sunset/replace criteria.
- **Instruments:** Benefit realization tracker; KPI/OKR tree; quarterly value review pack.

---

## 3. Instrument list (grouped; ~20 starters)

| Group | Instrument | Used in | Owner |
|---|---|---|---|
| A. Economics | Intake template | P0 | EPO |
| A. Economics | Triage scorecard | P0 | EPO + portfolio |
| A. Economics | Business case canvas | P1 | EPO |
| A. Economics | ROI model (org conventions) | P1 | EPO + Finance |
| A. Economics | TCO model (3–5 yr) | P2 | EPO + Procurement |
| B. Analysis | Value stream map (as-is/to-be) | P1 | EPO + process owners |
| B. Analysis | Pain quantification sheet | P1 | EPO |
| B. Analysis | Build-vs-buy decision matrix | P2 | EPO + Architecture |
| C. Selection | Vendor scorecard (weighted) | P2 | EPO + Procurement |
| C. Selection | RFP checklist | P2 | Procurement |
| C. Selection | PoC plan & evaluation script | P2 | EPO + delivery |
| D. Delivery | PRD template | P3 | EPO |
| D. Delivery | Backlog / roadmap | P3 | EPO + delivery lead |
| D. Delivery | RAID log | P3 | EPO |
| D. Delivery | Risk register | P3 | EPO |
| D. Delivery | RACI matrix | P0–P3 | EPO |
| D. Delivery | Decision log | P0–P5 | EPO |
| D. Delivery | Steering pack (1-pager) | P3–P5 | EPO |
| E. Change | Stakeholder map (power-interest) | P1 | EPO |
| E. Change | Change impact assessment | P1 | EPO + HR/change |
| E. Change | Comms plan | P3–P4 | EPO + Comms |
| E. Change | Training plan & materials checklist | P4 | EPO + L&D |
| E. Change | Rollout / hypercare checklist | P4 | EPO + operations |
| F. Measurement | KPI tree / OKRs | P1, P5 | EPO + sponsor |
| F. Measurement | Benefit realization tracker | P5 | EPO |
| F. Measurement | Adoption tracker | P4–P5 | EPO |
| F. Measurement | Quarterly value review pack | P5 | EPO |

**Minimal viable set for week one** (do not start with 27): Intake, Business case canvas + ROI model, Value stream map, RAID log, Decision log, Steering pack, Adoption tracker, Benefit realization tracker. Add the rest as the team's projects demand.

**Tooling preferences:** process/value-stream mapping via **diagrams.net (draw.io), Confluence diagrams, or Figma** (not Miro). Backlog, docs, and dashboards per org standards.

**Templates available** (in `templates/`): Phase 0 — intake-template.md, triage-scorecard.xlsx · Economics — roi-model.xlsx, business-case-canvas.md · Selection — build-vs-buy-matrix.xlsx, vendor-scorecard.xlsx, rfi-rfp.md, poc-evaluation.md · Delivery — prd-template.md, raid-log.xlsx, decision-log.md, steering-pager.md · Change — stakeholder-map.md, change-impact-assessment.md, comms-plan.md, training-plan.md, rollout-hypercare-checklist.md · Measurement — adoption-tracker.xlsx, benefit-tracker.xlsx.

---

## 4. Governance & decision rights (to be completed in workshop)

- Steering cadence: monthly steering 1-pager; gate decisions at G2 and G4 (money and go-live); quarterly value reviews after launch.
- Decision rights: who approves each gate; who escalates; sponsor accountability.
- Compliance touchpoints: security review, architecture review, data protection review, EU AI Act literacy record (deployer role) — built into gates 2–4, not after.
- Reporting standard: one steering pack format; no bespoke decks.

---

## 5. Value & measurement standards

- ROI basis (confirm): 1 FTE = 2,080 h/yr; fully loaded $36k/yr.
- Measure **outcomes** (hours saved, cycle time, error rate, cost per transaction, capacity freed), not activity (users logged in, messages sent).
- Baselines captured **before** deployment; benefit claims require before/after evidence.
- Benefits re-validated quarterly post-launch; unachieved benefits are reviewed, not hidden.
- Every business case states: expected payback period, break-even trigger, and the kill/stop criteria.

---

## 6. Team workshop plan (3 × 90 min)

| Session | Goal | Agenda | Output |
|---|---|---|---|
| W1 — Role & Process | Validate role + lifecycle with the team's real context | Walk phases/gates; map 2–3 real current projects onto the model; find what's missing; agree definitions of done per gate | Adapted process map + gate criteria |
| W2 — Instrument Selection | Choose the toolkit | Review each instrument: keep / adapt / drop; assign template owners; decide where templates live (single source of truth); agree minimal set | Template library + owners |
| W3 — Governance & Metrics | Decision rights + measurement | Decision rights table; steering cadence & format; KPI definitions; ROI/benefit reporting standards | Charter + governance table + metric definitions |

Facilitation tips:
- Start from real projects, not theory — map current workflow first, then design to-be.
- Resist template inflation: if an instrument won't be used within a month, it's cut.
- Agree a "definition of done" for each gate before any template is finalized.

---

## 7. Principles & anti-patterns

1. **Product over project:** value continues after launch; handover ≠ end of accountability.
2. **Adoption is the product:** most internal automation failure is adoption, not technology. Budget change effort explicitly (comms, training, hypercare).
3. **Scope control:** automation projects die from creep. Tie scope to quantified benefits; stop criteria written into the business case.
4. **Measure before, not only after:** no baseline, no claim.
5. **One decision log:** no tribal knowledge; every steering decision recorded.
6. **Don't over-engineer the process itself:** the playbook must be cheaper than the value it protects.

---

## Open questions (need team input)
- Team size and per-person portfolio load (one project vs. several)?
- Existing PMO / delivery leads — who does what vs. the EPO?
- Existing tooling standards (backlog, docs, mapping, dashboards) to align to?
- Procurement involvement and thresholds for vendor purchases?
- Do EPOs also own AI/automation platform components (CoE-style), or only use-case products?
