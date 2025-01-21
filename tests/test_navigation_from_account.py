import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from URL import BASE_URL
from locators import Locators
from config import TEST_EMAIL, TEST_PASSWORD

class TestLogoRedirect:

    def _wait_for_element(self, driver, locator, timeout=10):
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def _login(self, driver): # email и password больше не нужны в параметрах
        driver.get(BASE_URL + "login")
        self._wait_for_element(driver, Locators.EMAIL_FIELD).send_keys(TEST_EMAIL) # Используем TEST_EMAIL из config.py
        self._wait_for_element(driver, Locators.PASSWORD_FIELD).send_keys(TEST_PASSWORD) # Используем TEST_PASSWORD из config.py
        self._wait_for_element(driver, Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_contains(BASE_URL + "account"))

    def test_logo_click_redirects_to_constructor(self, driver):
        self._login(driver) # email и password больше не передаются в _login

        logo_image = self._wait_for_element(driver, Locators.LOGO_IMAGE)
        logo_image.click()

        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL, "Переход на страницу Конструктор не выполнен"

