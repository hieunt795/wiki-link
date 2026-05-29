---
node_id: secured_funding_instruments_repo_covered_bond_abs_001
type: mechanism
title: 'Secured Funding Instruments in Bank ALM: Repo, Covered Bonds, and ABS'
aliases:
- Repo mechanism
- Covered bond funding
- ABS securitisation funding
- Công cụ tài trợ có bảo đảm
- Repo ngân hàng
- Trái phiếu bảo đảm
domain:
  primary: alm
  secondary:
  - basel_risk
tags:
- repo
- covered_bonds
- abs
- secured_funding
- lcr
- nsfr
- asset_encumbrance
- collateral
confidence: 1
stability: stable
thesis: '[LLM] Secured funding instruments (repo, covered bonds, ABS) shifted from
  peripheral tools to the structural backbone of bank wholesale funding after the
  2007–9 crisis, driven by counterparty risk aversion in unsecured markets; each instrument
  creates asset encumbrance with distinct LCR/NSFR implications and a tradeoff between
  funding cost and unsecured creditor subordination. [LLM] Covered bonds dominate
  European medium-term secured funding (€2.5 trillion outstanding in 2016) while repo
  dominates short-term (€5.6 trillion European market in 2016); ABS provides capital
  relief but is structurally more complex and carries higher reputational risk post-crisis.

  '
source_refs:
- path: 02_sources/books/elkenbracht_huizing_alm/Elkenbracht_Huizing_Handbook_ALM.md
  pages: Ch 16 — Instruments for Secured Funding (Inter-American Development Bank;
    European Investment Bank)
  weight: primary
parent_node: null
related:
- node: '[[Asset_Encumbrance_Management_Bank_Alm]]'
  relation: related_to
- node: '[[Reserve_Asset_Management_Hqla_Portfolio_Bank]]'
  relation: related_to
- node: '[[Funding_Gap_Profile_And_Behavioural_Maturity_Calendar]]'
  relation: mechanism_of
date_created: '2026-05-28'
date_updated: '2026-05-28'
---

## 1. Repo (Repurchase Agreement)

### Mechanics
A repo is a short-term secured borrowing: the bank (borrower) delivers securities as collateral, receives cash on the "opening leg", and reverses the exchange on the "closing leg" at an agreed repo rate. Legal title transfers to the lender, but economic benefits (coupons, dividends) are passed back to the borrower. Accounting treatment: the underlying security stays on the borrower's balance sheet.

European market: ~€5.6 trillion outstanding (December 2016); ~56% of volume with maturity under 1 month; ~19% overnight. US market: ~US$3.4 trillion, predominantly overnight.

### Repo Rates
- **General Collateral (GC):** Rate determined by money market conditions, independent of specific security.
- **Special repos:** When a specific security is in high demand (e.g., on-the-run government bonds shorted by market-makers), the borrower accepts a below-GC rate to obtain that specific security.

### Haircuts
[LLM] Haircuts reflect collateral market and credit risk. Typical ranges:
- Highly rated government bonds: 0.5%–3%
- Covered bonds: 1%–8%
- Investment grade senior unsecured: 8%–20%
- Sub-investment grade bonds: up to 40%
- Developed market equities: 15%–25%

Regulators concern: haircuts are procyclical — low in booms, high in busts — amplifying deleveraging. FSB recommended haircut floors for non-centrally cleared repos (non-government collateral, non-bank to non-bank transactions) from 2015.

### Tri-Party Repos
Settlement, collateral management, and margining delegated to a tri-party agent (Clearstream, Euroclear, JP Morgan, BNY Mellon). The agent optimises collateral allocation automatically. Approximately 12% of European repo market (December 2016); over 50% of US market.

### Central Clearing Counterparties (CCPs)
CCPs interpose between borrower and lender, requiring initial margin, variation margin, and default fund contributions. Exposure on "qualifying CCPs" attracts only 2% capital weight under Basel III. ~27% of European repo cleared through CCPs as of December 2016 (mainly Eurex, LCH.Clearnet).

## 2. Covered Bonds

### Structural Features
Covered bonds are issued by the originating bank directly (on-balance-sheet); the cover pool (mortgages or public sector assets) remains on the bank's balance sheet, ring-fenced in favour of covered bondholders. Key investor protections:
1. Full recourse to the issuing credit institution
2. Priority access to the cover pool over unsecured creditors
3. Obligation to maintain the pool sufficiently at all times
4. Regulatory or independent supervision of the pool

[LLM] This dual-recourse structure makes covered bonds safer than senior unsecured bonds, enabling better ratings (often AAA) and lower funding cost. The cover pool must be actively managed: regulatory requirements specify maximum LTV ratios, overcollateralisation levels, replenishment eligibility, and disclosure requirements.

European market: €2.5 trillion outstanding at end 2016 (two-thirds from Germany, Denmark, France, Spain, Sweden). Mortgages account for over 80% of cover pools.

### LCR/NSFR Treatment
[LLM] Covered bonds (if investment grade and meeting EBA eligibility criteria) may qualify as Level 2A or Level 2B HQLA, giving them favourable LCR treatment. They also count as stable funding (ASF) under NSFR when they mature beyond 1 year. Central banks (ECB, BoE) accept covered bonds as collateral in monetary operations, with haircuts typically lower than for corporate bonds.

### Capital Relief
No capital relief — the originating bank retains all credit risk and the assets stay on its balance sheet.

## 3. Asset-Backed Securities (ABS / RMBS)

### Structural Features
ABS involves a **true sale** of assets to a special purpose vehicle (SPV), achieving bankruptcy remoteness from the originator. The SPV issues multiple tranches (senior, mezzanine, junior/equity) with different credit enhancement levels. The senior tranche typically achieves AAA rating even when the originator is not rated AAA. Cashflows to investors come exclusively from the asset pool.

Key distinction from covered bonds: assets are **off-balance-sheet** for accounting purposes, providing potential capital relief. The originator typically retains the equity tranche (first-loss piece) to align incentives; this attracts high capital charges under Basel III (risk weight 1,250% for low-rated retained positions).

### Capital Relief and Regulatory Treatment
[LLM] True-sale securitisation can reduce RWA if the originator transfers sufficient credit risk to third-party investors. However, regulatory capital treatment is complex: retained first-loss pieces and liquidity facilities can eliminate much of the apparent relief. Post-crisis regulations (simple, transparent, and comparable — STS — framework in Europe from 2015) create a higher-quality tier of ABS with better capital treatment.

ABS retained by the originator and not placed with investors do not encumber the underlying assets in the NSFR sense until pledged to a counterparty. Banks frequently retain their own ABS issuance specifically to repo it with the central bank for cheap secured funding.

### LCR/NSFR
[LLM] Only the highest-rated and most liquid ABS (e.g., AAA RMBS or CMBS meeting STS criteria) qualify for Level 2B HQLA status, with a 25%–50% haircut. Under NSFR, retained ABS require significant stable funding factors (up to 100% RSF if encumbrance period exceeds 1 year).

## Encumbrance Implications

[LLM] Every secured funding instrument creates asset encumbrance — the pledged assets cannot be freely withdrawn. The degree and duration of encumbrance varies:
- Repo: short-term encumbrance (typically days to months)
- Covered bonds: medium-to-long-term encumbrance (multi-year cover pool commitment)
- ABS: multi-year (SPV holds assets until full amortisation)

The encumbrance ratio is the key metric monitoring the balance between secured and unsecured funding. See the Asset Encumbrance node for detailed treatment.
