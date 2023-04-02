import pytest
from settings import email, password, base_url
from selenium.webdriver.common.by import By
from selenium import webdriver


# Инициализация браузера и его закрытие по окончанию тестов
@pytest.fixture()
def browser():
    print("\nstart browser for test")
    driver = webdriver.Chrome()  # инициализируем браузер
    yield driver
    print("\nquit browser")
    driver.quit()  # закрываем браузер


@pytest.fixture(autouse=True)
def login(browser):
    browser.implicitly_wait(10)  # неявное ожидание
    browser.get(base_url)
    # нажимаем на кнопку регистрации
    btn_new_user = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-success")
    btn_new_user.click()

    # нажимаем на кнопку "у меня уже есть аккаунт"
    btn_exist_acc = browser.find_element(By.CSS_SELECTOR, "a[href='/login']")
    btn_exist_acc.click()

    # вводим email
    field_email = browser.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys(email)

    # вводим пароль
    field_pass = browser.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys(password)

    # нажимаем на кнопку "войти"
    btn_submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    btn_submit.click()

    result = browser.find_element(By.CSS_SELECTOR, 'h1').text

    return result
