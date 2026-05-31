---
node_id: fed_global_jaws_frp_fima_001
type: framework
title: Fed Global Jaws FRP FIMA Public Dollar Architecture
aliases:
- Foreign Repo Pool
- FRP
- FIMA repo facility
- global jaws
- public dollar floor
- public dollar ceiling
- foreign official institutions
- FOI repo
- cơ chế đô la toàn cầu Fed
- hồ repo ngoại tệ
domain:
  primary: monetary_policy
  secondary:
  - financial_markets
tags:
- fed
- FRP
- FIMA
- swap-lines
- global-dollar
- foreign-official-institutions
- dollar-floor
- dollar-ceiling
- SOMA
- QE
confidence: 4
stability: stable
thesis: 'The Fed has assembled a four-layer "global jaws" architecture to control
  dollar rates for all market participants, operating as a "range floor system" (or
  "soft floor") rather than a single fixed rate. This architecture consists of: (1)
  private floor = ON RRP (banks/MMFs/GSEs), (2) public floor = Foreign Repo Pool/FRP
  (foreign official institutions), (3) private ceiling = Fed swap lines (allied central
  banks), and (4) public ceiling = FIMA repo facility (all foreign official institutions).
  The system ensures that both private and public dollar rates (unsecured and secured)
  evolve within a narrow range (typically 10-15 basis points), preventing forced asset
  firesales by foreign governments while structurally reinforcing dollar hegemony.

  '
source_refs:
- path: 02_sources/Clipping/ECB AND FED POLICY OPERATIONAL FRAMEWORKS – A PRIMER.md
  pages: 1, 10-12
  weight: primary
- path: 02_sources/books/conks/Conks - Fed's Policies and Facilities.md
  pages: The Fed's Final Frontier; The Fed's Global Put Part I
  weight: supporting
parent_node: null
related:
- node: '[[Fed_Dollar_Swap_Lines_Crisis_Hierarchy_And_Swapper_Of_Last_Resort]]'
  relation: private_global_ceiling_component
- node: '[[Fed_Overnight_Reverse_Repo_On_Rrp]]'
  relation: private_domestic_floor_component
- node: '[[Global_Dollar_System_Eurodollar_Architecture]]'
  relation: global_context
- node: '[[USD_Swap_Lines_Geopolitical_Dollar_Integration_Tool]]'
  relation: geopolitical_dimension_of_swap_lines
date_created: '2026-05-23'
date_updated: '2026-05-24'
---


## Scope Boundary

[LLM] This node is canonical for the four-layer global dollar facility architecture: private floor, public floor, private ceiling, and public ceiling.

[LLM] Detailed Fed swap-line mechanics should remain in [[Fed_Dollar_Swap_Lines_Crisis_Hierarchy_And_Swapper_Of_Last_Resort]].

[LLM] This node should only summarize swap lines as one component of the global dollar-rate corridor.

## The Complete "Global Jaws" Architecture

The Fed controls dollar rates for all market participants through four interlocking facilities:

```
╔══════════════════════════════════════════════════════════╗
║         GLOBAL DOLLAR RATES ARCHITECTURE                 ║
╠══════════════════════════════════════════════════════════╣
║  CEILING (borrow dollars)                                ║
║   Private: Swap lines (allied CBs) at OIS+25bps         ║
║   Public:  FIMA repo (all FOIs) — Treasuries for $      ║
╠══════════════════════════════════════════════════════════╣
║  FLOOR (invest dollars)                                  ║
║   Private: ON RRP (banks, MMFs, GSEs) at FOMC rate      ║
║   Public:  FRP (foreign official institutions)           ║
╚══════════════════════════════════════════════════════════╝
```

[RAW-CLIP Conks Final Frontier]

## Foreign Repo Pool (FRP) — The Public Dollar Floor

### What it is
The FRP (Foreign Repo Pool) was created in the 1970s as an investment facility exclusively for **Foreign Official Institutions (FOIs)**: foreign governments' treasuries, central banks, and international organizations (IMF, World Bank, etc.).

