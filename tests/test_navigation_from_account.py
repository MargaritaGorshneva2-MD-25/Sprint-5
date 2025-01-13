import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from URL import BASE_URL
from locators import Locators

def test_logo_click_redirects_to_constructor(driver):
    # Авторизация
    driver.get(BASE_URL + "login")
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


    WebDriverWait(driver, 10).until(EC.url_contains(BASE_URL + "account"))


    # Клик по логотипу
    logo = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.LOGO_IMAGE)
    )
    logo.click()

    # Проверка перехода на страницу Конструктор (главную страницу)
    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
    assert driver.current_url == BASE_URL, "Переход на страницу Конструктор не выполнен"