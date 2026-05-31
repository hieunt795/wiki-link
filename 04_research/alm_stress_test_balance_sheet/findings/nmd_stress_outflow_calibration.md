---
title: "NMD Behavioral Model → Stress Outflow Rate Calibration Bridge"
topic_slug: alm_stress_test_balance_sheet
sub_question: "Q7"
status: draft
confidence: 3
sources:
  - path: "02_sources/regulator/bcbs/insights59.md"
    paragraphs: "§13, §22, §30, §33, §64, §71; fn.25, fn.54, fn.55"
    weight: primary
  - path: "02_sources/regulator/bcbs/bcbs238.md"
    paragraphs: "§73-104 (retail + wholesale run-off floors)"
    weight: secondary
  - path: "02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md"
    paragraphs: "Ch.5 (NMD decay model)"
    weight: tertiary
promotion_candidate: false
notes: "TRUE_GAP partially resolved — calibration framework documented at methodology level. Specific regulator-published multiplier tables not in current corpus. Suggest acquiring: EBA ILAAP peer review reports, ECB Banking Supervision 2019 LST methodology publication."
---

## Core Problem

IRRBB NMD behavioral models (decay model, stochastic 3-factor, replicating portfolio) are designed to estimate:
- **Average life** of non-maturity deposits under normal market conditions
- **Rate sensitivity** of balances for EVE/NII interest rate risk measurement

They are NOT calibrated for stress scenarios. The key question for LST is:

> "Under an idiosyncratic / market-wide / combined scenario over a 30-day horizon, what percentage of each NMD segment leaves the balance sheet?"

---

## Step 1: NMD Segmentation Carries Over (from IRRBB model)

The IRRBB NMD model's segmentation is the starting point:

| Segment | IRRBB use | LST use |
|---|---|---|
| Stable core | Longest replicating tenor (e.g. 5-10yr) | Lowest run-off rate under stress |
| Volatile layer | Short tenor (e.g. 0-3m) | Highest run-off rate under stress |
| Transactional (salary accounts) | Medium repricing | Lower stress run-off (LCR stable deposit) |
| Rate-sensitive (high-yield savings) | Short repricing | Higher stress run-off (LCR less stable) |

The segmentation scheme is shared; the behavioral assumptions diverge after segmentation.

---

## Step 2: Calibration Approaches for Stress Run-Off Rates

### Approach A — LCR as Regulatory Floor

**Source:** FSI §33 + fn.25; bcbs238 §73-104

LCR floors are the **minimum** — ILAAP and sector-wide stress tests may apply higher rates.

| Segment | LCR floor (bcbs238) | ILAAP/stress may use |
|---|---|---|
| Retail stable (insured, transactional) | 5% (or 3% with qualifying DIS) | 5-20% depending on scenario severity |
| Retail less stable | 10%+ | 15-40%+ |
| Small business | 5%/10% | Same as retail treatment |
| Wholesale operational | 25% | 25-50% |
| Wholesale non-financial corporate | 40% | 40-75% |
| Financial institution | 100% | 100% (floor = ceiling) |

**Rule (FSI fn.25):** "The fact that deposit run-off rates and haircuts under these scenarios may be higher than those used under the LCR reflects the fact that the objective of the international liquidity standard is to establish minimum liquidity requirements."

---

### Approach B — Historical Stress Calibration

**Source:** FSI §30, §205, §238 (BCB methodology)

BCB (Brazil) methodology:
```
Deposit outflow_i = VaR(deposit_i, 30-day horizon, 95% confidence)
                  + early redemption add-on (3 largest wholesale counterparties)
```

Data inputs: daily historical deposit volatility from clearing house data.

For institutions without banking crisis history → use **hypothetical scenarios** anchored to comparable jurisdictions' experiences (FSI §30).

For European banks: ECB/SSM derives from LCR; calibration historically-driven via supervisory expertise on past stress events.

---

### Approach C — Supervisor-Imposed Rates (Sector-Wide Exercises)

**Source:** FSI §22

MAS Singapore: imposes uniform rates on all D-SIBs for system-wide comparability.
ECB/SSM: applies same scenario to all banks; rates consistent over time for comparability.

**Trade-off (FSI §22):** Uniform rates enable cross-bank comparison and aggregation but may miss institution-specific risk profiles.

---

## Step 3: Scenario Conditioning — Severity Multipliers

Different scenario types require different outflow severity:

| Scenario | Retail run-off | Wholesale run-off | Key driver |
|---|---|---|---|
| Idiosyncratic (bank-specific) | Moderate → High | High → Very High | Credit downgrade, rumour, reputational event |
| Market-wide (systemic) | Low → Moderate | Moderate → High | System-wide stress; competitors equally affected |
| Combined (worst case) | High → Very High | Very High → 100% | Simultaneous idiosyncratic + systemic |

**Principle (EBA GL §157):** Design **separate** adverse behavioural assumptions for each scenario type and each time horizon — not a single set for all scenarios.

---

## Step 4: Post-2023 Adjustments (Active Gap)

**Source:** FSI §64, §71, fn.54-55

Three adjustments required post-SVB/CS (2023):

### (a) Uninsured Deposit Concentration Add-on
- Standard LCR: retail deposits treated uniformly
- Post-2023: concentration of uninsured deposits in homogeneous corporate sectors (VC, crypto, tech) creates **correlated outflows** exceeding standard retail assumptions
- Required: deposit concentration analysis by counterparty type; add-on if >X% concentration

### (b) Intraday Velocity Shock
- Historical calibrations assume outflows spread over days
- Mobile banking + real-time payments → outflows can complete within hours
- Required: separate **intraday liquidity stress** (EBA GL §155 already mandates intraday test); calibrate how much of the 30-day assumed outflow may occur on Day 1

### (c) Social Media Amplification Factor
- FSI fn.54: "deposit outflows of bank runs on some of the distressed banks exceeded the one-size-fits-all regulatory assumptions of the LCR" (citing BCBS 2023)
- No established quantitative formula yet — current practice: qualitative scenario narrative + sensitivity analysis using 2×-3× LCR run-off rates for high-profile idiosyncratic scenarios
- Some large banks have introduced caps on monthly retail transfers to limit outflow velocity (FSI fn.55)

---

## Promotion Assessment

**Ready for wiki promotion:** Partially — the framework is documented but specific multiplier tables are institution/jurisdiction-specific and not in current corpus.

**Suggested new node:** `Liquidity_Stress_Test_Nmd_Runoff_Calibration_Framework.md` (conf=3, mechanism type)

**TRUE_GAP remaining:** Specific regulator-published stress run-off rate tables (ECB/SSM 2019 LST methodology, APRA guidance) not in corpus.

**Suggested source acquisitions:**
- ECB Banking Supervision: "Liquidity stress test 2019 — Methodology and results" (ECB, 2019)
- BCBS: "Report on the 2023 banking turmoil" (d555, October 2023) — available in `02_sources`?
- EBA: ILAAP peer review reports (quantitative benchmarks for run-off rates across EU banks)
