---
node_id: stagflation_policy_response_tradeoff_frm_001
type: framework
title: Stagflation Policy Response Tradeoff Framework
aliases:
- stagflation policy tradeoff
- look through vs tighten
- phan ung chinh sach voi dinh tram lam phat
domain:
  primary: monetary_policy
  secondary:
  - macro_outlook
tags:
- stagflation
- central_banks
- supply_shock
- credibility
- real_income
- policy_response
confidence: 3
stability: evolving
thesis: 'In a stagflation shock, the policy choice is state-contingent: central banks
  can look through direct price effects only if inflation expectations remain anchored
  and the shock does not become persistent through wages, contracts, or production
  networks.

  '
source_refs:
- path: 02_sources/books/imf_macro_accounting/Macroeconomic Accounting and Analysis
    IMF.md
  pages: Inflation; Incomes Policy
  weight: primary
- path: 02_sources/Inbox/Central Bank Commentary (April 2026)_ Fed, BoJ, and BoE..md
  pages: Introduction; Policy assessment
  weight: supporting
- path: 02_sources/Clipping/Fed, ECB, and BoJ_ A Matter of Credibility.md
  pages: full document
  weight: supporting
parent_node: null
related:
- node: '[[Supply Shock Policy Response Scenario Taxonomy]]'
  relation: scenario_implementation
- node: '[[Central Bank Credibility Supply Shock Policy Space]]'
  relation: credibility_condition
- node: '[[Cost Push Inflation Persistence Mechanism]]'
  relation: persistence_trigger
- node: '[[Stagflation Regime Diagnostic Framework]]'
  relation: diagnostic_parent
date_created: 2026-05-24
date_updated: 2026-05-24
---

## Core Tradeoff
[LLM] Stagflation creates a different policy problem from normal overheating because monetary tightening can restrain inflation expectations but cannot produce missing oil, food, shipping capacity, or intermediate inputs.

[RAW-BOOK §Inflation] The IMF text says a key relative-price shock can become generalized inflation if policy is not sufficiently firm.

[RAW-BOOK §Analyzing Inflation] The IMF text also says that if policy refuses to accommodate cost-push inflation, wage increases translate into higher unemployment rather than higher inflation.

[LLM] The policy maker is therefore allocating the shock between the price level, real wages, employment, and output.

## Look-Through Rule
[RAW-CLIP] The 2026 central-bank commentary says the Fed, BoE, and BoJ treated a Middle East energy shock as a supply shock to be looked through unless it changed inflation expectations or secondary effects.

[RAW-CLIP] The same source says the standard framework distinguishes direct effects, indirect effects, and second-round effects in wage- and price-setting behavior.

[LLM] A look-through strategy is coherent when the shock is temporary, expectations are anchored, wage behavior is contained, and production-network effects fade.

## Tightening Rule
[RAW-BOOK §Inflation] The IMF text says firm non-accommodating financial policies helped prevent a large energy shock from becoming persistent inflation in Japan.

[RAW-CLIP] The credibility source says central-bank credibility determines how much room a central bank has to tolerate temporary inflation during a supply shock.

[LLM] Tightening becomes more likely when the central bank cannot credibly promise that inflation will return to target without action.

## Policy Matrix
| Shock state | Policy bias | Reason |
|---|---|---|
| Temporary direct price effect | [LLM] Look through | [RAW-CLIP] Direct effects fade before policy acts |
| Indirect production costs | [LLM] Hold with hawkish optionality | [RAW-CLIP] Indirect effects may take longer to permeate |
| Wage/price second-round effects | [LLM] Tighten | [RAW-CLIP] Behavioral persistence outlasts the original shock |
| Weak credibility | [LLM] Tighten earlier | [RAW-CLIP] Expectations anchor is fragile |

[LLM] The framework implies that current stagflation analysis should focus less on a single CPI print and more on whether the cost shock is being absorbed by real incomes or being validated through wages, expectations, production networks, and policy accommodation.
