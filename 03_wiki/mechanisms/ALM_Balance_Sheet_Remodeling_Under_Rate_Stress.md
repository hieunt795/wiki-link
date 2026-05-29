---
node_id: alm_balance_sheet_remodeling_under_rate_stress_001
type: mechanism
title: ALM Balance Sheet Remodeling Under Rate Stress
aliases:
- Banking book P&L under rate stress
- NII attribution under rate shocks
- Balance sheet remodeling
- Rate stress impact on NII and EVE
- tác động của cú sốc lãi suất lên NII và EVE
- tái cơ cấu bảng cân đối dưới áp lực lãi suất
domain:
  primary: alm
  secondary:
  - basel_risk
tags:
- stress_testing
- nii
- eve
- irrbb
- margin_at_risk
- negative_rates
- rate_shock
confidence: 1
stability: stable
thesis: '[LLM] When interest rates move, the banking book P&L is affected through
  three channels simultaneously: (1) the change in NII from repricing of floating
  positions and the rollover of maturing fixed positions (measured by Δ NII); (2)
  the change in economic value of all outstanding fixed-rate positions (measured by
  Δ EVE); and (3) the change in value of embedded automatic options (zero floors,
  prepayment options, caps) captured in the option add-on (KAO) — and the relative
  magnitude of these channels depends critically on the duration gap and behavioral
  assumptions embedded in the balance sheet.

  '
source_refs:
- path: 02_sources/books/alm/A - Asset liability optimization.md
  pages: Introduction (margin locked-in, margin at risk), Ch 1 (negative rates), Ch
    2 (NII, EVE, ICAAP)
  weight: primary
parent_node: '[[ALM_Balance_Sheet_Optimization_Framework]]'
related:
- node: '[[Income_Gap_vs_Economic_Value_Gap]]'
  relation: mechanism_of
- node: '[[ALM_Hedging_Strategy_Design]]'
  relation: related_to
- node: '[[ALM_Balance_Sheet_Optimization_Framework]]'
  relation: component_of
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## The Two P&L Components: Locked-In vs. At-Risk

[LLM] Lubinska introduces a key distinction between two components of the ALM margin on any position:

**Margin locked-in:** The portion of the interest spread that has already been crystallized and attributed to ALM. Once locked in, it is not sensitive to future rate movements (as long as the position is fully hedged or the rates have already reset).

**Margin at risk:** The portion of the expected spread that remains uncertain because the position is open to future rate movements. This has two sub-components:
- **IRR margin at risk:** Arises from rate mismatches (fixed vs. floating repricing dates)
- **Liquidity margin at risk:** Arises from maturity mismatches (asset longer than funding)

[LLM] In Lubinska's core example (fixed-rate loan at 3.50% funded by EURIBOR 3M liability):
- Locked-in ALM margin from IRR = 0.75% (spread over 2% FTP base rate, until liability resets)
- Margin at risk from IRR = 1% (potential loss if EURIBOR 3M drops 25bps)
- Locked-in ALM margin from liquidity = 0.25% (spread between asset and liability liquidity premiums)
- Liquidity margin at risk = dependent on new funding spread when liability rolls over

## Channel 1: NII Sensitivity Under Rate Shocks

[LLM] The NII impact of a rate shock depends on the repricing gap in each time bucket. The standard formula:

Δ NII = GAP × Δ i (for the gapping period, typically 12 months)

[LLM] Key mechanics:
- **Asset-sensitive position (GAP > 0):** Rate rise → NII increase; rate fall → NII decrease
- **Liability-sensitive position (GAP < 0):** Rate rise → NII decrease; rate fall → NII increase
- **Zero-floor effect under negative rates:** Banks cannot charge negative rates on retail deposits. As rates go negative, the liability cost stays floored at 0%, but floating-rate assets (indexed to EURIBOR) continue to reprice below zero. This creates margin compression: NIM shrinks as asset yields go negative while funding costs cannot fall proportionally.

