import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os


@pytest.fixture
def driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless") # раскомментируйте для headless режима

    current_directory = os.path.dirname(os.path.abspath(__file__))  # Исправлено: __file__
    driver_path = os.path.join(current_directory, "chromedriver.exe")

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.maximize_window()
    yield driver
    driver.quit()
