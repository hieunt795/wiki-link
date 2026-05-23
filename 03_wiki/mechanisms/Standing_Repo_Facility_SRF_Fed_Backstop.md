---
node_id: standing_repo_facility_srf_mec_001
type: mechanism
title: Standing Repo Facility SRF Fed Backstop
aliases:
- SRF
- Công cụ Repo thường trực (SRF) của Fed
- Fed Repo Ceiling
domain:
  primary: monetary_policy
  secondary:
  - financial_markets
tags:
- fed
- repo
- sofr
- srf
- liquidity
- backstop
confidence: 3
stability: stable
thesis: 'The Standing Repo Facility (SRF) acts as a ceiling for the SOFR and a liquidity
  safety valve for the US Treasury market, designed to cap secured rates and mitigate
  dealer balance sheet stress by providing a destigmatized backstop.

  '
source_refs:
- path: 02_sources/Clipping/ECB AND FED POLICY OPERATIONAL FRAMEWORKS – A PRIMER.md
  pages: Introduction & Section 3.2
  weight: primary
related:
- node: '[[Repo_Market_Mechanics_Triparty_Bilateral]]'
  relation: backstop_for
- node: '[[SLR_LCR_Balance_Sheet_Constraints_Treasury_Market_Dealer]]'
  relation: mitigates
- node: '[[Central Bank Monetary Policy Operational Framework Typology]]'
  relation: shared_tag:fed
- node: '[[Currency as a Central Bank Liability]]'
  relation: shared_tag:fed
- node: '[[Fedwire Payment System Reserve Demand And LSM Policy]]'
  relation: shared_tag:fed
- node: '[[Fed Ample Reserves Rate Control Framework]]'
  relation: shared_tag:fed
- node: '[[QT Reserve Drain Effectiveness And Deposit Funding Condition]]'
  relation: shared_tag:fed
date_created: 2026-05-20
date_updated: 2026-05-20
---


## Overview
Introduced by the Federal Reserve in July 2021, the **Standing Repo Facility (SRF)** serves as a backstop in the overnight repo market. It allows primary dealers and eligible banks to borrow reserves from the Fed by providing high-quality collateral (Treasuries, Agency debt, MBS) [RAW-CLIP].

## Purpose and Mechanism

### 1. Capping Secured Rates (SOFR)
The primary role of the SRF is to contain spikes in the **Secured Overnight Financing Rate (SOFR)**. When demand for liquidity in the repo market exceeds supply, pushing rates upward, participants can turn to the SRF at its pre-set administered rate, which effectively acts as a ceiling for the market repo rate [RAW-CLIP].

### 2. De-stigmatization
Unlike the **Discount Window**, which has historically suffered from "stigma" (where banks avoid using it to prevent being seen as weak), the SRF is designed to be a "normal" part of market operations [RAW-CLIP]. 
- **Example:** In late 2025, concerns about stigma were discussed in a Fed meeting with primary dealers. Subsequent usage (e.g., **$24 billion** in a single week) indicated that the facility was becoming a functioning tool for containing rate pressure [RAW-CLIP].

### 3. Treasury Market Stability
The SRF is crucial for the stability of the US Treasury market. By providing a guaranteed way for dealers to fund their inventories of Treasuries via repos, it prevents forced selling of securities during liquidity stress [RAW-CLIP].
- **Basis Trades:** High repo rates can trigger the unwinding of basis trades executed by hedge funds (which involve $2 trillion in Treasuries). The SRF helps avoid this by capping repo rates and ensuring funding is available [RAW-CLIP].

## Key Features
- **Counterparties:** Primary dealers and eligible banks.
- **Collateral:** Treasury securities, Agency debt, and Agency MBS.
- **Rate:** Set by the Fed, typically at the top of the target range for the FFR.
- **Operation:** Daily, fixed-rate, full allotment (up to a large limit).

## Comparison with ON RRP
While the **ON RRP** allows participants to lend cash to the Fed (extracting liquidity), the **SRF** allows them to borrow cash from the Fed (injecting liquidity). Together, they provide a set of administered rates that bracket both the unsecured (FFR) and secured (SOFR) money markets [LLM].

---

## Repo Fortification: SRF's Ongoing Defects and Fixes

### The Stigma Problem
SRF stigma has grown worse since the facility was formalized in 2021. Banks fear that using the SRF signals balance sheet distress to peers, triggering credit concerns. Even when SRF offers rates meaningfully below private market repos, dealers avoid it. [RAW-CLIP Conks Repo Fortification]

Williams/NY Fed meeting with primary dealers (mid-November 2025): explicit reminder that dealers "could tap cash via the SRF freely without stigma." Lackluster usage persisted regardless.

