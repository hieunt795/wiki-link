---
node_id: fed_reserve_demand_reduction_tools_001
type: framework
title: Fed Reserve Demand Reduction Four Policy Tools
aliases:
- reduce reserve demand Fed
- four policies ample reserves
- TOMO TOMOs period-end sterilization
- IORB tiering reserves
- Fedwire LSM liquidity savings
- supply driven demand driven ample reserves
- bốn công cụ giảm cầu dự trữ Fed
domain:
  primary: monetary_policy
  secondary: financial_markets
tags:
- reserves
- fed_balance_sheet
- qt
- ample_reserves
- tomo
- iorb_tiering
- lsm
- fedwire
- liquidity_regulation
confidence: 1
stability: stable
thesis: "If the Fed aims to reduce the size of its balance sheet, four enabling policy tools can reduce the minimum required quantity of reserve balances without disrupting monetary policy implementation: (1) Temporary Open Market Operations (TOMOs) to sterilize unintended reserve shocks (TGA changes, FBO quarter-end window dressing); (2) revising liquidity regulations to reduce GSIB aversion to using Fed facilities; (3) adding a Liquidity Savings Mechanism (LSM) to Fedwire; and (4) tiering the IORB rate so banks with excess reserves prefer to lend them rather than hoard. The UK (BoE demand-driven approach) and Norway/New Zealand (IORB tiering) provide empirical precedents."
source_refs:
- path: 02_sources/books/duffie_bpea_payments_2026/Duffie_BPEA_Payments_Liquidity_2026.md
  pages: lines 50-805 (Sections I.D through VIII)
  weight: primary
related:
- node: '[[Fed Balance Sheet Floor Payment System Reserve Demand]]'
  relation: extends
- node: '[[Standing Repo Facility SRF Fed Backstop]]'
  relation: related_mechanism
- node: '[[Fed Policy Rate Shift EFFR To Secured Rate TGCR]]'
  relation: context
date_created: '2026-05-23'
date_updated: '2026-05-23'
---

## Supply-Driven vs Demand-Driven Ample Reserves

| Approach | Reserve Level | Rate Volatility | SRF Usage | Risk |
|----------|--------------|-----------------|-----------|------|
| **Supply-driven** | Conservatively large | Very low | Minimal (stigma preserved) | Ratchet effect — ever-larger reserve addiction |
| **Demand-driven** | Smaller standing supply | Higher (rate signals needed) | Frequent, normalized | Occasional liquidity crunches during stigma de-normalization |

**BoE example (2026)**: UK reduced sterling reserves from near £1T peak to £646B by late Jan 2026. Banks actively use STR (Short Term Repo) on a full-allotment basis at Bank Rate weekly. This demand-driven success gives the Fed a model. [RAW-CLIP]

**ECB**: Plans demand-driven approach for its ongoing QT — Schnabel (Nov 2025): "In a demand-driven framework, the central bank's operations are not a liquidity backstop. They are there to be used by banks as part of their day-to-day liquidity management." [RAW-CLIP]

## Policy Tool 1 — Temporary Open Market Operations (TOMOs)

**Problem**: Unintended period-end reserve shortfalls from:
- FBO (foreign banking organizations) quarter-end window dressing: shed reserves to reduce balance-sheet size for capital adequacy snapshots → system-wide reserves drop $100-400B at quarter ends
- TGA volatility: tax payments, debt issuance/spending cycles
- FIMA reverse repo pool fluctuations

**Solution**: Pre-announced TOMOs (term repos or T-bill purchases) that inject reserves at quarter-end and unwind immediately after. Could be priced at IORB-5 to IORB-10bps to reduce SRF stigma (below-IORB repo is clearly a profit opportunity, not a stress signal). [RAW-CLIP]

**Estimated quarter-end SOFR-IORB fixed effect**: ~10bps on average; ~30bps at the 99th percentile. TOMOs would reduce but not eliminate this effect. [RAW-CLIP]

## Policy Tool 2 — Liquidity Regulation Reform

**Problem**: Post-GFC liquidity regulations (Reg YY, CLAR, RLAP) require GSIBs to demonstrate self-sufficient intraday liquidity → systematic disincentive to use daylight overdrafts, Discount Window, or SRF. Peak system-wide daylight overdrafts: < $5B/day (vs $120B/day by top-10 banks pre-GFC). [RAW-CLIP]

**Proposed fixes**:
- Allow non-HQLA collateral held at Discount Window/SRF to count toward Reg YY liquidity requirements
- Re-examine supervisory preference for reserves over T-bills in LCR HQLA calculation
- If GSIBs become comfortable with large daylight overdrafts (re-normalize), required opening balances could fall dramatically [RAW-CLIP]

**Risk**: If banks remain unwilling to use Fed facilities except in existential crises, counting capacity as liquidity could induce fire-sale behavior during stress. [RAW-CLIP]

## Policy Tool 3 — Liquidity Savings Mechanism (LSM) for Fedwire

**Problem**: Fedwire uses Real-Time Gross Settlement (RTGS) with no LSM → each bank needs to pre-load reserve balances to cover its largest intraday net outflows; payment throttling cascades when reserves are tight. [RAW-CLIP]

**LSM mechanism**: Banks queue large outgoing payments; LSM offsets them bilaterally or multilaterally against queued incoming payments → only the net flows require balances. Example: 3 banks in a circle can settle $50-60 payments using only $5 of actual reserves. [RAW-CLIP]

**International evidence**:
- CHAPS (UK): LSM reduced required liquidity ~20%; payment efficiency increased from ~5 to >10 (vs Fedwire ≈4)
- BOK-Wire+ (Korea): 20% liquidity savings within one month
- BOJ-NET (Japan): ~15% savings
- Lynx (Canada): efficiency improved 30%+ vs predecessor

**Constraint**: Massive multi-year engineering project for the world's largest payment system. Banks would also need to retool internal payment systems. [RAW-CLIP]

## Policy Tool 4 — Tiering IORB Remuneration

**Problem**: Flat IORB means banks earn the same rate on every dollar of reserves → no incentive to lend excess reserves; interbank market atrophied.

**Solution**: Two-tier IORB — each bank gets a quota (linked to payment system needs); balances within quota earn full IORB; above-quota earns IORB − spread (enough to overcome FDIC+capital friction costs). Banks with excess reserves prefer to lend at the interbank rate rather than earn the reduced sub-IORB tier.

**Key result (Baughman and Carapella 2019)**: Tiering increases interbank lending, reduces required reserves, reduces CB interest expense — all simultaneously. [RAW-CLIP]

**Empirical evidence**:
- Norway (Oct 2011): overnight interbank volume surged dramatically after introducing two tiers
- New Zealand (2007): RBNZ reduced settlement balances while keeping overnight rates stable [RAW-CLIP]

**Fed precedent**: A two-tier IORB was briefly active in Oct-Dec 2008 before collapsing under the ZLB + QE dynamic. No new legislation required — existing statutes permit it. [RAW-CLIP]

## Ratchet Effect Risk (Acharya and Rajan 2022)

Abundant reserves cause banks to:
1. Stop developing efficient liquidity management systems
2. Provide more liquidity-intensive products to customers (credit lines, demand deposits)
3. Rely more on opening balances than payment inflows

Each of these is hard to reverse → even if per-dollar costs are small, absolute reserve demand escalates. Supply-driven approach risks permanent reserve demand ratcheting upward. [RAW-CLIP]
