from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    # Locators
    SEARCH_INPUT = (By.CSS_SELECTOR, "input.search-form__input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.search-form__submit")
    CART_BUTTON = (By.CSS_SELECTOR, "rz-cart")
    NAV_CATALOG_BUTTON = (By.CSS_SELECTOR, "button.menu-toggler")
    FOOTER = (By.CSS_SELECTOR, "rz-footer")
    PROMOTIONS_LINK = (By.CSS_SELECTOR, "a[href*='sale']")

    def open_home(self):
        self.open("/")

    def search(self, query):
        search_input = self.find_element(self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(query)
        self.click(self.SEARCH_BUTTON)

    def open_cart(self):
        self.click(self.CART_BUTTON)

    def is_footer_visible(self):
        return self.is_visible(self.FOOTER)
