



# **Dự án Tư vấn Phương pháp luận hoàn thiện khung quản lý tài sản nợ - tài sản có (ALM)**

# **Giao phẩm BC03.03.06: Hướng dẫn sử dụng mô hình thấu chi có tham số**

# Tháng 08, năm 2021 **BẢN CHÍNH THỨC**

![](_page_0_Picture_3.jpeg)

![](_page_0_Picture_4.jpeg)

![](_page_0_Picture_5.jpeg)

# **Lưu ý quan trọng**

Báo cáo này được thực hiện theo Hợp đồng cung cấp dịch vụ giữa Công ty TNHH Tư vấn PricewaterhouseCooper Việt Nam (PwC Việt Nam) và Ngân hàng TMCP An Bình ("ABBank") ngày 24 tháng 09 năm 2020 với các điều khoản và điều kiện đi kèm. Báo cáo này dành riêng cho việc sử dụng nội bộ và nhằm phục vụ lợi ích của ABBank và không được sử dụng bởi hoặc phục vụ cho lợi ích của bất kỳ đối tượng nào khác ("Bên Thứ Ba").

Bên thứ ba không được phép sử dụng Báo cáo này trừ khi đã ký Cam kết miễn trừ trách nhiệm cho PwC Việt Nam và gửi Cam kết này đến PwC Việt Nam hoặc nhận được một thông báo từ PwC Việt Nam về các trách nhiệm liên quan của công ty đối với Bên Thứ Ba.

Bất kỳ Bên Thứ Ba nào sử dụng và đọc báo cáo này trái với các điều khoản nêu trên, thì Bên Thứ Ba đó phải chấp nhận và đồng ý với các điều khoản sau:

- 1. Công việc được thực hiện bởi PwC Việt Nam theo các yêu cầu của khách hàng mà báo cáo này được gửi đến và được thực hiện chỉ dành riêng cho lợi ích và mục đích sử dụng của chính khách hàng mà báo cáo này được gửi đến.
- 2. Báo cáo này được thực hiện theo các yêu cầu của khách hàng mà báo cáo này được gửi đến và có thể không bao gồm tất cả những quy trình/ thủ tục có thể được cho là cần thiết cho mục đích của Bên Thứ Ba.
- 3. PwC Việt Nam, các giám đốc, nhân viên và các bên có liên quan của PwC Việt Nam sẽ không gánh chịu hay chấp nhận bất kỳ nghĩa vụ hay trách nhiệm nào đối với Bên Thứ Ba, dù là nghĩa vụ theo hợp đồng hay ngoài hợp đồng (bao gồm nhưng không giới hạn bởi sự bất cẩn và vi phạm các nghĩa vụ theo quy định của pháp luật), và sẽ không chịu trách nhiệm đối với bất kỳ tổn thất, thiệt hại hoặc phí tổn dưới bất kỳ hình thức nào phát sinh bởi hoặc liên quan đến Bên Thứ Ba do việc sử dụng báo cáo này, hoặc bất kỳ hậu quả nào khác do việc Bên Thứ Ba sử dụng báo cáo này. Ngoài ra, Bên Thứ Ba chấp nhận rằng báo cáo này không được dùng để tham chiếu hoặc trích dẫn toàn bộ hoặc từng phần, trong bất kỳ bản cáo bạch, bản đăng ký, tài liệu chào bán, tài liệu công bố ra công chúng, các hồ sơ vay, các thỏa thuận hoặc tài liệu khác và không công bố báo cáo này nếu không được sự chấp thuận trước bằng văn bản của PwC Việt Nam.

Các thông tin, số liệu thống kê và các ý kiến (gọi là "thông tin") trong báo cáo này được thực hiện bởi PwC Việt Nam từ các nguồn tài liệu có sẵn do ABBank cung cấp và trên trang web của ABBank trong khuôn khổ của dự án này và qua các buổi thảo luận được tổ chức với các lãnh đạo Ngân hàng.

PwC Việt Nam lập báo cáo này dựa trên các thông tin nhận được và có được và trên cơ sở rằng các thông tin được cung cấp bởi Ngân hàng là chính xác và hoàn chỉnh. Các thông tin trong báo cáo này không nhằm mục đích kiểm toán, không được sao chép, mô phỏng, phân phát, sử dụng một phần hoặc toàn bộ báo cáo này cho các mục đích khác ngoài mục đích đã được nêu trong Thỏa thuận giữa hai bên về Nội dung công việc thực hiện.

# **Mục lục**

|        | 1. Tổng quan mô hình      |    |  |  |
|--------|---------------------------|----|--|--|
| 1.1.   | Thông tin mô hình         | 4  |  |  |
| 1.2.   | Nền tảng lập trình        | 4  |  |  |
|        | 2. Quy trình              |    |  |  |
|        | 3. Quy trình lập trình    | 9  |  |  |
| 3.1.   | Trích xuất dữ liệu        | 9  |  |  |
| 3.2.   | Phân tích tương quan      | 9  |  |  |
| 3.2.1. | Thu thập dữ liệu vĩ mô    | 11 |  |  |
| 3.2.2. | Xác định thư mục làm việc | 11 |  |  |
| 3.2.3. | Xác định phân khúc        | 11 |  |  |
| 3.2.4. | Xác định độ trễ           | 12 |  |  |
| 3.2.5. | Phân tích tương quan      | 12 |  |  |
| 3.3.   | Xây dựng mô hình          | 13 |  |  |
|        | 4. Lịch sử tài liệu       | 37 |  |  |

# <span id="page-3-0"></span>**1.Tổng quan mô hình**

### <span id="page-3-1"></span>*1.1. Thông tin mô hình*

Mô hình sử dụng chuỗi thấu chi của phân khúc khách hàng cá nhân và giả sử phân khúc này có tương quan khi thực hiện phân tích

Các phần trích xuất dữ liệu, thực hiện phân khúc tương tự như mô hình phi tham số tương ứng với sản phẩm mô hình, sẽ không trình bày lại trong tài liệu này.

### <span id="page-3-2"></span>*1.2. Nền tảng lập trình*

Mô hình được xây dựng trên 2 nền tảng chính:

SQL server: nền tảng Oracle SQL server

