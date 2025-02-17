import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from locators import Locators
from URL import BASE_URL
from config import TEST_EMAIL, TEST_PASSWORD
from helpest import wait_for_element


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    if os.name == 'nt':
        chromedriver_path = os.path.join(os.path.dirname(__file__), "chromedriver.exe")
    else:
        chromedriver_path = os.path.join(os.path.dirname(__file__), "chromedriver")

    if not os.path.exists(chromedriver_path):
        raise FileNotFoundError(f"chromedriver не найден по пути: {chromedriver_path}")

    service = Service(executable_path=chromedriver_path)
    driver_ = webdriver.Chrome(service=service, options=chrome_options)
    driver_.maximize_window()
    yield driver_
    driver_.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    driver.get(BASE_URL + "login")

    email_field = wait_for_element(driver, Locators.EMAIL)
    email_field.send_keys(TEST_EMAIL)

    password_field = wait_for_element(driver, Locators.PASSWORD)
    password_field.send_keys(TEST_PASSWORD)

    login_button = wait_for_element(driver, Locators.LOGIN_BUTTON_FORM)
    login_button.click()

    WebDriverWait(driver, 10).until(EC.url_contains(BASE_URL))
    return driver



