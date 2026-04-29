import pytest
from pages.home_page import HomePage


class TestPromotionsPage:
    
    def test_tc_005_promotions_page(self, driver):
        driver.get("https://rozetka.com.ua/sale/")

        current_url = driver.current_url
        assert "sale" in current_url or "aktsii" in current_url or "akcii" in current_url, (
            f"Очікувалось 'sale' або 'aktsii' у URL сторінки акцій, "
            f"отримано: {current_url}"
        )
