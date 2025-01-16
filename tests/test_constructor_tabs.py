import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestIngredientTabSwitch:
    def _wait_for_element(self, driver, locator):
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    @pytest.mark.parametrize("tab_name, locator, expected_section_locator", [
        ("Булки", Locators.BUNS_TAB, Locators.BUNS_SECTION), # Добавили локаторы для секций
        ("Соусы", Locators.SAUCES_TAB, Locators.SAUCES_SECTION),
        ("Начинки", Locators.FILLINGS_TAB, Locators.FILLINGS_SECTION),
    ])
    def test_ingredient_tab_switching(self, driver, tab_name, locator, expected_section_locator):
        tab_element = self._wait_for_element(driver, locator) # Использование вспомогательного метода
        tab_element.click()

        # Ожидание и проверка, что секция стала видимой
        section_element = self._wait_for_element(driver, expected_section_locator)
        assert section_element.is_displayed(), f"Секция {tab_name} не отображается"


        # Проверка, что вкладка активна (замените 'tab_active' на реальный класс/атрибут)
        assert "tab_active" in tab_element.get_attribute("class"), f"Вкладка {tab_name} не активна"


