import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
 
class TestFilterByBrand:
 
    def test_tc_002_filter_by_brand(self, driver):
        driver.get("https://rozetka.com.ua/mobile-phones/c80003/producer=samsung/")
 
        # Чекаємо повного завантаження сторінки
        time.sleep(5)
 
        current_url = driver.current_url
 
        # Перевірка 1: URL містить фільтр
        assert "samsung" in current_url.lower() or "mobile-phones" in current_url.lower(), (
            f"Очікувалось URL з фільтром Samsung, отримано: {current_url}"
        )
 
        # Перевірка 2: сторінка не порожня — є хоча б якийсь контент
        body_text = driver.find_element(By.TAG_NAME, "body").text
        assert len(body_text) > 100, (
            "Сторінка з фільтром Samsung завантажилась порожньою."
        )
 
        # Перевірка 3: немає повідомлення про помилку або блокування
        assert "403" not in body_text and "blocked" not in body_text.lower(), (
            "Сторінка повернула помилку доступу."
        )