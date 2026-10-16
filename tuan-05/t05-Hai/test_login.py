from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# thông tin đăng nhập hợp lệ
def test_TC01():
    try: 
        # khởi tạo và mở web
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/login")
        # lấy các element và thao tác
        username = driver.find_element(By.ID,"username")
        username.send_keys("tomsmith")   
        password = driver.find_element(By.ID,"password")
        password.send_keys("SuperSecretPassword!")
        btn = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
        btn.click()
        time.sleep(3)  # chờ 3 giây để load trang sau khi đăng nhập
        # kiểm tra kết quả
        message = driver.find_element(By.ID,"flash")
        assert  "You logged into a secure area!" in message.text
        
    finally:
        driver.quit()
        
# username đúng, password sai
def test_TC02():
    try: 
        # khởi tạo và mở web
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/login")
        # lấy các element và thao tác
        username = driver.find_element(By.ID,"username")
        username.send_keys("tomsmith")   
        password = driver.find_element(By.ID,"password")
        password.send_keys("abc123")  # sai mật khẩu
        btn = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
        btn.click()
        time.sleep(3) 
        # kiểm tra kết quả
        message = driver.find_element(By.ID,"flash")
        assert  "Your password is invalid!" in message.text
        
    finally:
        driver.quit()

# username sai, passsword đúng
def test_TC03():
    try: 
        # khởi tạo và mở web
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/login")
        # lấy các element và thao tác
        username = driver.find_element(By.ID,"username")
        username.send_keys("abc123")  # sai username
        password = driver.find_element(By.ID,"password")
        password.send_keys("SuperSecretPassword!")  
        btn = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
        btn.click()
        time.sleep(3) 
        # kiểm tra kết quả
        message = driver.find_element(By.ID,"flash")
        assert  "Your username is invalid!" in message.text
        
    finally:
        driver.quit()