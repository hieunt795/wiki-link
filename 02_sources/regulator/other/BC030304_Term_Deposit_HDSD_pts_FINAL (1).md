Dự án Tư vấn Phương pháp luận hoàn thiện khung quản lý tài sản nợ - tài sản có (ALM)

## Giao phẩm BC03.03.04: Hướng dẫn sử dụng mô hình tiền gửi có kỳ hạn

Tháng 08, năm 2021 BẢN CHÍNH THỨC

<!-- image -->

<!-- image -->

<!-- image -->

## Lưu ý quan trọng

Báo cáo này được thực hiện theo Hợp  đồng cung cấp dịch vụ giữa Công  ty  TNHH  Tư  vấn PricewaterhouseCooper Việt Nam (PwC Việt Nam) và Ngân hàng TMCP An Bình ('ABBank') ngày 24 tháng 09 năm với các điều khoản và điều kiện đi kèm. Báo cáo này dành riêng cho việc sử dụng nội bộ và nhằm phục vụ lợi ích của ABBank và không được sử dụng bởi hoặc phục vụ cho lợi ích của bất kỳ đối tượng nào khác ('Bên Thứ Ba').

Bên thứ ba không được phép sử dụng Báo cáo này trừ khi đã ký Cam kết miễn trừ trách nhiệm cho PwC Việt Nam và gửi Cam kết này đến PwC Việt Nam hoặc nhận được một thông báo từ PwC Việt Nam về các trách nhiệm liên quan của công ty đối với Bên Thứ Ba.

Bất kỳ Bên Thứ Ba nào sử dụng và đọc báo cáo này trái với các điều khoản nêu trên, thì Bên Thứ Ba đó phải chấp nhận và đồng ý với các điều khoản sau:

1. Công việc được thực hiện bởi PwC Việt Nam theo các yêu cầu của khách hàng mà báo cáo này được gửi đến và được thực hiện chỉ dành riêng cho lợi ích và mục đích sử dụng của chính khách hàng mà báo cáo này được gửi đến.
2. Báo cáo này được thực hiện theo các yêu cầu của khách hàng mà báo cáo này được gửi đến và có thể không bao gồm tất cả những quy trình/ thủ tục có thể được cho là cần thiết cho mục đích của Bên Thứ Ba.
3. PwC Việt Nam, các giám đốc, nhân viên và các bên có liên quan của PwC Việt Nam sẽ không gánh chịu hay chấp nhận bất kỳ nghĩa vụ hay trách nhiệm nào đối với Bên Thứ Ba, dù là nghĩa vụ theo hợp đồng hay ngoài hợp đồng (bao gồm nhưng không giới hạn bởi sự bất cẩn và vi phạm các nghĩa vụ theo quy định của pháp luật), và sẽ không chịu trách nhiệm đối với bất kỳ tổn thất, thiệt hại hoặc phí tổn dưới bất kỳ hình thức nào phát sinh bởi hoặc liên quan đến Bên Thứ Ba do việc sử dụng báo cáo này, hoặc bất kỳ hậu quả nào khác do việc Bên Thứ Ba sử dụng báo cáo này. Ngoài ra, Bên Thứ Ba chấp nhận rằng báo cáo này không được dùng để tham chiếu hoặc trích dẫn toàn bộ hoặc từng phần, trong bất kỳ bản cáo bạch, bản đăng ký, tài liệu chào bán, tài liệu công bố ra công chúng, các hồ sơ vay, các thỏa thuận hoặc tài liệu khác và không công bố báo cáo này nếu không được sự chấp thuận trước bằng văn bản của PwC Việt Nam.

Các thông tin, số liệu thống kê và các ý kiến (gọi là 'thông tin') trong báo cáo này được thực hiện bởi PwC Việt Nam từ các nguồn tài liệu có sẵn do ABBank cung cấp và trên trang web của ABBank trong khuôn khổ của dự án này và qua các buổi thảo luận được tổ chức với các lãnh đạo Ngân hàng.

PwC Việt Nam lập báo cáo này dựa trên các thông tin nhận được và có được và trên cơ sở rằng các thông tin được cung cấp bởi Ngân hàng là chính xác và hoàn chỉnh. Các thông tin trong báo cáo này không nhằm mục đích kiểm toán, không được sao chép, mô phỏng, phân phát, sử dụng một phần hoặc toàn bộ báo cáo này cho các mục đích khác ngoài mục đích đã được nêu trong Thỏa thuận giữa hai bên về Nội dung công việc thực hiện.

## Mục lục

| 1. Phương pháp luận và giả định                                                    |   4 |
|------------------------------------------------------------------------------------|-----|
| 1.1. Phương pháp luận                                                              |   4 |
| 1.2. Giả định và lưu ý mô hình                                                     |   4 |
| 1.2.1. Thời gian trích xuất dữ liệu                                                |   4 |
| 1.2.2. Độ tin cậy                                                                  |   4 |
| 1.2.3. Nền tảng lập trình                                                          |   4 |
| 2. Quy trình                                                                       |   5 |
| 3. Quy trình lập trình                                                             |   9 |
| 3.1. Trích xuất dữ liệu                                                            |   9 |
| 3.2. Xây dựng mô hình                                                              |  19 |
| 3.2.1. Xác định thư mục làm việc cho xây dựng đầy đủ các ngày                      |  20 |
| 3.2.2. Trích xuất dữ liệu cho xây dựng đầy đủ các ngày                             |  20 |
| 3.2.3. Xây dựng mô hình để tạo các ngày bị thiếu                                   |  21 |
| 3.2.4. Xác định thư mục làm việc xây dựng mô hình phi tham số                      |  24 |
| 3.2.5. Xác định phân khúc và phân chia bộ dữ liệu cho xây dựng mô hình phi tham số |  24 |
| 3.2.6. Xác định độ tin cậy                                                         |  25 |
| 3.2.7. Xây dựng mô hình phi tham số                                                |  25 |
| 3.2.8. Kiểm tra hồi tố                                                             |  26 |
| 3.2.9. Hiệu chỉnh                                                                  |  26 |
| 3.2.10. Tổng hợp kết quả mô hình phi tham số                                       |  27 |
| 3.3. Ứng dụng kết quả mô hình                                                      |  28 |
| 3.3.1. Xác định thư mục làm việc ứng dụng mô hình                                  |  30 |
| 3.3.2. Xác định phân khúc và phân chia bộ dữ liệu ứng dụng mô hình                 |  30 |
| 3.3.3. Ứng dụng mô hình                                                            |  31 |
| 3.3.4. Tổng hợp kết quả ứng dụng mô hình                                           |  32 |
| 4. Lịch sử tài liệu                                                                |  34 |

## 1. Phương pháp luận và giả định

## 1.1. Phương pháp luận

