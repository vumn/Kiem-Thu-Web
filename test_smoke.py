import pytest
from selenium import webdriver

def test_smoke():
    # Bước 1: Khởi tạo trình duyệt
    driver = webdriver.Chrome()

    try:
        # Bước 2: Truy cập vào web
        driver.get("https://the-internet.herokuapp.com")

        # Bước 3: Lấy tiêu đề của trang web
        actual_title = driver.title

        # Bước 4: Kiểm tra kết quả
        assert actual_title == "The Internet"
    finally:
        # Bước 5: Kết thúc phiên
        driver.quit()

if __name__ == "__main__":
    test_smoke()