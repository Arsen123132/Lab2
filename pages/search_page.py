from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):
    PRODUCT_CARDS = (By.CSS_SELECTOR, "app-goods-tile-default")
    FILTER_SIDEBAR = (By.CSS_SELECTOR, "rz-sidebar-filters")
    FILTER_SECTION_TITLE = (By.CSS_SELECTOR, "rz-filter-section-item button")
    FILTER_CHECKBOX = (By.CSS_SELECTOR, "rz-filter-section-item a")
    PRODUCTS_COUNT = (By.CSS_SELECTOR, ".catalog-selection__found")
    CATEGORY_TITLE = (By.CSS_SELECTOR, "h1.catalog__title")
    PRICE_FILTER_MIN = (By.CSS_SELECTOR, "input[formcontrolname='min']")
    PRICE_FILTER_MAX = (By.CSS_SELECTOR, "input[formcontrolname='max']")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "rz-sort select")

    def get_product_count(self):
        cards = self.find_elements(self.PRODUCT_CARDS)
        return len(cards)

    def has_products(self):
        return self.get_product_count() > 0

    def get_page_title(self):
        return self.find_element(self.CATEGORY_TITLE).text

    def is_filter_sidebar_visible(self):
        return self.is_visible(self.FILTER_SIDEBAR)
