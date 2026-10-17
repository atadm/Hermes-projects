# AI Agent Data Access — Architecture Design

## Problem

Customer Success agents need to answer client questions (contracts, invoices, amounts) using data scattered across CRM, billing, contracts, and a data warehouse (24h freshness). AI agents can automate this — but the critical question is **how to give them data access without exposing data the client shouldn't see.**

## Core Principle

**Never give the agent direct database or API access.** Every data access goes through a permission-checking gateway function that verifies authorization before returning data.

---

## Approach Comparison

| Dimension | Warehouse (Options A/B) | Source APIs Only (Option C) |
|---|---|---|
| **Permission freshness** | ⚠️ Up to 24h stale if not decoupled | ✅ Real-time per system |
| **Data freshness** | ⏱ 24h SLA (acceptable per spec) | ✅ Real-time per system |
| **Implementation effort** | ✅ 1 integration (warehouse) + cache | ⚠️ N integrations (CRM, billing, contracts…) |
| **Business logic fidelity** | ⚠️ ETL may strip calculated fields | ✅ Native system logic |
| **Blast radius (gateway failure)** | ⚠️ Single point — all data types | ✅ Per-system isolation |
| **Audit trail clarity** | ⚠️ Warehouse row → source join needed | ✅ Direct per-access log |

## Option A: Warehouse + Real-Time Permission Cache (Recommended)

**Flow:** Client Email → Intent Classifier → Permission Gateway → Data Warehouse → Response Composer

- Permission cache updated from source systems every 15 minutes (near-real-time)
- Business data from warehouse (24h freshness — acceptable per spec)
- **Best balance of simplicity and security for getting started**
- **Critical rule:** Never let the warehouse supply permission data

## Option B: Warehouse + Source API Fallback

**Flow:** Client Email → Intent Classifier → Router → (Warehouse or Source APIs) → Permission Check → Response

- Warehouse for common queries
- Falls back to source-system APIs when real-time data is needed
- Best for: scenarios where 24h freshness creates risk but most queries are fine with the warehouse

## Option C: Source APIs Only (Maximum Security)

**Flow:** Client Email → Intent Classifier → Permission Check → CRM / Billing / Contracts APIs (parallel) → Audit Log → Response

- Every data request hits source systems directly
- Each API call carries its own permission check
- Full audit trail per system
- Most secure — but requires N separate integrations

## Recommendation

**Start with Option A.** It gives the quickest path to production with the strongest security-to-effort ratio. If the use case later demands real-time data for specific scenarios, add Option B's fallback per request type.

---

*Project: agent-data-access · Hermes-projects · 17 Oct 2026*