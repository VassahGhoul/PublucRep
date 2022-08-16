# module_28

Этот репозиторий — является итоговым проектом курса QA Python на платформе Skillfactory. 
Репозиторий был создан с использованием шаблона PageObject с Selenium и PyTest (Python). 
Проект содержит UI тесты интернет-магазина "Лабиринт" "https://www.labirint.ru/.

Подготовка к запуску:

скопируйте репозиторий на свой компьютер,

если вы используете PyCharm, он автоматически запрашивает установку необходимых библиотек,

если нет - установите требуемые библиотеки в файле requirements.txt.

Измените следующие данные:

в Config/config.py измените путь на (актуальный для вашей ОС и версии вашего браузера) chromedriver и/или geckodriver:

для macOS:
CHROME_EXECUTABLE_PATH = "/путь/chromedriver"
FIREFOX_EXECUTABLE_PATH = "/путь/geckodriver"

для Windows:
CHROME_EXECUTABLE_PATH = "C:\путь\chromedriver.exe"
FIREFOX_EXECUTABLE_PATH = "C:\путь\geckodriver.exe"

в Tests/conftest.py: если вы хотите начать тестирование браузеров Firefox и Chrome, оставьте (params=["chrome", "firefox"]), 
если вы хотите начать тестирование одного браузера за другим измените (params=["chrome "]) или (params=["firefox"]).

Чтобы НАЧАТЬ тест: 

для запуска всех тестов команда:

для Windows: pytest/Tests

для запуска одного набора тестов: 

pytest Tests/test_File_Name.py 

для запуска одного теста: 

pytest Tests/test_File_Name.py::TestClassName::test_name 
