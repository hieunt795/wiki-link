---
node_id: slr_lcr_balance_sheet_constraints_treasury_market_dealer_001
type: mechanism
title: SLR LCR Balance Sheet Constraints Treasury Market Dealer
aliases:
- SLR
- Supplementary Leverage Ratio
- LCR
- Liquidity Coverage Ratio
- dealer balance sheet
- he so don bay bo sung
- ti le dam bao thanh khoan
domain:
  primary: financial_markets
tags:
- slr
- lcr
- basel-iii
- dealer
- treasury-market
- hqla
- balance-sheet-constraints
confidence: 3
stability: evolving
thesis: Post-GFC Basel III regulations — especially the Supplementary Leverage Ratio
  (SLR) and Liquidity Coverage Ratio (LCR) — constrain primary dealer balance sheets,
  reducing their capacity to absorb Treasury supply during periods of elevated issuance
  or volatility. The resulting illiquidity spiral (volatility -> wider spreads ->
  forced selling -> more volatility) creates systemic risk in the world's largest
  bond market.
source_refs:
- path: 02_sources/books/conks/Conks - Liquidity and Market Dynamics.md
  pages: Great Sovereign Debt Intervention, Repo Market Blindspot
  weight: primary
related:
- node: '[[Basel III Capital And Liquidity Constraint Mechanics]]'
  relation: shared_tag:slr
- node: '[[Swap Spreads — Drivers, Balance Sheet Frictions, and Plumbing Indicators]]'
  relation: shared_tag:slr
- node: '[[Basel III Endgame — Capital, Liquidity, and Credit Migration]]'
  relation: shared_tag:lcr
- node: '[[LCR NSFR Long-Term Lending Penalty]]'
  relation: shared_tag:lcr
- node: '[[Basel Regional Implementation Dynamics]]'
  relation: shared_tag:basel-iii
date_created: '2026-05-20'
date_updated: '2026-05-20'
---


Basel III post-GFC regulations constrain bank balance sheets in ways that affect Treasury market function.

**Key regulations affecting dealer capacity:**

1. **SLR (Supplementary Leverage Ratio):** Banks must hold 3-5% capital against ALL assets, including risk-free reserves and Treasuries. No risk-weighting. Creates incentive to shed low-yield HQLA (Treasuries, reserves) to maximize ROE. March 2021: SLR relief expired -> banks dumped Treasuries -> yield spike.

2. **LCR (Liquidity Coverage Ratio):** Banks must hold 30 days of HQLA (reserves + Treasuries + agency MBS) to cover stressed outflows. Forces HQLA hoarding regardless of opportunity cost. Large LCR portfolios mean banks cannot flexibly deploy balance sheet to absorb Treasury supply.

3. **G-SIB surcharge:** Additional CET1 buffer for systemic banks (0.5-3.5%). Reduces risk appetite. G-SIBs are the primary Treasury market makers; constrained balance sheets = wider bid-ask spreads during stress.

**Cascade during Treasury market stress:**
Treasury supply surge + dealer balance sheet constraints -> dealers cannot absorb supply -> bid-ask widens -> price-insensitive sellers hit market -> illiquidity spiral (Conks model: volatility creates illiquidity, illiquidity creates more volatility).

**Policy response toolkit:**
1. Treasury buybacks (reduce net supply, improve duration distribution)
2. SLR exemption (temporary relief to allow dealer balance sheet expansion)
3. Fed Standing Repo Facility (SRF): dealers can repo Treasuries with Fed at penalty rate to fund positions
4. FICC cleared repo expansion: netting reduces balance sheet consumption

**SLR exemption precedent:** April 2020 Covid SLR relief enabled dealers to absorb trillions in new issuance. Expiration March 2021 directly contributed to March-April 2021 Treasury market stress.


