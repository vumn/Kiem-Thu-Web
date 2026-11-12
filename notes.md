# Ghi chú Học tập & Nhật ký Tuần 07

## 1. Trả lời Câu hỏi Đọc Tài liệu Tuần 7

### Q1: Vì sao không nên dùng lệnh `time.sleep()` để chờ?
- **Tốc độ lãng phí:** `time.sleep(N)` bắt chương trình ngưng cố định `N` giây dù cho phần tử đã xuất hiện ngay ở giây thứ 1. Điều này làm bộ test chạy rất chậm.
- **Dễ gây flaky test:** Nếu mạng chậm quá `N` giây, bài test vẫn bị đứt (FAILED) dù giao diện vẫn hoạt động bình thường.
- **Giải pháp:** Sử dụng **Chờ tường minh (`WebDriverWait`)**, Selenium sẽ liên tục kiểm tra và tiếp tục ngay khi phần tử xuất hiện.

### Q2: Chờ "Phần tử hiển thị" khác chờ "Phần tử bấm được" thế nào?
- **Chờ phần tử hiển thị (`visibility_of_element_located`):** Phần tử đã có trong cây DOM và có kích thước (chiều cao, chiều rộng > 0), mắt người có thể nhìn thấy trên màn hình.
- **Chờ phần tử bấm được (`element_to_be_clickable`):** Phần tử không những phải hiển thị mà còn phải ở trạng thái khả dụng (`enabled`), không bị các phần tử khác (pop-up, lớp phủ loading) che khuất.

### Q3: (Team W3) Làm sao bấm OK trên hộp thoại Alert/Confirm?
Sử dụng phương thức chuyển hướng `switch_to.alert`:
```python
alert = driver.switch_to.alert
alert.accept()  # Nhấn nút OK / Accept
# alert.dismiss() # Nhấn nút Cancel (nếu là hộp thoại Confirm)
