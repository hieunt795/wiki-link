---
node_id: repo_market_mechanics_triparty_bilateral_001
type: mechanism
title: Repo Market Mechanics Triparty Bilateral
aliases:
- repo
- repurchase agreement
- triparty repo
- GCF repo
- NCCBR
- thi truong repo
- hop dong mua lai
domain:
  primary: financial_markets
tags:
- repo
- sofr
- triparty
- nccbr
- collateral
- shadow-banking
- dealer
confidence: 3
stability: evolving
thesis: 'The repo market is the secured funding backbone of the US financial system,
  executing 3-4 trillion dollars daily across three segments: triparty (custodian-intermediated),
  GCF (centrally cleared interdealer), and NCCBR (bilateral, hedge-fund-dominated).
  Repo makes Treasuries functionally equivalent to cash and prices its rates into
  SOFR, the global USD benchmark.'
source_refs:
- path: 02_sources/books/conks/Conk - Repo.md
  pages: Demystifying the Repo Market, Repo Market Blindspot
  weight: primary
parent_node: null
related:
- node: '[[Collateral Velocity And Pledged Collateral Market Mechanics]]'
  relation: shared_tag:repo
- node: '[[Triparty Repo Market Structure And Daily Cycle]]'
  relation: shared_tag:repo
- node: '[[Collateral Velocity and Rehypothecation]]'
  relation: shared_tag:repo
- node: '[[Monetary Policy Transmission via Collateral and Repo Markets]]'
  relation: shared_tag:repo
- node: '[[Standing Repo Facility SRF Fed Backstop]]'
  relation: shared_tag:repo
- node: '[[Repo_Market_Structure_GC_SC_Cleared_Segments_And_Sec_Mandate]]'
  relation: canonical_repo_segment_taxonomy
- node: '[[Repo_Market_Clearing_Segments_FICC_Triparty_GCF_DVP_NCCBR]]'
  relation: compact_clearing_reference
date_created: '2026-05-20'
date_updated: '2026-05-24'
---


Repo (repurchase agreement) is a secured short-term funding transaction: one party sells securities and agrees to repurchase them at a fixed future date and price. The price difference = repo rate x days/360.

## Scope Boundary

[LLM] This node is a broad repo primer and should remain focused on what repo is, why it funds dealers, and how triparty/bilateral structures fit the secured funding system.

[LLM] For the canonical GC/SC, cleared/uncleared segment taxonomy and SEC clearing mandate, use [[Repo_Market_Structure_GC_SC_Cleared_Segments_And_Sec_Mandate]].

[LLM] For a compact rate/clearing table, use [[Repo_Market_Clearing_Segments_FICC_Triparty_GCF_DVP_NCCBR]].

**Three repo market segments:**

1. **Triparty repo** (base layer, $2-4T daily):
   - Custodian (BNY Mellon) intermediates collateral management between dealer (cash borrower) and MMF/GSE (cash lender)
   - Collateral: primarily Treasuries and agency MBS
   - Settlement: same day, end-of-day

2. **GCF repo (General Collateral Finance):**
   - Interdealer repo settled through DTCC FICC
   - Centrally cleared; netting reduces counterparty exposure
   - Rate benchmark: TGCR (Tri-Party General Collateral Rate)

3. **NCCBR (Non-Centrally Cleared Bilateral Repo):**
   - ~2T outstanding; most opaque segment
   - Primary user: hedge funds financing leveraged Treasury positions (basis trade)
   - Lower haircuts than cleared markets -> higher leverage achievable
   - Wider collateral eligibility (equities accepted)
   - Regulatory blind spot until OFR data collection 2023

**Key rates:**
- SOFR: volume-weighted median of overnight Treasury repo rates (triparty + GCF + bilateral)
- BGCR: broad general collateral rate (triparty + GCF)
- TGCR: triparty general collateral rate only

**Repocalypse (Sept 2019):** Overnight repo rates spiked to 10% (vs 2.25% Fed Funds). Causes: corporate tax payments + large Treasury settlement + bank reserve distribution concentration in few G-SIBs who did not redistribute to smaller dealers. Fed resumed repo operations to restore order.

**Function:** Makes Treasuries virtually equivalent to cash for all systemically important participants. Repo is the grease that allows the secured standard to function.


