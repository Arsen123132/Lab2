import pytest
from pages.home_page import HomePage


class TestFooterPresence:

    def test_tc_003_footer_presence(self, driver):
        page = HomePage(driver)
        page.open_home()

        assert page.is_footer_visible(), (
            "Футер сайту не знайдений або не видимий на головній сторінці."
        )
