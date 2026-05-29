---
node_id: fed_overnight_reverse_repo_on_rrp_mec_001
type: mechanism
title: Fed Overnight Reverse Repo ON RRP
aliases:
- ON RRP
- reverse repo facility
- Fed RRP
- co so repo dao nguoc qua dem
domain:
  primary: monetary_policy
tags:
- rrp
- money_market
- fed_facilities
- reserves
- liquidity_sponge
confidence: 4
stability: stable
thesis: 'The ON RRP facility serves as the Federal Reserve''s primary rate-floor mechanism
  and "liquidity shock absorber." It accepts cash from non-bank entities (MMFs, GSEs,
  Primary Dealers) overnight in exchange for Treasury collateral, effectively "neutralizing"
  excess reserves and preventing money market rates from falling below the FOMC''s
  target range.

  '
source_refs:
- path: 02_sources/books/conks/Conks - Fed's Policies and Facilities.md
  pages: The Federal Reserve Endgame Is Not a Collapse, It's Global Domination; The
    Fed's Plumbing Dilemma; The Fed's Reckoning
  weight: primary
parent_node: '[[Fed_Ample_Reserves_Rate_Control_Framework]]'
related:
- node: '[[Fed_Ample_Reserves_Rate_Control_Framework]]'
  relation: component_of_floor_system
- node: '[[QT_Reserve_Drain_Effectiveness_And_Deposit_Funding_Condition]]'
  relation: QT_buffer
- node: '[[TGA_Reserve_Swap_Mechanics_And_Debt_Ceiling_Dynamics]]'
  relation: offsetting_liability_flow
date_created: 2024-05-20
date_updated: 2024-05-20
---

## Overview
The Overnight Reverse Repo (ON RRP) facility was permanently established in 2013 to support rate control in an ample reserves regime. While the Fed pays **IORB** to banks to set a ceiling, it uses the **ON RRP** to offer a risk-free investment to non-bank financial institutions that lack Fed master accounts, thereby setting a hard floor for secured overnight rates [RAW-BOOK].

## The Mechanism: Neutralization
The ON RRP acts as a "liquidity sponge" through a process called **reserve neutralization**:
- **Flow:** When a Money Market Fund (MMF) moves cash from a bank deposit into the ON RRP, the bank's reserves at the Fed are debited, and the Fed's ON RRP liability is credited.
- **Impact:** These reserves are "neutralized"—they still exist as a Fed liability but cannot be used for interbank lending or credit creation as long as they are parked in the facility [RAW-BOOK].
- **Unwinding:** When the ON RRP balance declines (e.g., due to MMFs buying T-bills), neutralized reserves flow back into the banking system, becoming "pure reserves" once again [RAW-BOOK].

## Counterparties and Access
Eligibility is restricted to ensure the facility only absorbs systemic excess cash:
- **Money Market Funds (MMFs):** The dominant users (~90%+ of volume).
- **GSEs:** Fannie Mae, Freddie Mac, and Federal Home Loan Banks (FHLBs).
- **Primary Dealers:** Large broker-dealers authorized to trade directly with the Fed.

Commercial banks are generally excluded, as they are expected to use the higher-yielding IORB [RAW-BOOK] [LLM].

## The "Leaky Floor" and Technical Adjustments
Despite being designed as a hard floor, the ON RRP can be "leaky":
1. **Collateral Shortages:** If demand for U.S. Treasury collateral exceeds supply, private repo rates (e.g., TGCR, BGCR) may trade below the ON RRP rate [RAW-BOOK].
2. **Access Limits:** Entities without ON RRP access may be forced to lend at even lower rates to dealers who have access, creating a sub-floor market.
3. **Technical Adjustments:** The Fed frequently adjusts the ON RRP rate (e.g., 5bps above the bottom of the target range) to ensure it effectively "pulls" market rates into the desired band [RAW-BOOK].

## Role in Quantitative Tightening (QT)
The ON RRP balance is a critical signal for QT duration:
- **Liquidity Buffer:** As long as the ON RRP balance is high, QT removes "neutralized" reserves rather than "pure" bank reserves, acting as a buffer that prevents interbank stress [RAW-BOOK].
- **Zero-Bound Trigger:** Once the ON RRP balance hits zero, QT begins to drain pure bank reserves directly. This marks the transition toward the **LCLoR** (Lowest Comfortable Level of Reserves) and heightens the risk of repo market spikes [RAW-BOOK] [LLM].

[LLM] synthesis: The ON RRP effectively converted the Fed's balance sheet into a two-tiered liability structure (Pure vs. Neutralized), allowing for unprecedented control over liquidity flows during both expansionary and contractionary cycles.
