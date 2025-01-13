import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from URL import BASE_URL
from locators import Locators


@pytest.mark.parametrize("locator, expected_url", [
    (Locators.LOGIN_BUTTON_MAIN_PAGE, BASE_URL + "login"),
    (Locators.PERSONAL_AREA_BUTTON, BASE_URL + "login"),
    (Locators.LOGIN_LINK_REGISTRATION, BASE_URL + "login"),  # Для регистрации
    (Locators.LOGIN_LINK_FORGOT_PASSWORD, BASE_URL + "login"),  # Для восстановления пароля
])
def test_login_redirection(driver, locator, expected_url):
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(locator)
    )
    button.click()

    WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
    assert driver.current_url == expected_url, f"Ожидался URL: {expected_url}, текущий URL: {driver.current_url}"

