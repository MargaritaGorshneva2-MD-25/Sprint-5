import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from URL import BASE_URL
from locators import Locators

class TestLogoRedirect: # Создаем тестовый класс

    def _login(self, driver, email, password): # protected метод для авторизации
        driver.get(BASE_URL + "login")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.EMAIL_FIELD)
        ).send_keys(email)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.PASSWORD_FIELD)
        ).send_keys(password)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN_BUTTON)
        ).click()

        WebDriverWait(driver, 10).until(EC.url_contains(BASE_URL + "account"))


    def test_logo_click_redirects_to_constructor(self, driver):
        self._login(driver, "margarita_gorshnyova_13444@yandex.ru", "ваш_пароль") # Используем _login

        # Клик по логотипу
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGO_IMAGE)
        ).click()

        # Проверка перехода на страницу Конструктор (главную страницу)
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL, "Переход на страницу Конструктор не выполнен"


