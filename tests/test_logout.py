import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from URL import LOGIN_URL, PROFILE_URL
from helptest import login


def test_logout(driver):
    """Проверяет выход из аккаунта."""
    login(driver)

    personal_account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)
    )
    personal_account_button.click()
    WebDriverWait(driver, 10).until(EC.url_to_be(PROFILE_URL))

    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)
    )
    logout_button.click()

    WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
