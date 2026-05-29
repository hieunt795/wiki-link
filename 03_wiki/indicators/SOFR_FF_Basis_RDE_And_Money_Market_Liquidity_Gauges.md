---
node_id: sofr_ff_basis_rde_liquidity_gauges_001
type: indicator
title: SOFR-FF Basis RDE and Money Market Liquidity Gauges
aliases:
- SOFR-FF basis
- SOFR FF spread
- RDE
- reserve demand elasticity
- liquidity mirage
- money market blindspot
- TGA drawdown liquidity
- extraordinary measures headroom
- G Fund TSP
- ESF Exchange Stabilization Fund
- CSRD Fund
- chênh lệch SOFR-FF
- đo lường thanh khoản thị trường tiền tệ
domain:
  primary: monetary_policy
  secondary:
  - financial_markets
tags:
- sofr
- effr
- fed-funds
- rde
- reserves
- liquidity
- TGA
- debt-ceiling
- extraordinary-measures
- MMF
- RRP
- QT
confidence: 3
stability: evolving
thesis: 'Two complementary gauges measure reserve conditions in real time: (1) the
  SOFR-FF futures basis — positive = SOFR below EFFR = reserves abundant; negative
  = repo tighter than fed funds = reserves scarce; and (2) the Fed''s internal Reserve
  Demand Elasticity (RDE) — near zero = ample, sharply negative = approaching scarcity
  → triggers QT pause/end. Both gauges are distorted by a "liquidity mirage" during
  debt ceiling episodes: TGA drawdowns inject reserves into the system, but much of
  the apparent liquidity flows into RRP rather than the banking system — creating
  an illusion of ample reserves that reverses sharply when the ceiling is resolved
  and TGA is refilled.

  '
source_refs:
- path: 02_sources/books/conks/Conks - Shadow Banking and Cash Markets.md
  pages: Money Market Blindspot I; Money Market Blindspot II
  weight: primary
parent_node: null
related:
- node: '[[LCLoR_Lowest_Comfortable_Level_Of_Reserves_And_QT_Calibration]]'
  relation: RDE_feeds_into_LCLoR_determination
- node: '[[Repo_Market_Structure_GC_SC_Cleared_Segments_And_Sec_Mandate]]'
  relation: SOFR_basis_reflects_conditions_in_repo_segments
- node: '[[Fed_Policy_Rate_Shift_EFFR_To_Secured_Rate_Tgcr]]'
  relation: SOFR_FF_basis_informs_why_EFFR_is_unreliable_anchor
- node: '[[Fed_Ample_Reserves_Rate_Control_Framework]]'
  relation: framework_being_gauged_by_these_indicators
date_created: '2026-05-23'
date_updated: '2026-05-23'
---


## The SOFR-FF Futures Basis

### What It Measures

The SOFR-FF basis is the spread between SOFR futures and Fed Funds futures at equivalent tenors. Since both are overnight rates anchored to the same FOMC target range, any persistent divergence reflects relative liquidity conditions in the secured vs unsecured money markets.

| Basis State | Signal | Implication |
|------------|--------|-------------|
| **Positive** (SOFR < EFFR) | Repo is cheaper than fed funds | Reserves abundant; collateral flows freely |
| **Near zero** | Conditions balanced | Transition zone |
| **Negative** (SOFR > EFFR) | Repo is more expensive than fed funds | Reserves scarce; repo market stressed |

**Why this works:** In ample reserves, dealers have excess reserves → willing to lend in repo at or below unsecured rates. As reserves shrink, repo tightens relative to EFFR → basis goes negative. [RAW-CLIP Conks Blindspot I]

### SOFR-FF Forward Curve as Liquidity Timeline

STIR (short-term interest rate) traders price the SOFR-FF basis forward to map expected reserve depletion:

```
Current basis: [+15bps] → reserves ample now
3m forward:    [+8bps]  → expected continued QT, reserves shrinking
6m forward:    [-5bps]  → market pricing in repo tightening (reserves scarce)
```

Negative basis in the forward curve signals the market's estimate of when QT will exhaust the comfortable reserve buffer — before the Fed's own LCLoR signal fires. [RAW-CLIP Conks Blindspot I]

---

## RDE: Reserve Demand Elasticity

### Definition

The Fed's internal measure of how sensitive the reserve market is to small changes in reserve supply. Published in the Monetary Policy Report and fed into QT calibration decisions.

| RDE Value | Interpretation | Fed Response |
|-----------|---------------|-------------|
| Near 0 | Reserves ample; demand inelastic | Continue QT |
| Moderately negative | Buffer thinning | Slow QT pace |
| Sharply negative | Reserve scarcity approaching | Pause or end QT |

**Mechanics:** When reserves are ample, banks hold excess reserves without sensitivity to marginal changes — RDE ≈ 0. As reserves approach LCLoR, each marginal reserve unit becomes more precious → demand becomes elastic → RDE moves sharply negative. [RAW-CLIP Conks Blindspot I]

### RDE vs SOFR-FF Basis

Both signal the same underlying condition but from different vantage points:

