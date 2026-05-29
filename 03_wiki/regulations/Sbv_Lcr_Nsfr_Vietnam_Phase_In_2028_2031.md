---
node_id: sbv_lcr_nsfr_vietnam_phase_in_2028_2031_001
type: regulation
jurisdiction: vietnam
issuer: sbv
title: SBV LCR NSFR Vietnam Phase-In 2028–2031
aliases:
- LCR Vietnam phase-in
- tỷ lệ khả năng chi trả Vietnam
- tỷ lệ NSFR Vietnam
- tỷ lệ nguồn vốn ổn định ròng
- SBV LCR schedule
- SBV liquidity ratios 2028
domain:
  primary: alm
  secondary:
  - basel_risk
tags:
- lcr
- nsfr
- hqla
- liquidity-risk
- sbv
- vietnam-banking
- phase-in
- basel-iii
confidence: 1
stability: evolving
thesis: '[LLM] Under the SBV''s 2026 draft prudential circular, Vietnamese banks must
  phase in Basel III LCR from 2028 (70%) through 2031+ (100%), calculated in two dimensions
  — VND-equivalent LCR and standalone VND LCR. NSFR = 100% applies from 2028 (or earlier
  upon voluntary early adoption with SBV approval). Banks may opt into the LCR/NSFR
  regime before 2028 mandatory date by notifying SBV and providing independent auditor
  confirmation of compliance at the last fiscal year-end.

  '
source_refs:
- path: 02_sources/regulator/sbv/10_DTTT_thay_the_Thong_tu_22_260421_37a8.md
  pages: Điều 14 (application), Điều 17 (LCR formula and schedule), Điều 15 (liquidity
    risk mgmt)
  weight: primary
- path: 02_sources/regulator/bcbs/bcbs238.md
  pages: ''
  weight: supporting
parent_node: '[[Sbv_Draft_2026_Prudential_Safety_Ratios_Banks]]'
related:
- node: '[[Sbv_Draft_2026_Prudential_Safety_Ratios_Banks]]'
  relation: component_of
- node: '[[Basel_Iii_Lcr_Liquidity_Coverage_Ratio_Standard_2013]]'
  relation: implements
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

[LLM] Auto-generated stub from draft circular replacing TT22/2019, Articles 14–17. Verify numbers against final enacted text.

## LCR Phase-In Schedule (Điều 17(1)(c))

| Effective from | Minimum LCR (solo) |
|---|---|
| 2028 | 70% |
| 2029 | 80% |
| 2030 | 90% |
| 2031+ | 100% |

*Applies to: LCR-VND-equivalent (quy VNĐ) and standalone VND LCR.*

Banks must report LCR ratios daily before 15:00 to SBV.

## LCR Formula

LCR = HQLA (eligible high-quality liquid assets) / Net Cash Outflows (next 30 days) ≥ threshold

Three calculations required:
1. LCR quy VNĐ (all currencies converted to VND)
2. LCR VNĐ (VND only)
3. LCR for material foreign currencies (managed under internal policy)

## NSFR (Điều 14)

Mandatory from 01 Jan 2028; minimum threshold = 100%.
Early adoption: banks notify SBV in writing and must have auditor confirmation of full compliance at last fiscal year-end with no qualified opinion.

Prior to 2028: TT22/2019 LCR and short-term capital usage ratios remain in effect.

## Liquidity Risk Management Framework (Điều 15)

Banks must manage:
- Intraday liquidity (cash flow monitoring, collateral management)
- Intra-group liquidity transfers (subsidiary HQLA counts only up to subsidiary's net outflows)
- Stress testing: results sent to SBV within 10 days; scenarios include 3-notch rating downgrade, market volatility, and counterparty-specific funding loss
- HQLA reserve: must hold unencumbered liquid core (cash + government bonds) as last-resort buffer

## LCR Breach Triggers

- "At-risk" status: HQLA < 90% of minimum required for 30 consecutive days
- "Lost payment capacity": unable to meet obligations within 30 days of maturity
