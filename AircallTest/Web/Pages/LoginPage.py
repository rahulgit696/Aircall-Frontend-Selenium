from selenium.webdriver.common.by import By
from AircallTest.Web.Pages.BasePage import BasePage


class LoginPage(BasePage):
    """ This class represents the Login Page """

    # Locators for various elements on the page
    email_address_text_field = (By.XPATH, "//input[@type='text']")
    password_text_field = (By.XPATH, "//input[@type='password']")
    sign_in_button = (By.XPATH, "//button[@data-test='signin-button']")
    validation_error_message = (By.XPATH, "//div[@data-test='toast-message']")

    def __init__(self, driver):
        """ Constructor of the LoginPage class """
        self.driver = driver

    # Methods to interact with the elements on the page

    def enter_email_address(self, email):
        """ Enter the email address in the email field """
        self.send_keys(self.email_address_text_field, email)

    def enter_password(self, password):
        """ Enter the password in the password field """
        self.send_keys(self.password_text_field, password)

    def click_on_sign_in_button(self):
        """ Click on the 'Sign In' button """
        self.click(self.sign_in_button)

    def login_into_application(self, email, password):
        """
        Enter email and password, then click on the 'Sign In' button

        Args:
            email (str): Email address to enter.
            password (str): Password to enter.

        Returns:
            None
        """
        self.enter_email_address(email)
        self.enter_password(password)
        self.click_on_sign_in_button()

    def get_validation_error_message(self):
        """
        Get the validation error message displayed on the page

        Returns:
            str: Text of the validation error message.
        """
        return self.get_element_text(self.validation_error_message)