- **SOFR-FF basis**: Market-derived, real-time, tradeable, forward-looking
- **RDE**: Fed's internal model, backward-looking, updated quarterly, directly informs QT decisions

The SOFR-FF futures market can anticipate RDE deterioration weeks before the Fed publishes it. [RAW-CLIP Conks Blindspot I]

---

## The Liquidity Mirage (Debt Ceiling Episodes)

### Mechanism

During debt ceiling standoffs, the Treasury cannot issue new debt → TGA balance runs down as the Treasury spends from existing funds without replenishment. On accounting, TGA drawdowns inject reserves into the banking system (Treasury spends → recipients' bank accounts credited → bank reserves rise).

**The mirage:** This apparent reserve injection is partially or fully absorbed by RRP:

```
Treasury spends (TGA ↓) 
  → Government contractors, beneficiaries receive payments
  → Payments deposited into bank accounts
  → Banks with excess liquidity buy T-bills (bill yields fall)
  → Lower bill yields → MMFs switch from bills to ON RRP
  → RRP balance rises (reserves neutralized in RRP)
```

**Result:** The banking system looks liquid by traditional metrics (bank reserves up), but the actual reserve injection is partially sterilized by RRP. The Fed's models — calibrated on normal conditions — may see ample reserves when the effective free-float of usable reserves is lower. [RAW-CLIP Conks Blindspot I & II]

### The Double-Whammy Reversal

When the debt ceiling is resolved (or X-date avoided via deal):

1. **TGA refill**: Treasury issues massive wave of bills/notes to replenish TGA → drains reserves
2. **MMF rotation**: As bill yields rise (supply surge), MMFs shift from RRP back to bills → RRP falls (but this doesn't return reserves to banks — it just shifts from one Fed liability to another)
3. **Tax receipts**: April/September corporate and personal tax payments arrive simultaneously → further TGA buildup

Three simultaneous reserve drains → repo can gap wider sharply even if daily QT pace is unchanged. The SOFR-FF basis can flip negative within days. [RAW-CLIP Conks Blindspot II]

---

## Extraordinary Measures Specifics

When the US hits the debt ceiling, the Treasury Secretary invokes "extraordinary measures" to extend the borrowing runway without congressional action. Three main sources:

| Instrument | Full Name | Mechanism | Size |
|-----------|----------|-----------|------|
| **G Fund** | Government Securities Investment Fund (TSP) | Treasury suspends investment of federal employee retirement contributions; redeems existing G Fund Treasuries → creates headroom | ~$200B+ |
| **ESF** | Exchange Stabilization Fund | Treasury temporarily ceases investing ESF assets in Treasuries; statutory authority under Gold Reserve Act of 1934 | ~$30-40B |
| **CSRD Fund** | Civil Service Retirement and Disability Fund | OPM postpones reinvestment of civil service pension assets in Treasuries | ~$50B+ |

**Total extraordinary headroom:** ~$300B+ depending on existing fund balances. G Fund is always the largest single source.

**Timing:** Extraordinary measures typically provide 3-6 months of runway post-ceiling hit. Treasury publishes "Debt Limit Update" letters to Congress showing daily depletion rate. [RAW-CLIP Conks Blindspot II]

---

## MMF Structural Constraints on Liquidity Distribution

### WAM (Weighted Average Maturity) Constraint

SEC requires MMF portfolio WAM < 60 days. This forces MMFs toward:

- Overnight repos (0-day maturity, contributes 0 to WAM)
- 1-month T-bills (30-day maturity, counts fully)
- Avoidance of 3m+ bills, floating rate notes, and coupons

**Consequence:** MMFs are structurally demand-inelastic for longer-dated instruments → any reserve drain that forces MMFs to choose between very short instruments and ON RRP will consistently push money into ON RRP. The WAM constraint is why the TGA drawdown → RRP channel is so reliable. [RAW-CLIP Conks Blindspot II]

### TGA Target and Bill Supply

Treasury's stated TGA target: **~$850B** (Yellen policy, continued under Bessent). This target is driven by the size of short-term maturities coming due in any 30-day window — the Treasury holds ~1 month of payment obligations as a liquidity cushion.

When TGA falls below target during extraordinary measures, Treasury's first action on ceiling resolution is to rebuild to $850B → creating the double-whammy bill supply surge. [RAW-CLIP Conks Blindspot II]

---

## Basis Trade and Repo Demand Signal

SEC data shows hedge fund long Treasury positions financed via repo grew >50% YoY. The largest multi-strategy funds dominate this activity. Basis trade growth has two liquidity implications:

1. **Demand for repo funding**: Larger basis positions = more repo demand = upward pressure on SOFR relative to EFFR → SOFR-FF basis effect
2. **Systemic fragility**: Rapid basis trade unwind (margin call, volatility spike) causes simultaneous Treasury selling + repo market contraction → cascading liquidity stress (March 2020 episode; April 2025 tariff shock)

The SOFR-FF basis as a gauge inherits this basis-trade signal — a widening negative basis in stress can reflect both fundamental reserve scarcity and leveraged position liquidation simultaneously. [RAW-CLIP Conks Blindspot II]
