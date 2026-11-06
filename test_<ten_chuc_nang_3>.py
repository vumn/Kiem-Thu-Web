import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestChucNang3:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com/product/1")
        self.wait = WebDriverWait(self.driver, 10)

    def test_add_to_cart_success(self):
        """TC1: Kiểm thử thêm vào giỏ hàng thành công"""
        driver = self.driver
        add_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-btn")))
        add_btn.click()
        
        cart_badge = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        assert cart_badge.text == "1"

    def test_add_invalid_quantity(self):
        """TC2: Kiểm thử nhập số lượng sai"""
        driver = self.driver
        qty_input = driver.find_element(By.ID, "quantity")
        qty_input.clear()
        qty_input.send_keys("0")
        
        driver.find_element(By.ID, "add-to-cart-btn").click()
        error_msg = self.wait.until(EC.visibility_of_element_located((By.ID, "error-msg")))
        assert "Số lượng phải lớn hơn 0" in error_msg.text

    def teardown_method(self):
        self.driver.quit()
