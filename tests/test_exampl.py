import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from locators import Locators
from URL import BASE_URL, PROFILE_URL
from helptest import login


def test_constructor_button_click(driver):
    """Проверяет переход в конструктор по кнопке."""
    login(driver)

    personal_account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
    )
    personal_account_button.click()
    WebDriverWait(driver, 10).until(EC.url_to_be(PROFILE_URL))

    constructor_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.CONSTRUCTOR)
    )
    constructor_button.click()
    time.sleep(2)  # Пауза в 2 секунды
    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))


def test_logo_click(driver):
    """Проверяет переход в конструктор по логотипу."""
    login(driver)

    personal_account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
    )
    personal_account_button.click()
    WebDriverWait(driver, 10).until(EC.url_to_be(PROFILE_URL))

    logo = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.LOGO)
    )
    logo.click()
    time.sleep(2)  # Пауза в 2 секунды
    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
