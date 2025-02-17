from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from URL import BASE_URL
from config import TEST_EMAIL, TEST_PASSWORD
from locators import Locators

class TestTransition:
    def test_transition_to_constructor_from_profile(self, driver):
        driver.get(BASE_URL + "login")
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[text()='Войти']")))
        driver.find_element(By.XPATH, "//input[@formcontrolname='email']").send_keys(TEST_EMAIL) # Локатор для email
        driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys(TEST_PASSWORD) # Локатор для password
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        WebDriverWait(driver, 10).until(ec.url_to_be(BASE_URL))

        driver.get(BASE_URL + "account/profile")
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(Locators.PROFILE)) # Убедитесь, что Locators.PROFILE корректен
        driver.find_element(*Locators.CONSTRUCTOR).click() # Убедитесь, что Locators.CONSTRUCTOR корректен
        WebDriverWait(driver, 10).until(ec.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

    def test_transition_to_constructor_by_logo_from_profile(self, driver):
        driver.get(BASE_URL + "login")
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[text()='Войти']")))
        driver.find_element(By.XPATH, "//input[@formcontrolname='email']").send_keys(TEST_EMAIL) # Локатор для email
        driver.find_element(By.XPATH, "//input[@formcontrolname='password']").send_keys(TEST_PASSWORD) # Локатор для password
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        WebDriverWait(driver, 10).until(ec.url_to_be(BASE_URL))

        driver.get(BASE_URL + "account/profile")
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(Locators.PROFILE)) # Убедитесь, что Locators.PROFILE корректен
        driver.find_element(*Locators.LOGO).click() # Убедитесь, что Locators.LOGO корректен
        WebDriverWait(driver, 10).until(ec.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL
