---
node_id: central_bank_pledgening_runnable_liabilities_001
type: concept
title: Central Bank Pledgening Runnable Liabilities and Discount Window Reform
aliases:
- Central Bank Pledgening
- runnable liabilities
- runnable ratio
- prepositioning collateral
- Discount Window destigmatization
- G30 LoLR reform
- runnables
- ký quỹ trước tại cửa sổ chiết khấu
domain:
  primary: monetary_policy
  secondary:
  - financial_markets
tags:
- discount-window
- prepositioning
- runnable-liabilities
- bank-run-prevention
- G30
- FDIC
- LoLR
- SVB
- secured-standard
confidence: 3
stability: evolving
thesis: 'Post-SVB, monetary leaders are reforming LoLR (lender of last resort) access
  via "prepositioning" — requiring banks to pre-pledge enough assets at the Discount
  Window to cover a specified share (~40%) of "runnable" liabilities (uninsured deposits
  >$250k), destigmatizing emergency borrowing while creating structural demand for
  Treasury and other high-quality collateral. This reinforces the "secured standard"
  where sovereign liabilities are structurally embedded in the banking system.

  '
source_refs:
- path: 02_sources/books/conks/Conks - Fed's Policies and Facilities.md
  pages: The Central Bank Pledgening; The Fed's New Rescue Mechanism
  weight: primary
parent_node: null
related:
- node: '[[BTFP_SVB_Crisis_And_Fed_Emergency_Lending_Evolution]]'
  relation: structural_predecessor
- node: '[[Collateral_Framework_Haircuts_Central_Bank_Credit]]'
  relation: same_domain_collateral_mechanics
- node: '[[LCR_NSFR_Long_Term_Lending_Penalty]]'
  relation: parallel_structural_demand_for_HQLA
- node: '[[Basel_III_Endgame_Capital_Liquidity_Credit_Migration]]'
  relation: complementary_HQLA_demand_driver
date_created: '2026-05-23'
date_updated: '2026-05-23'
---


## What Are "Runnables"?

"Runnable liabilities" (Fed-speak: "runnables") = liabilities that can be withdrawn quickly, creating a bank run:
- **Primary:** Uninsured deposits > $250K FDIC limit → large depositors withdraw in minutes (SVB: via mobile app + social media in hours)
- **Secondary:** Wholesale funding (repo, CP) — can also run, but with slightly more friction

SVB had ~$150B+ in uninsured deposits concentrated in a narrow VC community → single WhatsApp message triggered coordinated flight. [RAW-CLIP Conks Pledgening]

## The Prepositioning ("Pledgening") Proposal

**G30 Working Group (Jan 2024 report)** proposed:
1. Banks must "preposition" collateral at the Fed's Discount Window BEFORE a crisis
2. The pledged pool covers a specified "runnable ratio" of their runnable liabilities
3. No need to borrow immediately — just being pledged assures regulators and depositors

```
Bank balance sheet during normal times:
  Securities portfolio → pledged to Fed DW → "prepositioned"
  
In stress:
  Bank can convert pledged securities to reserves instantly (no operational delay)
  → No firesale needed → bank run preemptively countered
```

**Key insight:** Simply announcing that the bank has pre-positioned collateral reduces depositor panic → the pledge deters the run it aims to handle. Self-fulfilling stability mechanism. [RAW-CLIP]

## Runnable Ratio

Initial proposal: **~40%** of runnables need to be covered by reserves + pledged collateral. Some advocates call for 100% coverage (Full Reserve lite). 

**Trade-off:**
- Higher ratio → greater bank run resilience
- But: securities tied up as collateral can't be used for market making or lending
- If banks are simultaneously required to hold HQLA for LCR AND preposition for DW → double constraint on balance sheet capacity
- May require Basel III adjustment to avoid compressing market-making capacity [RAW-CLIP Conks Pledgening]

## Structural Demand for Sovereign Assets

The Pledgening reinforces the "secured standard" doctrine:
```
Regulations creating demand for sovereign liabilities:
  LCR → HQLA buffer (Treasuries/reserves)
  NSFR → stable funding (requires liabilities-side discipline)
  SLR → Tier 1 capital constraint
  Runnable Ratio → pre-pledged Treasuries at DW
  Basel III Output Floor → more capital → more Treasuries as HQLA

Net effect: banks structurally forced to hold/demand US sovereign paper
         → Fed balance sheet grows (not normalizes) over time
```

[LLM synthesis from RAW-CLIP — "Excess is the new normal, and the secured standard demands it."]

## Destigmatization Strategy (G30 Proposals)

Beyond prepositioning, G30 also proposed:
1. Normalize DW usage by having regulators publicly borrow from the Window periodically
2. Remove banks' ability to net unrealized losses vs. capital in stress scenarios
3. Expand FDIC deposit insurance limit (or make unlimited in systemic events)
4. Consider 24/7 Discount Window access (social media bank runs happen at 2am)

These represent a fundamental shift: the DW moves from "emergency last resort" to "routine liquidity management tool." [RAW-CLIP]

