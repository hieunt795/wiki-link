



## **Dự án Tư vấn Phương pháp luận hoàn thiện khung quản lý tài sản nợ - tài sản có (ALM)**

## **Giao phẩm BC03.03.06: Hướng dẫn sử dụng mô hình cho Thấu chi**

### Tháng 08, năm 2021 **BẢN CHÍNH THỨC**

![](_page_0_Picture_3.jpeg)

![](_page_0_Picture_4.jpeg)

![](_page_0_Picture_5.jpeg)

# <span id="page-1-0"></span>**Lưu ý quan trọng**

Báo cáo này được thực hiện theo Hợp đồng cung cấp dịch vụ giữa Công ty TNHH Tư vấn PricewaterhouseCooper Việt Nam (PwC Việt Nam) và Ngân hàng TMCP An Bình ("ABBank") ngày 24 tháng 09 năm với các điều khoản và điều kiện đi kèm. Báo cáo này dành riêng cho việc sử dụng nội bộ và nhằm phục vụ lợi ích của ABBank và không được sử dụng bởi hoặc phục vụ cho lợi ích của bất kỳ đối tượng nào khác ("Bên Thứ Ba").

Bên thứ ba không được phép sử dụng Báo cáo này trừ khi đã ký Cam kết miễn trừ trách nhiệm cho PwC Việt Nam và gửi Cam kết này đến PwC Việt Nam hoặc nhận được một thông báo từ PwC Việt Nam về các trách nhiệm liên quan của công ty đối với Bên Thứ Ba.

Bất kỳ Bên Thứ Ba nào sử dụng và đọc báo cáo này trái với các điều khoản nêu trên, thì Bên Thứ Ba đó phải chấp nhận và đồng ý với các điều khoản sau:

- 1. Công việc được thực hiện bởi PwC Việt Nam theo các yêu cầu của khách hàng mà báo cáo này được gửi đến và được thực hiện chỉ dành riêng cho lợi ích và mục đích sử dụng của chính khách hàng mà báo cáo này được gửi đến.
- 2. Báo cáo này được thực hiện theo các yêu cầu của khách hàng mà báo cáo này được gửi đến và có thể không bao gồm tất cả những quy trình/ thủ tục có thể được cho là cần thiết cho mục đích của Bên Thứ Ba.
- 3. PwC Việt Nam, các giám đốc, nhân viên và các bên có liên quan của PwC Việt Nam sẽ không gánh chịu hay chấp nhận bất kỳ nghĩa vụ hay trách nhiệm nào đối với Bên Thứ Ba, dù là nghĩa vụ theo hợp đồng hay ngoài hợp đồng (bao gồm nhưng không giới hạn bởi sự bất cẩn và vi phạm các nghĩa vụ theo quy định của pháp luật), và sẽ không chịu trách nhiệm đối với bất kỳ tổn thất, thiệt hại hoặc phí tổn dưới bất kỳ hình thức nào phát sinh bởi hoặc liên quan đến Bên Thứ Ba do việc sử dụng báo cáo này, hoặc bất kỳ hậu quả nào khác do việc Bên Thứ Ba sử dụng báo cáo này. Ngoài ra, Bên Thứ Ba chấp nhận rằng báo cáo này không được dùng để tham chiếu hoặc trích dẫn toàn bộ hoặc từng phần, trong bất kỳ bản cáo bạch, bản đăng ký, tài liệu chào bán, tài liệu công bố ra công chúng, các hồ sơ vay, các thỏa thuận hoặc tài liệu khác và không công bố báo cáo này nếu không được sự chấp thuận trước bằng văn bản của PwC Việt Nam.

Các thông tin, số liệu thống kê và các ý kiến (gọi là "thông tin") trong báo cáo này được thực hiện bởi PwC Việt Nam từ các nguồn tài liệu có sẵn do ABBank cung cấp và trên trang web của ABBank trong khuôn khổ của dự án này và qua các buổi thảo luận được tổ chức với các lãnh đạo Ngân hàng.

PwC Việt Nam lập báo cáo này dựa trên các thông tin nhận được và có được và trên cơ sở rằng các thông tin được cung cấp bởi Ngân hàng là chính xác và hoàn chỉnh. Các thông tin trong báo cáo này không nhằm mục đích kiểm toán, không được sao chép, mô phỏng, phân phát, sử dụng một phần hoặc toàn bộ báo cáo này cho các mục đích khác ngoài mục đích đã được nêu trong Thỏa thuận giữa hai bên về Nội dung công việc thực hiện.

## *Mục lục*

| Lưu ý quan trọng                                                                   | 2  |
|------------------------------------------------------------------------------------|----|
| 1. Phương pháp luận và giả định                                                    | 4  |
| 1.1. Phương pháp luận                                                              | 4  |
| 1.2. Giả định và lưu ý mô hình                                                     | 4  |
| 1.2.1. Thời gian trích xuất dữ liệu                                                | 4  |
| 1.2.2. Xác định khoản trả trước / đúng hạn                                         | 4  |
| 1.2.3. Độ tin cậy                                                                  | 4  |
| 1.2.4. Nền tảng lập trình                                                          | 4  |
| 2. Quy trình                                                                       | 5  |
| 3. Quy trình lập trình                                                             | 10 |
| 3.1. Trích xuất dữ liệu                                                            | 10 |
| 3.2. Xây dựng mô hình                                                              | 15 |
| 3.2.1. Xác định thư mục làm việc xây dựng mô hình phi tham số                      | 18 |
| 3.2.2. Xác định phân khúc và phân chia bộ dữ liệu cho xây dựng mô hình phi tham số | 18 |
| 3.2.3. Xác định độ tin cậy                                                         | 19 |
| 3.2.4. Xây dựng mô hình phi tham số                                                | 19 |
| 3.2.5. Kiểm tra hồi tố và hiệu chỉnh                                               | 20 |
| 3.2.6. Hiệu chỉnh                                                                  | 23 |
| 3.2.7. Tổng hợp kết quả mô hình phi tham số                                        | 24 |
| 3.3. Ứng dụng kết quả mô hình                                                      | 25 |
| 3.3.1. Xác định thư mục làm việc ứng dụng mô hình                                  | 27 |
| 3.3.2. Phân chia bộ dữ liệu ứng dụng mô hình                                       | 27 |
| 3.3.3. Ứng dụng mô hình                                                            | 28 |
| 3.3.4. Tổng hợp kết quả ứng dụng mô hình                                           | 30 |
| 4. Lịch sử tài liệu                                                                | 31 |

## <span id="page-3-0"></span>*1. Phương pháp luận và giả định*

### <span id="page-3-1"></span>*1.1. Phương pháp luận*

Văn bản này trình bày các bước để làm mô hình hành vi trả trước/đúng hạn và hành vi tiêu dùng cho danh mục Thấu chi (TC) theo phương pháp Phân tích duy trì (Survival Analysis). Nhân sự xây dựng mô hình được khuyến nghị tham khảo **Giao phẩm BC03.03.05: Phương pháp luận cho mô hình Thấu chi** nhằm hiểu rõ phương pháp luận đầy đủ.

### <span id="page-3-2"></span>*1.2. Giả định và lưu ý mô hình*

### <span id="page-3-3"></span>**1.2.1.** *Thời gian trích xuất dữ liệu*

Dữ liệu cho TC được trích xuất từ 1/10/2015 đến 30/09/2020.

#### <span id="page-3-4"></span>**1.2.2.** *Xác định khoản trả trước / đúng hạn*

Hành vi trả nợ trước hạn được xác định là các khoản thanh toán được khách hàng thực hiện trước / đúng ngày trả nợ theo lịch/hợp đồng.

Dựa trên hệ thống dữ liệu của Ngân hàng, hành vi trả nợ được xác định là Ngày trả nợ thực tế.

Hành vi trả nợ hạn được xác định là trước / đúng hạn nếu ngày trả nợ thực tế (Ngày báo cáo – Rep\_date trong bảng ALM\_Overdraft\_pmt và ALM\_Overdraft\_pmt\_update\_2 không xảy ra sau ngày thanh toán theo hợp đồng – Pmt\_date): Rep\_date <= Pmt\_date.

