import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import Locators

base_url = "https://stellarburgers.nomoreparties.site/"


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver

def test_logout(driver):
    # Авторизация
    driver.get(base_url + "login")
    driver.find_element(By.XPATH, Locators.email_field).send_keys("email@example.com")
    driver.find_element(By.XPATH, Locators.password_field).send_keys("Пароль123")
    driver.find_element(By.XPATH, Locators.login_button).click()
    # Ждем, пока загрузится страница Личного Кабинета
    WebDriverWait(driver, 5).until(EC.url_contains(base_url + "account/profile"))

    # Клик по кнопке "Выйти"
    driver.find_element(By.XPATH, Locators.logout_button).click()

    # Проверка, что пользователь перенаправлен на страницу входа/регистрации или что кнопка "Войти в аккаунт" появилась.
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, Locators.login_button_main_page))) # Проверяем наличие кнопки "Войти в аккаунт"
        # Или, если перенаправление на другую страницу:
        # WebDriverWait(driver, 5).until(EC.url_to_be(base_url + "login")) # Если перенаправляет на страницу логина
    except TimeoutException:
        pytest.fail("Выход из аккаунта не выполнен.")
