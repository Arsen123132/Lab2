Testing-lab-2
https://github.com/Arsen123132/Lab2
Загальна кількість тестів: 5
Успішно пройдено (PASSED): 5 (100%)
Загальний час виконання: 116.49 секунд
tests/test_tc_001_navigation_to_smartphones.py::TestNavigationToSmartphones::test_tc_001_navigation_to_smartphones PASSED [ 20%]
tests/test_tc_002_filter_by_brand.py::TestFilterByBrand::test_tc_002_filter_by_brand PASSED [ 40%]
tests/test_tc_003_footer_presence.py::TestFooterPresence::test_tc_003_footer_presence PASSED [ 60%]
tests/test_tc_004_cart_empty_state.py::TestCartEmptyState::test_tc_004_cart_empty_state PASSED [ 80%]
tests/test_tc_005_promotions_page.py::TestPromotionsPage::test_tc_005_promotions_page PASSED [100%]
============================ 5 passed in 116.49s (0:01:56) ============================
Короткий опис реалізованих тестових сценаріїв
В рамках роботи було розроблено та автоматизовано наступні користувацькі сценарії з використанням патерну Page Object Model на базі веб-застосунку rozetka.com.ua:
test_tc_001_navigation_to_smartphones (Навігація): Перевіряє коректність переходу з головної сторінки до розділу каталогу зі смартфонами. Валідація здійснюється шляхом перевірки наявності ключового слова "mobile-phones" або "smartphones" у URL-адресі сторінки після кліку.
test_tc_002_filter_by_brand (Функціональний тест): Перевіряє роботу фільтрації товарів за брендом. Сценарій переходить у відповідний розділ каталогу смартфонів, застосовує фільтр за брендом "Samsung" та перевіряє, що URL містить параметр фільтру і сторінка успішно завантажила контент.
test_tc_003_footer_presence (UI-тест): Перевіряє наявність та видимість нижньої інформаційної панелі сайту (футера) при завантаженні головної сторінки rozetka.com.ua.
test_tc_004_cart_empty_state (Функціональний тест кошика): Сценарій відкриває сторінку кошика без попереднього додавання товарів та перевіряє, що користувачу коректно відображається повідомлення про те, що кошик наразі порожній.
test_tc_005_promotions_page (Навігація): Перевіряє роботу переходу на сторінку акційних пропозицій. Успішність перевіряється через аналіз поточного URL (очікується наявність "sale" у посиланні).