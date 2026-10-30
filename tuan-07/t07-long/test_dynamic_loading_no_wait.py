import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_dynamic_loading_no_wait():
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        driver.find_element(By.CSS_SELECTOR, "#start button").click()

        result = driver.find_element(By.CSS_SELECTOR, "#finish h4")
        assert result.text == "Hello World!"
        print(f"Example 1: {result.text}")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_dynamic_loading_no_wait()