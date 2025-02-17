import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from URL import BASE_URL
from locators import Locators
from config import TEST_EMAIL, TEST_PASSWORD


class TestLogin:
    @pytest.mark.parametrize("locator, initial_url", [
        (Locators.LOGIN_ACCOUNT_BUTTON, BASE_URL),
        (Locators.PERSONAL_ACCOUNT_BUTTON, BASE_URL),
        (Locators.LINK_LOGIN, BASE_URL + "register"),
        (Locators.LINK_LOGIN, BASE_URL + "forgot-password"),
    ])
    def test_login_navigation(self, driver, locator, initial_url):
        driver.get(initial_url)
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "login"))
        assert driver.current_url == BASE_URL + "login"

    def test_login_with_valid_credentials(self, driver):
        driver.get(BASE_URL + "login")

        email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='email']")))
        email_input.send_keys(TEST_EMAIL)
        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']")))
        password_input.send_keys(TEST_PASSWORD)

        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти']")))
        login_button.click()

        WebDriverWait(driver, 10).until(EC.url_contains(BASE_URL + "account"))
        assert BASE_URL + "account/profile" in driver.current_url