Văn bản này trình bày các bước để làm mô hình hành vi cho danh mục Tiền gửi có kỳ hạn (TGCKH) theo phương pháp Phân tích duy trì (Survival Analysis). Nhân sự xây dựng mô hình được khuyến nghị tham khảo Giao phẩm BC03.03.04: Phương pháp luận cho mô hình tiền gửi có kỳ hạn nhằm hiểu rõ phương pháp luận đầy đủ.

## 1.2. Giả định và lưu ý mô hình

## 1.2.1. Thời gian trích xuất dữ liệu

Dữ liệu cho TGCKH được lấy theo cấp độ số dư hàng ngày của tài khoản, trong thời gian tối thiểu 5 năm gần nhất so với ngày bắt đầu xây dựng mô hình.

Trong phạm vi giao phẩm dự án, dữ liệu được trích xuất từ 1/10/2015 đến 30/09/2020.

## 1.2.2. Độ tin cậy

Độ tin cậy được khuyến nghị lấy tại 99%.

## 1.2.3. Nền tảng lập trình

Mô hình được xây dựng trên 2 nền tảng chính:

- SQL server: nền tảng Oracle SQL server
- R Studio: Mô hình được xây dựng trên R 4.0.3 of R - phiên bản mới nhất hiện tại, với giao diện bởi RStudio 1.3.1093. Phiên bản mới nhất của R và R Studio có thể được tải về từ https://cran.r-project.org/bin/windows/base/ và

https://www.rstudio.com/products/rstudio/download/

Các library cần có để thực hiện xây dựng mô hình

library(ggplot2) library(tidyr) library(sqldf) library(dplyr) library(data.table) library(zoo) library(lubridate)

## 2. Quy trình

Mô hình cho TGCKH được xây dựng theo phương pháp Phân tích duy trì (Survival Analysis) phi tham số.

Mô hình hiện được lưu tại thư mục của Ngân hàng tại 07. ALM PROJECT\04. DU LIEU MHHV\TD Deliverables Round 3\TD\_code\_final .

Quy trình xây dựng mô hình được chia thành các bước chính như sau:

- (1) Trích xuất và xử lý dữ liệu
- (2) Phân tích tương quan
- (3) Xây dựng mô hình

<!-- image -->

## Trích xuất dữ liệu

## Xây dựng mô hình

| STT                        | Quy trình                  | Mô tả                                                                                                                          | Thư mục                    | Tên tệp                    | Nền tảng                   |
|----------------------------|----------------------------|--------------------------------------------------------------------------------------------------------------------------------|----------------------------|----------------------------|----------------------------|
| Bước 1: Trích xuất dữ liệu | Bước 1: Trích xuất dữ liệu | Bước 1: Trích xuất dữ liệu                                                                                                     | Bước 1: Trích xuất dữ liệu | Bước 1: Trích xuất dữ liệu | Bước 1: Trích xuất dữ liệu |
| 1.1                        | Tạo bảng ALM_TD_rp_full    | Tạo bảng để fill những ngày bị thiếu dữ liệu như những ngày chủ nhật hay ngày nghỉ lễ                                          | Modeling                   | TD_extract.txt             | SQL Server                 |
| 1.2                        | Tạo bảng ALM_ckh_prod      | Bảng lọc ra phân khúc mà Ngân hang muốn chạy mô hình trên dữ liệu                                                              | Modeling                   | TD_extract.txt             | SQL Server                 |
| 1.1                        | Tạo bảng ALM_dps_first     | Record đầu tiên các tài khoản thuộc phân khúc được xây dựng mô hình trong thời gian trích xuất dữ liệu.                        | Modeling                   | TD_extract.txt             | SQL Server                 |
| 1.2                        | Tạo bảng ALM_dps_collapse  | Record dữ liệu tiền gửi rút gọn và đã chỉnh để không cho balance tăng lên                                                      | Modeling                   | TD_extract.txt             | SQL Server                 |
| 1.3                        | Tạo bảng ALM_ckh_acc       | Bảng thông tin ngày đóng -mở của từng tài khoản thuộc phân khúc mô hình.                                                       | Modeling                   | TD_extract.txt             | SQL Server                 |
| 1.4                        | Tạo bảng ALM_ckh_acc_all   | Các bảng tổng hợp các tài khoản được nối với nhau trong thời gian cho phép tối đa 3 ngày theo giả định tái tục khác tài khoản. | Modeling                   | TD_extract.txt             | SQL Server                 |
| 1.5                        | Tạo bảng ALM_ckh_acc_full  | Bảng tổng hợp các tài khoản được nối với nhau, đã lọc theo tính ưu tiên của giả định tái tục khác tài khoản.                   | Modeling                   | TD_extract.txt             | SQL Server                 |

| 1.6                      | Tạo bảng ALM_ckh_roll                                                                           | Lọc lại List Account, chỉ nối về 1 tài khoản gốc                                                         | Modeling                 | TD_extract.txt           | SQL Server               |
|--------------------------|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|--------------------------|--------------------------|--------------------------|
| 1.7                      | Tạo bảng ALM_all_dps_full                                                                       | Bảng biến đổi từ ALM_ckh_acc sau khi đã gán các tài khoản với tài khoản gốc được nối (nếu có).           | Modeling                 | TD_extract.txt           | SQL Server               |
| 1.8                      | Tạo các bảng ALM_dps_daily_total_bal, ALM_dps_age_total_bal_st udy, ALM_dps_age_total_bal_te st | Các bảng số dư theo ngày, và Các bảng số dư theo tuổi cho tập dữ liệu study và test.                     | Modeling                 | TD_extract.txt           | SQL Server               |
| 1.9                      | Tạo bảng ALM_dps_fulldd                                                                         | Bảng record tất toán cho từng tài khoản, nhằm quan sát đủ biến động rút tiền khi các tài khoản tất toán. | Modeling                 | TD_extract.txt           | SQL Server               |
| 2.0                      | Tạo bảng ALM_all_dps_full_no_min                                                                | Bảng lấy thông tin các ngày t+1                                                                          | Modeling                 | TD_extract.txt           | SQL Server               |
| 2.1                      | Tạo bảng ALM_dps_daily_final, ALM_dps_study_final, ALM_dps_test_final                           | Các bảng về biến động số dư rút tiền sử dụng cho phân tích tương quan và xây dựng mô hình.               | Modeling                 | TD_extract.txt           | SQL Server               |
| Bước 2: Xây dựng mô hình | Bước 2: Xây dựng mô hình                                                                        | Bước 2: Xây dựng mô hình                                                                                 | Bước 2: Xây dựng mô hình | Bước 2: Xây dựng mô hình | Bước 2: Xây dựng mô hình |
| 2.1                      | Xác định thư mục làm việc                                                                       | Thư mục làm việc là nơi chứa mô hình cùng tất cả các giá trị đầu vào và đầu ra sau khi chạy code.        | Modeling                 | TD_survival_final.Rmd    | Rmd                      |
| 2.2                      | Xác định phân khúc và phân chia dữ liệu study, kiểm tra và hiệu chỉnh                           | Lựa chọn phân khúc được lưu tại SQL Server để đưa vào mô hình                                            | Modeling                 | TD_survival_final.Rmd    | Rmd                      |
| 2.3                      | Xác định độ tin cậy                                                                             | Độ tin cậy được lấy là 0.99                                                                              | Modeling                 | TD_survival_final.Rmd    | Rmd                      |