**True upper ceiling is not SRFR**: Because of SRF frictions, dealers require spreads as wide as **25bps above SRFR** before SRF arbitrage becomes worthwhile — making the practical ceiling ~SRFR + 25bps, not SRFR itself.

### Balance Sheet Cost: Can't Net SRF Trades

Using the SRF requires two transactions (borrow from Fed + lend to private market to bridge imbalance). These cannot be "netted" → capital must be held against BOTH positions simultaneously → higher capital costs → SRF arbitrage less attractive.

Additionally, the Fed applies **haircuts** to pledged collateral (Treasuries, agency MBS) even when private repo markets apply 0% haircuts → further discourages borrowing via SRF at the margin. [RAW-CLIP Conks Repo Fortification]

### SRF Settlement Structure: Triparty (Not DVP)

A structural cause of the timing defect: **SRF repos are triparty repos** (not DVP), settling exclusively on BNY's triparty platform.

**Why this matters:** Post-GFC, BNY reformed its triparty settlement schedule. Before the reform, BNY extended large amounts of intraday credit to dealers (as early as 8:30am). This exposed BNY to systemic risk → BNY deferred triparty settlement to **3:30pm** (not morning). This means even if the SRF had opened at 8am for bidding, actual cash wouldn't arrive until 3:30pm — making the SRF structurally useless for morning repo trading.

Dealers book DVP repos (which settle at 8:30am) with hedge fund customers in the morning, then cover via triparty repos (MMFs, and now SRF) settling in the afternoon. The SRF's role as an afternoon backstop is therefore by design, not a temporary choice. [RAW-CLIP Conks Repo Defensive Part II]

**SRF auction mechanics:** Dealers submit "propositions" via the Fed's **FedTrade** system (proprietary, open only to approved SRF counterparties). Bids must be at or above SRFR. Higher collateral quality → more cash allocated. The $500B SRF capacity is competed for in a daily auction — dealers bid *above* SRFR to increase odds of receiving Fed liquidity over other bidders.

### Timing Defect: Fixed Pre-Reform to 1:15pm

Before reform: SRF opened only at 1:15pm. But ~70% of overnight repo trading occurs 7am–8:30am. Dealers lending in the morning and covering via SRF in the afternoon faced "grueling wait" + potential negative carry (lent at lower morning rate, covered at higher afternoon SRF rate). [RAW-CLIP Conks Repo Fortification]

### Fix #1: Morning Fed Repos (December 2024)

**First Repo Fortification step:** NY Fed added morning SRF auctions (settling by 9am, during peak repo trading). SRF trades booked 7am–9am window.

**Effect:** Dealers less exposed to negative carry. Reduces (some) timing barrier, but does not address stigma or balance sheet costs. [RAW-CLIP Conks Repo Fortification]

### Fix #2: Centrally Cleared SRF (Planned Q2 2026)

**Next planned step:** Route SRF trades through FICC (the sole CCP in repo markets) → bilateral identity of SRF borrower becomes anonymous → stigma partially reduced.

**Additional benefit:** FICC clearing allows dealers to distribute Fed cash without raising additional capital (netting reduces balance sheet consumption). Primary dealers gain access to emergency balance sheet when approaching SRF.

**Timeline:** Q2 2026 announcement likely; implementation 1-2 years. May accelerate if TGCR/SOFR adopted as Fed target rate. [RAW-CLIP Conks Repo Fortification]

### Fix #3: Term Fed Repos (Proposed, Not Yet Implemented)

**Proposed** (not implemented as of Dec 2025): Allow dealers to borrow from SRF for multi-day/week terms (not just overnight). This would:
- Lock in funding rates over balance sheet-intensive periods (month-ends, quarter-ends, year-end)
- Reduce basis trader exposure to overnight repo rate spikes
- Help dealers absorb UST supply over volatile periods

Basis trades are partly financed via term repos in private markets. A term Fed repo would directly compete with private term repo funding → stronger SRF ceiling. [RAW-CLIP Conks Repo Fortification]

### Triparty-Fed Spread (TGCR-SRFR)

A key market gauge for SRF ceiling effectiveness: the **TGCR-SRFR spread** measures how far triparty repo rates (TGCR) trade above the SRF's minimum bid (SRFR).

```
TGCR-SRFR = 0bps → SRF ceiling fully effective; dealers substitute to SRF at margin
TGCR-SRFR > 0bps → SRF ceiling leaking; dealers paying above SRF for various reasons
TGCR-SRFR > 25bps → True spread that makes SRF trades worthwhile despite frictions
```

In the "excess collateral" regime (QT era), rates above SRF on month-ends/mid-months became "commonplace." Conks characterizes this as the Fed "losing the battle to convince prominent market makers to use the SRF in size." [RAW-CLIP Conks Repo Fortification]

