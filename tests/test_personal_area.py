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



def test_personal_area_from_main_page_login_button(driver):
    driver.get(base_url)
    driver.find_element(By.XPATH, Locators.login_button_main_page).click() # Кнопка "Войти в аккаунт"
    driver.find_element(By.XPATH, Locators.email_field).send_keys("email@example.com")
    driver.find_element(By.XPATH, Locators.password_field).send_keys("Пароль123")
    driver.find_element(By.XPATH, Locators.login_button).click()

    check_personal_area_page_opened(driver)
    driver.quit()




def test_personal_area_from_main_page_personal_area_button(driver):
    driver.get(base_url)
    driver.find_element(By.XPATH, Locators.personal_area_button).click()
    driver.find_element(By.XPATH, Locators.email_field).send_keys("email@example.com")
    driver.find_element(By.XPATH, Locators.password_field).send_keys("Пароль123")
    driver.find_element(By.XPATH, Locators.login_button).click()
    check_personal_area_page_opened(driver)
    driver.quit()



def check_personal_area_page_opened(driver):
    try:
        WebDriverWait(driver, 5).until(EC.url_contains(base_url + "account")) # Проверяем часть URL, т.к. он может меняться
        # Дополнительные проверки элементов на странице, если необходимо
    except TimeoutException:
        pytest.fail("Страница 'Личный кабинет' не открылась")
