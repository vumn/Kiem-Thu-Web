### Kiểm thử tự động với Selenium

1. Khái niệm:

- Là xử lý một cách tự động các bước thực hiện các testcase, kiểm thử tự động bằng một công cụ nhằm rút ngắn thời gian kiểm thử.
- Là sử dụng phần mềm và tự viết mã lệnh để kiểm thử phần mềm.

2. Mục đích:

- Giảm công sức và thời gian thực hiện kiểm thử.
- Tăng độ tin cậy và giảm sai sót từ con người.
- Giảm tỏng chi phí cho quá trình kiểm thử.

3.  Các thành phần của Selenium

                            Selenium Suite
                                    |
                                    |
                -------------------------------------------------
                |               |               |               |
            Selenium         Selenium         WebDriver     Selenium Grid
              IDE               RC              /
                                \              /
                                 \            /
                                    Selenium 2

- Selenium IDE: Công cụ tích hợp trên trình duyệt.
- Selenium RC: Hỗ trợ thực hiện kiểm tra phức tạp với các câu lệnh.
- Selenium Grid: Hỗ trợ thực hiện kiểm thử trên các trình duyệt song song với 1 kịch bản.
- Selenium WebDriver: Bộ thư viện API giúp xây dựng kịch bản kiểm thử.

4. Nhược điểm

- Chỉ hỗ trợ cho web.
- Người dùng cần có kiến thức về lập trình.
- Không thể kiểm thử API hoặc backend trực tiếp.
- Tốn tài nguyên hơn so với các phương pháp kiểm thử trực tiếp khi số lượng case quá lớn.

5. Đường đi của 1 lệnh:

---

| WebDriver.get | -----> | Driver | -----> | |
|("https://the-internet.herokuapp.com/login") | | (Chrome, FireFox,...)| | Browser |
| | <----- | | <----- | |

---
