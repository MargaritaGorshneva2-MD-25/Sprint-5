import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from URL import BASE_URL
from locators import Locators

def test_logout(driver):
    # Переход на страницу логина
    driver.get(BASE_URL + "login")

    # Ввод email
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.EMAIL_FIELD)
    )
    email_field.send_keys("маргарита_горшнёва_13444@yandex.ru")

    # Ввод пароля
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.PASSWORD_FIELD)
    )

    password_field.send_keys("Пароль123")

    # Клик по кнопке "Войти"
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.LOGIN_BUTTON)
    )
    login_button.click()

    # Ожидание загрузки страницы личного кабинета (проверка по URL)
    WebDriverWait(driver, 10).until(EC.url_contains(BASE_URL + "account/profile"))

    # Клик по кнопке "Выйти"
    logout_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.LOGOUT_BUTTON)
    )

    logout_button.click()
    # Ожидание появления кнопки "Войти в аккаунт" после выхода
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.LOGIN_BUTTON_MAIN_PAGE)
    )

    # Проверка наличия кнопки "Войти в аккаунт" после выхода
    assert driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).is_displayed(), "Кнопка 'Войти в аккаунт' не отображается после выхода"

