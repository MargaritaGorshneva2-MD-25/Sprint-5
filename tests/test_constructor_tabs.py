import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


@pytest.mark.parametrize("tab_name, locator", [
    ("Булки", Locators.BUNS_TAB),
    ("Соусы", Locators.SAUCES_TAB),
    ("Начинки", Locators.FILLINGS_TAB),
])
def test_ingredient_tab_switch(driver, tab_name, locator):
    # Открываем страницу в фикстуре conftest.py

    # Ожидаем кликабельности вкладки
    tab_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(locator)
    )
    tab_element.click()

    # Ожидаем появления активного класса у соответствующей секции
    section_locator = Locators.get_section_locator(tab_name)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((section_locator[0], section_locator[1] + ".tab_selected")) # Проверяем наличие класса tab_selected (или аналогичного)
    )

    # Проверка, что секция стала активной (содержит класс "tab_selected" или аналогичный)
    active_section = driver.find_element(*section_locator)
    assert "tab_selected" in active_section.get_attribute("class"), f"Раздел '{tab_name}' не стал активным"
