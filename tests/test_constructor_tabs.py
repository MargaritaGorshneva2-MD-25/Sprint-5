import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestIngredientTabSwitch:
    def _wait_for_element(self, driver, locator):
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    @pytest.mark.parametrize("tab_name, locator, expected_section_locator, expected_active_class", [
        ("Булки", Locators.BUNS_TAB, Locators.BUNS_SECTION, "tab_active"),
        ("Соусы", Locators.SAUCES_TAB, Locators.SAUCES_SECTION, "tab_active"),
        ("Начинки", Locators.FILLINGS_TAB, Locators.FILLINGS_SECTION, "tab_active"),
    ])
    def test_ingredient_tab_switching(self, driver, tab_name, locator, expected_section_locator, expected_active_class):
        # 1. Находим и кликаем на вкладку
        tab_element = self._wait_for_element(driver, locator)
        tab_element.click()

        # 2. Ждем, пока секция станет видимой, и проверяем это
        section_element = self._wait_for_element(driver, expected_section_locator)
        assert section_element.is_displayed(), f"Секция '{tab_name}' не отображается"

        # 3. Проверяем, что вкладка стала активной
        assert expected_active_class in tab_element.get_attribute("class"), f"Вкладка '{tab_name}' не активна"


