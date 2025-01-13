import pytest
from selenium import webdriver
from URL import BASE_URL

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL) # Открываем главную страницу в фикстуре driver
    yield driver
    driver.quit()