| 2.4                      | Xây dựng mô hình              | Bao gồm xây dựng đường cong duy trì (survival_curv) cho dữ liệu study và tính CDR tại từng tuổi                                               | Modeling                 | TD_survival_final.Rmd        | Rmd                      |
|--------------------------|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|------------------------------|--------------------------|
| 2.5                      | Kiểm tra hồi tố               | Bao gồm xây dựng đường cong duy trì (survival_curv) cho dữ liệu test và tính CDR tại từng tuổi Đánh giá kết quả từ 2 bộ dữ liệu study và test | Modeling                 | TD_survival_final.Rmd        | Rmd                      |
| 2.6                      | Hiệu chỉnh                    | Hiệu chỉnh những giá trị không đạt từ kiểm tra hồi tố. Kết quả sau hiệu chỉnh là kết quả cuối cùng của mô hình                                | Modeling                 | TD_survival_final.Rmd        | Rmd                      |
| 2.7                      | Tổng hợp và xuất file kết quả | Kết quả được tổng hợp lại thành dạng bảng và lưu tại Modeling trong thư mục làm việc                                                          | Modeling                 | TD_survival_final.Rmd        | Rmd                      |
| Bước 3: Ứng dụng mô hình | Bước 3: Ứng dụng mô hình      | Bước 3: Ứng dụng mô hình                                                                                                                      | Bước 3: Ứng dụng mô hình | Bước 3: Ứng dụng mô hình     | Bước 3: Ứng dụng mô hình |
| 3.1                      | Xác định thư mục làm việc     | Thư mục làm việc là nơi chứa mô hình cùng tất cả các giá trị đầu vào và đầu ra sau khi chạy code.                                             | Application              | TD_dps_application_final.Rmd | Rmd                      |
| 3.2                      | Xác định bộ dữ liệu           | Lựa chọn bcf_ccf được lưu tại SQL Server để đưa vào mô hình                                                                                   | Application              | TD_dps_application_final.Rmd | Rmd                      |
| 3.3                      | Ứng dựng mô hình              | Ứng dụng mô hình để ra kết quả bcf và survival rate cho từng tuổi                                                                             | Application              | TD_dps_application_final.Rmd | Rmd                      |
| 3.4                      | Tổng hợp và xuất file kết quả | Kết quả được tổng hợp lại thành dạng bảng và lưu tại Application trong thư mục làm việc                                                       | Application              | TD_dps_application_final.Rmd | Rmd                      |

## 3. Quy trình lập trình

## 3.1. Trích xuất dữ liệu

## Đầu vào

| Nguồn dữ liệu    | Vị trí     |
|------------------|------------|
| ALM_Term_Deposit | SQL Server |

## Code

```
Tên file Vị trí TD_extract.txt TD_code_final --ALM_raw_rp: Bang lay ra tat ca cac ngay hien co de fill nhung ngay thieu vao -------------------------------------------------------------------------------------------------------------------select distinct Rep_Date into ALM_raw_rp from ALM_Term_deposit -- Trich xuat distinct cột reporting_date -- Chay file TD_rp_update_code.R de tao bang va import vao SQL thanh bang ALM_rp_full --ALM_TD_rp_full: Bang chua day du cac ngay -------------------------------------------------------------------------------------------------------------------with ALM_dps_tmp as ( select d.Rep_Date, d.Acc_ID, CONCAT(d.Acc_ID, d.Cus_ID) as accid, d.Cus_ID, d.Ccy, c.Biz_Line, d.EOD_Bal_Conv as ori_bal, d.Op_Date ori_date, d.Mat_Date, d.Tenor, d.Val_Date, d.Prod_Code from (select a.Cus_ID, (case when b.GL_Code like '41%' then 'TCTD' else b.Biz_Line end) Biz_Line from (select Cus_ID,  min(Rep_Date) mind from ALM_Term_deposit group by Cus_ID ) a, -- Tao bang de lay duoc 1st date of Acc_ID (select Cus_ID, Rep_Date, Biz_Line, GL_Code from ALM_Term_deposit ) b -- Tao bang gom day du Rep_Date de so sanh ngay 1st date voi bang g where a.Cus_ID = b.Cus_ID and a.mind = b.Rep_Date ) c, (select * from ALM_Term_deposit )d where c.Cus_ID = d.Cus_ID group by Rep_Date, Acc_ID, d.Cus_ID, Ccy, c.Biz_Line, EOD_Bal_Conv, Op_Date, Mat_Date, Tenor, Val_Date, Prod_Code, GL_Code ) ---select * into ALM_TD_rp_full from ( (select Rep_Date, Acc_ID, CONCAT(Acc_ID, Cus_ID) as accid, Cus_ID, Ccy, Biz_Line, Val_Date, Mat_Date, ori_date, ori_bal, Prod_Code, Tenor from ALM_dps_tmp a) union all ( --lay them cac record so du bi thieu tu bang rp fill select a.missing_rp as Rep_Date, b.Acc_ID, CONCAT(b.Acc_ID, b.Cus_ID) as accid, b.Cus_ID, b.Ccy, b.Biz_Line,
```

## Tên file

## Vị trí

