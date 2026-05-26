---
node_id: basel_iii_lcr_hqla_cashflow_mechanics_001
type: mechanism
title: "Basel III LCR: HQLA Stock and 30-Day Net Cash Outflow Mechanics"
aliases:
  - LCR Basel III
  - Liquidity Coverage Ratio
  - HQLA classification
  - tỷ lệ bao phủ thanh khoản
  - LCR HQLA
  - run-off rates LCR
domain:
  primary: basel_risk
  secondary:
    - financial_markets
tags:
  - lcr
  - hqla
  - liquidity
  - run_off_rates
  - stress_scenario
  - level1_level2
  - 30day_horizon
  - basel3
confidence: 3
stability: stable
thesis: >
  The LCR requires banks to hold a stock of unencumbered HQLA ≥ 100% of total
  net cash outflows over a 30-day combined idiosyncratic and market-wide stress
  scenario; HQLA is tiered into Level 1 (no limit, no haircut), Level 2A (≤40%
  of stock; 15% haircut), and Level 2B (≤15% of stock; 25–50% haircuts), while
  the outflow denominator applies product-specific run-off rates (retail stable
  3–5%, less stable ≥10%; wholesale operational 25%; non-financial corporate 40%;
  financial institution 100%) capped such that net inflows cannot reduce required
  outflows by more than 75%.
source_refs:
  - path: 02_sources/regulator/bcbs/BaselFramework.md
    pages: "LCR20 (stress scenario, 100% minimum, reporting), LCR30 (HQLA definition and levels), LCR40 (cash outflows and inflows)"
    weight: primary
related:
  - node: "[[Basel_Iii_Nsfr_Available_Required_Stable_Funding]]"
    relation: complementary_liquidity_standard
  - node: "[[Basel_Iii_Capital_And_Liquidity_Constraint_Mechanics]]"
    relation: part_of_four_constraints
  - node: "[[Basel_Iii_Leverage_Ratio_Non_Rwa_Capital_Constraint]]"
    relation: balance_sheet_constraint_peer
  - node: "[[Slr_Lcr_Balance_Sheet_Constraints_Treasury_Market_Dealer]]"
    relation: us_dealer_transmission
  - node: "[[Bank_Alm_Structural_Liquidity_Management_Nsfr_Lcr_Framework]]"
    relation: alm_implementation_context
date_created: "2026-05-26"
date_updated: "2026-05-26"
---

## Overview

The LCR promotes short-term liquidity resilience: a bank must be able to survive 30 calendar days of a combined **idiosyncratic and market-wide stress** using only its stock of HQLA.

**Formula:** `LCR = HQLA Stock / Total Net Cash Outflows (30-day) ≥ 100%`

**Net cash outflows** = total expected outflows − total expected inflows, with inflows capped at **75% of total outflows** (minimum net outflow = 25% of gross outflows even if inflows exceed outflows). (LCR40.1)

In periods of actual stress, banks may draw down their HQLA below 100% — the LCR is a survival horizon, not a rigid floor that triggers immediate insolvency. Supervisors subsequently assess and guide usability. (LCR20.5)

## The Stress Scenario (LCR20.2)

The 30-day scenario combines seven simultaneous shocks:
1. Run-off of a proportion of retail deposits
2. Partial loss of unsecured wholesale funding
3. Partial loss of secured short-term financing (repo, securities lending)
4. Additional contractual outflows from a **3-notch credit rating downgrade** (collateral posting, derivatives)
5. Market volatility increasing collateral requirements on derivatives
6. Unscheduled draws on committed credit and liquidity facilities granted to clients
7. Potential buy-back of bank's own debt or honoring non-contractual obligations for reputational reasons

## HQLA Definition and Tiers (LCR30)

Assets qualify as HQLA if they can be quickly converted to cash at little or no loss even in stress. Key characteristics: low risk, ease of valuation, low correlation with risky assets, active and sizable market, low volatility, flight-to-quality properties. (LCR30.2-12)

**Operational requirements for HQLA:** Assets must be unencumbered, under control of the liquidity function (treasurer), operationally monetisable within standard settlement periods, and periodically monetised to test access. (LCR30.13-28)

### Level 1 — No cap, no haircut (LCR30.40-41)

| Asset | Condition |
|---|---|
| Coins and banknotes | — |
| Central bank reserves | Drawable in stress per CB policy |
| Sovereign/CB/PSE/MDB securities | 0% risk weight; large/deep/active market; no bank-issued obligation |
| Domestic sovereign/CB debt (non-0% RW) | In domestic or specific foreign currency up to stressed NCO |

