---
node_id: liquidity_stress_test_depositor_behaviour_assumptions_key_driver_001
type: concept
title: Liquidity Stress Test Depositor Behaviour Assumptions Key Driver
aliases:
- depositor behaviour
- deposit run assumptions
- deposit outflow rates
- giả định hành vi người gửi tiền
- deposit velocity digital banking
domain:
  primary: alm
tags:
- depositor_behaviour
- liquidity_stress_testing
- svb
- digital_banking
- fsi
- '2023'
confidence: 3
stability: evolving
thesis: 'BIS FSI Insights No.59 §13, §33, §64, §71: depositor behaviour assumptions
  are the most uncertain input in LST — expressed as run-off rates on funding sources.
  Three calibration approaches coexist: (1) LCR-derived floor — ECB/SSM and SCB
  use bcbs238 rates as minimum; ILAAP exercises may apply higher rates (FSI fn.25);
  (2) historical stress data — BCB uses 30-day VaR at 95% confidence on deposit
  volatility; hypothetical scenarios supplement where historical data is scarce (§30);
  (3) supervisor-imposed fixed rates — MAS applies same rates to all D-SIBs for
  comparability (§22). Post-2023 banking turmoil (SVB, Credit Suisse): three structural
  challenges identified — (a) uninsured large deposit concentration risk: similar
  corporate profiles run together (VC/crypto March 2023); (b) digital banking accelerates
  outflow intraday — mobile transfers eliminate the "bank run queue" that absorbed
  time in historical crises; (c) social media amplification raises effective run-off
  rates above LCR floors. The retail/wholesale hierarchy (retail less flighty) may
  not hold post-digitisation (§64, fn.54-55).'
source_refs:
- path: 02_sources/regulator/bcbs/insights59.md
  pages: '§13, §22, §30, §33, §34, §64, §71; fn.25, fn.54, fn.55'
  weight: primary
- path: 02_sources/regulator/bcbs/bcbs238 - Basel III The Liquidity Coverage Ratio and liquidity risk monitoring tools.md
  pages: '§73-84 (retail floors), §87-104 (wholesale floors)'
  weight: secondary
parent_node: null
related:
- nmd_decay_model_volume_segmentation_001
- lcr_retail_deposit_run_off_rates_stable_less_stable_categories_001
- lcr_wholesale_unsecured_funding_run_off_by_counterparty_type_001
- liquidity_stress_test_three_building_blocks_assets_liabilities_management_response_001
date_created: '2026-05-27'
date_updated: '2026-05-29'
---

## Three Types of Behavioural Assumptions (FSI §13)

LST behavioural assumptions cover three distinct categories:

1. **Run-off rates** — stability of funding sources: how much of each deposit/funding type leaves in stress
2. **Haircuts** — price volatility of marketable assets under fire-sale conditions
3. **Draw probabilities** — contingent liquidity: probability of drawdown on committed credit/liquidity lines

Run-off rates for deposits are the most uncertain and the most consequential for overall LST outcome.

---

## Calibration Methodology: Three Approaches in Practice

### ① LCR-Derived Floor (ECB/SSM, SCB/Riksbank)

**Source:** FSI §33, fn.25

- ECB/SSM and SCB derive run-off rates from bcbs238 LCR parameters as the starting point
- ILAAP and sector-wide stress tests may apply **higher rates** than LCR floors — LCR sets minimum regulatory requirements, not stress test severity (fn.25)
- Retail sight deposits: preset conservative assumption (some withdrawal assumed at stress onset) — higher than bcbs238 5%/3% stable floor
- Term deposits with contractual maturity >30 days: replacement coefficient applied, lower for "flightier" funding (FI deposits vs commercial deposits)

**Key insight:** LCR run-off rates ≠ stress test run-off rates. LCR is a minimum standard; ILAAP scenarios must be institution-specific and can be materially more severe.

---

### ② Historical Stress Data + VaR (BCB/Brazil)

**Source:** FSI §30, §238 (Table 4)

- BCB uses **historical market data** for scenario design where historical crises exist
- Deposit outflows modeled using **VaR methodology**: 30-day (or 21-business-day) holding period at **95% confidence level**
- Add-ons applied for early redemption from the **3 largest wholesale counterparties** of each bank
- Hypothetical features used where historical data insufficient (no Brazilian banking crisis recently)

---

### ③ Supervisor-Imposed Fixed Rates (MAS Singapore)

**Source:** FSI §22

- MAS requires all D-SIBs to use the **same scenario and same assumptions** — including deposit run-off rates
- Rationale: Singapore D-SIBs have similar enough risk profiles that uniform assumptions enable meaningful cross-bank comparison and system-wide aggregation
- Rates: at least as restrictive as LCR parameters; may be more restrictive
- MAS also runs a **parallel top-down exercise** using banks' submitted LCR/cash flow data to cross-check that banks are not underestimating liquidity needs

---

## Post-2023 Banking Turmoil: Three Structural Challenges

**Source:** FSI §64, §71, fn.54, fn.55

### (a) Uninsured Deposit Concentration Risk (SVB/March 2023)
- SVB concentrated deposits in VC/crypto corporates — similar business profiles → correlated outflows
- Assumption that retail deposits are always less flighty than wholesale **may not hold** when retail accounts are concentrated in a homogeneous group
- FSI §64: "Authorities may also want to verify that behavioural assumptions that lead to the classification of retail deposits as less flighty than wholesale ones hold up"

### (b) Digital Banking → Intraday Outflow Velocity
- Mobile apps enable transfers in seconds; the "bank run queue" of the Northern Rock era is gone
- FSI §71: "social media in spreading information and technology in allowing for continuous transactions make deposits flightier"
- FSI fn.55: "Financial technology makes it possible to transfer deposits and open/close accounts in a few clicks online; combined with social media, this may substantially increase run-off rates"
- Implication: stress tests must model **intraday outflow velocity**, not just 30-day cumulative flows

### (c) Social Media Amplification
- FSI fn.54 / BCBS (2023): deposit outflows at distressed banks (SVB, CS) **exceeded LCR regulatory assumptions** — one-size-fits-all floors insufficient
- Rumour spreads instantly; bank's reputation can deteriorate in hours, not days
- Historical calibration based on pre-social-media episodes systematically underestimates modern run speed

---

## IRRBB NMD Model vs Stress Outflow Rate: The Gap

The standard NMD behavioral model (decay model, stochastic 3-factor, replicating portfolio) estimates:
- **Average life** of deposits under normal conditions
- **Repricing sensitivity** of balances to rate changes (for IRRBB EVE/NII)

These are **not directly usable** as stress outflow rates because:
- Normal-condition behavioral assumptions assume no crisis sentiment
- Decay model captures attrition over years, not acute 30-day outflows
- Stress calibration requires explicit scenario-conditioning: what % leaves in *idiosyncratic* vs *combined* scenario?

**Bridge approach (best practice):**
```
IRRBB decay model → stable core / volatile layer segmentation (normal conditions)
                  ↓ apply stress multiplier per scenario type
Stress outflow rate = volatile layer × scenario severity factor
                    + portion of core layer (idiosyncratic: higher; market-wide: lower)
```
Stress multipliers are calibrated from: (1) LCR floors as lower bound; (2) historical crises; (3) supervisor challenge in SREP dialogue.

