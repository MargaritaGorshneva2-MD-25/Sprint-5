import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from URL import LOGIN_URL
from config import TEST_EMAIL, TEST_PASSWORD

@pytest.fixture
def driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless") # раскомментируйте для headless режима

    current_directory = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(current_directory, "chromedriver.exe")

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def authorized_driver(driver):
    """Фикстура для авторизованного пользователя."""
    driver.get(LOGIN_URL)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located(Locators.EMAIL))
    driver.find_element(*Locators.EMAIL).send_keys(TEST_EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(TEST_PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON_FORM).click()
    WebDriverWait(driver, 20).until(EC.url_changes(LOGIN_URL))
    return driver # Возвращаем драйвер после авторизации
