import pytest
from locators import Locators
from URL import BASE_URL
from helpest import check_profile_page_opened, wait_for_element


class TestPersonalArea:
    def test_personal_area_from_main_page_login_button(self, logged_in_driver): # <--- logged_in_driver
        logged_in_driver.get(BASE_URL)
        wait_for_element(logged_in_driver, Locators.LOGIN_ACCOUNT_BUTTON).click()
        wait_for_element(logged_in_driver, Locators.PROFILE).click()
        check_profile_page_opened(logged_in_driver)

    def test_personal_area_from_main_page_personal_area_button(self, logged_in_driver): # <--- logged_in_driver
        logged_in_driver.get(BASE_URL)
        wait_for_element(logged_in_driver, Locators.PERSONAL_ACCOUNT_BUTTON).click()
        wait_for_element(logged_in_driver, Locators.PROFILE).click()
        check_profile_page_opened(logged_in_driver)

