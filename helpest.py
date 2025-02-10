import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from URL import BASE_URL
from locators import Locators


def check_profile_page_opened(driver):
    wait_for_url(driver, BASE_URL + "account/profile")
    assert driver.find_element(*Locators.LOGOUT_BUTTON).is_displayed(), "Страница профиля не открылась."


def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase, k=10))
    domain = "yandex.ru"
    return f"{username}@{domain}"


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def wait_for_url(driver, expected_url, timeout=10):
    WebDriverWait(driver, timeout).until(EC.url_to_be(expected_url))
    assert driver.current_url == expected_url, f"Ожидался URL: {expected_url}, текущий URL: {driver.current_url}"


def click_and_check_url(driver, locator, expected_url, base_url=None):
    """Кликает на элемент и проверяет, что URL соответствует ожидаемому."""
    if base_url:
        driver.get(base_url)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
    else:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))

    element.click()
    WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))
    assert driver.current_url == expected_url, f"Ожидался URL: {expected_url}, текущий URL: {driver.current_url}"


def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )
