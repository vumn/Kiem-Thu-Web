import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By 

def test_login_wrong_password():
    # Bước 1: Khởi tạo trình duyệt
    driver = webdriver.Chrome()

    try:
        # Bước 2: Truy cập vào web
        driver.get("https://the-internet.herokuapp.com/login")

        # Bước 3: Tìm username, password, nút login
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        # Bước 4: Nhập tài khoản đúng nhưng mật khẩu sai
        username.send_keys("tomsmith")
        password.send_keys("WrongPassword!")

        # Bước 5: Nhấn nút đăng nhập
        login.click()

        # Kiểm tra thông báo thực tế trên web
        # Thẻ có id='flash' chứa nội dung thông báo thành công/thất bại
        flash_message = driver.find_element(By.ID, "flash").text

        assert "Your password is invalid!" in flash_message
    finally:
        # Bước 5: Kết thúc phiên
        driver.quit()

if __name__ == "__main__":
    test_login_wrong_password()