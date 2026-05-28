---
node_id: reserve_asset_management_hqla_portfolio_bank_001
type: concept
title: "Reserve Asset Management: Bank HQLA Portfolio Strategy"
aliases:
  - Liquidity reserve
  - Liquid asset buffer
  - Reserve asset portfolio
  - Quản lý tài sản dự trữ thanh khoản
  - Danh mục tài sản thanh khoản cao

domain:
  primary: alm
  secondary:
    - basel_risk
tags:
  - hqla
  - liquidity_reserve
  - reserve_assets
  - lcr
  - sovereign_bonds
  - basis_risk
  - credit_risk

confidence: 1
stability: stable

thesis: >
  [LLM] A bank's liquidity reserve (HQLA portfolio) must be funded long-term on the liability side despite holding short-to-medium-maturity sovereign bonds on the asset side — creating an intentional negative maturity transformation whose cost functions as an insurance premium. [LLM] Active management of this portfolio involves navigating three embedded risks: basis risk (Euribor tenor mismatch), credit spread risk (sovereign and non-sovereign spread movements), and the liquidity black-hole risk that arises when all banks hold identical collateral and try to sell simultaneously.

source_refs:
  - path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
    pages: "Ch 15 — Managing Reserve Assets (Commerzbank AG)"
    weight: primary

related:
  - node: "[[Funding_Gap_Profile_And_Behavioural_Maturity_Calendar]]"
    relation: related_to
  - node: "[[Asset_Encumbrance_Management_Bank_Alm]]"
    relation: related_to
  - node: "[[Bank_Alm_Structural_Liquidity_Management_Nsfr_Lcr_Framework]]"
    relation: component_of

date_created: "2026-05-28"
date_updated: "2026-05-28"
---

## Purpose and Core Concept

[LLM] The liquidity reserve (also called "liquid asset buffer", "liquidity portfolio" or "portfolio of reserve assets") exists to generate **crisis liquidity** — cash that can be mobilised quickly under an idiosyncratic or market-wide stress without requiring extraordinary central bank intervention. Its size is calibrated to the largest cumulative funding gap revealed by stress tests.

The fundamental trade-off: shorter-maturity, more-liquid assets produce lower yields; longer-maturity assets produce better carry but reduced liquidity. Liquidation value and liquidation time frame are negatively correlated.

## Asset Composition Criteria

Eligible assets for the HQLA/reserve portfolio, in order of liquidity quality:
1. Cash and central bank reserves (benchmark; zero risk, but at negative ECB deposit rate, potentially the highest-yielding option post-2014)
2. Level 1 HQLA: sovereign bonds of the bank's home country — the benchmark for return calculation (e.g., German Bunds for German banks)
3. Level 2A HQLA: other EU sovereign debt, agencies, covered bonds rated AA– or above (15% LCR haircut)
4. Level 2B HQLA: lower-rated covered bonds, equities in main indexes, RMBS (25%–50% haircut)
5. Central-bank-eligible but non-HQLA: assets usable for repo with the central bank under its standard operations

[LLM] The portfolio composition is largely a **passive management strategy** constrained by regulation. The benchmark is always the bank's home sovereign. Portfolio maturity limits (e.g., a maximum of 2–5–10 years) are set by risk management to limit duration and ensure assets remain liquid.

## Funding Strategy for the Reserve Portfolio

[LLM] Paradoxically, the HQLA portfolio must be **funded long-term** even though it holds mostly short-to-medium-dated assets. This creates a deliberate negative maturity transformation. The rationale: in a stress event, both unsecured interbank markets and repo markets dry up simultaneously. If the reserve portfolio is repo-funded, the bank gets no net crisis liquidity from it (selling the bond repays the repo). Only long-term liabilities (senior unsecured bonds, subordinated debt, stable deposits) genuinely back the portfolio with permanent funding.

The negative carry of funding the reserve long-term while holding low-yielding sovereign bonds is treated as an **insurance premium** for surviving a stress period long enough to restructure the funding base.

## Managing Basis Risk

[LLM] A key operational risk in the reserve portfolio is basis risk arising from the mismatch between the reference rate on the asset (typically 6-month Euribor on asset swap packages) and the funding reference rate (typically 3-month Euribor via the internal transfer price curve).

This 3×6 Euribor basis spread risk is actively managed using basis swaps. If the portfolio receives 6M Euribor on assets but pays 3M Euribor on funding, a widening of the 3×6 spread benefits the portfolio; a tightening costs. An overlay hedge using 3×6 basis swaps can stabilise the carry. Similarly, when reverse repos are included, an Eonia-Euribor spread risk arises and can be hedged with Eonia swap overlays or FRAs.

Rule: [LLM] outright interest rate risk must not be deliberately taken in the reserve portfolio; the only acceptable residual risk is basis risk.

## Managing Credit Risk

[LLM] Credit risk in a sovereign bond portfolio is managed on a **relative value** basis rather than by outright CDS hedges (which are expensive given negative asset-swap spreads on high-quality sovereigns). Risk management sets country limits (covering both public and private issuers in a country) with sub-limits for the reserve portfolio.

The incremental credit spread over the home-sovereign benchmark must compensate for:
1. Additional credit risk (as measured by the internal model)
2. Additional capital charges

[LLM] Post-financial-crisis experience showed that diversifying across eurozone sovereigns to earn a spread (e.g., Italian BTPs over German Bunds) introduced material sovereign credit risk that did not qualify as "risk-free". The standard practice shifted back toward home-sovereign concentration.

## Liquidity Measurement Metrics

Direct measures of asset liquidity:
- Bid-ask spread
- Non-default component (NDC) of the asset-swap spread (measuring the non-credit part of the spread, i.e., the pure liquidity premium)

Indirect proxies:
- Age and tenor (shorter maturities are more liquid)
- Issue and trading volume
- Price volatility

## Post-Crisis Market Challenges (Euro Area)

[LLM] ECB asset purchase programmes (APP, QE from 2015) compressed sovereign spreads to near zero and crowded out private investors. Reserve portfolio managers faced a shrinking investable universe. Data point: the share of cash in euro-area bank liquidity reserves rose from 31.4% (June 2011) to 38.5% (September 2016), while government debt fell from 55.0% to 41.5%, as government bonds yielded less than the ECB deposit rate (itself negative from June 2014). Banks responded by swapping excess euro liquidity into higher-yielding currencies (JPY, CHF) to buy short-dated foreign sovereigns.

## Sizing

[LLM] The size of the reserve portfolio is determined by the stress scenario that produces the largest net cumulative funding gap. The inverse relationship holds: the more wholesale-funded the bank, the larger the required reserve. A longer target survival period also requires a larger buffer.
