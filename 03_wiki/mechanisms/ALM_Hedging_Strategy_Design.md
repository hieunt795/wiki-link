---
node_id: alm_hedging_strategy_design_001
type: mechanism
title: ALM Macro Hedging Strategy Design
aliases:
- Macro hedging
- ALM hedge portfolio construction
- Banking book hedging
- Interest rate hedge strategy
- thiết kế chiến lược phòng ngừa rủi ro ALM
- phòng ngừa rủi ro lãi suất sổ ngân hàng
domain:
  primary: alm
  secondary:
  - basel_risk
tags:
- hedging
- irrbb
- irs
- derivatives
- macro_hedge
- pv01
- gap_management
confidence: 1
stability: stable
thesis: '[LLM] ALM macro hedging selects and sizes derivative instruments (predominantly
  interest rate swaps, cross-currency swaps, and options) to close or reduce the structural
  interest rate and liquidity mismatches revealed by repricing gap analysis and PV01
  bucket sensitivity, with the hedge portfolio constructed based on risk appetite
  (target immunization vs. directional positioning), the cost of hedging, and the
  dual constraint of managing both Δ NII and Δ EVE within ALCO-approved limits.

  '
source_refs:
- path: 02_sources/books/alm/A - Asset liability optimization.md
  pages: Ch 1 (ALM Role, FTP), Ch 2 (Maturity Gap, Repricing Gap, EVE, PV01)
  weight: primary
parent_node: '[[ALM_Balance_Sheet_Optimization_Framework]]'
related:
- node: '[[Income_Gap_vs_Economic_Value_Gap]]'
  relation: implements
- node: '[[ALM_Balance_Sheet_Optimization_Framework]]'
  relation: component_of
- node: '[[FTP_Methodology]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Hedging Objectives and Strategy Choice

[LLM] The ALM function has two broad hedging strategies available:

**1. Immunization strategy:** Set the Duration Gap (DGAP = DA – w × DL) to zero, or equivalently set GAP = 0 in each time bucket. The balance sheet is neutral to parallel rate shifts. This is the risk-free choice: it protects capital but forfeits the potential profit from correct rate positioning.

**2. Directional GAP strategy:** Deliberately maintain a positive or negative GAP, or DGAP ≠ 0, based on rate expectations:
- GAP > 0 (asset-sensitive position): bank profits if rates rise; loses if rates fall
- GAP < 0 (liability-sensitive position): bank profits if rates fall; loses if rates rise

[LLM] The choice between immunization and directional positioning is made at ALCO level and codified in the Risk Appetite Statement (RAS). In most regulated banks post-GFC, full immunization of large structural mismatches is expected, with directional positioning permitted only within defined limits on Δ NII and Δ EVE.

## Instruments Used

### Interest Rate Swaps (IRS)

[LLM] The dominant instrument for macro hedging. A bank with asset-sensitive balance sheet (more fixed-rate assets than fixed-rate liabilities on the short end):
- Enters **payer swaps** (pays fixed, receives floating): converts the fixed asset's rate sensitivity into floating, closing the GAP
- Example: €100M 5Y fixed-rate mortgage portfolio hedged with a 5Y payer IRS at the 5Y rate

[LLM] The FTP process determines whether the hedge is booked at the portfolio level (macro hedge) or transaction level (micro hedge). Under macro hedge accounting (IAS 39 / IFRS 9), a portfolio of assets or liabilities can be designated as the hedged item, with the derivative recognized in hedge accounting to reduce P&L volatility.

### Forward Rate Agreements (FRA)

[LLM] Used to lock in short-term rates on future repricing. From Lubinska's refixing gap example: a bank with a large negative gap in refixing (€1bn net liability position in October 2010 linked to EURIBOR 6M) buys an FRA to lock the rate on that position, eliminating the exposure to an unexpected rate hike in October.

### Cross-Currency Swaps

[LLM] Used when the bank's assets and liabilities are denominated in different currencies, creating both IRR and FX risk simultaneously. A cross-currency swap converts:
- The currency of the liability (e.g., USD funding) into the currency of the asset (e.g., EUR loan)
- Closes both the IRR mismatch and the FX mismatch in a single instrument

### Interest Rate Options (Caps, Floors, Swaptions)

[LLM] Used to hedge convexity (non-linear rate sensitivity) arising from:
- **Prepayment optionality:** Mortgages embed a short call option (the borrower can refinance). As rates fall, prepayments accelerate, truncating the bank's asset duration. A purchased floor or swaption offsets this by gaining value when rates fall.
- **Zero floors on deposits:** Retail deposits have an implicit floor at 0% (the bank cannot charge negative rates). This creates an automatic option that gains value as rates go negative. The option risk is captured in the KAO (Automatic Options) add-on in EVE calculation.

## Hedge Sizing: PV01 and Time Bucket Sensitivity

[LLM] The core tool for sizing hedges is PV01 (Present Value of a 1 Basis Point Move):

PV01 = PV(base) – PV(shocked by 1bp)

[LLM] Time bucket sensitivity analysis distributes PV01 by maturity bucket, identifying where the bank is most exposed. From Lubinska's example: a bank with PV01 concentrated in 1Y–5Y buckets due to a liability position (receives fixed from assets, pays floating on liabilities) — a rise in 1bp in those tenors produces a gain (net liability position benefits from rate rises). The hedge targets the largest PV01 concentrations.

**Hedge sizing formula:**
Notional of IRS = PV01(banking book position to be hedged) / PV01 per notional of IRS at same tenor

## The Three Treasurer Choices (FTP Decomposition)

[LLM] Lubinska illustrates the interaction of IRR and liquidity hedging with three strategies for a 5Y fixed-rate loan funded by ALM:

| Strategy | Payer swap tenor (m) | Funding bond tenor (n) | Result |
|---|---|---|---|
| a) Close all risks | 5Y | 5Y | Both IRR and liquidity risk closed |
| b) Close IRR only | 5Y | 3Y | IRR closed, liquidity risk open (funding shorter than asset) |
| c) Close liquidity only | 3Y | 5Y | Liquidity risk closed, IRR open (partial hedge only) |

[LLM] Strategy (a) is the fully hedged position and eliminates both margin at risk components. Strategies (b) and (c) retain residual risk in exchange for potential profit from correct positioning on rates or funding spreads.

## Structural Mismatches and the Refixing Gap

[LLM] The refixing gap enriches the repricing gap by showing ALL future repricing dates for floating positions (not just the next one). This is critical for hedging because:
- A €1bn EURIBOR 6M liability has repricing dates every 6 months until maturity
- The repricing gap only shows the next reset date
- The refixing gap shows all subsequent reset dates, revealing the full timeline of rate exposure
- Hedging must therefore use instruments with matching reset profiles (e.g., a series of FRAs, or a swap with the same floating leg frequency)

## FTP as a Balance Sheet Shaping Tool

[LLM] Beyond using external derivatives, ALM can adjust FTP rates to incentivize or discourage specific balance sheet behaviors:
- Raising the FTP rate credited to retail current accounts → increases margin for deposits, encourages collection
- Charging a higher FTP rate on long-term fixed assets → discourages origination if EVE sensitivity is too high
- Dampening the FTP curve at medium-long tenors → reduces cost charged to long-duration assets, encouraging origination when structural liquidity is strong

[LLM] This internal mechanism allows balance sheet management before external hedging is required, reducing hedging costs. External derivatives are then used to close the residual mismatch that internal FTP signals cannot eliminate.
