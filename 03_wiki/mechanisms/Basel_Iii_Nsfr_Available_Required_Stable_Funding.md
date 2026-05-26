---
node_id: basel_iii_nsfr_available_required_stable_funding_001
type: mechanism
title: "Basel III NSFR: Available and Required Stable Funding Factor Tables"
aliases:
  - NSFR Basel III
  - Net Stable Funding Ratio
  - ASF factor
  - RSF factor
  - tỷ lệ tài trợ ổn định ròng
  - NSFR ASF RSF
  - structural funding ratio
domain:
  primary: basel_risk
  secondary:
    - financial_markets
tags:
  - nsfr
  - asf
  - rsf
  - stable_funding
  - structural_liquidity
  - 1year_horizon
  - basel3
  - liquidity
confidence: 3
stability: stable
thesis: >
  The NSFR requires ASF / RSF ≥ 100% on a structural 1-year horizon; ASF is
  weighted by liability stability (100% for capital/long-term debt → 95% stable
  retail → 90% less stable retail → 50% short-term wholesale → 0% short-term
  financial institution funding), while RSF reflects asset illiquidity (0% cash/CB
  reserves → 5% Level 1 HQLA → 15% Level 2A → 50% Level 2B/short-term loans →
  65% low-RW mortgages ≥1yr → 85% high-RW performing loans ≥1yr → 100% encumbered
  or illiquid), with the 85% RSF for unrated corporate loans ≥1yr being the
  primary mechanism constraining bank balance sheet capacity for long-term corporate
  credit.
source_refs:
  - path: 02_sources/regulator/bcbs/BaselFramework.md
    pages: "NSF10 (definitions, scope), NSF20 (minimum requirement, reporting), NSF30 (ASF/RSF calculation: 30.5-30.32), NSF99 (summary tables 1-3)"
    weight: primary
related:
  - node: "[[Basel_Iii_Lcr_Hqla_Cashflow_Mechanics]]"
    relation: complementary_liquidity_standard
  - node: "[[Basel_Iii_Capital_And_Liquidity_Constraint_Mechanics]]"
    relation: part_of_four_constraints
  - node: "[[Basel_Driven_Credit_Migration_To_Private_Markets]]"
    relation: structural_driver
  - node: "[[Bank_Alm_Structural_Liquidity_Management_Nsfr_Lcr_Framework]]"
    relation: alm_implementation_context
  - node: "[[Funds_Transfer_Pricing_Rate_Decomposition_Base_Liquidity_Credit_Optionality_Components]]"
    relation: ftp_liquidity_cost_source
date_created: "2026-05-26"
date_updated: "2026-05-26"
---

## Overview

The NSFR promotes **structural funding stability** on a 1-year horizon — the counterpart to the LCR's 30-day stress horizon. While the LCR ensures short-term survival, the NSFR ensures that long-duration assets are funded with stable long-duration liabilities, preventing over-reliance on short-term wholesale funding.

**Formula:** `NSFR = Available Stable Funding (ASF) / Required Stable Funding (RSF) ≥ 100%`

**Reporting:** Quarterly minimum; not less than monthly for large internationally active banks.

The NSFR calibration rests on two principles (NSF30.2):
1. **Funding tenor:** Longer-term liabilities are assumed more stable than short-term.
2. **Funding type and counterparty:** Retail/small-business deposits are behaviourally more stable than same-maturity wholesale funding.

## Available Stable Funding (ASF) Factors (NSF30.10-14, NSF99 Table 1)

ASF reflects how reliably a liability will remain over the next year. Banks multiply each liability's carrying value by its ASF factor to compute total ASF.

| ASF Factor | Liability / Capital Category |
|---|---|
| **100%** | Regulatory capital (CET1, AT1, Tier 2 ≥1yr maturity) |
| **100%** | Other capital instruments and liabilities with effective residual maturity ≥1yr |
| **100%** | Retail term deposits ≥1yr that cannot be withdrawn early without significant penalty |
| **95%** | **Stable** retail and small-business demand deposits and term deposits <1yr |
| **90%** | **Less stable** retail and small-business demand deposits and term deposits <1yr |
| **50%** | Non-financial corporate funding (secured and unsecured) <1yr |
| **50%** | Operational deposits (clearing, custody, cash management — per LCR40.26-36) |
| **50%** | Sovereign, PSE, MDB funding <1yr |
| **50%** | Other funding (including CB and financial institution) with maturity 6m–<1yr |
| **0%** | All other liabilities and equity not in above categories |
| **0%** | Short-term CB and financial institution funding <6m maturity |
| **0%** | Liabilities without stated maturity (except deferred tax and minority interest) |
| **0%** | Net NSFR derivative liabilities (if derivative liabilities > derivative assets) |
| **0%** | Trade date payables from purchases of financial instruments |

**Critical practical point:** Banks predominantly funded by short-term interbank/financial institution deposits (<6m) receive **0% ASF** on those liabilities — they contribute nothing to available stable funding. This forces structural reform toward retail deposits or long-term debt issuance as the funding base.

