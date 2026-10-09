1. Một script Selenium gồm 4 bước, và mỗi bước ứng với dòng các dòng trong bài kiếm thử

    Bước 1: Khởi tạo WebDriver (mở trình duyệt Chrome)
        Dòng: driver = webdriver.Chrome()
    Bước 2: Điều hướng đến trang web cần kiểm thử
        Dòng: driver.get("[https://the-internet.herokuapp.com] (https://the-internet.herokuapp.com)")
    Bước 3: Lấy dữ liệu từ trang web
        Dòng: actual_title = driver.title
    Bước 4: Kiểm tra kết quả (Assert)
        Dòng: assert actual_title == "The Internet"

2. pytest tự tìm bài kiểm thử dựa vào quy tắc đặt tên

    Tên file: Phải bắt đầu bằng test_*.py hoặc kết thúc bằng *_test.py
    Tên hàm: Bắt đầu bằng test_
    Tên class: không chứa hàm __init__()

3. Các lỗi gặp phải trong quá trình làm

    Khi chạy test lần đầu bị lỗi AssertionError: assert 'Application Error' == 'The Internet' mất hơn 42s do máy chủ của trang the-internet.herokuapp.com bị lỗi tạm thời (Application Error) dẫn đến title trả về sai. Sau khi kiểm tra lại server web và chạy lại thì test pass thành công.
    Khi cố tình sửa tiêu đề so sánh thành "The Internet Sai", pytest báo lỗi AssertionError chỉ rõ sự sai khác giữa chuỗi thực tế và chuỗi mong đợi. Sau khi sửa lại đúng thì toàn bộ bài test chạy PASS bình thường.
