import pytest
from selenium import webdriver

def test_smoke():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/")
        assert driver.title == "The Internet"
        print("\n=> Test thanh cong!")
    finally:
        driver.quit()
