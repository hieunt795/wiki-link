---
finding_id: fed_qe_collateral_velocity_001
topic: fed_qe_mechanics_2026
sub_question: "What is the interaction between QE asset purchases and collateral velocity in repo markets?"
confidence: 5
status: stable
promote_to_wiki: true
source_nodes:
  - "[[QE_Collateral_Velocity_Monetary_Policy_Transmission]]"
source_raw:
  - "02_sources/books/singh_collateral_plumbing/Singh_Collateral_Financial_Plumbing.md"
  - "02_sources/books/conks/Conk - Repo.md"
date: 2026-05-24
---

## Finding

QE asset purchases exert a negative impact on "collateral velocity" by "siloing" high-quality collateral (HQC) on central bank balance sheets, thereby reducing the "lubrication" available to financial plumbing.

### Collateral Siloing
- When the Fed buys Treasuries and MBS, it takes them out of the hands of market participants (dealer banks, hedge funds, money market funds).
- These securities are the primary "pledged collateral" used to settle repo transactions and derivatives margins [RAW-BOOK Singh Ch.1].
- Once siloed at the Fed, they can no longer be "reused" (rehypothecated) multiple times to support private credit creation.

### Impact on Repo Markets
- QE replaces "HQC" (which has velocity) with "Reserves" (which generally do not have velocity in the same sense, as they remain in the banking system) [RAW-BOOK Singh Ch.2].
- This can lead to collateral scarcity, driving repo rates down (often below the ON RRP floor if non-banks are flush with cash) [RAW-CLIP Conks Repo].
- Reversing this (via QT or Reverse Repo) returns collateral to the market, increasing "lubrication" and potentially raising repo rates [RAW-BOOK Singh Ch.11].

## Evidence Chain
1. Fed buys Treasuries → 2. Pledged collateral supply falls → 3. Collateral velocity (reuse rate) decreases → 4. Financial plumbing "rusts" as private secured lending becomes more expensive or constrained [LLM].

## Source Labels
[RAW-BOOK Singh Ch.1, Ch.2]
[RAW-CLIP Conks Repo]
[LLM]

## Limitations / Caveats
The Fed can partially offset this via its **Securities Lending Facility**, which allows dealers to borrow specifically needed Treasuries overnight against other collateral, returning some "velocity" to the market [LLM].
