from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "app-cart-empty")
    CART_ITEMS = (By.CSS_SELECTOR, "rz-cart-product")
    CART_TOTAL = (By.CSS_SELECTOR, ".cart-receipt__sum-price")

    def open_cart_page(self):
        self.open("/cart")

    def is_cart_empty(self):
        return self.is_visible(self.EMPTY_CART_MESSAGE)

    def get_cart_items_count(self):
        items = self.find_elements(self.CART_ITEMS)
        return len(items)
