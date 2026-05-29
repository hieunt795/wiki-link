---
node_id: swap_spreads_001
type: mechanism
title: Swap Spreads — Drivers, Balance Sheet Frictions, and Plumbing Indicators
aliases:
- swap spread
- SOFR-ASW
- asset swap spread
- interpolated swap spread
- Treasury swap spread
- chênh lệch lãi suất hoán đổi
- swap spread âm
domain:
  primary: financial_markets
  secondary:
  - monetary_policy
  - shadow_banking
tags:
- swap-spreads
- asset-swap
- SLR
- LCR
- balance-sheet-constraints
- shadow-cost
- plumbing
- SOFR
confidence: 3
stability: stable
thesis: 'Swap spreads — the difference between bond yield and the swap rate of equivalent
  maturity — decompose into: SOFR-ASW = repo-SOFR basis swap + adjusted CDS (credit
  risk). Negative swap spreads (Treasury yield > SOFR swap rate) signal dealer balance
  sheet constraints: when banks face binding SLR/LCR constraints, their ability to
  intermediate arbitrage between bonds and swaps is impaired, causing the spread to
  persist at values inconsistent with no-arbitrage. Shadow costs of regulatory constraints
  — not visible in funding rates — are a primary structural driver of Treasury swap
  spreads in the post-Basel III era. Swap spreads are therefore a measure of plumbing
  friction and dealer balance sheet stress.

  '
source_refs:
- path: 02_sources/books/huggins_schaller_relative_value/Huggins_Schaller_Fixed_Income_RV.md
  pages: Ch.10 overview, Ch.17 (SOFR-ASW), Ch.18 (regulatory constraints, shadow costs)
  weight: primary
- path: 02_sources/books/conks/Conks - Liquidity and Market Dynamics.md
  pages: Swap spreads as plumbing indicator
  weight: supporting
- path: 02_sources/books/tuckman_serrat_fixed_income/Tuckman_Serrat_Fixed_Income_2022.md
  pages: Ch.13 §13.6 (basis swaps), Ch.14 (asset swap spreads)
  weight: supporting
parent_node: '[[Interest_Rate_Swaps_OIS_Fixed_Floating]]'
related:
- node: '[[SLR_LCR_Balance_Sheet_Constraints_Treasury_Market_Dealer]]'
  relation: primary_driver
- node: '[[Repo_Market_Mechanics_Triparty_Bilateral]]'
  relation: transmission_path
- node: '[[Interest_Rate_Swaps_OIS_Fixed_Floating]]'
  relation: component_of
- node: '[[Collateral_Framework_Haircuts_Central_Bank_Credit]]'
  relation: related_mechanism
- node: '[[Basel III Capital And Liquidity Constraint Mechanics]]'
  relation: shared_tag:SLR
- node: '[[SLR LCR Balance Sheet Constraints Treasury Market Dealer]]'
  relation: shared_tag:SLR
- node: '[[Basel III Endgame — Capital, Liquidity, and Credit Migration]]'
  relation: shared_tag:LCR
- node: '[[LCR NSFR Long-Term Lending Penalty]]'
  relation: shared_tag:LCR
- node: '[[Collateral Velocity And Pledged Collateral Market Mechanics]]'
  relation: shared_tag:plumbing
date_created: 2026-05-20
date_updated: 2026-05-20
---


## Core Decomposition: SOFR-ASW Formula

**Asset swap spread (SOFR basis):**
```
SOFR-ASW = repo-SOFR basis swap + adjusted CDS

Where:
  repo-SOFR basis swap = repo rate of the bond minus SOFR
    (reflects bond-specific specialness and secured vs. secured funding)
  adjusted CDS = sovereign/issuer credit risk premium
    (stripped of delivery option, USD-redemption effects for non-USD issuers)
```
[RAW-BOOK Huggins-Schaller Ch.17]

**Transition from LIBOR to SOFR significance:** LIBOR contained an unsecured-secured basis (LIBOR > SOFR by bank credit risk premium). SOFR swap curve closely tracks the bond yield curve (both effectively secured). SOFR-ASW is therefore the superior RV indicator post-LIBOR:
- LIBOR-ASW: structural discrepancy between unsecured LIBOR swap curve and secured bond yield curve → not suitable for cross-bond comparison
- SOFR-ASW: minimal discrepancy → usable as universal bond RV indicator (for USD bonds) and as yardstick for global bonds via CCBS

## What Drives Swap Spreads?

| Driver | Direction | Mechanism |
|--------|-----------|-----------|
| Treasury supply ↑ | Spreads tighter (more negative) | More bonds to absorb → dealers need balance sheet → cost rises |
| Dealer balance sheet constraint ↑ | Spreads tighter (more negative) | Arbitrage harder; risk premium for capacity |
| Credit risk of issuer ↑ | Spreads wider | Higher adjusted CDS component |
| Bond specialness ↑ | Spreads wider (bond yield lower relative to GC) | Repo rate below SOFR → repo-SOFR basis negative |
| Regulatory relaxation (SLR exemption) | Spreads wider (less negative) | Dealers can absorb more bonds; arbitrage restored |
| QT (reserve drain) | Ambiguous | Reserve scarcity → repo rate pressures; simultaneously fewer bonds purchased by Fed |
| Flight to quality | Spreads tighter | UST yields fall faster than swap rates (demand spike) |

**Historical context:** Post-GFC, US Treasury swap spreads turned persistently negative — Treasury yields fell *below* SOFR swap rates. This is a violation of pre-GFC conventions. Key driver: SLR forces dealers to hold capital against all exposure (bonds + swaps), making the bond-swap arbitrage prohibitively costly. [RAW-BOOK Huggins-Schaller Ch.18]

