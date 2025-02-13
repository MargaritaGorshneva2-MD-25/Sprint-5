import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from URL import BASE_URL
from config import TEST_EMAIL, TEST_PASSWORD
from helpest import wait_for_element

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def logged_in_user(driver):
    driver.get(BASE_URL + "login")
    wait_for_element(driver, Locators.EMAIL_FIELD).send_keys(TEST_EMAIL)
    wait_for_element(driver, Locators.PASSWORD_FIELD).send_keys(TEST_PASSWORD)
    wait_for_element(driver, Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_contains(BASE_URL + "account"))
    return driver
