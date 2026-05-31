---
node_id: repo_market_structure_gc_sc_cleared_001
type: concept
title: Repo Market Structure GC SC Cleared Segments and SEC Mandate
aliases:
- repo market taxonomy
- GC repo vs SC repo
- triparty repo
- DVP repo
- NCCBR
- bilateral repo
- FICC clearing
- GCF repo
- specific collateral repo
- general collateral repo
- SEC Treasury clearing mandate
- cấu trúc thị trường repo
- repo thế chấp chung vs cụ thể
domain:
  primary: financial_markets
  secondary:
  - monetary_policy
tags:
- repo
- GC
- SC
- triparty
- DVP
- NCCBR
- FICC
- GCF
- clearing
- SEC-mandate
- SOFR
- TGCR
- BGCR
- money-market
confidence: 3
stability: evolving
thesis: 'The U.S. repo market is organized along two dimensions: (1) purpose — General
  Collateral (GC/triparty: cash-focused) vs Specific Collateral (SC/DVP/bilateral:
  securities-focused), and (2) clearing — centrally cleared via FICC vs non-centrally
  cleared. The four resulting segments (triparty uncleared, GCF cleared, DVP cleared,
  NCCBR uncleared) produce a rate hierarchy (o/n TPR < o/n GCF < o/n DVP < o/n NCCBR)
  and underlie the Fed''s three secured benchmarks (TGCR, BGCR, SOFR). The SEC''s
  mandatory central clearing mandate (July 2027) will force most NCCBR volumes into
  FICC-cleared segments, permanently reshaping the rate complex.

  '
source_refs:
- path: 02_sources/books/conks/Conks - Fed's Policies and Facilities.md
  pages: Plumbing Notes Repo 101; The Fed's New Target Part II
  weight: primary
parent_node: null
related:
- node: '[[Fed_Policy_Rate_Shift_EFFR_To_Secured_Rate_Tgcr]]'
  relation: rates_produced_by_this_structure
- node: '[[Treasury_Market_Dealer_Intermediation_Capacity]]'
  relation: dealers_primary_repo_intermediaries
- node: '[[Fixed_Income_Relative_Value_Framework]]'
  relation: NCCBR_primary_funding_for_RV_trades
- node: '[[LCLoR_Lowest_Comfortable_Level_Of_Reserves_And_QT_Calibration]]'
  relation: repo_rate_spikes_signal_reserve_scarcity
date_created: '2026-05-23'
date_updated: '2026-05-24'
---


## Scope Boundary

[LLM] This node is the canonical detailed taxonomy for U.S. repo segments across GC/SC purpose and cleared/uncleared structure.

[LLM] [[Repo_Market_Mechanics_Triparty_Bilateral]] should be used as the broad primer, while [[Repo_Market_Clearing_Segments_FICC_Triparty_GCF_DVP_NCCBR]] should be used only as the compact rate/clearing lookup.

## The Two Dimensions of Repo Structure

### Dimension 1: Purpose (What the Trade Achieves)

| Type | Abbreviation | Goal | Collateral | Venue |
|------|-------------|------|-----------|-------|
| General Collateral | GC | Raise cash / earn yield | Any basket of HQLA (Treasuries, Agency MBS) | BNY triparty platform |
| Specific Collateral | SC | Obtain specific security for trading | Named security | Fedwire (DVP settlement) |

**GC repo:** Cash lender doesn't care which specific security backs the loan — any HQLA suffices. Cash and collateral are locked in "boxes" on BNY's triparty custodian system, preventing active trading. Money market funds are the dominant cash lenders; primary dealers are dominant borrowers.

**SC repo (bilateral/DVP):** Security is the primary objective. Cash lender wants a specific Treasury to execute basis trades, RV trades, or futures delivery. Securities AND cash can be freely transferred during the trade. Primarily used by hedge funds (via dealers) for leveraged trades. [RAW-CLIP Conks Repo 101]

### Dimension 2: Clearing (Who Guarantees the Trade)

| Clearing Type | Abbreviation | Who Can Access | Risk Management |
|--------------|-------------|---------------|----------------|
| Centrally cleared | CC | FICC members (large dealers, banks) + sponsored clients | FICC absorbs counterparty default losses; requires margin posting |
| Non-centrally cleared | NCC | Any bilateral agreement | No third-party guarantee; lower margin → higher leverage available |

**FICC** (Fixed Income Clearing Corporation) is the sole central counterparty for U.S. repo markets. Membership is costly and restricted to large dealers and banks.

## The Four Segments

```
GC (triparty) + Uncleared = Triparty (open)
GC (triparty) + Cleared   = GCF Repo (interdealer)
SC (bilateral) + Cleared  = DVP Repo (+ Sponsored DVP + DVP ACS)
SC (bilateral) + Uncleared = NCCBR
```

### 1. Triparty (Uncleared GC) — The Base Layer

- **Platform:** BNY Mellon triparty system
- **Participants:** Money market funds → Primary dealers
- **Rate:** o/n TPR (overnight triparty rate)
- **Benchmark:** TGCR (Triparty General Collateral Rate, published by NY Fed)
- **Function:** Core funding market — dealers raise cash from MMFs to finance their operations

### 2. GCF Repo (Centrally Cleared GC Interdealer)

