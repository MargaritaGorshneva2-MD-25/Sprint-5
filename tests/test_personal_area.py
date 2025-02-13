import pytest
from locators import Locators
from URL import BASE_URL
from helpest import check_profile_page_opened, wait_for_element


class TestPersonalArea:
    def test_personal_area_from_main_page_login_button(self, logged_in_user):
        logged_in_user.get(BASE_URL)
        wait_for_element(logged_in_user, Locators.LOGIN_BUTTON_MAIN_PAGE).click()
        wait_for_element(logged_in_user, Locators.PROFILE_LINK).click()
        check_profile_page_opened(logged_in_user)

    def test_personal_area_from_main_page_personal_area_button(self, logged_in_user):
        logged_in_user.get(BASE_URL)
        wait_for_element(logged_in_user, Locators.PERSONAL_AREA_BUTTON).click()
        wait_for_element(logged_in_user, Locators.PROFILE_LINK).click()
        check_profile_page_opened(logged_in_user)
