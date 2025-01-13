import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from URL import BASE_URL
from locators import Locators

def test_personal_area_from_main_page_login_button(driver):
    driver.get(BASE_URL)
    login_button_main = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.LOGIN_BUTTON_MAIN_PAGE)
    )
    login_button_main.click() # Кнопка "Войти в аккаунт"

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

    check_personal_area_page_opened(driver)



def test_personal_area_from_main_page_personal_area_button(driver):
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
    check_personal_area_page_opened(driver)


def check_personal_area_page_opened(driver):
    WebDriverWait(driver, 10).until(EC.url_contains(BASE_URL + "account")) # Проверяем часть URL
    # Здесь можно добавить дополнительные проверки элементов на странице, если необходимо
