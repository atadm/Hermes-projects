# AI Strategy — Design (Strategy Truth)

Status: draft (placeholder — to be filled through WS1-WS4)
This document is the primary AI Strategy artifact. It wins over README.md on conflicts.

---

## 1. Vision & objectives

_To be drafted (WS3)._ Working premise: apply AI to meaningfully reduce operating cost and
lift efficiency across the business, then extend to product value where quick wins exist.

## 2. Current state summary

_To be drafted (WS1)._ Expected contents: cost map by function, AI readiness, tooling,
external benchmarks.

## 3. Prioritized opportunity portfolio

_To be drafted (WS2)._ Expected contents: top 5-8 use cases, value×feasibility scorecard,
quick-win vs build-bet vs strategic classification.

## 4. Target architecture

_To be drafted (WS3)._ Working blueprint:

```
Existing data platform (mature)
        │
        ├── Feature / vector store  ──►  LLM ops / MLOps layer
        │                                    │
        └── Integration layer ──────────────┤
                                             ▼
        Business applications: support AI, eng copilots, marketing ops,
        finance ops, internal knowledge / RAG, agentic workflows
```

Key decisions to record: build vs buy per cluster, LLM provider(s), model ops approach,
data residency, security boundaries, vendor risk.

## 5. Governance & responsible AI

_To be drafted (WS3)._ Expected contents: policy, acceptable use, risk framework,
EU AI Act mapping (company is a SaaS vendor), vendor assessment, data governance.

## 6. Talent & enablement

_To be drafted (WS3)._ Expected contents: target roles, operating model (CoE vs embedded),
upskilling, partner model.

## 7. Investment case

_To be drafted (WS3-WS4)._ Expected contents: TCO, savings model, ROI, payback, phasing,
sensitivity analysis.

## 8. Roadmap

_To be drafted (WS3)._ Horizons: quick wins (0-3 mo) → scale (3-12 mo) → transform (12-18 mo).

## 9. KPIs & measurement

_To be drafted (WS3-WS4)._ Per-initiative metrics + portfolio-level AI ROI dashboard.

## 10. Appendix

- Use case inventory & scorecard
- Vendor landscape
- Benchmark sources
- Interview notes