Level 1 is the core of the buffer — includes government bonds and central bank reserves. No haircut is applied for LCR purposes, though supervisors may add haircuts for interest rate sensitivity.

### Level 2A — Max 40% of stock; 15% haircut (LCR30.42-43)

| Asset | Condition |
|---|---|
| Sovereign/CB/PSE/MDB securities | 20% risk weight; active market; price decline ≤10% in stress |
| Corporate debt / covered bonds | Rated ≥AA-; not bank-issued; price decline ≤10% in stress |

### Level 2B — Max 15% of stock (within 40% Level 2 cap); national discretion (LCR30.44-46)

| Asset | Haircut | Key Criteria |
|---|---|---|
| RMBS | 25% | Rated ≥AA; underlying residential mortgages only; LTV ≤80% at issuance |
| Corporate debt (incl. CP) | 50% | Rated ≥BBB-; not bank-issued; price decline ≤20% in stress |
| Common equity shares | 50% | Constituent of major national index; price decline ≤40% in stress |

## Cash Outflow Run-off Rates (LCR40)

### Retail deposits

| Category | Run-off rate | Condition |
|---|---|---|
| Stable deposits | 5% (floor) | Fully insured + established relationship or transactional account |
| Stable deposits (strict DI) | 3% | Meets additional pre-funded DI criteria (LCR40.11) |
| Less stable deposits | ≥10% | Uninsured or high-value or internet/FX deposits |
| Term deposits (>30d notice + penalty) | 0% | No legal right to withdraw within 30 days AND material early withdrawal penalty |

### Wholesale funding

| Counterparty | Run-off rate | Notes |
|---|---|---|
| Small business customers | Same as retail | Aggregated funding < €1M; managed as retail exposure |
| Operational deposits (clearing/custody/cash mgmt) | 25% | Substantive dependency, supervisory approval required |
| Non-financial corporates, sovereigns, CBs, PSEs | 40% | Non-operational; 20% if fully insured |
| Banks, securities firms, insurance, funds, SPVs | **100%** | All other legal entities |

### Secured funding (repo) — run-off based on collateral type (LCR40.46-47)

| Collateral | Run-off rate |
|---|---|
| Level 1 HQLA or domestic central bank | 0% |
| Level 2A HQLA | 15% (≈ haircut amount) |
| Domestic sovereign/MDB/PSE (other collateral) | 25% |
| Non-HQLA, non-sovereign | 100% |

### Off-balance sheet commitments

- Committed credit lines to non-financials: 10% draw-down rate
- Committed liquidity lines to non-financials: 30% draw-down rate
- Committed credit and liquidity lines to financial institutions: 40% draw-down rate

## Why the LCR Constrains Bank Business Models

The LCR creates direct costs for specific activities:

**Committed credit lines to corporate/private credit funds** — assumed 10–30% draw-down in stress → bank must hold low-yielding HQLA against contingent liability. [LLM]

**Wholesale funding reliance** — a bank funded predominantly by financial institutions (100% run-off) requires a much larger HQLA buffer than one funded by stable retail deposits (5%). This creates a structural preference for retail deposit-funded balance sheets. [LLM]

**Repo funding with non-HQLA collateral** — 100% outflow rate forces banks to treat non-HQLA secured funding as completely unavailable in stress. This penalises repo-funded dealer inventories in illiquid securities. [LLM]

## Reporting and Usability (LCR20.5-8)

- **Minimum reporting frequency:** Monthly; can be increased to weekly or daily in stressed situations
- **Usability:** Banks may fall below 100% in genuine stress — the HQLA is designed to be used. Supervisors guide restoration, avoiding procyclical responses.
- **Interaction with other standards:** LCR and NSFR are complementary — LCR covers 30-day stress horizon; NSFR covers structural 1-year funding horizon. See `[[Basel_Iii_Nsfr_Available_Required_Stable_Funding]]`.

## Related Concepts

`[[Basel_Iii_Capital_And_Liquidity_Constraint_Mechanics]]` places LCR as the fourth constraint axis alongside RWA capital, output floor, and leverage ratio. `[[Bank_Alm_Structural_Liquidity_Management_Nsfr_Lcr_Framework]]` describes how ALM teams implement LCR alongside NSFR in practice. `[[Slr_Lcr_Balance_Sheet_Constraints_Treasury_Market_Dealer]]` shows how LCR + SLR jointly constrained US Treasury dealer capacity.
