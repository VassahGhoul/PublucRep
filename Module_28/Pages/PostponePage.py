from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class PostponePage(BasePage):

    URL = TestData.BASE_URL

    # локатор "Лабиринт" логотип, с помощью которого мы можем вернуться на домашнюю страницу
    LABIRINT_MAIN_LOGO = (By.XPATH, '//a[@title="Лабиринт - самый большой книжный интернет магазин"]')

    # локатор кнопки "Отложено"
    POSTPONED_BOOKS_BUTTON = (By.XPATH, '//a[@class="b-header-b-personal-e-link top-link-main top-link-main_putorder"]')
    # локатор кнопки "Отложить" по книгой на главной странице
    HEART_SYMBOL_AT_HOME_PAGE = (By.XPATH, '//a[@data-tooltip_title="Отложить"]')
    # локатор выпадающего окна "Отложить"
    POPUP_BOOK_POSTPONED = (By.XPATH, '//div[contains(text(), "Вы добавили  в отложенные книгу ")]')
    # локаторкнопки закрыть выпадающего окна "Отложить"
    CLOSE_POPUP_BOOK_POSTPONED = (By.XPATH, '//a[@class="b-basket-popinfo-close"]')
    # локатро количества книг в "Отложенно"
    QUANTITY_OF_POSTPONED_BOOKS = (By.XPATH, '//span[@class="b-header-b-personal-e-icon-count-m-putorder '
                                             'basket-in-dreambox-a"]')
    # локатор удаления отложенной книги
    DELETE_POSTPONED_BOOK = (By.XPATH, '//span[@class="b-list-item-hover pointer"]')
    # локатор "Что почитать" на главной странице
    BOOKS_DESCRIPTION_COVER = (By.XPATH, '//a[@class="cover"]')
    # локатор "Все отложенные товары" в сплывющем оке "Отложено"
    BUTTON_IN_POSTPONE_ICON_POPUP = (By.XPATH, '//a[@class="btn btn-middle btn-clear font_size_s all-putorder-btn-js"]')

    # локатор списка "labirint.ru/cabinet/putorder/"
    BOOK_IN_POSTPONE_PAGE = (By.XPATH, '//span[@class="product-title"]')

    # локатор кнопки "Очистить" в Отложенных
    CLEAR_POSTPONE_BUTTON = (By.XPATH, '//a[@title="Удалить все отложенные товары"]')
    # локатор сообщения "Сообщение Выбранные товары удалены!"
    POSTPONED_BOOKS_DELETED_MESSAGE = (By.XPATH, '//p[contains(text(),"Выбранные товары удалены!")]')

    # локатор кнопки "Выделить все"
    SELECT_ALL_POSTPONED_BOOKS = (By.XPATH, '//a[@title="Выделить все "]')
    # локатор чек-бокса выделения
    CHECKBOX_POSTPONED_BOOKS = (By.XPATH, '//label[@class="checkbox-ui checkbox-ui-m-bg checkbox-ui-m-multi '
                                          'checkbox-ui-m-big"]')
    # локатор "Удалить" после выдеоения книги
    DELETE_SELECTED_BOOKS = (By.XPATH, '//a[contains(text(),"Удалить")]')
    # аннотация книги
    ALL_SELECTED_BOOKS = (By.XPATH, '//div[@class="product-cover short-title"]')
    # локатор кнопки "В КОРЗИНУ" под книгой
    MOVE_IN_BASKET_FM_POSTPONE_BUTTON = (By.XPATH, '//a[@class="btn buy-link btn-primary" and contains(text(), '
                                                   '"В КОРЗИНУ")]')
    # локатор "ОФОРМИТЬ" по книгой, после добавления в корзину
    SWITCH_TO_CHECKOUT_BOOK_IN_BASKET_FM_POSTPONE_PAGE = (By.XPATH, '//a[@class="btn buy-link btn-more" and contains('
                                                                    'text(), "ОФОРМИТЬ")]')
    # локатор закрывает окно о сообнении что книга отложена
    CLOSE_POPUP_POSTPONED_BOOK_MOVED_IN_BASKET = (By.XPATH, '//a[@class="b-basket-popinfo-close"]')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)


    """получаем заголовок страницы"""
    def get_home_page_title(self, title):
        return self.get_title(title)

    """удаляем отложенное и возвращаемся на главную страницу """
    def clear_postpone_reload_page(self):
        self.do_click(PostponePage.POSTPONED_BOOKS_BUTTON)
        if self.is_visible(PostponePage.CLEAR_POSTPONE_BUTTON):
            self.do_click(PostponePage.CLEAR_POSTPONE_BUTTON)
            alert = self.driver.switch_to.alert
            alert.accept()
        self.do_click(PostponePage.LABIRINT_MAIN_LOGO)