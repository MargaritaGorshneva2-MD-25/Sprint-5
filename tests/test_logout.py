import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from URL import BASE_URL
from locators import Locators
from helpest import wait_for_element

class TestLogout:
    def test_logout(self, logged_in_user):
        logged_in_user.get(BASE_URL + "account/profile") # Переходим в профиль пользователя, где есть кнопка "Выйти"

        logout_button = wait_for_element(logged_in_user, Locators.LOGOUT_BUTTON)
        logout_button.click()

        WebDriverWait(logged_in_user, 10).until(EC.url_to_be(BASE_URL + "login")) # Ожидаем перенаправления на страницу логина
        assert logged_in_user.current_url == BASE_URL + "login", "Перенаправление на страницу входа не выполнено после выхода"
        # Или можно проверить наличие элемента на странице входа, как в исходном варианте:
        login_button = wait_for_element(logged_in_user, Locators.LOGIN_BUTTON) # Используйте локатор для кнопки на странице логина
        assert login_button.is_displayed(), "Кнопка 'Войти' не отображается после выхода"


