import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from helptest import login


def test_navigation_buns(driver):
    login(driver)
    buns_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(Locators.BUNS_BUTTON)
    )
    driver.execute_script("arguments[0].scrollIntoView();", buns_button)
    driver.execute_script("arguments[0].click();", buns_button)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.BUNS_MENU)
    )


def test_navigation_sauces(driver):
    login(driver)
    sauces_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(Locators.SAUCES_BUTTON)
    )
    driver.execute_script("arguments[0].scrollIntoView();", sauces_button)
    driver.execute_script("arguments[0].click();", sauces_button)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.SAUCES_MENU)
    )


def test_navigation_fillings(driver):
    login(driver)
    fillings_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(Locators.FILLINGS_BUTTON)
    )
    driver.execute_script("arguments[0].scrollIntoView();", fillings_button)
    driver.execute_script("arguments[0].click();", fillings_button)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.FILLINGS_MENU)
    )
