import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import Locators

# базовый URL
base_url = "https://stellarburgers.nomoreparties.site/"

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver

def test_successful_registration(driver):
    driver.get(base_url + "register")
    driver.find_element(By.XPATH, Locators.name_field).send_keys("Имя")
    driver.find_element(By.XPATH, Locators.email_field).send_keys("email@example.com")
    driver.find_element(By.XPATH, Locators.password_field).send_keys("Пароль123")
    driver.find_element(By.XPATH, Locators.register_button).click()

    # Проверка успешной регистрации (например, редирект или появление элемента)
    try:
        WebDriverWait(driver, 5).until(EC.url_to_be(base_url + "login"))
    except TimeoutException:
        pytest.fail("Регистрация не удалась")
    finally:
        driver.quit()


def test_incorrect_password_registration(driver):
    driver.get(base_url + "register")
    driver.find_element(By.XPATH, Locators.name_field).send_keys("Имя")
    driver.find_element(By.XPATH, Locators.email_field).send_keys("email@example.com")
    driver.find_element(By.XPATH, Locators.password_field).send_keys("123") # Некорректный пароль
    driver.find_element(By.XPATH, Locators.register_button).click()

     # Проверка наличия сообщения об ошибке или того, что регистрация не прошла
    try:
        error_message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locators.error_message_locator))
        )
        assert error_message.is_displayed(), "Сообщение об ошибке не отображается"
    except TimeoutException:
        pytest.fail("Сообщение об ошибке не появилось")
    finally:
        driver.quit()
