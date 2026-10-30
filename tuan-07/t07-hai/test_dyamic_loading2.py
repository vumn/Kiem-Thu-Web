import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (NoSuchElementException)

# Kiểm tra Invisibility: kiểm tra sau 10s thì loading không còn hiển thị trên giao diện
def test_invisibility_loading():
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
        driver.find_element(By.CSS_SELECTOR, "#start button").click()
        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.invisibility_of_element_located((By.ID, "loading"))
        )
        loading = driver.find_element(By.ID, "loading")
        assert loading.is_displayed() == False

    finally:
        driver.quit()

# Kiểm tra Presence: kiêmr tra phần tử chưa được tạo ra trong DOM
def test_presence_after_loading():
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        driver.find_element(By.CSS_SELECTOR, "#start button").click()

        with pytest.raises(NoSuchElementException):
            driver.find_element(By.CSS_SELECTOR, "#finish h4")
            print("NoSuchElementException: Phần tử chưa được tạo ra trong DOM")

    finally:
        driver.quit()


# Kiểm tra Visibility: Chờ phần tử được tạo và hiển thị
def test_visibility_after_loading():
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        driver.find_element(By.CSS_SELECTOR, "#start button").click()

        wait = WebDriverWait(driver, 10)

        result = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )
        assert result.is_displayed() == True
        assert result.text == "Hello World!"

    finally:
        driver.quit()





