# Research Notes — Seed Benchmarks (WS1 External)

Status: draft
Sources: web search (Aug 2026). All figures are **external benchmarks, not company data**.
Use in business case with labeled assumptions; validate against company specifics.

---

## 1. AI Customer Support — Deflection & Cost

| Metric | Value | Source |
|---|---|---|
| Realistic net org-wide cost reduction, year 1 | **20-35%** | Intercom/Fin, Lorikeet, Salesforce cross-refs |
| Median T1 deflection rate (enterprise) | **41.2%** (top quartile 58.7%, bottom 22.4%) | Zendesk CX Trends 2026 |
| Human-handled ticket cost | $6-13.50 (B2B high-tech: $28-35) | Gartner/IBM, aissist |
| AI resolution cost | $0.50-2.00 | Gartner/IBM |
| Per-ticket cost reduction on AI-eligible tickets | 85-95% | vendor data (eligible subset only) |
| AI customer service ROI | ~$3.50 per $1 invested; 3-6 mo payback; leaders to 8x | Intercom/Fin |
| Self-service vs agent-assisted contact | $1.84 vs $13.50 (7.3x) | Gartner |

**Interpretation:** Vendor headlines (70-90% deflection) apply to AI-eligible tickets only.
For business case modeling use: **eligible-ticket share × per-ticket savings**, and expect
**20-35% net org-wide support cost reduction in year 1** after infrastructure/licensing.

## 2. SaaS Cost Structure — % of ARR (private B2B SaaS, 2026)

| Function | % of ARR (median) |
|---|---|
| R&D | 22% |
| Selling | 15% |
| G&A | 15% |
| Customer support + success | 9% |
| Marketing | 8% |
| Hosting | 5% |
| Pro services CoGS | 5% |
| Other CoGS | 3% |

Source: SaaS Capital spending benchmarks 2026. Also: ARR/employee ~$130K; CAC ~$2.00 per
$1 of new ARR (saasmag 2026).

**Interpretation for cost-focused AI:** the three biggest labor pools are R&D (22%), Sales
(15%), G&A (15%). Support (9%) is small but has the fastest, most measurable AI payback
(3-6 months). Classic strategy: use support + dev productivity for quick wins, then attack
S&M and G&A for scale.

## 3. Developer Productivity — AI Copilots

| Study | Result |
|---|---|
| GitHub (Copilot research) | ~26% faster on repetitive tasks (self-report + telemetry) |
| arXiv 2509.20353v2 (controlled) | 55.8% faster task completion; gains larger for junior devs |
| Microsoft paper | up to 40% (context-dependent) |

**Interpretation:** Heterogeneous. Realistic modeling band for business case: **15-30%
productivity lift on coding tasks**, higher for junior devs and boilerplate-heavy work.
Don't assume 40%+ org-wide.

## 4. EU AI Act — Status as of Aug 2026 (relevant for a SaaS vendor)

| Date | Event |
|---|---|
| 2 Aug 2026 | Article 50 transparency obligations in force (providers + deployers, incl. open-source); AI Office GPAI enforcement active — **not delayed** |
| 2 Aug 2026 | High-risk (Annex III) obligations originally due — **delayed** (Digital Omnibus); standards expected late 2026 |
| 2 Dec 2026 | Machine-readable marking: grace for systems on market before 2 Aug 2026 |

**Interpretation:** A SaaS vendor embedding AI in product faces transparency duties NOW.
High-risk classification timing is still evolving. Governance framework must include
AI-generated content marking + transparency, plus vendor/deployer duties. Sources:
artificialintelligenceact.eu, softwareimprovementgroup.com, snowflake.com (2026).

---

## TODO (full research pass, WS1)
- Competitive AI adoption by peer SaaS companies (top 5-8 reference peers)
- Vendor landscape per function: support AI, dev copilots, marketing ops, finance ops, internal RAG
- LLM provider pricing + cost per token / per seat benchmarks (2026)
- EU AI Act detailed mapping to SaaS product categories
- Benchmark validation: company's own cost structure vs these medians
