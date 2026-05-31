---
node_id: hqla_classification_level1_level2a_level2b_001
type: concept
title: Hqla Classification Level1 Level2a Level2b
aliases:
- HQLA
- high quality liquid assets
- Level 1 assets
- Level 2 assets
- tài sản thanh khoản chất lượng cao
- tài sản HQLA
domain:
  primary: alm
tags:
- hqla
- lcr
- liquidity_buffer
- alm
- bcbs
- haircut
confidence: 3
stability: stable
thesis: 'bcbs238 §46-54: HQLA has two tiers. Level 1 (§49-50): no haircut in LCR
  standard (supervisors may add duration/credit/liquidity haircuts); no cap; includes
  central bank reserves, 0%-RW sovereign/CB debt, qualifying foreign-currency sovereign
  debt up to stressed NCF in that currency. Level 2A (§51-52): 15% haircut; ≤40% of
  total HQLA after haircuts; must meet all criteria: 20% RW under Basel II SA (OR
  rated AA-), active deep repo/cash markets, proven liquidity record (max 10% price
  decline in relevant 30-day stress period), not issued by a financial institution.
  Level 2B (§47, §53-54): supervisor discretion — may or may not be permitted; ≤15%
  of total HQLA (within the 40% Level 2 cap); RMBS 25% haircut (rated AA+, active
  markets, not self-originated); other L2B assets (qualifying corporate bonds, equities)
  50% haircut. Correction vs LLM stub: Level 2A does NOT include RMBS — that is L2B
  only. L2A is sovereign/PSE/MDB securities and qualifying corporate bonds/covered bonds.'
source_refs:
- path: 02_sources/regulator/bcbs/bcbs238 - Basel III The Liquidity Coverage Ratio and liquidity risk monitoring tools.md
  pages: '§46-54 (HQLA classification); §28 (operational requirements); §190-191 (30-day monetisation)'
  weight: primary
parent_node: null
related:
- lcr_secured_funding_run_off_by_collateral_quality_asset_level_001
- bcbs_hqla_liquidity_cushion_principle_12_001
- basel_iii_lcr_hqla_cashflow_mechanics_001
date_created: '2026-05-27'
date_updated: '2026-05-29'
---

## HQLA Classification (bcbs238 §46-54)

### Level 1 — No haircut, no cap (§49-50)

- Central bank reserves (excess reserves + required reserves if freely withdrawable in stress)
- Marketable securities representing claims on sovereigns, CBs, PSEs, MDBs: **0% risk weight** under Basel II SA
- Domestic sovereign/CB debt with **non-0% RW**: eligible only up to the bank's stressed NCF in that foreign currency (FX liquidity need cap)
- **Haircut in LCR: 0%** (supervisors may optionally add haircuts for duration, credit, or liquidity risk)
- **Cap: none** — can comprise 100% of HQLA stock

### Level 2A — 15% haircut, ≤40% cap (§51-52)

All assets must meet **all** of the following:
- **Risk weight:** 20% under Basel II SA (sovereign, PSE, MDB) **OR** rated AA- or better (corporate, covered bond)
- **Markets:** traded in large, deep, active repo OR cash markets with low concentration
- **Proven liquidity record:** maximum decline of price or increase in haircut ≤10% in a relevant 30-day stress period
- **Not issued by a financial institution** or affiliated entity

Asset types: sovereign/PSE/MDB securities (20% RW); corporate debt securities (incl. CP); covered bonds

Cap: Level 2 assets (2A + 2B) ≤ **40%** of total HQLA stock after haircuts

### Level 2B — 25-50% haircut, ≤15% cap (§47, §53-54)

**Supervisor discretionary** — jurisdictions may or may not permit inclusion.

| L2B Asset | Haircut | Key criteria |
|---|---|---|
| RMBS | **25%** | Rated AA or higher (ECAI); active large markets; not originated by bank or affiliates |
| Other L2B (corporate bonds BBB- to A+, equities) | **50%** | Additional criteria: not issued by FI; included in major equity index; exchange-listed |

Cap: ≤**15%** of total HQLA (included within the 40% Level 2 cap)

---

## Key Corrections vs. Common LLM Errors

| Error | Correct |
|---|---|
| "Level 2A includes RMBS" | RMBS is Level **2B** (25% haircut), not 2A |
| "Level 2B is always available" | Level 2B is **supervisor-discretionary** (§47) |
| "Level 1 has no haircut anywhere" | LCR standard = 0%, but supervisors may add haircuts for duration/credit/liquidity risk (§49) |
| "40% cap applies to Level 2B" | The 40% cap applies to all Level 2 (2A+2B); Level 2B has an additional **15% sub-cap** |

---

## Operational Requirements (§28-43)

Assets must be:
- **Unencumbered** (free of liens; not pledged as collateral)
- **Accessible** — held by the liquidity management function, free from intragroup transfer restrictions
- **Periodically monetised** — banks must regularly repo or sell representative samples to test market access (§30)
- Hedges on HQLA permitted but must account for the cash outflow if hedge is closed early (§34)

