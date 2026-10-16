# Ghi chú Bài tập Tuần 05 - ThảoHT

## 1. Trả lời câu hỏi đọc tài liệu
- **Định vị ô login ổn định nhất:** Dùng `By.ID` vì ID là thuộc tính duy nhất trên trang web.
- **Lệnh nhập chữ:** Dùng hàm `.send_keys("nội dung")`.
- **Xem ID qua DevTools:** Bấm F12 -> Dùng công cụ Inspect chỉ vào ô nhập liệu để xem thuộc tính `id`.
- **Pytest khi kết quả khác mong đợi:** Báo lỗi `AssertionError` và đánh dấu bài test bị `FAILED`.

## 2. Bài học rút ra & AI Log
- **Nội dung đã học:**
  - Biết cách định vị element bằng `By.ID` và `By.CSS_SELECTOR`.
  - Biết cách giả lập thao tác gõ phím (`send_keys`) và click chuột (`click`).
  - Biết cách tạo `@pytest.fixture` để tự động mở/đóng browser cho từng test case.
- **Sử dụng AI:**
  - **Hỏi AI:** "Cách viết pytest fixture để dùng chung trình duyệt Chrome cho nhiều hàm test?"
  - **Kết quả:** AI gợi ý dùng `@pytest.fixture` giúp code ngắn gọn, tránh lặp lại đoạn `webdriver.Chrome()` nhiều lần.
