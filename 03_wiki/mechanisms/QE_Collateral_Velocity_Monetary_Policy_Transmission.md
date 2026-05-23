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
confidence: 4
stability: stable
thesis: "QE is a 'coiled spring' for collateral markets: by absorbing good collateral (Treasuries, gilts, Bunds) onto central bank balance sheets, QE suppresses collateral velocity → lowers financial lubrication → effectively tightens financial conditions via the collateral (repo) channel even as the money channel loosens; Fed RRP with non-banks is 'accounting drainage' not 'reserve drainage' because non-banks cannot rehypothecate received collateral, so velocity does not increase; QE unwind must be mindful that releasing collateral raises both the money rate (LM shifts left) and repo rate (IS shifts up), with implications for the full rate cycle path."
source_refs:
- path: 02_sources/books/singh_collateral_plumbing/Singh_Collateral_Financial_Plumbing.md
  pages: lines 1377-1512 (Chapter 4: Collateral and Monetary Policy)
  weight: primary
related:
- node: '[[Collateral Velocity Reuse Rate Financial Plumbing]]'
  relation: builds_on
- node: '[[Fed Balance Sheet Floor Payment System Reserve Demand]]'
  relation: related_mechanism
- node: '[[Standing Repo Facility SRF Fed Backstop]]'
  relation: related_mechanism
- node: '[[Fed Reserve Demand Reduction Four Policy Tools]]'
  relation: related_mechanism
date_created: '2026-05-23'
date_updated: '2026-05-23'
---

## The Collateral Gap in IS/LM

Standard IS/LM: LM = central bank money only. But cross-border financial markets use "cash or cash equivalent" (money + pledged collateral) to settle intraday accounts. The pledged collateral market (~$10T pre-Lehman) is as large as US M2 — yet it does not appear in LM. [RAW-CLIP]

Singh's extension: Pledged collateral can be treated as an asset under I (private investment) affecting the IS curve. When collateral use drops, IS shifts inward (same contractionary effect as reduced investment). When QE shifts LM right, it does not replace lost IS effect from collateral contraction. [RAW-CLIP]

## QE as a Coiled Spring

QE by Fed, BoE, BoJ, ECB removes good collateral (Treasuries, gilts, JGBs, Bunds) from the market and places it on central bank balance sheets. Effect on financial plumbing:

1. Non-banks sell collateral to central bank → receive reserves (cash) deposited at commercial banks
2. Good collateral silo-ed at central bank → no longer available for rehypothecation chains
3. Collateral velocity falls → financial lubrication decreases
4. Repo rates decline (collateral scarcity in repo market → cash providers drive down repo rates)
5. Non-banks starved of good collateral alternatives → force them toward riskier assets [RAW-CLIP]

QE converts good collateral into excess bank reserves: non-banks' bank deposits rise, but these deposits are NOT equivalent to freely-circulating collateral for plumbing purposes — excess reserves sit in a closed circuit (IOER remunerates them), they do not reach the bilateral repo market. [RAW-CLIP]

**The coiled spring**: As QE tightens collateral market conditions (lower velocity, lower repo rates), the eventual unwind releases collateral back to market → collateral velocity rises → repo rates rise → financial conditions tighten from the collateral side even before official rate hikes. [RAW-CLIP]

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
