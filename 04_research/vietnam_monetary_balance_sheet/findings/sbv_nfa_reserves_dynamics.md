---
finding_id: vietnam_nfa_reserves_001
topic: vietnam_monetary_balance_sheet
sub_question: SQ1, SQ3, SQ5
title: "SBV Foreign Reserves and NFA Dynamics — Two-Phase Pattern 2016-2024"
confidence: 3
status: provisional
date: "2026-05-26"
sources_used:
  - World Bank API (FI.RES.TOTL.CD, FM.AST.NFRG.CN, PA.NUS.FCRF)
  - data/2026-05-26_worldbank_monetary_data.md
framework_nodes:
  - "[[Imf_Balance_Of_Payments_Framework_And_External_Account_Analysis]]"
  - "[[Imf_Monetary_Survey_Valuation_Adjustment_Transaction_Flow_Decomposition]]"
  - "[[Imf_Exchange_Rate_Assessment_And_Crawling_Peg_Design]]"
---

## Two-Phase NFA Narrative

```
NFA CYCLE — VIETNAM BANKING SYSTEM (VND tn / USD bn)
────────────────────────────────────────────────────────
PHASE 1: ACCUMULATION (2016–2021)
  FX Reserves: $36.5 bn → $109.4 bn  (+$72.9 bn, +200%)
  NFA (VND tn): 946 → 2,688          (+1,742 tn)
  Driver: FDI boom + trade surplus (electronics, Samsung, FDI exports)
  SBV action: buy USD → inject VND → sterilize partially

  Annual reserve accumulation:
    2016→2017: +$12.6 bn (largest single-year jump pre-peak)
    2018→2019: +$22.8 bn (largest year, strong current account)
    2019→2020: +$16.5 bn (COVID year — but BoP surplus continued)
    2020→2021: +$14.6 bn → peak $109.4 bn

PHASE 2: DEFENSE (2022–2024)
  FX Reserves: $109.4 bn → $83.1 bn  (-$26.3 bn, -24%)
  NFA (VND tn): 2,688 → 2,314 (2022) → ~0 (2023, WB data gap)
  Driver: Fed tightening → dollar surge → VND pressure → SBV FX sales
  SBV action: sell USD → drain VND → defend crawling peg
────────────────────────────────────────────────────────
```

## NFA → M2 Transmission: Partial Sterilization Inference

During Phase 1 (2016-2020), SBV was accumulating reserves but M2 growth was ~13-14%/year. If full sterilization had occurred, NFA growth would have contributed 0 pp to M2. Actual NFA contribution was +3.5 to +6.7 pp annually (see monetary_survey_imf_framework.md). This implies:

**Sterilization was PARTIAL — roughly 50-60% sterilized** [LLM — inferred from residual M2 growth decomposition]

Sterilization instruments likely used (consistent with SBV operational framework):
1. T-bills / OMO bills (hút thanh khoản qua nghiệp vụ thị trường mở)
2. Deposit reserve requirements (raising RRR absorbs reserves without reversing NFA)
3. SBV certificates of deposit (chứng chỉ tiền gửi NHNN)
4. Government bond issuance absorbed by commercial banks (fiscal sterilization)

**Evidence for only partial sterilization:**
- Real interest rates remained positive throughout (2-7% real rate) — no overheating signal
- CPI stayed below 3.5% despite 14% annual M2 growth
- Velocity declined (V: 0.81 → 0.68, 2017-2021) — M2 growth outpaced spending
- Conclusion: SBV chose to allow NFA-driven monetary expansion to support growth targets; sterilization was used to prevent overheating, not to neutralize all FX inflows

## Valuation Effect 2022-2024

VND depreciated 8.5% over 2021-2024 (23,160 → 25,138 VND/USD). Apply IMF Box 5.8 formula:

```
Valuation adjustment (approximate):
  Opening NFA (end-2021): $109.4 bn (USD)
  ΔE = 25,138 − 23,160 = +1,978 VND/USD

  VAj ≈ A_$(t-1) × ΔE
       = 109.4 bn × 1,978
       = ~216 tn VND (positive — depreciation inflates VND value of USD assets)

Interpretation:
  If SBV had not sold any reserves AND VND depreciated 8.5%:
    ΔNFA (local currency) = +216 tn VND from valuation alone
  
  Actual ΔNFA (2021→2022): 2,314 − 2,688 = -374 tn VND

  Transaction component (actual sales):
    ΔNFA_transaction ≈ -374 − 216 = -590 tn VND
    In USD: ≈ -590 / 23,160 avg ≈ -$25.5 bn (consistent with reserve decline of -$22.9 bn)
```

[LLM-E: computed from WB data using IMF Box 5.8 methodology]

**Policy implication:** The NDA ceiling (if Vietnam were in an IMF program) would use ΔNFA_transaction = -590 tn VND, not the total stock change of -374 tn. Failure to adjust would make the NDA ceiling appear 216 tn VND tighter than it actually should be.

## Reserve Adequacy

IMF ARA metrics (approximate, 2022):
```
Metric                          Value         Status
────────────────────────────────────────────────────
M2 coverage (NFA/M2)            17.6%         ~OK (threshold ~10-15% for managed float)
Import months coverage          ~3.5 months   Adequate (threshold: 3 months)
  (at ~$27 bn/month imports)
Short-term external debt cover  High          Not computed (need ST debt data)
ARA composite (emerging market) ~130-140%     [LLM — estimate; above 100% = adequate]
────────────────────────────────────────────────────
```

Peak 2021 at $109 bn was excessive relative to trade needs but understandable as insurance against sudden stops and dollarization. Post-2022 drawdown to $83 bn (2024) is still adequate but declining.

**TRUE_GAP:** Short-term external debt data needed to compute full ARA composite. Vietnam's external debt was $96.6 bn (end-2017) — likely higher now. If significant short-term component, reserve adequacy ratio more binding.
