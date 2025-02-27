import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helptest import generate_random_email
from locators import Locators
from URL import REGIS_URL, LOGIN_URL
from config import TEST_PASSWORD


class TestRegistrationPage:
    def test_successful_registration(self, driver):
        random_email = generate_random_email()
        print(f"Используемый email: {random_email}") # Вывод email для отладки

        driver.get(REGIS_URL)
        WebDriverWait(driver, 10).until(EC.url_to_be(REGIS_URL))

        driver.find_element(*Locators.NAME).send_keys("Тест")
        driver.find_element(*Locators.EMAIL).send_keys(random_email)
        driver.find_element(*Locators.PASSWORD).send_keys(TEST_PASSWORD)

        print(driver.find_element(*Locators.REGISTER_BUTTON).get_attribute('outerHTML')) # HTML код кнопки

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON))
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))

    def test_failed_registration(self, driver):
        driver.get(REGIS_URL)
        WebDriverWait(driver, 10).until(EC.url_to_be(REGIS_URL))

        driver.find_element(*Locators.NAME).send_keys("Тест")
        driver.find_element(*Locators.EMAIL).send_keys("invalid_email")
        driver.find_element(*Locators.PASSWORD).send_keys("short")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON))
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Здесь нужно добавить проверку на сообщение об ошибке или другое поведение при неудачной регистрации
