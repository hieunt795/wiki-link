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
  primary: basel_risk
  secondary:
  - financial_markets
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

---

## eSLR Reform: The "Faulty Relief Valve" (Q1 2026)

### What Changed

The **eSLR (enhanced SLR)** is an extra buffer on top of the standard 3% SLR requirement, applied only to G-SIBs (globally systemically important banks).

| Version | eSLR Buffer |
|---------|------------|
| Pre-reform | Fixed buffer (typically 2-3%) |
| Post-reform (Q1 2026 adoption) | Half of the bank's G-SIB surcharge |

**Effect:** Higher-bucket G-SIBs (larger G-SIB surcharges) get proportionally less eSLR buffer reduction. Lower-bucket G-SIBs get more. Overall, G-SIBs' total leverage capital requirements decline. [RAW-CLIP Conks Faulty Relief Valve]

### The Capital Max Mechanic (Why SLR Easing ≠ More UST Buying)

**Critical insight:** Banks hold capital equal to the **maximum** of risk-weighted requirements (RWA) and leverage-based requirements (SLR), NOT the sum of both.

```
Example:
  RWA requirement: $100
  SLR requirement: $60 (pre-reform)
  → Bank must hold: max($100, $60) = $100

After eSLR ease:
  RWA requirement: $100
  SLR requirement: $50 (post-reform)
  → Bank must hold: max($100, $50) = $100  ← UNCHANGED
```

**Consequence:** If RWA is the binding constraint (true for most Big Six dealers in normal conditions), a lower SLR requirement makes no difference to actual capital held. Banks cannot expand UST absorption simply because leverage capital is relieved — they're still bound by risk-based capital. [RAW-CLIP Conks Faulty Relief Valve]

### When SLR Does Matter (Crisis-Only Relevance)

The SLR becomes binding only when leverage capital > RWA capital — which typically occurs during stress events when:
- Dealers expand balance sheet to absorb distressed UST supply
- Rapid balance sheet growth pushes SLR capital requirement above RWA

**The eSLR reform's actual purpose:** Reduce the probability that leverage capital becomes the binding constraint in crisis — not to routinely free up capacity.

### Why Banks Won't Use the "Excess Capacity"

Even post-reform, banks have theoretical "excess leverage capacity" (difference between max(RWA, SLR) and SLR alone). But excess leverage capacity doesn't translate to UST buying because:

1. **Reserve hoarding competes with UST hoarding**: Banks fund UST purchases with reserves (both are 0% risk-weighted). Regulatory liquidity requirements push banks to hold more reserves anyway.
2. **Duration risk**: USTs carry interest rate risk; dealer treasurers manage duration carefully regardless of leverage relief.
3. **Profitability optimization**: ROE incentives push toward higher-yielding risk-weighted assets, not more 0% RW USTs.

**Conks conclusion:** "A large bid from the largest banking giants is thus not assured." Non-SLR catalysts (growing deposit base, lighter Basel III endgame, Treasury buybacks) will drive more UST demand than eSLR reform. [RAW-CLIP Conks Faulty Relief Valve]

### Swap Spreads as the True Plumbing Gauge

Conks uses the **swap spread curve** (not the SLR reform announcement) as the primary signal for plumbing friction improvement:

```
Swap spread (swap rate − UST yield):
  More negative = more plumbing frictions (Basel constraints, deficit pressure, Fed QT)
  Less negative = easing frictions (RWA relief, buybacks, QT end, TGCR targeting)
```

By late 2025 / early 2026: swap spreads widened (rallied) sharply — driven by optimism around eSLR + non-eSLR catalysts. Conks warns: widening should slow until regulators implement stronger relief (e.g., excluding USTs from risk-based capital ratios entirely). [RAW-CLIP Conks Faulty Relief Valve]

