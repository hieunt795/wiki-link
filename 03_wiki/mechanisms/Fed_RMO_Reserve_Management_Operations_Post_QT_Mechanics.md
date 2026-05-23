---
node_id: fed_rmo_reserve_management_operations_001
type: mechanism
title: Fed RMO Reserve Management Operations Post QT Mechanics
aliases:
- RMO
- reserve management operations
- RMOs
- POMO bill purchases
- post-QT reserve injections
- ceiling management operations
- CMO
- permanent open market operations bills
- bơm dự trữ quản lý cân đối tiền tệ
- nghiệp vụ thị trường mở quản lý dự trữ
domain:
  primary: monetary_policy
  secondary:
  - financial_markets
tags:
- fed
- rmo
- qe
- qt
- reserves
- bills
- TGA
- ample-reserves
- pomo
- sofr-ff
confidence: 3
stability: evolving
thesis: 'Reserve Management Operations (RMOs) are the Fed''s post-QT balance sheet
  tool: outright bill purchases that inject reserves to maintain ample liquidity —
  NOT QE. Unlike QE (swapping reserves for long-duration Treasuries to absorb risk
  and stimulate), RMOs simply offset the structural reserve drains that continue even
  after QT ends: currency in circulation growth, bank asset expansion, and TGA re-accumulation.
  The Fed ended QT2 on December 1, 2025; RMOs were expected to start Q1 2026 (~$20-30B/month),
  totaling ~$240B in reserve injections needed by end-2027.

  '
