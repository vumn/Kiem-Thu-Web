import pytest
from selenium import webdriver

def test_smoke():
    # Bước 1: Khởi tạo trình điều khiển Chrome (mở trình duyệt)
    driver = webdriver.Chrome()

    try:
        # Bước 2: Truy cập vào trang web cần kiểm thử
        driver.get("https://the-internet.herokuapp.com")

        # Bước 3: Lấy tiêu đề thực tế của trang web
        actual_title = driver.title

        # Bước 4: Kiểm tra xem tiêu đề trang có đúng là "The Internet" không
        assert actual_title == "The Internet"
    finally:
        # Bước 5: Đóng trình duyệt sau khi kiểm thử kết thúc
        driver.quit()