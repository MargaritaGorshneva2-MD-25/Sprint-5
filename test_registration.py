import pytest
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helptest import generate_random_email
from locators import Locators
from URL import REGIS_URL, LOGIN_URL
from config import TEST_PASSWORD

# Настройка логгера
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class TestRegistrationPage:
    def test_successful_registration(self, driver):
        random_email = generate_random_email()
        logger.info(f"Используемый email: {random_email}")

        driver.get(REGIS_URL)
        WebDriverWait(driver, 10).until(EC.url_to_be(REGIS_URL))

        driver.find_element(*Locators.NAME).send_keys("Тест")
        driver.find_element(*Locators.EMAIL).send_keys(random_email)
        driver.find_element(*Locators.PASSWORD).send_keys(TEST_PASSWORD)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON))
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Проверка: URL должен быть LOGIN_URL после успешной регистрации
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL

    def test_failed_registration_invalid_email(self, driver):
        driver.get(REGIS_URL)
        WebDriverWait(driver, 10).until(EC.url_to_be(REGIS_URL))

        driver.find_element(*Locators.NAME).send_keys("Тест")
        driver.find_element(*Locators.EMAIL).send_keys("invalid_email")
        driver.find_element(*Locators.PASSWORD).send_keys(TEST_PASSWORD)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON))
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Проверка: URL остается REGIS_URL
        assert driver.current_url == REGIS_URL

    def test_failed_registration_short_password(self, driver):
        driver.get(REGIS_URL)
        WebDriverWait(driver, 10).until(EC.url_to_be(REGIS_URL))

        driver.find_element(*Locators.NAME).send_keys("Тест")
        driver.find_element(*Locators.EMAIL).send_keys(generate_random_email())
        driver.find_element(*Locators.PASSWORD).send_keys("short")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON))
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Проверка: URL остается REGIS_URL
        assert driver.current_url == REGIS_URL
