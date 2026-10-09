from selenium import webdriver

def test_title():
   try :
        #khai báo driver
        driver = webdriver.Chrome()
        
        # Mở trang web
        driver.get("https://the-internet.herokuapp.com")
        # Tìm và kiểm tra title của trang web
        title = driver.title    
        assert title == "The Internet"
   finally :
        # đóng trình duyệt
        driver.quit()
    
    
    
