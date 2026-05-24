---
finding_id: fed_qe_t_account_001
topic: fed_qe_mechanics_2026
sub_question: "What are the T-account flows for QE when the Fed buys from a bank vs. a non-bank?"
confidence: 5
status: stable
promote_to_wiki: true
source_nodes:
  - "[[CB_Reserve_System_Level_Constraint_Money_Multiplier_Myth]]"
source_raw:
  - "02_sources/books/central_bank_balance_sheet/Central_Bank_Balance_Sheet.md"
  - "02_sources/books/singh_collateral_plumbing/Singh_Collateral_Financial_Plumbing.md"
date: 2026-05-24
---

## Finding

The mechanics of Fed Quantitative Easing (QE) depend on the counterparty of the transaction. While all QE increases narrow money (reserves), only QE involving non-bank counterparties increases broad money (deposits).

### Case 1: Fed buys from a Commercial Bank
- **Federal Reserve**: Assets +UST, Liabilities +Reserves (at the selling bank's account).
- **Commercial Bank**: Assets -UST, Assets +Reserves.
- **Result**: No change in the bank's total assets, just a composition shift from securities to reserves. No new broad money is created [RAW-BOOK CB Balance Sheet].

### Case 2: Fed buys from a Non-Bank (e.g., Pension Fund, Hedge Fund)
- **Federal Reserve**: Assets +UST, Liabilities +Reserves (at the Non-Bank's clearing bank).
- **Commercial Bank (Clearing Bank)**: Assets +Reserves (at Fed), Liabilities +Deposits (Non-Bank's account).
- **Non-Bank**: Assets -UST, Assets +Deposits (at its bank).
- **Result**: Both narrow money (reserves) and broad money (deposits) increase. The Fed's balance sheet expands, and the commercial bank's balance sheet expands by the same amount [RAW-BOOK Singh Ch.1].

## Evidence Chain
1. Fed initiates purchase → 2. Payment is made by crediting a reserve account → 3. If the seller is a bank, it's a liability swap; if a non-bank, the bank creates a deposit to match the new reserve asset [LLM].

## Source Labels
[RAW-BOOK CB Balance Sheet p.12-13]
[RAW-BOOK Singh Ch.1]
[LLM]

## Limitations / Caveats
This assumes the "non-bank" does not immediately use the deposits to buy other assets, which would shift the deposits but not the total quantity [LLM].
