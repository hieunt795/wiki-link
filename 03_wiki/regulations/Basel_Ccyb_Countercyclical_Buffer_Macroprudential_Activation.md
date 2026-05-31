---
node_id: basel_ccyb_countercyclical_buffer_macroprudential_activation_001
type: regulation
title: 'Basel CCyB: Countercyclical Capital Buffer — Macroprudential Activation and
  Reciprocity'
aliases:
- CCyB Basel
- countercyclical capital buffer
- bộ đệm vốn nghịch chu kỳ
- CCyB activation
- credit-to-GDP buffer
domain:
  primary: basel_risk
  secondary:
  - monetary_policy
  - macro_outlook
tags:
- ccyb
- macroprudential
- countercyclical
- credit_cycle
- capital_buffer
- reciprocity
- cet1
- basel3
confidence: 3
stability: stable
thesis: 'The CCyB (0–2.5% of RWA, met with CET1) is a national macroprudential tool
  activated when excess aggregate credit growth signals systemic risk accumulation;
  increases take effect after a pre-announcement period of up to 12 months while decreases
  are effective immediately, preventing the buffer from becoming procyclical during
  downturns; internationally active banks compute a weighted average across jurisdictions
  they lend into, and mandatory reciprocity among Basel Committee members ensures
  consistent global application up to 2.5%.

  '
source_refs:
- path: 02_sources/regulator/bcbs/BaselFramework.md
  pages: RBC30.6-17 (countercyclical buffer mechanism, activation, bank-specific calculation,
    reciprocity)
  weight: primary
parent_node: null
related:
- node: '[[Basel_Iii_Capital_Stack_Cet1_Tier1_Total_Buffer_Architecture]]'
  relation: macroprudential_extension
- node: '[[Basel_Gsib_Surcharge_Bucket_Methodology_Capital_Add_On]]'
  relation: buffer_stack_peer
- node: '[[Basel_Iii_Capital_And_Liquidity_Constraint_Mechanics]]'
  relation: constraint_system_component
- node: '[[Imf_Flow_Of_Funds_4_Sector_Consistency_Framework]]'
  relation: credit_cycle_macro_context
date_created: '2026-05-26'
date_updated: '2026-05-26'
---

## Mechanism Overview

The CCyB is a **macroprudential capital buffer** designed to ensure banks build capital in credit expansion phases that can be drawn down when credit conditions deteriorate. Unlike the minimum capital requirement and the Conservation Buffer (which are permanent structural features), the CCyB is **discretionary and time-varying** — set by national authorities based on macro-financial conditions. (RBC30.6-7)

**Core formula:**
```
CCyB = 0% to 2.5% of total RWA (credit + market + operational)
Bank-specific CCyB = Σ (jurisdictional CCyB rate_j × credit exposure weight_j)
```

The buffer must be met with **CET1 only**. When active, it extends the Capital Conservation Buffer — increasing the unrestricted distribution threshold from 7.0% (with 2.5% CConB alone) to up to **9.5% CET1** (4.5% minimum + 2.5% CConB + 2.5% CCyB). (RBC30.12)

## Activation Logic

National authorities deploy the CCyB when excess aggregate credit growth is judged to be associated with systemic risk accumulation. The credit-to-GDP gap (actual credit-to-GDP ratio vs its long-run trend) is the BCBS-endorsed **primary guide**, though not a mechanistic trigger — authorities exercise judgment based on a broader set of indicators. (RBC30.9-10)

Typical activation circumstances: [LLM]
- Credit-to-GDP gap above a threshold (typically ~2 percentage points above trend)
- Rapid expansion of specific credit categories (housing, leveraged lending)
- Compression of credit spreads and loosening of underwriting standards
- Rising property prices funded by bank credit

## Timing Asymmetry: 12-Month Up / Immediate Down

The CCyB has a deliberate **asymmetric timing structure** designed to prevent procyclicality:

| Direction | Timing | Rationale |
|---|---|---|
| **Increase** | Pre-announcement ≤12 months before effective date | Banks need time to raise capital; cannot respond instantly |
| **Decrease** | **Effective immediately** on announcement | Prevents the buffer from constraining credit supply during downturns; avoids pro-cyclical tightening |

This asymmetry is critical: when a downturn hits, the released CCyB can be used immediately — there is no waiting period. Banks may also accelerate compliance with an increase before the 12-month window if they wish. (RBC30.11)

## Bank-Specific Buffer Calculation (RBC30.12-13)

Internationally active banks compute their **portfolio-weighted CCyB** based on the geographic location of their private sector credit exposures:

```
Bank CCyB_rate = Σ (CCyB_j × w_j)
where:
  CCyB_j = CCyB rate in jurisdiction j
  w_j = share of the bank's private sector credit exposure in jurisdiction j
```

"Private sector credit exposures" = banking book exposures attracting a credit risk capital charge + trading book risk-weighted equivalents for specific risk, incremental risk, and securitisation. Interbank and public-sector exposures are **excluded**. (RBC30.13, FAQ1)

Geographic location = location of the counterparty's ultimate risk. A Vietnamese bank lending to a Hong Kong entity applies Hong Kong's CCyB rate for that exposure.

## Mandatory Reciprocity

Within Basel Committee member jurisdictions, **reciprocity is mandatory up to 2.5%**: if Jurisdiction A sets a 1.5% CCyB, all Basel-member banks worldwide with credit exposures to Jurisdiction A must hold 1.5% CCyB against those exposures, regardless of their home country's CCyB. (RBC30.11, FAQ3-5)

Above 2.5%, reciprocity is voluntary — home authorities may but need not match a host country's higher requirement.

**Purpose:** Ensures that foreign bank branches/subsidiaries cannot circumvent domestic macroprudential rules by being regulated in more lenient home jurisdictions.

## MDA Distribution Restriction

When a bank's CET1 falls within the combined buffer (CConB + CCyB + G-SIB add-on), the standard **MDA constraint mechanism** applies: the buffer is divided into four equal quartile bands, with maximum distribution ratios of 0%/20%/40%/60% of earnings for each successive quartile from the bottom. The absolute level of the buffer threshold scales, but the four-band structure is constant. (RBC30.12)

## CCyB in the Buffer Stack

The full Basel III capital requirement for a Bucket 2 G-SIB with 2.0% CCyB active:

```
4.5%  CET1 minimum
+ 2.5%  Capital Conservation Buffer  → MDA threshold at 7.0%
+ 2.0%  CCyB (if national authority activates)
+ 1.5%  G-SIB surcharge (Bucket 2)
= 10.5% total CET1 threshold for unrestricted distributions
```

This demonstrates why G-SIBs in countries with active CCyBs face structurally higher CET1 requirements well above nominal minimums.

## Related Concepts

`[[Basel_Iii_Capital_Stack_Cet1_Tier1_Total_Buffer_Architecture]]` establishes the base CET1 requirements and MDA mechanism that the CCyB extends. `[[Basel_Gsib_Surcharge_Bucket_Methodology_Capital_Add_On]]` is the other discretionary add-on that sits on top of the Conservation Buffer. The credit-to-GDP gap logic underlying CCyB activation connects to the macro accounting framework in `[[Imf_Flow_Of_Funds_4_Sector_Consistency_Framework]]`.
