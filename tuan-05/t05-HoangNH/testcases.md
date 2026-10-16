### TC01: Đăng nhập thất bại - Sai Username, đúng Password

- **Mục tiêu:** Xác minh hệ thống hiển thị thông báo lỗi khi người dùng nhập sai tên đăng nhập.
- **Tiền điều kiện (Preconditions):** Trình duyệt mở trang `https://the-internet.herokuapp.com/login`.
- **Các bước thực hiện (Steps):**
  1. Định vị các phần tử trên trang:
     - Ô username: `By.ID, "username"` _(hoặc `By.NAME, "username"`)_
     - Ô password: `By.ID, "password"`
     - Nút đăng nhập: `By.CSS_SELECTOR, "button[type='submit']"` _(hoặc `By.CLASS_NAME, "radius"`)_
  2. Dùng phương thức `send_keys()` nhập:
     - Username không hợp lệ (ví dụ: `invalid_user`)
     - Password hợp lệ (`SuperSecretPassword!`)
  3. Dùng phương thức `click()` bấm nút Login.
- **Kiểm tra kết quả mong đợi (Assertion):**
  - Thông báo lỗi hiển thị (`div#flash`).
  - Kiểm tra `flash.is_displayed()` là `True`.
  - Nội dung thông báo chứa đoạn text: `"Your username is invalid!"` (dùng cú pháp: `"Your username is invalid!" in flash.text` để tránh lỗi do ký tự `\n` và `×`).

---

### TC02: Đăng nhập thất bại - Đúng Username, sai Password

- **Mục tiêu:** Xác minh hệ thống hiển thị thông báo lỗi khi người dùng nhập sai mật khẩu.
- **Tiền điều kiện (Preconditions):** Trình duyệt mở trang `https://the-internet.herokuapp.com/login`.
- **Các bước thực hiện (Steps):**
  1. Định vị các phần tử: username, password và nút Login.
  2. Dùng phương thức `send_keys()` nhập:
     - Username hợp lệ (`tomsmith`)
     - Password không hợp lệ (ví dụ: `wrong_password`)
  3. Bấm nút Login (`click()`).
- **Kiểm tra kết quả mong đợi (Assertion):**
  - Thông báo lỗi hiển thị (`div#flash`).
  - Kiểm tra `flash.is_displayed()` là `True`.
  - Nội dung thông báo chứa đoạn text: `"Your password is invalid!"`.

---

### TC03: Đăng nhập thành công - Đúng cả Username và Password

- **Mục tiêu:** Xác minh người dùng đăng nhập thành công vào trang quản trị khi nhập đúng tài khoản và mật khẩu.
- **Tiền điều kiện (Preconditions):** Trình duyệt mở trang `https://the-internet.herokuapp.com/login`.
- **Các bước thực hiện (Steps):**
  1. Định vị các phần tử: username, password và nút Login.
  2. Dùng phương thức `send_keys()` nhập thông tin tài khoản hợp lệ:
     - Username: `tomsmith`
     - Password: `SuperSecretPassword!`
  3. Bấm nút Login (`click()`).
  4. Sử dụng `WebDriverWait` (Explicit Wait) để đợi điều hướng hoàn tất.
- **Kiểm tra kết quả mong đợi (Assertion):**
  - URL hiện tại của trang chuyển thành: `https://the-internet.herokuapp.com/secure` (dùng `EC.url_to_be(...)`).
  - Thông báo thành công (`div#flash`) hiển thị và chứa đoạn text: `"You logged into a secure area!"`.
  - Nút **Logout** hiển thị trên trang (`By.CSS_SELECTOR, "a.button.secondary.radius"`).
