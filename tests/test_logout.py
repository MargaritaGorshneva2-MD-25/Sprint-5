import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from URL import BASE_URL
from locators import Locators


class TestLogout:
    def _login(self, driver, email, password):
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

        WebDriverWait(driver, 10).until(EC.url_contains(BASE_URL + "account/profile"))


    def test_logout(self, driver):
        self._login(driver, "margarita_gorshnyova_13444@yandex.ru", "ваш_пароль") # Логин

        # Клик по кнопке "Выйти"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.LOGOUT_BUTTON)
        ).click()

        # Ожидание появления кнопки "Войти в аккаунт" после выхода
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.LOGIN_BUTTON_MAIN_PAGE)
        )

        # Проверка наличия кнопки "Войти в аккаунт" после выхода
        assert driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).is_displayed(), "Кнопка 'Войти в аккаунт' не отображается после выхода"