```
b.Val_Date, b.Mat_Date, b.ori_date, b.ori_bal, b.Prod_Code, b.Tenor from dbo.ALM_rp_full a inner join ALM_dps_tmp b on a.rp_to_fill = b.Rep_Date ) ) c ; --ALM_ckh_prod: BANG LOC PHAN KHUC -------------------------------------------------------------------------------------------------------------------with dps_tmp as ( select distinct Rep_Date, a.Acc_ID, accid, Cus_ID, Ccy, Biz_Line, ori_bal, ori_date, Mat_Date, Tenor, Val_Date, Prod_Code from ALM_TD_rp_full a, (select Acc_ID, max(Rep_Date) maxdate from ALM_TD_rp_full group by Acc_ID) b where a.Acc_ID = b.Acc_ID and a.Rep_Date = b.maxdate and Biz_Line = 'CN' and Ccy = 'VND' ) ---select a.* into ALM_ckh_prod from -- Bang loc phan khuc (select min(Rep_Date) mind, Acc_ID, accid, Cus_ID, Ccy, Biz_Line, ori_bal, ori_date, Mat_Date, Tenor, Val_Date, Prod_Code from ALM_TD_rp_full group by Acc_ID, accid, Cus_ID, Ccy, Biz_Line, ori_bal, ori_date, Mat_Date, Tenor, Val_Date, Prod_Code) a, (select * from dps_tmp) b where a.Acc_ID = b.Acc_ID and a.Biz_Line = 'CN' and a.Ccy = 'VND' order by accid, Rep_Date ; --ALM_dps_first: LAY THONG TIN TAI RECORD DAU TIEN CUA ACCOUNT TRONG PHAN KHUC -------------------------------------------------------------------------------------------------------------------with dps_temp as ( select b.accid, min(b.Rep_Date) mindate from (select Rep_Date, accid from ALM_TD_rp_full) b group by b.accid ) ---select a.* into ALM_dps_first from -- Lay thong tin tai record dau tien cua account trong phan khuc (select * from ALM_ckh_prod) a inner join (select * from dps_temp) d on a.accid = d.accid and a.mind = d.mindate where a.Tenor = 6 ;
```

## Tên file

## Vị trí

```
-- ALM_dps_collapse: DU LIEU DPS RUT GON, DA CHINH KHONG CHO OUTSTANDING_PRINCIPAL TANG LEN -------------------------------------------------------------------------------------------------------------------with ALM_all_dps as( select c.Rep_Date as rp_date, accid, c.Val_Date, c.Mat_Date, c.ori_date, c.ori_bal bal, c.Tenor from (select a.* from dbo.ALM_TD_rp_full a, dbo.ALM_dps_first b where a.accid = b.accid) c ) ---select * into ALM_dps_collapse from ( --du lieu dps rut gon, da chinh khong cho bal tang len (select min(rp_date) as rp_date, accid, Val_Date, Mat_Date, bal, Tenor from ALM_all_dps group by accid, Val_Date, Mat_Date, bal, Tenor) union (select max(rp_date) as rp_date, accid, Val_Date, Mat_Date, bal, Tenor from ALM_all_dps group by accid, Val_Date, Mat_Date, bal, Tenor) ) d ; -- ALM_ckh_acc: BANG TONG HOP NGAY OPEN-CLOSE CUA TUNG ACCOUNT -------------------------------------------------------------------------------------------------------------------with ALM_dps_last as( select c.*, b.Cus_ID from (select a.* from ALM_dps_collapse a, (select accid, max(rp_date) maxdate from ALM_dps_collapse group by accid) b where a.accid = b.accid and a.rp_date = b.maxdate) c left join ALM_dps_first b on c.accid = b.accid ) ---select a.accid, a.Cus_ID, a.ori_date opend, a.ori_bal opn_bal, b.rp_date closed, b.bal closed_bal, a.Tenor opn_tenor, b.Tenor cls_tenor into ALM_ckh_acc from ALM_dps_first a -- Bang tong hop ngay open-close cua tung account left join ALM_dps_last b on a.accid = b.accid order by accid, opend ; -- ALM_ckh_acc_all: BANG TONG HOP NOI ACCOUNT SAU 1/2/3 NGAY -------------------------------------------------------------------------------------------------------------------select a.*, b.opend, b.cnt_opn, b.opn_tenor into ALM_dps_acc from --Bang noi Account va dieu kien chi co 1 tai khoan dong va mo sau 1/2/3 ngay (select Cus_ID, closed, cls_tenor, count(*) cnt_cls from ALM_ckh_acc group by Cus_ID, closed, cls_tenor) a, (select Cus_ID, opend, opn_tenor, count(*) cnt_opn from ALM_ckh_acc group by Cus_ID, opend, opn_tenor) b where a.Cus_ID = b.Cus_ID and ((DATEDIFF(day,a.closed,b.opend) = 1 --noi tai khoan sau 1 ngay and a.cnt_cls = 1 --dieu kien chi co 1 tai khoan dong and b.cnt_opn = 1) --dieu kien chi co 1 tai khoan mo or (DATEDIFF(day,a.closed,b.opend) = 2 --noi tai khoan sau 2 ngay and a.cnt_cls = 1 --dieu kien chi co 1 tai khoan dong
```

## Tên file

## Vị trí

```
and b.cnt_opn = 1) --dieu kien chi co 1 tai khoan mo or (DATEDIFF(day,a.closed,b.opend) = 3 --noi tai khoan sau 3 ngay and a.cnt_cls = 1 --dieu kien chi co 1 tai khoan dong and b.cnt_opn = 1)) --dieu kien chi co 1 tai khoan mo order by a.Cus_ID, a.closed --select a.*, b.opn_acc, b.opend, b.opn_bal, b.opn_tenor, DATEDIFF(day,a.closed,b.opend) diff into ALM_ckh_acc_all from --Bang tong hop noi Account sau 1/2/3 ngay (select a.Cus_ID, a.accid cls_acc, a.closed, a.closed_bal, a.cls_tenor from ALM_ckh_acc a, ALM_dps_acc b where a.Cus_ID = b.Cus_ID and a.closed = b.closed) a left join (select a.Cus_ID, a.accid opn_acc, a.opend, a.opn_bal, a.opn_tenor from ALM_ckh_acc a, ALM_dps_acc b where a.Cus_ID = b.Cus_ID and a.opend = b.opend) b on a.Cus_ID = b.Cus_ID where  a.cls_tenor = b.opn_tenor -- thay doi dieu kien so du and a.cls_tenor = 6 and b.opn_tenor = 6 and ((DATEDIFF(day,a.closed,b.opend) = 1) --noi tai khoan sau 1 ngay or (DATEDIFF(day,a.closed,b.opend) = 2) --noi tai khoan sau 1 ngay or (DATEDIFF(day,a.closed,b.opend) = 3)) --noi tai khoan sau 1 ngay order by a.Cus_ID, a.closed ; --ALM_ckh_acc_full: BANG TONG HOP NOI ACCOUNT SAU KHI DA LOC THEO UU TIEN -------------------------------------------------------------------------------------------------------------------with ALM_acc_all_tmp as( select a.* from ALM_ckh_acc_all a, (select cls_acc, min(diff) mindiff from ALM_ckh_acc_all group by cls_acc) b where a.cls_acc = b.cls_acc and a.diff = b.mindiff ) --select a.*, b.ori_date, b.ori_bal into ALM_ckh_acc_full from -- Bang tong hop noi account sau khi da loc theo uu tien (select a.* from ALM_acc_all_tmp a, (select opn_acc, min(diff) mindiff from ALM_acc_all_tmp group by opn_acc) b where a.opn_acc = b.opn_acc and a.diff = b.mindiff) a left join ALM_dps_first b on a.cls_acc = b.accid ; -- ALM_ckh_roll: LOC LAI LIST ACCOUNT, CHI NOI VE 1 TAI KHOAN GOC -------------------------------------------------------------------------------------------------------------------select * into ALM_ckh_roll from --Loc cac truong hop noi theo 1 chuoi, chi ve 1 tai khoan goc duy nhat (select *, row_number() over(partition by opn_acc order by closed desc, cls_acc desc) Corr from ALM_ckh_acc_full) A where Corr = 1 order by cls_acc ;
```

