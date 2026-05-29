---
node_id: btfp_svb_crisis_emergency_lending_001
type: mechanism
title: BTFP SVB Crisis and Fed Emergency Lending Evolution
aliases:
- BTFP
- Bank Term Funding Program
- SVB bank run
- Discount Window Primary Credit Facility
- PCF
- operational readiness
- phương tiện cho vay khẩn cấp Fed
- chương trình tài trợ vốn kỳ hạn ngân hàng
domain:
  primary: monetary_policy
  secondary:
  - financial_markets
tags:
- BTFP
- SVB
- discount-window
- PCF
- lender-of-last-resort
- bank-run
- emergency-lending
- LoLR
- SRF
confidence: 3
stability: evolving
thesis: 'SVB''s March 2023 collapse — driven by uninsured deposit flight amplified
  by social media — revealed that the Discount Window''s Primary Credit Facility was
  too stigmatized for bank use, prompting the Fed to create the BTFP (loans at par
  value, 1-year term). The BTFP later became a risk-free arbitrage (BTFP rate < IORB
  → 50bps spread) before expiring March 2024, prompting a broader reform agenda including
  Discount Window "prepositioning" and destigmatization.

  '
source_refs:
- path: 02_sources/books/conks/Conks - Fed's Policies and Facilities.md
  pages: The Fed's New Rescue Mechanism; The Central Bank Pledgening
  weight: primary
parent_node: null
related:
- node: '[[Standing_Repo_Facility_SRF_Fed_Backstop]]'
  relation: sibling_emergency_facility
- node: '[[Central_Bank_Pledgening_Runnable_Liabilities_And_Discount_Window_Reform]]'
  relation: reform_outcome_of_svb_lesson
- node: '[[IORB_Interest_on_Reserve_Balances]]'
  relation: arbitrage_reference_rate
- node: '[[Fed_Ample_Reserves_Rate_Control_Framework]]'
  relation: framework_context
date_created: '2026-05-23'
date_updated: '2026-05-23'
---


## SVB Collapse Sequence (March 2023)

SVB held massive uninsured deposits from VC-concentrated tech sector. Fed rate hikes → unrealized losses on long-duration securities portfolio → March 8 emergency restructuring announcement → coordinated VC investor exodus → $100B in deposits set to flee → March 10 FDIC closure.

Key structural weakness: SVB wasn't "operationally ready" for Discount Window access — hadn't pre-pledged collateral. When a bank isn't plugged in, emergency funding takes days, not hours. By then, deposit flight had already made it insolvent. [RAW-CLIP Conks BTFP]

## Discount Window (DW) — Primary Credit Facility (PCF) Mechanics

```
Discount Window
  └─ Primary Credit Facility (PCF) — "lender of last resort" for solvent banks
  └─ Secondary Credit Facility — for banks with capital deficiencies
  └─ SRF (Standing Repo Facility) — "dealer of last resort" for repo market
```

**PCF mechanics:**
- Bank pledges eligible securities → Fed credits reserves equal to (market value – haircut)
- Cost: discount rate = upper bound of FOMC target range (penalty above EFFR)
- Maximum term: 90 days
- Problem: **stigma** — banks fear being seen as troubled if they tap the PCF → prefer to firesale assets rather than borrow from Fed

## BTFP vs PCF — Key Differences

| Feature | PCF (Discount Window) | BTFP (2023) |
|---------|----------------------|-------------|
| Loan basis | Market value – haircut | **Par value** (no haircut) |
| Max term | 90 days | **1 year** |
| Eligible collateral | Any Fed-approved security (any purchase date) | Securities on balance sheet before March 13, 2023 |
| Cost | Discount rate (upper bound) | 1-year OIS + 0.10% |
| Credit protection | None | $25B from Treasury |
| Stigma | High | Low (presented as system-wide program) |

**BTFP innovation:** By lending at par value, Fed effectively provided capital relief on unrealized duration losses. Banks with underwater HTM bond portfolios could borrow face value → no forced loss realization. [RAW-CLIP]

## BTFP Arbitrage Abuse (Late 2023)

When multiple rate cuts were priced in, 1-year OIS rate fell → BTFP borrowing cost fell below IORB:

```
Banks: Borrow from BTFP at (1yr OIS + 0.10%) ≈ 4.60%
       Deposit at Fed to earn IORB = 5.10%
       Spread ≈ 50bps risk-free → BTFP volumes rose to ~$170B

Fix (Jan 25 2024): Fed raised BTFP minimum rate to equal IORB → spread = 0
Expiry: March 11, 2024 — no new BTFP loans accepted
```

## Fed vs Repo Market Emergency Facilities

```
Banking system stress:
  Solvent but illiquid banks → Discount Window PCF (reserves against pledged securities)
  
Repo market stress:
  Dealers without DW access → SRF (Standing Repo Facility) — exchange Treasuries/agency MBS for cash at SRF rate
  
System-wide stress (2008, 2020):
  → Ad hoc facilities (TALF, CPFF, MMLF, BTFP) for specific market segments
  → Global dollar shortage → Fed swap lines
```

[RAW-CLIP Conks New Rescue Mechanism]

## Key Lessons for Monetary Plumbing

1. **Stigma beats economics:** Banks prefer to firesale assets at large losses rather than tap the PCF if it might signal distress to counterparties
2. **Operational readiness matters:** Pre-pledging collateral at DW takes time; banks that aren't plugged in can't get emergency funds fast enough
3. **Par-value lending bails out duration risk:** BTFP's design effectively guaranteed the bank sector's HTM bond portfolio — a structural guarantee that wasn't publicly debated

