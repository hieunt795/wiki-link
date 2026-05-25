---
node_id: bcbs_liquidity_stress_testing_p10_001
type: mechanism
title: BCBS Liquidity Stress Testing Framework — Principle 10 (2008)
aliases:
  - BCBS liquidity stress test 2008
  - Principle 10 liquidity scenarios
  - institution-specific market-wide liquidity stress
  - stress test to CFP link
  - kiểm tra sức chịu đựng thanh khoản BCBS
  - nguyên tắc 10 kịch bản căng thẳng thanh khoản
domain:
  primary: banking_regulation
  secondary: financial_stability
tags:
  - stress_testing
  - liquidity_risk
  - bcbs
  - scenario_analysis
  - cfp
  - risk_tolerance
  - institution_specific
  - market_wide
  - bcbs144
confidence: 4
stability: stable
thesis: >
  BCBS Principle 10 (2008) requires regular stress testing across four scenario
  dimensions: short-term vs protracted, institution-specific vs market-wide
  (and combinations). Tests must feed directly into: (1) sizing of the HQLA cushion;
  (2) adjusting liquidity positions, strategies and limits; (3) shaping the
  Contingency Funding Plan (CFP). Critically, the standard pre-dates Basel III's
  ILAAP and SREP but establishes the same linkage principle: stress test results
  are not standalone exercises — they drive management action and capital/liquidity
  planning decisions. Scenarios must include simultaneous drying up of multiple
  funding markets, restriction on FX convertibility, and severe operational disruptions.
source_refs:
  - path: 02_sources/regulator/bcbs/bcbs144.md
    pages: "para 94–109 (Principle 10 full: process, scenarios, assumptions, utilisation), para 99 (scenario types), para 103 (assumption list), para 108–109 (utilisation: management actions, CFP link)"
    weight: primary
related:
  - node: "[[Bcbs_Sound_Liquidity_Risk_Management_17_Principles_2008]]"
    relation: parent_framework
  - node: "[[Bcbs_Hqla_Liquidity_Cushion_Principle_12]]"
    relation: cushion_sizing_output
  - node: "[[Bcbs_Liquidity_Contingency_Funding_Plan_Principle_11]]"
    relation: cfp_input
date_created: "2026-05-25"
date_updated: "2026-05-25"
---

## The Four-Dimension Scenario Matrix

```
                    │  Institution-specific  │  Market-wide
────────────────────┼────────────────────────┼────────────────────────
Short-term          │  Bank-specific event   │  Market disruption
                    │  (rating downgrade,    │  (CP market closes,
                    │   fraud, ops failure)  │   repo markets seize)
────────────────────┼────────────────────────┼────────────────────────
Protracted          │  Sustained loss of     │  Systemic liquidity
                    │  confidence in bank    │  crisis, multiple
                    │  (SVB-type slow run)   │  markets impaired
────────────────────┴────────────────────────┴────────────────────────
  ALSO: Combinations of above (most severe) — tested individually AND combined
[RAW-BOOK bcbs144 para 99]
```

---

## Mandatory Scenario Coverage

```
A bank should consider:
  ① Simultaneous drying up of market liquidity in several previously highly liquid markets
  ② Severe constraints in accessing secured AND unsecured funding sources
  ③ Restrictions on currency convertibility
  ④ Severe operational or settlement disruptions in one or more payment/settlement systems
  ⑤ Combination scenarios (bank-specific + market-wide at same time)
  [RAW-BOOK bcbs144 para 99]

INTRADAY dimension: tests must consider intraday liquidity needs, not just overnight
  → Time-critical payment obligations in multiple currencies simultaneously
  → Customer payment obligations (correspondent/custodian role)
  [RAW-BOOK bcbs144 para 101]

KEY LINKAGE (P10 → P8):
  Intraday stress scenarios must be reflected in CFP and stress test assumptions
  [RAW-BOOK bcbs144 para 101, 105]
```

---

## Stress Testing Assumptions: Required Considerations

Key assumptions a bank must consider in stress scenario design:
[RAW-BOOK bcbs144 para 103]

```
ASSET SIDE:
  - Asset market illiquidity and erosion in value of liquid assets
  - Operational ability of the bank to monetise assets

LIABILITY SIDE:
  - Run-off of retail funding
  - (Un)availability of secured and unsecured wholesale funding
  - Correlation between funding markets (failure of diversification under stress)
  - Funding tenors (shortening under stress)
  - Impact of credit rating triggers (derivative collateral calls, committed lines)

OFF-BALANCE SHEET:
  - Additional margin calls and collateral requirements
  - Contingent claims (committed lines drawn, conduit financing)
  - Draws on backup lines extended to third parties or subsidiaries

OPERATIONAL:
  - FX convertibility and access to FX markets
  - Ability to transfer liquidity across entities, sectors, borders
    (legal, regulatory, operational and time zone restrictions)
  - Access to central bank facilities
  - Remedial actions: availability of documentation and operational expertise
```

---

## Utilisation: Stress Results Must Drive Action

```
Results must be discussed by senior management and used for:
  ① Remedial / mitigating actions:
     → Limit reductions, position adjustments, funding source diversification
  ② HQLA cushion sizing:
     → Cushion must be sufficient to cover identified funding gaps under stress
  ③ CFP shaping:
     → Funding shortfalls identified in stress → incorporated into CFP design
  ④ Strategic planning:
     → Asset-liability composition adjustments
  ⑤ Day-to-day risk management:
     → Monitoring of sensitive cash flows, tightening concentration limits

"stress test results and vulnerabilities and any resulting actions should be
reported to and discussed with the board and the bank's supervisors"
[RAW-BOOK bcbs144 para 108]

IF projected funding deficits > risk tolerance:
  → Management must EITHER adjust liquidity position OR bolster CFP
  → Cannot passively accept a stress gap [RAW-BOOK bcbs144 para 109]
```

---

## Frequency, Review and Governance

```
Frequency: "regular basis" — commensurate with size and liquidity risk profile
  → Increase frequency during volatile market conditions
  → Or at supervisor request
  [RAW-BOOK bcbs144 para 96]

Senior management: must actively demand rigorous scenarios — even when liquidity is plentiful
  → Complacency in good times is a governance failure [RAW-BOOK bcbs144 para 97]

Scenario review cycle:
  → Regular reviews of scenario design: are scenarios still appropriate?
  → Consider: changes in market conditions, bank business model changes,
    actual experiences during stress events [RAW-BOOK bcbs144 para 106]

Sensitivity analysis (supplemental):
  → Analyse sensitivity of results to key assumptions
  → Identifies degree of vulnerability to specific factors [RAW-BOOK bcbs144 para 107]
```

---

## Diagnostic: Is P10 Compliant?

```
FAILING PATTERNS (documented from pre-2008 failures):
  ✗ Severe and prolonged stress treated as implausible — scenario design too mild
  ✗ Stress tests that did not factor in market-wide strain
  ✗ No testing of funding source correlation failure under stress
  ✗ CFP not linked to stress test results
  ✗ Stress tests not reviewed as business model changes
  [RAW-BOOK bcbs144 para 3, 72]

PASSING PATTERNS:
  ✓ Four-dimensional scenario coverage (short/protracted × bank/market)
  ✓ Intraday scenarios included
  ✓ Specific funding market closure scenarios (CP, repo, unsecured)
  ✓ Results drive cushion sizing + CFP design
  ✓ Board reviews results and requires management action
```