## Tên file

## Vị trí

```
--ALM_all_dps_full: BANG BIEN DOI KHI DA GAN CAC ACCOUNT GOC VA ACCOUNT NOI + TINH AGE + cao bang outstanding balance -------------------------------------------------------------------------------------------------------------------with ALM_ckh_final as ( select a.cls_acc, -- tk goc b.opend ori_vdate, -- ngay mo tk goc a.opn_acc --tk roll from ALM_ckh_roll a left join ALM_ckh_acc b on a.cls_acc = b.accid ) ---select d.*, -- Bang bien doi khi da gan cac account goc va account noi + tinh age + cao bang outstanding balance coalesce(e.cls_acc, d.accid) ori_acc, coalesce(e.ori_vdate, d.ori_date) ori_vdate, (DATEDIFF(day,coalesce(e.ori_vdate, d.ori_date),d.rp_date) + 1) age, ori_bal as bal into ALM_all_dps_full--lenh nham cao bang so du/chinh so du khong tang len (lay so du cumulative min) from ( select Rep_Date as rp_date, accid, Val_Date, Mat_Date, ori_date, ori_bal, Tenor from --lay cac thong tin account kem theo so du cao bang cua phan khuc (select a.* from ALM_TD_rp_full a, ALM_dps_first b where a.accid = b.accid) c ) d left join ALM_ckh_final e on d.accid = e.opn_acc where Tenor = 6 ; -- ALM_dps_daily_total_bal: DU LIEU EOD_BAL_CONV THEO NGAY -------------------------------------------------------------------------------------------------------------------select rp_date, sum(bal) total_bal into ALM_dps_daily_total_bal -- Du lieu EOD_Bal_Conv theo ngay from ALM_all_dps_full where rp_date <= '30-sep-2020' group by rp_date order by rp_date ; --ALM_dps_fulldd: BANG RECORD TAT TOAN -------------------------------------------------------------------------------------------------------------------
```

```
Tên file Vị trí select DATEADD(day,1,a.rp_date) rp_date, a.ori_acc, (0) bal, (a.age + 1) age into ALM_dps_fulldd from ALM_all_dps_full a, -- Bang record tat toan (select ori_acc, max(rp_date) maxdate from ALM_all_dps_full group by ori_acc ) b where a.ori_acc = b.ori_acc and a.rp_date = b.maxdate ; -- ALM_all_dps_full_no_min: Bang lay thong tin cac ngay t+1 -------------------------------------------------------------------------------------------------------------------with ALM_min_dps_full as( select * from (select rp_date, ori_acc, bal, age , Tenor from ALM_all_dps_full group by ori_acc, bal, age, rp_date, Tenor) b left join (select ori_acc as ori_acc_min, min(rp_date) mind  from ALM_all_dps_full group by ori_acc ) a on a.ori_acc_min = b.ori_acc and a.mind = b.rp_date group by a.ori_acc_min, a.mind, b.rp_date, b.ori_acc, b.bal, b.age, b.Tenor ) ---select rp_date, ori_acc, bal, age, Tenor into ALM_all_dps_full_no_min from ALM_min_dps_full -- Bang lay thong tin cua cac ngay t+1 where ori_acc_min is Null group by ori_acc, bal, age, rp_date, Tenor ; -- ALM_dps_daily_final: DU LIEU DAU VAO CHO CORRELATION -------------------------------------------------------------------------------------------------------------------select a.*, -- Du lieu dau vao cho Correlation coalesce(b.total_dd,0) total_drawdown into ALM_dps_daily_final from -- bang co so du ALM_dps_daily_total_bal a left join -- bang duoc tao de lay tong drawdown theo rp date (select rp_date, sum(dd) total_dd from (select c.*, (case when (d.bal > c.bal) then (d.bal-c.bal) else 0 end) dd from -- bang duoc tao de lay so du cua ngay t+1 (select * from (select rp_date, ori_acc, bal, age from ALM_all_dps_full_no_min union all -- lay them cac record tat toan select * from ALM_dps_fulldd) a ) c left join -- bang duoc tao de lay so du cua ngay t (select * from (select rp_date, ori_acc, bal, age from ALM_all_dps_full where Tenor = 6 union all -- lay them cac record tat toan select * from ALM_dps_fulldd) b
```

## Tên file

Vị trí

```
) d on c.ori_acc = d.ori_acc and c.rp_date =  DATEADD(day,1,d.rp_date) -- lay so du ngay t va t+1 tuong ung' ) a group by rp_date ) b on a.rp_date = b.rp_date order by rp_date ; -------------------------------------DU LIEU DUOC CHIA THEO TY LE 4 NAM VA 1 NAM CHO BO STUDY VA TEST----------------------------------------- ALM_dps_age_total_bal_study: DU LIEU EOD_BAL_CONV THEO TUOI DU LIEU STUDY -------------------------------------------------------------------------------------------------------------------select age, sum(bal) as total_bal into ALM_dps_age_total_bal_study -- Du lieu EOD_Bal_Conv theo tuoi du lieu study from ALM_all_dps_full where rp_date <= '30-sep-2019' group by age order by age ; -- ALM_dps_age_total_bal_test: DU LIEU EOD_BAL_CONV THEO TUOI DU LIEU TEST -------------------------------------------------------------------------------------------------------------------select age, sum(bal) as total_bal into ALM_dps_age_total_bal_test -- Du lieu EOD_Bal_Conv theo tuoi du lieu test from ALM_all_dps_full where rp_date >= '1-oct-2019' and rp_date <= '30-sep-2020' group by age order by age ; -- ALM_dps_study_final: DU LIEU STUDY, DAU VAO MO HINH -------------------------------------------------------------------------------------------------------------------select a.*,  -- Du lieu Study, dau vao mo hinh coalesce(b.total_dd,0) total_drawdown into ALM_dps_study_final from -- bang so du ALM_dps_age_total_bal_study a left join -- bang drawdown theo age (select age, sum(dd) total_dd from (select c.*, (case when (d.bal > c.bal) then (d.bal-c.bal) else 0 end) dd from -- bang duoc tao de lay so du cua age T+1 (select * from (select rp_date, ori_acc, bal, age from ALM_all_dps_full_no_min where rp_date <= '30-sep2019' union all -- lay them cac record tat toan select * from ALM_dps_fulldd where rp_date <= '1-oct2019') a ) c
```

