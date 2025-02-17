import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpest import generate_registration_data
from locators import Locators
from URL import BASE_URL

class TestRegistration:

    @pytest.mark.parametrize("name, email, password, expected_result", [
        ("Test User", generate_registration_data()['email'], "Password123!", "success"),
        ("Test User", generate_registration_data()['email'], "123", "incorrect_password"),
        ("", generate_registration_data()['email'], "Password123!", "empty_name"),
        ("Test User", "", "Password123!", "empty_email"),
        ("Test User", "invalid_email", "Password123!", "invalid_email"),
        ("Test User", generate_registration_data()['email'], "", "empty_password"), # Добавлен тест на пустой пароль
    ])
    def test_registration(self, driver, name, email, password, expected_result):
        driver.get(BASE_URL + "register") # Используем BASE_URL

        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        if expected_result == "success":
            # Ждем появления кнопки "Войти" на главной странице после редиректа
            WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL)) # Ожидаем редирект на главную
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON_FORM))
            assert driver.find_element(*Locators.LOGIN_BUTTON_FORM).is_displayed()

        elif expected_result == "incorrect_password":
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ERROR_TEXT))
            assert driver.find_element(*Locators.ERROR_TEXT).text == "Некорректный пароль"
        elif expected_result == "empty_name":
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ERROR_TEXT))
            assert driver.find_element(*Locators.ERROR_TEXT).text == "Имя не может быть пустым."
        elif expected_result == "empty_email":
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ERROR_TEXT))
            assert driver.find_element(*Locators.ERROR_TEXT).text == "Email не может быть пустым."
        elif expected_result == "invalid_email":
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ERROR_TEXT))
            assert driver.find_element(*Locators.ERROR_TEXT).text == "Некорректный Email"
        elif expected_result == "empty_password": # Проверка на пустой пароль
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ERROR_TEXT))
            assert driver.find_element(*Locators.ERROR_TEXT).text == "Некорректный пароль"