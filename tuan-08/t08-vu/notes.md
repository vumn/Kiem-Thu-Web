1. Vì sao nên tạo báo cáo dạng một file duy nhất khi gửi cho người khác
- Khi bạn gửi báo cáo cho người khác (qua email, chat, hoặc đính kèm ticket), nếu chỉ gửi mỗi file .html mà quên gửi kèm thư mục assets, người nhận mở lên sẽ bị lỗi mất định dạng CSS hoặc không xem được giao diện đầy đủ. Tạo báo cáo dạng một file duy nhất (self-contained report) sẽ nhúng toàn bộ CSS và dữ liệu vào thẳng bên trong file .html đó, giúp việc chia sẻ kết quả tiện lợi, gọn gàng và hiển thị nguyên vẹn trên máy người nhận.
2. Chọn theo chữ hiển thị và theo giá trị khác nhau thế nào
- Chọn theo chữ hiển thị (select_by_visible_text): chọn dựa trên nội dung văn bản hiển thị trên màn hình, nên dùng khi kiểm thử trên góc nhìn của người dùng cuối hoặc khi giá trị value bị sinh tự động, khó đọc.
- Chọn theo giá trị (select_by_value): chọn dựa trên giá trị của thuộc tính 'value=' bên trong thẻ option, nên dùng khi cần chọn chính xác theo mã định danh hệ thống hoặc khi giao diện có text thay đổi nhưng value giữ nguyên
3. Vì sao tải file bằng cách gõ đường dẫn vào ô chọn file
- Selenium không thể tương tác với hộp thoại upload, nên nếu phần tử trên web là thẻ input với type=file, ta chỉ cần sử dụng phương thức send_keys để truyền đường dẫn tuyệt đối của file vào ô input
4. Đếm số phần tử trên trang web bằng cách nào
- Sử dụng phương thức find_elements(): trả về 1 list chứa tất cả các web element khớp điều kiện
- Sử dụng hàm len() để lấy độ dài của danh sách đó
