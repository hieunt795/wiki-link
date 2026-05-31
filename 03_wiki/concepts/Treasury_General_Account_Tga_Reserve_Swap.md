---
node_id: treasury_general_account_tga_reserve_swap_mec_001
type: concept
title: Treasury General Account TGA Reserve Swap
aliases:
- TGA
- Treasury General Account
- government bank account
- tài khoản TGA
- tài khoản chính phủ
domain:
  primary: monetary_policy
  secondary:
  - financial_markets
tags:
- tga
- reserves
- fed-balance-sheet
- liquidity
- liability-swap
- autonomous-factors
confidence: 4
stability: stable
thesis: 'The Treasury General Account (TGA) is the US government''s checking account
  held at the Federal Reserve.  Changes in the TGA result in an opposite 1:1 change
  in bank reserves (dTGA = -dReserves) unless the Fed  adjusts its assets to maintain
  ample reserves. The TGA acts as an "autonomous factor" that directly  competes with
  reserves for space on the Fed''s liability side.

  '
source_refs:
- path: 02_sources/books/conks/Conks - Shadow Banking and Cash Markets.md
  pages: Money Market Blindspot I & II
  weight: primary
- path: 02_sources/Clipping/The Checking Account of the U.S. Federal Government....md
  pages: full document
  weight: primary
parent_node: null
related:
- node: '[[Fed_Ample_Reserves_Range_Floor_Framework]]'
  relation: context
- node: '[[Fed_Fiscal_Agent_Treasury_Relationship]]'
  relation: framework
- node: '[[TGA Reserve Swap Mechanics And Debt Ceiling Dynamics]]'
  relation: shared_tag:tga
- node: '[[Ample Reserves Buffer Sizing TGA Volatility]]'
  relation: shared_tag:tga
- node: '[[Debt Ceiling Extraordinary Measures Treasury]]'
  relation: shared_tag:tga
- node: '[[Fedwire Payment System Reserve Demand And LSM Policy]]'
  relation: shared_tag:reserves
- node: '[[QT Reserve Drain Effectiveness And Deposit Funding Condition]]'
  relation: shared_tag:reserves
date_created: 2026-05-20
date_updated: 2026-05-24
---


## Scope Boundary

[LLM] This node is canonical for the core TGA-reserve accounting identity and the 1:1 Fed liability swap.

[LLM] For volatility-driven reserve-buffer demand, use [[Tga_Volatility_And_Reserve_Buffer_Demand]].

[LLM] For the quantitative buffer-sizing formula, use [[Ample_Reserves_Buffer_Sizing_Tga_Volatility]].

[LLM] For TGA reform as a balance-sheet-reduction policy lever, use [[Tga_Reform_As_Fed_Balance_Sheet_Reduction_Tool]].

## Core Mechanism

The Fed balance sheet follows a fundamental identity (simplified):
**Assets = Reserves + TGA + Currency** [RAW-CLIP]

Because the Fed's assets are typically set by policy (QE/QT) or autonomous factors, the liability side must balance any change in the TGA through reserves or currency. Since currency is relatively stable, the primary offset is bank reserves.

### 1. The 1:1 Liability Swap (dTGA = -dReserves)
When a private entity pays taxes or buys a Treasury bond, their commercial bank sends reserves to the Fed to credit the TGA. [RAW-CLIP]
- **TGA Refill/Inflow:** Reserves ↓ | TGA ↑ (Drain of system liquidity)
- **TGA Drawdown/Outflow:** Reserves ↑ | TGA ↓ (Injection of system liquidity)

### 2. TGA as an "Autonomous Factor"
The TGA is considered an autonomous factor because its balance is determined by the Treasury's fiscal decisions (tax receipts, spending, debt issuance), not by the Fed's monetary policy. [RAW-CLIP] 

### 3. Impact on Balance Sheet Growth
While short-term TGA fluctuations shift the *composition* of liabilities (dTGA = -dReserves), long-term increases in either the **level** or the **volatility** of the TGA contribute to a larger Fed balance sheet. [RAW-CLIP]

- **Level Impact:** If the Treasury chooses to maintain a higher average balance (e.g., increasing from $5bn pre-2008 to $750bn-$850bn in 2026), the Fed must expand its assets to prevent this from permanently draining reserves below the "ample" threshold (dTGA = dAssets). [RAW-CLIP] [LLM]
- **Volatility Impact:** High TGA volatility requires the Fed to maintain a larger "reserve buffer" to ensure that sudden TGA spikes do not accidentally push reserves into scarcity (as occurred in September 2019). [RAW-CLIP] [RAW-BOOK SX]

## Historical & Structural Context
- **Pre-2008:** The Treasury kept most of its cash in private commercial banks (Treasury Tax and Loan accounts). [RAW-CLIP]
- **Post-2015:** The Treasury announced a policy to maintain a minimum TGA balance sufficient to cover one week of outflows (approx. $150bn), which has since scaled upward significantly. [RAW-CLIP] [LLM-E]
- **Variable Arrangement:** The hosting of the TGA at the Fed is an operational choice that has changed in the past and could be modified to reduce the Fed's balance sheet footprint (e.g., the Vissing-Jorgensen proposal). [RAW-CLIP]


