from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from URL import BASE_URL
from locators import Locators

class TestConstructorSections:
    def test_go_to_sauces_section(self, driver: WebDriver):
        driver.get(BASE_URL)
        driver.find_element(*Locators.FILLINGS_BUTTON).click()
        WebDriverWait(driver, 5).until(ec.visibility_of_element_located(Locators.FILLINGS_BUTTON))
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.SAUCES_MENU)))
        assert driver.find_element(*Locators.ACTIVE_DIV_IN_CONSTRUCTOR).text == 'Соусы'

    def test_go_to_fillings_section(self, driver: WebDriver):
        driver.get(BASE_URL)
        driver.find_element(*Locators.FILLINGS_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.FILLINGS_MENU)))
        assert driver.find_element(*Locators.ACTIVE_DIV_IN_CONSTRUCTOR).text == 'Начинки'

    def test_go_to_buns_section(self, driver: WebDriver):
        driver.get(BASE_URL)
        driver.find_element(*Locators.BUNS_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((Locators.BUNS_MENU)))
        assert driver.find_element(*Locators.ACTIVE_DIV_IN_CONSTRUCTOR).text == 'Булки'