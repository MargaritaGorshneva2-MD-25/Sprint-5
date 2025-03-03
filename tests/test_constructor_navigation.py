from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

def test_navigation_buns(authorized_driver):
    buns_button = WebDriverWait(authorized_driver, 20).until(
        EC.presence_of_element_located(Locators.BUNS_BUTTON)
    )
    authorized_driver.execute_script("arguments[0].scrollIntoView();", buns_button)
    authorized_driver.execute_script("arguments[0].click();", buns_button)

    buns_menu = WebDriverWait(authorized_driver, 10).until(
        EC.presence_of_element_located(Locators.BUNS_MENU)
    )
    assert buns_menu.is_displayed(), "Меню 'Булки' не отображается"

def test_navigation_sauces(authorized_driver):
    sauces_button = WebDriverWait(authorized_driver, 20).until(
        EC.presence_of_element_located(Locators.SAUCES_BUTTON)
    )
    authorized_driver.execute_script("arguments[0].scrollIntoView();", sauces_button)
    authorized_driver.execute_script("arguments[0].click();", sauces_button)

    sauces_menu = WebDriverWait(authorized_driver, 10).until(
        EC.presence_of_element_located(Locators.SAUCES_MENU)
    )
    assert sauces_menu.is_displayed(), "Меню 'Соусы' не отображается"

def test_navigation_fillings(authorized_driver):
    fillings_button = WebDriverWait(authorized_driver, 20).until(
        EC.presence_of_element_located(Locators.FILLINGS_BUTTON)
    )
    authorized_driver.execute_script("arguments[0].scrollIntoView();", fillings_button)
    authorized_driver.execute_script("arguments[0].click();", fillings_button)

    fillings_menu = WebDriverWait(authorized_driver, 10).until(
        EC.presence_of_element_located(Locators.FILLINGS_MENU)
    )
    assert fillings_menu.is_displayed(), "Меню 'Начинки' не отображается"
