---
node_id: ilaap_liquidity_adequacy_assessment_framework_001
type: framework
title: ILAAP — Internal Liquidity Adequacy Assessment Process Framework
aliases:
- ILAAP framework
- Internal Liquidity Adequacy Assessment
- individual liquidity adequacy assessment
- liquidity adequacy process
- quy trình đánh giá đủ thanh khoản nội bộ
- ILAAP thanh khoản
domain:
  primary: banking_regulation
  secondary: alm
tags:
- ilaap
- liquidity_risk
- stress_testing
- cfp
- srep
- risk_appetite
- bcbs
- eba
- ecb
- supervisory_review
- governance
- survival_period
confidence: 4
stability: stable
thesis: 'ILAAP is a bank''s own comprehensive internal process for assessing its liquidity
  adequacy — broader and more adaptive than LCR/NSFR because it encompasses internal
  stress tests (producing survival periods and time-to-central-bank metrics), risk
  appetite calibration, contingency planning, and a board-approved liquidity adequacy
  statement. Introduced by EBA/DNB in 2012 based on BCBS bcbs144 Principles 10–12,
  formalised by ECB in November 2018 under SSM. The regulator (L-SREP) challenges
  the ILAAP and issues Individual Liquidity Guidance that extends beyond LCR requirements.
  The core value proposition: banks understand their own business model, client behaviour,
  and market exposures better than supervisors can through standardised metrics —
  the ILAAP forces banks to make and justify those assumptions.

  '
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: 'lines 3853–3909 (Ch.13: ILAAP vs LCR/NSFR, supervisor rationale, Panel 13.3
    board test, Panel 13.4 scenarios/metrics, Panel 13.5 best practice structure)'
  weight: primary
- path: 02_sources/books/choudhry_banking_fixed_income/Choudhry_Principles_of_Banking.md
  pages: 'lines 11799–11981 (Ch.20: ILAAP definition, stress testing process, ILAAP
    drafting, L-SREP, Individual Liquidity Guidance, ILAAP ToC)'
  weight: primary
- path: 02_sources/regulator/bcbs/bcbs144.md
  pages: 'para 94–127 (Principles 10–12: stress testing, CFP, HQLA cushion — conceptual
    foundation for ILAAP)'
  weight: supporting
- path: 02_sources/regulator/bcbs/ssm.ilaap_guide_201811.en.md
  pages: full document — 7 ILAAP principles, dual economic/normative perspective,
    SSM expectations
  weight: primary
- path: 02_sources/regulator/bcbs/Final report on Guidelines on ICAAP ILAAP (EBA-GL-2016-10).md
  pages: full document — ILAAP-specific information requirements for SREP (Section
    3, ILAAP categories)
  weight: supporting
parent_node: null
related:
- node: '[[Bcbs_Liquidity_Stress_Testing_Principle_10]]'
  relation: stress_test_is_ilaap_input
- node: '[[Bcbs_Liquidity_Contingency_Funding_Plan_Principle_11]]'
  relation: cfp_is_ilaap_output
- node: '[[Bcbs_Sound_Liquidity_Risk_Management_17_Principles_2008]]'
  relation: conceptual_foundation
- node: '[[Bcbs_Hqla_Liquidity_Cushion_Principle_12]]'
  relation: hqla_buffer_from_ilaap_sizing
date_created: '2026-05-27'
date_updated: '2026-05-27'
---

## Position in Liquidity Framework

```
LCR / NSFR          Regulatory minimums — fixed thresholds, public disclosure
                    Cannot adapt quickly to changing balance sheet risk
        ↓ necessary but not sufficient
ILAAP               Internal, bank-specific, comprehensive liquidity assessment
                    Private (not public); covers scenarios beyond 30-day LCR horizon
        ↓ results submitted to supervisor
L-SREP              Supervisor challenges ILAAP assumptions
                    Issues Individual Liquidity Guidance (ILG) — extends beyond LCR
```

**Origin:** Term "ILAAP" not found in BCBS documents — construct of EBA/DNB (2012),
based directly on BCBS bcbs144 Principles 10–12. Formalised by ECB for SSM in 2018.
[RAW-BOOK Elkenbracht_Huizing_Handbook_ALM p.3855]

---

## Why ILAAP Adds Value Beyond LCR/NSFR

