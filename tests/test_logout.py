import pytest
from selenium.webdriver.support.ui import WebDriverWait # WebDriverWait нужен для EC.url_contains
from selenium.webdriver.support import expected_conditions as EC
from URL import BASE_URL
from locators import Locators
from config import TEST_EMAIL, TEST_PASSWORD
from helpest import wait_for_element


class TestLogout:
    def _login(self, driver, email, password):
        driver.get(BASE_URL + "login")
        wait_for_element(driver, Locators.EMAIL_FIELD).send_keys(email)
        wait_for_element(driver, Locators.PASSWORD_FIELD).send_keys(password)
        wait_for_element(driver, Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_contains("account/profile"))

    def test_logout(self, driver):
        self._login(driver, TEST_EMAIL, TEST_PASSWORD)

        logout_button = wait_for_element(driver, Locators.LOGOUT_BUTTON)
        logout_button.click()

        login_button = wait_for_element(driver, Locators.LOGIN_BUTTON_MAIN_PAGE)
        assert login_button.is_displayed(), "Кнопка 'Войти в аккаунт' не отображается после выхода"
