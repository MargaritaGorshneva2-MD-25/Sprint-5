import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from URL import BASE_URL
from helpest import generate_random_email, generate_random_string
from config import TEST_PASSWORD # Импорт данных из config.py


class TestRegistration:
    def test_successful_registration(self, driver):
        driver.get(BASE_URL + "register")
        random_email = generate_random_email() # Генерация уникального email
        name = generate_random_string(10) # генерация имени
        self._fill_registration_form(driver, name, random_email, TEST_PASSWORD)

        current_url = driver.current_url
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_changes(current_url))
        assert driver.current_url == BASE_URL + "login", "Регистрация не удалась"

    def test_incorrect_password_registration(self, driver):
        driver.get(BASE_URL + "register")
        random_email = generate_random_email()
        name = generate_random_string(10) # генерация имени
        short_password = "123"
        self._fill_registration_form(driver, name, random_email, short_password)

        current_url = driver.current_url
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.url_to_be(current_url)) # Ожидаем, что URL *не* изменится
        assert driver.current_url == current_url, "Регистрация прошла успешно с коротким паролем, хотя не должна была"

    def _fill_registration_form(self, driver, name, email, password):
         driver.find_element(*Locators.NAME_FIELD).send_keys(name)
         driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
         driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)

