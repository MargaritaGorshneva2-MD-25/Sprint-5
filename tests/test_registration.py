import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from URL import BASE_URL
from helpest import check_profile_page_opened, generate_random_email


class TestRegistration:
    def fill_registration_form(self, driver, name, email, password):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.NAME_FIELD)
        ).send_keys(name)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.EMAIL_FIELD)
        ).send_keys(email)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.PASSWORD_FIELD)
        ).send_keys(password)

    def test_successful_registration(self, driver):
        driver.get(BASE_URL + "register")
        random_email = generate_random_email()
        self.fill_registration_form(driver, "Имя", random_email, "Пароль123") # Используем новый метод

        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
        )
        current_url = driver.current_url
        register_button.click()

        WebDriverWait(driver, 10).until(EC.url_changes(current_url))
        assert driver.current_url == BASE_URL + "login", "Регистрация не удалась"

    def test_incorrect_password_registration(self, driver):
        driver.get(BASE_URL + "register")
        random_email = generate_random_email()
        self.fill_registration_form(driver, "Имя", random_email, "123") # Используем новый метод

        register_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
        )
        current_url = driver.current_url
        register_button.click()

        WebDriverWait(driver, 10, ignored_exceptions=EC.url_changes).until_not(EC.url_to_be(current_url))
        assert driver.current_url == current_url, "Регистрация должна была завершиться ошибкой, но URL изменился"