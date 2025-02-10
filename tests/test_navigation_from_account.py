import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from URL import BASE_URL
from locators import Locators
from helpers import wait_for_element


class TestStellarBurgersNavigation:  # Более descriptive название класса

    def test_logo_click_redirects_to_constructor(self, logged_in_user):
        logged_in_user.get(BASE_URL + "account")  # Переходим в личный кабинет после логина
        logo_image = wait_for_element(logged_in_user, Locators.LOGO_IMAGE)
        logo_image.click()
        WebDriverWait(logged_in_user, 10).until(EC.url_to_be(BASE_URL))
        assert logged_in_user.current_url == BASE_URL, "Переход на страницу Конструктор не выполнен"

    def test_constructor_link_redirects_to_constructor(self, logged_in_user):
        logged_in_user.get(BASE_URL + "account")  # Переходим в личный кабинет после логина
        constructor_link = wait_for_element(logged_in_user,
                                            Locators.CONSTRUCTOR_LINK)  # Предполагается наличие локатора для ссылки "Конструктор"
        constructor_link.click()
        WebDriverWait(logged_in_user, 10).until(EC.url_to_be(BASE_URL))
        assert logged_in_user.current_url == BASE_URL, "Переход на страницу Конструктор не выполнен"
