---
node_id: repo_clearing_segments_ficc_001
type: mechanism
title: Repo Market Clearing Segments FICC Triparty GCF DVP NCCBR
aliases:
- repo clearing structure
- FICC repo segments
- triparty repo market
- GCF repo
- DVP repo
- NCCBR
- cấu trúc thị trường repo thanh toán bù trừ
domain:
  primary: financial_markets
  secondary: monetary_policy
tags:
- repo
- ficc
- triparty
- gcf
- dvp
- nccbr
- clearing
- tgcr
- sofr
confidence: 1
stability: stable
thesis: The U.S. repo market is segmented into four clearing structures — triparty
  (uncleared GC via BNY Mellon, MMFs as cash lenders), GCF Repo (cleared interdealer
  GC via FICC), DVP Repo (cleared specific-collateral interdealer via FICC), and NCCBR
  (uncleared specific-collateral bilateral, dealers + hedge funds) — each producing
  a distinct overnight rate (TPR=TGCR, GCF index, DVP, NCCBR) used by the Fed to calibrate
  its rate corridor.
source_refs:
- path: 02_sources/books/conks/Conks - Plumping note (Money market.md
  pages: batch 21 (chars ~173114-182157)
  weight: primary
parent_node: null
related:
- node: '[[Standing Repo Facility SRF Fed Backstop]]'
  relation: context
- node: '[[Fed Policy Rate Shift EFFR To Secured Rate TGCR]]'
  relation: extends
- node: '[[SRF Structural Defects Morning Repo Fortification True Ceiling]]'
  relation: related_mechanism
- node: '[[Repo_Market_Structure_GC_SC_Cleared_Segments_And_Sec_Mandate]]'
  relation: canonical_detailed_taxonomy
date_created: '2026-05-23'
date_updated: '2026-05-24'
---

## Scope Boundary

[LLM] This node is a compact clearing-and-rate reference for the four repo segments.

[LLM] It overlaps by design with [[Repo_Market_Structure_GC_SC_Cleared_Segments_And_Sec_Mandate]], which should be treated as the canonical detailed taxonomy, especially for GC/SC purpose, FICC access, SOFR effects, and SEC mandate implications.

## Repo Market Clearing Taxonomy

The U.S. overnight repo market has four distinct segments, differentiated by clearing method and collateral specificity:

| Segment | Collateral | Clearing | Cash Lenders | Overnight Rate |
|---------|------------|----------|--------------|----------------|
| **Triparty** | GC (any eligible) | Uncleared (BNY Mellon custodian) | MMFs, banks, GSEs | o/n TPR = TGCR |
| **GCF Repo** | GC (any eligible) | Cleared (FICC) | Dealers only | o/n GCF index |
| **DVP Repo** | SC (named CUSIP) | Cleared (FICC) | Dealers + clients | o/n DVP |
| **NCCBR** | SC (named CUSIP) | Uncleared bilateral | Dealers + hedge funds | o/n NCCBR |

[RAW-CLIP]

## FICC Membership and Access Restriction

FICC (Fixed Income Clearing Corporation) membership is restricted to large banks and primary dealers — not open to all market participants. This creates two tiers:
- **Cleared** (GCF, DVP): FICC members only; central counterparty backstop; netting benefits
- **Uncleared** (Triparty, NCCBR): Broader access including MMFs and hedge funds; bilateral credit exposure; no FICC netting [RAW-CLIP]

## Key Overnight Rates

**o/n TPR (Tri-Party Repo rate) = TGCR:**
The broadest GC rate; published by the NY Fed; equivalent to TGCR; one of three SOFR component rates. [RAW-CLIP]

**o/n GCF (General Collateral Finance Repo):**
Cleared interdealer GC rate; narrower FICC-member-only population; slightly different from TGCR due to membership selection effect. [RAW-CLIP]

**o/n DVP:**
Cleared specific-collateral interdealer rate; reflects scarcity premium for on-the-run or special collateral. [RAW-CLIP]

**o/n NCCBR (Non-Centrally Cleared Bilateral Repo):**
Bilateral uncleared SC rate between dealers and hedge funds; includes basis trade leverage demand; typically the widest of the four rates during stress. [RAW-CLIP]

## Evolution: Sponsored Repo and Agent Clearing

Post-2020 expansion of **Sponsored Repo** and **Agent Clearing Service** began extending FICC clearing access to buy-side clients (hedge funds, asset managers) — gradually moving NCCBR volume toward central clearing and reducing bilateral exposure concentration. [LLM]
