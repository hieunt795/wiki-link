---
node_id: us_shadow_banking_post_gfc_market_based_finance_structure_001
type: mechanism
title: US Shadow Banking Post-GFC Market Based Finance Structure
aliases:
- Shadow Banking Post-GFC
- Market-Based Finance
- PTF Treasury Market Making
- Ngân hàng bóng tối Mỹ
- Tài chính thị trường
domain:
  primary: monetary_policy
tags:
- shadow_banking
- ptf
- securitization
- abs
- clo
- gfc
- treasury_market
- basel
confidence: 3
stability: evolving
thesis: Post-2008 US shadow banking transformed from a complex CDO/synthetic ABS machine
  into a repo-centric, collateral-based market-based finance system, where securitization
  (ABS, CLOs) survived but the toxic CDO-cubed structures collapsed; simultaneously,
  Principal Trading Firms (PTFs) replaced G-SIBs as the primary Treasury market makers
  due to Basel/SLR regulatory constraints on bank balance sheets.
source_refs:
- path: 02_sources/books/conks/Conks - Shadow Banking and Cash Markets.md
  pages: Full document
  weight: primary
parent_node: null
related:
- node: '[[Basel Driven Credit Migration To Private Markets]]'
  relation: shared_tag:shadow_banking
- node: '[[Collateral Velocity And Pledged Collateral Market Mechanics]]'
  relation: shared_tag:shadow_banking
- node: '[[Shadow Banking Market Based Finance]]'
  relation: shared_tag:securitization
- node: '[[Private Credit — SRT, NAV Loans, and Bank-PC Interconnection]]'
  relation: shared_tag:clo
- node: '[[Basel III Capital And Liquidity Constraint Mechanics]]'
  relation: shared_tag:basel
date_created: '2026-05-22'
date_updated: '2026-05-22'
---


## Pre-GFC Structure (1970s-2008)
Shadow banking originated in **government-sponsored enterprise** innovation, not private sector:
- **GSEs (Fannie/Freddie):** Founded the "originate-to-distribute" securitization model; provided credit risk transfer via implicit guarantees
- **FHLB:** "Loan warehousing" — extended credit to MBS securitizers
- **Wall Street innovation:** CDOs and CDS allowed banks to game Basel I capital requirements by pooling mortgages into "diversified" tranches with lower risk weights [RAW-CLIP]

## Post-GFC Transformation
After Lehman collapse, the shadow banking ecosystem pruned:

| Survived | Eliminated |
|---------|-----------|
| Repos (core collateral mechanism) | Synthetic CDOs, CDO-cubeds |
| ABS (auto, student, credit card) | Subprime MBS structures |
| CLOs (leveraged loan securitization) | CDS on CDS (synthetic on synthetic) |
| Prime money market funds (until 2016) | Structured investment vehicles (SIVs) |

Basel III (capital ratios) + Dodd-Frank (proprietary trading restrictions) constrained G-SIBs but did NOT constrain **Principal Trading Firms (PTFs)** [RAW-CLIP].

## Rise of PTFs in Treasury Markets
PTFs (e.g., Citadel Securities, Jane Street, Virtu) use HFT algorithms on electronic platforms:
- **Not constrained by SLR or G-SIB capital rules** → can hold more Treasuries per unit of capital
- Captured primary dealer market-making share in on-the-run Treasuries
- JPMorgan exited triparty repo in 2016 explicitly due to regulatory penalties [RAW-CLIP]

## Treasury Market Structure (2023+)
Three segments:
1. **Interdealer segment:** PTF-dominated, electronic, HFT, ~50-60% of volume
2. **Dealer-to-dealer:** ~10% of volume, large trades off-screen to avoid signaling
3. **Dealer-to-client:** G-SIBs + PTFs make markets for central banks, hedge funds, pensions

The secondary market remains fragmented and opaque vs. equities. Reform agenda: all-to-all clearing (CCP mandate) for Treasury cash trades [RAW-CLIP].

## The SLR Constraint
Basel III's **Supplementary Leverage Ratio** requires 3-5% capital against ALL assets (including Treasuries/reserves). This makes holding Treasuries for market-making unprofitable for large banks during normal conditions. SLR relief (as in COVID, March-September 2020) temporarily reverses this — banks gorge on Treasuries during exemption periods, then dump them when relief expires [RAW-CLIP].