```
PROBLEM WITH REGULATORY METRICS:
  → LCR/NSFR: fixed calibration, ~10 years to introduce as binding minimums
  → Cannot be recalibrated rapidly when bank balance sheets or markets change
  → One metric cannot accurately capture risks of all banks in all countries

ILAAP SOLUTION:
  ① Adaptability: bank calibrates metrics to its own business model, client base, markets
  ② Completeness: covers stress horizons beyond 30 days; all material risk drivers
  ③ Supervisor role: challenge assumptions, not dictate them
  ④ Integration: stress tests → risk appetite limits → CFP → board decision

KEY STATEMENT (DNB/ECB perspective):
  "We think the banks are in a better position to identify, measure and manage
   liquidity risks than we are. [...] direct supervisors are there to challenge
   the internal assumptions made by the bank, not to make them up themselves."
[RAW-BOOK Elkenbracht_Huizing_Handbook_ALM p.3869]
```

---

## ILAAP Process Architecture

```
STEP 1 — RISK IDENTIFICATION
  Input:  business model, client types, markets, regions, products
  Output: material risk drivers → select appropriate measurement tools

STEP 2 — MEASUREMENT + CALIBRATION
  Regulatory metrics: LCR, NSFR
  Internal metrics:   survival period, time-to-LCR-breach, time-to-central-bank
  QA: model validation, assumption testing, internal audit

STEP 3 — RISK APPETITE
  Set limits per metric per scenario
  Note: appetite differs by scenario type
    (LCR breach under market disruption = worse than breach under combined shock)

STEP 4 — REPORTING + ESCALATION
  Internal reporting: granular enough for board (entity, currency, actual vs limit)
  Escalation procedures: defined triggers and actions

STEP 5 — BOARD DECISION
  → Liquidity Adequacy Statement (board-approved conclusion)
  → Board decides action if liquidity position below desired level

STEP 6 — CFP + RECOVERY LINK
  → Liquidity Contingency Plan consistent with Recovery Plan triggers
  → Policies clarify: what actions already taken BEFORE recovery triggers
[RAW-BOOK Elkenbracht_Huizing_Handbook_ALM p.3902]
```

---

## Three Mandatory Stress Scenarios

| Scenario | Description | Retail Effect | Wholesale | Primary Source |
|---|---|---|---|---|
| **Market disruption** | Systemic stress, no bank-specific element | Nil or minor inflow | No rollover | Market-liquid HQLA |
| **Idiosyncratic** | Bank-specific event (downgrade, reputation) | Significant withdrawal (est. 7.5%–14% wks 1–2) | No rollover | CB facilities + HQLA |
| **Combined** | Both simultaneously (most severe) | Moderate withdrawal (~half idiosyncratic) | No rollover | ELA + HQLA + CB repo |

[RAW-BOOK Elkenbracht_Huizing_Handbook_ALM p.3880–3882; Choudhry_Principles_of_Banking p.11886–11888]

---

## Three Core Liquidity Metrics

```
① TIME-TO-LCR-BREACH
   Measures: days until LCR falls below 100% under stress
   Captures: absolute buffer distance × maturity profile of balance sheet
   Risk appetite set by: data lag, escalation speed, investor LCR sensitivity
   Warning: LCR peer pressure can lead to inaccurate (not conservative) calibration

② TIME-TO-CENTRAL-BANK
   Measures: days bank survives using ONLY market-liquid assets (no CB facilities)
   Minimum target: 30 days; internal targets typically higher
   Caveat: LCR ≥ 100% does NOT guarantee 30-day survival (intra-period mismatches)

③ COMBINED SURVIVAL PERIOD
   Measures: days using HQLA + contingent liquidity buffer (CB-eligible non-HQLA)
   Most comprehensive metric — reflects management actions available
   Key design choice:
     "Run-down of bank" view: assume contractual inflows received (bank closed for new business)
     "Going concern" view:    assume some loan rollover (lower inflows, but bank stays open)
   Higher uncertainty in assumptions → higher survival period target required
[RAW-BOOK Elkenbracht_Huizing_Handbook_ALM p.3886–3890]
```

---

## Liquidity Buffer Architecture

```
LAYER 1: LCR HQLA
  → Counts toward LCR
  → Market-liquid: can sell or repo in public markets
  → Central banks may prefer banks exhaust this before emergency facilities

LAYER 2: CONTINGENT LIQUIDITY BUFFER
  → CB-eligible assets not meeting HQLA criteria (credit quality, encumbrance)
  → Cannot sell easily in public markets but can repo with central bank
  → Key ILAAP component: extends combined survival period beyond LCR horizon

LAYER 3: CB EXTRAORDINARY FACILITIES (ELA, LOLR)
  → At central bank discretion — not guaranteed
  → Reputational cost: accessing signals distress to markets
  → Use only AFTER Layers 1 and 2 depleted

TRADE-OFF IN CRISIS:
  Bank can go to markets first (depletes HQLA, reduces LCR) OR
  repo non-HQLA with central bank (preserves LCR, avoids market signal)
  → Best strategy: case-dependent. ILAAP should pre-analyse both options.
[RAW-BOOK Elkenbracht_Huizing_Handbook_ALM p.3892–3894]
```

