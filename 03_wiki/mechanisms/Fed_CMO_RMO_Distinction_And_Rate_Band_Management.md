---
node_id: fed_cmo_rmo_distinction_001
type: mechanism
title: Fed CMO RMO Distinction And Rate Band Management
aliases:
- CMO ceiling management operations
- RMO reserve management operations difference
- Fed rate band operations
- Phân biệt CMO và RMO của Fed
domain:
  primary: monetary_policy
tags:
- fed
- cmo
- rmo
- iorb
- srfr
- money_market
- reserves
- rate_corridor
confidence: 1
stability: evolving
thesis: The Fed uses two distinct reserve injection tools to maintain the federal
  funds rate within its target band — CMOs (Ceiling Management Operations) are emergency
  interventions that push market rates away from the SRF ceiling, while RMOs (Reserve
  Management Operations) are routine outright bill purchases that maintain ample reserves
  over time — with CMOs typically preceding RMOs when rates breach the upper limit
  of the target band.
source_refs:
- path: 02_sources/books/conks/Conks - Plumping note (Money market.md
  pages: batch 15 (chars ~121242-130089)
  weight: primary
parent_node: null
related:
- node: '[[Fed RMO Reserve Management Operations Post QT Mechanics]]'
  relation: distinguishes
- node: '[[SRF Structural Defects Morning Repo Fortification And True Ceiling]]'
  relation: complements
date_created: '2026-05-23'
date_updated: '2026-05-23'
---

## Distinction

| | CMO (Ceiling Management Operations) | RMO (Reserve Management Operations) |
|--|--------------------------------------|--------------------------------------|
| **Purpose** | Emergency: push rates back within band when breaching SRF ceiling | Routine: maintain ample reserves over time |
| **Trigger** | Rate spike above SRF ceiling (SRFR + ~25bps) | Structural reserve drain exceeds buffer |
| **Instrument** | Targeted repo operations or short-term bill purchases | Outright bill purchases (POMO bills) |
| **Timing** | Reactive | Proactive/scheduled |

In practice: when repo rates breach SRFR on month-ends, CMOs act as an immediate patch; RMOs are the structural solution announced on a schedule (Fed first announced RMO schedule December 11, 2025). [RAW-CLIP]

## Sequencing

CMOs typically precede RMOs in a tightening-to-normalization cycle:
1. QT → reserve drain → rates drift above SRFR on stress dates
2. Fed deploys CMOs to cap rate spikes
3. Fed announces RMO schedule to begin routine reserve injections
4. Rate band pressure dissipates

[RAW-CLIP — Conks Plumbing Notes: Swifter Injections, A Faulty Relief Valve]

The CMO-to-RMO transition marks the shift from reactive rate management to proactive reserve supply restoration. [LLM]
