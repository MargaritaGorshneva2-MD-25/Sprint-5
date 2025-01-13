import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from URL import BASE_URL
from locators import Locators
import random
import string

# Функция для генерации случайного email
def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase, k=10))
    domain = "yandex.ru"
    return f"{username}@{domain}"

def test_successful_registration(driver):
    driver.get(BASE_URL + "register")
    random_email = generate_random_email()

    name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.NAME_FIELD)
    )
    name_field.send_keys("Имя")

    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.EMAIL_FIELD)
    )
    email_field.send_keys(random_email)

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.PASSWORD_FIELD)
    )
    password_field.send_keys("Пароль123")

    register_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
    )
    current_url = driver.current_url # Запоминаем текущий URL
    register_button.click()

    # Ожидаем изменения URL, если регистрация успешна
    WebDriverWait(driver, 10).until(EC.url_changes(current_url))
    assert driver.current_url == BASE_URL + "login", "Регистрация не удалась"



def test_incorrect_password_registration(driver):
    driver.get(BASE_URL + "register")

    name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.NAME_FIELD)
    )
    name_field.send_keys("Имя")

    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.EMAIL_FIELD)
    )
    email_field.send_keys(generate_random_email())


    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(Locators.PASSWORD_FIELD)
    )
    password_field.send_keys("123") # Некорректный пароль

    register_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
    )
    current_url = driver.current_url # Запоминаем текущий URL
    register_button.click()

    # Проверяем, что URL не изменился после нажатия на кнопку регистрации
    WebDriverWait(driver, 10, ignored_exceptions=EC.url_changes).until_not(EC.url_to_be(current_url))
    assert driver.current_url == current_url, "Регистрация должна была завершиться ошибкой, но URL изменился"

