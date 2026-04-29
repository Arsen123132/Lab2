import pytest
from pages.home_page import HomePage


class TestNavigationToSmartphones:

    def test_tc_001_navigation_to_smartphones(self, driver):
        page = HomePage(driver)
        page.open_home()

        driver.get("https://rozetka.com.ua/mobile-phones/c80003/")

        current_url = driver.current_url
        assert "mobile-phones" in current_url or "smartphones" in current_url, (
            f"Очікувалось 'mobile-phones' або 'smartphones' у URL, отримано: {current_url}"
        )