#### <span id="page-3-5"></span>**1.2.3.** *Độ tin cậy*

Mức độ tin cậy nhằm xác định khoảng sai số cho phép trong kết quả dự báo của mô hình.

Độ tin cậy được khuyến nghị lấy tại 99%.

### <span id="page-3-6"></span>**1.2.4.** *Nền tảng lập trình*

Mô hình được xây dựng trên 2 nền tảng chính:

- SQL server: nền tảng Oracle SQL server
- R Studio: Mô hình được xây dựng trên R 3.5.2 of R phiên bản mới nhất hiện tại, với giao diện bởi RStudio 1.2.1335. Phiên bản mới nhất của R và R Studio có thể được tải về từ <https://cran.r-project.org/bin/windows/base/> và Tinn-R cùng R-Studio <https://www.rstudio.com/products/rstudio/download/>

Các library cần có để thực hiện xây dựng mô hình

library(ggplot2) library(tidyr) library(sqldf) library(dplyr) library(data.table) library(zoo) library(lubridate)

## <span id="page-4-0"></span>*2. Quy trình*

Mô hình hành vi tiêu dùng và hành vi trả trước / đúng hạn thanh toán cho TC được xây dựng theo phương pháp Phân tích duy trì (Survival Analysis) phi tham số.

Mô hình hiện được lưu tại thư mục của Ngân hàng tại **07. ALM PROJECT\04. DU LIEU MHHV\OVER DRAFT Deliverables Round 3\OD\_code\_final**.

Quy trình xây dựng mô hình được chia thành hai bước chính như sau:

- (1) Trích xuất và xử lý dữ liệu
- (2) Xây dựng mô hình

![](_page_4_Picture_6.jpeg)

### Trích xuất dữ liệu Xây dựng mô hình

| STT | Quy trình                                                                             | Mô tả                                                                                                                                                                                                                            | Thư mục   | Tên tệp        | Nền tảng   |
|-----|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------|------------|
|     | Bước 1: Trích xuất dữ<br>liệu                                                         |                                                                                                                                                                                                                                  |           |                |            |
| 1.1 | Tạo bảng<br>ALM_overdraft_full_data                                                   | Bảng dữ<br>liệu phục vụ<br>cho mô hình hành vi tiêu<br>dùng tín dụng                                                                                                                                                             | Modelling | OD_extract.txt | SQL Server |
| 1.2 | Tạo bảng<br>ALM_od_pmt_final                                                          | Bảng thanh toán thấu chi cập nhật ngày trả<br>nợ<br>theo hợp đồng và bổ<br>sung thêm các tài khoản<br>còn thiếu                                                                                                                  | Modelling | OD_extract.txt | SQL Server |
| 1.3 | Tạo bảng<br>ALM_Overdraft_pmt_final                                                   | Bảng dữ<br>liệu phục vụ<br>cho mô hình hành trả<br>nợ<br>trước / đúng hạn                                                                                                                                                        | Modelling | OD_extract.txt | SQL Server |
| 1.4 | Tạo bảng<br>ALM_Overdraft_pmt_final_<br>study<br>ALM_Overdraft_pmt_fianl_<br>test     | Bảng dữ<br>liệu phục vụ<br>tính toán hành vi trả<br>nợ<br>gồm số<br>tiền thanh toán, dư nợ<br>Thấu chi, khoảng<br>cách ngày trả<br>nợ<br>thực tế<br>so với ngày trả<br>nợ<br>theo<br>hợp đồng của phân khúc cá nhân (CN)         | Modelling | OD_extract.txt | SQL Server |
| 1.5 | Tạo bảng<br>ALM_Overdraft_pmt_final_<br>study_1<br>ALM_Overdraft_pmt_fianl_<br>test_1 | Bảng dữ<br>liệu phục vụ<br>tính toán hành vi trả<br>nợ<br>gồm số<br>tiền thanh toán, dư nợ<br>Thấu chi, khoảng<br>cách ngày trả<br>nợ<br>thực tế<br>so với ngày trả<br>nợ<br>theo<br>hợp đồng của phân khúc phi cá nhân (Non-CN) | Modelling | OD_extract.txt | SQL Server |

| 1.6 | Tạo bảng<br>ALM_Overdraft_full_data_s<br>tudy<br>ALM_Overdraft_<br>full_data_test    | Bảng dữ<br>liệu phục vụ<br>tính toán hành vi tiêu dùng<br>gồm số<br>tiền vay thấu chi, hạn mức được cấp,<br>khoảng cách ngày trả<br>nợ<br>thực tế<br>so với ngày trả<br>nợ<br>theo hợp đồng của phân khúc cá nhân (CN) | Modelling | OD_extract.txt   | SQL Server |
|-----|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------|------------|
|     | Bước 2: Xây dựng mô hình                                                             |                                                                                                                                                                                                                        |           |                  |            |
|     | a. Mô hình hành vi trả<br>trước / đúng hạn                                           |                                                                                                                                                                                                                        |           |                  |            |
| 2.1 | Xác định thư mục làm việc                                                            | Thư mục làm việc là nơi chứa mô hình cùng tất<br>cả<br>các giá trị<br>đầu vào và đầu ra sau khi chạy<br>code.                                                                                                          | Modelling | Overdraft_pr.Rmd | Rmd        |
| 2.2 | Xác định phân khúc<br>và<br>phân chia<br>dữ<br>liệu study,<br>kiểm tra và hiệu chỉnh | Lựa chọn phân khúc được lưu tại SQL Server<br>để<br>đưa vào mô hình                                                                                                                                                    | Modelling | Overdraft_pr.Rmd | Rmd        |
| 2.3 | Xác định độ<br>tin cậy                                                               | Độ<br>tin cậy được lấy là 0.99                                                                                                                                                                                         | Modelling | Overdraft_pr.Rmd | Rmd        |
| 2.4 | Xây dựng mô hình                                                                     | Bao gồm xây dựng đường cong duy trì<br>(survival_curv) cho dữ<br>liệu study<br>và tính PR tại<br>từng khoảng cách thanh toán trước hạn                                                                                 | Modelling | Overdraft_pr.Rmd | Rmd        |
| 2.5 | Kiểm tra hồi tố                                                                      | Bao gồm xây dựng đường cong duy trì<br>(survival_curv) cho dữ<br>liệu test<br>và tính PR tại<br>từng khoảng cách thanh toán trước hạn<br>Đánh giá kết quả<br>từ<br>2 bộ<br>dữ<br>liệu study và test                    | Modelling | Overdraft_pr.Rmd | Rmd        |
| 2.6 | Hiệu chỉnh                                                                           | Hiệu chỉnh những giá trị<br>không đạt từ<br>kiểm tra<br>hồi tố.<br>Kết quả<br>sau hiệu chỉnh là kết quả<br>cuối cùng của<br>mô hình                                                                                    | Modelling | Overdraft_pr.Rmd | Rmd        |

