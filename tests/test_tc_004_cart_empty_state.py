import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
 
class TestCartEmptyState:
 
    def test_tc_004_cart_empty_state(self, driver):
        driver.get("https://rozetka.com.ua/cart/")
 
        wait = WebDriverWait(driver, 20)
 
        empty_selectors = [
            "app-cart-empty",
            ".cart-empty",
            "rz-empty-cart",
            ".empty-cart",
            "[class*='empty']",
        ]
 
        found = False
        for selector in empty_selectors:
            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                element = driver.find_element(By.CSS_SELECTOR, selector)
                if element.is_displayed():
                    found = True
                    break
            except Exception:
                continue
 
        if not found:
            page_text = driver.find_element(By.TAG_NAME, "body").text.lower()
            found = any(word in page_text for word in [
                "кошик порожній", "кошик пустий", "cart is empty",
                "порожній", "nothing here", "немає товарів"
            ])
 
        assert found, (
            "Очікувалось повідомлення про порожній кошик, "
            "але воно не відображається."
        )