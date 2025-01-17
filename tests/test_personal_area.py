import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from URL import BASE_URL
from config import TEST_EMAIL, TEST_PASSWORD
from helpest import check_profile_page_opened # Импортируем функцию


class TestPersonalArea:
    def login(self, driver, email, password):
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.EMAIL_FIELD)
        )
        email_field.send_keys(email)

        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.PASSWORD_FIELD)
        )
        password_field.send_keys(password)

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
        )
        login_button.click()

        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "account"))

    def test_personal_area_from_main_page_login_button(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN_PAGE)
        ).click()
        self.login(driver, TEST_EMAIL, TEST_PASSWORD)
        profile_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((Locators.PROFILE_LINK))
        )
        profile_link.click()
        check_profile_page_opened(driver) # Вызываем функцию проверки


    def test_personal_area_from_main_page_personal_area_button(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PERSONAL_AREA_BUTTON)
        ).click()
        self.login(driver, TEST_EMAIL, TEST_PASSWORD)
        profile_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((Locators.PROFILE_LINK))
        )
        profile_link.click()
        check_profile_page_opened(driver) # Вызываем функцию проверки
