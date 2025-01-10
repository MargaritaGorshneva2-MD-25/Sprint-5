import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import Locators
import time

base_url = "https://stellarburgers.nomoreparties.site/"


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver


@pytest.mark.parametrize("tab_name, locator", [
    ("Булки", Locators.buns_tab),
    ("Соусы", Locators.sauces_tab),
    ("Начинки", Locators.fillings_tab),
])
def test_ingredient_tab_scroll(driver, tab_name, locator):
    driver.get(base_url)

    # Получаем начальное положение раздела до скролла (не обязательно, но может быть полезно для отладки)
    section_locator = Locators.get_section_locator(tab_name)
    initial_location = driver.find_element(By.XPATH, section_locator).location

    # Клик по вкладке ингредиента
    tab_element = driver.find_element(By.XPATH, locator)
    tab_element.click()
    time.sleep(1) # небольшая задержка, чтобы дать время для скролла. Возможно, потребуется adjust

    # Проверка, что раздел проскроллился
    # (текущее положение раздела отличается от начального)
    final_location = driver.find_element(By.XPATH, section_locator).location
    assert initial_location != final_location, f"Раздел '{tab_name}' не проскроллился"
