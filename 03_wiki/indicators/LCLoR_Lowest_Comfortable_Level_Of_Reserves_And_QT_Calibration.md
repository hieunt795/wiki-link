---
node_id: lclor_qt_calibration_001
type: indicator
indicator_type: threshold
title: LCLoR Lowest Comfortable Level of Reserves and QT Calibration
aliases:
- LCLoR
- lowest comfortable level of reserves
- QT end signal
- reserve scarcity indicators
- pure reserves vs neutralized reserves
- plumbing soft landing
- mức dự trữ thoải mái thấp nhất
- hiệu chỉnh QT
domain:
  primary: monetary_policy
tags:
- fed
- QT
- reserves
- LCLoR
- EFFR
- repo-rates
- money-market
- daylight-overdraft
- ample-reserves
confidence: 3
stability: evolving
thesis: 'The Fed calibrates QT (quantitative tightening) to drain reserves until they
  hit the LCLoR (Lowest Comfortable Level of Reserves) — estimated ~$3T for the US
  banking system — below which repo rates spike above the EFFR target range. The key
  early-warning signals are: rising EFFR above IORB, increasing daylight overdraft
  volumes, SRF usage picking up, and SOFR/TGCR printing above IORB. The RRP balance
  falling to zero is NOT the LCLoR signal — it merely means excess liquidity has been
  redeployed from the Fed''s shock absorber to private markets.

  '
source_refs:
- path: 02_sources/books/conks/Conks - Fed's Policies and Facilities.md
  pages: The Fed's Reckoning Part I; The Fed's Reckoning Part II; The Fed's New Target
    Part I
  weight: primary
parent_node: null
related:
- node: '[[Ample_Reserves_Buffer_Sizing_Tga_Volatility]]'
  relation: quantifies_the_buffer_above_LCLoR
- node: '[[Quantitative_Tightening_Qt_Balance_Sheet_Runoff]]'
  relation: policy_stopped_by_LCLoR
- node: '[[Fed_Overnight_Reverse_Repo_On_Rrp]]'
  relation: misleading_proxy_for_LCLoR
- node: '[[Standing_Repo_Facility_SRF_Fed_Backstop]]'
  relation: activated_near_LCLoR
- node: '[[EFFR_Effective_Federal_Funds_Rate]]'
  relation: primary_LCLoR_canary
date_created: '2026-05-23'
date_updated: '2026-05-23'
---


## What is LCLoR?

"Lowest Comfortable Level of Reserves" — the Fed's internal threshold below which reserve scarcity causes money market rates to spike outside the Fed's target range. When pure reserves approach LCLoR, the Fed must stop QT or inject reserves.

**Current estimate (2025):** ~$3T in pure reserves (reserve account balances at the Fed) is considered ample. The ~$400B buffer above LCLoR gives the Fed a narrow window before forced QT pause. [RAW-CLIP Conks Reckoning I]

## Pure Reserves vs Neutralized Reserves

| Type | Definition | Status |
|------|-----------|--------|
| Pure reserves | Reserve balances directly in bank master accounts at Fed | Immediately deployable for settlement |
| Neutralized reserves | Reserves parked in Fed's ON RRP → removed from banking system | NOT available for interbank settlement |

**Key dynamic (2023-2024):** $2.5T+ in neutralized reserves were stored in ON RRP due to Basel III leverage constraints + SLR expiration. As QT ran and T-bill/repo supply rose, MMFs shifted from RRP to private markets → "de-neutralization" converted neutralized to pure reserves, offsetting QT's reserve drain.

When ON RRP hit zero (2024): de-neutralization buffer exhausted → pure reserves now being drained directly by QT. [RAW-CLIP Conks Reckoning I]

## Reserve Scarcity Early Warning System

The Fed watches a multi-signal alarm system:

| Signal | Normal (Ample) | Warning (Approaching LCLoR) |
|--------|---------------|---------------------------|
| EFFR | At/below IORB | Rising above IORB |
| SOFR/TGCR | Below IORB | Approaching or above IORB |
| SRF usage | Zero | Increasing overnight use |
| Daylight overdrafts | Low (large banks) | Rising (smaller banks) |
| Repo spread to IOER | Stable | Widening |

**"Canary in the coalmine":** Rising EFFR above IORB is the clearest signal — it means some banks are willing to pay above IORB for reserve funding, indicating scarcity for at least some participants. [RAW-CLIP Conks Reckoning II]

## The RRP Zero Misconception

When the Fed's ON RRP balance hit zero (late 2024), many analysts declared an impending reserve crisis. In reality:
- RRP hitting zero simply means all excess cash was redeployed to private repo/T-bills — not that reserves are scarce
- Banks can still have excess reserves even with ON RRP at zero
- The ACTUAL warning is rising EFFR and SRF usage, NOT ON RRP balance

[RAW-CLIP Conks Reckoning I — "The Fed's RRP balance hitting zero has been widely touted as a major liquidity bottleneck. Instead, it merely reveals a banking system able to handle all remaining reserves."]

## QT Calibration Strategy

Fed uses a "plumbing soft landing" playbook:
1. **Step 1 (excess cash era):** QT runs; ON RRP absorbs excess cash that banks reject
2. **Step 2 (de-neutralization):** ON RRP drains as private markets become more attractive → pure reserve level maintained
3. **Step 3 (pure reserve drain):** With ON RRP at zero, QT drains pure reserves directly; window before LCLoR narrows
4. **Step 4 (pre-emptive tools):** Fed lowers ON RRP rate (done Dec 2024: -5bps to bottom of range), adds SRF auctions (morning + afternoon) to prevent rate spikes
5. **Step 5 (QT pause/RMOs):** Reserve Management Operations (RMOs) restart → "Not QE" — injecting reserves to prevent EFFR breakout

**Goal:** Maximize balance sheet reduction (reload capacity for next crisis) without causing repo rate eruption. Each pre-emptive tool buys more room for QT to continue. [RAW-CLIP Conks Reckoning I]

