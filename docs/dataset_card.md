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

## 3. Phạm vi dữ liệu

Đồ án tách dữ liệu thành hai nhóm theo mục tiêu thí nghiệm.

| Mục đích | Dataset | Phạm vi thời gian | Trạng thái |
|---|---|---|---|
| Benchmark Hadoop–MapReduce và Spark | Yellow Taxi Trip Records | Tháng 01/2024 | Đã tải; đã kiểm tra metadata |
| Tái hiện bài toán phân loại theo paper | Yellow Taxi + Green Taxi + Uber lịch sử | Tháng 4–9/2014 | Chưa xác minh đầy đủ file và schema |
| Phát hiện bất thường mở rộng | Dữ liệu chuyến taxi được chọn | Chốt sau | Chưa triển khai |

### 3.1. Dataset benchmark hệ thống

Tệp được chọn ban đầu là `yellow_tripdata_2024-01.parquet`, tải từ nguồn TLC chính thức. Kiểm tra metadata bằng PyArrow ghi nhận dung lượng 47,65 MB, 2.964.624 bản ghi, 19 cột và 3 row groups.

Dataset này được dùng để xây dựng các tác vụ tổng hợp dữ liệu có đầu ra tương đương giữa Hadoop–MapReduce và Spark. Trước khi benchmark chính thức, cần hoàn thành kiểm tra chất lượng dữ liệu và xác định rõ các phép tính, đầu ra và cách đo thời gian.

### 3.2. Dataset tái hiện bài báo

Phương án dự kiến sử dụng dữ liệu Yellow Taxi, Green Taxi và Uber trong giai đoạn tháng 4–9/2014, nhằm bám sát bài toán phân loại khu vực theo dịch vụ có số lượt đón khách chiếm ưu thế trong paper tham khảo.

Tính khả thi của phương án này chưa được xác nhận. Cần kiểm tra các file lịch sử thực tế, schema và khả năng xác định khu vực tương thích giữa ba nguồn dữ liệu trước khi chốt thiết kế thí nghiệm.

### 3.3. Phạm vi mở rộng

Phát hiện bất thường là phần mở rộng dự kiến. Dataset, tiêu chí xác định bất thường và phương pháp đánh giá sẽ được chốt ở giai đoạn thiết kế thí nghiệm riêng.

## 4. Schema và các trường dữ liệu quan trọng

### 4.1. Yellow Taxi

### Kết quả kiểm tra ban đầu — Yellow Taxi, tháng 01/2024

| Thuộc tính | Kết quả |
|---|---|
| Tệp | `yellow_tripdata_2024-01.parquet` |
| Dung lượng trên đĩa | 47,65 MB |
| Số bản ghi theo Parquet metadata | 2.964.624 |
| Số cột | 19 |
| Số row groups | 3 |
| Định dạng | Apache Parquet |
| Công cụ kiểm tra | Python, PyArrow 26.0.0 |
| Môi trường | Windows, Python virtual environment (`.venv`) |

Các trường quan trọng đã xác nhận gồm thời gian đón/trả, mã khu vực đón/trả, quãng đường, số hành khách và các trường giá cước.

**Giới hạn:** Đây mới là kết quả kiểm tra metadata. Tỷ lệ giá trị thiếu, bản ghi trùng lặp, giá trị không hợp lệ và phân bố dữ liệu chưa được đo. Chưa xem các bản ghi là hợp lệ chỉ dựa trên metadata.
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

## 7. Quy mô dữ liệu đã xác minh

| Chỉ tiêu | Yellow Taxi tháng 01/2024 |
|---|---|
| Tên file | `yellow_tripdata_2024-01.parquet` |
| Dung lượng trên đĩa | 47,65 MB |
| Số bản ghi theo Parquet metadata | 2.964.624 |
| Số cột | 19 |
| Số row groups | 3 |
| Công cụ kiểm tra | Python, PyArrow 26.0.0 |

Các số liệu trên được lấy từ kết quả kiểm tra metadata của file đã tải. Đây chưa phải kết quả profiling chất lượng dữ liệu.

Tỷ lệ giá trị thiếu, bản ghi trùng, timestamp lỗi và giá trị bất hợp lý sẽ được đo trong Task 3, với sản phẩm `notebooks/01_data_profiling.ipynb` và `reports/data_profile.md`.

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
