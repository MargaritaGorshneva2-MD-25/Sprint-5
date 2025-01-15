import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import check_profile_page_opened
from URL import BASE_URL


class TestPersonalArea:
    def test_personal_area_from_main_page_login_button(self, driver):
        driver.get(BASE_URL)
        login_button_main = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN_PAGE)
        )
        login_button_main.click()

        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.EMAIL_FIELD)
        )
        email_field.send_keys("margarita_gorshnyova_13444@yandex.ru")

        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.PASSWORD_FIELD)
        )
        password_field.send_keys("ваш_пароль") # замените на ваш пароль

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
        )
        login_button.click()

        # Проверка, что мы на странице аккаунта, а не профиля
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "account"))

        profile_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((Locators.PROFILE_LINK))
        )
        profile_link.click()

        check_profile_page_opened(driver)

    def test_personal_area_from_main_page_personal_area_button(self, driver):
        driver.get(BASE_URL)
        personal_area_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PERSONAL_AREA_BUTTON)
        )
        personal_area_button.click()

        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.EMAIL_FIELD)
        )
        email_field.send_keys("margarita_gorshnyova_13444@yandex.ru")

        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.PASSWORD_FIELD)
        )
        password_field.send_keys("ваш_пароль") # замените на ваш пароль

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
        )
        login_button.click()

        # Проверка, что мы на странице аккаунта, а не профиля
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "account"))

        profile_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((Locators.PROFILE_LINK))
        )
        profile_link.click()

        check_profile_page_opened(driver)