[LLM] The negative rate environment exposed the inadequacy of linear NII models: the zero floor is a short put option position for the bank (it is short optionality on the deposit floor). As rates fall further into negative territory, the intrinsic value of this short option position becomes more negative, accelerating NIM compression.

## Channel 2: EVE Change Under Rate Shocks

[LLM] Under the standardized EVE approach (BCBS/EBA):

Δ EVE(i,c) = [Σ_k CF(k) × DF_shocked(tk)] – EVE_base + KAO(i,c)

Where:
- CF(k) = net notional repricing cash flow in time bucket k (positive for assets, negative for liabilities)
- DF_shocked(tk) = exp(–R_shocked(tk) × tk), the discount factor at the mid-point of bucket k under the shocked rate scenario
- KAO(i,c) = automatic option add-on for scenario i and currency c

[LLM] A bank with a positive DGAP (asset duration > liability duration):
- Rates rise → asset PV drops more than liability PV → Δ EVE < 0 (economic loss)
- Rates fall → asset PV rises more than liability PV → Δ EVE > 0 (economic gain)

[LLM] The magnitude scales with: DGAP × Δ i × Total assets. This is why long-duration banks (holding long-term fixed mortgages or bonds funded by short behavioural liabilities) are particularly exposed to rate rises from an EVE perspective, even if their NII sensitivity appears manageable.

## Channel 3: Automatic Option Effects (KAO)

[LLM] Embedded options create non-linear (convex) relationships between rate changes and balance sheet value:

**Prepayment options on mortgages (short call):** As rates fall, borrowers refinance. The bank loses the high-coupon loan and must reinvest at lower rates. In EVE terms: the KAO for the prepayment option is negative (bank is short this option), partially offsetting the positive Δ EVE from rate falls.

**Zero floor on deposits (short put embedded in liabilities):** As rates fall into negative territory, the floor becomes in-the-money and has positive economic value for depositors (they could invest at negative rates but leave deposits at 0%). For the bank, this is a cost — a short floor position. The KAO add-on captures this.

[LLM] In Lubinska's EVE case study, a bank shows:
- Parallel down scenario: Δ EVE (excluding options) = –42, but KAO (options gain) = +131.5 → net Δ EVE = +89.5. The option gain from zero floors dominates under falling rates.
- Parallel up scenario: Δ EVE (excluding options) = +39.6, but KAO = –6.8 → net Δ EVE = +32.8. Options are out-of-the-money, adding minimal impact.

## Rate Stress Under Negative Rate Environment

[LLM] The negative rate environment (ECB policy rate < 0, as in 2014–2022) creates additional complexity:
- The behavioural liabilities (CASA, savings accounts) cannot reprice below 0% → creates an implicit floor
- Floating-rate assets (EURIBOR-indexed) reprice below zero, compressing NIM
- This is modeled as: the asset side experiences the full rate move, while the liability side is floored at 0% → the gap between them widens as rates fall further
- Banks managing this carry an increasing negative cost of carry on behavioural liabilities: they are funding cheap short-term assets with zero-cost liabilities but the assets yield negative returns

[LLM] The regulatory response (EBA 2018 IRRBB Guidelines) requires banks to explicitly model zero floors in their NII and EVE calculations and to stress-test behavioral optionality.

## ICAAP Capital Charge for IRRBB

[LLM] Per EBA 2018, the IRRBB capital charge in ICAAP must reflect both Δ NII and Δ EVE:
- The Δ EVE-based charge captures the structural/long-term risk (the highest negative EVE impact across all prescribed scenarios)
- The Δ NII-based charge captures the earnings volatility impact (buffer needed for near-term income reduction)
- The total ICAAP charge = max(Δ EVE capital need, Δ NII capital need), or an integrated view combining both

[LLM] This dual-metric approach for ICAAP replaced prior practices where many banks only used VaR or Δ NII for IRRBB capital, potentially under-reserving for structural EVE risk.
