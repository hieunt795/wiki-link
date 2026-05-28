---
node_id: funding_gap_profile_behavioural_maturity_calendar_001
type: mechanism
title: "Funding Gap Profile and Behavioural Maturity Calendar in ALM"
aliases:
  - Liquidity gap profile
  - Behavioural maturity calendar
  - Contractual maturity calendar
  - Funding mismatch profile
  - Hồ sơ khoảng cách thanh khoản
  - Lịch đáo hạn hành vi

domain:
  primary: alm
tags:
  - liquidity_risk
  - maturity_transformation
  - behavioural_modelling
  - funding_gap
  - alm

confidence: 1
stability: stable

thesis: >
  [LLM] A bank's true liquidity risk cannot be read from contractual maturities alone; the behavioural maturity calendar — which incorporates modelled client behaviour for deposits, mortgages, and credit lines — reveals the actual cumulative funding gap that ALM must manage. [LLM] Short-term and structural liquidity management are distinct layers: the former handles daily cash positions and intraday collateral, while the latter uses the behavioural calendar to drive long-term wholesale funding decisions.

source_refs:
  - path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
    pages: "Ch 14 — Measuring and Managing Liquidity and Funding Risk (ABN AMRO)"
    weight: primary

related:
  - node: "[[Bank_Alm_Structural_Liquidity_Management_Nsfr_Lcr_Framework]]"
    relation: mechanism_of
  - node: "[[Reserve_Asset_Management_Hqla_Portfolio_Bank]]"
    relation: related_to

date_created: "2026-05-28"
date_updated: "2026-05-28"
---

## Core Mechanism

[LLM] Banks face funding liquidity risk because their assets and liabilities rarely mature at the same time. The standard analytical tool is the **liquidity gap profile** (also called the contractual maturity calendar), which maps all contractual cash inflows and outflows into time buckets (overnight, 1 week, 1 month, 3 months, 1 year, 5 years, 10+ years).

A raw contractual gap is almost always misleading. Demand deposits appear to mature overnight, yet in practice only a fraction flows out on any given day. Mortgages appear to mature in 30 years, yet prepayment rates (driven by client mobility, interest rate incentives, and macroeconomic conditions) shorten the average life substantially — often to 10 years for typical European mortgage portfolios.

## Two Calendar Types

**Contractual maturity calendar:** Distributes all balance-sheet items to buckets strictly by legal maturity. [LLM] This will almost always show a large net short position in short-term buckets (demand deposits concentrated overnight) and a large net long position in long-dated buckets (mortgages at 30 years). By itself, it overstates funding risk.

**Behavioural maturity calendar:** Replaces contractual assumptions with modelled client behaviour. Key behavioural adjustments include:

- **Non-maturing savings and current accounts:** Rather than assigning 100% of demand deposit balances to the overnight bucket, the bank models a stable "core" that remains in the deposit base for months to years. Drivers include client type (retail vs corporate), deposit size, sales channel (internet-only vs branch), and whether the deposit is covered by a deposit guarantee scheme.
- **Residential mortgages:** Prepayment models estimate when clients will repay early (moving, refinancing). A macroeconomic sensitivity layer captures the effect of rate levels (low rates trigger refinancing waves) and unemployment on prepayment speed.
- **Term loans:** Many short-maturity corporate term loans are rolled over; the behavioural model assigns rollover probability based on creditworthiness and historical patterns.
- **Non-maturing assets (overdrafts, credit cards, revolving credits):** The bank must model both when these are repaid and the risk that undrawn portions are drawn down under stress.
- **Collateral:** Derivatives portfolios create contingent liquidity demands from margin calls when market values move adversely.

## Three Balance-Sheet Views

1. **Run-off profile:** Starting from the current balance sheet, estimating expected cashflows with no new business. Useful as the base case for liquidity stress analysis.
2. **Static balance sheet:** Assumes all maturing items are replaced at same size and characteristics. Used for solvency stress testing (e.g., EBA methodology).
3. **Dynamic balance sheet:** Incorporates business forecasts, new origination, and growth plans. Used in full capital planning.

## Short-Term vs Structural Liquidity Management

[LLM] The chapter distinguishes two operational layers:

**Short-term (daily) liquidity management** handled by treasury:
- Morning cash position management across currencies
- Intraday collateral at central banks (covering minimum settlement buffer)
- Nostro position management with correspondent banks
- Issuance of commercial paper or short-term interbank deposits to cover residual gaps

**Structural (long-term) liquidity management** driven by the behavioural calendar:
- The funding plan is built from the cumulative net long-term gap revealed by the behavioural calendar
- Long-dated instruments (covered bonds, senior unsecured, NSFR-eligible deposits) are sized to close this gap
- Cross-currency swaps manage currency-specific mismatches

## Liquidity-Generating Capacity

[LLM] The size of the HQLA/liquid asset portfolio is calibrated to the stress scenario that produces the worst net cumulative outflow. The composition criteria for eligible assets include: bid-offer spreads, traded volumes, central bank eligibility, and LCR classification (Level 1 vs Level 2A vs Level 2B). A minimum cash cushion is required to cover the first days of stress before repo or bond sales can settle.

## Intraday Liquidity

[LLM] BCBS 248 introduced monitoring tools for intraday liquidity. Banks must track scheduled inflows and outflows intraday across time zones, maintain an unencumbered buffer at payment systems to avoid failing settlement obligations, and report maximum intraday liquidity usage.
