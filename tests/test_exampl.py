import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from URL import BASE_URL, PROFILE_URL

def test_constructor_button_click(authorized_driver):
    """Проверяет переход из личного кабинета в конструктор по кнопке."""

    # Переходим в личный кабинет
    personal_account_button = WebDriverWait(authorized_driver, 20).until(
        EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
    )
    personal_account_button.click()
    WebDriverWait(authorized_driver, 20).until(EC.url_to_be(PROFILE_URL))


    constructor_button = WebDriverWait(authorized_driver, 20).until(
        EC.element_to_be_clickable(Locators.CONSTRUCTOR)
    )
    constructor_button.click()
    WebDriverWait(authorized_driver, 20).until(EC.url_to_be(BASE_URL))
    assert authorized_driver.current_url == BASE_URL

def test_logo_click(authorized_driver):
    """Проверяет переход из личного кабинета в конструктор по логотипу."""
    # Переходим в личный кабинет
    personal_account_button = WebDriverWait(authorized_driver, 20).until(
        EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
    )
    personal_account_button.click()
    WebDriverWait(authorized_driver, 20).until(EC.url_to_be(PROFILE_URL))

    logo = WebDriverWait(authorized_driver, 20).until(
        EC.element_to_be_clickable(Locators.LOGO)
    )
    logo.click()
    WebDriverWait(authorized_driver, 20).until(EC.url_to_be(BASE_URL))
    assert authorized_driver.current_url == BASE_URL
