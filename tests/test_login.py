import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from URL import BASE_URL
from locators import Locators

class TestLoginRedirection: # Создаем тестовый класс
    @pytest.mark.parametrize("locator, expected_url", [
        (Locators.LOGIN_BUTTON_MAIN_PAGE, BASE_URL + "login"),
        (Locators.PERSONAL_AREA_BUTTON, BASE_URL + "login"),
        (Locators.LOGIN_LINK_REGISTRATION_FORM, BASE_URL + "login"), # Изменили локатор
        (Locators.LOGIN_LINK_FORGOT_PASSWORD_FORM, BASE_URL + "login"), # Изменили локатор
    ])
    def test_redirection(self, driver, locator, expected_url): # Изменили имя тестового метода
        if locator in (Locators.LOGIN_LINK_REGISTRATION_FORM, Locators.LOGIN_LINK_FORGOT_PASSWORD_FORM):
            # Для перехода на страницы регистрации и восстановления пароля
            # нужно сначала перейти на страницу входа или регистрации
            driver.get(BASE_URL + "register") # Можно использовать "login" или "register" в зависимости от вашего приложения

            if locator == Locators.LOGIN_LINK_FORGOT_PASSWORD_FORM:
                # Если проверяем ссылку "Восстановить пароль", нужно сначала перейти на страницу входа
                 WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.LOGIN_LINK_REGISTRATION_FORM)).click()
                 WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "login")) #Проверка, что мы на странице /login



        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        button.click()

        WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
        assert driver.current_url == expected_url, f"Ожидался URL: {expected_url}, текущий URL: {driver.current_url}"