## Tên file

Vị trí

```
left join -- bang duoc tao de lay so du cua age T (select * from (select rp_date, ori_acc, bal, age from ALM_all_dps_full where Tenor = 6 union all -- lay them cac record tat toan select * from ALM_dps_fulldd ) b ) d on c.ori_acc = d.ori_acc and c.rp_date =  DATEADD(day,1,d.rp_date) ) a group by age ) b on a.age = b.age order by a.age ; -- ALM_dps_test_final: DU LIEU TEST, DAU VAO MO HINH -------------------------------------------------------------------------------------------------------------------select a.*,  -- Du lieu Test, dau vao mo hinh coalesce(b.total_dd,0) total_drawdown into ALM_dps_test_final from -- bang so du ALM_dps_age_total_bal_test a left join -- bang drawdown theo age (select age, sum(dd) total_dd from (select c.*, (case when (d.bal > c.bal) then (d.bal-c.bal) else 0 end) dd from -- bang duoc tao de lay so du cua age T+1 (select * from (select rp_date, ori_acc, bal, age from ALM_all_dps_full_no_min where rp_date > '30-sep2019' union all -- lay them cac record tat toan select * from ALM_dps_fulldd) a where rp_date > '1-oct2019') c left join -- bang duoc tao de lay so du cua age T (select * from (select rp_date, ori_acc, bal, age from ALM_all_dps_full where Tenor = 6 union all -- lay them cac record tat toan select * from ALM_dps_fulldd) b ) d on c.ori_acc = d.ori_acc and c.rp_date = DATEADD(day,1,d.rp_date) ) a group by age) b on a.age = b.age order by a.age ;
```

## Tên file

Vị trí

```
---------------------------------------DU LIEU DUOC CHIA THEO TY LE 70-30 CHO BO STUDY VA TEST------------------------------------------- ALM_acc_study --select top 70 percent ori_acc into ALM_acc_study from --(select *, NEWID() new_id --from (select distinct ori_acc from ALM_all_dps_full) a --) b ---- ALM_acc_test --select a.ori_acc into ALM_acc_test from --(select distinct ori_acc  from ALM_all_dps_full) a --left join --(select distinct ori_acc from ALM_acc_study) b --on a.ori_acc = b.ori_acc --where b.ori_acc is null ---- ALM_dps_age_total_bal_study: DU LIEU EOD_BAL_CONV THEO TUOI DU LIEU STUDY -----------------------------------------------------------------------------------------------------------------------select age, sum(bal) as total_bal into ALM_dps_age_total_bal_study from  -- Du lieu EOD_Bal_Conv theo tuoi du lieu study --(select age, accid, bal from ALM_all_dps_full) a, --(select ori_acc from ALM_acc_study) b --where a.accid = b.ori_acc --group by age --order by age --; ---- ALM_dps_age_total_bal_test: DU LIEU EOD_BAL_CONV THEO TUOI DU LIEU TEST -----------------------------------------------------------------------------------------------------------------------select age, sum(bal) as total_bal into ALM_dps_age_total_bal_test from -- Du lieu EOD_Bal_Conv theo tuoi du lieu test --(select age, accid, bal from ALM_all_dps_full) a, --(select ori_acc from ALM_acc_test) b --where a.accid = b.ori_acc --group by age --order by age --; ---- ALM_dps_study_final: DU LIEU STUDY, DAU VAO MO HINH -----------------------------------------------------------------------------------------------------------------------select a.*,  -- Du lieu Study, dau vao mo hinh --       coalesce(b.total_dd,0) total_drawdown into ALM_dps_study_final --from ---- bang so du --ALM_dps_age_total_bal_study a --left join ---- bang drawdown theo age --    (select age, sum(dd) total_dd from --                        (select c.*, (case when (d.bal > c.bal) then (d.bal-c.bal) else 0 end) dd from --                         -- bang duoc tao de lay so du cua age T+1 --                                (select * from --                                        (select x.rp_date, x.ori_acc, x.bal, x.age from
```

```
Tên file Vị trí --(select rp_date, ori_acc, bal, age from ALM_all_dps_full_no_min) x, --(select ori_acc from ALM_acc_study) y --where x.ori_acc = y.ori_acc --                                            union all --                                         -- lay them cac record tat toan --select a.* from --(select * from ALM_dps_fulldd) a, --(select ori_acc from ALM_acc_study) b --where a.ori_acc = b.ori_acc --) z --                                 ) c --                        left join --                        -- bang duoc tao de lay so du cua age T --                                (select * from --                                        (select rp_date, ori_acc, bal, age from ALM_all_dps_full --where Tenor = 6 --                                            union all --                                         -- lay them cac record tat toan --                                         select * from ALM_dps_fulldd --) b --) d --                        on c.ori_acc = d.ori_acc and c.rp_date =  DATEADD(day,1,d.rp_date) --) a --    group by age --) b --on a.age = b.age --order by a.age --; ---- ALM_dps_test_final: DU LIEU TEST, DAU VAO MO HINH -----------------------------------------------------------------------------------------------------------------------select a.*,  -- Du lieu Test, dau vao mo hinh --       coalesce(b.total_dd,0) total_drawdown into ALM_dps_test_final --from ---- bang so du --ALM_dps_age_total_bal_test a --left join ---- bang drawdown theo age --    (select age, sum(dd) total_dd from --                        (select c.*, (case when (d.bal > c.bal) then (d.bal-c.bal) else 0 end) dd from --                         -- bang duoc tao de lay so du cua age T+1 --                                (select * from --                                        (select x.rp_date, x.ori_acc, x.bal, x.age from --(select rp_date, ori_acc, bal, age from ALM_all_dps_full_no_min) x, --(select ori_acc from ALM_acc_test) y
```

<!-- image -->

*** Hiện tại dữ liệu đang chia bộ Study và Test theo dữ liệu 4 năm và 1 năm. Ngân hàng có thể chia lại dữ liệu theo tỷ lệ 70% và 30% cho bộ Study và Test bằng cách Uncomment các dòng từ phần DU LIEU DUOC CHIA THEO TY LE 70-30 CHO BO STUDY VA TEST trở đi trong SQL. Để Uncomment ngân hàng có thể bôi đen tất cả các dòng cần Uncomment và sử dụng tổ hợp phím Ctrl + K rồi Ctrl + C.

## Đầu ra

| Tên file            | Vị trí     |
|---------------------|------------|
| ALM_dps_daily_final | SQL Server |
| ALM_dps_study_final | SQL Server |
| ALM_dps_test_final  | SQL Server |

