import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from URL import BASE_URL, LOGIN_URL, REGIS_URL, PROFILE_URL, FORGOT_URL
from config import TEST_EMAIL, TEST_PASSWORD

class TestLoginPage:

    def login_with_credentials(self, driver):
        driver.find_element(*Locators.EMAIL).send_keys(TEST_EMAIL)
        driver.find_element(*Locators.PASSWORD).send_keys(TEST_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_FORM).click()

    def test_login_from_main_page(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_ACCOUNT_BUTTON))
        driver.find_element(*Locators.LOGIN_ACCOUNT_BUTTON).click()
        self.login_with_credentials(driver)
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))

    def test_login_from_personal_area_button(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        self.login_with_credentials(driver)
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))

    def test_login_from_registration_form(self, driver):
        driver.get(REGIS_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LINK_LOGIN))
        driver.find_element(*Locators.LINK_LOGIN).click()
        self.login_with_credentials(driver)
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))

    def test_login_from_password_recovery_form(self, driver):
        driver.get(FORGOT_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_FORM))
        driver.find_element(*Locators.LOGIN_BUTTON_FORM).click()
        self.login_with_credentials(driver)
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
