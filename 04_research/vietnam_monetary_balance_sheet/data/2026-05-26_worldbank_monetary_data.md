# Vietnam Monetary Data — World Bank API + Web Sources
*Fetched: 2026-05-26 | Sources: World Bank API, Wikipedia*

---

## M2 Broad Money

| Year | M2 (VND tn) | M2/GDP (%) | ΔM2 (%) |
|------|-------------|------------|---------|
| 2015 | 5,771       | 111.17     | —       |
| 2016 | 6,803       | 120.64     | +17.9   |
| 2017 | 7,773       | 123.51     | +14.3   |
| 2018 | 8,760       | 124.99     | +12.7   |
| 2019 | 9,954       | 129.15     | +13.6   |
| 2020 | 11,311      | 140.60     | +13.6   |
| 2021 | 12,405      | 146.16     | +9.7    |
| 2022 | 13,110      | 136.26     | +5.7    |

*Source: WB indicator FM.LBL.BMNY.CN + FM.LBL.BMNY.GD.ZS [WEB-2026-05-26]*

---

## GDP Nominal (VND tn)

| Year | GDP (VND tn) |
|------|-------------|
| 2017 | 6,294       |
| 2018 | 7,009       |
| 2019 | 7,707       |
| 2020 | 8,044       |
| 2021 | 8,487       |
| 2022 | 9,621       |
| 2023 | 10,320      |
| 2024 | 11,512      |

*Source: WB indicator NY.GDP.MKTP.CN [WEB-2026-05-26]*

---

## Foreign Reserves (USD bn, including gold)

| Year | Reserves (USD bn) | Δ (USD bn) |
|------|------------------|------------|
| 2015 | 28.3             | —          |
| 2016 | 36.5             | +8.2       |
| 2017 | 49.1             | +12.6      |
| 2018 | 55.5             | +6.4       |
| 2019 | 78.3             | +22.8      |
| 2020 | 94.8             | +16.5      |
| 2021 | 109.4            | +14.6 ← PEAK |
| 2022 | 86.5             | -22.9      |
| 2023 | 92.2             | +5.7       |
| 2024 | 83.1             | -9.1       |

*Source: WB indicator FI.RES.TOTL.CD [WEB-2026-05-26]*

---

## NFA of Banking Sector (VND tn)

| Year | NFA (VND tn) | NFA/M2 (%) |
|------|-------------|-----------|
| 2016 | 946         | 13.9      |
| 2017 | 1,262       | 16.2      |
| 2018 | 1,538       | 17.6      |
| 2019 | 2,128       | 21.4      |
| 2020 | 2,638       | 23.3      |
| 2021 | 2,688       | 21.7      |
| 2022 | 2,314       | 17.6      |
| 2023 | ~0 (≈-0.5) | ~0        |

*Note: 2023 figure (WB indicator FM.AST.NFRG.CN) appears anomalous — -534.9 bn VND.
Likely data gap/revision; SBV reserves of $92 bn implies NFA should be ~2,100+ tn VND.
Flag as DATA_CAVEAT — verify against SBV annual report.*
*Source: WB indicator FM.AST.NFRG.CN [WEB-2026-05-26]*

---

## CPS — Domestic Credit to Private Sector

| Year | CPS/GDP (%) | CPS (VND tn, derived) |
|------|------------|----------------------|
| 2015 | 90.40      | ~4,927               |
| 2016 | 98.86      | ~5,968               |
| 2017 | 103.97     | 6,544                |
| 2018 | 105.28     | 7,381                |
| 2019 | 108.03     | 8,326                |
| 2020 | 115.53     | 9,295                |
| 2021 | 124.28     | 10,549               |
| 2022 | 124.96     | 12,021               |

*CPS (VND tn) = CPS/GDP% × GDP_VND | Source: WB indicator FS.AST.PRVT.GD.ZS [WEB-2026-05-26]*

---

## Exchange Rate (VND/USD, annual average)

| Year | VND/USD (avg) | YoY depr. (%) |
|------|--------------|---------------|
| 2015 | 21,698       | —             |
| 2016 | 21,935       | +1.1          |
| 2017 | 22,370       | +2.0          |
| 2018 | 22,602       | +1.0          |
| 2019 | 23,050       | +2.0          |
| 2020 | 23,208       | +0.7          |
| 2021 | 23,160       | -0.2          |
| 2022 | 23,271       | +0.5          |
| 2023 | 23,787       | +2.2          |
| 2024 | 24,165       | +1.6          |

*Current central rate: 25,138 VND/USD (as of ~May 2026)*
*Source: WB indicator PA.NUS.FCRF + SBV portal [WEB-2026-05-26]*

---

## CPI Inflation (%)

| Year | CPI (%) | Real rate (%) |
|------|---------|---------------|
| 2015 | 0.63    | 8.99          |
| 2016 | 2.67    | 5.05          |
| 2017 | 3.52    | 2.59          |
| 2018 | 3.54    | 3.61          |
| 2019 | 2.80    | 5.16          |
| 2020 | 3.22    | 6.09          |
| 2021 | 1.83    | 4.79          |
| 2022 | 3.16    | 3.42          |
| 2023 | 3.25    | 7.08          |
| 2024 | 3.62    | —             |

*Source: WB indicators FP.CPI.TOTL.ZG + FR.INR.RINR [WEB-2026-05-26]*