---

## Board Information Quality Test

Board must be able to answer all seven of these from the ILAAP pack:

```
1. Where does liquidity risk come from for this bank?
2. How is it measured? What assumptions are critical?
3. Is information complete? (all entities, countries, currencies)
4. Is information granular enough? (entity level, actual vs limit between reporting dates)
5. Can information be trusted? (QA, validation, audit in place)
6. Does information link actual positions to risk appetite (limits)?
7. Does information yield a clear conclusion in well-defined metrics?

→ If board cannot answer all seven: ILAAP governance is deficient.
[RAW-BOOK Elkenbracht_Huizing_Handbook_ALM Panel 13.3, p.3857–3868]
```

---

## ILAAP Document Structure (Choudhry Best Practice)

```
1   Executive Summary
2   Firm business model, governance, strategy
3   Firm risk management framework
4   Forecast balance sheet
5   Funding profile and plan
6   Liquidity risk definition and ownership
7   Liquidity risk management framework
8   Liquidity risk appetite
9   ILAAP coverage (scope: legal entities, currencies, products)
10  Stress scenarios
11  Stress testing results — all material liquidity and funding risks
12  Pillar 2 Liquidity
13  Liquidity risk assessment (adequacy conclusion)
14  Liquidity risk mitigants + management actions table
15  HQLA policy and portfolio
16  Other funding sources / mitigants
17  Reverse Stress Test
18  ILAAP challenge and internal approval process
19  Use of ILAAP in the firm (evidence of embedding)

Appendices:
  A1: LCP (Liquidity Contingency Plan) reference
  A2: Stress testing assumptions
  A3: FTP Policy
  A4: Deposit pricing policy and model
[RAW-BOOK Choudhry_Principles_of_Banking p.11951–11974]
```

---

## L-SREP and Individual Liquidity Guidance

```
L-SREP (Liquidity Supervisory Review and Evaluation Process):
Supervisor assesses 6 dimensions:
  ① IT/framework: adequate system to identify liquidity risk?
  ② Governance: governance around LRM process sufficient?
  ③ FTP: adequate transfer pricing mechanism for liquidity?
  ④ LAB controls: adequate controls over liquid asset buffer?
  ⑤ Strategy: clearly defines and communicates liquidity risk tolerance?
  ⑥ Limits: comprehensive internal limit and control framework?

Individual Liquidity Guidance (ILG) output:
  → Quantity + quality of liquid assets: adequate?
  → Funding profile: appropriate?
  → Qualitative arrangements needed to mitigate residual risks
  → EXTENDS BEYOND LCR — covers liquidity risks not captured by LCR
[RAW-BOOK Choudhry_Principles_of_Banking p.11940–11981]
```

---

## ILAAP vs ICAAP Parallel

```
ICAAP: Internal Capital Adequacy Assessment Process
  → Pillar 2 capital add-ons under SREP
  → Solvency-focused

ILAAP: Internal Liquidity Adequacy Assessment Process
  → Individual Liquidity Guidance under L-SREP
  → Liquidity-focused

Both must:
  → Be board-approved annually (or on business model change)
  → Be proportionate to nature, scale, complexity
  → Link to the same Risk Appetite Framework
  → Inform real decisions — not be compliance-only documents

Integration: ICAAP/ILAAP/Recovery Planning should be one integrated
risk management cycle, not separate documents.
```

---

## Common Failures

```
DESIGN FAILURES:
  ✗ Document created for supervisor rather than internal use → paper exercise
  ✗ Metrics not adapted to bank's actual business model → miss material risks
  ✗ Scenarios too mild — severe-and-prolonged stress treated as implausible
  ✗ CFP not linked to stress test results (pre-2008 documented failure)
  ✗ LCR sensitivity to assumptions not shown to board
  ✗ Calibration biased toward peer comparison rather than conservatism

GOVERNANCE FAILURES:
  ✗ Board approves ILAAP without challenging key assumptions
  ✗ ILAAP not integrated with ALM, Treasury, Recovery Planning processes
  ✗ Documentation overload: multiple documents with no internal logic
  ✗ Contingent buffer in wrong legal entity / jurisdiction at time of stress
[RAW-BOOK Elkenbracht_Huizing_Handbook_ALM p.3898–3902; Choudhry_Principles_of_Banking p.11938]
```
