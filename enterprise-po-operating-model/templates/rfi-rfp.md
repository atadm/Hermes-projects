# RFI / RFP Pack — <Requirement / Project>

**Purpose:** Structured vendor discovery (RFI) and formal solicitation (RFP) for Phase 2 solution selection. RFI first (broad market scan) → vendor scorecard shortlist → RFP + PoC for the top candidates.

**Owner:** <EPO> with Procurement · **Timeline:** RFI 2–3 weeks · RFP 3–4 weeks

---

## Part A — RFI template (what vendors receive)

### 1. Introduction
- Company background (1 paragraph) and why we're exploring this capability
- Project context and objectives (from the business case, de-identified)
- Expected timeline and procurement process overview

### 2. Scope of requirements

Ask vendors to respond to each category with **meets / partially meets / does not meet** + evidence:

| # | Category | Requirement areas to cover |
|---|---|---|
| 1 | Functional | Core workflows, user roles, reporting, config without code |
| 2 | Technical | Architecture, APIs, data model, integration options, hosting model |
| 3 | Security & compliance | Certifications (ISO 27001, SOC 2), data residency, EU AI Act posture, auditability, DPA readiness |
| 4 | Commercial | Pricing model, licensing, TCO inputs, contract terms, exit clause |
| 5 | Implementation | Effort estimate, methodology, timeline, partner requirements |
| 6 | Support & SLAs | Support tiers, response times, uptime commitments |
| 7 | Roadmap & stability | Company, funding, product roadmap, recent releases |
| 8 | References | 2–3 customer references in similar size/industry, with use cases |

### 3. Response format
- Max <N> pages, structured per the categories above
- Pricing in a separate commercial annex
- Deadline and contact point

### 4. Evaluation notice
- Responses scored against the vendor scorecard (weighted criteria)
- Shortlisted vendors invited to demo / PoC — no purchase commitment from an RFI response

---

## Part B — RFP checklist (internal, before issuing)

- [ ] RFI responses received and scored (vendor-scorecard.xlsx) → shortlist top 2–3
- [ ] Requirements frozen in the PRD — RFP goes out only against agreed requirements
- [ ] Commercial framework aligned with Procurement (pricing model, term, exit, SLA)
- [ ] Legal/compliance pre-check: DPA, data residency, EU AI Act obligations in scope
- [ ] RFP document drafted: background, requirements (from Part A §2), evaluation criteria + weights, timeline, T&Cs
- [ ] Vendor Q&A session scheduled (same answer to all — no bilateral side deals)
- [ ] PoC criteria pre-agreed (see poc-evaluation.md) — announced in the RFP
- [ ] Reference call template prepared (2 calls per shortlisted vendor)
- [ ] Scoring panel named (EPO, procurement, architecture, process owner)
- [ ] Decision and contract authority confirmed (who signs, at which gate)

---

## Part C — Commercial comparison notes

- Collect all pricing in the same unit (annual, all-in) — normalize before comparing.
- TCO = license + implementation + integration + training + internal maintenance (3-yr). Feed into ROI model.
- Exit clause matters: data export, contract termination, migration assistance — score it explicitly.

---
*RFI/RFP artifacts stay in Procurement's records; the scorecard, PoC report, and decision log carry the outcome into Gate 3.*
