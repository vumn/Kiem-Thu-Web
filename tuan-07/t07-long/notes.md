# Ghi chú tuần 07

## 1. Nhận xét thí nghiệm (Trang /dynamic_loading/1 và /dynamic_loading/2)

### Đối với trang Example 1
* **Khi không dùng lệnh chờ:** Bài test vẫn chạy qua bước tìm kiếm (không lỗi `NoSuchElementException`) vì phần tử `#finish h4` thực chất đã nằm sẵn trong mã nguồn HTML (DOM) ngay từ đầu. Tuy nhiên, do phần tử đang bị ẩn (`display:none`), hàm `.text` trả về một chuỗi rỗng `""`. Nếu thực hiện so sánh `assert result.text == "Hello World!"`, bài test sẽ bị **FAILED** vì dữ liệu chưa kịp hiển thị.
* **Khi dùng lệnh chờ tường minh (Explicit Wait):** Bài test chạy **PASSED** ổn định. Lệnh `WebDriverWait` đã giữ trình duyệt đứng đợi cho đến khi thanh hiệu ứng loading biến mất hẳn và chữ `"Hello World!"` hiện rõ lên màn hình rồi mới lấy dữ liệu.

### Đối với trang Example 2
* **Khi không dùng lệnh chờ:** Bài test bị sập ngay lập tức và báo lỗi **`NoSuchElementException` (FAILED)**. Lý do là vì ở trang này, phần tử `#finish h4` hoàn toàn chưa tồn tại trong mã nguồn HTML khi mới tải trang. Khi bấm nút Start, mã JavaScript mới bắt đầu tạo ra phần tử này. Việc Selenium tìm kiếm ngay lập tức khi nó chưa được sinh ra dẫn đến lỗi không tìm thấy phần tử.
* **Khi dùng lệnh chờ tường minh:** Bài test chạy **PASSED** thành công. Trình điều khiển kiên nhẫn đợi JavaScript dựng xong cấu trúc HTML của phần tử và hiển thị nó lên, giúp quá trình kiểm thử diễn ra đồng bộ với tốc độ phản hồi của trang web.

---

## 2. Trả lời các câu hỏi

### Câu 1:
`time.sleep()` thuộc thư viện mặc định của Python và là một cơ chế **Hard Wait**. Chúng ta nên tránh sử dụng nó trong kiểm thử tự động vì các lý do sau:
* **Lãng phí thời gian:** Nếu ta đặt `time.sleep(10)` nhưng trang web chỉ cần 2 giây đã tải xong, script test vẫn bị ép buộc phải đứng im và đóng băng thêm 8 giây vô ích. Khi số lượng bài test tăng lên hàng trăm bài, việc này sẽ làm chậm tiến độ chạy kiểm thử một cách nghiêm trọng.
* **Không linh hoạt:** Nếu gặp ngày mạng chậm hoặc server phản hồi lâu hơn 10 giây, bài test sẽ lập tức bị lỗi dù bản chất tính năng không hề sai.
* **Ngược lại với Explicit Wait:** Các lệnh chờ của Selenium như `WebDriverWait` hoạt động thông minh theo cơ chế "chờ động" — cứ mỗi 500ms nó sẽ kiểm tra lại một lần, nếu điều kiện thỏa mãn sớm thì nó sẽ đi tiếp luôn chứ không chờ hết thời gian tối đa.

### Câu 2:
Trong danh sách điều kiện chờ (`expected_conditions`), đây là hai trạng thái hoàn toàn khác nhau về mức độ tương tác:
* **`visibility_of_element_located`:** 
  * Định nghĩa: Phần tử không chỉ xuất hiện trong mã nguồn DOM mà còn phải hiển thị trên giao diện người dùng
  * Ứng dụng: Phù hợp nhất khi cần đọc thông tin văn bản.
* **`element_to_be_clickable`:**
  * Định nghĩa: Phần tử đó bắt buộc phải hiển thị trên màn hình, **ĐỒNG THỜI** phải ở trạng thái sẵn sàng nhận tương tác, không bị thuộc tính `disabled`, không bị ẩn sau một màn che loading, không bị các phần tử khác đè lên chặn click.
  * Ứng dụng: Phù hợp nhất khi chuẩn bị thực hiện hành vi Click vào các Button, Link, hoặc Checkbox/Radio.

### Câu 3:
Hộp thoại Alert là các cửa sổ pop-up mặc định của hệ thống trình duyệt, Selenium không thể dùng các câu lệnh tìm phần tử CSS Selector hay XPath thông thường để tương tác trực tiếp. Để bấm nút **OK** trên hộp thoại này, ta cần chuyển ngữ cảnh điều khiển sang Alert và gọi lệnh chấp nhận:

```python
# 1. Chờ cho hộp thoại Alert xuất hiện
from selenium.webdriver.support import expected_conditions as EC
WebDriverWait(driver, 10).until(EC.alert_is_present())

# 2. Chuyển hướng sang điều khiển hộp thoại Alert
alert = driver.switch_to.alert

# 3. Bấm nút Accept trên hộp thoại
alert.accept()

# (Nếu muốn bấm nút Cancel thì dùng alert.dismiss(), muốn nhập text thì dùng alert.send_keys("text"))
```
