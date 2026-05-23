---
node_id: endogenous_bank_money_loans_create_deposits_001
type: mechanism
title: Endogenous Bank Money Creation Loans Create Deposits
aliases:
- endogenous money
- loans create deposits
- banks don't lend reserves
- credit creation mechanism
- money multiplier myth
- tín dụng tạo ra tiền gửi
- tiền tệ nội sinh
domain:
  primary: monetary_policy
  secondary: financial_markets
tags:
- monetary_theory
- endogenous_money
- bank_credit
- money_creation
- reserves
- mmt
- central_bank
- money_multiplier
confidence: 4
stability: stable
thesis: "Banks create money endogenously by making loans: when a creditworthy borrower receives a loan, the bank simultaneously creates a new asset (the loan IOU) and a new liability (a deposit) ex nihilo — no prior deposit or reserve is needed. The central bank then provides whatever reserves are required for interbank settlement at the target policy rate. The money supply is therefore demand-driven (endogenous), not supply-constrained by the monetary base as the neoclassical money multiplier implies. The CB sets the price of money (short-term interest rate), not its quantity."
source_refs:
- path: 02_sources/books/watts_wray_mmt_macro/Watts_Wray_Macroeconomics.md
  pages: lines 4948-5084 (Chapter 10.4: What Do Banks Do? — MMT credit creation, loans create deposits, endogenous money)
  weight: primary
related:
- node: '[[Currency As A Central Bank Liability]]'
  relation: related_concept
- node: '[[Reserve Floor Payment System Demand]]'
  relation: related_mechanism
- node: '[[Interest Rate Corridor Floor System Standing Facilities]]'
  relation: related_mechanism
- node: '[[CB Three Techniques Short Rate Control Floor Corridor Allotment]]'
  relation: companion
date_created: '2026-05-23'
date_updated: '2026-05-23'
---

## The Neoclassical Money Multiplier — What Banks Do NOT Do

The standard textbook model (neoclassical) presents banks as financial intermediaries: [RAW-CLIP]
- Banks receive deposits → keep a fraction as reserves → lend the remainder
- Causality: deposits → reserves → loans
- Central bank controls monetary base → controls money supply via the multiplier
- Money supply is exogenous (set by CB)

**This is a myth.** The money multiplier as a description of modern banking is not how banks actually operate. [RAW-CLIP]

## What Banks Actually Do: Loans Create Deposits

**The MMT / endogenous money account:** [RAW-CLIP]

1. A creditworthy customer applies for a loan
2. Bank assesses creditworthiness (income, assets, credit history, default probability)
3. If approved, the bank creates a demand deposit in the customer's account **ex nihilo** (from nothing) by entering a number in a computer ledger
4. Simultaneously: loan appears on asset side of bank's balance sheet; deposit appears on liability side
5. No prior deposit needed; no prior reserve balance needed

**The critical sequence:** Loans create deposits; deposits create the need for reserves. NOT the reverse. [RAW-CLIP]

> "A cheque account was created ex nihilo, that is, from nothing, by entering a number (200) in a computer ledger on behalf of the borrower. The bank did not need any prior deposits, or any cash in its vault." [RAW-CLIP]

## Banks Do Not Loan Out Reserves

Reserves serve a specific and limited function: **interbank settlement** (not loan funding). [RAW-CLIP]

- When a customer spends their deposit (e.g., pays a car dealer at another bank), the payer bank owes the payee bank reserves
- The payer bank acquires reserves by: (1) borrowing from other banks with excess reserves in the interbank market, or (2) borrowing from the central bank
- Individual bank loan officers "neither know, nor care, about the aggregate level of reserves in the banking system" — no loan officer checks reserve position before approving a loan [RAW-CLIP]
- Bank lending is affected by **the price of reserves** (the short-term interest rate) and **expected return on the loan**, NOT by the volume of reserves

**Corollary**: Adding reserves to the banking system does not increase lending capacity. Removing reserves does not reduce lending capacity. QE (which adds reserves) cannot mechanically stimulate bank lending for this reason. [RAW-CLIP]

## Endogenous Money: CB Cannot Control the Money Supply

Since loans create deposits (not the reverse), and banks lend to anyone creditworthy at a profitable spread: [RAW-CLIP]

- **Money supply is endogenous**: determined by loan demand from creditworthy borrowers plus bank willingness to lend
- **CB sets the price (interest rate), not the quantity (reserves)**: the CB must supply whatever reserves are needed to keep the interbank rate at its target
- **Monetary base adjusts to endogenous money growth**: CB cannot use the monetary base as an independent control lever — it must accommodate reserve demand to maintain rate control

**The direction of causation**: [RAW-CLIP]
```
Creditworthy loan demand 
  → Bank approves and creates loan + deposit (ex nihilo)
  → Customer spends deposit 
  → Payer bank loses reserves to payee bank
  → Payer bank borrows reserves (interbank market or CB discount window)
  → CB provides reserves at target rate
```

## What Constrains Bank Lending?

Since money creation is endogenous and banks can create deposits at will, what prevents infinite credit expansion? [RAW-CLIP]

1. **Creditworthiness**: Lack of creditworthy applicants → banks quantity-ration (refuse some loans even at market rate, not just raise interest)
2. **Profitability**: Spread between loan rate and cost of reserves must be positive
3. **Capital ratios**: Bank equity must remain above regulatory minimums (binding constraint in times of stress)
4. **Asymmetric information**: Banks exercise quantity rationing rather than pure price rationing because they cannot always raise the rate to cover all risk

## Policy Implications

**For monetary policy**: The CB controls the short-term interbank rate (the price of reserves), not the quantity of reserves or the money supply. Rate changes affect credit demand by changing the cost of borrowing — the transmission mechanism runs through the interest rate, not through reserve supply. [RAW-CLIP]

**For QE interpretation**: QE adds excess reserves to the banking system. Since banks don't lend out reserves, QE cannot directly expand credit. Its mechanism of action (if any) runs through: (i) lowering long-term rates (portfolio rebalancing), (ii) signaling, (iii) wealth effects — NOT through the money multiplier. [RAW-CLIP]

**For inflation theories**: The Quantity Theory of Money (QTM) — which links money supply growth to inflation — is undermined by endogenous money: if CB cannot control the money supply, CB cannot use money supply as an inflation control lever. Rate-based (Taylor Rule) inflation control is the empirically correct framework. [LLM]
