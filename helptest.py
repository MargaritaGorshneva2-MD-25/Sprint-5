import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from URL import LOGIN_URL
from config import TEST_EMAIL, TEST_PASSWORD


def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "mail.ru", "outlook.com"]
    username_length = 10
    letters = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(letters) for i in range(username_length))
    domain = random.choice(domains)
    return f"{username}@{domain}"


def login(driver):
    """Авторизует пользователя, используя данные из config.py."""
    driver.get(LOGIN_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.EMAIL))
    driver.find_element(*Locators.EMAIL).send_keys(TEST_EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(TEST_PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON_FORM).click()

    WebDriverWait(driver, 10).until(EC.url_changes(LOGIN_URL))

