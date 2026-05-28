---
node_id: credit_spread_risk_banking_book_csrbb_001
type: concept
title: Credit Spread Risk in the Banking Book (CSRBB)
aliases:
  - node: "[[CSRBB]]"
    relation: related_to
  - credit spread risk banking book
  - hazard rate model CSRBB
  - OAS banking book
  - reduced-form credit model ALM
  - rủi ro chênh lệch tín dụng sổ ngân hàng
  - CSRBB mô hình tỷ lệ rủi ro
  - OAS sổ ngân hàng
domain:
  primary: alm
  secondary: []
tags:
  - node: "[[CSRBB]]"
    relation: related_to
  - credit-spread
  - hazard-rate
  - reduced-form
  - node: "[[OAS]]"
    relation: related_to
  - node: "[[IRRBB]]"
    relation: related_to
  - node: "[[IFRS9]]"
    relation: related_to
  - duration
  - node: "[[LGD]]"
    relation: related_to
  - node: "[[ALM]]"
    relation: related_to
confidence: 1
stability: stable
thesis: >
  CSRBB is the sensitivity of banking book economic value to changes in credit
  spreads independent of default events, measured via three modelling approaches
  (cashflow/hazard rate, credit-spread-adjusted discount, and OAS) that each imply
  different effective durations; the cashflow model most accurately captures duration
  shortening from default-contingent early termination, while the OAS model
  overstates duration by ignoring it. [LLM]
source_refs:
  - path: "02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md"
    pages: "Chapter 11: Credit Spread Risk in the Banking Book"
related:
  - node: "[[IRRBB_Standardised_Versus_Internal_Model_Approach]]"
    relation: related_to
  - node: "[[Hedge_Accounting_IFRS9_ALM]]"
    relation: related_to
  - node: "[[Interest_Rate_Basis_Risk_Measurement_ALM]]"
    relation: related_to
date_created: "2026-05-28"
date_updated: "2026-05-28"
---

## Thesis

CSRBB is the sensitivity of banking book economic value to changes in credit spreads independent of default events. [LLM] Three modelling approaches each imply different effective durations: the cashflow/hazard rate model is most accurate as it captures duration shortening from default-contingent early termination; the OAS model overstates duration by ignoring this effect. [LLM]

## Definition and Scope

**CSRBB** = the risk that the market value of a banking book instrument changes due to a widening or tightening of credit spreads, even in the absence of an actual default. [LLM]

BCBS IRRBB Principle 2 requires that CSRBB be monitored and managed separately from IRRBB proper (interest rate risk from risk-free rate movements). [LLM] Key distinctions: [LLM]

- **IRRBB** = sensitivity to risk-free interest rate changes (OIS/government curve). [LLM]
- **CSRBB** = sensitivity to issuer/sector credit spread changes (corporate spread, covered bond spread, sovereign spread above risk-free). [LLM]
- **Credit risk** = probability of default and expected loss → captured separately in ECL (IFRS 9) and credit RWA. [LLM]

## Reduced-Form Valuation Framework

In the reduced-form approach, the yield on a defaultable instrument is decomposed as: [LLM]

> **R(t) ≈ r(t) + λ(t) × L(t)** [LLM]

Where: [LLM]
- r(t) = risk-free short rate (OIS) [LLM]
- λ(t) = hazard rate (instantaneous default probability per unit time) [LLM]
- L(t) = Loss Given Default (LGD), fraction of notional lost on default [LLM]
- λ(t) × L(t) = default-adjusted credit spread [LLM]

The default-adjusted discount rate thus equals the risk-free rate plus the expected loss rate per period. [LLM]

## Three CSRBB Modelling Approaches

### Approach 1: Cashflow / Hazard Rate Model

- Cash flows are probability-weighted by survival probability: CF_k × Π(1 − λ_m dt) for m up to k. [LLM]
- On default (probability λ dt per period), the cashflow terminates early and recovers R × notional at that point. [LLM]
- **Duration effect:** early termination on default reduces the effective duration below that of a comparable risk-free bond. [LLM]
- High recovery rate → shorter expected duration (more recovery cashflows arrive early on default). [LLM]
- This is the most theoretically correct approach: it integrates credit risk directly into the cash flow timing model. [LLM]

### Approach 2: Credit-Spread-Adjusted Discount Model

- Cash flows are discounted at r(t) + credit_spread without adjusting the timing or probability of cash flows. [LLM]
- A wider spread → higher discount rate → lower PV, giving a credit spread sensitivity. [LLM]
- **Duration error:** this approach ignores the truncation of cash flows on default, so it **overstates effective duration** relative to the cashflow model, particularly at high recovery rates. [LLM]
- Simple to implement but systematically biases CSRBB sensitivity upward. [LLM]

### Approach 3: OAS (Option-Adjusted Spread) Model

- The OAS is calibrated so that the model price = market price after stripping out embedded optionality (calls, prepayment). [LLM]
- Sensitivity to a shift in OAS gives the CSRBB measure. [LLM]
- **Duration effect:** the OAS approach implicitly treats the instrument as having the full duration of the contractual cash flows, ignoring default-contingent termination. [LLM]
- This produces the **longest effective duration** of the three approaches, and therefore overstates CSRBB sensitivity the most. [LLM]
- Appropriate for instruments where optionality (not credit) is the primary concern; less accurate for pure credit spread risk. [LLM]

## Duration Comparison Across Approaches

For a hypothetical corporate bond with moderate recovery rate (LGD = 40%): [LLM]

| Approach | Relative Duration | Recovery Rate Effect |
|----------|------------------|----------------------|
| Cashflow / hazard rate | Shortest (most accurate) | High recovery → shorter duration |
| Credit-spread-adjusted discount | Medium | Recovery rate ignored |
| OAS model | Longest (overstates sensitivity) | Recovery rate ignored |

[LLM]

## Interaction with Interest Rate Risk

The relationship between credit spreads and interest rates is generally second-order for IRRBB measurement purposes but becomes important in stress scenarios: [LLM]

- **Macro linkage:** in recession scenarios, credit spreads widen simultaneously with central bank rate cuts (flight to quality). [LLM]
- **Unemployment → default intensity:** rising unemployment increases hazard rates λ(t). [LLM]
- **LTV → recovery rates:** falling collateral values reduce L in real estate portfolios. [LLM]
- **GDP growth:** declining growth widens corporate credit spreads across the board. [LLM]

These correlations mean that CSRBB stress scenarios must be consistent with the macro scenario driving the IRRBB stress, particularly in ICAAP and ILAAP stress testing. [LLM]

## IFRS 9 Double-Counting Avoidance

IFRS 9 Expected Credit Loss (ECL) provisions reduce the carrying value of financial assets for credit deterioration. [LLM] When measuring CSRBB-driven changes in economic value of equity (EVE), the credit-spread-driven revaluation must not double-count provisions already recognized in the P&L: [LLM]

- For assets on amortised cost: the credit risk is captured in ECL, not in fair value; CSRBB is largely not applicable (unless the bank also computes a "shadow" economic value). [LLM]
- For FVOCI instruments: credit-spread changes are recognized in OCI; CSRBB and IFRS 9 ECL interact in the regulatory capital calculation (unrealized OCI gains/losses flow through CET1). [LLM]
- ALM must ensure that the CSRBB EVE calculation and IFRS 9 ECL provisions are not summed as independent risks for capital purposes. [LLM]

---
*Source: Chapter 11 of Elkenbracht-Huizing, "The Handbook of ALM in Banking" (2nd ed., Risk Books 2017). All body sentences tagged [LLM] are synthesized from source material. Confidence: 1.*
