## Nguyễn Đức Hải

1. Với ô tên đăng nhập ở trang /login, nên xác định bằng id, vì id là độc nhất trên trang.

2. Dùng send_keys() để nhập chữ vào ô nhập liệu

3. Để biết id của 1 ô nhập trên trang :
   - Nhấn F12 trên bàn phím -> chọn tab Elements
   - Nhấn tổ hợp phím Ctrl + Shift + C rồi chọn ô nhập muốn lấy id
     -> Trang Elements bôi xanh dòng chứa thông tin ô nhập

4. Nếu kết quả thực tế khác kết quả mong đợi, pytest báo FAILED với lỗi AssertionError.

## Hỏi AI

1. Cách kiểm chuyển element thành String và check bàng in
2. Luôn có time_sleep() để trang web có thể load sau khi thao tác với các element
