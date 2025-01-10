import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import Locators # Импорт локаторов


base_url = "https://stellarburgers.nomoreparties.site/"


def test_login_from_main_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get(base_url)
        driver.find_element(By.XPATH, Locators.login_button_main_page).click()
        check_login_page_opened(driver) # Вызов вспомогательной функции
    finally:
        driver.quit()


def test_login_from_personal_area_button():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get(base_url)
        driver.find_element(By.XPATH, Locators.personal_area_button).click()
        check_login_page_opened(driver)
    finally:
        driver.quit()


def test_login_from_registration_form():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get(base_url + "register")
        driver.find_element(By.XPATH, Locators.login_button_registration_form).click()
        check_login_page_opened(driver)
    finally:
        driver.quit()


def test_login_from_forgot_password_form():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get(base_url + "forgot-password")
        driver.find_element(By.XPATH, Locators.login_button_forgot_password_form).click()
        check_login_page_opened(driver)
    finally:
        driver.quit()



def check_login_page_opened(driver): # Вспомогательная функция
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(base_url + "login"))
    except TimeoutException:
        pytest.fail("Страница входа не открылась")
