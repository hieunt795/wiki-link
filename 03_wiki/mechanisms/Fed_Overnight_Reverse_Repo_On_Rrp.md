---
node_id: fed_overnight_reverse_repo_on_rrp_001
type: mechanism
title: Fed Overnight Reverse Repo ON RRP
aliases:
- ON RRP
- ONRRP
- reverse repo facility
- Fed RRP
- co so repo dao nguoc qua dem
domain:
  primary: monetary_policy
tags:
- rrp
- money-market
- fed-facilities
- reserves
- mmt
confidence: 3
stability: evolving
thesis: 'The Fed Overnight Reverse Repo facility (ON RRP) is the Fed liquidity shock
  absorber: it accepts cash from money market funds and GSEs overnight in exchange
  for Treasury collateral, paying the ON RRP rate. When bank deposits and bill supply
  are abundant, RRP drains to zero; when reserves are scarce and bill supply falls,
  RRP surges as MMFs have nowhere else to park cash.'
source_refs:
- path: 02_sources/books/conks/Conks - Shadow Banking and Cash Markets.md
  pages: Money Market Blindspot I & II, Shadow Bank Shutdown
  weight: primary
related:
- node: '[[Debt Ceiling Extraordinary Measures Treasury]]'
  relation: shared_tag:money-market
- node: '[[Fedwire Payment System Reserve Demand And LSM Policy]]'
  relation: shared_tag:reserves
- node: '[[QT Reserve Drain Effectiveness And Deposit Funding Condition]]'
  relation: shared_tag:reserves
- node: '[[TGA Reserve Swap Mechanics And Debt Ceiling Dynamics]]'
  relation: shared_tag:reserves
- node: '[[Central Bank Balance Sheet Structure Liabilities Assets]]'
  relation: shared_tag:reserves
date_created: '2026-05-20'
date_updated: '2026-05-20'
---


The Fed ON RRP is a key instrument for floor-system rate control and reserve management.

**Who uses it:** Money market funds, GSEs, primary dealers. Not commercial banks (they use IOER/IORB instead).

**Rate control:** ON RRP rate sets the floor under money market rates. No rational MMF will lend below the ON RRP rate when the Fed offers a riskless overnight alternative.

**Shock absorber role:** When TGA drawdowns flood the banking system with reserves, banks cannot profitably hold all excess deposits — they push depositors to MMFs. MMFs, facing lower T-bill yields, park cash in ON RRP. RRP balance surges, temporarily absorbing the liquidity flood.

**RRP drain → reserve release:** As RRP is depleted (post-2022 QT), reserves that were locked up flow back into the banking system. This extended the runway for QT without triggering a reserve shortage.

**Monitoring:** Watch daily RRPONTSYD (FRED) alongside bank reserve balances. A rapidly declining RRP below 00B signals reserves approaching scarce territory.