| 2.7 | Tổng hợp và xuất file kết<br>quả                                                     | Kết quả<br>được tổng hợp lại thành dạng bảng và<br>lưu tại Modelling<br>trong thư mục làm việc                                                                                                         | Modelling | Overdraft_pr.Rmd | Rmd |
|-----|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------|-----|
|     | b. Mô hình hành vi tiêu dùng Thấu chi                                                |                                                                                                                                                                                                        |           |                  |     |
| 2.1 | Xác định thư mục làm việc                                                            | Thư mục làm việc là nơi chứa mô hình cùng tất<br>cả<br>các giá trị<br>đầu vào và đầu ra sau khi chạy<br>code.                                                                                          | Modelling | Overdraft_wr.Rmd | Rmd |
| 2.2 | Xác định phân khúc<br>và<br>phân chia<br>dữ<br>liệu study,<br>kiểm tra và hiệu chỉnh | Lựa chọn phân khúc được lưu tại SQL Server<br>để<br>đưa vào mô hình                                                                                                                                    | Modelling | Overdraft_wr.Rmd | Rmd |
| 2.3 | Xác định độ<br>tin cậy                                                               | Độ<br>tin cậy được lấy là 0.99                                                                                                                                                                         | Modelling | Overdraft_wr.Rmd | Rmd |
| 2.4 | Xây dựng mô hình                                                                     | Bao gồm xây dựng đường cong duy trì<br>(survival_curv) cho dữ<br>liệu study<br>và tính WR<br>tại<br>từng khoảng cách thanh toán trước hạn                                                              | Modelling | Overdraft_wr.Rmd | Rmd |
| 2.5 | Kiểm tra hồi tố                                                                      | Bao gồm xây dựng đường cong duy trì<br>(survival_curv) cho dữ<br>liệu test<br>và tính WR<br>tại<br>từng khoảng cách thanh toán trước hạn<br>Đánh giá kết quả<br>từ<br>2 bộ<br>dữ<br>liệu study và test | Modelling | Overdraft_wr.Rmd | Rmd |
| 2.6 | Hiệu chỉnh                                                                           | Hiệu chỉnh những giá trị<br>không đạt từ<br>kiểm tra<br>hồi tố.<br>Kết quả<br>sau hiệu chỉnh là kết quả<br>cuối cùng của<br>mô hình                                                                    | Modelling | Overdraft_wr.Rmd | Rmd |
| 2.7 | Tổng hợp và xuất file kết<br>quả                                                     | Kết quả<br>được tổng hợp lại thành dạng bảng và<br>lưu tại Modelling<br>trong thư mục làm việc                                                                                                         | Modelling | Overdraft_wr.Rmd | Rmd |

| 3.1 | Xác định thư mục làm việc        | Thư mục làm việc là nơi chứa mô hình cùng tất<br>cả<br>các giá trị<br>đầu vào và đầu ra sau khi chạy<br>code. | Application | Overdraft_app.Rmd | Rmd |
|-----|----------------------------------|---------------------------------------------------------------------------------------------------------------|-------------|-------------------|-----|
| 3.2 | Xác định bộ<br>dữ<br>liệu        | Lựa chọn bcf_ccf<br>được lưu tại SQL Server<br>để<br>đưa vào mô hình                                          | Application | Overdraft_app.Rmd | Rmd |
| 3.3 | Ứng<br>dựng mô hình              | Ứng dụng mô hình để<br>ra kết quả<br>bcf và survival<br>rate cho từng tuổi                                    | Application | Overdraft_app.Rmd | Rmd |
| 3.4 | Tổng hợp và xuất file kết<br>quả | Kết quả<br>được tổng hợp lại thành dạng bảng và<br>lưu tại Application<br>trong thư mục làm việc              | Application | Overdraft_app.Rmd | Rmd |

## <span id="page-9-0"></span>*3. Quy trình lập trình*

### <span id="page-9-1"></span>**3.1. Trích xuất dữ liệu**

#### **Đầu vào**

| Nguồn dữ liệu              | Vị trí     |
|----------------------------|------------|
| ALM_Overdraft              | SQL Server |
| ALM_Overdraft_pmt          | SQL Server |
| ALM_Overdraft_pmt_update_2 | SQL Server |
| ALM_Overdraft_schedule     | SQL Server |

