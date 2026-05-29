---
node_id: asset_encumbrance_management_bank_alm_001
type: concept
title: Asset Encumbrance Management in Bank ALM
aliases:
- Asset encumbrance ratio
- AE ratio
- Tỷ lệ tài sản bị cầm cố
- Quản lý tài sản bị phong tỏa
- Encumbrance ratio
domain:
  primary: alm
  secondary:
  - basel_risk
tags:
- asset_encumbrance
- secured_funding
- lcr
- nsfr
- crr
- eba_reporting
- collateral_management
- contingent_encumbrance
confidence: 1
stability: stable
thesis: '[LLM] Asset encumbrance — the pledging of bank assets as collateral for secured
  funding — is a structural consequence of the post-2008 shift to secured wholesale
  markets, and creates a risk cascade: it subordinates unsecured creditors, reduces
  the pool of assets available for central bank operations, increases procyclical
  margin calls, and constrains future funding flexibility. [LLM] Under EU regulation
  (CRR Article 100, EBA ITS), banks must disclose the asset encumbrance ratio (encumbered
  assets / total assets) quarterly and set internal limits that preserve sufficient
  unencumbered "encumberable" capacity to survive stressed outflows.

  '
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: Ch 17 — Asset Encumbrance (Intesa Sanpaolo)
  weight: primary
parent_node: null
related:
- node: '[[Secured_Funding_Instruments_Repo_Covered_Bond_Abs]]'
  relation: mechanism_of
- node: '[[Funding_Gap_Profile_And_Behavioural_Maturity_Calendar]]'
  relation: related_to
- node: '[[Reserve_Asset_Management_Hqla_Portfolio_Bank]]'
  relation: related_to
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Definition

An asset is **encumbered** if it has been pledged or is subject to any arrangement to secure, collateralise, or credit-enhance any transaction from which it cannot be freely withdrawn. Main transaction types creating encumbrance:

1. **Secured financing transactions (SFTs):** Repos, securities lending — short-term, often daily encumbrance
2. **Collateralised deposits:** Supranational funding requiring collateral backing the loan itself
3. **Central bank facilities:** Assets posted at the central bank as collateral pool; encumbered proportionally on use
4. **Derivative liabilities (variation margin):** Collateral posted against out-of-the-money derivative positions
5. **CCPs:** Cash, bonds, or other assets posted as initial margin and default fund contributions
6. **Covered bonds:** The entire cover pool (including overcollateralisation) backing placed covered bonds
7. **Securitisations:** The underlying asset pool backing placed ABS tranches

## The Asset Encumbrance Ratio (AE Ratio)

Defined by EU Implementing Regulation 2015/79 (based on EBA ITS under CRR Article 100):

**AE Ratio = Encumbered assets (+ collateral received and reused) / Total assets (+ total collateral received)**

The numerator always exceeds the matched liabilities value because of:
- Overcollateralisation requirements (rating agency and regulatory demands)
- Haircuts applied by the counterparty
- Market value differences between the asset and the liability it secures

[LLM] EU weighted average AE ratio at end-2016: 26.6% (up from 25.4% at end-2015 and 25.1% at end-2014). Wide cross-country variation: Denmark (>50% due to large covered bond markets) and Greece (>40% due to heavy central bank funding reliance) at the top; most other EU banking systems below 30%.

Sources of encumbrance at end-2016:
- Repurchase agreements: largest single source (39% in UK, 32% in Italy)
- Covered bonds: 21% of EU total
- OTC derivatives: 10%
- Central bank facilities: 8% (declining from 10% at end-2015)

## Risks from Excessive Encumbrance

**1. Structural subordination of unsecured creditors**
[LLM] When assets are pledged, they are not available to general creditors in insolvency. Unsecured bondholders and uninsured depositors receive a recovery only from unencumbered assets that remain. As the encumbrance ratio rises, unsecured creditors' expected recovery falls, which eventually raises their required yields — potentially eroding the funding cost advantage of secured issuance.

**2. Reduced access to unsecured markets**
[LLM] High encumbrance increases risk perception among unsecured investors, concentrates the remaining unsecured investor base, and may limit the bank's ability to issue senior bonds when needed.

**3. Contingent encumbrance**
[LLM] Existing encumbrance grows during stress because:
- Market volatility reduces collateral values → margin calls require additional pledging
- Rating downgrades trigger contractual obligations (e.g., covered bond account bank replacement clauses require moving collected amounts to a differently rated institution, causing cash outflows)
- The encumbrance is procyclical: available collateral shrinks precisely when funding stress is highest

**4. Central bank policy effectiveness**
[LLM] Very high sectoral encumbrance across the banking system can limit central banks' ability to provide emergency liquidity if there are insufficient unencumbered assets to serve as collateral.

## Regulatory Reporting Framework (EU)

Five-part reporting template under EBA ITS:
- **Part A:** Breakdown of encumbered vs unencumbered assets (by product type); collateral received
- **Part B:** Maturity buckets for encumbered assets matching their liabilities' residual maturities
- **Part C:** Contingent encumbrance — additional assets required under two stress scenarios: (i) 30% fall in fair value of encumbered assets; (ii) 10% depreciation of significant currencies
- **Part D:** Specific covered bond data (nominal, present value, credit ratings, eligible unencumbered assets)
- **Part E:** Additional granular data by asset type and collateral received; central-bank-eligible asset amounts

Pillar III public disclosure required (EBA RTS published March 2017): Templates A–D covering carrying amounts, collateral, associated liabilities, and qualitative narrative.

## Connection to LCR and NSFR

**LCR:** The HQLA buffer (numerator) must be **unencumbered**. Repo-funded HQLA backed by Level 1 assets produce no LCR outflow (100% rollover assumed); repos backed by non-HQLA produce a 100% outflow in the stressed window. [LLM] Managing which assets are pledged and when determines both the HQLA numerator size and the net outflow denominator — making collateral management inseparable from LCR management.

**NSFR:** Required Stable Funding (RSF) factors for encumbered assets are higher than for unencumbered assets and increase with the remaining encumbrance period. Example from the source:
- Mortgage (35% risk weight or lower) encumbered for 9 months: RSF = 65%
- Same mortgage encumbered for 2 years: RSF = 100% (requires stable funding ≥ 1 year in full)
- Same mortgage unencumbered with residual maturity < 1 year: RSF = lower rate

## Internal Limit Setting

[LLM] Supervisors do not mandate a specific AE ratio limit; instead, banks must define internal early warning thresholds and hard limits based on:
- Available "encumberable" assets (those eligible for pledging but not yet pledged)
- Timing to mobilise each category (cash-like collateral is immediate; new securitisation may take months)
- Contingency funding plan requirements (stressed outflows over 1 year + beyond 1 year)
- Peer comparison (the bank's target AE ratio vs sector median)

[LLM] A worked example from the chapter: Bank YY with AE ratio of 24% and €30M in unencumberable assets + €30M encumberable (€8M immediately available including €5M needed for LCR minimum). With stressed outflows requiring €6.9M additional encumbrance within 1 year and €8.4M beyond, the internal early warning threshold is set at 34% AE ratio. The hard limit at 41% reflects the point where remaining flexibility is critically depleted.