## 3.2. Xây dựng mô hình

## Tổng quan thao tác kỹ thuật

Tại thư mục Modeling để xây dựng đầy đủ các ngày cho dữ liệu (TD\_rp\_update\_code.Rmd)

Bước 1: Nhập các ngày đang có vào file R

<!-- image -->

Bước 2: Hiển thị kết quả các ngày cần tạo thêm. Sau đó import file này vào SQL để chạy trích xuất dữ liệu.

<!-- image -->

## 3.2.1. Xác định thư mục làm việc cho xây dựng đầy đủ các ngày

<!-- image -->

## 3.2.2. Trích xuất dữ liệu cho xây dựng đầy đủ các ngày

<!-- image -->

## 3.2.3. Xây dựng mô hình để tạo các ngày bị thiếu

<!-- image -->

Tại thư mục Modeling bắt đầu xây dựng mô hình phi tham số.

Bước 1: Chạy function 'survi()'

<!-- image -->

Bước 2: Nhập đường dẫn thư mục làm việc tương ứng

<!-- image -->

Bước 3: Nhập server dữ liệu trích xuất của tiền gửi CKH từ SQL

Bước 4: Nhập database dữ liệu trích xuất của tiền gửi CKH từ SQL

<!-- image -->

<!-- image -->

Bước 5: Nhập ID dữ liệu trích xuất của tiền gửi CKH từ SQL

Bước 6: Nhập password dữ liệu trích xuất của tiền gửi CKH từ SQL

<!-- image -->

Bước 7: Nhập các bộ dữ liệu test và study

<!-- image -->

<!-- image -->

Bước 8: Nhập tên phân khúc

Bước 5: Nhập mức độ tin cậy

<!-- image -->

Bước 6: Tùy chọn hiệu chỉnh mô hỉnh

<!-- image -->

<!-- image -->

Hiển thị kết quả xây dựng mô hình

<!-- image -->

## 3.2.4. Xác định thư mục làm việc xây dựng mô hình phi tham số

## Code

<!-- image -->

## 3.2.5. Xác định phân khúc và phân chia bộ dữ liệu cho xây dựng mô hình phi tham số

## Code

<!-- image -->

```
Tên file Vị trí TD_survival_final.Rmd TD_code_final\Modeling study_table_sql <- svDialogs::dlg_input(message = "Which study table is the model input: ")$res %>% as.character() study_sql <- paste('select * from ',study_table_sql) td_study <- sqlQuery(dbhandle,study_sql) names(td_study) <- c("age", "total_bal", "drawdown")#rename ten cot cho bang du lieu XDMH td_study <- td_study[order(td_study$age),]#sap xep thu tu theo tuoi test_table_sql <- svDialogs::dlg_input(message = "Which test table is the model input: ")$res %>% as.character() test_sql <- paste('select * from ',test_table_sql) td_test <- sqlQuery(dbhandle,test_sql) names(td_test) <- c("age", "total_bal", "drawdown")#rename ten cot cho bang du lieu backtest td_test <- td_test[order(td_test$age),]#sap xep thu tu theo tuoi seg_names <- svDialogs::dlg_input(message = "Segment name: ")$res %>% as.character()#dat ten cho phan khuc
```

## 3.2.6. Xác định độ tin cậy

## Code

| Tên file                                                                                                                                 | Vị trí                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| TD_survival_final.Rmd                                                                                                                    | TD_code_final\Modeling                                                                                                                   |
| conf_lvl <- svDialogs::dlg_input(message = "Confident level(99% recommend): ",default = "0.99")$res %>% as.numeric()#nhap muc do tin cay | conf_lvl <- svDialogs::dlg_input(message = "Confident level(99% recommend): ",default = "0.99")$res %>% as.numeric()#nhap muc do tin cay |

## 3.2.7. Xây dựng mô hình phi tham số

## Code

<!-- image -->

| Tên file                                                                               | Vị trí                                                                                 |
|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| TD_survival_final.Rmd                                                                  | TD_code_final\Modeling                                                                 |
| rate_tbl$svv_rate_low_study <- rate_tbl$svv_rate_study - rate_tbl$conf_int #lower XDMH | rate_tbl$svv_rate_low_study <- rate_tbl$svv_rate_study - rate_tbl$conf_int #lower XDMH |

## 3.2.8. Kiểm tra hồi tố

## Code

<!-- image -->

## 3.2.9. Hiệu chỉnh

## Code

| Tên file                                                                                                                                                                                                                                                                                   | Vị trí                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| TD_survival_final.Rmd                                                                                                                                                                                                                                                                      | TD_code_final\Modeling |
| ###choosing calibrate CDR or not calibration <- dlg_input(message = c("1 = Yes, calibrate", "2 = No calibration"), default = "2")$res repeat{ if (calibration %!in% c("1","2")) { dlg_message("Input must be 1,2", type = "ok") calibration <- dlg_input(message = c("1 = Yes, calibrate", |                        |

```
Tên file Vị trí TD_survival_final.Rmd TD_code_final\Modeling "2 = NO calibration"), default = "2")$res } else {break} } if (calibration == "1"){ final$CDR_final <- final$CDR.x*final$backtest + final$CDR.y*(1-final$backtest)#ket qua backtest + hieu chinh survival rate svv_calib <- 1-final$CDR_final svv_calib <- sapply(1:length(svv_calib), function(x){ prod(svv_calib[1:x])}) final$svv_final <- svv_calib } else { final$CDR_final <- final$CDR.x svv_calib <- 1-final$CDR_final svv_calib <- sapply(1:length(svv_calib), function(x){ prod(svv_calib[1:x])}) final$svv_final <- svv_calib }
```

## 3.2.10. Tổng hợp kết quả mô hình phi tham số

## Code

```
Tên file Vị trí TD_survival_final.Rmd TD_code_final\Modeling ##### result summary write.csv(final, paste("./result_summary_", seg_names,".csv", sep = "")) ggsave(paste("./survival_curv_",seg_names,".jpeg", sep = ""), ggplot(data = final, aes(x = age)) + geom_line(aes(y = svv_final), color = "blue", size = 1) + xlab("AGE") + xlim(0,max(final$age)) + ylab("Survival final") + ylim(0,1), device = "jpeg", width = 50.8, height = 28.575, units = "cm") ggsave(paste("./CDR_",seg_names,".jpeg", sep = ""), ggplot(data = final, aes(x = age)) + geom_line(aes(y = CDR_final), color = "blue", size = 1) + xlab("AGE") + xlim(0,max(final$age)) + ylab("CDR final") + ylim(0,max(final$CDR_final)), device = "jpeg", width = 50.8, height = 28.575, units = "cm") done <- readline("The result is saved") odbcClose(dbhandle) }
```

<!-- image -->

