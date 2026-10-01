# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Khởi động phiên
driver = webdriver.Chrome()

# Đến trang web cần test
driver.get("https://the-internet.herokuapp.com/")

# Tìm kiếm phần tử 
page_title = driver.title

def test_title():
    assert page_title == "The Internet"

# Kết thúc phiên
driver.quit()

if __name__ == "__main__":
    test_title()