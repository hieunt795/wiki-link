---
node_id: mp_collateral_channel_001
type: mechanism
title: Monetary Policy Transmission via Collateral and Repo Markets
aliases:
- collateral channel monetary policy
- repo rate monetary transmission
- kênh truyền dẫn qua thị trường repo
- tài sản thế chấp và chính sách tiền tệ
domain:
  primary: monetary_policy
  secondary:
  - financial_markets
  - shadow_banking
tags:
- monetary-transmission
- collateral
- repo
- QE
- shadow-banking
- plumbing
confidence: 3
stability: stable
thesis: 'Repo rates — which reflect collateral availability and quality — guide the
  policy rate more directly than unsecured interbank rates. QE, by removing high-quality
  collateral from circulation and replacing it with reserves, suppresses collateral
  velocity and may impair monetary transmission: large CB footprint in collateral
  markets weakens the market signals that normally guide policy.

  '
source_refs:
- path: 02_sources/books/singh_collateral_plumbing/Singh_Collateral_Financial_Plumbing.md
  pages: Ch.4, Ch.11, Introduction
  weight: primary
- path: 02_sources/books/conks/Conks - Shadow Banking and Cash Markets.md
  pages: TGA, ON RRP, QT sections
  weight: supporting
parent_node: null
related:
- node: '[[Collateral_Velocity_Rehypothecation]]'
  relation: depends_on
- node: '[[Repo_Market_Mechanics_Triparty_Bilateral]]'
  relation: channel_through
- node: '[[Quantitative_Tightening_Qt_Balance_Sheet_Runoff]]'
  relation: reverse_of
- node: '[[Fed_Overnight_Reverse_Repo_On_Rrp]]'
  relation: instrument_in
- node: '[[Monetary Policy Transmission Mechanism — All Channels]]'
  relation: shared_tag:monetary-transmission
- node: '[[Collateral Velocity And Pledged Collateral Market Mechanics]]'
  relation: shared_tag:collateral
- node: '[[Collateral Framework Haircuts Central Bank Credit]]'
  relation: shared_tag:collateral
- node: '[[Collateral Velocity and Rehypothecation]]'
  relation: shared_tag:collateral
- node: '[[Repo Market Mechanics Triparty Bilateral]]'
  relation: shared_tag:collateral
date_created: 2026-05-20
date_updated: 2026-05-20
---


## Core Mechanism

Traditional monetary transmission theory focuses on the unsecured interbank rate (EFFR / policy rate) → bank lending rate → credit → real economy. The collateral channel adds a parallel path:

```
CB Policy Rate (IORB / deposit facility)
       ↓
Repo rate (SOFR / TGCR) — reflects collateral supply, quality, haircuts
       ↓
Shadow banking secured funding costs
       ↓
Non-bank credit creation (hedge funds, MMFs, dealers via repo)
       ↓
Asset prices, credit spreads, leverage
       ↓
Real economy investment and consumption
```

**Key insight:** Repo rates map the financial landscape between banks and non-banks. If they don't move in sync with policy rates, monetary policy transmission is compromised. [RAW-BOOK Singh Ch.11]

## QE's Effect on Collateral Transmission

| QE Phase | Effect on Collateral | Effect on Transmission |
|----------|---------------------|----------------------|
| Large-scale asset purchases | Removes USTs/Bunds from market; replaces with reserves | Suppresses collateral velocity; weakens repo market price signal |
| CB becomes dominant holder | "Footprint" in collateral markets grows | Market signals (repo spreads) weaker; less information for policy |
| Zero-lower bound + QE | Reserves ample, repo rates = IORB | Transmission via interest rate channel intact; collateral channel compressed |
| QT (unwinding) | Returns collateral; reduces reserves | Repo rates re-emerge as signal; collateral velocity rises; secured funding conditions ease |

**Coiled spring effect:** The larger the QE program, the longer the CB will dominate collateral markets and distort the signal. When QT reverses QE, both reserves AND collateral dynamics shift simultaneously — policymakers need to monitor both.

## Collateral as Money-Equivalent

Pledged collateral ($5-10T range, comparable to M2) functions as near-money:
- Repo: cash vs. collateral swap → collateral temporarily "monetized"
- Securities lending: fee-based lending of high-quality collateral (HQLA) to those needing it
- OTC derivatives margining: collateral posted against mark-to-market exposure

When collateral markets seize (2008-9 crash from $10T → $5T), financial intermediation halves — equivalent effect to interbank market freeze. This is why monitoring pledged-collateral volume alongside M2/M3 is important.

## Singh's Key Policy Implications

1. **Repo rate as policy guide**: SOFR/TGCR tracks CB operational stance more faithfully than EFFR (which is dominated by FHLB-bank arbitrage flows). [See Dallas Fed Logan's shift to TGCR as target — corroborated by Conks Money Market]

2. **Collateral shortage at ZLB**: When rates at zero, QE removes collateral AND repo rates compress — double-impairment of the collateral channel. Policy effectiveness diminished beyond what simple money metrics suggest.

3. **Regulatory-collateral tension**: SLR/LCR constraints simultaneously limit dealer balance sheet capacity to intermediate collateral → collateral gets "stuck," velocity drops, spreads widen. [See [[Slr_Lcr_Balance_Sheet_Constraints_Treasury_Market_Dealer]]]

4. **Sovereign-bank nexus**: Sovereigns typically don't post collateral on OTC derivatives → concentrated risk at banks; regulatory reforms incomplete. [Singh Ch.9]

