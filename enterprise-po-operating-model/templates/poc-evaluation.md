# PoC Plan & Evaluation — <Vendor / Solution>

**Purpose:** Prove the top candidate(s) on the team's real scenarios before committing at Gate 3. A PoC answers "does it actually work for OUR process, with OUR data, at OUR volume" — not "is it a nice demo."

**Owner:** <EPO> · **Duration:** 2–4 weeks · **Scope:** top 2 vendors max (see vendor-scorecard.xlsx)

---

## 1. Objectives

- Verify the top 2–3 must-have requirements end-to-end on real scenarios
- Measure effort to configure/integrate (drives implementation estimate)
- Test edge cases that the sales demo didn't cover
- Evaluate usability with 2–3 real users from the process team

## 2. Success criteria (agree BEFORE the PoC starts)

| # | Must-have scenario | Success = | Evidence |
|---|---|---|---|
| 1 | <e.g. invoice capture + validation> | <e.g. 95% auto-extraction accuracy> | <test log / screenshot> |
| 2 | <e.g. integration with ERP sandbox> | <e.g. round-trip in < 5 min, no data loss> | <integration test result> |
| 3 | <e.g. exception handling> | <e.g. clear error path, no silent failures> | <demo walkthrough> |
| 4 | <e.g. user role + access control> | <e.g. matches our security model> | <config review> |

Separate **must-have** (fail = vendor out) from **nice-to-have** (inform final choice only).

## 3. Evaluation script (scenarios)

- Use **real anonymized data** from our process, not vendor sample data
- Cover: happy path, exception path, volume spike, restart/recovery, concurrent users
- Each scenario: steps, data needed, expected outcome, pass/fail criteria, owner

## 4. Scoring

| Criterion | Weight | Vendor A | Vendor B | Evidence |
|---|---|---|---|---|
| Must-have requirements met | 40% | | | from script results |
| Configuration effort | 20% | | | hours logged by team |
| Usability (users' verdict) | 15% | | | user feedback sheet |
| Integration quality | 15% | | | test results |
| Support responsiveness during PoC | 10% | | | response log |

Score 1–5. Weighted total feeds the final Gate 3 decision (with the vendor scorecard and commercial terms).

## 5. Decision rules

- Any must-have failure → vendor disqualified, regardless of score
- If both vendors pass: choose on weighted score + commercial + reference calls; gap < 0.3 → escalate the tie to sponsor
- Decision recorded in Decision Log with rationale; result goes to Gate 3

## 6. Timeline

| Week | Activity |
|---|---|
| 1 | Kickoff, environment setup, data preparation |
| 2 | Scenarios 1–2, integration work |
| 3 | Scenarios 3–4, usability session, support test |
| 4 | Scoring, report, Gate 3 decision |

## 7. Outputs

- [ ] PoC report per vendor (scenario results, effort log, user feedback)
- [ ] Weighted score comparison
- [ ] Updated implementation estimate for the business case
- [ ] Decision Log entry + Gate 3 pack
