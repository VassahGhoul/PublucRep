import time
from Config.config import TestData
from Pages.BasketPage import BasketPage
from Tests.test_base import BaseTest


# для запуска всех тестов: pytest Tests/test_BasketPage.py

class TestBasketFmHomePage(BaseTest):

    # поиск первой книги на домашней странице, в корзину, проверка цены в корзине
    # цена не меняется
    def test_first_book_moved_in_basket_and_price_is_same(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.accept_cookies_policy()
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # поиск "В КОРЗИНУ" на главной странице
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # поиска добавить "В КОРЗИНУ" первой книги
        fist_book_button_move_into_basket = self.list_of_buttons_move_into_basket[0]
        # поиск цены книг
        self.list_of_book_prices = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # цена первой книги
        first_book_price_element = self.list_of_book_prices[0]
        # получить цену книги
        first_book_price = self.basketPage.price_by_int(first_book_price_element)
        # нажать "В КОРЗИНУ"
        fist_book_button_move_into_basket.click()
        # закрыть окно всплывающее
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # нажать "Корзина" в заголовке
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # все цены книг в карзине
        self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # поиск элемента с ценами книг в корзине
        price_of_first_book_string = self.list_of_book_prices_in_basket[0]
        # получить цену книги в корзине
        first_book_price_in_basket = self.basketPage.price_by_int(price_of_first_book_string)
        assert first_book_price == first_book_price_in_basket

    # тест кнопки "Очистить корзину" отображается и удаляет из корзины
    def test_that_clear_basket_button_clean_basket(self):
        self.basketPage = BasketPage(self.driver)
        # ищем "В КОРЗИНУ"
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # ищем и добавляем "В КОРЗИНУ" книгу
        self.list_of_buttons_move_into_basket[0].click()
        # закрыть окно всплывающее
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # жмем "Корзина" в заголовке сайта
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # поиск цен книг в "корзине", страница корзины
        self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # ищем первую книку,  страница корзины
        price_of_first_book_string = self.list_of_book_prices_in_basket[0]
        self.basketPage.do_click(BasketPage.REMOVE_ALL_GOODS_IN_BASKET)
        result = self.basketPage.get_element_text(BasketPage.BASKET_IS_EMPTY)
        assert self.basketPage.element_is_not_visible(price_of_first_book_string)
        assert result.lower() == TestData.YOUR_BASKET_IS_EMPTY_TEXT.lower()

    # проверка цены книги и в итоге без доставкив корзине
    def test_first_book_moved_in_basket_and_price_is_same_and_equal_final_sum(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # ищем "В КОРЗИНУ"
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # ищем и добавляем "В КОРЗИНУ" книгу
        fist_book_button_move_into_basket = self.list_of_buttons_move_into_basket[0]
        # ищем цены всех книг
        self.list_of_book_prices = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # ищем элемент с ценой нашей книги
        first_book_price_element = self.list_of_book_prices[0]
        # получаем цену книги
        first_book_price = self.basketPage.price_by_int(first_book_price_element)
        # перемещаем "В КОРЗИНУ" нашу книгу
        fist_book_button_move_into_basket.click()
        # закрыть всплывающее окно
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # жмем "Корзина" в заголовке
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # ищем цены всех книг в "корзина", страница корзина
        self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # ищем элемент с ценой нашей книги, страница корзина
        price_of_first_book_string = self.list_of_book_prices_in_basket[0]
        # получаем цену книги, , страница корзина
        first_book_price_in_basket = self.basketPage.price_by_int(price_of_first_book_string)
        # получаем конечную сумму
        final_sum = self.basketPage.get_element_text(BasketPage.PURCHASE_FINAL_SUM).replace(' ', '')
        assert (first_book_price and first_book_price_in_basket) == int(final_sum)

    # проверка цены книги и в итоге без доставкив корзине
    def test_that_button_in_popup_window_leads_to_basket(self):
        self.basketPage = BasketPage(self.driver)
        # ищем "В КОРЗИНУ"
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # ищем и добавляем "В КОРЗИНУ" книгу
        fist_book_button_move_into_basket = self.list_of_buttons_move_into_basket[0]
        # жмем "В КОРЗИНУ"
        fist_book_button_move_into_basket.click()
        # жмем "Оформить" в выпадающем окне
        self.basketPage.find_several_element(BasketPage.POPUP_CHECKOUT_BOOK_BUTTON)[0].click()
        assert self.basketPage.get_current_url() == BasketPage.BASKET_URL

    # тест начального кол-ва товара "В КОРЗИНУ" 1 штука
    def test_that_initial_quantity_of_item_added_in_basket_is_one(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # ищем "В КОРЗИНУ"
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # ищем и добавляем "В КОРЗИНУ" книгу
        self.list_of_buttons_move_into_basket[0].click()
        # закрыть всплывающее окно
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # жмем "Корзина" в заголовке
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # ищем поле ввода кол-ва товара в товарах
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
            BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
        # ищем поле последнего добавленного товара
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        # ищем кол-во последнего добавленного товара
        quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        assert int(quantity_of_first_book) == 1

    # тест проверки увеличения товара в "корзине" увеличилось кнопкой "+"
    def test_that_quantity_of_item_added_in_basket_can_be_increased(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # ищем "В КОРЗИНУ"
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # ищем и добавляем "В КОРЗИНУ" книгу
        self.list_of_buttons_move_into_basket[0].click()
        # закрыть всплывающее окно
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # cжмем "Корзина" в заголовке
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # ищем поле ввода кол-ва товара в товарах
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
            BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
        # ищем поле ввода кол-ва последнего товара
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        # ищем количество последнего товара
        quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        # ищем все кнопки "+"
        self.list_of_increase_buttons = self.basketPage.find_several_element(BasketPage.INCREASE_QUANTITY_OF_ITEM)
        # увеличиваем количество товара кнопкой "+"
        self.list_of_increase_buttons[0].click()
        # повторяем запрос количество последнего товара
        new_quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        assert int(new_quantity_of_first_book) - int(quantity_of_first_book) == 1

    # тест проверки уменьшения товара в "корзине" кнопкой "-"
    def test_that_quantity_can_set_by_enter_digits_into_input_field(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # ищем кнопку "В КОРЗИНУ"
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # ищем и добавляем товар "В КОРЗИНУ"
        self.list_of_buttons_move_into_basket[0].click()
        # закрываем всплывающее окно
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # жмем "Корзина" в заголовке
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # ищем поля ввода кол-ва товара
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
            BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
        # ищем поля ввода кол-ва добавленного товара
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        # ищем кол-во добавленного товара
        quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        # задаем кол-во в поле ввода
        self.basketPage.clear_text_in_element_and_send_text_with_enter(
            first_book_input_field, BasketPage.QUANTITY_TO_ENTER)
        #новый запрос кол-ва
        new_quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        assert int(quantity_of_first_book) == 1
        assert int(new_quantity_of_first_book) == int(BasketPage.QUANTITY_TO_ENTER)

    # тест проверки уменьшения товара в "корзине" кнопкой "-"
    def test_that_quantity_can_decreased_by_pressing_decrease_button(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # ищем "В КОРЗИНУ"
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # ищем и добавляем товар "В КОРЗИНУ"
        self.list_of_buttons_move_into_basket[0].click()
        # закрыть всплывающее окно
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # жмем "Корзина" в заголовке
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # ищем поля ввода кол-ва
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
            BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
        # ищем поля ввода кол-ва последнего товара
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        # передаем кол-во в поле ввода
        self.basketPage.clear_text_in_element_and_send_text_with_enter(
            first_book_input_field, BasketPage.QUANTITY_TO_ENTER)
        # ищем кол-во добавленного товара
        quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        # ищем кнопку "-"
        self.list_of_increase_buttons = self.basketPage.find_several_element(BasketPage.DECREASE_QUANTITY_OF_ITEM)
        # уменьшаем кол-во на 1 кнопкой "-"
        self.list_of_increase_buttons[0].click()
        # запрашиваем новое кол-во
        new_quantity_of_first_book = first_book_input_field.get_attribute(TestData.ATTRIBUTE_VALUE)
        assert int(quantity_of_first_book) - int(new_quantity_of_first_book) == 1

    # тест цены: меняется с новым количестовм в корзине
    def test_that_sum_will_raise_accordingly_when_quantity_of_item_increased(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # ищем "В КОРЗИНУ"
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # ижем и добавляем товар "В КОРЗИНУ"
        self.list_of_buttons_move_into_basket[0].click()
        # закрыть всплываюшее окно
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # жмем "Корзина" в заголовке
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # ищем поля ввода товаров
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
            BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
        # ищем цены книг в корзине
        self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # ищем элемент с ценой первой книги в корзине
        price_of_first_book_string = self.list_of_book_prices_in_basket[0]
        # получаем цену первой книги
        first_book_price_in_basket = self.basketPage.price_by_int(price_of_first_book_string)
        # ищем поле ввода товара
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        # передаем кол-во пероый книги
        self.basketPage.clear_text_in_element_and_send_text_with_enter(
            first_book_input_field, BasketPage.QUANTITY_TO_ENTER)
        # обновление страницы
        time.sleep(5)
        # ищем цены в корзине
        self.list_of_book_prices_in_basket_new = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # fэлемент с ценой первой книгши
        price_of_first_item = self.list_of_book_prices_in_basket_new[0]
        # получаем цену первого товара с новым кол-вом
        new_price = self.basketPage.price_by_int(price_of_first_item)
        assert (first_book_price_in_basket * int(BasketPage.QUANTITY_TO_ENTER)) == new_price

    # тест итоговой цены в  "Подытог без учета доставки" всх товаров "В КОРЗИНУ" меняется с количеством
    def test_that_final_sum_will_raise_accordingly_when_quantity_of_item_increased(self):
        self.basketPage = BasketPage(self.driver)
        # self.basketPage.accept_cookies_policy()
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # ищем "В КОРЗИНУ"
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # добавляем 2 товара в корзину
        for book in self.list_of_buttons_move_into_basket[0:2]:
            book.click()
        # закрыть окно всплывающее
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # жмем "Корзина" в заголовке
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # ищем поля ввода товаров
        self.list_of_quantity_of_all_items_in_basket = self.basketPage.find_several_element(
            BasketPage.QUANTITY_OF_EACH_ITEM_IN_BASKET)
        # ищем тены товаров в корзине
        self.list_of_book_prices_in_basket = self.basketPage.find_several_element(BasketPage.BOOK_PRICE_STRING)
        # элемент с ценой первого товара
        price_of_first_book_string = self.list_of_book_prices_in_basket[0]
        # элемент с ценой второго товара
        price_of_second_book_string = self.list_of_book_prices_in_basket[1]
        # берем цену первого товара
        first_book_price_in_basket = self.basketPage.price_by_int(price_of_first_book_string)
        # берем цену второго товара
        second_book_price_in_basket = self.basketPage.price_by_int(price_of_second_book_string)
        # ищем поле ввода последнего добавленного товара
        first_book_input_field = self.list_of_quantity_of_all_items_in_basket[0]
        # передаем кол-во первому товару
        self.basketPage.clear_text_in_element_and_send_text_with_enter(
            first_book_input_field, BasketPage.QUANTITY_TO_ENTER)
        # обновление страницы
        time.sleep(7)
        # получаем финальную сумму товаров
        final_sum = self.basketPage.get_element_text(BasketPage.PURCHASE_FINAL_SUM).replace(' ', '')
        assert (first_book_price_in_basket * int(BasketPage.QUANTITY_TO_ENTER) + second_book_price_in_basket) == int(final_sum)

    # тест кнопки "Оформить"
    def test_that_start_checkout_button_open_checkout_page(self):
        self.basketPage = BasketPage(self.driver)
        self.basketPage.remove_all_good_in_basket_and_reload_page()
        # ищем "В КОРЗИНУ"
        self.list_of_buttons_move_into_basket = self.basketPage.find_several_element(BasketPage.MOVE_BOOK_TO_BASKET)
        # ищем и добавляем товар "В КОРЗИНУ"
        self.list_of_buttons_move_into_basket[0].click()
        # закрываем окно всплывающее
        self.basketPage.do_click(TestData.CLOSE_POPUP_ANY_ACTION)
        # жмем "Корзина" в заголовке
        self.basketPage.do_click(TestData.BASKET_BUTTON_AT_HEADER)
        # жмем "Начать оформление"
        self.basketPage.do_click(BasketPage.START_CHECKOUT)
        # "Оформить"
        self.basketPage.is_visible(BasketPage.CHECKOUT_AND_PAY)
        current_url = self.basketPage.get_current_url()
        assert current_url == BasketPage.BASKET_URL + "checkout/"