## Required Stable Funding (RSF) Factors (NSF30.25-32, NSF99 Table 2)

RSF reflects how much stable funding must support each asset based on its liquidity characteristics and tenor. Banks multiply each asset's carrying value by its RSF factor to compute total RSF.

| RSF Factor | Asset Category |
|---|---|
| **0%** | Coins and banknotes; all central bank reserves; CB claims <6m; trade date receivables |
| **5%** | Unencumbered Level 1 HQLA (excl. cash and CB reserves) — sovereign bonds at 0% RW |
| **10%** | Unencumbered loans to financial institutions <6m secured by Level 1, with rehypothecation right |
| **15%** | All other unencumbered loans to financial institutions <6m |
| **15%** | Unencumbered Level 2A assets (sovereign/PSE at 20% RW; corporate debt/covered bonds ≥AA-) |
| **50%** | Unencumbered Level 2B assets (RMBS ≥AA, corporate debt BBB- to A+, major-index equities) |
| **50%** | HQLA encumbered for 6m–<1yr |
| **50%** | Loans to financial institutions and central banks, residual maturity 6m–<1yr |
| **50%** | Deposits at other financial institutions for operational purposes |
| **50%** | All other non-HQLA assets with residual maturity <1yr (loans to non-FI corporates, retail, sovereigns) |
| **65%** | Unencumbered residential mortgages ≥1yr with ≤35% risk weight under standardised approach |
| **65%** | Other unencumbered loans ≥1yr to sovereigns, MDBs, PSEs with ≤35% RW (non-FI) |
| **85%** | Initial margin posted for derivative contracts; CCP default fund contributions |
| **85%** | **Other unencumbered performing loans ≥1yr with >35% RW** (excl. loans to FIs) |
| **85%** | Non-HQLA securities ≥1yr maturity; exchange-traded equities |
| **85%** | Physical traded commodities including gold |
| **100%** | All assets encumbered ≥1yr |
| **100%** | Net NSFR derivative assets (if derivative assets > derivative liabilities) |
| **100%** | Assets without stated maturity (including open-maturity reverse repos) |
| **100%** | Non-performing loans; loans to FIs ≥1yr; non-exchange-traded equities; fixed assets |

**Encumbrance treatment:** Assets encumbered ≥1yr receive 100% RSF regardless of underlying asset type. Assets encumbered 6m–<1yr receive at least 50% RSF. (NSF30.20)

## Off-Balance Sheet RSF (NSF30.33-34, NSF99 Table 3)

| RSF Factor | Exposure Type |
|---|---|
| **5%** of undrawn | Irrevocable and conditionally revocable credit and liquidity facilities to any client |
| National discretion | Unconditionally revocable facilities; trade finance; guarantees; non-contractual obligations |

## Why the NSFR Penalizes Long-Duration Corporate Lending

The **85% RSF** for unrated/high-RW performing loans ≥1yr is the central mechanism. For an unrated corporate loan with >35% standardised risk weight:

```
Loan = 100 notional
RSF required = 100 × 85% = 85 of stable funding

If funded by:
  Retail stable deposits → 95% ASF (need 85/0.95 = 89.5 of deposits to support 85 RSF)
  Short-term wholesale (<6m) → 0% ASF (no credit) → must replace with stable sources
```

Combined with the LCR outflow treatment for revolving credit lines and the RWA capital charge, each layer of Basel III makes holding long-duration unrated corporate credit structurally punitive. [LLM] This is the structural driver documented in `[[Basel_Driven_Credit_Migration_To_Private_Markets]]`.

## LCR vs NSFR: Complementary Horizons

| Dimension | LCR | NSFR |
|---|---|---|
| Time horizon | 30-day stress | 1-year structural |
| Focus | Short-term survival buffer | Structural funding match |
| Key metric | HQLA ≥ net cash outflows | Stable funding ≥ stable funding needed |
| Reporting | Monthly (weekly/daily in stress) | Quarterly |
| Critical rate | Retail deposit run-off rate (3–10%) | RSF 85% for long corporate loans |

## FTP Linkage

The NSFR's RSF factors feed directly into FTP liquidity charges: a 85%-RSF asset requires expensive stable funding (long-term deposits or bonds); the liquidity cost component of FTP = tenor premium to source this stable funding. [LLM] See `[[Funds_Transfer_Pricing_Rate_Decomposition_Base_Liquidity_Credit_Optionality_Components]]` for the FTP decomposition mechanism.

## Related Concepts

`[[Basel_Iii_Lcr_Hqla_Cashflow_Mechanics]]` covers the 30-day LCR complement. `[[Basel_Iii_Capital_And_Liquidity_Constraint_Mechanics]]` places NSFR as the fifth constraint axis in the integrated Basel framework. `[[Bank_Alm_Structural_Liquidity_Management_Nsfr_Lcr_Framework]]` describes how ALM units manage both ratios together.
