import pytest
from URL import BASE_URL
from locators import Locators
from helpest import click_and_check_url

class TestLoginRedirection:
    def test_login_button_main_page_redirection(self, driver):
        click_and_check_url(driver, Locators.LOGIN_BUTTON_MAIN_PAGE, BASE_URL + "login", BASE_URL)

    def test_personal_area_button_redirection(self, driver):
        click_and_check_url(driver, Locators.PERSONAL_AREA_BUTTON, BASE_URL + "login", BASE_URL)

    def test_login_link_from_registration_form_redirection(self, driver):
        click_and_check_url(driver, Locators.LOGIN_LINK_REGISTRATION_FORM, BASE_URL + "login", BASE_URL + "register")

    def test_forgot_password_link_redirection(self, driver):
        driver.get(BASE_URL + "login")
        click_and_check_url(driver, Locators.LOGIN_LINK_FORGOT_PASSWORD_FORM, BASE_URL + "forgot-password")

    def test_login_link_from_forgot_password_form_redirection(self, driver):
        click_and_check_url(driver, Locators.LOGIN_LINK_FORGOT_PASSWORD_FORM_2, BASE_URL + "login", BASE_URL + "forgot-password") #forgot-password -> login

