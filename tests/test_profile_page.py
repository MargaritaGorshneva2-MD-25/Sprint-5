import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from URL import BASE_URL, LOGIN_URL


def test_personal_account_button_redirect_unauthenticated(driver):
    driver.get(BASE_URL)

    # Явное ожидание кнопки "Личный кабинет"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON))

    # Клик по кнопке "Личный кабинет"
    driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

    # Явное ожидание перехода на страницу входа
    WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))

    # Проверка: URL должен быть LOGIN_URL после перенаправления
    assert driver.current_url == LOGIN_URL
