import pytest
from selenium import webdriver


@pytest.fixture()  # объявляем, что функция является фикстурой
def browser():
    print("\nstart browser for test")
    browser = webdriver.Chrome()  # инициализируем браузер
    yield browser
    # код внутри функции под этой командой будет выполнятся по завершении каждого теста
    print("\nquit browser")
    browser.quit()  # закрываем браузер
