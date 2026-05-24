---
node_id: fed_qe_debt_maturity_transformation_fiscal_impact_001
type: mechanism
title: Fed QE Debt Maturity Transformation Fiscal Impact
aliases:
- Fed QE debt maturity swap
- monetary-fiscal QE interaction
- QE biến đổi kỳ hạn nợ
- tương tác tiền tệ tài khóa
domain:
  primary: monetary_policy
tags:
- fed
- qe
- treasury
- debt_maturity
- fiscal_policy
- monetary_fiscal_interaction
- interest_rate_risk
confidence: 5
stability: stable
thesis: "Fed QE programs perform a 'maturity swap' on the consolidated public sector balance sheet (Fed + Treasury). By purchasing long-term fixed-rate Treasuries and issuing floating-rate reserves (IORB), the Fed effectively converts the sovereign's interest rate hedge into a floating-rate mortgage. This creates a 'Giant Carry Trade' for the public sector, which generates profits when rates are low but causes massive fiscal losses—and a cessation of Fed remittances to the Treasury—when interest rates rise."
source_refs:
- path: 02_sources/Clipping/A new Fed-Treasury Accord_.md
  pages: Full document
  weight: primary
- path: 02_sources/Clipping/What about Japan_ (Part I).md
  pages: Full document
  weight: supporting
related:
- node: "[[QE_Duration_Extraction_from_Private_Sector]]"
  relation: related_mechanism
- node: "[[CB_Seigniorage_Income_Capital_Loss_Policy_Independence]]"
  relation: fiscal_consequence_of_qe_losses
date_created: "2026-05-23"
date_updated: "2026-05-24"
---

## The Fed-Treasury Maturity Swap

The U.S. Treasury typically manages interest rate risk by issuing debt across the curve, often favoring long-term fixed-rate bonds (e.g., 10-year, 30-year) to lock in low rates. QE systematically undoes this "interest rate protection" [RAW-CLIP Cochrane]:

1. **Treasury Action**: Issues $100 billion in 30-year bonds at 2%. The taxpayer is now hedged against rate hikes for 30 years.
2. **Fed Action (QE)**: Buys the $100 billion in 30-year bonds. Pays by issuing $100 billion in reserves.
3. **Consolidated Result**: The long-term bond is now held by a government agency (the Fed). The debt held by the *public* is now $100 billion in reserves, which pay a floating rate (IORB/EFFR).

**The Analogy**: As John Cochrane notes, it is as if the "wife" (Treasury) got a 30-year fixed mortgage, but the "husband" (Fed) sheepishly went back to the bank and swapped it for a floating-rate mortgage. When rates go up, the "family" (the taxpayer) loses [RAW-CLIP Cochrane].

## The "Giant Carry Trade"

This mechanism effectively turns the consolidated public sector into a carry trader.
- **In Japan**: The public sector added a fixed-for-floating swap with a notional of 91% of GDP. Borrow short at BoJ-controlled rates (reserves) and invest long. This added 6.25% of GDP in excess returns between 2013-2023 [RAW-CLIP Japan I].
- **The Risk**: While profitable when rates are zero, the trade becomes toxic when the CB must raise rates to fight inflation. The interest paid on reserves (the funding cost) quickly exceeds the fixed coupons earned on the bond portfolio.

## Fiscal and Institutional Consequences

1. **Loss of Remittances**: When the Fed's interest expense exceeds its interest income, it stops sending remittances to the Treasury. Instead, it records a "deferred asset"—effectively an IOU for future profits.
2. **Taxpayer Burden**: Higher interest costs on the consolidated debt must be funded by more issuance or higher taxes. By 2026, U.S. interest costs reached ~$1 trillion per year, exacerbated by the floating-rate nature of the QE-expanded balance sheet [RAW-CLIP Cochrane].
3. **Political Risk**: Large losses and the cessation of remittances undermine the Fed's perceived independence and can lead to calls for "Fed-Treasury Accords" to coordinate debt management [RAW-CLIP Cochrane].

## Summary

QE maturity transformation creates a massive "floating rate" exposure for the government. While it provides stimulus by lowering yields, it leaves the sovereign's fiscal position vulnerable to interest rate cycles, binding monetary and fiscal outcomes together. [LLM]
