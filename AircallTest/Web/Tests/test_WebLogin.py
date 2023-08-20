import pytest
from AircallTest.Web.Pages.LoginPage import LoginPage
from AircallTest.Web.Pages.OnboardingPage import OnboardingPage
from AircallTest.Web.Test_Data.Aircall_Web_Login_Test_Data import LoginTestData


# Using a fixture for test setup
@pytest.mark.usefixtures('setup')
class TestLogin():

    def setup_method(self):
        """ Setup method to initialize page objects """
        # Initialize page objects for login and onboarding pages
        self.login = LoginPage(self.driver)
        self.onboarding = OnboardingPage(self.driver)

    def test_verify_valid_login(self):
        """ Test case to verify valid login """
        # Perform a valid login
        self.login.login_into_application(LoginTestData.VALID_LOGIN_USER, LoginTestData.VALID_PASSWORD)

        # Check if the expected language header title matches the actual one
        assert LoginTestData.EXPECTED_LANGUAGE_HEADER_TITLE == self.onboarding.get_language_header_title()

    def test_verify_invalid_login(self):
        """ Test case to verify invalid login """
        # Perform an invalid login
        self.login.login_into_application(LoginTestData.INVALID_LOGIN_USER, LoginTestData.INVALID_PASSWORD)

        # Check if the expected validation error message matches the actual one
        assert LoginTestData.EXPECTED_VALIDATION_ERROR_MESSAGE == self.login.get_validation_error_message()

    def test_complete_onboarding_flow_for_new_user(self):
        """ Test case to complete the onboarding flow for a new user """
        # Perform a valid login
        self.login.login_into_application(LoginTestData.VALID_LOGIN_USER, LoginTestData.VALID_PASSWORD)

        # Check if the expected language header title matches the actual one
        assert LoginTestData.EXPECTED_LANGUAGE_HEADER_TITLE == self.onboarding.get_language_header_title()

        # Click on the next button in the onboarding process
        self.onboarding.click_on_next_button()

        # Check if the expected header title matches the actual one
        assert LoginTestData.EXPECTED_YOUR_NEW_AIRCALL_EXPERIENCE_HEADER_TITLE == self.onboarding.get_your_new_aircall_experience_header_title()

        # Click on the next button on the slides
        self.onboarding.click_on_next_button_on_slides()

        # Check if the expected test line name matches the actual one
        assert LoginTestData.EXPECTED_TEST_LINE_NAME == self.onboarding.get_test_line_name_text()

        # Check if the expected test line number matches the actual one
        assert LoginTestData.EXPECTED_TEST_LINE_NUMBER == self.onboarding.get_test_line_number_text()
