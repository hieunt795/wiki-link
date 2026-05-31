---
node_id: bcbs_intraday_liquidity_management_p8_001
type: regulation
title: BCBS Intraday Liquidity Management — Principle 8 (2008)
aliases:
- BCBS intraday liquidity Principle 8
- intraday liquidity risk management 2008
- payment and settlement intraday liquidity
- intraday funding risk BCBS
- quản lý thanh khoản trong ngày BCBS
- nguyên tắc 8 thanh khoản trong ngày
domain:
  primary: banking_regulation
  secondary: payment_systems
tags:
- intraday_liquidity
- payment_systems
- settlement_risk
- liquidity_risk
- bcbs
- real_time_gross_settlement
- correspondent_banking
- collateral_management
- bcbs144
confidence: 4
stability: stable
thesis: 'BCBS Principle 8 (2008) requires active intraday liquidity management across
  all payment and settlement systems, under both normal and stressed conditions. The
  principle addresses a critical systemic risk: a bank''s failure to settle payments
  when expected can cascade through interconnected systems, triggering gridlock, contagion,
  and overnight funding pressures across many institutions. Six operational elements
  are required: (1) measurement and forecasting of gross inflows/outflows; (2) real-time
  monitoring of intraday positions; (3) arrangements to acquire sufficient intraday
  funding; (4) collateral management for intraday pledging; (5) timing control over
  outflows; (6) preparedness for unexpected disruptions.

  '
source_refs:
- path: 02_sources/regulator/bcbs/bcbs144 - Principles for Sound Liquidity Risk Management and Supervision.md
  pages: 'para 77–87 (Principle 8 full: systemic rationale, objectives, six operational
    elements), para 77 (systemic contagion risk), para 78 (objectives), para 79 (challenges),
    para 80–85 (six elements), para 86–87 (scope, correspondents)'
  weight: primary
parent_node: '[[Bcbs_Sound_Liquidity_Risk_Management_17_Principles_2008]]'
related:
- node: '[[Bcbs_Sound_Liquidity_Risk_Management_17_Principles_2008]]'
  relation: parent_framework
- node: '[[Bcbs_Liquidity_Contingency_Funding_Plan_Principle_11]]'
  relation: cfp_intraday_coverage
- node: '[[Bcbs_Hqla_Liquidity_Cushion_Principle_12]]'
  relation: cushion_includes_intraday_needs
- node: '[[Reserve_Floor_Payment_System_Demand]]'
  relation: payment_system_liquidity_demand
date_created: '2026-05-25'
date_updated: '2026-05-25'
---

## Why Intraday Matters Systemically

```
"Given the interdependencies that exist among systems, a bank's failure to meet
certain critical payments could lead to liquidity dislocations that cascade quickly
across many systems and institutions."
[RAW-BOOK bcbs144 para 77]

CONTAGION MECHANISM:
  Bank A fails to settle payment ON TIME
    → Counterparties interpret as financial weakness signal
    → Counterparties withhold/delay payments back to Bank A (credit concern)
    → Bank A receives fewer inflows → deeper intraday shortfall → more payment delays
    → Counterparties C, D, E also short of expected inflows → cascades through system
    → Overnight funding needs increase across many banks
    → Potential money market disruption

GROSS VS NET SCALE:
  "A bank's daily gross cash outflows can often far exceed its net overnight balances"
  → Even a bank with adequate overnight reserves can face intraday shortfall
  → The timing mismatch of gross flows is the risk, not just the net position
  [RAW-BOOK bcbs144 para 79]
```

---

## Two Management Objectives

```
OBJECTIVE A: Identify and prioritise TIME-SPECIFIC and critical obligations
  → Meet these when expected — not just by end of day
  → Examples of critical:
    - CLS Bank payment deadlines (FX settlement)
    - Margin payments with intraday deadlines
    - Delivery of money market transactions
    - Payments critical to bank's business or reputation
  [RAW-BOOK bcbs144 para 78, footnote 10]

OBJECTIVE B: Settle other obligations as soon as possible
  → Not delay non-critical payments unnecessarily (creates contagion)
  → Balance: conserving intraday liquidity vs contributing to system flow
```

