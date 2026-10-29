import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. TRƯỜNG HỢP KHÔNG DÙNG LỆNH CHỜ
def test_dynamic_loading_2_no_wait():
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
        driver.find_element(By.CSS_SELECTOR, "#start button").click()

        # Tìm và lấy chữ ngay -> Case này sẽ bị báo FAILED
        result = driver.find_element(By.CSS_SELECTOR, "#finish h4")
        print(f"No Wait Result: {result.text}")

    finally:
        driver.quit()

# 2. TRƯỜNG HỢP CÓ DÙNG LỆNH CHỜ
def test_dynamic_loading_2_with_wait():
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
        driver.find_element(By.CSS_SELECTOR, "#start button").click()

        # Chờ tối đa 10 giây cho đến khi chữ hiển thị -> Case này sẽ PASSED
        result = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )
        
        assert result.text == "Hello World!"
        print(f"With Wait Result: {result.text}")

    finally:
        driver.quit()
