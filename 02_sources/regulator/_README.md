# 02_sources/regulator/ — Regulatory Documents

Thư mục chứa các văn bản pháp lý, quy định ràng buộc từ các cơ quan quản lý và giám sát tài chính.

## Cấu trúc thư mục

```
02_sources/regulator/
  bcbs/       # Basel Committee on Banking Supervision — Basel III/IV, IRRBB, FRTB, LCR, NSFR
  sbv/        # State Bank of Vietnam — Thông tư, Quyết định, Nghị định
  fed/        # US Federal Reserve — Regulation W, Regulation Y, SR Letters, Capital Rules
  ecb/        # European Central Bank / SSM — CRR, CRD, SREP requirements
  fsb/        # Financial Stability Board — TLAC, resolution standards, crypto frameworks
  iosco/      # International Organization of Securities Commissions
  bis/        # BIS working papers with binding/standard-setting status
  other/      # Other regulators: MAS, BOJ, PRA, APRA, SEC, CFTC, etc.
```

## Nguồn document được ingest vào đây

- Basel Committee consultative documents và final standards
- BIS papers có tính chất tiêu chuẩn (CPMI, CGFS)
- Thông tư, Quyết định, Nghị định của NHNN/SBV
- Federal Reserve regulatory releases (FRB, OCC, FDIC joint rules)
- ECB/SSM regulations và guidelines
- FSB thematic reviews và binding standards

## Quy tắc đặt tên file

```
{Issuing_Body}_{Short_Description}_{Year}.md

Ví dụ:
  bcbs/BCBS_Basel_III_Capital_Framework_2010.md
  bcbs/BCBS_IRRBB_Standards_2016.md
  bcbs/BCBS_Basel_IV_Output_Floor_2017.md
  sbv/SBV_Circular_22_2019_Credit_Concentration.md
  sbv/SBV_Circular_41_2016_Capital_Adequacy.md
  fed/Fed_Regulation_W_Affiliate_Transactions.md
  ecb/ECB_SREP_Methodology_2024.md
```

## Lưu ý IMMUTABLE

Giống tất cả các file trong `02_sources/`, các file trong thư mục này là **IMMUTABLE** — không bao giờ sửa đổi sau khi đã đặt vào. Chỉ `_source_registry.yaml` là writable.
