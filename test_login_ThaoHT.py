import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    # Khởi tạo trình duyệt Chrome trước mỗi bài test
    browser = webdriver.Chrome()
    browser.implicitly_wait(10) # Chờ tối đa 10 giây để các phần tử hiển thị
    yield browser
    # Đóng trình duyệt sau khi test xong
    browser.quit()

# -------------------------------------------------------------
# Test Case 1: Đăng nhập thành công
# -------------------------------------------------------------
def test_login_success(driver):
    # 1. Mở trang đăng nhập
    driver.get("https://the-internet.herokuapp.com/login")
    
    # 2. Tìm ô username và nhập tài khoản đúng
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    
    # 3. Tìm ô password và nhập mật khẩu đúng
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    
    # 4. Bấm nút Login
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # 5. Kiểm tra kết quả mong đợi
    flash_message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in flash_message
    assert "/secure" in driver.current_url

# -------------------------------------------------------------
# Test Case 2: Đăng nhập thất bại do sai Username
# -------------------------------------------------------------
def test_login_invalid_username(driver):
    # 1. Mở trang đăng nhập
    driver.get("https://the-internet.herokuapp.com/login")
    
    # 2. Nhập sai username
    driver.find_element(By.ID, "username").send_keys("sai_username")
    
    # 3. Nhập đúng password
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    
    # 4. Bấm nút Login
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # 5. Kiểm tra thông báo lỗi
    flash_message = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in flash_message

# -------------------------------------------------------------
# Test Case 3: Đăng nhập thất bại do sai Password
# -------------------------------------------------------------
def test_login_invalid_password(driver):
    # 1. Mở trang đăng nhập
    driver.get("https://the-internet.herokuapp.com/login")
    
    # 2. Nhập đúng username
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    
    # 3. Nhập sai password
    driver.find_element(By.ID, "password").send_keys("sai_password")
    
    # 4. Bấm nút Login
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # 5. Kiểm tra thông báo lỗi
    flash_message = driver.find_element(By.ID, "flash").text
    assert "Your password is invalid!" in flash_message
