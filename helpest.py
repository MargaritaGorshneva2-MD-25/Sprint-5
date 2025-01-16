import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from URL import BASE_URL
from locators import Locators


def check_profile_page_opened(driver):
    WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL + "account/profile"))
    assert driver.find_element(*Locators.LOGOUT_BUTTON).is_displayed(), "Страница профиля не открылась."


def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase, k=10))
    domain = "yandex.ru"
    return f"{username}@{domain}"