source_refs:
- path: 02_sources/books/conks/Conks - Plumping note (Money market.md
  pages: Plumbing Notes - It's Not QE; Plumbing Notes - The Post-QT Era; Plumbing Notes - A Faulty Relief Valve
  weight: primary
related:
- node: '[[Quantitative_Tightening_Qt_Balance_Sheet_Runoff]]'
  relation: RMO_replaces_QT_as_balance_sheet_tool
- node: '[[LCLoR_Lowest_Comfortable_Level_Of_Reserves_And_QT_Calibration]]'
  relation: LCLoR_triggers_RMO_onset
- node: '[[SOFR_FF_Basis_RDE_And_Money_Market_Liquidity_Gauges]]'
  relation: SOFR_FF_forward_curve_prices_expected_RMO_timing
- node: '[[Fed_Ample_Reserves_Rate_Control_Framework]]'
  relation: RMOs_maintain_ample_reserves_regime
date_created: '2026-05-23'
date_updated: '2026-05-23'
---


## RMOs vs QE: The Critical Distinction

The dominant misconception during QT2 end (late 2025) was that the Fed ending QT and buying bills was equivalent to QE. Conks' framework explicitly rejects this:

| Dimension | QE | RMO |
|-----------|-----|-----|
| Asset purchased | Long-duration USTs + MBS | Short-term bills only |
| Objective | Extract duration risk from private sector, stimulate via portfolio rebalancing | Maintain ample interbank reserves (plumbing) |
| Transmission | Risk assets via wealth/portfolio channel | Short-term interest rates (SOFR-FF basis, XCCY basis) |
| Balance sheet impact | Grows Treasuries as % of SOMA | Grows bills on SOMA |
| Stimulative? | Yes (QE is a monetary policy tool) | No — purely operational maintenance |
| Historical analog | QE1 (2008), QE2 (2010), COVID QE (2020) | Pre-GFC OMOs for reserve targeting |

**Key Conks quote:** "Slight changes in interbank liquidity don't prevent or encourage passive flows from bidding up risk assets or hedge funds from entering long positions via their prime broker." [RAW-CLIP Conks It's Not QE]

TGA drawdowns being "positive for risk assets" is explicitly called "just plain wrong" — no correlation or causation to risk assets from reserve level changes per se. [RAW-CLIP Conks It's Not QE]

---

## Why Reserves Keep Draining Even After QT Ends

Three "permanent" reserve drain forces persist regardless of QT status:

### 1. Currency Drain
When bank customers demand physical cash → bank pays Fed using reserves → reserves decline, currency in circulation rises.

```
T-account:
  Fed: ↑CURRENCY (liability), ↓RESERVES (liability)
  Bank: ↓RESERVES (asset), ↓DEPOSITS (liability)
```

Physical cash supply: Fed sends armored trucks to banks that need currency. [RAW-CLIP Conks It's Not QE]

### 2. Bank Asset Expansion
As banks lend and grow assets → reserves must grow proportionally to settle larger payment flows between banks. Banks don't need reserves to make loans (they need capital); they do need reserves to settle payments between banks when borrowers spend.

**Why:** Rising bank loan book → more interbank payments → more reserve demand for settlement. [RAW-CLIP Conks It's Not QE]

### 3. TGA Re-accumulation
After any debt ceiling resolution or government spending slowdown, Treasury rebuilds its TGA. Each $1 held in TGA is $1 not in the banking system.

**TGA target trajectory:** Yellen-era $850B target → Bessent maintains → likely rises to $900B+ by 2026 year-end as Treasury shifts issuance to more bills (which require larger cash cushions due to more frequent maturities). [RAW-CLIP Conks Post-QT Era]

---

## Structural Reserve Drain Arithmetic

Conks' estimate as of QT end (Dec 1, 2025):
- Reserves: ~$100B above LCLoR (still "above scarcity" but narrowing)
- Expected RMO size: **$20-30B/month**
- Total RMOs needed by end-2027: **~$240B**

Driven by:
- Secular currency demand growth (steady drain ~$10B/month structural)
- $50-100B TGA increase toward $900B target
- Bank balance sheet expansion as "balance sheet winter" ends post-QT

---

## CMOs vs RMOs

The Fed distinguishes between two types of post-QT reserve operations:

| Type | Name | Function |
|------|------|---------|
| **RMOs** | Reserve Management Operations | Routine bill purchases; maintain ample reserves long-term |
| **CMOs** | Ceiling Management Operations | Extra add-on; hold SOFR/EFFR well within target range (not just in range) |

CMOs are more aggressive — used when money market rates approach the upper boundary. RMOs are the steady-state tool. [RAW-CLIP Conks A Faulty Relief Valve]

---

## Timing and SOFR-FF Signal

The market prices expected RMO start via relative SOFR-FF spreads:

```
Jan'26 SOFR-FF vs Mar'26 SOFR-FF:
  Jan spread tightening → market betting on earlier RMOs
  Jan spread widening   → market pricing delayed injections

Dec'25/Jan'26 SOFR-FF spread:
  Negative = market expects MORE easing in Jan than Dec (earlier injections)
  Positive = market expects Dec tighter than Jan (delayed)
```

Key dynamic: "Fed will keep its ample reserve regime ticking over (almost) on autopilot" — not a dramatic policy shift, but routine operational maintenance. [RAW-CLIP Conks Post-QT Era]

---

## Why Not IORB/SRFR Cuts Instead?

Fed alternatives to RMOs that were considered but rejected:

1. **IORB cut**: Would attract banks to deploy more reserves into repo → eases SOFR. But: IORB cuts don't address structural reserve drain; usually deployed only when EFFR drifts toward IORB (signal of genuine scarcity). Also risks inter-Fed political conflict (Board controls IORB).

2. **SRFR cut**: Reduces the floor for SRF borrowing → dealers more willing to tap Fed for repo. But: lowering SRFR below the target range upper limit risks Fed credibility signal. "Tarnishes credibility" per STIR community consensus. [RAW-CLIP Conks Oct 27 Update]

3. **Term repos**: Proposed as fix for year-end spikes. Would allow dealers to lock in funding via SRF over balance sheet-intensive periods. Not yet implemented as of Dec 2025. [RAW-CLIP Conks Oct 27 Update]

**Conks' preferred sequence:** Announce QT end → start RMOs ($20-30B/month) → let market front-run SOFR-FF compression → avoid IORB/SRFR cuts unless EFFR drifts materially.
