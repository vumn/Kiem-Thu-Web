# Danh sách Test Case Chức năng Đăng nhập (Tuần 05)

## Test Case 1: Đăng nhập thành công
- **Các bước thực hiện:**
  1. Truy cập trang `https://the-internet.herokuapp.com/login`
  2. Nhập `tomsmith` vào ô Username
  3. Nhập `SuperSecretPassword!` vào ô Password
  4. Nhấn nút Login
- **Kết quả mong đợi:** Đăng nhập thành công, xuất hiện thông báo chứa chữ "You logged into a secure area!" và URL chuyển sang `/secure`.

## Test Case 2: Đăng nhập thất bại (Sai Username)
- **Các bước thực hiện:**
  1. Truy cập trang `https://the-internet.herokuapp.com/login`
  2. Nhập `sai_username` vào ô Username
  3. Nhập `SuperSecretPassword!` vào ô Password
  4. Nhấn nút Login
- **Kết quả mong đợi:** Đăng nhập thất bại, xuất hiện thông báo lỗi chứa chữ "Your username is invalid!".

## Test Case 3: Đăng nhập thất bại (Sai Password)
- **Các bước thực hiện:**
  1. Truy cập trang `https://the-internet.herokuapp.com/login`
  2. Nhập `tomsmith` vào ô Username
  3. Nhập `sai_password` vào ô Password
  4. Nhấn nút Login
- **Kết quả mong đợi:** Đăng nhập thất bại, xuất hiện thông báo lỗi chứa chữ "Your password is invalid!".
