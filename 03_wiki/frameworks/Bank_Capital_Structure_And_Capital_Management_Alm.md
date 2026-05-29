---
node_id: bank_capital_structure_capital_management_alm_001
type: framework
title: Bank Capital Structure and Capital Management in ALM
aliases:
- Bank capital stack
- CET1 AT1 T2 capital hierarchy
- Capital management ALM
- SREP Pillar 2 capital
- Quản lý vốn ngân hàng
- Cấu trúc vốn Basel III
domain:
  primary: alm
  secondary:
  - basel_risk
tags:
- capital_management
- cet1
- at1
- tier2
- tlac
- mrel
- srep
- rwa
- leverage_ratio
- capital_buffers
confidence: 1
stability: stable
thesis: '[LLM] Bank capital management is the continuous balancing of capital supply
  (the quality stack from CET1 through AT1, Tier 2, and TLAC/MREL liabilities) against
  capital demand (RWA- and leverage-based requirements plus buffers) under evolving
  regulatory standards; capital instruments are simultaneously a source of long-term
  funding for ALM and a critical input to the SREP process that determines the binding
  constraint on distributions. [LLM] The ALM linkage runs in both directions: capital
  bucketing transfers proceeds of capital issuance at floating rates to the business,
  while FVOCI accounting for HQLA bonds creates mark-to-market CET1 volatility when
  rates move.

  '
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: Ch 18 — Capital Management (Deutsche Bank)
  weight: primary
parent_node: null
related:
- node: '[[Bank_Alm_Structural_Liquidity_Management_Nsfr_Lcr_Framework]]'
  relation: related_to
- node: '[[Asset_Encumbrance_Management_Bank_Alm]]'
  relation: related_to
- node: '[[Basel_Iii_Capital_And_Liquidity_Constraint_Mechanics]]'
  relation: implements
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## Capital Hierarchy

### Common Equity Tier 1 (CET1)
The highest quality capital: fully loss-absorbing, most subordinated in liquidation, perpetual, no mandatory distributions. Components: nominal share value + share premium + retained earnings + accumulated OCI + other disclosed reserves + eligible minority interest, **minus** regulatory adjustments.

Key deductions from CET1:
- **Goodwill and intangibles:** Unlikely to be realisable under stress
- **Deferred tax assets (DTA):** Especially DTA on net operating losses (tax claims contingent on future profits); above-threshold DTA on temporary differences also deducted
- **Significant FSE investments (>10% equity stake):** Deducted above a 10%-of-CET1 threshold; below the threshold, risk-weighted at 250%
- **Net pension assets:** Overfunded pension surplus deducted (difficult to recover from the pension fund)
- **Own shares, cashflow hedge reserves, securitisation gains-on-sale, own credit risk gains/losses, AVA (additional valuation adjustments)**

Minimum Pillar 1 CET1 requirement: **4.5% of RWA**

### Additional Tier 1 (AT1)
Hybrid equity/bond: perpetual, coupon cancellable at issuer's sole discretion (non-payment is not a default event), convertible to equity or written down if CET1 falls below a trigger level (typically 5.125% or 7%). Issuer call right exists after 5 years (requires regulatory approval). AT1 absorbs losses on a going-concern basis. Up to **1.5% of RWA** can fill the gap between the 4.5% CET1 minimum and the 6% Tier 1 minimum.

AT1 advantages from an issuer perspective:
- Non-dilutive to existing shareholders
- Coupon may be tax-deductible in some jurisdictions
- FX-denomination flexibility for managing FX-driven capital ratio volatility
- Tool for managing the leverage ratio constraint (same Tier 1 qualifies for both solvency and leverage)

### Tier 2 (T2)
Gone-concern capital — absorbs losses in bankruptcy/resolution. Subordinated to depositors, general creditors, and senior debt holders. Minimum original maturity of 5 years; no call right for issuer in first 5 years. Up to **2.0% of RWA** fills the gap between 6% T1 and 8% total capital requirement.

### TLAC / MREL
[LLM] Total Loss-Absorbing Capacity (TLAC) for G-SIBs (from 2019): the greater of 16% of RWA (rising to 18% from 2022) plus applicable buffers, or 6% of leverage exposure (rising to 6.75%). These bail-in liabilities sit above T2 in seniority but below senior preferred debt. In Europe, TLAC is implemented via MREL (minimum requirement for eligible liabilities) under BRRD.

## Capital Requirements — Pillar 1 Buffers

On top of minimum own funds requirements (4.5% CET1 / 6% T1 / 8% total), three combined buffers apply (all must be covered by CET1):

| Buffer | Rate | Purpose |
|--------|------|---------|
| Capital Conservation Buffer | 2.5% | Going-concern buffer against ordinary losses |
| Countercyclical Buffer (CCyB) | 0%–2.5% (set by national authorities) | Dampen credit cycle overheating |
| G-SIB / D-SIB buffer | 1.0%–3.5% (5th bucket empty at writing) | Systemic importance surcharge |

[LLM] When the combined buffer is breached, the Maximum Distributable Amount (MDA) mechanism restricts distributions (dividends, AT1 coupons, bonuses) based on CRD Article 142. A breach >75% of the combined buffer results in a full distribution ban.

## Pillar 2 Requirements (SREP)

The ECB SREP (Supervisory Review and Evaluation Process) adds:
- **P2R (Pillar 2 Requirement):** Binding; sits between minimum own funds and combined buffers. ECB average P2R in 2016: 2.0% of RWA (all in CET1 in ECB practice)
- **P2G (Pillar 2 Guidance):** Supervisory guidance (non-binding in law, but reputationally significant); sits on top of combined buffers. ECB average P2G in 2016: 2.1% of RWA

## Leverage Ratio

A non-risk-based backstop: Tier 1 capital ≥ 3% of leverage exposure (nominal balance sheet plus off-balance-sheet items measured by standardised rules). Under Basel III, €100M cash at the central bank requires the same leverage-ratio capital as €100M in corporate loans.

[LLM] The leverage ratio creates a binding constraint for low-risk-weight banks (e.g., sovereign bond-heavy or repo-heavy business models). Optimal RWA density = Tier 1 solvency target / Tier 1 leverage target. A bank targeting 12% Tier 1 solvency and 4% T1 leverage should aim for ~33% RWA density.

## ALM Integration

**Capital as long-term funding:** [LLM] CET1 and AT1 instruments (perpetual or 5+ year call) are genuinely long-term funding, appropriate for funding illiquid long-term assets. Capital management typically invests capital proceeds at short-term floating rates with the central cash pool ("capital bucketing"), where the pool manages the resulting interest rate risk mismatch by entering into swaps.

**FVOCI and CET1 volatility:** [LLM] HQLA bonds classified as Fair Value through OCI (FVOCI) create unrealised gains/losses that flow through the OCI component of CET1. Rising interest rates reduce bond values, compressing CET1 even if no loss is realised. This creates a channel by which IRRBB risk affects solvency ratios. ALM hedging programmes using derivatives may introduce hedge accounting mismatches that further compound CET1 volatility.

**FX capital management:** A bank holding CET1 in euros but with USD-denominated RWA faces ratio compression when USD strengthens. Capital management monitors currency composition of RWA vs currency of capital; FX forwards or branch capital injections are used to manage the ratio sensitivity.