| Tên file              | Vị trí                 |
|-----------------------|------------------------|
| TD_survival_final.Rmd | TD_code_final\Modeling |
| survi()               |                        |

## Đầu ra

<!-- image -->

| Tên file                                                  | Vị trí   |
|-----------------------------------------------------------|----------|
| result_summary_td_mod_pwc.csv survival_curv.jpeg CDR.jpeg | Modeling |

## 3.3. Ứng dụng kết quả mô hình

## Tổng quan thao tác kỹ thuật

Tại folder Application

Bước 1: Chạy function dps\_td\_app()

Ctrl-Alt+R

Bước 2: Nhập đường dẫn thư mục làm việc tương ứng

<!-- image -->

Bước 3: Nhập server dữ liệu trích xuất của tiền gửi CKH từ SQL

Bước 4: Nhập database dữ liệu trích xuất của tiền gửi CKH từ SQL

<!-- image -->

<!-- image -->

Bước 5: Nhập ID dữ liệu trích xuất của tiền gửi CKH từ SQL

<!-- image -->

Bước 6: Nhập password dữ liệu trích xuất của tiền gửi CKH từ SQL

Bước 7: Nhập dữ liệu trích xuất của bcf\_ccf

<!-- image -->

Bước 8: Nhập tên phân khúc ứng dụng cho mô hình

<!-- image -->

<!-- image -->

Bước 9: Nhập dữ liệu cho ứng dụng mô hình và survival của mô hình

<!-- image -->

Hiển thị thông báo kết quả xây dựng mô hình

The result is saved

## 3.3.1. Xác định thư mục làm việc ứng dụng mô hình

## Code

<!-- image -->

## 3.3.2. Xác định phân khúc và phân chia bộ dữ liệu ứng dụng mô hình

## Code

<!-- image -->

```
Tên file Vị trí TD_dps_application_final.Rmd Application dt <- sqlQuery(dbhandle,dt_sql) names(dt) <- c("age", "ttm", "balance") dt <- dt[order(dt$age),] seg_names <- svDialogs::dlg_input(message = "Segment name: ")$res %>% as.character()#dat ten cho phan khuc #surv_names <- svDialogs::dlg_input(message = "Survival rate name: ")$res %>% as.character()#dat ten cho bang survival rate #nhap file survival rate surv <- read.csv(choose.files())[c(2, 14)] #tao age day du cho survival surv[(nrow(surv)+1):(nrow(surv)+2),] <data.frame(age = c(max(surv$age)+1,max(surv$age)+2), svv_final = c(0,0)) surv <- rbind.data.frame(data.frame(age = 1, svv_final = 1), surv) age_max <- max(surv$age) surv_add <- data.frame(age = 1:age_max) surv_full <- merge.data.frame(surv_add, surv, by = c("age"), all.x = T, all.y = F) surv_full$svv_final <- surv_full$svv_final %>% na.locf()
```

## 3.3.3. Ứng dụng mô hình

## Code

<!-- image -->

| Tên file                                                                                                                                                                                                                                                                                                                                                                                             | Vị trí                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TD_dps_application_final.Rmd                                                                                                                                                                                                                                                                                                                                                                         | Application                                                                                                                                                                                                                                                                                                                                                                                          |
| #thanh progress pb <- txtProgressBar(min = 1, max = nrow(dt), style = 3) #bat dau tinh toan cashflow cashflow <- lapply(1:nrow(dt), function(x){ svv_x <- surv_full[surv_full$age == dt[x,]$age,]$svv_final agez <- dt[x,]$age #tinh toan dong bcf zzz <- data.frame(dayz = 1:(age_max - agez), age = (agez+1):age_max) zzz <- merge.data.frame(zzz, surv_full, by = c("age"), all.x = T, all.y = F) | #thanh progress pb <- txtProgressBar(min = 1, max = nrow(dt), style = 3) #bat dau tinh toan cashflow cashflow <- lapply(1:nrow(dt), function(x){ svv_x <- surv_full[surv_full$age == dt[x,]$age,]$svv_final agez <- dt[x,]$age #tinh toan dong bcf zzz <- data.frame(dayz = 1:(age_max - agez), age = (agez+1):age_max) zzz <- merge.data.frame(zzz, surv_full, by = c("age"), all.x = T, all.y = F) |

```
Tên file Vị trí TD_dps_application_final.Rmd Application zzz$b_bal <- 0 } else { zzz$b_bal <- zzz$svv_final/svv_x*dt[x,]$balance } zzz$cbcf <- dt[x,]$balance - zzz$b_bal setTxtProgressBar(pb, x) final <- data.frame(bucket = c(1, 7, 30, 90, 180, 360, 10000000)) #tinh toan dong ccf final$ccf <- 0 final$ccf[ which(final$bucket >= dt[x,]$ttm) ] <- dt[x,]$balance final <- merge.data.frame(final, zzz[c(2,5)], by.x = "bucket", by.y = "dayz", all.x = T, all.y = F) final$cbcf[is.na(final$cbcf)] <- dt[x,]$balance final })
```

## 3.3.4. Tổng hợp kết quả ứng dụng mô hình

## Code

```
Tên file Vị trí TD_dps_application_final.Rmd Application result <- data.frame( bucket = c(1, 7, 30, 90, 180, 360, 10000000), ccf = sapply(cashflow, function(x){x[[2]]}) %>% t() %>% as.data.frame() %>% sapply(sum), bcf = sapply(cashflow, function(x){x[[3]]}) %>% t() %>% as.data.frame() %>% sapply(sum) ) result[2:7, 2:3] <- sapply(result[2:3], diff) result <- result[2:3] %>% t() %>% as.data.frame() names(result) <- c("Daily", "2-7 days","8-30 days", "31-90 days", "91-180 days", "181-360 days", ">360 days") write.csv(result, paste("./result_summary_", seg_names,".csv", sep = ""))
```

| Tên file                                                                                                                                     | Vị trí                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| TD_dps_application_final.Rmd                                                                                                                 | Application                                                                                                                                  |
| #write.csv(surv_full, paste("./result_summary_", surv_names,".csv", sep = "")) done <- readline("The result is saved") odbcClose(dbhandle) } | #write.csv(surv_full, paste("./result_summary_", surv_names,".csv", sep = "")) done <- readline("The result is saved") odbcClose(dbhandle) } |

## Đầu ra

| Tên file                      | Vị trí                    |
|-------------------------------|---------------------------|
| result_summary_td_app_pwc.csv | TD_code_final\Application |

## 4. Lịch sử tài liệu

| Ngày   | Phiên bản   | Mô tả             | Chỉnh sửa bởi   | Phê duyệt bởi   |
|--------|-------------|-------------------|-----------------|-----------------|
|        |             | Bản thảo đầu tiên |                 |                 |