---
node_id: mechanism_treasury_dealer_capacity_001
type: mechanism
title: Treasury Market Dealer Intermediation Capacity
aliases:
- dealer intermediation capacity
- Treasury market dealer constraints
- primary dealer balance sheet
- dealer balance sheet capacity
- khả năng trung gian của dealer thị trường Treasury
domain:
  primary: financial_markets
  secondary:
  - monetary_policy
  - fiscal_policy
tags:
- treasury-market
- dealer
- balance-sheet
- liquidity
- slr
- market-structure
confidence: 2
stability: evolving
thesis: 'Primary dealers intermediate between Treasury issuance and end investors
  by warehousing Treasury inventory on their balance sheets. Their capacity to do
  so is directly constrained by regulatory capital ratios — SLR, LCR, and G-SIB surcharge
  — which treat Treasury holdings as consuming balance sheet. As Treasury supply has
  grown from ~$14tn (2019) toward ~$30tn (2025), dealer intermediation capacity has
  grown proportionally less, creating a structural capacity gap that widens during
  stress events (March 2020, September 2019, SVB March 2023).

  '
source_refs:
- path: 02_sources/books/duffie_bpea_payments_2026/Duffie_BPEA_Payments_Liquidity_2026.md
  weight: primary
- path: 02_sources/books/conks/Conks - Plumping note (Money market.md
  weight: supporting
- path: 02_sources/deep-research/Deep Dive_ Private Credit.md
  weight: supporting
parent_node: null
related:
- node: '[[Slr_Lcr_Balance_Sheet_Constraints_Treasury_Market_Dealer]]'
  relation: constrained_by
- node: '[[Swap_Spreads_Balance_Sheet_Plumbing_Frictions]]'
  relation: drives
- node: '[[Repo_Market_Mechanics_Triparty_Bilateral]]'
  relation: uses
- node: '[[Fed_Overnight_Reverse_Repo_On_Rrp]]'
  relation: substituted_by
- node: '[[Standing_Repo_Facility_SRF_Fed_Backstop]]'
  relation: backstopped_by
- node: '[[Collateral_Velocity_Rehypothecation]]'
  relation: related_to
- node: '[[BIS_Bank_for_International_Settlements]]'
  relation: monitored_by
steps:
- 'Step 1: Treasury issues new bonds at auction; primary dealers obligated to bid'
- 'Step 2: Dealers warehouse unsold inventory on balance sheet (funded via repo)'
- 'Step 3: Dealers intermediate: buy from Treasury, sell to end investors over days/weeks'
- 'Step 4: SLR/LCR constraints limit warehouse capacity → larger spread required to
  clear inventory'
- 'Step 5: Under stress, dealer willingness to warehouse collapses → bid-ask widens,
  yields spike'
- 'Step 6: Fed SRF/ON RRP or Treasury buyback programs provide relief valve'
transmission_lags: immediate
empirical_evidence: strong
date_created: 2026-05-23
date_updated: 2026-05-23
last_reviewed: 2026-05-23
---

## Overview

The US Treasury market is the world's largest and most liquid government bond market (~$27tn outstanding as of 2025). Its functioning depends critically on **primary dealer intermediation**: the 24 FRBNY-designated primary dealers are obligated to participate in Treasury auctions and provide two-way markets in Treasuries. They perform this function by warehousing Treasury inventory — buying bonds at auction or in the secondary market and selling to end investors (insurance companies, pension funds, foreign CBs, mutual funds) over hours to days.

This warehousing function requires balance sheet capacity. [RAW-BOOK Duffie_BPEA_Payments_Liquidity_2026]

## Regulatory Constraints on Capacity

Three overlapping constraints bind dealer Treasury inventory capacity:

**1. Supplementary Leverage Ratio (SLR):** Post-Basel III, the SLR requires banks to hold Tier 1 capital against all on-balance-sheet exposures regardless of risk weight — including Treasuries (nominally zero risk weight under RWA frameworks). This creates a direct capital cost for Treasury warehousing absent a specific SLR exemption.

The April 2020 SLR relief (excluding Treasuries and reserves) temporarily expanded capacity; its expiration March 2021 contributed to the 2021 Treasury market strains. SLR reform (permanent exclusion or recalibration) remains contested. [RAW-CLIP Conks Money Market Update]

**2. LCR HQLA requirement:** LCR requires banks to hold HQLA (Treasuries qualify). But the LCR also constrains the short-term funding of Treasury warehousing — repo borrowing to fund inventory increases outflows in the LCR denominator. See [[Slr_Lcr_Balance_Sheet_Constraints_Treasury_Market_Dealer]].

**3. G-SIB surcharge:** The largest dealers face supplemental capital charges based on size and systemic importance. Any increase in Treasury inventory raises the G-SIB score, potentially triggering a higher surcharge tier, creating non-linear capacity constraints near tier boundaries. [LLM]

## The Structural Capacity Gap

Treasury supply growth has outpaced dealer balance sheet capacity growth. Supply/capacity mismatch:
- 2007: Treasury outstanding ~$5tn; dealer repo book large relative to supply
- 2019: Treasury ~$17tn; September repo spike signalled capacity strain
- 2020: March COVID Treasury market dysfunction → Fed forced to buy $1.6tn in two weeks
- 2025: Treasury ~$28tn; capacity concerns persist despite SRF backstop

Duffie (2026 BPEA paper) frames this as a structural intermediation gap: private balance sheet has not scaled proportionally with public supply. He proposes: (1) all-to-all central clearing mandates to reduce bilateral balance sheet usage; (2) permanent SLR exclusion for Treasuries; (3) expanded SRF eligibility. [RAW-BOOK Duffie_BPEA_Payments_Liquidity_2026]

## Stress Dynamics

During stress (risk-off events, month-end, auction failures), dealers face simultaneous pressures:
- Customer selling pressure (need to absorb) ↑
- Funding capacity (repo market) ↓ (counterparties withdraw)
- Mark-to-market losses on inventory ↑

This produces the **illiquidity paradox**: Treasuries are the world's safest asset but can become temporarily illiquid when the dealer system cannot intermediate. The March 2020 episode — yields spiking despite flight-to-safety demand — is the canonical example.

## SRF as Relief Valve

The Standing Repo Facility (2021) addresses the acute stress scenario: primary dealers and depository institutions can repo Treasuries to the Fed at the SRF rate (currently IORB + 0bps), providing an intraday backstop. But the SRF does not address the structural supply/capacity gap — it only provides emergency liquidity, not permanent intermediation capacity. See [[Standing_Repo_Facility_SRF_Fed_Backstop]].
