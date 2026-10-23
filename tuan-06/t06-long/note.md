## 1. Selenium và các thành phần chính

Selenium là bộ công cụ mã nguồn mở dùng để tự động hóa trình duyệt web, thường được sử dụng để kiểm thử chức năng giao diện web.

Ba thành phần chính cần phân biệt:

| Thành phần | Vai trò | Ví dụ sử dụng |
|---|---|---|
| **Selenium WebDriver** | Điều khiển trình duyệt thông qua code | Viết Python để mở Chrome, đăng nhập, nhấn nút và kiểm tra kết quả |
| **Selenium IDE** | Ghi lại và phát lại các thao tác trên trình duyệt | Ghi lại thao tác đăng nhập để chạy lại |
| **Selenium Grid** | Chạy test trên nhiều máy, trình duyệt hoặc môi trường khác nhau | Chạy bộ test trên Chrome và Firefox song song |

Điểm quan trọng: WebDriver tập trung vào việc **viết và thực thi kịch bản tự động hóa**, IDE hỗ trợ ghi lại thao tác, còn Grid giúp phân phối việc chạy test trên nhiều môi trường.

## 2. WebDriver khác Selenium IDE và Selenium Grid ở đâu?

- **WebDriver:** Viết chương trình để nhập username, password, nhấn Login rồi xác nhận đăng nhập thành công.
- **Selenium IDE:** Ghi lại thao tác đăng nhập bằng giao diện và phát lại các bước đó.
- **Selenium Grid:** Phân phối kịch bản đăng nhập để chạy trên nhiều trình duyệt hoặc máy khác nhau.

WebDriver và Grid không hoàn toàn là hai lựa chọn thay thế nhau. Có thể viết test bằng WebDriver rồi dùng Grid để chạy các test đó trên nhiều môi trường.

## 3. Đường đi của một lệnh Selenium

WebDriver giao tiếp với trình duyệt thông qua một driver tương ứng, chẳng hạn ChromeDriver cho Chrome hoặc GeckoDriver cho Firefox. Việc giao tiếp diễn ra theo hai chiều: gửi lệnh và nhận kết quả.

```text
Test Script (Python / Java / C#)
              |
              v
      Selenium WebDriver
              |
              v
       Browser Driver
        (ChromeDriver)
              |
              v
         Web Browser
           (Chrome)

Phản hồi đi ngược lại:
Browser -> Driver -> WebDriver -> Test Script
```

### Ví dụ với Python

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")

print(driver.title)

driver.quit()
```

Luồng hoạt động:

1. Code tạo một phiên làm việc với Chrome.
2. `driver.get()` yêu cầu trình duyệt mở website.
3. WebDriver gửi lệnh qua ChromeDriver.
4. ChromeDriver điều khiển Chrome mở trang web.
5. Khi gọi `driver.title`, tiêu đề trang được trả về cho code.
6. `driver.quit()` kết thúc phiên làm việc.

**Lưu ý:** Trong Selenium hiện đại, Selenium Manager có thể tự quản lý việc tìm kiếm hoặc thiết lập driver phù hợp, không nhất thiết phải tự tải ChromeDriver và cấu hình thủ công trong mọi trường hợp.

Nếu dùng Selenium Grid, đường đi sẽ thêm lớp phân phối lệnh đến máy chạy trình duyệt từ xa. Grid không thay thế WebDriver mà hỗ trợ thực thi các kịch bản WebDriver trên những môi trường khác nhau.

## 4. Tháp kiểm thử và kiểm thử giao diện (UI Testing)

Tháp kiểm thử là cách tổ chức các loại kiểm thử theo mức độ, nhằm giúp đội ngũ cân bằng giữa tốc độ, chi phí và độ tin cậy của bộ test.

```text
             / UI / E2E Tests \
            /   Ít hơn         \
           /--------------------\
          /  Integration Tests   \
         /     Số lượng vừa       \
        /--------------------------\
       /        Unit Tests          \
      /          Nhiều nhất          \
     /________________________________\
```

Đây là mô hình minh họa phổ biến, không phải tỷ lệ bắt buộc cho mọi dự án.

- **Unit test:** Kiểm tra một hàm hoặc thành phần nhỏ. Ví dụ: kiểm tra hàm tính tổng tiền đơn hàng.
- **Integration test:** Kiểm tra nhiều thành phần hoạt động cùng nhau. Ví dụ: dịch vụ đặt hàng kết nối với cơ sở dữ liệu.
- **UI/E2E test:** Kiểm tra luồng hoạt động từ góc nhìn người dùng. Ví dụ: mở website, đăng nhập, thêm sản phẩm vào giỏ và đặt hàng.

### Vì sao kiểm thử qua giao diện nên ít và có chọn lọc?

1. **Chạy chậm hơn:** Test phải mở trình duyệt, tải trang, chờ các thành phần xuất hiện và thực hiện thao tác.
2. **Dễ bị ảnh hưởng bởi thay đổi giao diện:** Chẳng hạn, đổi thuộc tính hoặc cấu trúc HTML có thể khiến bộ chọn phần tử không còn hoạt động, dù chức năng nghiệp vụ vẫn đúng.
3. **Khó xác định nguyên nhân lỗi:** Một bài test đăng nhập thất bại có thể do giao diện, mạng, máy chủ hoặc dữ liệu kiểm thử.
4. **Chi phí bảo trì cao:** Khi giao diện thay đổi thường xuyên, nhiều kịch bản có thể cần sửa theo.

Vì vậy, nên kiểm tra logic ở cấp unit hoặc integration khi phù hợp, sau đó dùng Selenium cho những luồng quan trọng cần xác nhận hoạt động thực tế qua trình duyệt.

### Ví dụ: chức năng đăng nhập

- **Unit test:** Kiểm tra logic xác thực thông tin.
- **Integration test:** Kiểm tra dịch vụ đăng nhập và cơ sở dữ liệu.
- **Selenium UI test:** Kiểm tra người dùng nhập thông tin, nhấn nút Login và nhìn thấy trang chủ hoặc thông báo lỗi phù hợp.

Không cần viết hàng chục UI test chỉ để kiểm tra mọi trường hợp sai mật khẩu nếu các trường hợp đó có thể được xác minh đáng tin cậy ở tầng thấp hơn.

