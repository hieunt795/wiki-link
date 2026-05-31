---
node_id: bcbs_liquidity_contingency_funding_plan_p11_001
type: regulation
title: BCBS Contingency Funding Plan (CFP) — Principle 11 (2008)
aliases:
- BCBS CFP Principle 11
- contingency funding plan liquidity 2008
- liquidity crisis response plan
- CFP invocation escalation procedures
- kế hoạch tài trợ dự phòng thanh khoản
- CFP thanh khoản BCBS nguyên tắc 11
domain:
  primary: banking_regulation
  secondary: financial_stability
tags:
- cfp
- contingency_plan
- liquidity_risk
- bcbs
- crisis_management
- stress_scenarios
- escalation
- bcbs144
confidence: 4
stability: stable
thesis: 'BCBS Principle 11 (2008) requires a formal Contingency Funding Plan (CFP)
  that is directly linked to stress test outcomes, covers a range of stress environments
  (not just a single scenario), has clear invocation and escalation procedures, and
  is regularly tested to verify operational feasibility. The CFP is not a static document
  — it must be updated at least annually and reviewed after each test. Key requirements:
  (1) clear roles and responsibilities with named alternates; (2) realistic timelines
  for contingency measure activation; (3) intraday coverage; (4) communication plans
  for internal and external parties; (5) integration with business continuity planning.
  CFPs that are not operationally tested are non-compliant even if the document is
  comprehensive.

  '
source_refs:
- path: 02_sources/regulator/bcbs/bcbs144 - Principles for Sound Liquidity Risk Management and Supervision.md
  pages: 'para 110–122 (Principle 11 full: design, roles, communication, testing),
    para 110 (CFP definition), para 111 (content requirements), para 113 (scenario
    range), para 114–115 (roles, escalation), para 116 (communication plan), para
    117–120 (design elements), para 121 (testing and update), para 122 (BCP integration)'
  weight: primary
parent_node: '[[Bcbs_Sound_Liquidity_Risk_Management_17_Principles_2008]]'
related:
- node: '[[Bcbs_Sound_Liquidity_Risk_Management_17_Principles_2008]]'
  relation: parent_framework
- node: '[[Bcbs_Liquidity_Stress_Testing_Principle_10]]'
  relation: cfp_is_stress_test_output
- node: '[[Bcbs_Intraday_Liquidity_Management_Principle_8]]'
  relation: intraday_coverage_requirement
date_created: '2026-05-25'
date_updated: '2026-05-25'
---

## Definition

"A contingency funding plan (CFP) is the compilation of policies, procedures and
action plans for responding to severe disruptions to a bank's ability to fund
some or all of its activities in a timely manner and at a reasonable cost."
[RAW-BOOK bcbs144 para 110]

---

## Required CFP Content

```
1. CONTINGENCY FUNDING SOURCES:
   → Diversified set of viable, readily available, flexibly deployable options
   → Amount of funds estimable from each source
   → Lead time needed to activate each source
   [RAW-BOOK bcbs144 para 111]

2. ESCALATION / INVOCATION PROCEDURES:
   → Clear decision-making: what actions, by whom, at what trigger level
   → Escalation to senior levels specified with criteria
   → "Crisis team" may be designated for internal coordination
   [RAW-BOOK bcbs144 para 114–115]

3. ROLES AND RESPONSIBILITIES:
   → Named individuals with authority to invoke CFP
   → Names + contact details of team members + their locations
   → Designated alternates for all key roles
   [RAW-BOOK bcbs144 para 114]

4. COMMUNICATION PLAN:
   → Internal: across business lines and locations
   → External: supervisors, central banks, payment system operators
   → Correspondents, custodians, counterparties, customers
   → Timing and messaging protocols per type of stress
   [RAW-BOOK bcbs144 para 115–116]

5. INTRADAY COVERAGE:
   → CFP must address intraday as well as overnight/term liquidity shortfalls
   → Procedures to prioritise critical payments when intraday resources scarce
   → Ability to identify and mobilise additional intraday collateral
   [RAW-BOOK bcbs144 para 119]
```

---

## Design Requirements

```
STRESS SCENARIO RANGE:
  CFP must cover: firm-specific + generalised market-wide + combinations
  Must not be designed for only one scenario type
  [RAW-BOOK bcbs144 para 113]

ASSET SALE / REPO CONSTRAINTS:
  CFP must account for:
  → Impaired ability to sell or securitise assets under stress
  → Link between asset market liquidity and funding liquidity closure
  → Second-round and reputational effects of executing contingency measures
    (eg publicly drawing on emergency facilities signals distress)
  [RAW-BOOK bcbs144 para 117]

CENTRAL BANK LENDING:
  CFP must reflect central bank programmes and collateral requirements
  → Include types of facilities available, acceptable collateral
  → Include operational procedures to access CB funds
  → Include assessment of reputational issues in accessing CB facilities
  [RAW-BOOK bcbs144 para 118]

CROSS-BORDER / INTRAGROUP TRANSFERS:
  CFP must realistically model:
  → Legal, regulatory, operational and time zone restrictions on fund transfers
  → Time required to complete transfers under actual arrangements
  → Assets intended as CFP collateral must be in correct legal entity and location NOW
    (not planned to be moved at the time of crisis)
  [RAW-BOOK bcbs144 para 120]
```

---

## Testing, Update and Maintenance Requirements

```
TESTING (regular, not just annual):
  Key test elements:
  → Roles and responsibilities: appropriate and understood by all named personnel?
  → Contact information: up to date?
  → Transferability of cash and collateral (especially cross-border): provably workable?
  → Legal and operational documentation: in place to execute at short notice?
  → Ability to sell or repo specific assets: periodically tested by actually doing it
  → Credit line drawdown: periodically tested with actual draws
  [RAW-BOOK bcbs144 para 121]

ANNUAL REVIEW:
  → Senior management reviews all aspects post each exercise
  → Updates submitted for board approval at least annually
  → More frequent if business or market circumstances change
  [RAW-BOOK bcbs144 para 121]

BCP INTEGRATION:
  → CFP must be operational when business continuity arrangements are invoked
  → Liquidity crisis team and BCP team must coordinate
  → CFPs stored in central repository AND at locations accessible to responsible parties
    under emergency conditions (off-site access required)
  [RAW-BOOK bcbs144 para 122]
```

---

## Common Failures (Pre-2008 Experience)

```
"Contingency funding plans (CFPs) were not always appropriately linked to
stress test results and sometimes failed to take account of the potential
closure of some funding sources."
[RAW-BOOK bcbs144 para 3]

SPECIFIC DOCUMENTED FAILURES:
  ✗ CFP as paper exercise — not operationally tested
  ✗ CFP assumes funding markets remain open (one scenario only)
  ✗ Intragroup transfers assumed possible but legally/operationally blocked
  ✗ Cross-border collateral mobilisation assumed instantaneous
  ✗ Communication plan names outdated (personnel changes)
  ✗ Liquidity crisis response team unaware of BCP activation procedures
  [LLM — derived from para 3 failure context + Principle 11 requirements]
```