## Shadow Costs of Balance Sheet Constraints

Banks with binding leverage/capital constraints face **shadow costs** that don't appear in marginal funding rates:

```
Unconstrained bank:
  Hurdle rate for new investment = marginal cost of deposits (e.g., 2%)

Constrained bank (CET1 at 4.5% minimum):
  Must either: (a) raise equity to fund investment → blended cost = 2% × 95.5% + 10% × 4.5% = ~2.36%
           or: (b) liquidate existing asset to make room → shadow cost = return on liquidated asset
                    (e.g., 7% if displacing a 7% return project)
```

Shadow cost = opportunity cost of using constrained balance sheet capacity. [RAW-BOOK Huggins-Schaller Box 18.1]

**Key insight for swap spreads:** When regulators tighten leverage requirements:
1. Dealers need more equity per unit of Treasury position
2. Shadow cost of Treasury intermediation rises
3. Dealers require wider compensation to hold Treasury-swap positions
4. Swap spreads widen (less negative) when dealers can absorb more; tighten (more negative) when constrained

## Regulatory Drivers (Post-Basel III)

### Supplementary Leverage Ratio (SLR)
- Applies to: G-SIBs and large US bank holding companies
- Definition: Tier 1 Capital / Exposure Measure; Exposure includes on-balance sheet + derivatives + repo
- G-SIB requirement: ~5.64% SLR (vs. 3% Basel minimum)
- Treasury bonds carry SLR cost even though 0% risk weight; Treasuries are NOT exempted from SLR denominator
- Effect: Holding Treasuries consumes equity capital regardless of risk-weight → arbitrage cost for bond-swap positioning

### Capital Requirements (CET1)
- CET1 ≥ 4.5% of RWAs; Tier 1 ≥ 6%
- Treasuries have 0% RWA → no capital cost on RWA basis
- SLR is the binding constraint for Treasuries specifically (not RWA-based capital)

### Liquidity Coverage Ratio (LCR)
- Banks must hold HQLA (Treasuries count) as buffer
- Incentive to hold Treasuries for LCR compliance → demand for bonds may offset some spread pressure

### Net Stable Funding Ratio (NSFR)
- Requires stable funding (≥1yr tenor) to back illiquid assets
- Short-term repo funding of long-term bonds → NSFR headwind
- Forces dealers to use more expensive term funding or reduce repo-financed bond positions

## Haircuts and Their Effect on Swap Spreads

Haircuts vary by collateral quality and CB:
- US Fed haircuts: T-bills 1%; notes/bonds <10Y 2%; 20-30Y bonds 2.9%
- BOE haircuts: much steeper (5.5% for 10-20Y; 8.5% for 20-30Y gilts)
- ECB: tiered by country (Germany/France <2% for 5Y; Italy 8.5-11.5% for 5Y)

**Effect on cross-currency spreads:** Steeper haircut schedules → higher excess financing cost → yield curves (when swapped into SOFR) appear steeper. BOE haircut schedule steepness contributes to the UK Gilt yield curve (basis-swapped to USD) being steeper than the Treasury curve. [RAW-BOOK Huggins-Schaller Ch.18, Table 18.2]

Excess cost of haircut = (cost of equity or alternative capital) − (repo rate). E.g., if cost of equity = 10%, repo = 5.3%, excess cost = 4.7%. A 5% haircut on 30Y Gilt → excess cost per year = 5% × 4.7% = 23.5bps of yield impact per year of position.

## Swap Spreads as Plumbing Friction Indicator

Swap spreads — particularly the Treasury-SOFR swap spread — serve as a real-time gauge of dealer intermediation capacity and regulatory constraints:

```
Swap spread becoming more negative → signal of:
  1. Increasing Treasury supply (fiscal deficit expansion)
  2. Tighter dealer balance sheets (approaching SLR limit)
  3. Reduced CB Treasury holdings (QT removing balance sheet from system)
  4. Increased political uncertainty (risk premium on sovereign credit)

Swap spread becoming less negative (widening toward zero) → signal of:
  1. Regulatory relief (SLR exemption, Basel III Endgame softening)
  2. Reduced Treasury supply
  3. CB reserve management purchases (RMPs) easing repo stress
  4. Fed balance sheet expansion
```

**SOFR-FF basis** as companion indicator: SOFR > EFFR by more than 6bps typically signals repo market stress (period-end effects, reserve scarcity) rather than structural dealer constraints.

## Asset Swap Spreads as RV Tool

Par asset swap spread (SOFR-ASW) as bond RV indicator:
```
Bond X is "cheap" if SOFR-ASW(X) > fitted-curve-implied SOFR-ASW
Bond Y is "rich" if SOFR-ASW(Y) < fitted-curve-implied SOFR-ASW

With structural adjustments:
  Adjusted SOFR-ASW = Raw SOFR-ASW − specialness − adjusted CDS
```

**Interpolated swap spread** (yield minus par swap rate of same maturity) is a **flawed** RV indicator because it does not control for coupon effect: higher-coupon bonds have lower yields than low-coupon bonds on an upward-sloping curve, even when priced fairly on the same curve. Par asset swap spread corrects for this. [RAW-BOOK Huggins-Schaller §17]

Universal yardstick via CCBS: Any bond globally can be converted to USD SOFR spread via asset swap + cross-currency basis swap. USD SOFR = universal denominator for global bond comparison.

