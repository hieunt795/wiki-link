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
confidence: 4
stability: stable
thesis: 'Reserve Management Operations (RMOs), formally implemented as "Reserve Management Purchases" (RMPs) in late 2025, are the Fed''s tool for maintaining an ample supply of reserves post-QT through outright purchases of short-term Treasury securities (bills). Triggered by money market stress (SOFR-IORB spreads > 30bps), RMOs are operationally distinct from Quantitative Easing (QE); while QE aims to extract duration risk for stimulus, RMOs purely offset structural reserve drains (currency growth, TGA accumulation) to ensure effective control of the policy rate. On December 10, 2025, the Fed initiated RMPs at a rate of ~$40 billion per month following a sharp spike in repo rates.

'
source_refs:
- path: 02_sources/books/duffie_bpea_payments_2026/Duffie_BPEA_Payments_Liquidity_2026.md
  pages: "2, 10, 27"
  weight: primary
- path: 02_sources/books/conks/Conks - Plumping note (Money market.md
  pages: Plumbing Notes - It's Not QE; Plumbing Notes - The Post-QT Era
  weight: supporting
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

## The 2025 Reserve Scarcity Trigger

The transition from Quantitative Tightening (QT) to Reserve Management Operations was triggered by acute money market stress in late 2025:

1. **QT Halt (Oct 29, 2025):** The FOMC announced an immediate stop to balance sheet reduction after repo rates (SOFR) began consistently trading significantly above the Interest on Reserve Balances (IORB). [RAW-BOOK Duffie 2026, p.2]
2. **Spread Spike (Oct 31, 2025):** SOFR reached **32 basis points above IORB**, signaling that reserves had reached the "Lowest Comfortable Level" (LCLoR) and were no longer ample enough to facilitate seamless settlement without rate volatility. [RAW-BOOK Duffie 2026, p.2]
3. **RMP Initiation (Dec 10, 2025):** Fed Chair Jay Powell announced the resumption of "reserve management purchases" (RMPs) to maintain an ample supply of reserves. [RAW-BOOK Duffie 2026, p.2]

---

## RMP Operational Arithmetic (2025-2026)

The Duffie (2026) analysis details the scale of the Fed's response:
- **Purchase Rate:** ~$40 billion per month in Treasury bills.
- **Timeline:** Continued from December 2025 until at least May 2026.
- **Cumulative Injection:** Aimed at restoring a buffer of ~$200-250B above the observed LCLoR to dampen rate spikes.

**A -> B -> C Causal Chain:**
QT drains reserves → Bank settlement liquidity tightens → Banks/Dealers demand more reserves for payment timing → SOFR spikes above IORB → Fed buys bills (RMPs) → Reserves injected → Rate volatility subsides.

---

## Why Not IORB/SRFR Cuts Instead?

Fed alternatives to RMOs that were considered but rejected:

1. **IORB cut**: Would attract banks to deploy more reserves into repo → eases SOFR. But: IORB cuts don't address structural reserve drain; usually deployed only when EFFR drifts toward IORB (signal of genuine scarcity). Also risks inter-Fed political conflict (Board controls IORB).

2. **SRFR cut**: Reduces the floor for SRF borrowing → dealers more willing to tap Fed for repo. But: lowering SRFR below the target range upper limit risks Fed credibility signal. "Tarnishes credibility" per STIR community consensus. [RAW-CLIP Conks Oct 27 Update]

3. **Term repos**: Proposed as fix for year-end spikes. Would allow dealers to lock in funding via SRF over balance sheet-intensive periods. Not yet implemented as of Dec 2025. [RAW-CLIP Conks Oct 27 Update]

**Conks' preferred sequence:** Announce QT end → start RMOs ($20-30B/month) → let market front-run SOFR-FF compression → avoid IORB/SRFR cuts unless EFFR drifts materially.
