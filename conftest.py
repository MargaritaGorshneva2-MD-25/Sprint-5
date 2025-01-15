import pytest
from selenium import webdriver
from URL import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

# Проверка перехода на страницу профиля
def check_profile_page_opened(driver):
    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "account/profile"))
    assert driver.find_element(*Locators.LOGOUT_BUTTON).is_displayed(), "Страница профиля не открылась."
