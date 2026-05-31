---
title: "Net Cumulative Cash Flow (NCCF) and Survival Horizon — LST Output Metrics"
topic_slug: alm_stress_test_balance_sheet
sub_question: "Q6"
status: draft
confidence: 3
sources:
  - path: "02_sources/regulator/bcbs/Guidelines on institutions stress testing (EBA-GL-2018-04).md"
    paragraphs: "§155, §159-162"
    weight: primary
promotion_candidate: true
target_wiki_type: mechanism
target_wiki_slug: "Liquidity_Stress_Test_Nccf_Survival_Horizon_Output_Metrics"
---

## Core Concept

A liquidity stress test produces two primary output metrics that operate at different levels of abstraction:

1. **Net Cumulative Cash Flow (NCCF)** — the time-series output
2. **Survival Horizon** — the summary scalar derived from NCCF and counterbalancing capacity

---

## 1. Net Cumulative Cash Flow (NCCF)

**Source:** EBA GL/2018/04 §159

> "The main methodology used for calculating the magnitude of the impact should be the net cash flow profile. For each scenario, at each stress level, the institution identifies cash inflows and outflows that are projected for each future time period and the resulting net cash flows. Institutions should consider the **lowest cumulative point of net cash flows** within the time period assessed in each given scenario."

**Mechanics:**

```
NCF(t) = Σ Inflows(0→t) − Σ Outflows(0→t)

For each scenario:
  - Project daily/weekly cash flows across time horizon (overnight → 12 months)
  - Accumulate: NCCF(t) = NCCF(t-1) + NetFlow(t)
  - Key output: lowest point of NCCF within the time horizon
```

**Time horizons required** (EBA GL §155):
- Short acute phase: up to 30 days (no business model change assumed)
- Prolonged phase: 3–12 months (less acute but sustained)
- Separate test: intraday liquidity risks

---

## 2. Survival Horizon

**Source:** EBA GL/2018/04 §160(c)

> "The survival horizon of the institution as derived from its counterbalancing capacity, i.e. the institution's ability to hold, or have access to, excess liquidity over short-term, medium-term and long-term time horizons in response to stress scenarios... and stressed cash flows, taken jointly, **before and after the impact of counterbalancing measures**."

**Definition:** The first time period at which the institution's counterbalancing capacity (CBC) is exhausted under a given stress scenario — i.e., when cumulative net outflows exceed available liquidity buffer.

**Two versions reported:**
- Before management actions (counterbalancing): pure structural survival
- After management actions: adjusted survival horizon (reflects CBC deployment)

**Relationship to LCR:**
- LCR is a standardised 30-day NCCF test using bcbs238 scenario parameters
- Survival horizon is a broader, multi-horizon, institution-specific version
- LCR ≥ 100% ≠ survival horizon ≥ 30 days (different scenarios, behavioral assumptions)

---

## 3. Counterbalancing Capacity (CBC)

**Source:** EBA GL §160(b)

> "Their available liquidity buffer, over and above the [LCR/NSFR] ratios, and other counterbalancing measures, i.e. their counterbalancing capacity, for each stress scenario; the stress testing of this metric should be accompanied by an assessment of the impact on the **proportion and nature of encumbered assets**."

CBC = HQLA buffer (post-haircut) + unencumbered assets monetisable under stress + CB access (repo facilities)

**Conservative approach rule** (§161): When applying CB counterbalancing (monetary policy operations), institutions must adopt a conservative approach — access to CB facilities cannot be assumed unless pre-arranged and operationally tested.

---

## 4. Interpretation Framework

| Metric | What it answers | Regulatory parallel |
|--------|-----------------|---------------------|
| NCCF time series | When does the gap appear? How deep? | LCR 30-day window |
| Lowest NCCF point | Worst-case liquidity need | LCR denominator |
| Survival horizon (pre-CBC) | How long can bank survive without management action? | — |
| Survival horizon (post-CBC) | How long can bank survive deploying all tools? | ILAAP adequacy test |

---

## Promotion Assessment

**Ready for wiki promotion:** Yes — mechanism is structural, cross-topic, conf=3 (cited EBA GL §155/159-161).

**Blocking issues:** None. Create node: `03_wiki/mechanisms/Liquidity_Stress_Test_Nccf_Survival_Horizon_Output_Metrics.md`

**Related nodes to link:**
- `[[Liquidity_Stress_Test_Three_Building_Blocks_Assets_Liabilities_Management_Response]]`
- `[[Ilaap_Recovery_Plan_Management_Actions_No_Double_Counting]]`
- `[[Basel_Iii_Lcr_Hqla_Cashflow_Mechanics]]`
- `[[Liquidity_Stress_Three_Scenario_Types_Idiosyncratic_Market_Wide_Combined_Eba]]`