---

## Six Required Operational Elements

```
ELEMENT 1 — MEASUREMENT AND FORECASTING:
  → Capacity to measure expected GROSS (not net) daily inflows and outflows
  → Anticipate intraday timing of these flows where possible
  → Forecast range of potential net funding shortfalls at different points in day
  → Requires: understanding rules of all payment systems where active;
    identifying key counterparties and their payment timing patterns;
    identifying critical times/days when liquidity needs spike
  → Ask key customers (including customer banks) to forecast their own payment traffic
  [RAW-BOOK bcbs144 para 80]

ELEMENT 2 — REAL-TIME MONITORING:
  → Monitor intraday positions against expected activities and available resources
  → Resources to monitor: balances, remaining intraday credit capacity, available collateral
  → Frequent intraday position monitoring → judge when to acquire more liquidity or restrict outflows
  → Enables efficient allocation of intraday liquidity across own needs + customer banks' needs
  → Allows quick reaction to unexpected flows; adjust overnight funding positions
  [RAW-BOOK bcbs144 para 81]

ELEMENT 3 — ACQUIRE INTRADAY FUNDING:
  → Arrange sufficient intraday funding to meet objectives
  → Sources:
    - Central bank intraday credit (main source for account holders)
    - Correspondent/custodian intraday credit to customer banks
    - Other market sources (overnight transactions delivered at specific times)
  → Sources may vary within and across currencies
  [RAW-BOOK bcbs144 para 82]

ELEMENT 4 — COLLATERAL MANAGEMENT:
  → Manage and mobilise collateral to obtain intraday funds (links to P9)
  → Sufficient collateral available for intraday liquidity objectives
  → Operational arrangements in place: pledge/deliver to CBs, correspondents, custodians
  → Understand timeframes to mobilise different collateral types including cross-border
  [RAW-BOOK bcbs144 para 83]

ELEMENT 5 — TIMING CONTROL OVER OUTFLOWS:
  → Robust capability to manage timing of liquidity outflows
  → Ability to manage payment outflows of key customers
  → If customers have intraday credit: credit procedures support timely decisions
  → Internal coordination across business lines for outflow controls
  [RAW-BOOK bcbs144 para 84]

ELEMENT 6 — DISRUPTION PREPAREDNESS:
  → Prepared to deal with unexpected disruptions to intraday liquidity flows
  → Reflected in stress testing (P10) and CFP (P11) — intraday coverage required
  → Understand level and timing of needs from payment system failure-to-settle procedures
  → Business continuity arrangements are critical to intraday LRM effectiveness
  [RAW-BOOK bcbs144 para 85]
```

---

## Correspondent and Custodian Banks

```
Special challenge: correspondent/custodian role creates bilateral intraday exposures

AS PROVIDER of correspondent/custodian services:
  → Customer payment traffic can create large gross inflows and outflows
  → Unexpected changes → large net deposits, withdrawals or credit drawdowns
  → Impact both intraday AND overnight positions
  [RAW-BOOK bcbs144 para 87, footnote 46]

AS USER of correspondent/custodian:
  → Assure that arrangement allows timely obligation settlement
  → Understand potential for operational/financial disruption at correspondent
  → Have alternative arrangements if correspondent cannot perform
  [RAW-BOOK bcbs144 para 87]

SECURITIES SETTLEMENT SYSTEMS:
  For banks relying on collateralised funding:
  → Monitoring positions in securities settlement systems = equally important as RTGS
  → Collateral pledging/return flows must be tracked intraday
  [RAW-BOOK bcbs144 para 86]
```

---

## Scope and Proportionality

```
Applies to: "all financial markets and currencies in which [bank] has significant
payment and settlement flows" [RAW-BOOK bcbs144 para 86]

Tools and resources scaled to:
  ① Bank's business model
  ② Role in financial system
  ③ How it conducts activities (direct participant vs via correspondent)
  ④ Whether it provides correspondent/custodian services to others
```
