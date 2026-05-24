---
node_id: qe_collateral_velocity_monetary_policy_001
type: mechanism
title: QE Collateral Velocity And Monetary Policy Transmission
aliases:
- QE coiled spring collateral
- collateral and monetary policy
- repo rate monetary transmission
- RRP accounting drainage
- IS/LM collateral extension
- QE tắc nghẽn kênh thế chấp
domain:
  primary: monetary_policy
  secondary: financial_markets
tags:
- qe
- collateral
- repo
- monetary_policy_transmission
- collateral_velocity
- financial_plumbing
- fed_balance_sheet
- rrp
- ioer
confidence: 5
stability: stable
thesis: "QE is a 'coiled spring' for collateral markets: by absorbing high-quality collateral (HQC) onto central bank balance sheets, it suppresses collateral velocity and financial lubrication. This 'siloing' effect creates collateral scarcity, driving repo rates down (often below the CB's floor). The subsequent withdrawal (QT) or 'Not-QE' interventions (like RMOs or BTFP) must manage the dual tension of releasing collateral back to the market while maintaining rate control, a process that can trigger a 'Scissors Effect' where rising supply meets falling CB support."
source_refs:
- path: 02_sources/books/singh_collateral_plumbing/Singh_Collateral_Financial_Plumbing.md
  pages: "Chapter 4: Collateral and Monetary Policy; Chapter 11: Transmission"
  weight: primary
- path: 02_sources/books/conks/Conk - Repo.md
  pages: "The QE Flood and RRP shock absorber"
  weight: supporting
- path: 02_sources/Clipping/Who Buys When the ECB Doesn't_.md
  pages: Full document
  weight: supporting
related:
- node: "[[Collateral_Velocity_And_Pledged_Collateral_Market_Mechanics]]"
  relation: foundational_concept
- node: "[[Scissors_Effect_Ecb_Qt_And_Sovereign_Supply]]"
  relation: consequence_of_unwinding_qe
- node: "[[Fed_Overnight_Reverse_Repo_ON_RRP]]"
  relation: accounting_drainage_mechanism
date_created: "2026-05-23"
date_updated: "2026-05-24"
---

## Scope Boundary

[LLM] This node is canonical for QE/QT transmission through collateral velocity and repo-market plumbing.

[LLM] It relies on [[Collateral_Velocity_Reuse_Rate_Financial_Plumbing]] for the general collateral-velocity measurement framework.

[LLM] It should not duplicate the full pledged-collateral taxonomy or the collateral-transformation chain mechanics.

## QE as a Coiled Spring for Plumbing

QE removes "HQC" (Treasuries, Bunds, Gilts) from the bilateral market and replaces it with "Reserves." This has a profound impact on financial lubrication [RAW-BOOK Singh Ch.4]:

1. **Collateral Siloing**: HQC is "siloed" on the Fed's balance sheet. Unlike when it is held by a dealer or hedge fund, it cannot be reused (rehypothecated) to settle other transactions.
2. **Velocity Suppression**: Collateral velocity (the number of times a security is reused) falls. Pre-Lehman velocity was ~3.0x; post-QE, it collapsed toward ~1.0x in several jurisdictions [RAW-BOOK Singh Ch.2].
3. **Repo Rate Distortion**: Collateral scarcity drives repo rates down. In the Eurozone, repo rates on German collateral went as low as -40bps or more because the ECB siloed so much supply [RAW-BOOK Singh Ch.4].

## Price of Money vs. Price of Collateral

**Price of money (IOER/fed funds)**: Post-GFC, IOER creates a wedge — only depository institutions earn IOER. Non-banks (Fannie, Freddie, MMFs) cannot access IOER directly; they drive fed funds rate below IOER (FHLB-foreign bank arbitrage, ~$2-3B true interbank). This bifurcates the short-term rate market. [RAW-CLIP]

**Price of collateral (repo rate)**: Repo rate = rate at which cash is lent against collateral. Collateral shortage → repo rate falls (cash providers accept lower yield to secure scarce good collateral). Collateral abundance → repo rate rises. Post-QE: US repo rates stayed positive due to RRP floor; eurozone repo rates on German/French/Dutch collateral went negative (minus 40bps and below) as ECB QE drained good collateral from eurozone. [RAW-CLIP]

Key insight: Repo rates (not fed funds) represent the true cost of money for non-depository institutions that cannot access IOER. If repo markets don't comply with central bank policy, the central bank loses effective transmission to the non-bank sector. [RAW-CLIP]

## Fed RRP: Accounting Drainage, Not Reserve Drainage

The Fed's reverse repo program (RRP) with non-banks (MMFs, Fannie/Freddie, select asset managers) launched September 2013:

**Mechanism**: Fed lends Treasuries to non-banks via reverse repo → non-bank pays cash → on Fed's balance sheet, "excess reserves of non-banks" converts to "RRP with non-banks." Total Fed balance sheet unchanged. [RAW-CLIP]

**Critical limitation — no velocity increase from RRP with non-banks**:
- Non-banks are NOT members of GCF (General Collateral Finance interdealer triparty service) at DTCC
- GCF/triparty collateral can only be rehypothecated within the triparty system by banks
- Collateral received by non-banks via RRP cannot be pledged to CCPs, bilateral derivatives markets, or the bilateral repo market
- Securities remain effectively on the Fed's balance sheet; they are NOT in the market's possession for plumbing purposes [RAW-CLIP]

> "Securities in the market's possession have velocity; those at the central bank do not." [RAW-CLIP]

**Banks via RRP CAN increase velocity**: If a bank receives collateral via RRP and has balance-sheet space, it can substitute this collateral for other securities, freeing those to enter the bilateral market. But this requires bank balance-sheet capacity — constrained by leverage ratio and LCR. [RAW-CLIP]

## QE Unwind and Rate Path Implications

QE unwind (balance sheet reduction) has a dual rate impact:
1. **Money channel**: Absorbing reserves → LM shifts left → policy/money rates rise
2. **Collateral channel**: Releasing securities → collateral velocity rises → repo rates rise

Both effects simultaneously tighten financial conditions. The key risk: if collateral is released too quickly, repo rates may overshoot IOER → depository institutions switch from IOER to repo markets → money multiplier increases → inflation risk. [RAW-CLIP]

**Rate cycle implication**: QE lowered effective real rates by ~150-200bps (NY Fed estimate, Dudley 2012) beyond what official rates show. If QE had not occurred, the real rate would be ~2% lower. With a typical 400bps tightening cycle, the terminal rate could be as low as 2% (from an effective minus 2% starting point) — i.e., rate cycles may be shallower once QE's hidden tightening via collateral suppression is unwound by balance sheet reduction. [LLM]

## ECB vs. Fed: Different Plumbing Implications

**ECB LTRO**: Provides financing to banks by accepting not-so-good collateral (eligible euro sovereign debt) while leaving good collateral (German Bunds, French OATs) circulating in the market. Does NOT drain good collateral → does not suppress velocity. Unwind is contractually set (3-year LTRO unwinds at maturity). [RAW-CLIP]

**Fed/BoE/BoJ QE**: Purchases good collateral (Treasuries, gilts, JGBs) → drains it from bilateral market → suppresses velocity. Unwind is open-ended and at central bank discretion. [RAW-CLIP]

**Policy implication for ECB QE**: If ECB embarks on QE, it should simultaneously implement an aggressive securities lending program — lend collateral back to the market (securities belong to ECB but are lent short-term) → preserves collateral velocity while achieving QE monetary objectives. [RAW-CLIP]
