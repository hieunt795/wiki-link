---
node_id: irrbb_interest_rate_risk_types_classification_001
type: concept
title: "IRRBB Interest Rate Risk Types Classification"
aliases:
  - interest rate gap risk
  - basis risk
  - yield curve risk
  - IRRBB risk types
  - phân loại rủi ro lãi suất
  - rủi ro tái định giá
  - rủi ro cơ sở

domain:
  primary: alm
  secondary:
    - basel_risk
tags:
  - IRRBB
  - gap_risk
  - basis_risk
  - option_risk
  - CSRBB
  - interest_rate_risk

confidence: 1
stability: stable

thesis: >
  [LLM] IRRBB comprises three distinct sub-risks — gap (repricing) risk from maturity mismatches, basis risk from different rate indices, and option risk from explicit and behavioral optionality — each requiring separate identification and quantification under EBA guidelines; credit spread risk (CSRBB) is closely related but treated separately under EBA/GL/2022/14.

source_refs:
  - path: 02_sources/books/tata_bank_alm/Tata_Bank_ALM_2025.md
    pages: "Ch 1, sections 1.2.2.1–1.2.2.5"
    weight: primary

related:
  - node: "[[Repricing_Gap_Analysis_Nii_Eve_Impact]]"
    relation: related_to
  - node: "[[Option_Risk_Behavioral_Optionality_Banking_Book]]"
    relation: related_to
  - node: "[[Irrbb_Eve_Nii_Dual_Metric_Framework]]"
    relation: component_of

date_created: "2026-05-28"
date_updated: "2026-05-28"
---

## IRRBB Definition

Interest rate risk arising from the banking book (IRRBB) is defined by EBA (EBA/GL/2022/14) as: "The current and prospective risk of a negative impact to the institution's economic value of equity, or to the institution's net interest income, taking market value changes into account as appropriate, which arise from adverse movements in interest rates affecting interest rate sensitive instruments, including gap risk, basis risk and option risk."

[LLM] IRRBB arises from the core banking function of maturity transformation — taking short-term deposits and deploying them as longer-term loans — creating inherent mismatches between the repricing characteristics of assets and liabilities.

## Type 1: Interest Rate Gap Risk (Repricing Risk / Yield Curve Risk)

EBA definition: "Risk resulting from the term structure of interest rate sensitive instruments that arises from differences in the timing of their rate changes, covering changes to the term structure of interest rates occurring consistently across the yield curve (parallel risk) or differentially by period (non-parallel risk)."

[LLM] Gap risk manifests when assets and liabilities reprice at different times. The bank's NII and EVE change because rate-sensitive positions on one side of the balance sheet reprice before matching positions on the other side.

*Illustrative example*: An asset reprices based on 6-month EURIBOR in August; an otherwise comparable liability reprices based on 6-month EURIBOR in June. A rate rise in May immediately affects the liability (repriced in June) while the asset continues at the old rate until August. The bank faces a temporary margin compression despite both instruments being linked to the same index.

[LLM] Gap risk encompasses both parallel yield curve risk (all maturities move equally) and non-parallel risk (yield curve steepening, flattening, short-rate or long-rate shocks). The six EBA supervisory shock scenarios capture both forms: parallel up, parallel down, steepener, flattener, short rates up, short rates down.

## Type 2: Interest Rate Basis Risk

EBA definition: "Risk arising from the impact of relative changes in interest rates on interest rate sensitive instruments that have similar tenors but are priced using different interest rate indices. Basis risk arises from the imperfect correlation in the adjustment of the rates earned and paid on different interest rate sensitive instruments with otherwise similar rate change characteristics."

[LLM] Basis risk arises when assets and liabilities are linked to different rate benchmarks that do not move in perfect lockstep. Common bases include: IBOR rates (EURIBOR, LIBOR), overnight index swaps (OIS), risk-free rates (eSTR, SOFR), and repo rates.

*Illustrative example*: An asset reprices based on 6-month EURIBOR; a liability reprices based on 1-month EURIBOR, both in June. Even though both reset on the same date, a EURIBOR move in May may affect the 1-month rate differently from the 6-month rate. If 1-month EURIBOR rises from 4% to 6% while 6-month EURIBOR rises only from 4% to 5%, the liability reprices to 6% while the asset reprices to 5%, generating a 100 bp negative margin swing.

[LLM] EBA requires banks to identify basis risk by inventorying instrument groups based on different interest rate indices and focusing on derivative hedges that create basis exposures.

## Type 3: Interest Rate Option Risk

EBA definition: "Risk arising from options (embedded and explicit), where the institution or its customer can alter the level and timing of their cash flows."

[LLM] Option risk is subdivided into automatic options (rule-based, exercise when in-the-money — caps, floors, swaptions) and behavioral options (exercise depends partly on non-financial factors — prepayment, early withdrawal, deposit run-off). [LLM] See dedicated node on Option Risk and Behavioral Optionality in the Banking Book for full mechanics.

## Type 4: Credit Spread Risk (CSRBB) — Related but Separate

EBA definition: "Risk driven by changes of the market price for credit risk, for liquidity and for potentially other characteristics of credit-risky instruments, which is not captured by another existing prudential framework such as IRRBB or by expected credit / (jump-to-) default risk."

[LLM] CSRBB captures mark-to-market losses on banking book positions when credit spreads widen, even without a change in general interest rate levels. Example: a bank holds callable liabilities; even if general rates are unchanged, a deterioration in the bank's credit quality forces call buyers to exercise, requiring the bank to refinance at higher credit spreads.

[LLM] CSRBB is explicitly included in EBA/GL/2022/14 (2022 update), which extended the previous IRRBB framework to cover credit spread risk in the banking book. This was a major new addition compared to EBA/GL/2018/02.

## Type 5: Liquidity Risk — Adjacent but Separate

[LLM] Liquidity risk (the inability to fund or liquidate positions at reasonable cost) is closely related to IRRBB but treated under a separate framework (LCR, NSFR). Interest rate simulations for gap, basis, and option risk shift general yields and do not include entity-specific or instrument-specific liquidity spreads. However, rising interest rates can trigger deposit outflows that create funding liquidity risk — the SVB failure being the archetypal example.

## EBA Identification Requirements

[LLM] EBA guidelines require institutions to identify all five risk types and to implement quantitative tools for gap risk (repricing gap or duration gap analysis), basis risk (inventory of different rate indices used in the portfolio), and option risk (inventory of automatic and behavioral options with behavioral assumptions). Measurement frequency must be at least quarterly, and more often in periods of elevated rate volatility.
