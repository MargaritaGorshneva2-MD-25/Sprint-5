import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window() # или другие настройки, если нужны
    yield driver
