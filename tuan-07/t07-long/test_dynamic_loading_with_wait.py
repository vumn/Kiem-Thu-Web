import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_dynamic_loading_with_wait():
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        driver.find_element(By.CSS_SELECTOR, "#start button").click()

        # Áp dụng lệnh chờ tường minh: Chờ tối đa 10s cho đến khi chữ hiển thị hẳn lên
        result = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )
        
        assert result.text == "Hello World!"
        print(f"Example 1: {result.text}")

    finally:
        driver.quit()