- **Clearing:** FICC GCF Repo Service
- **Participants:** FICC member dealers ↔ other FICC member dealers/banks
- **Rate:** o/n GCF (DTCC GCF Repo Index)
- **Note:** Smaller dealers without triparty access borrow from larger dealers here
- **Rate premium:** o/n GCF > o/n TPR (reflects interdealer vs client-to-dealer friction)

### 3. DVP Repo (Centrally Cleared SC)

- **Platform:** Fedwire (DVP settlement)
- **Clearing:** FICC DVP Repo Service + Sponsored DVP + DVP ACS (Agent Clearing Service)
- **Participants:** FICC dealers ↔ other dealers; non-members via "sponsored" access
- **Rate:** o/n DVP (OFR Cleared Repo benchmark)
- **Function:** Funding for leveraged basis/RV trades; securities can be actively used
- **Note:** Sponsored Repo and ACS allow hedge funds to access cleared clearing without direct FICC membership

### 4. NCCBR (Non-Centrally Cleared Bilateral Repo)

- **Platform:** Bilateral (no CCP)
- **Participants:** Dealers ↔ Hedge funds
- **Rate:** o/n NCCBR (NO published benchmark — opacity by design)
- **Function:** ~70% RV/basis trades; ~30% leveraged asset purchases (mortgage REITs, pensions)
- **Key feature:** No regulatory oversight → dealers compete on margins/haircuts → maximum hedge fund leverage
- **Rate:** Most expensive in private repo universe (reflects scarcity of leverage and collateral)

[RAW-CLIP Conks New Target II]

## Rate Hierarchy

```
Cheapest (most abundant cash)
  o/n TPR (uncleared triparty: MMF → dealer)
  o/n GCF (interdealer cleared triparty)
  o/n DVP (interdealer cleared bilateral + sponsored)
  o/n NCCBR (uncleared bilateral: dealer → hedge fund)
Most expensive (scarcest cash / most leverage available)
```

Higher rates reflect: (1) more creditworthy counterparty required, (2) higher friction/cost of clearing, (3) more leverage available (less regulation).

## Fed Secured Benchmarks

| Benchmark | Segments Captured | Volume (~) |
|-----------|------------------|-----------|
| TGCR (Triparty GC Rate) | o/n TPR uncleared only | $1T+ |
| BGCR (Broad GC Rate) | o/n TPR + o/n GCF | TGCR + ~$100B |
| SOFR (Secured Overnight Financing Rate) | o/n TPR + o/n GCF + o/n DVP | $4T+ |

**TGCR** is the "cleanest" benchmark: captures client-to-dealer funding rates without dealer-to-dealer volatility (BGCR adds GCF noise) or speculative segment rates (SOFR adds DVP noise). [RAW-CLIP Conks New Target II]

## Repo "Specials" and SOFR Distortion

### What is a Special?

In the SC (specific collateral) / DVP market, most securities trade at rates near GC rates. But certain securities experience outsized demand — enough that cash lenders accept *lower* repo rates just to obtain that specific bond. This is called a **"special"** (the security "trades special").

```
Specialness = GC rate − Repo rate on the specific security

High specialness → cash lenders accept near-zero or negative spreads just to get that bond
```

**Primary drivers of specials:**

1. **On-the-run Treasury auctions:** The latest issue of each maturity is in high demand due to liquidity premium. Specialness builds until the next auction is announced, then fades as supply increases.

2. **Cash-futures basis trades:** The CTD (cheapest-to-deliver) bond into a futures contract — and close alternatives — experience high demand from basis traders. CTD often trades special near futures roll periods. [RAW-CLIP Conks Dislocation Part II]

### Why Specials Distort SOFR

SOFR is a volume-weighted average of rates across triparty, GCF, and FICC-DVP segments. When specials trade in the DVP market at rates significantly below GC, they pull SOFR *downward* (artificially low). As the central clearing mandate pushes more NCCBR volume into the DVP service, more specials will flow into SOFR's calculation.

**Fed's SOFR Modification (July 2024 Proposal):** Remove the **lowest 20%** of DVP repo volumes by rate from the SOFR calculation (replacing the prior approach of a volume-weighted trim of the lower quarter). This prevents a growing population of DVP specials from suppressing the benchmark. [RAW-CLIP Conks Dislocation Part II]

**Note:** NCCBR is excluded from SOFR entirely — the market was opaque with no OFR data available when SOFR was designed, and remains excluded by design. This means the most leveraged, most specialized repo market is invisible to the Fed's primary benchmark.

---

## SEC Mandatory Central Clearing Mandate (July 2027)

The SEC has mandated central clearing for almost all UST-backed repos conducted between FICC members:
- **July 2026 deadline**: MMFs and other cash lenders must shift from uncleared triparty to centrally cleared triparty segments
- **July 2027 deadline**: Most NCCBR volumes must migrate to FICC-cleared segments (Sponsored DVP or DVP ACS)

**Effect:** NCCBR volumes will collapse as speculative trades shift to Sponsored DVP and DVP ACS. SOFR and o/n DVP rates will be reshaped by this migration. The Fed's secured benchmarks will all print within a tighter range post-mandate.

## FICC Clearing Expansion Services

To reduce barriers for non-members:
- **Sponsored Repo (Sponsored GC + Sponsored DVP):** FICC members sponsor non-member clients to trade in cleared markets
- **Agent Clearing Service (DVP ACS + Triparty ACS):** Members act as agents for client repo transactions

These services are accelerating the exodus from uncleared segments.
