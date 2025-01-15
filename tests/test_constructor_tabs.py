import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestIngredientTabSwitch:
    @pytest.mark.parametrize("tab_name, locator", [
        ("Булки", Locators.BUNS_TAB),
        ("Соусы", Locators.SAUCES_TAB),
        ("Начинки", Locators.FILLINGS_TAB),
    ])
    def test_scroll_to_section(self, driver, tab_name, locator): # Изменено название метода

        tab_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(locator)
        )

        # Получаем координаты раздела ДО клика
        section_locator = Locators.get_section_locator(tab_name) # Возвращаем метод get_section_locator
        section_element = driver.find_element(*section_locator)
        initial_location = section_element.location["y"]

        tab_element.click()

        # Ожидаем, что координаты раздела изменятся после клика (произойдет скроллинг)
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element(*section_locator).location["y"] != initial_location
        )
