---
node_id: income_gap_vs_economic_value_gap_001
type: concept
title: Income Gap vs Economic Value Gap — Dual IRRBB Perspectives
aliases:
- NII vs EVE dual view
- Earnings perspective vs economic value perspective
- Delta NII vs Delta EVE
- IRRBB dual metric
- góc nhìn kép IRRBB
- NII so với EVE trong quản lý IRRBB
domain:
  primary: alm
  secondary:
  - basel_risk
tags:
- irrbb
- nii
- eve
- gap_analysis
- interest_rate_risk
- dual_view
- hedging
confidence: 1
stability: stable
thesis: '[LLM] The two IRRBB measurement perspectives — the earnings perspective (Δ
  NII, focused on short-term NII impact over 1–2 years) and the economic value perspective
  (Δ EVE, measuring the present value change in the entire banking book) — can produce
  contradictory signals about a bank''s risk position and can incentivize offsetting
  hedging decisions, making it essential to manage both simultaneously rather than
  optimizing for only one metric.

  '
source_refs:
- path: 02_sources/books/alm/A - Asset liability optimization.md
  pages: Ch 1 (Overview of Financial Risks), Ch 2 (Maturity Gap Analysis, EVE section)
  weight: primary
parent_node: '[[ALM_Balance_Sheet_Optimization_Framework]]'
related:
- node: '[[ALM_Hedging_Strategy_Design]]'
  relation: related_to
- node: '[[ALM_Balance_Sheet_Optimization_Framework]]'
  relation: component_of
- node: '[[IRRBB_EVE_NII_Dual_Metric]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## The Dual View Requirement

[LLM] Interest rate risk in the banking book (IRRBB) must be measured from two fundamentally different perspectives because each captures a different dimension of risk that the other cannot reveal. The EBA Final Report on IRRBB (July 2018) — implementing the BCBS Standards (April 2016) — mandates both.

**Earnings perspective (Δ NII):**
- Measures the change in net interest income over a short time horizon (typically 12 months)
- Uses the repricing/maturity gap methodology: NII impact = GAP × Δ interest rate × time fraction
- Captures the immediate P&L sensitivity to rate movements
- Limitation: fails to reveal long-term structural mismatches beyond the gapping period

**Economic value perspective (Δ EVE):**
- Measures the change in present value of all future cash flows from banking book positions
- Computed as: PV(assets) – PV(liabilities) under shocked rates versus base rates
- Captures the full-life risk embedded in fixed-rate and long-duration positions
- Uses six prescribed regulatory shocks: parallel up/down, short up/down, steepener, flattener

## When the Two Views Disagree

[LLM] The critical insight is that the two metrics can give opposite signals. Lubinska illustrates this with an example:

A bank holds long-duration fixed-rate bonds funded by short-term repricing behavioural liabilities (CASA). The treasurer, expecting rates to rise, holds maturing bonds in cash rather than reinvesting:
- **Δ NII impact:** Immediate loss (cash yields nothing while liabilities still repriced); treasurer drives banking book exposure based solely on short-term NII and sees the NII drop as rates do not move as expected
- **Δ EVE impact:** The combination of increased prepayments on mortgages + maturing bonds creates a shorter asset duration, opening a structural liability position on the medium-long curve that represents embedded loss — but this was **not measured** because no EVE limit existed

[LLM] The lesson: a bank managing only Δ NII without Δ EVE limits can accumulate structural mismatches that are invisible to short-term earnings metrics but represent real economic loss. Only when Δ EVE limits are in place does the treasurer receive a signal to reinvest cash and restore duration alignment.

## Mechanics: How Each Metric Is Calculated

### Δ NII (Maturity Gap / Repricing Gap)

[LLM] The repricing gap positions transactions at their next rate-reset date (floating) or contractual maturity (fixed). The NII impact is:

Δ NII = GAP × Δ i

Where:
- GAP = RSA (rate-sensitive assets) – RSL (rate-sensitive liabilities) in each time bucket
- Δ i = interest rate shock (±200 bps parallel shock required by regulators)
- Gapping period: typically 12 months

**Advanced repricing gap** improvements over simple maturity gap:
- Positions transactions at exact risk date (not mid-point of time bucket)
- Separates flows-in-maturity from flows-in-refixing
- Identifies the specific rate index (EURIBOR 3M, SOFR, etc.) to which each position is linked
- Captures basis risk and imperfect indexation

### Δ EVE (Economic Value of Equity)

[LLM] Under the BCBS/EBA standardized approach:

1. All notional repricing cash flows are slotted to time bucket k and netted within each bucket
2. Net cash flows in each bucket are discounted using the risk-free rate at the shocked curve: DF(tk) = exp(–R_shocked(tk) × tk)
3. Sum of discounted net positions = EVE under scenario i
4. Δ EVE = EVE(shocked) – EVE(base) + automatic option add-on (KAO)

[LLM] The EVE calculation includes the impact of automatic interest rate options (caps, floors, prepayment options) via the KAO add-on. This is critical because behavioral options embedded in deposits (zero-floor) create significant asymmetric value that only manifests under the economic value lens.

## Divergence Scenarios

| Rate scenario | Δ NII signal | Δ EVE signal | Interpretation |
|---|---|---|---|
| Long-term fixed assets funded by short-term floating liabilities | Positive if rates fall (assets retain high rate, liabilities reprice lower) | Negative if rates rise (asset PV drops faster than liability PV) | Asset-sensitive short-term, liability-sensitive long-term |
| Rates fall: prepayments surge | NII stabilizes (rate lock-in) | EVE drops (options exercised, cash flows truncated) | Option risk visible only in EVE |
| CASA deposits with zero floor | NII protected (floor prevents negative pass-through) | EVE improves (floor is valuable option) | Floor optionality captured in KAO |

## Hedging Implications

[LLM] Because the two metrics measure different risk horizons, they can create a "hedging dilemma":
- Receiving fixed in an IRS (to hedge reinvestment risk on floating assets) shortens NII sensitivity (reduces Δ NII exposure to falling rates) but simultaneously makes the EVE position more negative if long-term rates rise
- Managing Δ NII in isolation can lead to over-hedging from the EVE perspective, or vice versa

[LLM] Best practice (per EBA 2018 Guidelines) requires banks to set limits on both metrics simultaneously, with the ICAAP capital charge for IRRBB based on the worst-case impact across both perspectives. The hedging strategy must therefore be designed to operate within limits on both dimensions concurrently.