● R Studio: Mô hình được xây dựng trên R 4.0.3 of R – phiên bản mới nhất hiện tại, với giao diện bởi RStudio 1.3.1093. Phiên bản mới nhất của R và R Studio có thể được tải về từ [https://cran.r](https://cran.r-project.org/bin/windows/base/)[project.org/bin/windows/base/](https://cran.r-project.org/bin/windows/base/) và<https://www.rstudio.com/products/rstudio/download/>

Các library cần có để thực hiện xây dựng mô hình

- library(tseries)
- library(dplyr)
- library(plyr)
- library(zoo)
- library(lmtest)
- library(lubridate)
- library(urca)
- library(ggplot2)
- library(forecast)
- library(svDialogs)
- library(RODBC)
- library(Metrics)
- library(BBmisc)

# <span id="page-4-0"></span>**2.Quy trình**

Quy trình xây dựng mô hình được chia thành các bước chính như sau:

- 1. Trích xuất và xử lý dữ liệu
- 2. Phân tích tương quan
- 3. Xây dựng mô hình

![](_page_4_Figure_5.jpeg)

### Trích xuất và xử lý dữ liệu Phân tích tương quan Xây dựng mô hình

| STT  | Quy trình                         | Mô tả                                                                                                                                                                                                           |                | Tên tệp                         | Nền<br>tảng       |
|------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|---------------------------------|-------------------|
|      | Bước 1: Trích xuất và xử<br>lý dữ | liệu                                                                                                                                                                                                            |                |                                 |                   |
| 1.1  | Trích xuất và xử<br>lý dữ<br>liệu | Dữ<br>liệu được trích xuất từ<br>SQL Server của Ngân<br>hàng với ngày và tổng số<br>dư danh mục tương ứng<br>từ<br>01-10-2015<br>đến 30-09-2020 và được trích xuất<br>vào thẳng R                               | OD_arima_final |                                 | SQL<br>Serve<br>r |
|      | Bước 2: Phân tích tương quan      |                                                                                                                                                                                                                 |                |                                 |                   |
| 2.1  | Thu thập dữ<br>liệu vĩ mô         | Dữ<br>liệu vĩ mô cho các yếu tố<br>được thu thập bởi Ngân<br>hàng trong khoảng thời gian từ<br>01-10-2015 đến 30-<br>09-2020 và lưu trong thư mục làm việc                                                      | OD_arima_final | macro.csv                       | Rmd               |
| 2.2. | Xác định thư mục làm việc         | Thư mục làm việc là nơi chứa mô hình cùng tất cả<br>các giá trị<br>đầu vào và đầu ra sau khi chạy code.                                                                                                         | OD_arima_final | correlation_final.Rmd           | Rmd               |
| 2.3  | Xác định phân khúc                | Lựa chọn phân khúc được lưu trong thư mục làm<br>việc để<br>đưa vào phân tích tương quan                                                                                                                        | OD_arima_final | correlation_final.Rmd           | Rmd               |
| 2.4  | Xác định độ<br>trễ                | Độ<br>trễ<br>là biến đầu vào của phân tích tương quan. Độ<br>trễ<br>khuyến nghị<br>được lấy là 365 (ngày), tương ứng<br>với 1 năm                                                                               | OD_arima_final | correlation_final.Rmd           | Rmd               |
| 2.5  | Phân tích tương quan              | Tính hệ<br>số<br>tương quan với độ<br>trễ<br>(lag) xác định cho<br>biến động của dải kỳ<br>hạn Qua đêm với từng biến vĩ<br>mô và đưa ra giá trị<br>lớn nhất và nhỏ<br>nhất trong các<br>hệ<br>số<br>tương quan. | OD_arima_final | correlation_final.Rmd           | Rmd               |
| 2.6  | Lưu kết quả                       | Lưu kết quả<br>phân tích tương quan của sản phẩm vào<br>thư mục làm việc                                                                                                                                        | OD_arima_final | correlation_result_loan_pwc.csv | Rmd               |

|      | Bước 3: Xây dựng mô hình                |                                                                                                                                                                                      |                |                 |     |
|------|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|-----------------|-----|
| 3.1  | Nhập thư viện và function               | Tải các thư viện và các function mặc định vào phiên<br>làm việc của R                                                                                                                | OD_arima_final | arima_final.Rmd | Rmd |
| 3.2  | Chọn sản phẩm mô hình                   | Xác định sản phẩm (CASA, LOAN hoặc TERM<br>DEPOSIT, OVERDRAFT, CREDIT CARD) và nhập<br>chuỗi hành vi theo ngày tương ứng                                                             | OD_arima_final | arima_final.Rmd | Rmd |
| 3.3  | Nhập chuỗi hành vi                      | Nhập chuỗi hành vi từ<br>bước 1 vào phiên làm việc của<br>R                                                                                                                          | OD_arima_final | arima_final.Rmd | Rmd |
| 3.4  | Nhập dữ<br>liệu kinh tế<br>vĩ mô        | Nhập dữ<br>liệu các biến kinh tế<br>vĩ mô từ<br>bảng macro.csv<br>vào phiên làm việc của R                                                                                           | OD_arima_final | arima_final.Rmd | Rmd |
| 3.5  | Nhập kết quả<br>phân tích tương<br>quan | Nhập kết quả<br>phân tích tương quan tại bước 2 vào<br>phiên làm việc của R                                                                                                          | OD_arima_final | arima_final.Rmd | Rmd |
| 3.6  | Nhập số<br>ngày dự<br>báo               | Nhập số<br>ngày được dự<br>báo (mặc định = 365, tương<br>đương với 1 năm)                                                                                                            | OD_arima_final | arima_final.Rmd | Rmd |
| 3.7  | Tạo bảng dữ<br>liệu tổng hợp            | Tạo dữ<br>liệu tổng hợp 5 năm của biến hành vi và các<br>biến kinh tế<br>vĩ mô                                                                                                       | OD_arima_final | arima_final.Rmd | Rmd |
| 3.8  | Chọn ngày chia dữ<br>liệu               | Chọn ngày chia dữ<br>liệu là ngày đầu tiên của bộ<br>dữ<br>liệu<br>kiểm tra dưới dạng yyy-mm-dd. Mặc định là ngày chia<br>dữ<br>liệu = ngày lớn nhất của bộ<br>dữ<br>liệu -<br>1 năm | OD_arima_final | arima_final.Rmd | Rmd |
| 3.9  | Kiểm tra tính dừng                      | Kiểm tra tính dừng các biến để<br>tìm tham số<br>d                                                                                                                                   | OD_arima_final | arima_final.Rmd | Rmd |
| 3.10 | Kiểm định nhân quả                      | Kiểm định nhân quả<br>Granger và loại bỏ<br>các biến<br>không thỏa mãn                                                                                                               | OD_arima_final | arima_final.Rmd | Rmd |

| 3.11 | Kiểm định đa cộng tuyến                        | Kiểm định và loại bỏ<br>các biến gây ra đa cộng tuyến.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | OD_arima_final | arima_final.Rmd | Rmd |
|------|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|-----------------|-----|
| 3.12 | Xác định các tổ<br>hợp của X                   | Xác định các tổ<br>hợp có thể<br>có của X                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | OD_arima_final | arima_final.Rmd | Rmd |
| 3.13 | Xác định (p,q)                                 | Xác định các tổ<br>hợp (p,q) dựa trên AIC                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | OD_arima_final | arima_final.Rmd | Rmd |
| 3.14 | Dự<br>báo các biến kinh tế<br>vĩ mô            | Dự<br>báo các biến kinh tế<br>vĩ mô sử<br>dụng hàm<br>auto.arima() với p,d,q được chọn tự<br>động hoặc nhập<br>bảng dự<br>báo có sẵn cho năm dự<br>báo (năm thứ<br>6). Lưu<br>ý bảng dữ<br>liệu dự<br>báo cần phải có tên các cột và thứ<br>tự<br>các cột tương ứng với file macro.csv                                                                                                                                                                                                                                                                                 | OD_arima_final | arima_final.Rmd | Rmd |
| 3.15 | Ước lượng và dự<br>báo mô hình                 | Tiến hành ước lượng, kiểm định phần dư và dự<br>báo<br>mô hình cho tất cả<br>các tổ<br>hợp mô hình (cặp (p,q) + tổ<br>hợp X)                                                                                                                                                                                                                                                                                                                                                                                                                                           | OD_arima_final | arima_final.Rmd | Rmd |
| 3.16 | Thông báo kết quả<br>ước lượng                 | Thông báo kết quả<br>ước lượng, có bao nhiêu mô hình<br>"Đạt". Lưu ý, có lựa chọn bỏ<br>kiểm định phân phối<br>chuẩn để<br>nới lỏng mô hình khi không có mô hình nào<br>"Đạt". Nếu vẫn không có mô hình nào đạt, có lựa chọn<br>để<br>bỏ<br>qua kết quả<br>kiểm tra hồi tố<br>và dự<br>báo<br>Lưu ý:<br>•<br>Nếu lựa chọn bỏ<br>kiểm định phân phối chuẩn<br>thì dự<br>báo điểm vẫn đáng tin cậy, nhưng<br>khoảng tin cậy của dự<br>báo sẽ<br>rộng hơn<br>Nếu không mô hình nào "Đạt", dự<br>báo điểm sẽ<br>là ước<br>lượng chệch và kết quả<br>mô hình không đáng tin | OD_arima_final | arima_final.Rmd | Rmd |
| 3.17 | Đưa kết quả<br>dự<br>báo vào các dải<br>kì hạn | Đưa kết quả<br>dự<br>báo vào các dải kì hạn và tính<br>toán giá trị<br>không cộng dồn của từng dải kì hạn.<br>Xuất kết quả<br>ra thư mục làm việc                                                                                                                                                                                                                                                                                                                                                                                                                      | OD_arima_final | Result.csv      | Rmd |

# <span id="page-8-0"></span>**3.Quy trình lập trình**

# <span id="page-8-1"></span>*3.1. Trích xuất dữ liệu*

Tham khảo tài liệu của sản phẩm được mô hình tương ứng.

### <span id="page-8-2"></span>*3.2. Phân tích tương quan*

Tổng quan thao tác kỹ thuật Bước 1: Chạy function "correlation\_od"

Bước 2: Nhập đường dẫn thư mục làm việc tương ứng

![](_page_8_Figure_6.jpeg)

### Bước 3: Nhập server dữ liệu trích xuất của Thấu chi từ SQL

![](_page_8_Figure_8.jpeg)

#### Bước 4: Nhập database dữ liệu trích xuất của Thấu chi từ SQL

![](_page_8_Picture_10.jpeg)

Bước 5: Nhập ID dữ liệu trích xuất của Thấu chi từ SQL

![](_page_8_Picture_12.jpeg)

Bước 6: Nhập password dữ liệu trích xuất của Thấu chi từ SQL

![](_page_9_Picture_1.jpeg)

Bước 7: Nhập dữ liệu Thấu chi cần phân tích tương quan

![](_page_9_Picture_3.jpeg)

Bước 8: Nhập tên phân khúc cần phân tích tương quan

![](_page_9_Picture_5.jpeg)

Bước 9: Nhập dữ liệu vĩ mô cần cho phân tích tương quan

![](_page_9_Picture_7.jpeg)

Bước 10: Nhập độ trễ

![](_page_9_Picture_9.jpeg)

Hiển thị thông báo kết quả phân tích tương quan

### <span id="page-10-0"></span>**3.2.1.***Thu thập dữ liệu vĩ mô*

#### **Đầu vào**

| Nguồn dữ<br>liệu | Vị<br>trí      |
|------------------|----------------|
| macro.csv        | OD_arima_final |
| SQLServer        | OD_arima_final |

**<sup>\*</sup>Lưu ý**: trong tương lai, Ngân hàng có thể cập nhật lại các yếu tố vĩ mô được đưa vào phân tích tương quan (thêm/bớt các yếu tố; hoặc thay đổi độ dài dữ liệu), tuy nhiên cần đảm bảo dữ liệu vĩ mô mới phải tuân theo cấu trúc của file macro.csv.

### <span id="page-10-1"></span>**3.2.2.***Xác định thư mục làm việc*

#### **Code**

| Tên file                                                                                                                                                | Vị<br>trí      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| correlation_final                                                                                                                                       | OD_arima_final |
| library(dplyr)<br>library(RODBC)<br>library(svDialogs)<br>library(zoo)                                                                                  |                |
| correlation_od <- function(){<br>##### chuan bi va trien khai du lieu #####<br>### Dat thu muc lam viec (working directory - wd)<br>setwd(choose.dir()) |                |

### <span id="page-10-2"></span>**3.2.3.***Xác định phân khúc*

| Tên file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Vị<br>trí                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| correlation_final                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | OD_arima_final                                                                                                         |
| #Nhap du lieu phan khuc od<br>as.character()<br>database_sql <- svDialogs::dlg_input(message = "Which database is the model input:", default = "BANTAICHINH")\$res<br>%>% as.character()<br>id_sql <- svDialogs::dlg_input(message = "Which id is the model input:")\$res %>% as.character()<br>password_sql <- svDialogs::dlg_input(message = "Which password is the model input:")\$res %>% as.character()<br>driver_sql <- paste('driver={SQL<br>Server};server=',server_sql,';database=',database_sql,';uid=',id_sql,';pwd=',password_sql, sep="")<br>dbhandle <- odbcDriverConnect(driver_sql)<br>table_sql <- svDialogs::dlg_input(message = "Which table is the model input: ")\$res %>% as.character()<br>sql <- paste('select * from ',table_sql)<br>od <- sqlQuery(dbhandle,sql) | server_sql <- svDialogs::dlg_input(message = "Which server is the model input:", default = "10.32.8.10,8899")\$res %>% |
| ### lua chon phan khuc<br>seg_names <- svDialogs::dlg_input(message ="Which segment is the model input: ")\$res %>% as.character()<br>names(od) <- c("date", "bl")#dat ten lai cac cot trong bang du lieu input<br>od\$date <- as.Date(od\$date)#format lai cot date trong bang du lieu<br>date_min <- min(od\$date)<br>date_max <- max(od\$date)                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                        |

```
Tên file

vi trí

od <- od[order(od$date),]#sap xep cac dong theo ngay
od_date <- data.frame(date = seq(as.Date(date_min), as.Date(date_max), by = "days"))
od_all <- merge.data.frame(od_date, od, by = c("date"), all.x = T, all.y = F)
od_all$bl <- od_all$bl %>% na.locf()
```

# <span id="page-11-0"></span>3.2.4. Xác định độ trễ

#### Code

| Tên file                                                                                             | Vị trí         |  |  |  |  |
|------------------------------------------------------------------------------------------------------|----------------|--|--|--|--|
| correlation_final                                                                                    | OD_arima_final |  |  |  |  |
| ### nhap macro file macro <- read.csv(choose.files())#input du lieu cua phan khuc                    |                |  |  |  |  |
| macro\$date <- as.Date(macro\$date, "%d-%b-%y") macro <- macro[order(macro\$date),] macro\$X <- NULL |                |  |  |  |  |
| lag <- svDialogs::dlg_input(message = "Lag: ",default = "365")\$res %>% as.numeric()                 |                |  |  |  |  |

# <span id="page-11-1"></span>3.2.5. Phân tích tương quan

#### Code

| Tên file                                                                                                                                                                                                 | Vị trí          |  |  |  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|--|--|--|
| correlation_final                                                                                                                                                                                        | OD_arima_final  |  |  |  |
| <pre>colnum &lt;- as.numeric(length(macro))   correlation &lt;- sapply(2:colnum, function(x){     sapply(0:lag, function(y){         a &lt;- merge.data.frame(od_all[c(1,2)], macro[c(1,x)], #by =</pre> | = 1, all.x = T) |  |  |  |
| row.names(correlation) <- 0:lag names(correlation) <- names(macro)[2:length(macro)]                                                                                                                      |                 |  |  |  |
| <pre>### Xuat file ket qua write.csv(correlation, paste("./correlation_result_", seg_names,".csv", sep = "")) dlg_message(c("Model end")) odbcClose(dbhandle) }</pre>                                    |                 |  |  |  |
| correlation_od()                                                                                                                                                                                         |                 |  |  |  |

### Kết quả

| File                          | Vị trí         |
|-------------------------------|----------------|
| correlation_result_od_pwc.csv | OD_arima_final |

### <span id="page-12-0"></span>*3.3. Xây dựng mô hình*

Tổng quan thao tác kỹ thuật Tại thư mục làm việc Bước 1: Chạy function

Bước 2: Nhập đường dẫn thư mục làm việc tương ứng

![](_page_12_Figure_4.jpeg)

Bước 3: Chọn loại sản phẩm

![](_page_12_Figure_6.jpeg)

Bước 4: Nhập server dữ liệu trích xuất của Thấu chi từ SQL

![](_page_12_Picture_8.jpeg)

Bước 5: Nhập database dữ liệu trích xuất của Thấu chi từ SQL

![](_page_12_Picture_10.jpeg)

Bước 6: Nhập ID dữ liệu trích xuất của Thấu chi từ SQL

![](_page_13_Figure_0.jpeg)

Bước 7: Nhập password dữ liệu trích xuất của Thấu chi từ SQL

![](_page_13_Figure_2.jpeg)

Bước 8: Nhập dữ liệu Thấu chi

![](_page_13_Figure_4.jpeg)

Bước 9: Nhập file csv chứa các biến kinh tế vĩ mô

Bước 10: Nhập file csv chứa kết quả phân tích tương quan

Bước 11: Nhập số ngày dự báo

![](_page_13_Picture_10.jpeg)

Bước 12: Nhập ngày chia dữ liệu (yyyy-mm-dd)

split date là ngày đầu tiên của dữ liệu kiểm tra hồi tố. Dữ liệu làm mô hình bắt đầu từ đầu đến ngay trước split

date, phần còn lại là dữ liệu kiểm tra hồi tố

![](_page_14_Picture_1.jpeg)

Bước 13: Nhập giá trị p, q lớn nhất: Khuyến nghị là 10, như mặc định

![](_page_14_Picture_3.jpeg)

Bước 14: Lựa chọn nhập dữ liệu tương lai hoặc dự báo các biến kinh tế vĩ mô hoặc không dùng dự báo các biến kinh tế vĩ mô

![](_page_14_Figure_5.jpeg)

Lưu ý: nếu lựa chọn nhập giá trị forecast của macro thì bảng nhập vào phải có các cột tương đương với bảng macro (cột đầu tiên là date, sau đó là các giá trị tương ứng tiếp theo của macro, theo tần suất hàng ngày) và số dòng ≥ số điểm cần dự báo đã được nhập bước trên.

Ví dụ: Bảng macro

**date bond\_1y bond\_2y bond\_3y bond\_5y bond\_7y bond\_10y**

| 02/10/2015 | 4.99 | 5.44 | 5.81 | 6.39 | 6.82 | 7.27 |
|------------|------|------|------|------|------|------|
| 03/10/2015 | 4.99 | 5.44 | 5.81 | 6.39 | 6.82 | 7.27 |
| 04/10/2015 | 4.99 | 5.44 | 5.81 | 6.39 | 6.82 | 7.27 |
| 05/10/2015 | 4.98 | 5.37 | 5.72 | 6.32 | 6.81 | 7.34 |
| 06/10/2015 | 4.91 | 5.37 | 5.77 | 6.42 | 6.89 | 7.35 |
| 07/10/2015 | 4.89 | 5.36 | 5.76 | 6.41 | 6.88 | 7.36 |
| …          |      |      |      |      |      |      |
| 30/09/2020 | 0.49 | 0.58 | 0.80 | 1.39 | 1.98 | 2.65 |

Bảng dự báo của macro

| date       | bond_1y | bond_2y | bond_3y | bond_5y | bond_7y | bond_10y |
|------------|---------|---------|---------|---------|---------|----------|
| 01/07/2019 | 4.69    | 4.95    | 5.135   | 6.16    | 6.75    | 7.19     |
| 02/07/2019 | 4.69    | 4.95    | 5.135   | 6.16    | 6.75    | 7.19     |
| 03/07/2019 | 4.69    | 4.95    | 5.135   | 6.16    | 6.75    | 7.19     |
| 04/07/2019 | 4.69    | 4.95    | 5.135   | 6.16    | 6.75    | 7.19     |
| 05/07/2019 | 4.69    | 4.95    | 5.135   | 6.16    | 6.75    | 7.19     |
| 06/07/2019 | 4.705   | 4.988   | 5.164   | 6.171   | 6.75    | 7.19     |
| …          |         |         |         |         |         |          |
| 30/09/2020 | 3.141   | 3.417   | 3.552   | 3.796   | 4.21    | 4.696    |

Nếu không có biến vĩ mô nào tương quan với dữ liệu tại phần correlation. Mô hình sẽ tự đổi sang chạy ARIMA

![](_page_15_Figure_4.jpeg)

Bước 15: Lựa chọn bỏ kiểm định phân phối chuẩn (nếu không có mô hình nào đạt kiểm tra hồi tố)

![](_page_16_Figure_1.jpeg)

Bước 16: Lựa chọn bỏ qua kết quả kiểm tra hồi tố và dự báo

![](_page_16_Figure_3.jpeg)

Bước 17: Nhập tham số cho tỉ lệ MAPE để so sánh

![](_page_16_Picture_5.jpeg)

Bước 18: Lưu kết quả mô hình

![](_page_16_Picture_7.jpeg)

# **3.3.1.***Nhập thư viện và function*

| Tên file                                | Vị<br>trí      |  |  |  |  |
|-----------------------------------------|----------------|--|--|--|--|
| arima_final.Rmd                         | OD_arima_final |  |  |  |  |
| ##### library #####<br>library(tseries) |                |  |  |  |  |

```
Tên file Vị trí
library(dplyr)
library(plyr)
library(zoo)
library(lmtest)
library(lubridate)
library(urca)
library(ggplot2)
library(forecast)
library(svDialogs)
library(RODBC)
library(Metrics)
library(BBmisc)
##### function #####
# add function not in
"%!in%"<-Negate("%in%")
# add fuction for multicollinear
mtcln <- function(x){
 dt <- x
 repeat {
 vifz <- sapply(1:length(dt), function(i){
 a <- summary(
 lm(paste(names(dt)[i], "~.", sep = ""), data = dt)
 )$r.squared
 1/(1-a)
 }) 
 if(max(vifz) < 5){ break }
 dt <- dt[vifz != max(vifz)]
 }
 return(dt)
}
##### chuan bi va trien khai du lieu #####
### Dat thu muc lam viec (working directory - wd)
setwd(choose.dir("Chon folder chua mo hinh ARIMAX"))#Chon folder chua mo hinh ARIMAX
```

# **3.3.2.***Chọn sản phẩm mô hình*

| Tên file                                                                                                                                                 | Vị<br>trí      |  |  |  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|--|--|--|
| arima_final.Rmd                                                                                                                                          | OD_arima_final |  |  |  |
| ##### import #####                                                                                                                                       |                |  |  |  |
| ## import runoff                                                                                                                                         |                |  |  |  |
| user_input <- dlg_input(message = "1 = CASA, 2 = LOAN PREPAYMENT, 3 = TERM DEPOSIT, 4 = OVERDRAFT, 5 =<br>CREDIT CARD, 6 = LCBG On-BS, 7 = LCBG Off-BS", |                |  |  |  |
| default = "3")\$res                                                                                                                                      |                |  |  |  |
| repeat{                                                                                                                                                  |                |  |  |  |
| if (user_input %!in% c("1", "2", "3", "4" ,"5", "6", "7")) {                                                                                             |                |  |  |  |
| dlg_message("Input must be 1, 2, 3, 4, 5, 6, 7", type = "ok")                                                                                            |                |  |  |  |
| user_input <- dlg_input(message = "1 = CASA, 2 = LOAN PREPAYMENT, 3 = TERM DEPOSIT, 4 = OVERDRAFT, 5 =<br>CREDIT CARD, 6 = LCBG On-BS, 7 = LCBG Off-BS", |                |  |  |  |
| default = "3")\$res                                                                                                                                      |                |  |  |  |
| } else {break}<br>}                                                                                                                                      |                |  |  |  |

# 3.3.3. Nhập chuỗi hành vi

| Tên file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Vị trí            |  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--|
| arima_final.Rmd                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | OD_arima_final    |  |
| #Nhap du lieu phan khuc server_sql <- svDialogs::dlg_input(message = "Which server is the model input: ", default = "10.32.8.10,8899")\$res %>% as.character() database_sql <- svDialogs::dlg_input(message = "Which database is the model input:", default = "BANTAICHINH")\$res %>% as.character()\nid_sql <- svDialogs::dlg_input(message = "Which id is the model input:")\$res %>% as.character() password_sql <- svDialogs::dlg_input(message = "Which password is the model input:")\$res %>% as.character() driver_sql <- paste('driver={SQL Server};server=',server_sql,';database=',database_sql,';uid=',id_sql,';pwd=',password_sql, sep="") dbhandle <- odbcDriverConnect(driver_sql) table_sql <- svDialogs::dlg_input(message = "Which table is the model input: ")\$res %>% as.character() sql <- paste('select * from ',table_sql) runoff <- sqlQuery(dbhandle,sql) |                   |  |
| # bucket <- c(1, 7, 30, 90, 180, 360, 10000000)#gan ngay ch<br>bucket_short <- c(1,7,30)<br>bucket_long <- c(90,180,360)<br>bucket_td_short <- c(1,7)<br>bucket_td_long <- c(30,90,180,360)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | o cac time bucket |  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |                   |  |
| bal_bucket_short <- sapply(if(user_input == "3"){bucket_td_short} else {bucket_short}, function(b){ # format runoff\nif (user_input == "1"   user_input == "4"   user_input == "5"   user_input == "7") { runoff_add <- data.frame(date = seq(as.Date(date_max), as.Date(date_min), by = -(b))) runoff_full <- merge.data.frame(runoff_add, runoff_all, by = c("date"), all.x = T, all.y = F) runoff_full\$runoff_daily <- c(NA, diff(runoff_full\$bl)/runoff_full\$bl[1:(nrow(runoff_full)-1)]) runoff_full <- runoff_full[1:nrow(runoff_full),c(1,2)] } else if (user_input == "6") { runoff_add <- data.frame(date = seq(as.Date(date_max), as.Date(date_min), by = -(b))) runoff_full <- merge.data.frame(runoff_add, runoff, by = c("date"), all.x = T, all.y = F) runoff_full <- runoff_full[1:nrow(runoff_full),c(1,2)] runoff_full\$bl <- runoff_full\$bl %>% na.locf()     |                   |  |

```
Tên file Vị trí
 } else {
 runoff_add <- data.frame(date = seq(as.Date(date_max), as.Date(date_min), by = -(b)))
 runoff_full <- merge.data.frame(runoff_add, runoff, by = c("date"), all.x = T, all.y = F)
 runoff_full <- runoff_full[1:nrow(runoff_full),c(1,2)]
 runoff_full$bl <- runoff_full$bl %>% na.locf()
 }
```

# **3.3.4.***Nhập dữ liệu kinh tế vĩ mô*

#### **Code**

| Tên file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Vị<br>trí      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| arima_final.Rmd                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | OD_arima_final |
| ## import macro<br># import macro<br>macro_raw <- read.csv(choose.files(multi = F,<br>caption = "INSERT MACRO"),<br>stringsAsFactors=F)<br># format macro<br>macro <- data.frame(date = seq(as.Date(date_min), as.Date(date_max), by = "days"))<br>macro_raw <- macro_raw[(nrow(macro_raw)-nrow(macro)+1):nrow(macro_raw),c(2:ncol(macro_raw))]<br>macro_raw[] <- lapply(macro_raw, function(x) as.numeric(na.locf(replace(x, x=="", NA), fromLast=TRUE)))<br>macro <- cbind.data.frame(macro, macro_raw)<br>macro\$date <- as.Date(macro\$date, "%d-%b-%y")<br>macro\$X <- NULL |                |

### **3.3.5.***Nhập kết quả phân tích tương quan*

#### **Code**

| Tên file                                                                                                                                                                                                                                                                                                                         | Vị<br>trí      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| arima_final.Rmd                                                                                                                                                                                                                                                                                                                  | OD_arima_final |
| ## import correlation<br># import correlation<br>correlation <- read.csv(choose.files(multi = F,<br>caption = "INSERT CORRELATION RESULT"),<br>stringsAsFactors=F)<br># format correlation<br>correlation\$X <- NULL<br>cor_smr <- sapply(correlation, function(x){<br>max(abs(x))<br>})<br>names(cor_smr) <- names(correlation) |                |

# **3.3.6.***Nhập số ngày dự báo*

| Tên file                                                                                                                                               | Vị<br>trí      |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|--|
| arima_final.Rmd                                                                                                                                        | OD_arima_final |  |
| # input number of days forecast<br>n_forecast <- svDialogs::dlg_input(message = "Number of forecast days: ",<br>default = "365")\$res %>% as.numeric() |                |  |

# 3.3.7. Tạo bảng dữ liệu tổng hợp

#### Code

| Tên file                                                                                                                                                                                | Vị trí         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| arima_final.Rmd                                                                                                                                                                         | OD_arima_final |
| ## all_data # join table to create all data table all_data <- merge.data.frame(runoff_full, macro, by = "date", all.x = T)                                                              |                |
| # sort all data table all_data <- all_data[order(all_data\$date),] # filter macro with  correlation  > 0.4 all_data <- all_data[ names(all_data) %!in% names(cor_smr)[cor_smr <= 0.4] ] |                |

# 3.3.8. Chọn ngày chia dữ liệu cho bucket ngắn hạn

#### Code

| Tên file                                                                                                                                                                                                                                                                                                                                                                                                                           | Vị trí         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| arima_final.Rmd                                                                                                                                                                                                                                                                                                                                                                                                                    | OD_arima_final |
| <pre># input split date\nif(b==1){     splitz &lt;- as.Date(dlg_input(         "split date:",         default = as.character(max(all_data\$date) - 29)     )\$res, "%Y-%m-%d") } else if (b==7) {     splitz &lt;- as.Date(dlg_input(         "split date:",         default = as.character(max(all_data\$date) - 104)     )\$res, "%Y-%m-%d") } else if (b==30){     splitz &lt;- as.Date(dlg_input(         "split date:",</pre> |                |
| <pre>default = as.character(max(all_data\$date) - 299) )\$res, "%Y-%m-%d") }</pre>                                                                                                                                                                                                                                                                                                                                                 |                |

# 3.3.9. Kiểm tra tính dừng cho bucket ngắn hạn

| Tên file                                                                                                                                                                                  | Vị trí         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| arima_final.Rmd                                                                                                                                                                           | OD_arima_final |
| ##### Stationarity test ##### # check for macro input exist\nif (length(all_data) > 2) {    tmp <- all_data[all_data\$date < splitz ,2:length(all_data)] } else {    tmp <- all_data[2] } |                |
| <pre>if(     sapply(tmp, function(x){     #test stationarity</pre>                                                                                                                        |                |

```
 adf.test(x)$p.value
 }) %>% max() > 0.05
 ) {
 d = 1
 repeat{
 # differencing 
 tmp <- sapply(all_data[2:length(all_data)], function(x){
 diff(x, differences = d)
 }) %>% as.data.frame()
 if(
 sapply(tmp, function(x){
 #test stationarity
 adf.test(x)$p.value
 }) %>% max() <= 0.05
 ) { break }
 d = d +1
 }
 } else {
 d = 0
 }
```

# **3.3.10.** *Kiểm định nhân quả cho bucket ngắn hạn*

#### **Code**

| Tên file                                                                                                                                                                                                                                                                                                                  | Vị<br>trí      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| arima_final.Rmd                                                                                                                                                                                                                                                                                                           | OD_arima_final |
| ##### granger #####<br>if (length(tmp) >1 ) {<br>pb <- txtProgressBar(max = length(tmp)-1, min = 1, style = 3)<br>G_C <- sapply(2:length(tmp), function(x){<br># test causality<br>setTxtProgressBar(pb, x-1)<br>grangertest(tmp[[1]], tmp[[x]], order = 1)\$`Pr(>F)`[2]<br>})<br>names(G_C) <- names(tmp)[2:length(tmp)] |                |
| # filter variables that pass causality test<br>tmp <- cbind.data.frame(tmp[1], tmp[2:length(tmp)][G_C < 0.05])<br>}                                                                                                                                                                                                       |                |

# **3.3.11.** *Kiểm định đa cộng tuyến cho bucket ngắn hạn*

| Tên file                                                                                                                   | Vị<br>trí      |
|----------------------------------------------------------------------------------------------------------------------------|----------------|
| arima_final.Rmd                                                                                                            | OD_arima_final |
| ##### multicollinear #####<br>if (length(tmp) > 2) {<br>tmp <- cbind.data.frame(tmp[1],<br>mtcln(tmp[2:length(tmp)]))<br>} |                |
| # filter all_data table by tmp table result<br>all_data <- all_data[<br>names(all_data) %in% c("date", names(tmp))<br>]    |                |

# **3.3.12.** *Xác định các tổ hợp của X cho bucket ngắn hạn*

#### **Code**

```
Tên file Vị trí
arima_final.Rmd OD_arima_final
# select X
 if (length(all_data) > 2) {
 No_x <- length(all_data)-2
 # generate 1st X combinations
 X_comb <- combn(names(all_data)[3:(No_x+2)], 1) %>% 
 as.data.frame() %>% lapply(function(x){as.character(x)})
 # loop to generate X combinations
 if (No_x > 1) {
 for (i in 2:No_x) {
 X_comb <- append(X_comb, 
 combn(names(all_data)[3:(No_x+2)], i) %>% 
 as.data.frame() %>% 
 lapply(function(x){as.character(x)}))
 }
 }
 }
```

# **3.3.13.** *Xác định (p, q) cho bucket ngắn hạn*

| Tên file                                                                                                                                                                                                                                                                                            | Vị<br>trí      |  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|--|
| arima_final.Rmd                                                                                                                                                                                                                                                                                     | OD_arima_final |  |
| ##### estimating #####<br># filter study data and test data<br>all_data_std <- all_data[all_data\$date < splitz, 2:length(all_data)] %>%<br>as.data.frame()<br>all_data_tst <- all_data[all_data\$date >= splitz, 2:length(all_data)] %>%<br>as.data.frame()                                        |                |  |
| # input max p, q<br>max_p <- as.numeric(dlg_input("Max p: ", default = "10")\$res)<br>max_q <- as.numeric(dlg_input("Max q: ", default = "10")\$res)                                                                                                                                                |                |  |
| pb <- txtProgressBar(max = max_p*max_q, min = 1, style = 3)<br># estimate and calculate AIC<br>aic_result <- try(sapply(1:max_p, function(p){<br>sapply(1:max_q, function(q){<br>setTxtProgressBar(pb, (p-1)*max_q+q)<br>arima(all_data_std[1],<br>order = c(p,d,q),<br>method = "ML"               |                |  |
| )\$aic<br>})<br>}), silent = TRUE)<br>if(inherits(aic_result, "try-error")){<br>aic_result <-<br>sapply(1:max_p, function(p){<br>sapply(1:max_q, function(q){<br>setTxtProgressBar(pb, (p-1)*max_q+q)<br>arima(all_data_std[1],<br>order = c(p,d,q),<br>method = "ML", optim.method = "Nelder-Mead" |                |  |

```
Tên file Vị trí
 )$aic
 })
 })
 }
 # take smallest AIC model
 ord_qp <- which(aic_result <= sort(aic_result)[5],
 arr.ind = T) %>% as.data.frame()
 names(ord_qp) <- c("q", "p")
 ord_qp %>% as.matrix()
```

# **3.3.14.** *Dự báo các biến kinh tế vĩ mô cho bucket ngắn hạn*

| Tên file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Vị<br>trí      |  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|--|
| arima_final.Rmd                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | OD_arima_final |  |
| # choosing import X forecast or using auto.arima<br>xforecast <- dlg_input(message = c("1 = import forecast for x",<br>"2 = forecast X using auto arima",<br>"3 = forecast without X"),<br>default = "1")\$res                                                                                                                                                                                                                                                                                                                                                              |                |  |
| repeat{<br>if (xforecast %!in% c("1", "2", "3")) {<br>dlg_message("Input must be 1, 2", type = "ok")<br>xforecast <- dlg_input(message = c("1 = import forecast for x",<br>"2 = forecast X using auto arima",<br>"3 = forecast without X"),<br>default = "3")\$res<br>} else {break}<br>}                                                                                                                                                                                                                                                                                   |                |  |
| if (length(all_data) <= 2 & (xforecast==1   xforecast==2)){<br>dlg_message(c("No macro factor(X) correlates with the data. Proceed to ARIMA model."))<br>}                                                                                                                                                                                                                                                                                                                                                                                                                  |                |  |
| # running model + residual test<br>if (length(all_data) > 2 & (xforecast==1   xforecast==2)) {<br>######## forecast macro #############                                                                                                                                                                                                                                                                                                                                                                                                                                     |                |  |
| if (xforecast == "1") {<br># import forecast macro<br>forecast_macro <- read.csv(choose.files(multi = F,<br>caption = "INSERT FORECAST MACRO"),<br>stringsAsFactors=F)<br># format forecast macro<br>forecast_macro <- forecast_macro[order(forecast_macro[[1]]),]<br>forecast_macro <- forecast_macro[1:n_forecast, 2:length(forecast_macro)]<br>} else {<br># forecast macro using auto.arima<br>forecast_macro <-<br>sapply(macro[2:length(macro)], function(x){<br>forecast(auto.arima(x, max.p = 10, max.q = 10), h = n_forecast)\$mean<br>}) %>% as.data.frame()<br>} |                |  |
| # create x forecasted table (xreg)<br>xreg <- rbind.data.frame(<br>all_data_tst[2:length(all_data_tst)],<br>forecast_macro[names(all_data_tst[2:length(all_data_tst)])]                                                                                                                                                                                                                                                                                                                                                                                                     |                |  |

| Tên file | Vị<br>trí |
|----------|-----------|
| )        |           |

# **3.3.15.** *Ước lượng và dự báo mô hình cho bucket ngắn hạn*

```
Tên file Vị trí
arima_final.Rmd OD_arima_final
pb <- txtProgressBar(max = 5*length(X_comb), min = 1, style = 3)
 runtest <- lapply(1:5, function(x){
 # estimating
 lapply(1:length(X_comb), function(y){
 arimax <- arima(all_data_std[1], 
 order = c(ord_qp[[2]][[x]],d,ord_qp[[1]][[x]]),
 xreg = as.matrix(
 all_data_std[names(all_data_std) %in% X_comb[[y]]], method = "ML"
 )
 )
 # residual test
 res <- arimax$residuals
 res_adf <- adf.test(res)$p.value <= 0.05
 if(b==1){
 res_bp <- Box.test(res, lag = 365, type = "Box-Pierce",
 ord_qp[[1]][[x]] + ord_qp[[2]][[x]])$p.value <= 0.05
 } else {
 res_bp <- Box.test(res, type = "Box-Pierce",
 ord_qp[[1]][[x]] + ord_qp[[2]][[x]])$p.value <= 0.05
 }
 res_jb <- jarque.bera.test(res)$p.value > 0.05
 # forecast
 Fi <- predict(arimax, n.ahead = 1,newxreg = as.matrix(xreg[X_comb[[y]]]))$pred
 F_se <- predict(arimax, n.ahead = 1,newxreg = as.matrix(xreg[X_comb[[y]]]))$se
 a = nrow(all_data_std) + 1
 while(a<=nrow(all_data)){
 arimax <- arima(all_data[1:a,c(2:2)],
 order = c(ord_qp[[2]][[x]],d,ord_qp[[1]][[x]]),xreg = as.matrix(
 all_data_std[names(all_data_std) %in% X_comb[[y]]], method = "ML")
 )
 Fi <- rbind(Fi, predict(arimax, n.ahead=1,newxreg = as.matrix(xreg[X_comb[[y]]]))$pred)
 F_se <- rbind(F_se, predict(arimax, n.ahead=1,newxreg = as.matrix(xreg[X_comb[[y]]]))$se)
 a = a + 1
 }
 Ai <- all_data_tst[[1]]
 # MAPE calculating
 mape = 0
 i = 1
 while (i <= length(Ai)){
 if(Ai[i] != 0){
 sumabs = abs((Ai[i] - Fi[i])/Ai[i])
 }
 else{
 sumabs = 0
 }
 mape = mape + sumabs
 i = i + 1
 }
 mape = mape/nrow(all_data_tst)
```

```
Tên file Vị trí
 rs <- list(paste(ord_qp[[2]][[x]], ord_qp[[1]][[x]], sep = " "),
 X_comb[[y]],
 arimax,
 res_adf,
 res_bp,
 res_jb,
 Fi,
 F_se,
 Ai,
 mape
 )
 names(rs) <- c("order", "MEV", "arimax",
 "adf_result", "BP_result", "JB_result",
 "forecast", "forecast_SE", "backtest_actual",
 "MAPE")
 setTxtProgressBar(pb, (x-1)*length(X_comb)+y)
 rs
 })
 })
 runtest <- runtest[[1]] %>% append(runtest[[2]]) %>%
 append(runtest[[3]]) %>% append(runtest[[4]]) %>%
 append(runtest[[5]])
 } else {
 pb <- txtProgressBar(max = 5, min = 1, style = 3)
 runtest <- lapply(1:5, function(x){
 # estimating
 arimax <- arima(all_data_std[1],
 order = c(ord_qp[[2]][[x]],d,ord_qp[[1]][[x]]), method = "ML"
 )
 # residual test
 res <- arimax$residuals
 res_adf <- adf.test(res)$p.value <= 0.05
 if(b==1){
 res_bp <- Box.test(res, lag = 365, type = "Box-Pierce",
 ord_qp[[1]][[x]] + ord_qp[[2]][[x]])$p.value <= 0.05
 } else {
 res_bp <- Box.test(res, type = "Box-Pierce",
 ord_qp[[1]][[x]] + ord_qp[[2]][[x]])$p.value <= 0.05
 }
 res_jb <- jarque.bera.test(res)$p.value > 0.05
 Fi <- predict(arimax, n.ahead = 1)$pred
 F_se <- predict(arimax, n.ahead = 1)$se
 a = nrow(all_data_std) + 1
 arimax <- try(while(a<=nrow(all_data)){
 arima(all_data[1:a,c(2:2)],
 order = c(ord_qp[[2]][[x]],d,ord_qp[[1]][[x]]), method = "ML"
 )
 Fi <- rbind(Fi, predict(arimax, n.ahead=1)$pred)
 F_se <- rbind(F_se, predict(arimax, n.ahead=1)$se)
 a = a + 1
 }, silent = TRUE)
 if(inherits(arimax, "try-error")){
 while(a<=nrow(all_data)){
 arimax <- arima(all_data[1:a,c(2:2)],
 order = c(ord_qp[[2]][[x]],d,ord_qp[[1]][[x]]), method = "ML", optim.method = "Nelder-Mead"
 )
```

```
Tên file Vị trí
 Fi <- rbind(Fi, predict(arimax, n.ahead=1)$pred)
 F_se <- rbind(F_se, predict(arimax, n.ahead=1)$se)
 a = a + 1
 }
 }
 Ai <- all_data_tst[[1]]
 # MAPE
 mape = 0
 i = 1
 while (i <= length(Ai)){
 if(Ai[i] != 0){
 sumabs = abs((Ai[i] - Fi[i])/Ai[i])
 }
 else{
 sumabs = 0
 }
 mape = mape + sumabs
 i = i + 1
 }
 mape = mape/nrow(all_data_tst)
 rs <- list(paste(ord_qp[[2]][[x]], ord_qp[[1]][[x]], sep = " "),
 NA,
 arimax,
 res_adf,
 res_bp,
 res_jb,
 Fi,
 F_se,
 Ai,
 mape
 )
 names(rs) <- c("order", "MEV", "arimax",
 "adf_result", "BP_result", "JB_result",
 "forecast", "forecast_SE", "backtest_actual",
 "MAPE")
 setTxtProgressBar(pb, x)
 rs
 })
 }
```

# **3.3.16.** *Thông báo kết quả ước lượng cho bucket ngắn hạn*

| Tên file                                                                                                                                          | Vị<br>trí      |
|---------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| arima_final.Rmd                                                                                                                                   | OD_arima_final |
| # result that using all post-run test<br>strict_test_result <- runtest[<br>sapply(runtest, function(x){<br>x[[4]] + x[[5]] +x[[6]]== 3<br>})<br>] |                |
| # result using all post-run test except residual normality test (jacque-bera)<br>loose_test_result <- runtest[                                    |                |

```
Tên file Vị trí
 sapply(runtest, function(x){
 x[[4]] + x[[5]] == 2
 })
 ]
 # announcing result
 if (length(strict_test_result) == 0) {
 runtest_mess <-
 dlg_message(c("No combination passed residual test.",
 "Loosen up with only 2 test (remove jarque - bera test)?"),
 type = "yesno")$res
 } else {
 runtest_mess <-
 dlg_message(c("There is/are combination(s) passed strict residual test.",
 "Loosen up with only 2 test (remove jarque - bera test) to have more combinations?"),
 type = "yesno")$res
 }
 if (runtest_mess == "yes") {
 final <- loose_test_result
 } else {
 final <- strict_test_result
 }
 # force forecast 
 if (length(final) == 0) {
 forecast_mess <- dlg_message(c("No combination passed residual test.",
 "Proceed to forecast anyway?"),
 type = "yesno")$res
 if (forecast_mess == "yes") {
 final <- runtest
 } 
 } 
 if (length(final) == 0) {
 dlg_message("Model end. No combination passed residual test")
} else {
 final <- final[[
 which(
 sapply(final, function(x){
 x[[10]]
 }) == sapply(final, function(x){
 x[[10]]
 })%>%min()
 )
 ]]
}
}) %>% as.data.frame()
if (user_input == "3"){
 names(bal_bucket_short) <- c("Daily", "2-7")
 } else {
 names(bal_bucket_short) <- c("Daily", "2-7", "8-30")
 }
```

# **3.3.17.** *Tạo chuỗi hành vi cho bucket dài hạn*

| Tên file                                                                                         | Vị<br>trí      |
|--------------------------------------------------------------------------------------------------|----------------|
| arima_final.Rmd                                                                                  | OD_arima_final |
| bal_bucket_long <- sapply(if(user_input == "3"){bucket_td_long} else {bucket_long}, function(b){ |                |

```
Tên file
                                                                                            Vi trí
  if (user input == "1" | user input == "4" | user input == "5") {
    runoff_add_min_date <- as.Date(runoff_all$date[b+3])
    runoff full <- data.frame(matrix(ncol=5.nrow=date max - runoff add min date+1.dimnames=list(NULL.
c("date", "bl", "t3", "t2", "t1"))))
    runoff full$date <- seq(runoff add min date, as.Date(date max), by = "days")
    runoff_full$bl <- runoff_all$bl[(b+3):nrow(runoff_full_date)]
    runoff full[3] <- runoff all$bl[3:(nrow(runoff full date)-b)]
    runoff_full[4] <- runoff_all$bl[2:(nrow(runoff_full_date)-(b+1))]
    runoff_full[5] <- runoff_all$bl[1:(nrow(runoff_full_date)-(b+2))]
  } else if (user_input == "6") {
    date_min <- min(runoff$date)
    date_max <- max(runoff$date)
    runoff_full_date <- data.frame(date = seg(as.Date(date_min), as.Date(date_max), by = "days"))
    runoff_all <- merge.data.frame(runoff_full_date, runoff, by = c("date"), all.x = T, all.y = F)
    runoff_all$bl <- runoff_all$bl %>% na.locf()
    runoff_all <- runoff_all[1:nrow(runoff_all),c(1,2)]
    runoff_add_min_date <- as.Date(runoff_full_date$date[b+3])
    runoff_full <- data.frame(matrix(ncol=5,nrow=date_max - runoff_add_min_date+1,dimnames=list(NULL,
c("date", "bl", "t3", "t2", "t1"))))
    runoff full$date <- seq(runoff add min date, as.Date(date max), by = "days")
    runoff_full$bl <- runoff_all$bl[(b+3):nrow(runoff_all)]</pre>
    runoff_full[3] <- runoff_all$bl[3:(nrow(runoff_all)-b)]
    runoff full[4] <- runoff all$bl[2:(nrow(runoff all)-(b+1))]
    runoff_full[5] <- runoff_all$bl[1:(nrow(runoff_all)-(b+2))]
  } else if (user_input == "7") {
    runoff add min date <- as.Date(runoff all$date[b+3])
    runoff_full <- data.frame(matrix(ncol=5,nrow=date_max - runoff_add_min_date+1,dimnames=list(NULL,
c("date", "bl", "t3", "t2", "t1"))))
    runoff_full$date <- seq(runoff_add_min_date, as.Date(date_max), by = "days")
    runoff_full$bl <- runoff_all$bl[(b+3):nrow(runoff_full_date)]
    runoff_full[3] <- runoff_all$bl[3:(nrow(runoff_full_date)-b)]
    runoff_full[4] <- runoff_all$bl[2:(nrow(runoff_full_date)-(b+1))]
    runoff_full[5] <- runoff_all$bl[1:(nrow(runoff_full_date)-(b+2))]
    runoff_add_min_date <- as.Date(runoff$date[b+3])
    runoff full <- data.frame(matrix(ncol=5.nrow=date max - runoff add min date+1,dimnames=list(NULL,
c("date", "bl", "t3", "t2", "t1"))))
    runoff_full$date <- seq(runoff_add_min_date, as.Date(date_max), by = "days")
    runoff full$bl <- runoff$blI(b+3):nrow(runoff)1
    runoff_full[3] <- runoff$bl[3:(nrow(runoff)-b)]
    runoff_full[4] <- runoff$bl[2:(nrow(runoff)-(b+1))]
    runoff_full[5] <- runoff$bl[1:(nrow(runoff)-(b+2))]
```

### 3.3.18. Chọn ngày chia dữ liệu cho bucket dài hạn

#### Code

| Tên file                                                                                                                                                                               | Vị trí         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| arima_final.Rmd                                                                                                                                                                        | OD_arima_final |
| # input split date splitz_num <- nrow(runoff_full) * 0.2 - 1 splitz <- as.Date(dlg_input("split date:", default = as.character(max(runoff_full\$date) - splitz_num))\$res, "%Y-%m-%d") |                |

# 3.3.19. Ước lượng và dự báo mô hình cho bucket dài hạn

| Tên file        | Vị trí         |
|-----------------|----------------|
| arima_final.Rmd | OD_arima_final |

```
Tên file Vị trí
all_data_std <- runoff_full[runoff_full$date < splitz, 1:length(runoff_full)] %>% 
 as.data.frame()
 all_data_tst <- runoff_full[runoff_full$date >= splitz, 1:length(runoff_full)] %>%
 as.data.frame()
 lm_test <- lm(bl ~ t3 + t2 + t1, data = all_data_std)
 alpha_table <- data.frame(matrix(ncol=4,nrow=1))
 names(alpha_table) <- c("alpha0","alpha1","alpha2","alpha3")
 alpha_table$alpha0 <- summary(lm_test)$coefficients[,1][1]
 alpha_table$alpha1 <- summary(lm_test)$coefficients[,1][2]
 alpha_table$alpha2 <- summary(lm_test)$coefficients[,1][3]
 alpha_table$alpha3 <- summary(lm_test)$coefficients[,1][4]
 Ai_study <- all_data_std$bl
 Fi_study <- alpha_table$alpha0 + alpha_table$alpha1*all_data_std$t3[1:nrow(all_data_std)] + 
alpha_table$alpha2*all_data_std$t2[1:nrow(all_data_std)] + alpha_table$alpha3*all_data_std$t1[1:nrow(all_data_std)]
 mape_study = 0
 study = 1
 while (study <= length(Ai_study)){
 if(Ai_study[study] != 0){
 sumabs_study = abs((Ai_study[study] - Fi_study[study])/Ai_study[study])
 }
 else{
 sumabs_study = 0
 }
 mape_study = mape_study + sumabs_study
 study = study + 1
 }
 mape_study = mape_study/length(Ai_study)
 Ai_test <- all_data_tst$bl
 Fi_test <- alpha_table$alpha0 + alpha_table$alpha1*all_data_tst$t3[1:nrow(all_data_tst)] + 
alpha_table$alpha2*all_data_tst$t2[1:nrow(all_data_tst)] + alpha_table$alpha3*all_data_tst$t1[1:nrow(all_data_tst)]
 For_bal <- alpha_table$alpha0 + alpha_table$alpha1*runoff_full$bl[nrow(runoff_full)] + 
alpha_table$alpha2*runoff_full$bl[nrow(runoff_full) - 1] + alpha_table$alpha3*runoff_full$bl[nrow(runoff_full) - 2]
 mape_test = 0
 test = 1
 while (test <= length(Ai_test)){
 if(Ai_test[test] != 0){
 sumabs_test = abs((Ai_test[test] - Fi_test[test])/Ai_test[test])
 }
 else{
 sumabs_test = 0
 }
 mape_test = mape_test + sumabs_test
 test = test + 1
 }
 mape_test = mape_test/length(Ai_test)
 rs <- list(alpha_table$alpha0,
 alpha_table$alpha1,
 alpha_table$alpha2,
 alpha_table$alpha3,
 Fi_test,
 For_bal,
 Ai_test,
 mape_study,
 mape_test
 )
 names(rs) <- c("Alpha0", "Alpha1", "Alpha2", "Alpha3",
 "forecast", "forecast_balance", "backtest_actual",
 "MAPE_Study", "MAPE_Test")
 rs
 }) %>% as.data.frame()
 if (user_input == "3"){
 names(bal_bucket_long) <- c("8-30", "31-90", "91-180", "181-360") 
 } else {
 names(bal_bucket_long) <- c("31-90", "91-180", "181-360") 
 }
```



## **3.3.20.** *Đưa kết quả dự báo vào các dải kì hạn*

## **Code**

```
Tên file Vị trí
arima_final.Rmd OD_arima_final
if (user_input == "3"){
 #enter MAPE percentage 
 mape_lv <- svDialogs::dlg_input(message = "Enter MAPE percentage value: ",
 default = "0.5")$res %>% as.numeric()
 if(bal_bucket_short$Daily[10] > mape_lv){
 stop(dlg_message(paste("Model end. MAPE result is greater than ",mape_lv))$res)
 } else if (bal_bucket_short$`2-7`[10] > mape_lv) {
 stop(dlg_message(paste("Model end. MAPE result is greater than ",mape_lv))$res)
 } else if (bal_bucket_long$`8-30`[9] > mape_lv) {
 stop(dlg_message(paste("Model end. MAPE result is greater than ",mape_lv))$res)
 } else if (bal_bucket_long$`31-90`[9] > mape_lv) {
 stop(dlg_message(paste("Model end. MAPE result is greater than ",mape_lv))$res)
 } else if (bal_bucket_long$`91-180`[9] > mape_lv) {
 stop(dlg_message(paste("Model end. MAPE result is greater than ",mape_lv))$res)
 } else if (bal_bucket_long$`181-360`[9] > mape_lv) {
 stop(dlg_message(paste("Model end. MAPE result is greater than ",mape_lv))$res)
 } else {
 if (user_input %in% c("3")) {
 bucket <- c(1, 7, 30, 90, 180, 360, 10000000)#gan ngay cho cac time bucket
 bucket_name <- c("Daily", "2-7 days", "8-30 days",
 "31-90 days", "91-180 days", "181-360 days",">360 days") #gan ten cho cac time bucket
 rs_bucket <- data.frame(matrix(nrow = 7, ncol=4))
 names(rs_bucket) <- c("cummulative_runoff", "uncummulative_runoff", "balance", "MAPE")
 row.names(rs_bucket) <- bucket_name
 # calculate runoff for each time bucket
 for_bucket_1 <- bal_bucket_short$Daily["forecast"]
 for_bucket_7 <- bal_bucket_short$`2-7`["forecast"]
 for_bucket_30 <- bal_bucket_long$`8-30`["forecast_balance"]
 for_bucket_90 <- bal_bucket_long$`31-90`["forecast_balance"]
 for_bucket_180 <- bal_bucket_long$`91-180`["forecast_balance"]
 for_bucket_360 <- bal_bucket_long$`181-360`["forecast_balance"]
 rs_bucket$cummulative_runoff[1] <- abs(min((for_bucket_1$forecast[length(for_bucket_1$forecast)] -
runoff$bl[nrow(runoff)])/runoff$bl[nrow(runoff)],0))
 rs_bucket$cummulative_runoff[2] <- abs(min((for_bucket_7$forecast[length(for_bucket_7$forecast)] -
runoff$bl[nrow(runoff)])/runoff$bl[nrow(runoff)],0))
 rs_bucket$cummulative_runoff[3] <-
abs(min((for_bucket_30$forecast_balance[length(for_bucket_30$forecast_balance)] -
runoff$bl[nrow(runoff)])/runoff$bl[nrow(runoff)],0))
 rs_bucket$cummulative_runoff[4] <-
abs(min((for_bucket_90$forecast_balance[length(for_bucket_90$forecast_balance)] -
runoff$bl[nrow(runoff)])/runoff$bl[nrow(runoff)],0))
 rs_bucket$cummulative_runoff[5] <-
abs(min((for_bucket_180$forecast_balance[length(for_bucket_180$forecast_balance)] -
runoff$bl[nrow(runoff)])/runoff$bl[nrow(runoff)],0))
 rs_bucket$cummulative_runoff[6] <-
abs(min((for_bucket_360$forecast_balance[length(for_bucket_360$forecast_balance)] -
runoff$bl[nrow(runoff)])/runoff$bl[nrow(runoff)],0))
 rs_bucket$cummulative_runoff[7] <- NA
 a <- rs_bucket$cummulative_runoff
 b <- rs_bucket$cummulative_runoff
 for (i in (2:(length(bucket)-1))) {
 if (b[i]>max(na.omit(a[1:i-1]))){
 b[i] <- a[i] - max(na.omit(a[1:(i-1)]))
 } else {
 b[i] = 0
 }
```

```
Tên file
                                                                                         Vi trí
     rs bucket$uncummulative runoff <- b
     rs bucket$balance[1] <- for bucket 1$forecast[length(for bucket 1$forecast)]
     rs bucket$balance[2] <- for bucket 7$forecast[length(for bucket 7$forecast)]
     rs bucket$balance[3] <- for bucket 30$forecast balance[length(for bucket 30$forecast balance)]
     rs bucket$balance[4] <- for bucket 90$forecast balance[length(for bucket 90$forecast balance)]
     rs_bucket$balance[5] <- for_bucket_180$forecast_balance[length(for_bucket_180$forecast_balance)]
     rs bucket$balance[6] <- for bucket 360$forecast balance[length(for bucket 360$forecast balance]]
     mape_bucket_1 <- bal_bucket_short$Daily[10]
     mape_bucket_7 <- bal_bucket_short$`2-7`[10]
     mape bucket 30 <- bal bucket long\$`8-30\[9]
     mape_bucket_90 <- bal_bucket_long$`31-90`[9]
     mape_bucket_180 <- bal_bucket_long$`91-180`[9]
     mape_bucket_360 <- bal_bucket_long$`181-360`[9]
     rs_bucket$MAPE[1] <- mape_bucket_1$MAPE[1]
     rs bucket$MAPE[2] <- mape bucket 7$MAPE[1]
     rs bucket$MAPE[3] <- mape bucket 30$MAPE Test[1]
     rs_bucket$MAPE[4] <- mape_bucket_90$MAPE_Test[1]
     rs_bucket$MAPE[5] <- mape_bucket_180$MAPE_Test[1] rs_bucket$MAPE[6] <- mape_bucket_360$MAPE_Test[1]
     write.csv(rs bucket, choose.files(default = "result.csv",
                            caption = "Saving result into csv",
                            multi = F)
 odbcClose(dbhandle)
   dlg_message(c("Model end"))
} else {
   #enter MAPE percentage
  mape_lv <- svDialogs::dlg_input(message = "Enter MAPE percentage value: ",
                        default = "0.5")$res %>% as.numeric()
  if(bal bucket short$Daily[10] > mape lv){
   stop(dlg message(paste("Model end. MAPE result is greater than ",mape lv))$res)
  } else if (bal_bucket_short$`2-7`[10] > mape_lv) {
   stop(dlg_message(paste("Model end, MAPE result is greater than ".mape_lv))$res)
  } else if (bal_bucket_short$`8-30`[10] > mape_lv) {
   stop(dlg_message(paste("Model end. MAPE result is greater than ",mape_lv))$res)
  } else if (bal_bucket_long$`31-90`[9] > mape_lv) {
    stop(dlg_message(paste("Model end. MAPE result is greater than ",mape_lv))$res)
  } else if (bal_bucket_long$`91-180`[9] > mape_lv) {
   stop(dlg_message(paste("Model end, MAPE result is greater than ".mape_lv))$res)
  } else if (bal_bucket_long$`181-360`[9] > mape_lv) {
   stop(dlg_message(paste("Model end. MAPE result is greater than ",mape_lv))$res)
  } else {
    if (user_input %in% c("1", "4", "5")) {
     bucket <- c(1, 7, 30, 90, 180, 360, 10000000)#gan ngay cho cac time bucket
     bucket_name <- c("Daily", "2-7 days", "8-30 days",
               "31-90 days", "91-180 days", "181-360 days",">360 days") #gan ten cho cac time bucket
     rs_bucket <- data.frame(matrix(nrow = 7, ncol=4))
     names(rs bucket) <- c("cummulative runoff", "uncummulative runoff", "balance", "MAPE")
     row.names(rs bucket) <- bucket name
     # calculate runoff for each time bucket
     for_bucket_1 <- bal_bucket_short$Daily["forecast"]
     for_bucket_7 <- bal_bucket_short$`2-7`["forecast"]
     for bucket 30 <- bal bucket short $\ 8-30 \[ "forecast" \]
     for bucket 90 <- bal bucket long$`31-90`["forecast balance"]
     for bucket 180 <- bal bucket long$`91-180`["forecast balance"]
     for bucket 360 <- bal bucket long$`181-360`["forecast balance"]
```

```
Tên file
                                                                                        Vi trí
     rs_bucket$cummulative_runoff[1] <- abs(min((for_bucket_1$forecast[length(for_bucket_1$forecast)] -
runoff_all$bl[nrow(runoff_all)])/runoff_all$bl[nrow(runoff_all)],0))
     rs bucket$cummulative runoff[2] <- abs(min((for bucket 7$forecast[length(for bucket 7$forecast)] -
runoff all$bl[nrow(runoff all)])/runoff all$bl[nrow(runoff all)],0))
     rs bucket$cummulative runoff[3] <- abs(min((for bucket 30$forecast[length(for bucket 30$forecast)] -
runoff_all$bl[nrow(runoff_all)])/runoff_all$bl[nrow(runoff_all)],0))
     rs bucket$cummulative runoff[4] <-
abs(min((for_bucket_90$forecast_balance)|ength(for_bucket_90$forecast_balance)|
runoff_all$bl[nrow(runoff_all)])/runoff_all$bl[nrow(runoff_all)],0))
     rs_bucket$cummulative_runoff[5] <-
abs(min((for_bucket_180$forecast_balance[length(for_bucket_180$forecast_balance)] -
runoff_all$bl[nrow(runoff_all)])/runoff_all$bl[nrow(runoff_all)],0))
     rs bucket$cummulative runoff[6] <-
abs(min((for_bucket_360$forecast_balance[length(for_bucket_360$forecast_balance)] -
runoff_all$bl[nrow(runoff_all)])/runoff_all$bl[nrow(runoff_all)],0))
     rs_bucket$cummulative_runoff[7] <- NA
     a <- rs bucket$cummulative runoff
     b <- rs bucket$cummulative runoff
     for (i in (2:(length(bucket)-1))) {
      if (b[i]>max(na.omit(a[1:i-1]))){
       b[i] <- a[i] - max(na.omit(a[1:(i-1)]))
      } else {
       b[i] = 0
     rs_bucket$uncummulative_runoff <- b
     rs_bucket$balance[1] <- for_bucket_1$forecast[length(for_bucket_1$forecast)]
     rs_bucket$balance[2] <- for_bucket_7$forecast[length(for_bucket_7$forecast)]
     rs_bucket$balance[3] <- for_bucket_30$forecast[length(for_bucket_30$forecast)]
     rs_bucket$balance[4] <- for_bucket 90$forecast_balance[length(for_bucket_90$forecast_balance])
     rs_bucket$balance[5] <- for_bucket_180$forecast_balance[length(for_bucket_180$forecast_balance)]
     rs_bucket$balance[6] <- for_bucket_360$forecast_balance[length(for_bucket_360$forecast_balance)]
     mape bucket 1 <- bal bucket short$Daily[10]
     mape bucket 7 <- bal bucket short $\frac{2-7}{10}
     mape_bucket_30 <- bal_bucket_short$`8-30`[10]
     mape bucket 90 <- bal bucket long$`31-90`[9]
     mape_bucket_180 <- bal_bucket_long$`91-180`[9]
     mape bucket 360 <- bal bucket long$`181-360`[9]
     rs bucket$MAPE[1] <- mape bucket 1$MAPE[1]
     rs bucket$MAPE[2] <- mape bucket 7$MAPE[1]
     rs bucket$MAPE[3] <- mape bucket 30$MAPE[1]
     rs_bucket$MAPE[4] <- mape_bucket_90$MAPE_Test[1]
     rs_bucket$MAPE[5] <- mape_bucket_180$MAPE_Test[1]
     rs_bucket$MAPE[6] <- mape_bucket_360$MAPE_Test[1]
     write.csv(rs_bucket, choose.files(default = "result.csv",
                            caption = "Saving result into csv",
                            multi = F)
    } else if (user_input == "7") {
     bucket <- c(1, 7, 30, 90, 180, 360, 10000000)#gan ngay cho cac time bucket
     bucket_name <- c("Daily", "2-7 days", "8-30 days", "31-90 days", "91-180 days", "181-360 days",">360 days") #gan ten cho cac time bucket
     rs bucket <- data.frame(matrix(nrow = 7, ncol=4))
     names(rs bucket) <- c("cummulative runoff", "uncummulative runoff", "disbursement", "MAPE")
     row.names(rs bucket) <- bucket name
     # calculate runoff for each time bucket
     for bucket 1 <- bal bucket short$Daily["forecast"]
     for_bucket_7 <- bal_bucket_short$`2-7`["forecast"]
     for_bucket_30 <- bal_bucket_short$`8-30`["forecast"]
```

```
Tên file
                                                                                     Vi trí
     for bucket 90 <- bal bucket long$`31-90`["forecast balance"]
     for_bucket_180 <- bal_bucket_long$`91-180`["forecast_balance"]
     for bucket 360 <- bal bucket long$`181-360`["forecast balance"]
     rs bucket$cummulative runoff[1] <- abs(min((for bucket 1$forecast[length(for bucket 1$forecast)] -
runoff all$bl[nrow(runoff all)])/runoff all$bl[nrow(runoff all)],0))
     rs_bucket$cummulative_runoff[2] <- abs(min((for_bucket_7$forecast[length(for_bucket_7$forecast)] -
runoff all$bl[nrow(runoff all)])/runoff all$bl[nrow(runoff all)],0))
     rs_bucket$cummulative_runoff[3] <- abs(min((for_bucket_30$forecast[length(for_bucket_30$forecast)] -
runoff_all$bl[nrow(runoff_all)])/runoff_all$bl[nrow(runoff_all)],0))
     rs_bucket$cummulative_runoff[4] <-
abs(min((for_bucket_90$forecast_balance[length(for_bucket_90$forecast_balance)] -
runoff_all$bl[nrow(runoff_all)])/runoff_all$bl[nrow(runoff_all)],0))
     rs bucket$cummulative runoff[5] <-
abs(min((for_bucket_180$forecast_balance[length(for_bucket_180$forecast_balance)] -
runoff_all$bl[nrow(runoff_all)])/runoff_all$bl[nrow(runoff_all)],0))
     rs_bucket$cummulative_runoff[6] <-
abs(min((for bucket 360$forecast balance)] -
runoff_all$bl[nrow(runoff_all)])/runoff_all$bl[nrow(runoff_all)],0))
     rs bucket$cummulative runoff[7] <- NA
     a <- rs bucket$cummulative runoff
     b <- rs_bucket$cummulative_runoff
     for (i in (2:(length(bucket)-1))) {
      if (b[i]>max(na.omit(a[1:i-1]))){
       b[i] <- a[i] - max(na.omit(a[1:(i-1)]))
      } else {
       b[i] = 0
     rs_bucket$uncummulative_runoff <- b
     rs_bucket$disbursement[1] <- for_bucket_1$forecast[length(for_bucket_1$forecast)]
     rs_bucket$disbursement[2] <- for_bucket_7$forecast[length(for_bucket_7$forecast)]
     rs_bucket$disbursement[3] <- for_bucket_30$forecast[length(for_bucket_30$forecast)]
     rs_bucket$disbursement[4] <- for_bucket_90$forecast_balance[length(for_bucket_90$forecast_balance)]
     rs bucket$disbursement[5] <- for bucket 180$forecast balance[length(for bucket 180$forecast balance)]
     rs bucket$disbursement[6] <- for bucket 360$forecast balance[length(for bucket 360$forecast balance]]
     mape bucket 1 <- bal bucket short$Dailv[10]
     mape_bucket_7 <- bal_bucket_short$`2-7`[10]
     mape_bucket_30 <- bal_bucket_short$`8-30`[10]
     mape bucket 90 <- bal bucket long$`31-90`[9]
     mape bucket 180 <- bal bucket long$`91-180`[9]
     mape bucket 360 <- bal bucket long$`181-360`[9]
     rs_bucket$MAPE[1] <- mape_bucket_1$MAPE[1]
     rs_bucket$MAPE[2] <- mape_bucket_7$MAPE[1]
     rs_bucket$MAPE[3] <- mape_bucket_30$MAPE[1]
     rs_bucket$MAPE[4] <- mape_bucket_90$MAPE_Test[1]
     rs_bucket$MAPE[5] <- mape_bucket_180$MAPE_Test[1]
     rs_bucket$MAPE[6] <- mape_bucket_360$MAPE_Test[1]
     write.csv(rs_bucket, choose.files(default = "result.csv",
                           caption = "Saving result into csv",
                           multi = F)
     bucket <- c(1, 7, 30, 90, 180, 360, 10000000)#gan ngay cho cac time bucket
     bucket_name <- c("Daily", "2-7 days", "8-30 days",
               "31-90 days", "91-180 days", "181-360 days", ">360 days") #gan ten cho cac time bucket
     rs_bucket <- data.frame(matrix(nrow = 7, ncol=4))
     names(rs bucket) <- c("cummulative runoff", "uncummulative runoff", "balance", "MAPE")
     row.names(rs bucket) <- bucket name
     # calculate runoff for each time bucket
```

```
Tên file
                                                                                      Vi trí
     for bucket 1 <- bal bucket short$Dailv["forecast"]
     for_bucket_7 <- bal_bucket_short$`2-7`["forecast"]
     for bucket 30 <- bal bucket short$`8-30`["forecast"]
     for bucket 90 <- bal bucket long$`31-90`["forecast balance"]
     for bucket 180 <- bal bucket long$`91-180`["forecast balance"]
     for bucket 360 <- bal bucket long$`181-360`["forecast_balance"]
     rs bucket$cummulative runoff[1] <- abs(min((for bucket 1$forecast[]ength(for bucket 1$forecast)] -
runoff$bl[nrow(runoff)])/runoff$bl[nrow(runoff)],0))
     rs_bucket$cummulative_runoff[2] <- abs(min((for_bucket_7$forecast[length(for_bucket_7$forecast)] -
runoff$bl[nrow(runoff)])/runoff$bl[nrow(runoff)],0))
     rs_bucket$cummulative_runoff[3] <- abs(min((for_bucket_30$forecast[length(for_bucket_30$forecast)] -
runoff$bl[nrow(runoff)])/runoff$bl[nrow(runoff)],0))
     rs bucket$cummulative runoff[4] <-
abs(min((for_bucket_90$forecast_balance|length(for_bucket_90$forecast_balance)] -
runoff$bl[nrow(runoff)])/runoff$bl[nrow(runoff)],0))
     rs_bucket$cummulative_runoff[5] <-
abs(min((for_bucket_180$forecast_balance[length(for_bucket_180$forecast_balance)] -
runoff$bl[nrow(runoff)])/runoff$bl[nrow(runoff)],0))
     rs bucket$cummulative runoff[6] <-
abs(min((for bucket 360$forecast balance]]ength(for bucket 360$forecast balance)] -
runoff$bl[nrow(runoff)])/runoff$bl[nrow(runoff)],0))
     rs_bucket$cummulative_runoff[7] <- NA
     a <- rs bucket$cummulative runoff
     b <- rs bucket$cummulative runoff
     for (i in (2:(length(bucket)-1))) {
      if (b[i]>max(na.omit(a[1:i-1]))){
       b[i] <- a[i] - max(na.omit(a[1:(i-1)]))
      } else {
       b[i] = 0
     rs_bucket$uncummulative_runoff <- b
     rs_bucket$balance[1] <- for_bucket_1$forecast[length(for_bucket_1$forecast)]
     rs_bucket$balance[2] <- for_bucket_7$forecast[length(for_bucket_7$forecast)]
     rs bucket$balance[3] <- for bucket 30$forecast[length(for bucket 30$forecast)]
     rs_bucket$balance[4] <- for_bucket_90$forecast_balance[length(for_bucket_90$forecast_balance)]
     rs bucket$balance[5] <- for bucket 180$forecast balance[length(for bucket 180$forecast balance)]
     rs bucket$balance[6] <- for bucket 360$forecast balance[length(for bucket 360$forecast balance)]
     mape bucket 1 <- bal bucket short$Daily[10]
     mape bucket 7 <- bal bucket short$\^2-7\^[10]
     mape bucket 30 <- bal bucket short$`8-30`[10]
     mape bucket 90 <- bal bucket long$`31-90`[9]
     mape_bucket_180 <- bal_bucket_long$`91-180`[9]
     mape_bucket_360 <- bal_bucket_long$`181-360`[9]
     rs_bucket$MAPE[1] <- mape_bucket_1$MAPE[1]
     rs_bucket$MAPE[2] <- mape_bucket_7$MAPE[1]
     rs_bucket$MAPE[3] <- mape_bucket_30$MAPE[1]
     rs_bucket$MAPE[4] <- mape_bucket_90$MAPE_Test[1]
     rs_bucket$MAPE[5] <- mape_bucket_180$MAPE_Test[1]
     rs_bucket$MAPE[6] <- mape_bucket_360$MAPE_Test[1]
     write.csv(rs_bucket, choose.files(default = "result.csv",
                           caption = "Saving result into csv",
                           multi = F)
   odbcClose(dbhandle)
   dlg message(c("Model end"))
```

## **Đầu ra**

| Tên file | Vị<br>trí      |  |
|----------|----------------|--|
| result   | OD_arima_final |  |

## **4.Lịch sử tài liệu**

| Ngày | Phiên bản | Mô tả            | Chỉnh sửa bởi | Phê duyệt bởi |
|------|-----------|------------------|---------------|---------------|
|      |           | Bản thảo lần đầu |               |               |