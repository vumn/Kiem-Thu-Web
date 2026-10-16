# Kịch bản kiểm thử - Chức năng Đăng nhập (Tuần 5)

## Test Case 1: Đăng nhập thành công với tài khoản hợp lệ
* **Mô tả:** Kiểm tra hệ thống khi người dùng nhập đúng cả tên đăng nhập và mật khẩu.
* **Các bước thực hiện:**
  1. Truy cập vào trang đăng nhập `/login`.
  2. Nhập tên đăng nhập: `tomsmith`.
  3. Nhập mật khẩu: `SuperSecretPassword!`.
  4. Nhấn nút Đăng nhập.
* **Dữ liệu kiểm thử:** 
  * Username: `tomsmith`
  * Password: `SuperSecretPassword!`
* **Kết quả mong đợi:** 
  * Hệ thống chuyển hướng thành công hoặc hiển thị thông báo: `"You logged into a secure area!"`.

---

## Test Case 2: Đăng nhập thất bại do sai mật khẩu
* **Mô tả:** Kiểm tra hệ thống khi người dùng nhập đúng tên đăng nhập nhưng sai mật khẩu.
* **Các bước thực hiện:**
  1. Truy cập vào trang đăng nhập `/login`.
  2. Nhập tên đăng nhập: `tomsmith`.
  3. Nhập một mật khẩu sai (ví dụ: `WrongPassword123`).
  4. Nhấn nút Đăng nhập.
* **Dữ liệu kiểm thử:**
  * Username: `tomsmith`
  * Password: `WrongPassword123`
* **Kết quả mong đợi:**
  * Hệ thống từ chối đăng nhập và hiển thị thông báo lỗi: `"Your password is invalid!"`.

---

## Test Case 3: Đăng nhập thất bại do sai tên đăng nhập
* **Mô tả:** Kiểm tra hệ thống khi người dùng nhập sai tên đăng nhập.
* **Các bước thực hiện:**
  1. Truy cập vào trang đăng nhập `/login`.
  2. Nhập một tên đăng nhập sai (ví dụ: `wronguser`).
  3. Nhập một mật khẩu bất kỳ.
  4. Nhấn nút Đăng nhập.
* **Dữ liệu kiểm thử:**
  * Username: `wronguser`
  * Password: `SuperSecretPassword!`
* **Kết quả mong đợi:**
  * Hệ thống từ chối đăng nhập và hiển thị thông báo lỗi: `"Your username is invalid!"`.
