import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from URL import BASE_URL
from helpest import generate_random_email
from config import TEST_EMAIL, TEST_PASSWORD  # Импорт данных из config.py


class TestRegistration:

    def _wait_for_element(self, driver, locator, timeout=10):
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

    def _fill_registration_form(self, driver, name, email, password):
        self._wait_for_element(driver, Locators.NAME_FIELD).send_keys(name)
        self._wait_for_element(driver, Locators.EMAIL_FIELD).send_keys(email)
        self._wait_for_element(driver, Locators.PASSWORD_FIELD).send_keys(password)

    def test_successful_registration(self, driver):
        driver.get(BASE_URL + "register")
        self._fill_registration_form(driver, "Имя", TEST_EMAIL, TEST_PASSWORD)  # Используем TEST_PASSWORD

        current_url = driver.current_url
        self._wait_for_element(driver, Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_changes(current_url))
        assert driver.current_url == BASE_URL + "login", "Регистрация не удалась"

    def test_incorrect_password_registration(self, driver):
        driver.get(BASE_URL + "register")
        random_email = generate_random_email()
        self._fill_registration_form(driver, "Имя", random_email, "123")  # Короткий пароль для негативного теста

        current_url = driver.current_url
        self._wait_for_element(driver, Locators.REGISTER_BUTTON).click()

        try:
            WebDriverWait(driver, 10).until(EC.url_changes(current_url))
            pytest.fail("Регистрация должна была завершиться ошибкой, но URL изменился")
        except:  # pytest.fail.Exception:
            assert driver.current_url == current_url, "URL неожиданно изменился"

