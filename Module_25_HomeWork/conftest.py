
import pytest
from selenium import webdriver



@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('G:\Anaconda\Driverss\chromedriver.exe')
   pytest.driver.implicitly_wait(10)
   # страница авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   # размер окна
   pytest.driver.set_window_size(1400, 1000)
   # авторизируемси
   pytest.driver.find_element_by_id('email').send_keys('aaa@bbb.ccc')
   pytest.driver.find_element_by_id('pass').send_keys('12345678')
   # кнопка входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

   yield

   pytest.driver.quit()