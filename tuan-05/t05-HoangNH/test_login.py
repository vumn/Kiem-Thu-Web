import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def driver():
    # Khởi tạo trình duyệt trước mỗi test
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    # Tự động đóng trình duyệt sau khi test xong
    driver.quit()

# TC01: Nhập sai username -> đăng nhập thất bại
def test_login_failed_username(driver):
    username = driver.find_element(By.NAME, value="username")
    password = driver.find_element(By.ID, value="password")
    submit_button = driver.find_element(By.CLASS_NAME, value="radius")

    username.send_keys("randomUserName")
    password.send_keys("SuperSecretPassword!")
    submit_button.click()

    failed_username = driver.find_element(By.ID, value="flash")
    assert "Your username is invalid!" in failed_username.text

# TC02: Nhập sai password -> đăng nhập thất bại
def test_login_failed_password(driver):
    username = driver.find_element(By.NAME, value="username")
    password = driver.find_element(By.ID, value="password")
    submit_button = driver.find_element(By.CLASS_NAME, value="radius")

    username.send_keys("tomsmith")
    password.send_keys("wrongPassword")
    submit_button.click()
    
    failed_password = driver.find_element(By.ID, value="flash")
    assert "Your password is invalid!" in failed_password.text

# TC03: Login thành công
def test_login_success(driver):
    username = driver.find_element(By.NAME, value="username")
    password = driver.find_element(By.ID, value="password")
    submit_button = driver.find_element(By.CLASS_NAME, value="radius")

    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")
    submit_button.click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://the-internet.herokuapp.com/secure") 
    )
    success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )
    assert success.is_displayed()
    assert "You logged into a secure area!" in success.text