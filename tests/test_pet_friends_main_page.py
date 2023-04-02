from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# проверка удачной авторизации
def test_petfriends_login(browser):
    result = browser.find_element(By.CSS_SELECTOR, 'h1').text
    assert result == "PetFriends", "login error"


# проверка элементов карточек питомцев (фото, имя, описание)
def test_petfriends_pets_cards(browser):
    images = browser.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = browser.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = browser.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != '', 'Image not found'
        assert names[i].text != '', 'Name not found'
        assert descriptions[i].text != '', 'Description not found'
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0, 'Species not found'
        assert len(parts[1]) > 0, 'Age not found'


# Проверка элементов страницы
def test_petfriends_card_deck(browser):
    # наличие навигационной панели
    WebDriverWait(browser, 10).until(  # явное ожидание
        EC.presence_of_element_located((By.ID, 'navbarNav')))
    # наличие кнопки "PetFriends"
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.navbar-brand.header2')))
    # наличие кнопки "Мои питомцы"
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/my_pets"]')))
    # наличие кнопки "Все питомцы"
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/all_pets"]')))
    # наличие кнопки "Выйти"
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.btn.btn-outline-secondary')))
    # наличие центральной надписи "PetFriends"
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.text-center')))
    # наличие центральной надписи "Все питомцы наших пользователей"
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.text-center:nth-child(2)')))
    # наличие таблицы с питомцами
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.card-deck')))
