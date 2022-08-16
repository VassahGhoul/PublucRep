from selenium.webdriver.common.by import By


class TestData:
    CHROME_EXECUTABLE_PATH = "G:\Anaconda\Driverss\chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = "G:\Anaconda\Driverss\geckodriver.exe"

    BASE_URL = "https://www.labirint.ru/"

    # HOME PAGE данные для тестирования главного меню - кнопка "Книги"
    BOOKS_BUTTON_DESCRIPTION = "Книги"
    TITLE_OF_BOOK_PAGE = "Книги"
    TITLE_OF_MAIN_YEAR_BOOK_PAGE = "Главное 2022"
    ALL_BOOKS_TITLE = "Книги"
    TEENS_BOOKS_TITLE = "Молодежная литература"
    PERIODICALS_TITLE = "Периодические издания"
    BILINGUAL_TITLE = "Билингвы"
    CHILD_BOOK_TITLE = "Детский досуг"
    MANGA_BOOK_TITLE = "Манга для детей"
    RELIGION_BOOK_TITLE = "Религии мира"

    # Настройка текущего региона
    CITY_TO_SET = "Москва"
    CURRENT_CITY = "Москва"

    # проверка "москва" кирилица
    CITY_TO_SET_IN_CYRILLIC = "Новосибирск"
    FIRST_CITY_IN_AUTO_ADVICE = "Новосибирск"

    CITY_TO_SET_WRONG_LANGUAGE = "Rfkbybyuhfl"
    FIRST_CITY_IN_AUTO_ADVICE_IN_CYRILLIC = "Калининград"

    # Данные для теста страницы "Отложенные товары" PostponePage
    NUMBER_OF_BOOKS_TO_POSTPONE = 3

    # Страница "Отложенные товары" PostponePage - удаление книг
    SUCCESSFUL_DELETION = "Выбранные товары удалены!"

    # Страница "Моя корзина" Basket - удаление книг
    YOUR_BASKET_IS_EMPTY_TEXT = "Ваша корзина пуста. Почему?"

    # Имена атррибутов
    ATTRIBUTE_ID = "id"
    ATTRIBUTE_TITLE = "title"
    ATTRIBUTE_VALUE = "value"

    # Данные для поиска
    AUTHOR_SEARCH = "Иван Тургенев"
    SEARCHED_BOOK_NAME = "Муму"
    SEARCHED_RUSSIAN_BOOK_NAME_BY_LATIN = "Uhfa Vjynt-Rhbcnj"  # "Граф Монте-Кристо"
    EXPECTED_RESULT_BOOK_NAME = "Граф Монте-Кристо"

    # Данные для фильтра
    MIN_PRICE = "500"
    MAX_PRICE = "600"

    """Локаторы"""

    # Локатор закрытия окна после действий ("В Корзину", "ОТЛОЖИТЬ", etc)
    CLOSE_POPUP_ANY_ACTION = (By.XPATH, '//a[@class="b-basket-popinfo-close"]')

    """for BASKET"""
    # Локатор кнопки "Корзина" в header
    BASKET_BUTTON_AT_HEADER = (By.XPATH, '//a[@class="b-header-b-personal-e-link top-link-main '
                                         'analytics-click-js cart-icon-js"]')
    # Локатор кнопки "Корзина" с товарами
    BASKET_COUNTER = (By.XPATH, '//span[@class="b-header-b-personal-e-icon-count-m-cart basket-in-cart-a"]')

