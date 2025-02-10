import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from URL import BASE_URL
from locators import Locators
from helpers import wait_for_element, click_and_check_url

# Тесты перенаправления НА страницу логина (до авторизации)
class TestLoginRedirection:
    @pytest.mark.parametrize("locator, initial_url", [
        (Locators.LOGIN_BUTTON_MAIN_PAGE, BASE_URL),
        (Locators.PERSONAL_AREA_BUTTON, BASE_URL),
        (Locators.LOGIN_LINK_REGISTRATION_FORM, BASE_URL + "register"),
        (Locators.LOGIN_LINK_FORGOT_PASSWORD_FORM_2, BASE_URL + "forgot-password"),
    ])
    def test_login_redirection(self, driver, locator, initial_url):
        driver.get(initial_url)
        click_and_check_url(driver, locator, BASE_URL + "login")


    def test_forgot_password_link_redirection(self, driver):
        driver.get(BASE_URL + "login")
        click_and_check_url(driver, Locators.LOGIN_LINK_FORGOT_PASSWORD_FORM, BASE_URL + "forgot-password")

# Тест перенаправления ПОСЛЕ клика на логотип (после авторизации)
class TestLogoRedirect:
    def test_logo_click_redirects_to_constructor(self, logged_in_user):
        logged_in_user.get(BASE_URL + "account") # Начальная страница - личный кабинет
        wait_for_element(logged_in_user, Locators.LOGO_IMAGE).click()
        WebDriverWait(logged_in_user, 10).until(EC.url_to_be(BASE_URL))
        assert logged_in_user.current_url == BASE_URL, "Переход на страницу Конструктор не выполнен"


