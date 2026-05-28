---
node_id: integrated_stress_testing_capital_liquidity_link_001
type: framework
title: "Integrated Stress Testing: Linking Capital, Liquidity, IRRBB, and Credit Risk"
aliases:
  - CCAR stress testing framework
  - EBA stress test methodology
  - Integrated balance-sheet steering
  - Kiểm tra stress tích hợp vốn và thanh khoản
  - Stress test toàn diện

domain:
  primary: alm
  secondary:
    - basel_risk
tags:
  - stress_testing
  - ccar
  - eba_stress_test
  - irrbb
  - capital_planning
  - integrated_balance_sheet
  - ppnr
  - rwa_stress
  - liquidity_stress

confidence: 1
stability: evolving

thesis: >
  [LLM] Integrated stress testing links macro scenarios simultaneously to credit losses, NII changes, RWA migration, LCR impacts, and capital ratios across a multi-quarter horizon; the 2007–9 crisis revealed that solvency-only stress tests were insufficient because liquidity failures can precede capital insolvency. [LLM] The US CCAR framework (dynamic balance sheet, internal scenarios, 9-quarter horizon) and the EU EBA framework (static balance sheet, external scenarios only, 3-year adverse scenario) represent different regulatory philosophies, but both now require integration with IRRBB stress metrics (EVE and NII) under BCBS 368.

source_refs:
  - path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
    pages: "Ch 19 — A Global Perspective on Stress Testing (Boston Consulting Group)"
    weight: primary

related:
  - node: "[[Bank_Capital_Structure_And_Capital_Management_Alm]]"
    relation: component_of
  - node: "[[Funding_Gap_Profile_And_Behavioural_Maturity_Calendar]]"
    relation: related_to
  - node: "[[Reserve_Asset_Management_Hqla_Portfolio_Bank]]"
    relation: related_to

date_created: "2026-05-28"
date_updated: "2026-05-28"
---

## Historical Context

Pre-crisis stress testing (before 2007) was largely siloed:
- Market risk stress tests (required under 1996 Basel I market risk amendment)
- Credit risk sensitivity tests (required under Basel II from 2004)
- Liquidity risk was essentially absent from regulatory stress frameworks

[LLM] The 2007–9 crisis demonstrated that solvency and liquidity risks are deeply interconnected: a deteriorating capital position triggers funding outflows (creditors withdraw), which in turn accelerates the capital decline. Post-Lehman systemic liquidity freeze exposed that banks with adequate capital ratios could nonetheless become illiquid within days.

## CCAR (US) — Key Features

**Scope (2017):** 39 institutions; annual cycle (instructions in January, submission by April, FRB decision in June).

**Four forecast components under each scenario:**
1. **PPNR (Pre-Provision Net Revenue):** Net interest income + non-interest income (fees) − non-interest expense. Modelled from asset/deposit/funding balances, margins, transaction volumes, and macro-driven market share assumptions.
2. **Stress losses:** Credit losses (PD × EAD × LGD models), trading losses (price shock / full revaluation), counterparty losses, operational losses.
3. **RWA:** Modelled centrally under Basel III rules; includes balance-sheet volume change impacts.
4. **Capital ratios:** CET1, Tier 1, Total Capital, Tier 1 leverage — all must stay above minimums across the full 9-quarter horizon, every quarter.

**Three scenario types:**
- FRB supervisory baseline, adverse, and severely adverse (macro variables: GDP, unemployment, equity indexes, house prices, bond yields, FX rates; ~28 domestic and international variables)
- Global Market Shock (GMS) for large trading books: ~20,000 risk factor shocks across 6 asset classes
- Bank-specific (BHC/IHC) internal scenarios: must be at least as severe as FRB severely adverse in capital impact terms; must stress idiosyncratic vulnerabilities

**Dynamic balance sheet:** New business originations, defaults, prepayments, and customer behaviour all modelled as scenario-dependent.

**Qualitative dimension:** Governance, model validation, data quality, and process documentation are assessed as a separate qualitative element. Most capital plan rejections have been for qualitative rather than quantitative reasons.

## EBA Stress Test (EU) — Key Features

**Scope (2018 vintage):** All banks with ≥€30 billion in assets; covers 70% of total consolidated EU banking assets. Biennial.

**Timeline:** Up to 12 months from preliminary methodology publication to result disclosure.

**Scenario types:** External only — EBA-set base and adverse scenarios (no internal scenarios required). Adverse scenario defined as a 3-year path of macroeconomic deterioration (GDP, unemployment, property prices, sovereign spreads) versus a stable base case.

**Static balance sheet assumption:** After the snapshot date, no new business origination or business mix changes are modelled. Assets and liabilities run off contractually. This simplification makes results comparable across banks but misses dynamic management responses.

**Risk coverage:**
- Credit risk (banking book, including securitisation)
- Market risk (all fair-value positions: HFT, AFS, fair value option)
- Operational risk (including conduct risk; increase in capital/RWA)
- NII and P&L sensitivity under stress macro conditions

**Output:** CET1 ratio reduction expressed in percentage points; serves as input to SREP for setting P2G.

## CCAR vs EBA: Key Differences

| Feature | CCAR (US) | EBA (EU) |
|---------|-----------|----------|
| Frequency | Annual | Biennial |
| Balance sheet assumption | Dynamic | Static |
| Internal scenarios | Required | Not required |
| Horizon | 9 quarters | 3 years |
| Qualitative assessment | Strong (model risk, governance) | Lighter |
| Capital action constraints | Direct (dividend/buyback restrictions) | Indirect (SREP input) |

## IRRBB Integration (BCBS 368)

[LLM] The 2016 IRRBB standard (BCBS 368) requires banks to stress-test EVE (Economic Value of Equity — present value sensitivity) and NII (Net Interest Income — 12-month earnings sensitivity) under 6 prescribed rate scenarios (parallel shock ±200bps, short-rate shock, long-rate shock, flattener, steepener). Results feed into ICAAP/SREP capital assessment.

Harmonisation opportunities with CCAR:
1. **Governance:** Both require board oversight and quarterly+ briefings; common target operating model possible
2. **Risk methodology:** Both use scenario-dependent prepayment and behavioural assumptions; aligned calibration reduces inconsistency
3. **Risk horizon:** CCAR = 9 quarters disclosed; BCBS 368 EVE = lifetime; BCBS 368 NII = 12 months
4. **Balance-sheet assumptions:** CCAR = dynamic; BCBS 368 disclosed EVE = run-off; BCBS 368 NII = constant
5. **IT/data:** Strong overlap in data requirements; BCBS 239-compliant common data infrastructure is best practice

## Integrated Balance-Sheet Steering

[LLM] The logical evolution of stress testing is away from periodic regulatory exercises and toward continuous integrated balance-sheet management. Three building blocks required:
1. **Methodological framework:** Scenario-dependent modelling choices for credit, market, liquidity, and operational risk
2. **Implementation tools:** Integrated systems, governance, and data workflows linking stress to planning
3. **Optimisation:** Strategy and management actions calibrated to trade off capital, liquidity, funding cost, and leverage under both normal and stressed conditions

[LLM] An integrated balance-sheet view enables joint optimisation of capital, liquidity, funding tenor, and leverage simultaneously — rather than managing each constraint separately in silos, which often produces inconsistent or suboptimal solutions.
