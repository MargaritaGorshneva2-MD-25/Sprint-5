import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from URL import BASE_URL
from config import TEST_EMAIL, TEST_PASSWORD
from helpers import check_profile_page_opened # Исправлено название файла

class TestPersonalArea:
    def _wait_for_element(self, driver, locator, timeout=10):
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

    def _login(self, driver): # Используем данные из config.py напрямую
        driver.get(BASE_URL + "login")
        self._wait_for_element(driver, Locators.EMAIL_FIELD).send_keys(TEST_EMAIL)
        self._wait_for_element(driver, Locators.PASSWORD_FIELD).send_keys(TEST_PASSWORD)
        self._wait_for_element(driver, Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_contains(BASE_URL + "account"))

    def test_personal_area_from_main_page_login_button(self, driver):
        driver.get(BASE_URL)
        self._wait_for_element(driver, Locators.LOGIN_BUTTON_MAIN_PAGE).click()
        self._login(driver) # вызов метода логина
        self._wait_for_element(driver, Locators.PROFILE_LINK).click()
        assert check_profile_page_opened(driver) is True, "Страница профиля не открылась" # Добавлено assert

    def test_personal_area_from_main_page_personal_area_button(self, driver):
        driver.get(BASE_URL)
        self._wait_for_element(driver, Locators.PERSONAL_AREA_BUTTON).click()
        self._login(driver) # вызов метода логина
        self._wait_for_element(driver, Locators.PROFILE_LINK).click()
        assert check_profile_page_opened(driver) is True, "Страница профиля не открылась" # Добавлено assert
