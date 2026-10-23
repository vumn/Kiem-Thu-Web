## 1. So sánh WebDriver, Selenium IDE và Selenium Grid

| Tiêu chí | WebDriver | Selenium IDE | Selenium Grid |
| :--- | :--- | :--- | :--- |
| **Mục đích** | Điều khiển trình duyệt và chạy các bài kiểm thử tự động bằng code | Phát triển các test case Selenium nhanh dạng record & playback | Chạy test case trên nhiều máy và nền tảng khác nhau cùng lúc |
| **Cách hoạt động** | Sử dụng API tự động hóa do nhà cung cấp trình duyệt cung cấp để điều khiển trình duyệt như người dùng thật | Ghi lại thao tác người dùng trên trình duyệt bằng các lệnh Selenium có sẵn | Kích hoạt test ở máy cục bộ, sau đó test được thực thi tự động ở máy từ xa |
| **Cách tạo test** | Sử dụng WebDriver API (Python/Java) để xây dựng test script | Ghi/phát lại thao tác trên trình duyệt, chỉnh sửa các tham số định vị phần tử | Sử dụng để chạy các bài test WebDriver đã phát triển |

---

## 2. Đường đi của một lệnh: Từ Code, qua Driver, tới Trình duyệt ##

```text
+------------------+         1. Gọi API         +---------------------------+
|  Code (Pytest)   | -------------------------> |  Thư viện (WebDriver API) |
+------------------+                            +---------------------------+
         ^                                                    |
         |                                                    | 2. Gửi lệnh HTTP/JSON
         | 5. Trả về kết quả                                  v
+------------------+        4. Điều khiển       +---------------------------+
|Trình duyệt Chrome| <------------------------- | ChromeDriver (Driver)     |
+------------------+                            +---------------------------+