| Tên file                                                                                                                              | Vị trí    |  |
|---------------------------------------------------------------------------------------------------------------------------------------|-----------|--|
| Overdraft_pts_data_extract                                                                                                            | Modelling |  |
| Use BANTAICHINH                                                                                                                       |           |  |
| Go                                                                                                                                    |           |  |
| /* Step 1: Trích xuất các trường dữ liệu cần dùng cho hành vi tiêu dùng thẻ tín dụng */                                               |           |  |
| Drop table ##ALM_Over_draft_data                                                                                                      |           |  |
| select rep_date,Acc_Id, Biz_Line, EOD_Bal, EOD_Limit, ISNULL(Use_Amt,0) Use_amt, [Expiry_Date]<br>into ##ALM_Over_draft_data          |           |  |
| from ALM_Over_Draft<br>where EOD_limit is not null and [Expiry_Date] is not null and [Expiry_Date] != '1900-01-01' and EOD_Bal <0 and |           |  |
| EOD_Limit !=0<br>Loại bỏ các trường hợp không phải là OD va cac truong hop bi loi limit                                               |           |  |
| /*Step 2: Fixed biz_line*/                                                                                                            |           |  |
| Tạo bảng cố định Biz_line đầu tiên cho từng account<br>drop table ##First_biz_line                                                    |           |  |
| select * into ##First_biz_line from                                                                                                   |           |  |
| (select Acc_id, biz_line, ROW_NUMBER() over (partition by acc_id order by rep_date) as rn                                             |           |  |
| from ##ALM_Over_draft_data) a<br>where a.rn =1                                                                                        |           |  |
| fix biz_line of each account                                                                                                          |           |  |
| drop table ALM_overdraft_full_data<br>select * into ALM_overdraft_full_data3193969                                                    |           |  |
| from ( select                                                                                                                         |           |  |
| a.rep_date                                                                                                                            |           |  |
| , a.acc_id<br>, b.Biz_Line                                                                                                            |           |  |
| , a.eod_bal                                                                                                                           |           |  |
| , a.eod_limit<br>, a.Use_amt                                                                                                          |           |  |
| , [Expiry_Date]                                                                                                                       |           |  |

```
Tên file
                                                                                     Vi trí
from ##ALM Over draft_data A
left join ( select acc_id, case when biz_line = 'CN' then 'CN'
                                                             else 'Non-CN' end Biz_line from ##First_biz_line) b
on A.Acc_ID = b.acc_id) c
--- xử lý các trường hợp sử dụng vượt han mức
drop table ##treat_amount_od
select rep date, acc id. biz line. EOD Bal, EOD Limit*factor EOD Limit, Use Amt, [Expiry date]
into ##treat_amount_od
from
(select * , ceiling(1.00*abs(use amt)/eod limit) factor
from ALM overdraft full data
where eOD_limit < abs(use_amt)
) a --15.173 rows
--xóa bỏ các trường hợp sử dụng vượt hạn mức và thay thế bằng dữ liệu sau khi xử lý
delete from ALM overdraft full data
where EOD limit < abs(use amt) --15.173 rows
insert into ALM overdraft full data
select * from ##treat_amount_od --15.173 rows
/* Step 3: create overdraft data with payment update*/
drop table ##OD_pmt
select Rep_date, acc_id, act_pmt, pmt_date
into ##OD pmt
from ALM Over Draft PMT
where pmt_date is not null
-- không lấy những khoản pmt date null)
insert into ##OD_pmt
select Rep_date, acc_id, act_pmt, pmt_date
from ALM_Overdraft_pmt_update_2
where pmt_date is not NULL
-- remove duplicate records in payment table
drop table ALM_od_pmt_final
select *
into ALM_od_pmt_final --367748
(select *, row_number()over (partition by rep_date, acc_id, act_pmt order by pmt_date) as duplicate
from ##OD_pmt) a
where duplicate =1
drop table ALM_overdraft_pmt_final
select rep date
          , acc_id
          , isnull(act_pmt,0) act_pmt
          , isnull(pmt_date,[Expiry_Date]) pmt_date
```

```
Tên file Vị trí
         , EOD_Bal_lag
         , Biz_line
into ALM_overdraft_pmt_final
from (
select b.rep_date, a.acc_id, a.act_pmt
                 , pmt_date
                 ,b.EOD_Bal_lag, b.Biz_line
                 ,b.[Expiry_Date] 
from ALM_od_pmt_final a
right join
                          (select dateadd(day,+1,Rep_date) Rep_date, 
                          -- nối bảng payment với bảng số dư theo quy tắc nối ngày báo cáo ở bảng payment với ngày 
trước đó tại bảng số dư
                                   Acc_id, Biz_line, EOD_Bal EOD_Bal_lag, [Expiry_Date] 
                                   from ALM_overdraft_full_data ) b
on a.Acc_ID = b.acc_id and a.Rep_Date = b.Rep_Date) c
/*Step 4: Tính khoảng cách từ ngày trả nợ thực tế so với ngày trả nợ theo hợp đồng. Xác định hành vi trả nợ, hành vi sử
dụng thẻ tín dụng */
-------------------------------------DU LIEU DUOC CHIA THEO TY LE 4 NAM VA 1 NAM CHO BO STUDY VA TEST--------------
-------------------------
--Withdrawal amount---
drop table ALM_overdraft_full_data_study --391 rows
select [datediff], sum(eod_limit) eod_limit,
                 -sum(use_amt) use_amt into ALM_overdraft_full_data_study
from (select * from
                                   (select Rep_Date,acc_id,biz_line
                                   , use_amt, eod_limit 
                                   , datediff(day, rep_date, expiry_date) as [datediff] from ALM_overdraft_full_data) c
                                   where rep_date < '2019-10-01'and biz_line ='CN' and [datediff]>=0 and 
[datediff]<=390
                                   ) a
group by [datediff]
drop table ALM_overdraft_full_data_test --391 rows
select [datediff], sum(eod_limit) eod_limit,
                 -sum(use_amt) use_amt into ALM_overdraft_full_data_test
from (select * from 
                                   (select Rep_Date,acc_id,biz_line
                                   , use_amt, eod_limit
                                   , datediff(day, rep_date, expiry_date) as [datediff] from ALM_overdraft_full_data) c
                                   where rep_date >= '2019-10-01' and biz_line ='CN' and [datediff]>=0 and 
[datediff]<=390
                                   ) a
group by [datediff]
```

```
Tên file Vị trí
--prepayment---
drop table Alm_overdraft_pmt_final_study ----391 rows
select [datediff], -sum(eod_Bal_lag) eod_Bal_lag,
                sum(act_pmt) act_pmt into Alm_overdraft_pmt_final_study
from (select rep_date, acc_id, pmt_date,[datediff], EOD_Bal_lag,
                         case when act_pmt > abs(EOD_Bal_lag) then abs(EOD_Bal_lag) --nếu trả nhiều hơn số dư 
thì cap payment bằng số dư
                                          else act_pmt end act_pmt 
                         from 
                                 (select *
                                 , datediff(day, rep_date, pmt_date) as [datediff] from ALM_overdraft_pmt_final) c
                                 where rep_date < '2019-10-01' and biz_line ='CN' and [datediff]>=0 and 
[datediff]<=390
                                 ) a
group by [datediff]
drop table Alm_overdraft_pmt_final_test --391 rows
select [datediff], -sum(eod_Bal_lag) eod_Bal_lag,
                sum(act_pmt) act_pmt into Alm_overdraft_pmt_final_test
from (select rep_date, acc_id, pmt_date,[datediff], EOD_Bal_lag,
                         case when act_pmt > abs(EOD_Bal_lag) then abs(EOD_Bal_lag) --nếu trả nhiều hơn số dư 
thì cap payment bằng số dư
                                          else act_pmt end act_pmt 
                         from 
                                 (select *
                                 , datediff(day, rep_date, pmt_date) as [datediff] from ALM_overdraft_pmt_final) c
                                 where rep_date >= '2019-10-01' and biz_line ='CN' and [datediff]>=0 and 
[datediff]<=390
                                 ) a
group by [datediff]
-----------------------------------------DU LIEU DUOC CHIA THEO TY LE 70-30 CHO BO STUDY VA TEST--------------------------
-------------
---- ALM_od_acc_study
--select top 70 percent Acc_ID into ALM_od_acc_study from
-- (select *, NEWID() new_id
-- from (select distinct Acc_ID from ALM_overdraft_full_data
-- where Biz_line = 'CN') a
-- ) b
---- ALM_od_acc_test
--select a.Acc_ID into ALM_od_acc_test from
-- (select distinct Acc_ID from ALM_overdraft_full_data
-- where Biz_line = 'CN') a
-- left join
-- (select distinct Acc_ID from ALM_od_acc_study) b
-- on a.Acc_ID = b.Acc_ID
--where b.Acc_ID is null
--/*Step 4: Tính khoảng cách từ ngày trả nợ thực tế so với ngày trả nợ theo hợp đồng. Xác định hành vi trả nợ, hành vi 
sử dụng thẻ tín dụng */
```

```
Tên file
                                                                                       Vị trí
----Withdrawal amount---
--drop table ALM_overdraft_full_data_study --391 rows
--select [datediff], sum(eod limit) eod limit,
                  -sum(use_amt) use_amt into ALM_overdraft_full_data_study
--from (select c.* from
                                   (select Rep_Date, acc_id, biz_line, use_amt, eod_limit, datediff(day, rep_date,
expiry date) as [datediff] from ALM overdraft full data) c.
                                   (select Acc_ID from ALM_od_acc_study) b
                                   where c.[datediff]>=0 and c.[datediff]<=390 and c.Acc ID = b.Acc ID
--group by [datediff]
--drop table ALM_overdraft_full_data_test --391 rows
--select [datediff], sum(eod_limit) eod_limit,
                  -sum(use amt) use amt into ALM overdraft full data test
--from (select c.* from
                                   (select Rep Date, acc id, biz line, use amt, eod limit, datediff(day, rep date,
expiry date) as [datediff] from ALM overdraft full data) c.
                                   (select Acc ID from ALM od acc test) b
                                   where c.[datediff]>=0 and c.[datediff]<=390 and c.Acc ID = b.Acc ID
                                   ) a
--group by [datediff]
----prepayment---
--drop table Alm overdraft pmt final study ----391 rows
--select [datediff], -sum(eod_Bal_lag) eod_Bal_lag,
                  sum(act_pmt) act_pmt into Alm_overdraft_pmt_final_study
--from (select c.Rep_date, c.Acc_ID, c.pmt_date, c.[datediff], c.EOD_Bal_lag,
                           case when c.act_pmt > abs(c.EOD_Bal_lag) then abs(c.EOD_Bal_lag) --néu trả nhiều hơn
số dư thì cap payment bằng số dư
                                            else c.act_pmt end act_pmt
                          from
                                   (select *, datediff(day, rep_date, pmt_date) as [datediff] from
ALM_overdraft_pmt_final) c,
                                   (select Acc_ID from ALM_od_acc_study) b
                                   where c.[datediff]>=0 and c.[datediff]<=390 and c.Acc_ID = b.Acc_ID
                                   ) a
--group by [datediff]
--drop table
                 Alm_overdraft_pmt_final_test --391 rows
--select [datediff], -sum(eod_Bal_lag) eod_Bal_lag,
                  sum(act_pmt) act_pmt into Alm_overdraft_pmt_final_test
--from (select c.Rep_date, c.Acc_ID, c.pmt_date, c.[datediff], c.EOD_Bal_lag,
                           case when c.act_pmt > abs(c.EOD_Bal_lag) then abs(c.EOD_Bal_lag) --néu trả nhiều hơn
số dư thì cap payment bằng số dư
                                            else c.act_pmt end act_pmt
                           from
                                   (select *, datediff(day, rep_date, pmt_date) as [datediff] from
ALM_overdraft_pmt_final) c,
                                   (select Acc ID from ALM od acc test) b
```

| Tên file                    |     | Vị trí                                                              |
|-----------------------------|-----|---------------------------------------------------------------------|
| <br><br>group by [datediff] | ) a | where c.[datediff]>=0 and c.[datediff]<=390 and c.Acc_ID = b.Acc_ID |

<sup>\*\*\*</sup> Hiện tại dữ liệu đang chia bộ Study và Test theo dữ liệu 4 năm và 1 năm. Ngân hàng có thể chia lại dữ liệu theo tỷ lệ 70% và 30% cho bộ Study và Test bằng cách Uncomment các dòng từ phần DU LIEU DUOC CHIA THEO TY LE 70-30 CHO BO STUDY VA TEST trở đi trong SQL. Để Uncomment ngân hàng có thể bôi đen tất cả các dòng cần Uncomment và sử dụng tổ hợp phím Ctrl + K rồi Ctrl + C.

#### **Đầu ra**

| Tên file                      | Vị trí     |
|-------------------------------|------------|
| ALM_Overdraft_pmt_final_study | SQL Server |
| ALM_Overdraft_pmt_final_test  | SQL Server |
| ALM_Overdraft_full_data_study | SQL Server |
| ALM_Overdraft_full_data_test  | SQL Server |

### <span id="page-14-0"></span>**3.2. Xây dựng mô hình**

### **Tổng quan thao tác kỹ thuật**

Tạo folder OD\_code\_final

Bước 1: chạy function "survi()"

Bước 2: Nhập đường dẫn thư mục làm việc tương ứng

![](_page_14_Picture_10.jpeg)

Bước 3: Nhập server dữ liệu trích xuất của Thấu chi từ SQL

![](_page_14_Picture_12.jpeg)

Bước 4: Nhập database dữ liệu trích xuất của Thấu chi từ SQL

![](_page_15_Picture_0.jpeg)

Bước 5: Nhập ID dữ liệu trích xuất của Thấu chi từ SQL

![](_page_15_Picture_2.jpeg)

Bước 6: Nhập password dữ liệu trích xuất của Thấu chi từ SQL

![](_page_15_Picture_4.jpeg)

Bước 7: Nhập dữ liệu xây dựng mô hình

![](_page_15_Picture_6.jpeg)

Bước 8: Nhập dữ liệu kiểm tra hồi tố

![](_page_16_Figure_0.jpeg)

Bước 9: Nhập tên phân khúc xây dựng mô hình

![](_page_16_Picture_2.jpeg)

Bước 10: Nhập mức độ tin cậy cho mô hình

![](_page_16_Picture_4.jpeg)

Hiện thị kết quả thông báo xây dựng mô hình

| Tên file         | Mô tả                                                                        |
|------------------|------------------------------------------------------------------------------|
| Overdraft_wr.Rmd | Code xây dựng mô hình phi tham số cho hành vi tiêu<br>dùng Thấu chi          |
| Overdraft_pr.Rmd | Code xây dựng mô hình phi tham số cho hành vi<br>thanh toán trước / đúng hạn |

### <span id="page-17-0"></span>**3.2.1. Xác định thư mục làm việc xây dựng mô hình phi tham số**

#### **Code**

| Tên file                                          | Vị trí    |
|---------------------------------------------------|-----------|
| Overdraft_pr.Rmd / Overdraft_wr.Rmd               | Modelling |
| library(dplyr)                                    |           |
| library(zoo)                                      |           |
| library(lubridate)                                |           |
| library(openxlsx)                                 |           |
| library(RODBC)                                    |           |
| library(svDialogs)                                |           |
| library(ggplot2)                                  |           |
| survi <- function(){                              |           |
| ##### chuan bi va trien khai du lieu #####        |           |
| ### Dat thu muc lam viec (working directory - wd) |           |
| setwd(choose.dir())#Chi chon den folder           |           |

### <span id="page-17-1"></span>**3.2.2. Xác định phân khúc và phân chia bộ dữ liệu cho xây dựng mô hình phi tham số**

| Tên file                                                                                                                                                                                                         | Vị trí                                                                                                                  |  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|--|
| Overdraft_wr.Rmd                                                                                                                                                                                                 | Modelling                                                                                                               |  |
| #Nhap du lieu phan khuc OD                                                                                                                                                                                       |                                                                                                                         |  |
|                                                                                                                                                                                                                  | server_sql <- svDialogs::dlg_input(message = "Which server is the model input: ", default = "10.32.8.10,8899")\$res %>% |  |
| as.character()                                                                                                                                                                                                   |                                                                                                                         |  |
| database_sql <- svDialogs::dlg_input(message = "Which database is the model input:", default = "BANTAICHINH")\$res                                                                                               |                                                                                                                         |  |
| %>% as.character()                                                                                                                                                                                               |                                                                                                                         |  |
| id_sql <- svDialogs::dlg_input(message = "Which id is the model input:")\$res %>% as.character()<br>password_sql <- svDialogs::dlg_input(message = "Which password is the model input:")\$res %>% as.character() |                                                                                                                         |  |
| driver_sql <- paste('driver={SQL                                                                                                                                                                                 |                                                                                                                         |  |
| Server};server=',server_sql,';database=',database_sql,';uid=',id_sql,';pwd=',password_sql, sep="")                                                                                                               |                                                                                                                         |  |
| dbhandle <- odbcDriverConnect(driver_sql)                                                                                                                                                                        |                                                                                                                         |  |
| #chon study data                                                                                                                                                                                                 |                                                                                                                         |  |
|                                                                                                                                                                                                                  | table_sql1 <- svDialogs::dlg_input(message = "Withdrawal: Choose study data grouped by datediff from actual payment     |  |
| date to contractual payment date: ")\$res %>% as.character()                                                                                                                                                     |                                                                                                                         |  |
| sql1 <- paste('select * from ',table_sql1)                                                                                                                                                                       |                                                                                                                         |  |
| OD_study <- sqlQuery(dbhandle,sql1)                                                                                                                                                                              |                                                                                                                         |  |
| names(OD_study) <- c("datediff","Limit","Usage")                                                                                                                                                                 |                                                                                                                         |  |
| OD_study <- OD_study%>%<br>arrange(-datediff)                                                                                                                                                                    |                                                                                                                         |  |
| #chon test data                                                                                                                                                                                                  |                                                                                                                         |  |
| table_sql2 <- svDialogs::dlg_input(message = "Withdrawal: Choose test data grouped by datediff from actual payment                                                                                               |                                                                                                                         |  |
| date to contractual payment date: ")\$res %>% as.character()                                                                                                                                                     |                                                                                                                         |  |
| sql2 <- paste('select * from ',table_sql2)                                                                                                                                                                       |                                                                                                                         |  |
| OD_test <- sqlQuery(dbhandle,sql2)                                                                                                                                                                               |                                                                                                                         |  |
| names(OD_test) <- c("datediff","Limit","Usage")                                                                                                                                                                  |                                                                                                                         |  |
| OD_test <- OD_test%>%                                                                                                                                                                                            |                                                                                                                         |  |
| arrange(-datediff)                                                                                                                                                                                               |                                                                                                                         |  |

```
seg_names <- svDialogs::dlg_input(message = "Segment name: ")$res %>% as.character()
Overdraft pr.Rmd
                                                            Modelling
#Nhap du lieu phan khuc OD
 server_sql <- svDialogs::dlg_input(message = "Which server is the model input: ", default = "10.32.8.10,8899")$res %>%
 database_sql <- svDialogs::dlg_input(message = "Which database is the model input:", default = "BANTAICHINH")$res
%>% as.character()
 id sql <- svDialogs::dlg input(message = "Which id is the model input:")$res %>% as.character()
 password_sql <- svDialogs::dlg_input(message = "Which password is the model input:")$res %>% as.character()
 driver sql <- paste('driver={SQL
Server];server=',server_sql,';database=',database_sql,';uid=',id_sql,';pwd=',password_sql, sep="")
 dbhandle <- odbcDriverConnect(driver_sql)
 #chon study data
 table_sql1 <- svDialogs::dlg_input(message = "Prepayment: Choose study data grouped by datediff from actual payment
date to contractual payment date: ")$res %>% as.character()
 sql1 <- paste('select * from ',table sql1)
 OD_study <- sqlQuery(dbhandle,sql1)
 names(OD study) <- c("datediff","OS","prepayment")</pre>
 OD study <- OD study%>%
  arrange(-datediff)
 #chon test data
 table_sql2 <- svDialogs::dlg_input(message = "Prepayment: Choose test data grouped by datediff from actual payment
date to contractual payment date: ")$res %>% as.character()
 sql2 <- paste('select * from ',table_sql2)
 OD_test <- sqlQuery(dbhandle,sql2)
 names(OD_test) <- c("datediff", "OS", "prepayment")
 OD test <- OD test%>%
  arrange(-datediff)
 seg_names <- svDialogs::dlg_input(message = "Segment name: ")$res %>% as.character()
```

### <span id="page-18-0"></span>3.2.3. Xác định độ tin cậy

#### Code

| Tên file                                                                                                                                  | Vị trí    |  |
|-------------------------------------------------------------------------------------------------------------------------------------------|-----------|--|
| Overdraft_pr.Rmd Overdraft_wr.Rmd                                                                                                         | Modelling |  |
| conf_lvl <- svDialogs::dlg_input(message = "Confident level(99% recommend): ",default = "0.99")\$res %>% as.numeric()#nhap muc do tin cay |           |  |

### <span id="page-18-1"></span>3.2.4. Xây dựng mô hình phi tham số

| Tên file                                                                                                                               | Vị trí    |
|----------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Overdraft_wr.Rmd                                                                                                                       | Modelling |
| OD_study\$Usage[is.na(OD_study\$Usage)] <- 0 svv_rate_study <- 1-OD_study\$Usage[1:nrow(OD_study)]/OD_study\$Limit[1:(nrow(OD_study))] |           |
| ### rate tbl table                                                                                                                     |           |

```
rate_tbl <- cbind.data.frame(OD_study$datediff[1:nrow(OD_study)], svv_rate_study)
 names(rate_tbl) <- c("datediff", "svv_rate_study")
 rate_tbl$conf_int <- OD_study$Usage[1:nrow(OD_study)]/
  OD_study$Limit[1:(nrow(OD_study))]/(
   OD_study$Limit[1:(nrow(OD_study))]-OD_study$Usage[1:nrow(OD_study)]
 rate_tbl$conf_int <- sapply(1:nrow(rate_tbl), function(x){
  sum(rate_tbl$conf_int[1:x])
})
 rate_tbl$conf_int <- -qnorm((1-conf_lvl)/2)*rate_tbl$svv_rate_study*sqrt(rate_tbl$conf_int)
 rate_tbl$svv_rate_up_study <- rate_tbl$svv_rate_study + rate_tbl$conf_int
 rate_tbl$svv_rate_low_study <- rate_tbl$svv_rate_study - rate_tbl$conf_int
 rate_tbl$WR <- OD_study$Usage[1:nrow(OD_study)]/OD_study$Limit[1:(nrow(OD_study))]
Overdraft_pr.Rmd
                                                           Modelling
############ MODELLING
 OD_study$prepayment[is.na(OD_study$prepayment)] <- 0
 svv_rate_study <- 1-OD_study$prepayment[1:nrow(OD_study)]/OD_study$OS[1:(nrow(OD_study))]
 ### rate tbl table
 rate_tbl <- cbind.data.frame(OD_study$datediff[1:nrow(OD_study)], svv_rate_study)
 names(rate_tbl) <- c("datediff", "svv_rate_study")
 rate_tbl$conf_int <- OD_study$prepayment[1:nrow(OD_study)]/
  OD study$OS[1:(nrow(OD study))]/(
   OD study$OS[1:(nrow(OD study))]-OD study$prepayment[1:nrow(OD study)]
 rate_tbl$conf_int <- sapply(1:nrow(rate_tbl), function(x){</pre>
  sum(rate_tbl$conf_int[1:x])
 rate_tbl$conf_int <- -qnorm((1-conf_lvl)/2)*rate_tbl$svv_rate_study*sqrt(rate_tbl$conf_int)
 rate_tbl$svv_rate_up_study <- rate_tbl$svv_rate_study + rate_tbl$conf_int
 rate_tbl$svv_rate_low_study <- rate_tbl$svv_rate_study - rate_tbl$conf_int
 rate tbl$PR <- OD study$prepayment[1:nrow(OD study)]/OD study$OS[1:(nrow(OD study))]
```

### <span id="page-19-0"></span>3.2.5. Kiểm tra hồi tố và hiệu chỉnh

| Tên file                                                                                                                        | Vị trí                    |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| Overdraft_wr.Rmd                                                                                                                | Modelling                 |
| OD_test\$Usage[is.na(OD_test\$Usage)] <- 0 svv_rate_test <- 1-OD_test\$Usage[1:nrow(OD_test)]/OD_test\$Limit[1:(nrow(OD_test))] |                           |
| rate_tbl_test <- cbind.data.frame(OD_test\$datediff[1:nrow(0 names(rate_tbl_test) <- c("datediff", "svv_rate_test")             | OD_test)], svv_rate_test) |

```
### rate_tbl_test table
 rate_tbl_test$conf_int <- OD_test$Usage[1:nrow(OD_test)]/
  OD_test$Limit[1:(nrow(OD_test))]/(
   OD_test$Limit[1:(nrow(OD_test))]-OD_test$Usage[1:nrow(OD_test)]
 rate_tbl_test$conf_int <- sapply(1:nrow(rate_tbl_test), function(x){</pre>
  sum(rate_tbl_test$conf_int[1:x])
 rate tbl test$conf int <- -qnorm((1-conf lvl)/2)*rate tbl test$svv rate test*sqrt(rate tbl test$conf int)
 rate_tbl_test$svv_rate_up_test <- rate_tbl_test$svv_rate_test + rate_tbl_test$conf_int
 rate tbl test$svv rate low test <- rate tbl test$svv rate test - rate tbl test$conf int
 rate_tbl_test$WR <- OD_test$Usage[1:nrow(OD_test)]/OD_test$Limit[1:(nrow(OD_test))]
 ##### final table #####
 final <- merge(rate\_tbl[c(1,2,4,5,6)], \ rate\_tbl\_test[c(1,2,4,5,6)], \ by = 1, \ all = T)
 final <- final %>% arrange(-datediff)
 final <- sapply(final, function(x){
  a \leftarrow na.locf(x)
  c(rep(1, nrow(final) - length(a)), a)
 })%>%as.data.frame()
 final$diff <- final$WR.y - final$WR.x
 for (i in (1:(nrow(final)))) {
  if (final diff[i] < 0)
     final$diff[i] <-0
  }
}
 final$backtest <- final$svv_rate_low_study <= final$svv_rate_up_test
###choosing calibrate WR or not
 calibration <- dlg input(message = c("1 = Yes, calibrate",
                          "2 = No calibration"),
                 default = "2")$res
 repeat{
  if (calibration %!in% c("1", "2")) {
   dlg_message("Input must be 1,2", type = "ok")
    calibration <- dlg_input(message = c("1 = Yes, calibrate",
                            "2 = NO calibration"),
                    default = "2")$res
  } else {break}
}
 if (calibration == "1"){
  final$CDR_final <- final$CDR.x*final$backtest + final$CDR.y*(1-final$backtest)#ket qua backtest + hieu chinh survival
rate
  svv calib <- 1-final$CDR final
  svv_calib <- sapply(1:length(svv_calib), function(x){</pre>
   prod(svv_calib[1:x])})
  final$svv final <- svv calib
 } else {
  final$CDR_final <- final$CDR.x
  svv_calib <- 1-final$CDR_final
```

```
svv_calib <- sapply(1:length(svv_calib), function(x){
  prod(svv_calib[1:x])})
  final$svv_final <- svv_calib
}</pre>
```

#### Overdraft\_pr.Rmd

#### Modelling

```
##### Backtest + Calibrating #####
 OD test$prepayment[is.na(OD test$prepayment)] <- 0
 svv_rate_test <- 1-OD_test$prepayment[1:nrow(OD_test)]/OD_test$OS[1:(nrow(OD_test))]
 rate tbl test <- cbind.data.frame(OD test$datediff[1:nrow(OD test)], svv rate test)
 names(rate_tbl_test) <- c("datediff", "svv_rate_test")
 ### rate_tbl_test table
 rate_tbl_test$conf_int <- OD_test$prepayment[1:nrow(OD_test)]/
  OD test$OS[1:(nrow(OD test))]/(
   OD_test$OS[1:(nrow(OD_test))]-OD_test$prepayment[1:nrow(OD_test)]
 rate tbl test$conf int <- sapply(1:nrow(rate tbl test), function(x){
  sum(rate_tbl_test$conf_int[1:x])
 rate_tbl_test$conf_int <- -qnorm((1-conf_lvl)/2)*rate_tbl_test$svv_rate_test*sqrt(rate_tbl_test$conf_int)
 rate_tbl_test$svv_rate_up_test <- rate_tbl_test$svv_rate_test + rate_tbl_test$conf_int
 rate_tbl_test$svv_rate_low_test <- rate_tbl_test$svv_rate_test - rate_tbl_test$conf_int
 rate_tbl_test$PR <- OD_test$prepayment[1:nrow(OD_test)]/OD_test$OS[1:(nrow(OD_test))]
 ##### final table #####
 final <- merge(rate tbl[c(1,2,4,5,6)], rate tbl test[c(1,2,4,5,6)], by = 1, all = T)
 final <- final %>% arrange(-datediff)
 final <- sapply(final, function(x){
  a \leftarrow na.locf(x)
  c(rep(1, nrow(final) - length(a)), a)
 })%>%as.data.frame()
 final$diff <- final$PR.x - final$PR.y
 for (i in (1:(nrow(final)))) {
  if \{final diff[i] < 0\}
    final$diff[i] <-0
  }
}
 final$backtest <- final$svv rate low test <= final$svv rate up study
###choosing calibrate PR or not
 calibration <- dlg_input(message = c("1 = Yes, calibrate",
                         "2 = No calibration"),
                 default = "2")$res
 repeat(
  if (calibration %!in% c("1"."2")) {
   dlg message("Input must be 1.2", type = "ok")
   calibration <- dlg_input(message = c("1 = Yes, calibrate",
                           "2 = NO calibration").
                   default = "2")$res
  } else {break}
```

```
if (calibration == "1"){
    final$CDR_final <- final$CDR.x*final$backtest + final$CDR.y*(1-final$backtest)#ket qua backtest + hieu chinh survival
rate
    svv_calib <- 1-final$CDR_final
    svv_calib <- sapply(1:length(svv_calib), function(x){
        prod(svv_calib[1:x])})
    final$svv_final <- svv_calib
} else {
    final$CDR_final <- final$CDR.x
    svv_calib <- 1-final$CDR_final
    svv_calib <- sapply(1:length(svv_calib), function(x){
        prod(svv_calib[1:x])})
    final$svv_final <- svv_calib
}
```

## <span id="page-22-0"></span>3.2.6. Hiệu chỉnh

| Tên file                                                                             | Vị trí                |
|--------------------------------------------------------------------------------------|-----------------------|
| Overdraft_wr.Rmd                                                                     | Modelling             |
| ##### final table #####                                                              |                       |
| final <- merge(rate_tbl[c(1,2,4,5,6)], rate_tbl_test[c(1,2,4,5,                      | 6)], by = 1, all = T) |
| final <- final %>% arrange(-datediff)                                                |                       |
| final <- sapply(final, function(x){                                                  |                       |
| a <- na.locf(x)                                                                      |                       |
| c(rep(1, nrow(final) - length(a)), a)                                                |                       |
| })%>%as.data.frame()                                                                 |                       |
| final\$diff <- final\$WR.y - final\$WR.x                                             |                       |
|                                                                                      |                       |
| for (i in (1:(nrow(final)))) {                                                       |                       |
| if (final\$diff[i] < 0){                                                             |                       |
| final\$diff[i] <-0                                                                   |                       |
| }                                                                                    |                       |
| }                                                                                    |                       |
|                                                                                      |                       |
| final\$backtest <- final\$svv_rate_low_study <= final\$svv_rate                      | te_up_test            |
| final\$WR_calib <- final\$WR.x*final\$backtest +                                     |                       |
| final\$WR.y*(1-final\$backtest)#ket qua backtest + hieu chi                          | nh survival rate      |
| Inaly virty (1 inaly backtosty met qua backtost + filed chillif sal vival fate       |                       |
| svv_calib <- 1-final\$WR_calib                                                       |                       |
| svv_calib <- sapply(1:length(svv_calib), function(x){                                |                       |
| prod(svv_calib[1:x])})                                                               |                       |
|                                                                                      |                       |
| final\$svv_calib <- svv_calib                                                        |                       |
| Overdraft_pr.Rmd                                                                     | Modelling             |
| ##### final table #####                                                              |                       |
| final <- merge(rate_tbl[c(1,2,4,5,6)], rate_tbl_test[c(1,2,4,5,6)], by = 1, all = T) |                       |
| final <- final %>% arrange(-datediff)                                                |                       |

```
 final <- sapply(final, function(x){
 a <- na.locf(x)
 c(rep(1, nrow(final) - length(a)), a)
 })%>%as.data.frame()
 final$diff <- final$PR.x - final$PR.y
 for (i in (1:(nrow(final)))) {
 if (final$diff[i] < 0){
 final$diff[i] <-0
 }
 }
 final$backtest <- final$svv_rate_low_test <= final$svv_rate_up_study
 final$PR_calib <- final$PR.x*final$backtest +
 final$PR.y*(1-final$backtest)#ket qua backtest + hieu chinh survival rate
 svv_calib <- 1-final$PR_calib
 svv_calib <- sapply(1:length(svv_calib), function(x){
 prod(svv_calib[1:x])})
 final$svv_calib <- svv_calib
```

### <span id="page-23-0"></span>**3.2.7. Tổng hợp kết quả mô hình phi tham số**

| Tên file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Vị trí    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Overdraft_wr.Rmd                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Modelling |
| ###### result summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |           |
| write.csv(final, paste("./result_summary_WR_",seg_names,".csv", sep = ""))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |           |
| ggsave(paste("./survival_curv_WR_",seg_names,".jpeg", sep = ""),<br>ggplot(data = final, aes(x = datediff)) +<br>geom_line(aes(y = svv_calib), color = "blue", size = 1) +<br>xlab("datediff") + xlim(max(final\$datediff),min(final\$datediff)) +<br>ylab("Survival calibrated") + ylim(0,1),<br>device = "jpeg",<br>width = 50.8,<br>height = 28.575,<br>units = "cm")<br>ggsave(paste("./WR_",seg_names,".jpeg", sep = ""),<br>ggplot(data = final, aes(x = datediff)) +<br>geom_line(aes(y = WR_calib), color = "blue", size = 1)+<br>xlab("datediff") + xlim(max(final\$datediff),min(final\$datediff)) +<br>ylab("WR calibrated") + ylim(0,max(final\$WR_calib)),<br>device = "jpeg",<br>width = 50.8,<br>height = 28.575,<br>units = "cm") |           |
| done <- readline("The result is saved in OD_code_final")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |           |

```
 odbcClose(dbhandle)
}
Overdraft_pr.Rmd Modelling
##### result summary
 write.csv(final, paste("./result_summary_pr_",seg_names,".csv", sep = ""))
 ggsave(paste("./survival_curv_pr_",seg_names,".jpeg", sep = ""),
 ggplot(data = final, aes(x = datediff)) + 
 geom_line(aes(y = svv_calib), color = "blue", size = 1) + 
 xlab("datediff") + xlim(max(final$datediff),min(final$datediff)) +
 ylab("Survival calibrated") + ylim(0,1),
 device = "jpeg",
 width = 50.8,
 height = 28.575,
 units = "cm")
 ggsave(paste("./PR_",seg_names,".jpeg", sep = ""),
 ggplot(data = final, aes(x = datediff)) + 
 geom_line(aes(y = PR_calib), color = "blue", size = 1)+ 
 xlab("datediff") + xlim(max(final$datediff),min(final$datediff)) +
 ylab("PR calibrated") + ylim(0,max(final$PR_calib)),
 device = "jpeg",
 width = 50.8,
 height = 28.575,
 units = "cm") 
 done <- readline("The result is saved in OD_code_final")
 odbcClose(dbhandle)
}
```

#### **Đầu ra**

| Tên file                                                                                                                                                                                                                          | Vị trí    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| result_summary_pr_od_modelling_pwc.csv<br>result_summary_WR_ od_modelling_pwc.csv<br>survival_curv_pr_ od_modelling_pwc.jpeg<br>survival_curv_WR_ od_modelling_pwc.jpeg<br>PR_ od_modelling_pwc.jpeg<br>WR_ od_modelling_pwc.jpeg | Modelling |

### <span id="page-24-0"></span>**3.3. Ứng dụng kết quả mô hình**

### **Tổng quan thao tác kỹ thuật**

Tại folder Application

Bước 1: Chạy function od\_app()

Bước 2: Nhập đường dẫn thư mục làm việc tương ứng

Bước 3: Nhập server dữ liệu trích xuất của thấu chi từ SQL

![](_page_25_Figure_2.jpeg)

Bước 4: Nhập database dữ liệu trích xuất của thấu chi từ SQL

![](_page_25_Picture_4.jpeg)

Bước 5: Nhập ID dữ liệu trích xuất của thấu chi từ SQL

![](_page_25_Picture_6.jpeg)

Bước 6: Nhập password dữ liệu trích xuất của thấu chi từ SQL

![](_page_25_Picture_8.jpeg)

Bước 7: Nhập dữ liệu trích xuất của bcf\_ccf

![](_page_26_Picture_0.jpeg)

Bước 8: Nhập tên phân khúc ứng dụng cho mô hình

![](_page_26_Picture_2.jpeg)

Bước 9: Nhập dữ liệu cho ứng dụng mô hình

Hiển thị thông báo kết quả xây dựng mô hình

### <span id="page-26-0"></span>**3.3.1. Xác định thư mục làm việc ứng dụng mô hình**

#### **Code**

| Tên file              | Vị trí      |
|-----------------------|-------------|
| Overdraft_app.Rmd     | Application |
| library(dplyr)        |             |
| library(zoo)          |             |
| library(RODBC)        |             |
| library(svDialogs)    |             |
|                       |             |
| od_app <- function(){ |             |
| setwd(choose.dir())   |             |

### <span id="page-26-1"></span>**3.3.2. Phân chia bộ dữ liệu ứng dụng mô hình**

| Tên file | Vị trí |
|----------|--------|
|          |        |

```
Overdraft_app.Rmd
                                                            Application
#nhap file bcf ccf
server_sql <- svDialogs::dlg_input(message = "Which server is the model input:", default = "10.32.8.10,8899")$res
%>% as.character()
 database_sql <- svDialogs::dlg_input(message = "Which database is the model input:", default = "BANTAICHINH")$res
%>% as.character()
 id_sql <- svDialogs::dlg_input(message = "Which id is the model input:")$res %>% as.character()
 password_sql <- svDialogs::dlg_input(message = "Which password is the model input:")$res %>% as.character()
 driver_sql <- paste('driver={SQL
Server):server='.server sql.':database='.database sql.':uid='.id sql.':pwd='.password sql. sep="")
 dbhandle <- odbcDriverConnect(driver_sql)
 od table sql <- svDialogs::dlg input(message = "Which bcf ccf table is the model input: ")$res %>% as.character()
 od sql <- paste('select * from '.od table sql)
 od <- sqlQuery(dbhandle,od_sql)
 names(od) <- c("datediff", "os", "limit")
 od <- od[order(od$datediff, decreasing =TRUE),]
 seg_names <- svDialogs::dlg_input(message = "Segment name: ")$res %>% as.character()#dat ten cho phan khuc
 # sury_names <- syDialogs::dlg_input(message = "Survival rate name: ")$res %>% as.character()#dat ten cho bang
survival rate
 #nhap file survival rate
 pr <- read.csv(choose.files(multi = F.
                    caption = "INSERT PR"),
            stringsAsFactors=F)[c(2, 13)]
 wr <- read.csv(choose.files(multi = F,
                    caption = "INSERT WR").
            stringsAsFactors=F)[c(2, 13)]
```

### <span id="page-27-0"></span>3.3.3. Ứng dung mô hình

| Tên file                                                     | Vị trí      |
|--------------------------------------------------------------|-------------|
| Overdraft_app.Rmd                                            | Application |
| cashflow <- lapply(1:nrow(od), function(x){                  |             |
| ## max_age = max age in schedual table                       |             |
| max_datediff <- max(od\$datediff[x])                         |             |
| ## create zzz temp table with age + day to maturity          |             |
| zzz <- data.frame(                                           |             |
| datediff = max_datediff:0,                                   |             |
| days = 0:max_datediff                                        |             |
| )                                                            |             |
| ## add CPR by left join zzz with cpr on age                  |             |
| zzz <- merge.data.frame(zzz, pr, by = c("datediff"), all.x = |             |
| zzz <- merge.data.frame(zzz, wr, by = c("datediff"), all.x = | = T)        |
| zzz <- merge.data.frame(zzz, od, by = c("datediff"), all.x : | = T)        |
| zzz[is.na(zzz)] <- 0                                         |             |
| zzz <- zzz[order(zzz\$datediff, decreasing =TRUE),]          |             |
| zzz\$cf <- 0                                                 |             |
| zzz\$cf[nrow(zzz)] <- zzz\$os[1]                             |             |
| zzz\$payment <- 0                                            |             |

```
zzz$usage <- 0
   zzz$bcf <- 0
   if (zzz$datediff == 0){
     zzz$payment[1] <- zzz$os[1]*zzz$PR_calib[1]
     zzz$usage[1] <- zzz$limit[1] * zzz$WR_calib[1]</pre>
     zzz$bcf[1] <- zzz$payment[1] - zzz$usage[1]</pre>
   } else {
     i = 2
      repeat {
      if(i > max_datediff) {
       break
      } else {
       zzz$payment[i] <- zzz$os[i-1]*zzz$PR_calib[i]
       zzz$usage[i] <- zzz$limit[i-1] * zzz$WR_calib[i]
      if (zzz$payment[i] - zzz$usage[i] >= zzz$os[i-1]) {
       zzz$bcf[i] <- zzz$payment[i] - zzz$usage[i]
       if (zzz\$os[i] > 0) {
        zzz$payment[i] <- 0
       break
      } else {
       zzz$os[i] <- zzz$os[i-1] - zzz$payment[i] + zzz$usage[i]
       zzz$limit[i] <- zzz$limit[i-1]
       zzz$bcf[i] <- zzz$payment[i] - zzz$usage[i]
       i = i+1
       }
      }
    }
   ## loop to calculating each row
   zzz <- zzz[1:nrow(zzz), c(2,1,3,4,5,6,7,8,9,10)]
   zzz <- zzz[order(zzz$days),]
})
bucket <- data.frame(bucket = c(1, 7, 30, 90, 180, 360, 10000000))
bucket_name <- c("Daily", "2-7 days", "8-30 days",
            "31-90 days", "91-180 days", "181-360 days", "over a year") #naming the time
CCF_all <-
 sapply(cashflow, function(x){
  x$cumsum <- cumsum(x$cf)
  a <- merge.data.frame(bucket, x, by = 1, all.x = T)$cumsum
  a[is.na(a)] <- x$os[1]
  a <- c(a[[1]], diff(a))
 }) %>% t() %>% as.data.frame()
 BCF_all <-
 sapply(cashflow, function(x){
```

```
 x\$cumsum <- cumsum(x\$bcf) \\ a <- merge.data.frame(bucket, x, by = 1, all.x = T)\$cumsum \\ a[is.na(a)] <- x\$cumsum[nrow(x)] \\ a <- c(a[[1]], diff(a)) \\ a \\ \}) %>% t() %>% as.data.frame()
```

## <span id="page-29-0"></span>3.3.4. Tổng hợp kết quả ứng dụng mô hình

#### Code

| Tên file                                                           | Vị trí        |
|--------------------------------------------------------------------|---------------|
| Overdraft_app.Rmd                                                  | Application   |
| final <- rbind( sapply(CCF_all, sum), sapply(BCF_all, sum) )       |               |
| row.names(final) <- c("CCF", "BCF") colnames(final) <- bucket_name |               |
| write.csv(final, paste("./result_summary_", seg_names,".csv'       | ', sep = "")) |
| done <- readline("The result is saved") odbcClose(dbhandle) }      |               |

#### Đầu ra

| Tên file                      | Vị trí      |
|-------------------------------|-------------|
| result_summary_od_app_pwc.csv | Application |



## *4. Lịch sử tài liệu*

| Ngày | Phiên bản | Mô tả             | Chỉnh sửa bởi | Phê duyệt bởi |
|------|-----------|-------------------|---------------|---------------|
|      |           | Bản thảo đầu tiên |               |               |