import pytest
from URL import BASE_URL
from locators import Locators
from helpest import click_and_check_url

class TestLoginRedirection:

    @pytest.mark.parametrize("locator, expected_url, initial_url", [
        (Locators.LOGIN_BUTTON_MAIN_PAGE, BASE_URL + "login", BASE_URL),
        (Locators.PERSONAL_AREA_BUTTON, BASE_URL + "login", BASE_URL),
        (Locators.LOGIN_LINK_REGISTRATION_FORM, BASE_URL + "login", BASE_URL + "register"),
        (Locators.LOGIN_LINK_FORGOT_PASSWORD_FORM_2, BASE_URL + "login", BASE_URL + "forgot-password"),
    ])
    def test_login_redirection(self, driver, locator, expected_url, initial_url):
        if initial_url:
            driver.get(initial_url)
        result = click_and_check_url(driver, locator, expected_url)
        assert result, f"Перенаправление с {initial_url or 'текущей страницы'} по локатору {locator} на {expected_url} некорректно"


    def test_forgot_password_link_redirection(self, driver):
        driver.get(BASE_URL + "login")
        result = click_and_check_url(driver, Locators.LOGIN_LINK_FORGOT_PASSWORD_FORM, BASE_URL + "forgot-password")
        assert result, "Перенаправление на страницу 'forgot-password' некорректно"
