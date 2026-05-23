---
node_id: fed_policy_rate_shift_effr_to_secured_rate_tgcr_001
type: mechanism
title: Fed Policy Rate Shift EFFR to Secured Rate TGCR
aliases:
- TGCR targeting
- EFFR to TGCR shift
- Logan rate reform
- secured policy rate
- OBFR
- secured rate complex
- two-step rate evolution
- TGCR then SOFR
- mục tiêu lãi suất chính sách có bảo đảm
- chuyển đổi EFFR sang TGCR
domain:
  primary: monetary_policy
tags:
- fed
- effr
- tgcr
- sofr
- bgcr
- obfr
- policy_rate
- money_market
- floor_system
- operating_framework
- secured-standard
confidence: 3
stability: evolving
thesis: 'The Fed''s EFFR target has become a technical artifact of FHLB-GSE regulatory
  arbitrage rather than genuine interbank borrowing demand — Fed Funds volume collapsed
  ~80% post-2008 and surviving activity is dominated by FHLB→FBO IORB arbitrage and
  FHLB→G-SIB IBDA intraday liquidity trades. The inevitable replacement is a two-step
  evolution: first TGCR (Triparty General Collateral Rate, $1T+ of MMF→dealer repo
  funding), then SOFR (broader, captures DVP segment too). TGCR is preferred over
  BGCR (adds GCF interdealer noise) and over SOFR (adds speculative DVP volumes that
  will be reshaped by the SEC''s July 2027 central clearing mandate). Targeting an
  administered rate (IORB or ON RRP) was ruled out as it would shift power between
  Fed factions and erode public trust.

  '
source_refs:
- path: 02_sources/books/conks/Conks - Fed's Policies and Facilities.md
  pages: The Fed's New Target Part I; The Fed's New Target Part II
  weight: primary
- path: 02_sources/books/conks/Conks - Plumping note (Money market.md
  pages: ''
  weight: secondary
related:
- node: '[[Repo_Market_Structure_GC_SC_Cleared_Segments_And_Sec_Mandate]]'
  relation: rate_complex_this_node_targets
- node: '[[FHLB_IBDA_Intraday_Resolution_Liquidity_And_Fed_Funds_Market_Survival]]'
  relation: explains_why_EFFR_is_technical_artifact
- node: '[[LCLoR_Lowest_Comfortable_Level_Of_Reserves_And_QT_Calibration]]'
  relation: reserve_scarcity_signals_that_matter_more_than_EFFR
- node: '[[Fed_Ample_Reserves_Rate_Control_Framework]]'
  relation: current_framework_being_updated
date_created: '2026-05-22'
date_updated: '2026-05-23'
---


## Why EFFR is Dying as a Policy Target

### The Collapse of the Fed Funds Market

Post-2008 QE injected massive reserves into G-SIBs → no bank needed to borrow overnight in the unsecured market. Fed Funds volume fell ~80%. The surviving activity is not genuine interbank borrowing but two regulatory arbitrage trades:

1. **FHLB→FBO IORB arbitrage**: FHLBs (can't earn IORB) lend FF to foreign bank branches (FBOs) at below-IORB rates → FBOs deposit at Fed, earn IORB, pocket spread (FBOs exempt from FDIC insurance → arbitrage persists)

2. **FHLB→G-SIB IBDA trades**: FHLBs supply intraday resolution liquidity via Interest-Bearing Deposit Accounts at 5-10bps above target range (see `[[FHLB_IBDA_Intraday_Resolution_Liquidity_And_Fed_Funds_Market_Survival]]`)

Neither reflects genuine dollar scarcity or interbank borrowing demand. EFFR is thus an artifact of GSE restrictions (FHLBs can't earn IORB) and bank resolution rules. [RAW-CLIP Conks New Target I & II]

## Why Not an Administered Rate Target?

Options rejected: IORB, ON RRP as the new target rate.

**Power dynamics problem**: Different Fed bodies control different rates:
- Board of Governors: sets IORB
- FOMC: sets SRF rate (SRFR) and ON RRP rate
- Reserve Bank boards: set Discount Window rate

Switching to an administered rate target would grant one faction outsized control → inter-Fed political conflict → erosion of public trust and market clarity. [RAW-CLIP Conks New Target II]

**Rate basket rejected**: A basket of multiple rates would create disagreement among voting members on weights and communication — "a recipe for disaster."

## The Three Secured Benchmarks

| Benchmark | Full Name | Segments Captured | Volume |
|-----------|----------|------------------|--------|
| TGCR | Triparty General Collateral Rate | Uncleared triparty only (MMF→dealer) | $1T+ |
| BGCR | Broad General Collateral Rate | TGCR + GCF interdealer | TGCR + ~$100B |
| SOFR | Secured Overnight Financing Rate | TGCR + GCF + DVP bilateral | $4T+ |

### Why TGCR > BGCR as Target

BGCR adds only ~$100B in interdealer GCF volume on top of TGCR's $1T+. The GCF addition introduces:
- Dealer-to-dealer volatility (balance sheet tidying before regulatory reporting dates)
- Quarter-end spikes from banks compressing balance sheets

The Fed uses volume-weighted means, which masks extreme outliers somewhat — but GCF noise remains unnecessary. BGCR and TGCR print at nearly identical levels, so BGCR has no informational advantage over TGCR. [RAW-CLIP Conks New Target II]

### Why TGCR > SOFR (for now)

SOFR includes DVP bilateral repo volumes (~$4T total). DVP segment is dominated by hedge fund leveraged trades (basis, RV). These volumes will be dramatically reshaped by the **SEC's mandatory central clearing mandate (July 2027)**, which forces most NCCBR (uncleared bilateral) trades into FICC-cleared DVP segments.

Targeting SOFR before this transition completes means the policy target rate would be volatile during the migration. The two-step approach avoids this. [RAW-CLIP Conks New Target II]

## The Two-Step Target Evolution

```
Step 1: EFFR → TGCR (within ~2 years of announcement)
  → "Holding period" while repo market structural shifts complete
  → Central clearing mandate implementation (July 2026-2027)
  → Fed's own SRF repo operations centrally cleared
  
Step 2: TGCR → SOFR (after Step 1 complete)
  → SOFR stable after NCCBR exodus to cleared segments
  → Targets broader, deeper, most representative rate
  → Compresses rate volatility across secured rate complex
```

**Timeline caveat:** The process spans 3 quarters to 2 years from selection to execution. Markets will price effects immediately upon announcement. Potential delay under Warsh-led Fed that favors smaller balance sheet. [RAW-CLIP Conks New Target II]

## Rate Reference Glossary

| Rate | Full Name | Market | Nature |
|------|----------|--------|--------|
| EFFR | Effective Federal Funds Rate | Overnight unsecured interbank | Current Fed target |
| OBFR | Overnight Bank Funding Rate | EFFR + eurodollar/offshore unsecured | EFFR companion; barely adds volume |
| TGCR | Triparty General Collateral Rate | Uncleared triparty GC repo | Likely next target |
| BGCR | Broad General Collateral Rate | TGCR + GCF interdealer | Near-identical to TGCR |
| SOFR | Secured Overnight Financing Rate | All o/n repo (triparty + GCF + DVP) | End-state target |

**OBFR note:** OBFR = EFFR + Eurodollar overnight trades. It barely adds volume over EFFR and thus fails to represent broader dollar funding markets — ruled out as a target. [RAW-CLIP Conks New Target II]


