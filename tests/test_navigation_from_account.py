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

def test_logo_click_redirects_to_constructor(driver):
    # Авторизация (этот блок кода нужно добавить, чтобы попасть на страницу Личный Кабинет)
    driver.get(base_url + "login")
    driver.find_element(By.XPATH, Locators.email_field).send_keys("email@example.com")
    driver.find_element(By.XPATH, Locators.password_field).send_keys("Пароль123")
    driver.find_element(By.XPATH, Locators.login_button).click()
    # Ждем, пока загрузится страница Личного Кабинета
    WebDriverWait(driver, 5).until(EC.url_contains(base_url + "account/profile"))

    # Клик по логотипу
    driver.find_element(By.XPATH, Locators.logo_image).click()

    # Проверка перехода на страницу Конструктор
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(base_url)) # Ожидаем точный URL главной страницы
    except TimeoutException:
        pytest.fail("Переход на страницу Конструктор не выполнен")
