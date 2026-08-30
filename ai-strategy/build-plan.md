# AI Strategy — Research & Analysis Plan

Status: draft
Owner: Tom (Hermes agent) + Antonina
Version: 0.1 (2026-08-26)

---

## 1. Purpose

Produce an actionable AI Strategy for a mid-size SaaS company (250-1,000 FTEs) whose
primary objective is **cost reduction and operational efficiency**, leveraging an
already-mature data platform. Draft target: **~4 weeks**.

## 2. Company profile (confirmed)

| Dimension | Profile |
|---|---|
| Industry | Technology / SaaS / Software |
| Size | 250-1,000 employees |
| Digital maturity | Advanced — cloud-native, mature data platform, analytics/BI in place |
| Primary objective | Cost reduction / operational efficiency |
| Timeframe | Draft within weeks |

**Strategic implications**

1. **Baseline phase compresses.** The data platform exists; the assessment shifts from
   "do we have data infrastructure?" to "where do costs live and which processes are AI-ready?".
2. **Cost structure is the map.** Efficiency AI should target the 20% of cost centers that
   produce 80% of the opportunity. For SaaS, the usual heavy clusters:
   - Engineering / R&D (~30-40% of cost) — developer productivity, QA, documentation
   - Sales & marketing (~25-35%) — content, lead ops, deal support
   - G&A / back-office (~15-20%) — finance ops, legal, HR, IT
   - Customer support (~10-15%) — deflection, agent assist, triage
3. **Product-side AI is secondary but worth scanning.** A pure internal-cost play may
   underuse the company's data assets; we scan for embedded-AI quick wins but do not make
   them the strategy's spine.
4. **Governance is a first-class concern.** As a SaaS vendor, the company's own AI policy
   governs both internal use and its product roadmap (EU AI Act exposure, data residency).

## 3. Deliverables

| # | Deliverable | Format |
|---|---|---|
| D1 | AI Strategy document | `design.md` (primary artifact) |
| D2 | Use case inventory + prioritization matrix | `docs/use-cases.md` + scorecard |
| D3 | Quick-win roadmap (0-3-6-12-18 months) | `docs/roadmap.md` |
| D4 | Business case model (cost savings, investment, ROI, payback) | `docs/business-case.xlsx` |
| D5 | Governance & responsible AI framework | `docs/governance.md` |
| D6 | Executive summary presentation | `docs/exec-summary.md` (deck-ready) |

## 4. Workstreams & timeline (~4 weeks)

### WS1 — Baseline & context (Week 1, compressed)

**Internal (needs company input)**
- Cost structure by function (approx. % of opex; or headcount + loaded cost)
- Current tooling inventory: which SaaS/cloud tools, which already ship AI features
- Existing AI usage incl. shadow AI (ChatGPT/Claude/GitHub Copilot adoption)
- Process hotspots: recurring manual work, known bottlenecks, ticket volumes
- Stakeholder inputs: COO, CFO, Heads of Support / Eng / Sales / Marketing / People

**External research (I can start now, no dependencies)**
- SaaS cost benchmarks by function (% of revenue, typical ratios)
- AI efficiency benchmarks: support deflection rates, dev productivity gains, ops savings
- Competitive AI adoption by peer SaaS companies

**Exit criteria:** cost map by function + AI-readiness snapshot + external benchmarks.

### WS2 — Opportunity identification (Week 2)

- Build use case inventory (target 20-30) across support, eng, marketing, sales, finance, legal, HR, IT
- Score each on: cost impact, feasibility, data readiness, risk, time-to-value, capex/opex
- Shortlist top 5-8 use cases with rough business cases (assumptions labeled)
- Classify: quick wins (<3 mo), build bets (3-12 mo), strategic (12+ mo)

**Exit criteria:** prioritized shortlist + top-3 quick wins validated with owners.

### WS3 — Strategy formulation (Week 3)

- Vision, mission, guiding principles
- Target architecture: how AI lands on the existing data platform
  (data platform → feature/vector store → LLM ops / MLOps → applications)
- Build vs buy decisions per use case cluster (vendor landscape from WS1 research)
- Governance & responsible AI: policy, risk, compliance, vendor risk, EU AI Act mapping
- Talent & enablement: roles (AI PM, ML engineer, prompt/LLM ops), center-of-excellence
  vs embedded model, upskilling plan, partner model
- Investment case: TCO, cost savings model, ROI, payback, phasing

**Exit criteria:** draft strategy sections, each internally consistent and quantified where possible.

### WS4 — Synthesis & delivery (Week 4)

- Integrate into D1-D6
- Stress-test assumptions: sensitivity on savings %, adoption ramp, licensing costs
- Review with stakeholders; finalize

**Exit criteria:** all deliverables complete, reviewed, ready for exec presentation.

## 5. Immediate next steps

1. **I run external research now** (benchmarks, competitor AI plays, vendor landscape) —
   no company input required. ~1-2 days.
2. **Company provides** (to unblock WS1 internal):
   - Cost structure by function (or headcount + loaded cost)
   - Current tool inventory + which already have AI features
   - Support ticket volume + cost per ticket (if available)
   - Who should be interviewed (COO / CFO / functional heads)
3. **Kickoff interview plan** — 5-8 x 30-45 min stakeholder sessions in Week 1.

## 6. Assumptions (to be validated)

- Cost structure data will come from company (labeled estimates if not).
- Primary objective stays cost/efficiency; product-side AI treated as secondary scan.
- Mature data platform means no major data-infrastructure build required (verify in WS1).
- AI licensing/vendor budget is not yet fixed — business case will model ranges.

## 7. Risks & mitigations

| Risk | Mitigation |
|---|---|
| Savings overestimated | Sensitivity analysis; pilot-then-scale; label assumptions |
| Shadow AI sprawl | Governance framework covers acceptable use + tools |
| No internal ownership for interviews | Stakeholder map + exec sponsorship confirmed in kickoff |
| EU AI Act / data residency (SaaS vendor) | Compliance mapping in governance workstream |
| Scope creep toward product AI | Keep product AI as secondary scan; explicit non-goals |
