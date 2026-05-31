---
node_id: fed_dollar_swap_lines_crisis_hierarchy_and_swapper_of_last_resort_mec_001
type: concept
title: Fed Dollar Swap Lines Crisis Hierarchy and Swapper of Last Resort
aliases:
- Swapper of Last Resort
- Central Bank Liquidity Swaps
- Global Dollar Backstop
- FX Swap Lines
- Hệ thống hoán đổi USD (Swap Lines)
domain:
  primary: monetary_policy
tags:
- fed
- swap_lines
- eurodollar
- fx_swap
- fima
- liquidity
- backstop
confidence: 4
stability: stable
thesis: 'The Federal Reserve acts as the global "Swapper of Last Resort" by providing
  unlimited USD liquidity to foreign central banks through swap lines; this mechanism
  prevents offshore dollar shortages from triggering forced sales of US Treasuries
  and serves as the ultimate backstop in the global dollar funding hierarchy.

  '
source_refs:
- path: 02_sources/Clipping/I need a dollar (through your swap line).md
  pages: Full document
  weight: primary
- path: 02_sources/books/conks/Conks - Fed's Policies and Facilities.md
  pages: 497, 853-919, 1171-1257
  weight: primary
- path: 02_sources/books/central_bank_balance_sheet/Central_Bank_Balance_Sheet.md
  pages: 384-402
  weight: supporting
parent_node: null
related:
- node: '[[Eurodollar System Mechanics And Post-Reform Decline]]'
  relation: offshore_funding_context
- node: '[[Fed Global Jaws FRP FIMA Public Dollar Architecture]]'
  relation: complementary_facility
- node: '[[FX Swap Basis CIP Deviation Dollar Scarcity]]'
  relation: market_indicator
- node: '[[USD Swap Lines Geopolitical Dollar Integration Tool]]'
  relation: geopolitical_implication
date_created: 2026-05-22
date_updated: 2026-05-24
---

## Overview
The Federal Reserve's **Central Bank Liquidity Swaps** (Swap Lines) are bilateral agreements with foreign central banks (FCBs) to provide USD liquidity to offshore markets. While primarily an economic tool to stabilize US financial conditions, they have become the structural "glue" that prevents the collapse of the global **Eurodollar** system during crises [RAW-CLIP].

## Scope Boundary

[LLM] This node is canonical for the mechanics and crisis hierarchy of Fed dollar swap lines.

[LLM] It should not absorb the full four-facility architecture of ON RRP, FRP, swap lines, and FIMA; that broader architecture belongs to [[Fed_Global_Jaws_FRP_FIMA_Public_Dollar_Architecture]].

[LLM] [[Fed_Usd_Swap_Line_Architecture_And_Crisis_Function]] is a routing stub for the same clipping and should not be expanded separately unless this canonical node is later archived.

## The Hierarchy of Dollar Funding
In normal conditions, the ~$80 trillion offshore dollar market is intermediated by private dealers. When stress emerges, liquidity is sought through a hierarchy:
1. **Private Repos/Interbank:** Secured and unsecured lending in NY.
2. **Private FX Swaps:** Global banks swap foreign currency for USD.
3. **U.S. G-SIB Intermediation:** Large U.S. banks lend excess reserves.
4. **FHLB Arbitrage:** Foreign bank branches in the U.S. borrow from FHLBs to fund HQs.
5. **Fed Swap Lines:** The final backstop when private intermediation breaks down [RAW-CLIP].

## Mechanism of Action
A swap line operation is a double-exchange (spot + forward) between the Fed and an FCB.

### Step 1: The Injection
- **The Fed:** Credits the FCB's account at the FRBNY with USD reserves.
- **The FCB:** Credits the Fed's account at the foreign central bank with an equivalent amount of domestic currency (e.g., Euros, Yen).
- **Exchange Rate:** Based on the current market spot rate.

### Step 2: Domestic Distribution
- The FCB auctions these dollars to its domestic commercial banks (e.g., the ECB lends to Deutsche Bank).
- The FCB takes all credit risk of its domestic banks; the Fed only faces the FCB (sovereign risk) [RAW-CLIP].

### Step 3: The Reversal
- At maturity (typically 7 or 84 days), the transaction is reversed at the **original** exchange rate.
- The FCB pays interest to the Fed (usually OIS + a spread, e.g., 25bps) [RAW-CLIP].

## The "Global Jaws" and Market Stabilization
By acting as the **Swapper of Last Resort**, the Fed enforces a "global ceiling" on dollar rates:
- **Basis Control:** The swap line rate (e.g., OIS + 25bps) acts as the theoretical maximum cost for obtaining dollars offshore. If private FX swap rates spike above this, banks switch to central bank liquidity [RAW-CLIP].
- **Preventing Firesales:** Without swap lines, foreign banks would be forced to sell their holdings of US Treasuries to raise cash, which would drive up US yields and destabilize the US domestic mortgage and corporate credit markets [RAW-CLIP].

## FIMA Repo Facility: The Shadow Layer
For central banks without standing swap lines (e.g., EMs or China), the Fed introduced the **FIMA Repo Facility** in 2020.
- **Mechanism:** Instead of swapping currency, FCBs repo their own holdings of US Treasuries directly with the Fed for USD.
- **Distinction:** Unlike swap lines (which create new reserves against foreign currency), FIMA is a collateralized loan against existing high-quality assets [RAW-CLIP].

## T-Account: Swap Line Activation (Fed Perspective)
When the ECB taps $10bn via the swap line:

**Step 1: Initiation**
| Fed (Assets) | Fed (Liabilities) |
| :--- | :--- |
| + $10bn Foreign Currency (Euro) | + $10bn Reserves (ECB Account) |

[LLM] This expands the Fed's balance sheet and increases the global supply of USD reserves without requiring the Treasury to issue new debt or the Fed to buy securities in the open market [RAW-CLIP].
