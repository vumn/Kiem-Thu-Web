import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Kiểm tra Implicit Wait: Kiểm tra sau 5s Hello World! được hiển thị trên giao diện chưa
def test_implicit_wait():
    driver = webdriver.Chrome()

    try:
        driver.implicitly_wait(5)
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        driver.find_element(By.CSS_SELECTOR, "#start button").click()
        result = driver.find_element(By.CSS_SELECTOR, "#finish h4")
        assert result.is_displayed() == False

    finally:
        driver.quit()

# kiểm tra Implicit Wait: Kiểm tra sau 10s Hello World! được hiển thị trên giao diện chưa
def test_implicit_wait_after_loading():
    driver = webdriver.Chrome()
    try:
        driver.implicitly_wait(10)
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        driver.find_element(By.CSS_SELECTOR, "#start button").click()
        result = driver.find_element(By.CSS_SELECTOR, "#finish h4")
        assert result.is_displayed() == True

    finally:
        driver.quit()

# Kiểm tra Presence: Phần tử có tồn tại trong DOM nhưng bị ẩn trên giao diện
def test_presence_hidden_element():
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

        wait = WebDriverWait(driver, 1)

        result = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )

        assert result.is_displayed() == False

    finally:
        driver.quit()


# Kiểm tra Visibility: Chờ phần tử hiển thị sau khi nhấn Start
def test_visibility_after_loading():
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

        driver.find_element(By.CSS_SELECTOR, "#start button").click()

        wait = WebDriverWait(driver, 10)

        result = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )

        assert result.is_displayed() == True

    finally:
        driver.quit()

# Kiểm tra TimeoutException: Visibility thất bại khi chưa nhấn Start
def test_visibility_timeout():
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

        wait = WebDriverWait(driver, 3)
        with pytest.raises(TimeoutException):
            wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
            )
            print("TimeoutException: Phần tử chưa được hiển thị trên giao diện")
    finally:
        driver.quit()





    


