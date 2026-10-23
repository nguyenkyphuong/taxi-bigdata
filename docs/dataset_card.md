# Dataset Card — NYC Taxi Trip Records

## 1. Mục đích sử dụng dữ liệu

Đồ án sử dụng dữ liệu chuyến đi taxi tại New York City (NYC) để thực hiện hai nhóm thí nghiệm:

1. **Benchmark hệ thống Big Data:** triển khai các tác vụ thống kê dữ liệu bằng Hadoop–MapReduce và Apache Spark trên cùng đầu vào, cùng định nghĩa đầu ra.
2. **Tái hiện và cải tiến thuật toán theo paper:** sử dụng dữ liệu Yellow Taxi, Green Taxi và Uber lịch sử để xây dựng bài toán phân loại khu vực theo dịch vụ có số lượt đón khách chiếm ưu thế.

Hai nhóm thí nghiệm có yêu cầu dữ liệu khác nhau, vì vậy cần quản lý và đánh giá riêng.

## 2. Nguồn dữ liệu

### 2.1. Nguồn chính thức TLC

- **Tên nguồn:** NYC Taxi and Limousine Commission (TLC) — Trip Record Data.
- **URL:** https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- **Đơn vị cung cấp:** New York City Taxi and Limousine Commission.
- **Các nhóm dữ liệu:** Yellow Taxi, Green Taxi, For-Hire Vehicle (FHV) và High Volume For-Hire Vehicle (HVFHV).
- **Tần suất công bố:** dữ liệu chuyến đi được công bố theo tháng.
- **Định dạng:** dữ liệu các năm gần đây được cung cấp chủ yếu dưới dạng Parquet; định dạng của dữ liệu lịch sử cần kiểm tra theo từng năm và file cụ thể.

TLC cho biết dữ liệu chuyến đi được thu thập từ các nhà cung cấp công nghệ hoặc đơn vị gửi báo cáo được cấp phép. TLC không bảo đảm tính chính xác tuyệt đối của toàn bộ dữ liệu.

### 2.2. Nguồn Uber lịch sử phục vụ tái hiện paper

- **Tên nguồn:** FiveThirtyEight — Uber TLC FOIL Response.
- **URL:** https://github.com/fivethirtyeight/uber-tlc-foil-response
- **Phạm vi liên quan:** dữ liệu hơn 4,5 triệu lượt đón Uber tại NYC trong giai đoạn tháng 4–9/2014.
- **Định dạng:** CSV.
- **Các trường chính:** `Date/Time`, `Lat`, `Lon`, `Base`.

Nguồn này được FiveThirtyEight công bố từ dữ liệu thu thập qua yêu cầu cung cấp thông tin đối với TLC. Đây là nguồn dữ liệu lịch sử bổ sung, không phải bộ file Uber hiện hành trên trang TLC.

## 3. Phạm vi dữ liệu dự kiến

| Mục đích | Dataset dự kiến | Phạm vi thời gian | Trạng thái |
|---|---|---|---|
| Benchmark MapReduce–Spark | Yellow Taxi Trip Records | Một tháng dữ liệu được chọn sau khi kiểm tra khả năng xử lý | Chưa tải/đo thực tế |
| Tái hiện bài toán phân loại | Yellow Taxi + Green Taxi + Uber | Tháng 4–9/2014 | Cần kiểm tra file và schema |
| Phát hiện bất thường mở rộng | Có thể sử dụng dữ liệu chuyến taxi đã chọn | Chốt sau | Chưa triển khai |

Việc sử dụng dữ liệu năm 2014 cho bài toán phân loại nhằm bám sát paper. Dataset benchmark hệ thống được lựa chọn theo yêu cầu thống kê chuyến đi, khả năng tương thích và giới hạn tài nguyên của môi trường thử nghiệm.

## 4. Schema và các trường dữ liệu quan trọng

### 4.1. Yellow Taxi

Các trường cần khảo sát trong dữ liệu Yellow Taxi bao gồm:

| Trường | Ý nghĩa | Ứng dụng |
|---|---|---|
| `tpep_pickup_datetime` | Thời điểm đón khách | Thống kê theo ngày/giờ |
| `tpep_dropoff_datetime` | Thời điểm trả khách | Tính thời lượng chuyến |
| `PULocationID` | Mã khu vực đón | Thống kê theo khu vực |
| `DOLocationID` | Mã khu vực trả | Thống kê theo khu vực |
| `trip_distance` | Quãng đường chuyến đi | Thống kê quãng đường |
| `fare_amount` | Tiền cước cơ bản | Phân tích doanh thu |
| `tip_amount` | Tiền tip | Phân tích tiền tip |
| `total_amount` | Tổng tiền được ghi nhận | Phân tích tổng tiền |
| `passenger_count` | Số hành khách được báo cáo | Phân tích đặc trưng chuyến đi |

**Lưu ý:** tên trường và kiểu dữ liệu phải được xác nhận trên file thực tế trước khi viết chương trình xử lý. Schema có thể khác nhau giữa các năm.

### 4.2. Green Taxi

