from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class SearchPage(BasePage):

    URL = TestData.BASE_URL + "search/"

    # локатор "Лабиринт" логотип, с помощью которого мы можем вернуться на домашнюю страницу
    LABIRINT_MAIN_LOGO = (By.XPATH, '//span[@class="b-header-b-logo-e-logo"]')

    # локатор кнопки  "Принять" политику cookies
    COOKIES_POLICY_BUTTON = (By.XPATH, '//button[@class="cookie-policy__button js-cookie-policy-agree"]')

    # локатор заголовка "Поиск по Лабиринту"
    SEARCH_FIELD = (By.ID, "search-field")
    # локатор "Искать"
    SEARCH_SUBMIT = (By.XPATH, '//button[@class="b-header-b-search-e-btn"]')

    # локатор поиска по автору
    AUTHOR_NAME = (By.XPATH, '//div[@class="product-author"]/a')
    # локатор поиска описания книги, под абложкой
    BOOK_DESCRIPTION = (By.XPATH, '//a[@class="product-title-link"]')

    # локатор меню "ВСЕ ФИЛЬТРЫ"
    ALL_FILTERS = (By.XPATH, '//span[@class="navisort-item__content" and contains(text(), "ВСЕ ФИЛЬТРЫ")]')
    # локатор "Бумажные книги" в меню "ВСЕ ФИЛЬТРЫ"
    PAPER_BOOKS_IN_ALL_FILTERS = (By.XPATH, '//span[contains(text(), "Бумажные книги")]')
    # кнопка "Электронные книги" вменю "ВСЕ ФИЛЬТРЫ"
    DIGITAL_BOOKS_IN_ALL_FILTERS = (By.XPATH, '//span[contains(text(), "Электронные книги")]')
    # кнопка "Показать" в конце "ВСЕ ФИЛЬТРЫ" для подтверждения настроек
    SHOW_RESULTS = (By.XPATH, '//input[@class="show-goods__button" and @value="Показать"]')
    # кнопка "ЦЕНА", появляется скрытое меню для настройки цена
    PRICE_MENU_BUTTON = (By.XPATH, '//div[@class="bl-name" and contains(text(), "ЦЕНА")]')
    # поле ввода минимальной цены
    SET_MIN_PRICE = (By.ID, "section-search-form-price_min")
    # поле ввода максимальной цены
    SET_MAX_PRICE = (By.ID, "section-search-form-price_max")

    # локатор быстрой настройки, текущая настройка, бумажные включены
    ENABLED_PAPER_BOOKS = (By.XPATH, '//div[contains(text(), "Бумажные книги")]')
    # локатор "В наличии" включен
    BOOKS_AVAILABLE_CURRENTLY = (By.XPATH, '//div[@class="filter-reset__content" and contains(text(), "В наличии")]')
    ALL_CURRENT_SETTINGS = (By.XPATH, '//div[@class="filter-reset__content"]')

    # локатор для метки "ЭЛЕКТРОННАЯ КНИГА" под обложкой
    DIGITAL_BOOKS_LABEL = (By.XPATH, '//span[@class="card-label__text card-label__text_inversed" and contains(text(), '
                                     '"Электронная книга")]')
    # локатор "КУПИТЬ", отображается если доступна сейчас
    BUY_NOW_BUTTON = (By.XPATH, '//a[@class="btn buy-link js-ebooks-buy-btn btn-primary" and contains(text(), '
                                '"КУПИТЬ")]')

    # локатор цены книги
    BOOK_PRICE_STRING = (By.XPATH, '//span[@class="price-val"]/span')
    # локатор для кнопки разивки по странице
    PAGINATION_PAGE_BUTTON = (By.XPATH, '//a[@class="pagination-next__text" and contains(text(), "Следующая")]')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(SearchPage.URL)


    """проверка, "слова поиска" находятся в текстовом результате, если результат был найден по значению атрибута"""

    def search_match_fully(self, element, search_name):
        element_text = element.get_attribute(TestData.ATTRIBUTE_TITLE)
        element_in_list = element_text.lower().split()
        name_list = search_name.lower().split()
        result = list(set(element_in_list) & set(name_list))
        return len(name_list) == len(result)

    """получить цену книги"""

    def price_by_int(self, element):
        element_text = element.text
        price_string = element_text.replace(' ', '').replace('₽', '')
        return int(price_string)