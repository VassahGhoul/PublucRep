from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class BasketPage(BasePage):


    BASKET_URL = "https://www.labirint.ru/cart/"

    # для теста с с вводом количества в поле ввода
    QUANTITY_TO_ENTER = "7"

    # локатор "Лабиринт" для лого, возврат на главную станицу
    LABIRINT_MAIN_LOGO = (By.XPATH, '//a[@title="Лабиринт - самый большой книжный интернет магазин"]')

    # локатор кнопки  "В КОРЗИНУ" под каждой книгой
    MOVE_BOOK_TO_BASKET = (By.XPATH, '//a[@class="btn buy-link btn-primary" and contains(text(), "В КОРЗИНУ")]')
    # локатор цены книги
    BOOK_PRICE_STRING = (By.XPATH, '//span[@class="price-val"]')
    # локатор конечной цены книг на странице "Корзина"
    PURCHASE_FINAL_SUM = (By.ID, "basket-default-sumprice-discount")
    # локатор кнопки "Очистить корзину" страници "Корзина"
    REMOVE_ALL_GOODS_IN_BASKET = (By.XPATH, '//a[@class="b-link-popup" and contains(text(), "Очистить корзину")]')
    # локатор пустой корзины "Ваша корзина пуста. Почему?"
    BASKET_IS_EMPTY = (By.XPATH, '//span[@class="g-alttext-small g-alttext-grey g-alttext-head" and contains(text(), '
                                 '"Ваша корзина пуста. Почему?")]')
    # локатор всплывающего окна с кнопкой "Оформить"
    POPUP_CHECKOUT_BOOK_BUTTON = (By.XPATH, '//a[@class="color_white btn btn-small btn-primary basket-go '
                                            'analytics-click-js"]')
    # локатор поля ввода штук книг в корзине, под книгой
    QUANTITY_OF_EACH_ITEM_IN_BASKET = (By.XPATH, '//input[@class="quantity"]')
    # локатор кнопки "+", увеличить штук книг в корзине
    INCREASE_QUANTITY_OF_ITEM = (By.XPATH, '//span[@class="btn btn-increase btn-increase-cart"]')
    # локатор кнопки "-", уменьшить штук книг в корзине
    DECREASE_QUANTITY_OF_ITEM = (By.XPATH, '//span[@class="btn btn-lessen btn-lessen-cart"]')
    # локатор кнопки "Начать оформление"
    START_CHECKOUT = (By.XPATH, '//input[@class="btn btn-small btn-more"]')
    # Локатор кнопки "Оформить "
    CHECKOUT_AND_PAY = (By.XPATH, '//input[@value="Оформить и оплатить"]')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)


    """получаем цену книги"""
    def price_by_int(self, element):
        element_text = element.text
        price_string = element_text.replace(' ', '').replace('₽', '')
        return int(price_string)

    """удалить все книги из корзины, и возврат на главную страницу """

    def remove_all_good_in_basket_and_reload_page(self):
        quantity = self.get_element_text(TestData.BASKET_COUNTER)
        if int(quantity) != 0:
            self.do_click(TestData.BASKET_BUTTON_AT_HEADER)
            self.do_click(BasketPage.REMOVE_ALL_GOODS_IN_BASKET)
            self.do_click(BasketPage.LABIRINT_MAIN_LOGO)