Các trường dự kiến khảo sát gồm thời điểm đón/trả, mã khu vực đón/trả, quãng đường và các trường tiền cước. Tên trường cụ thể cần đối chiếu với Green Trips Data Dictionary và file được tải.

### 4.3. Uber lịch sử năm 2014

| Trường | Ý nghĩa | Ứng dụng |
|---|---|---|
| `Date/Time` | Thời gian đón khách | Phân tích theo thời gian |
| `Lat` | Vĩ độ điểm đón | Xác định vùng theo paper |
| `Lon` | Kinh độ điểm đón | Xác định vùng theo paper |
| `Base` | Mã đơn vị/base liên quan | Thông tin mô tả bổ sung |

Bộ dữ liệu Uber nêu trên là dữ liệu lượt đón, không có đầy đủ các trường quãng đường và tiền cước như dữ liệu chuyến Yellow Taxi. Vì vậy, không được mặc định rằng các trường này tồn tại trong cả ba dataset.

## 5. Dữ liệu không gian

TLC cung cấp Taxi Zone Lookup Table và dữ liệu bản đồ khu vực taxi tại trang Trip Record Data.

- Với dữ liệu Yellow/Green Taxi có `PULocationID` và `DOLocationID`, sử dụng bảng lookup để tra cứu tên khu vực.
- Với dữ liệu Uber 2014 có tọa độ, có thể làm tròn vĩ độ và kinh độ đến ba chữ số thập phân để xây dựng vùng theo cách mô tả trong paper.

Mã khu vực taxi (`LocationID`) và tọa độ GPS không phải cùng một loại dữ liệu, không được sử dụng thay thế cho nhau mà không có bước chuyển đổi phù hợp.

## 6. Điều khoản sử dụng và hạn chế

Dữ liệu chuyến đi được công bố để người dùng truy cập và phân tích. Tuy nhiên, trang dữ liệu TLC được khảo sát không đủ để kết luận rằng tất cả file đều được phát hành theo cùng một giấy phép mở tiêu chuẩn.

Trước khi phân phối lại dữ liệu hoặc đưa dữ liệu vào sản phẩm công khai, cần kiểm tra điều khoản hiện hành của nguồn tương ứng. Trong đồ án, cần ghi nguồn, đường dẫn tải và ngày truy cập.

Các hạn chế đã biết:

- TLC không bảo đảm tính chính xác tuyệt đối của dữ liệu do các đơn vị gửi báo cáo.
- Schema có thể thay đổi theo thời gian và giữa các nhóm dữ liệu.
- Một số trường có thể thiếu hoặc chứa giá trị không hợp lệ.
- Dữ liệu Uber lịch sử và dữ liệu TLC hiện hành có cấu trúc khác nhau.
- Kết quả phân tích phản ánh dữ liệu được công bố, không tự động đại diện cho toàn bộ nhu cầu di chuyển thực tế của NYC.

## 7. Quy mô dữ liệu và chất lượng

Các thông tin dưới đây phải được bổ sung sau khi tải và kiểm tra file thực tế.

| Chỉ tiêu | Kết quả |
|---|---|
| Dataset/file được chọn | Chưa chốt |
| Khoảng thời gian thực tế | Chưa xác minh |
| Dung lượng file tải xuống | Chưa đo |
| Số bản ghi | Chưa đo |
| Số cột và kiểu dữ liệu | Chưa kiểm tra |
| Tỷ lệ thiếu theo trường | Chưa đo |
| Số bản ghi trùng | Chưa đo |
| Khoảng thời gian sớm nhất/muộn nhất | Chưa đo |
| Giá trị không hợp lệ | Chưa đo |

Không điền số liệu giả định vào các trường này. Kết quả chỉ được ghi sau khi chạy bước profiling trên dữ liệu đã tải.

## 8. Kế hoạch tiếp nhận và lưu trữ

1. Chọn file phù hợp với mục tiêu thí nghiệm.
2. Tải file vào thư mục `data/raw/`, không sửa đổi dữ liệu gốc.
3. Ghi lại nguồn, tên file, khoảng thời gian và dung lượng.
4. Kiểm tra schema, kiểu dữ liệu, giá trị thiếu, bản ghi trùng và khoảng thời gian.
5. Ghi kết quả khảo sát vào `reports/data_profile.md`.
6. Chỉ sau khi xác nhận dữ liệu và khả năng xử lý mới chuyển dữ liệu cần thiết lên HDFS.
7. Không commit file dữ liệu dung lượng lớn lên GitHub; chỉ quản lý mã nguồn, tài liệu, cấu hình và kết quả được phép công bố.

## 9. Tài liệu tham khảo

1. NYC Taxi and Limousine Commission, “TLC Trip Record Data.” https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
2. FiveThirtyEight, “Uber TLC FOIL Response.” https://github.com/fivethirtyeight/uber-tlc-foil-response
3. Sun et al. (2018), “Big Data Trip Classification on the New York City Taxi and Uber Sensor Network.” https://doi.org/10.3966/160792642018031902027
