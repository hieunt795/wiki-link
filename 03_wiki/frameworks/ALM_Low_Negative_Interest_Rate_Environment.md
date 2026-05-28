---
node_id: alm_low_negative_interest_rate_environment_001
type: framework
title: ALM in a Low/Negative Interest Rate Environment
aliases:
  - low rate ALM
  - negative rate ALM
  - deposit beta ALM
  - floor risk banking book
  - margin compression low rates
  - ALM lãi suất thấp âm
  - rủi ro sàn tiền gửi
  - beta tiền gửi lãi suất thấp
  - nén biên lãi suất môi trường lãi thấp
domain:
  primary: alm
  secondary: []
tags:
  - low-rate
  - negative-rate
  - deposit-beta
  - floor-risk
  - node: "[[NII]]"
    relation: related_to
  - node: "[[EVE]]"
    relation: related_to
  - margin-compression
  - swaption
  - interest-rate-floor
  - node: "[[IRRBB]]"
    relation: related_to
  - node: "[[ALM]]"
    relation: related_to
confidence: 1
stability: stable
thesis: >
  In a low/negative interest rate environment, ALM faces a structural dilemma because
  deposit beta collapses near zero (breaking standard rate-sensitivity models), retail
  deposits cannot be priced below zero creating a floor risk that produces nonlinear
  NII losses in negative rate scenarios, and countermeasures — including receiver
  swaptions, interest rate floors, fee introduction, and maturity extension — involve
  explicit trade-offs between NII stability (balance sheet A) and EVE stability
  (balance sheet B). [LLM]
source_refs:
  - path: "02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md"
    pages: "Chapter 10: ALM in a Low/Negative Interest Rate Environment"
related:
  - node: "[[NMD_Stochastic_Three_Factor_Model]]"
    relation: related_to
  - node: "[[NMD_Decay_Model_Volume_Segmentation]]"
    relation: related_to
  - node: "[[IRRBB_Standardised_Versus_Internal_Model_Approach]]"
    relation: related_to
  - node: "[[ILAAP_Supervisory_Liquidity_Framework]]"
    relation: related_to
date_created: "2026-05-28"
date_updated: "2026-05-28"
---

## Thesis

In a low/negative interest rate environment, ALM faces a structural dilemma because deposit beta collapses near zero, breaking standard rate-sensitivity models, and retail deposits cannot be priced below zero, creating floor risk that produces nonlinear NII losses. [LLM] Countermeasures involve explicit trade-offs between NII stability and EVE stability. [LLM]

## Deposit Beta — Definition and Breakdown Near Zero

**Deposit beta** (β_deposit) measures the pass-through of market rate changes to client deposit rates: [LLM]

> **β_deposit = Δclient_rate / Δmarket_rate** [LLM]

In normal rate environments: [LLM]
- Current accounts: β ≈ 0 (rate-insensitive, not repriced with market moves). [LLM]
- Savings accounts: β ≈ 0.3–0.6 (partial pass-through). [LLM]
- Rate-sensitive deposits / term deposits: β ≈ 0.8–1.0. [LLM]

**Near-zero rate breakdown:** [LLM]

- As market rates approach zero, the correlation between market rate changes and client rate changes collapses because client rates are already at or near their practical floor. [LLM]
- The standard regression model (client_rate = α + β × market_rate) produces unreliable beta estimates when the dependent variable (client rate) is censored at zero. [LLM]
- Calibration error: beta calibrated in a 2–5% rate regime will systematically underestimate the NII impact of rate cuts in a 0–0.5% regime. [LLM]

## Floor Risk Mechanics

**Floor risk** is the exposure arising from the inability to price retail deposits below 0%: [LLM]

- If market rates = −0.5%, a bank ideally would pay depositors −0.5% on deposits (charging them). [LLM]
- In practice, retail depositors withdraw cash or switch to zero-rate current accounts rather than accept negative rates. [LLM]
- The bank therefore bears a **negative carry** on the deposit portfolio: it funds itself at 0% (client rate floor) but invests in assets yielding negative market rates. [LLM]
- The cost = −market_rate × deposit_volume (when market_rate < 0). [LLM]

This is equivalent to being **long an embedded interest rate floor** (strike = 0%) on the total deposit volume. [LLM]

## NII Impact: Balance Sheet A vs Balance Sheet B

The textbook contrasts two stylized balance sheets to illustrate the NII/EVE trade-off: [LLM]

| Metric | Balance Sheet A (NII-stable) | Balance Sheet B (EVE-stable) |
|--------|------------------------------|------------------------------|
| Strategy | Long-duration assets, short liabilities | Short-duration assets, match-funded |
| ΔNII in −100bp shock (low-rate environment) | **−0.8** | **−1.0** |
| ΔEVE in +200bp shock | Higher loss | Lower loss |
| Countermeasure needed | Receiver swaptions / floors to protect NII floor | Limited; EVE already stable |

[LLM]

Balance sheet A suffers less EVE loss in rate-down scenarios but loses NII when rates turn negative due to floor risk on liabilities and reinvestment at negative yields on assets. [LLM] The ordering of NII impact can reverse in low-rate environments compared to normal rate scenarios. [LLM]

## Countermeasures and Their Trade-offs

### 1. Fee Introduction

- Replace interest income lost to floor risk with explicit account fees (monthly maintenance fees, transaction fees). [LLM]
- Offsets NII compression without requiring balance sheet restructuring. [LLM]
- Risk: depositor attrition if fee levels are above market norms. [LLM]

### 2. Maturity Transformation Extension

- Extend asset duration to capture higher yields further out on the curve. [LLM]
- Increases EVE sensitivity to rate rises (Pillar 2 EVE risk increases). [LLM]
- May push the bank toward the supervisory outlier test threshold. [LLM]

### 3. Higher Asset Margins (Loan Pricing)

- Pass negative funding cost benefits to new loan origination at higher spreads to compensate NII. [LLM]
- Constrained by competitive pricing pressures in the lending market. [LLM]

### 4. Asymmetric Derivatives

- **Receiver swaptions:** right to receive fixed / pay floating at a future date; profitable when rates fall further (negative carry environment deepens). [LLM]
- **Interest rate floors:** provide payoff when the reference rate falls below the strike (typically 0%); directly hedge the embedded deposit floor. [LLM]
- Both instruments protect NII downside but cost premium upfront and reduce EVE gains if rates normalize upward. [LLM]

## Stress Test Flooring Issue

Standard IRRBB stress testing applies a **0% floor** on the shocked interest rate path: rates cannot go below zero in the scenario. [LLM] In a low/negative rate environment, this flooring masks the true downside NII risk: [LLM]

- If market rates are already at −0.5%, a −100bp shock floored at 0% is evaluated at max(−0.5% − 1%, 0%) = 0%, implying no further rate decline. [LLM]
- This understates the NII risk of further rate cuts below zero. [LLM]
- The ECB **removed the 0% floor** in its 2017 IRRBB sensitivity analysis for significant institutions, requiring banks to model genuine negative rate scenarios. [LLM]
- Banks must now stress-test NII under scenarios where market rates remain deeply negative for an extended period. [LLM]

---
*Source: Chapter 10 of Elkenbracht-Huizing, "The Handbook of ALM in Banking" (2nd ed., Risk Books 2017). All body sentences tagged [LLM] are synthesized from source material. Confidence: 1.*
