import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from URL import BASE_URL
from locators import Locators
from helpest import wait_for_element


class TestLogout:
    def test_logout(self, logged_in_driver):
        # Нажимаем кнопку "Личный кабинет"
        personal_account_button = wait_for_element(logged_in_driver, Locators.PERSONAL_ACCOUNT_BUTTON)
        personal_account_button.click()

        # Ждем появления кнопки "Выход" и кликаем
        logout_button = wait_for_element(logged_in_driver, Locators.LOGOUT_BUTTON)
        logout_button.click()

        # Проверяем, что URL стал BASE_URL после выхода
        WebDriverWait(logged_in_driver, 10).until(EC.url_to_be(BASE_URL+"login"))
