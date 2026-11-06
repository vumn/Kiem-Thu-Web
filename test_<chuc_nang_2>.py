import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestChucNang2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        # Chờ tường minh tối đa 10 giây
        self.wait = WebDriverWait(self.driver, 10)

    def test_wait_element_success(self):
        """Test Case 1: Thử nghiệm bấm Start và chờ dòng chữ kết quả xuất hiện"""
        driver = self.driver
        
        # 1. Tìm nút Start và click
        start_btn = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_btn.click()
        
        # 2. CHỜ TƯỜNG MINH cho đến khi phần tử kết quả hiển thị (thay vì dùng time.sleep)
        finish_text = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )
        
        # 3. Xác nhận kết quả
        self.assertEqual(finish_text.text, "Hello World!")

    def test_search_invalid_keyword(self):
        """Test Case 2 (Trường hợp sai): Nhập từ khóa sai và kiểm tra kết quả"""
        # Thay bằng kịch bản thực tế chức năng 2 của nhóm bạn
        pass

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