### How it works
```
FOI (e.g. Bank of Japan) holds excess dollars in its
  master account at the Fed (NY Fed)
→ Invests overnight via FRP: "sells" Treasuries from
  Fed's SOMA portfolio, agrees to buy back next day
→ Earns FRPR (Foreign Repo Pool Rate) on the loan
→ Next day: Treasuries returned, dollars returned with interest

Result: FOI earns risk-free dollar yield; Fed absorbs excess FOI cash
```

**FRPR** (Foreign Repo Pool Rate) = public dollar floor for FOIs (analogous to ON RRP rate for private entities). Because the Fed is deemed the safest dollar counterparty, the FRPR sets the minimum yield any FOI would accept.

**Key usage surge:** In late 2015, the Fed started paying higher FRP rates → attracted large inflows from foreign CBs parking their FX reserves. FRP balances rose again after COVID-19 (2020) as FOIs sought to invest excess dollars. [RAW-CLIP Conks Final Frontier]

## FIMA Repo Facility — The Public Dollar Ceiling

### Creation
Created March 31, 2020, during the COVID dollar shortage. COVID triggered a "dash for cash" — even FOIs began selling Treasuries to raise dollars, threatening a firesale that would collapse Treasury market prices.

### How it works
```
FOI (e.g. People's Bank of China) needs dollars urgently
→ Posts Treasuries from its own portfolio at the NY Fed
→ Receives dollar reserves in exchange (as a loan)
→ Repays at maturity with interest
→ Gets Treasuries back

Result: FOI avoids fireselling Treasuries; Fed provides emergency $
```

**Key distinction from swap lines:**
| Feature | Swap Lines | FIMA |
|---------|-----------|------|
| Access | Allied CBs only (ECB, BoJ, BoE, etc.) | ANY foreign CB/government entity |
| Collateral | None (CB credit standing) | Must post U.S. Treasuries |
| Motivation | Partner coordination | Prevents U.S. asset firesale |
| Geopolitical | Selective (US allies) | Universal (incl. China) |

**China as likely largest FIMA user (March 2020):** Rather than dumping Treasuries (which would signal dollar exit), China used FIMA to access dollars, demonstrating the dollar system's resilience even among rivals. [RAW-CLIP Conks Final Frontier]

## Why FIMA Reinforces Dollar Hegemony

The FIMA facility creates a structural trap for dollar alternatives:
1. Any nation holding U.S. Treasuries can access dollars in a crisis via FIMA → no need to dump Treasuries
2. Nations that don't hold Treasuries can't access FIMA → incentive to accumulate Treasuries
3. "Escaping Uncle Sam requires ditching the Greenback. But a modern-day exodus will result in most of its allies and rivals demanding more dollars." [RAW-CLIP Conks Final Frontier]

## Cross-Border Currency Repo (CBCR) — How Swap Lines Distribute Dollars

When swap lines are activated, the mechanism is:
```
Step 1: Fed and foreign CB engage in "central bank reserve swap"
  → Both expand balance sheets
  → Fed credits foreign CB's reserve account
  → Foreign CB credits Fed's reserve account
  
Step 2: Foreign CB instructs Fed via SWIFT
  → Transfers new reserves to NY branches of domestic banks
  → Banks post sovereign bonds as collateral to foreign CB
  
Step 3: Banks receive reserves at NY branch
  → Can now make dollar loans to offshore customers
  → Back dollar deposits at offshore branches with NY reserves (LCR compliance)
```

This "cross-border currency repo" (CBCR) is how the Fed's swap lines bypass Eurodollar channel constraints (no direct Fed access) while maintaining Basel III compliance. [RAW-CLIP Conks Global Put I]

## Dollar Rates Hierarchy (From Cheapest to Most Expensive)

The cost of accessing dollars rises as you move up the hierarchy:

```
Secured repo (onshore)       → cheapest; direct Fed reserve access
Unsecured (CP, Eurodollars)  → slightly higher; credit risk premium
FX swaps                     → highest private cost; currency risk + balance sheet
FHLB-brokered Fed Funds      → G-SIBs' private LoLR
Fed swap lines (OIS+25bps)   → public dollar backstop for allied CBs
```

Large U.S. G-SIBs are the private "dealers of last resort" before swap lines activate. FHLBs act as government-sponsored bridge lenders at the top of the private hierarchy. [RAW-CLIP Conks Global Put I]
