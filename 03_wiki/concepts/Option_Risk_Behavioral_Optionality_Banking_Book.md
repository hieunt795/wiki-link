---
node_id: option_risk_behavioral_optionality_banking_book_001
type: concept
title: Option Risk and Behavioral Optionality in the Banking Book
aliases:
- option risk IRRBB
- behavioral optionality
- embedded options banking
- automatic options banking
- rủi ro quyền chọn trong sổ ngân hàng
- quyền chọn hành vi
domain:
  primary: alm
  secondary:
  - basel_risk
tags:
- option_risk
- behavioral_options
- embedded_options
- prepayment
- NMD
- IRRBB
- interest_rate_risk
confidence: 1
stability: stable
thesis: '[LLM] Option risk in the banking book arises from both explicit (automatic)
  options with rule-based exercise and behavioral (embedded) options where customer
  actions depend on economic and non-economic factors; both alter the timing and amount
  of cashflows on bank instruments, creating EVE and NII exposures that cannot be
  fully hedged with standard financial options.

  '
source_refs:
- path: 02_sources/books/tata_bank_alm/Tata_Bank_ALM_2025.md
  pages: Ch 1, section 1.2.2.3; Ch 2, sections 2.4.2–2.4.3; Ch 3, sections 3.3 and
    3.6
  weight: primary
parent_node: '[[Irrbb_Eve_Nii_Dual_Metric_Framework]]'
related:
- node: '[[Behavioralization_Non_Maturity_Deposit_Alm_Prepayment_Early_Withdrawal_Modeling]]'
  relation: related_to
- node: '[[Non_Maturity_Deposit_Fair_Margin_And_Replicating_Portfolio]]'
  relation: related_to
- node: '[[Irrbb_Eve_Nii_Dual_Metric_Framework]]'
  relation: component_of
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## EBA Definition

Interest rate option risk (EBA/GL/2022/14): "Risk arising from options (embedded and explicit), where the institution or its customer can alter the level and timing of their cash flows, namely the risk arising from interest rate sensitive instruments where the holder will almost certainly exercise the option if it is in their financial interest to do so (embedded or explicit automatic options) and the risk arising from flexibility embedded implicitly or within the terms of interest rate sensitive instruments, such that changes in interest rates may affect a change in the behaviour of the client (embedded behavioural option risk)."

## Two Types of Option Risk

### Automatic (Rule-Based) Options

[LLM] Automatic options execute mechanically based on contractual terms and prevailing market rates. Standard examples:

- **Interest rate caps** on floating-rate loans: when market rates exceed the cap, the customer's interest expense is capped — equivalent to the bank being short a call on rates.
- **Interest rate floors** on deposit accounts: when market rates go below the floor (e.g., 0%), the bank cannot pass through negative rates — equivalent to the bank being short a put on rates.
- **Swaptions** and other explicit derivatives sold to corporate customers.

[LLM] Automatic options are relatively straightforward to value using standard option pricing models and can be hedged with traded options, though the hedges are imperfect for banking book positions with amortizing notionals.

### Behavioral (Embedded) Options

[LLM] Behavioral options give customers the right to alter cashflows based on personal circumstances, not purely on whether the option is in-the-money. Key examples:

- **Prepayment option** on mortgages: customers may repay early due to relocation, divorce, or refinancing; some prepayment occurs even when the in-force rate is below current market rates (irrational exercise from the bank's perspective). [LLM] The bank is short this option; prepayment risk is the risk that customers repay early in a low-rate environment, forcing reinvestment at lower yields.

- **Deposit redemption option** on sight deposits: customers can withdraw at any time without penalty. [LLM] The contractual maturity is zero, but behavioral analysis typically assigns a maturity of 1–5 years based on observed withdrawal patterns.

- **Early withdrawal of term deposits**: customers may break term deposits before maturity even when subject to penalties, particularly when market alternatives offer significantly higher rates.

- **Overdraft drawdown option**: the bank has committed to provide liquidity but cannot predict drawdown timing.

- **Default option**: extreme case — the borrower's bankruptcy can be modeled as a put option on the asset value.

[LLM] Behavioral options cannot be fully hedged with standard traded options because their exercise is driven partly by non-financial events (death, divorce, job change) and partly by rational rate comparison. The bank is both short and long optionality depending on the product: short the prepayment option on mortgages, but long the administered-rate option on deposit accounts (right to set rates at its own discretion).

## Interest Rate Dependence

[LLM] In a rising rate environment, fixed-rate mortgage prepayment slows (customers hold on to below-market rates), extending asset duration and increasing EVE sensitivity. Floating-rate borrowers may accelerate prepayment to reduce their cost of debt. [LLM] In a falling rate environment, mortgage prepayment accelerates (refinancing at lower rates), compressing the bank's interest income from the replacement mortgage at lower rates — a classic "negative convexity" effect.

[LLM] Deposit behavior also changes with rates: as observed in 2022–2023, a rapid rise in market rates caused European bank customers to shift from sight deposits (paying near zero) into term deposits and money market alternatives with higher yields, reducing the stable funding base and shortening the effective duration of deposits.

## 0% Floor as Embedded Option

[LLM] In a negative interest rate environment, the inability of banks to charge retail depositors negative rates creates a 0% floor that behaves as an embedded option. Two floor types exist:

- **Coupon floor**: The customer's actual deposit rate cannot fall below 0%, regardless of the reference rate. The bank cannot pass negative indicator rates to retail depositors.
- **Indicator floor**: The reference rate used to calculate the deposit rate is floored at 0%, but the margin above the floor is preserved. This protects the bank's margin when indicator rates go negative.

[LLM] The value of these floors increases as market rates fall, making them an important source of asymmetric risk for deposit-heavy retail banks during NIRP periods.

## Regulatory Requirements

[LLM] EBA guidelines require banks to: (1) maintain an inventory of all instruments with explicit or embedded options, distinguishing automatic from behavioral options; (2) make behavioral assumptions about prepayment, early withdrawal, and deposit run-off rates based on historical data; (3) apply a maximum behavioral repricing date of 5 years for non-maturity deposits (NMDs); (4) report behavioral modeling parameters (pass-through rates, core volume designations, prepayment rates) in supervisory templates under Commission Implementing Regulation 2024/855.

## Model Risk

[LLM] Behavioral option modeling carries significant model risk: data from negative interest rate environments is not reliable for calibrating models in positive rate environments and vice versa. SVB's failure illustrated the consequence of unsubstantiated behavioral assumptions — extending deposit duration assumptions without supporting data, effectively hiding interest rate risk from reported metrics rather than removing it from the balance sheet.
