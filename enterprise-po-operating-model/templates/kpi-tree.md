# KPI Tree / OKRs — <Product / Portfolio>

**Purpose:** Connect the top-level outcome to the measures that drive it — so the team measures *outcomes* (not activity) and every KPI has a definition, source, and owner (matches playbook §5 standards).

## 1. Outcome (top of the tree)

**<e.g. Reduce invoice processing cost per transaction by 50% within 12 months of go-live>**

## 2. KPI tree (outcome → drivers → measures)

```
OUTCOME: Cost per transaction −50%
├── Driver: Processing speed
│   ├── KPI: Cycle time per invoice (min)
│   └── KPI: Throughput per clerk (invoices/h)
├── Driver: Quality
│   ├── KPI: Rework rate (%)
│   └── KPI: Error-related credits/penalties ($)
├── Driver: Adoption
│   ├── KPI: Active users (weekly)
│   └── KPI: % of transactions through automation
└── Driver: Cost
    ├── KPI: Hours saved (h/mo) → $ at org rate
    └── KPI: Cost per transaction ($)
```

## 3. KPI definitions

| KPI | Definition (what exactly) | Formula / source | Baseline | Target | Owner | Cadence |
|---|---|---|---|---|---|---|
| Cycle time | Time from invoice receipt to booked | System timestamps, avg monthly | 15 min | 6 min | Process owner | Monthly |
| Rework rate | Share of invoices needing manual correction | QA log | 12% | 3% | Process owner | Monthly |
| Active users | Users with ≥1 action in the tool per week | Tool analytics | 0 | 40 | EPO | Weekly |
| Hours saved | Manual hours avoided, measured from logs | Bot logs × avg time | 0 | 312 h/mo | EPO | Monthly |
| Cost per transaction | Total process cost ÷ transactions | Finance data | $2.50 | $1.10 | Finance | Quarterly |

## 4. Optional OKR framing (if the team runs OKRs)

**Objective:** <outcome statement>

| Key result | Owner | Target | Status |
|---|---|---|---|
| KR-1 | | | |
| KR-2 | | | |
| KR-3 | | | |

## 5. Rules

- **No activity metrics** (logins, messages sent) — measure outcomes only.
- Every KPI has exactly one owner and one source. "We'll figure it out" is not a source.
- Baselines captured before deployment (playbook §5).
- KPI tree reviewed quarterly in the value review; dead KPIs are retired, not kept for decoration.
- Feeds: benefit-tracker.xlsx (actuals), steering-pager.md (top metrics).
