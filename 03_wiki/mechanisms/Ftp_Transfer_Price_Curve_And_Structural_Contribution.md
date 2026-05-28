---
node_id: ftp_transfer_price_curve_and_structural_contribution_001
type: mechanism
title: "FTP Transfer Price Curve and Structural Contribution"
aliases:
  - funds transfer pricing
  - FTP curve
  - transfer price curve
  - cost of funds curve
  - structural contribution
  - định giá chuyển giao vốn
  - đường cong giá chuyển giao

domain:
  primary: alm
  secondary:
    - financial_markets
tags:
  - FTP
  - transfer_pricing
  - NIM
  - liquidity_risk
  - interest_rate_risk
  - IRRBB
  - treasury

confidence: 1
stability: stable

thesis: >
  [LLM] Funds Transfer Pricing (FTP) is an internal bank process that assigns a maturity-matched funding rate to each asset and an earning rate to each liability, using the transfer price curve; FTP decomposes net interest margin into business-unit contributions and centralizes interest rate and liquidity risk in treasury, which earns the "structural contribution" — the spread between the liability FTP rate and the asset FTP rate reflecting the term premium and liquidity premium.

source_refs:
  - path: 02_sources/books/tata_bank_alm/Tata_Bank_ALM_2025.md
    pages: "Ch 2, sections 2.3.1–2.3.11"
    weight: primary

related:
  - node: "[[Non_Maturity_Deposit_Fair_Margin_And_Replicating_Portfolio]]"
    relation: related_to
  - node: "[[Behavioralization_Non_Maturity_Deposit_Alm_Prepayment_Early_Withdrawal_Modeling]]"
    relation: related_to
  - node: "[[Bank_Alm_Banking_Book_Risk_Management_Framework]]"
    relation: component_of

date_created: "2026-05-28"
date_updated: "2026-05-28"
---

## Purpose of FTP

[LLM] FTP serves three interrelated functions in bank ALM:

1. **Internal NIM allocation**: Splits the bank-wide net interest margin (NIM) into contribution margins for each business unit based on the opportunity cost of the funds they originate. [LLM] The customer deposit department earns the spread between the customer deposit rate and the FTP rate; the customer lending department earns the spread between the lending rate and the FTP rate; treasury captures the structural contribution.

2. **Risk centralization**: All interest rate and liquidity risk is transferred to treasury at the FTP rate, allowing business units to focus on customer margin without managing duration or funding risk. [LLM] Without FTP, cross-subsidization between business units can occur, incentivizing excessive risk-taking (moral hazard) or adverse selection.

3. **Balance sheet steering**: FTP rates can be adjusted to incentivize or discourage specific types of customer business. Lowering the FTP curve makes lending more attractive to the lending department (higher margin) and deposits less attractive (lower margin), encouraging loan growth. [LLM] This steering function is inherently political: small changes in FTP assumptions can dramatically shift apparent profitability across business units.

## Transfer Price Curve Construction

[LLM] In the matched maturity method, each position is assigned an FTP rate corresponding to the maturity of that position. The set of rates for all maturities constitutes the transfer price curve (also called the cost of funds curve).

[LLM] The FTP curve is decomposed into two components:
- **Pure interest rate risk curve**: A nearly risk-free yield curve representing the time value of money without institution-specific credit risk. Candidates include AAA-rated euro-area government bond yields, eSTR-based OIS curves, repo rates, or the EURIBOR swap curve. Each has advantages and limitations (EURIBOR incorporates interbank credit risk; eSTR lacks a forward-looking term structure; repo markets are short-dated).
- **Funding spread (liquidity premium)**: The institution-specific spread over the risk-free curve, reflecting the bank's own funding cost. [LLM] This is calibrated by observing the bank's actual market funding rates — for example, if 2-year fixed notes price at 3% and the 2-year risk-free rate is 2.2%, the liquidity premium is 80 bps.

[LLM] Separating the FTP curve into these two components is especially useful for instruments where the reference rate tenor differs from the contractual maturity. Example: a 2-year loan that resets annually uses a 1-year rate for interest rate risk but requires 2-year funding — the FTP rate = 1-year interest rate risk component + 2-year liquidity premium.

## Structural Contribution

[LLM] The structural contribution is the compensation treasury earns for assuming two risks simultaneously: liquidity (refinancing) risk and interest rate risk arising from maturity transformation. [LLM] In the example where a 2-year loan is funded by a 1-year deposit: at year-end, the deposit must be rolled (liquidity risk); if rates rise in year 2, the rolled deposit costs more (interest rate risk). The structural contribution = FTP rate on the 2-year asset minus FTP rate on the 1-year liability = the slope of the FTP curve between 1 and 2 years.

## Regulatory Costs in the FTP Curve

[LLM] Post-GFC regulation adds mandatory cost components to the FTP curve for positions that trigger regulatory requirements:

- **LCR cost**: Positions requiring additional HQLA buffers should be charged the incremental cost of holding those buffers. Failure to include LCR costs causes new business to systematically undermine the bank's liquidity ratio without compensation.
- **NSFR cost**: Positions that require stable funding should bear the cost of that funding (longer-dated, more expensive debt). Derivative positions may not need direct funding but can worsen NSFR metrics, requiring adjustment.
- **Clearing/margin cost**: Centrally cleared OTC derivatives require initial and variation margin; the funding cost of margin should be reflected in FTP.
- **Optionality premium**: Short optionality (e.g., prepayable customer loans, withdrawable deposits) should be charged an option premium in the FTP rate; long optionality (callable bonds issued by the bank) earns a discount.

## Multi-Currency FTP

[LLM] For foreign-currency positions, the FTP curve can be extended using cross-currency swap basis adjustments observed in the cross-currency swap market. A centralized ALM desk in one currency jurisdiction prices non-base-currency positions by applying the relevant cross-currency basis to its domestic FTP curve.

## FTP and Model Risk

[LLM] Schäfer et al. (2017) note that a significant portion of NII in interest-bearing businesses is driven not by actual client margins but by internal models — particularly behavioral maturity assumptions for sight deposits and the rate applied to calculate capital benefit. Changing the behavioral maturity assumption for a corporate sight deposit portfolio can shift apparent NII significantly without any change to real economic relationships. [LLM] This makes FTP assumptions a major source of model risk and a frequent subject of internal political pressure from business unit managers.
