from selenium.webdriver.common.by import By
from AircallTest.Web.Pages.BasePage import BasePage


class OnboardingPage(BasePage):
    """ This class represents the Onboarding Page """

    # Locators for various elements on the page
    language_header_title = (By.XPATH, "(//div[contains(text(), 'Language')])[1]")
    next_button = (By.XPATH, "//button[@data-test='continue-button']")
    your_new_aircall_experience_header_title = (By.XPATH, "//div[@data-test='heading-text']")
    next_button_on_second_slide = (By.XPATH, "//button[@data-test='next-button']")
    todo_header_title = (By.XPATH, "//div[@data-test='heading-text']")
    test_line_name_text = (By.XPATH, "//p[@data-test='line-name']")
    test_line_number_text = (By.XPATH, "//p[@data-test='line-number']")

    def __init__(self, driver):
        """ Constructor of the OnboardingPage class """
        self.driver = driver

    # Methods to interact with the elements on the page

    def get_language_header_title(self):
        """ Get the text of the language header title """
        return self.get_element_text(self.language_header_title)

    def click_on_next_button(self):
        """ Click on the 'Next' button """
        self.click(self.next_button)

    def get_your_new_aircall_experience_header_title(self):
        """ Get the text of the 'Your New Aircall Experience' header title """
        return self.get_element_text(self.your_new_aircall_experience_header_title)

    def click_on_next_button_on_slides(self):
        """ Click on the 'Next' button on the slides multiple times """
        # The button is clicked multiple times, potentially advancing slides
        self.click(self.next_button_on_second_slide)
        self.click(self.next_button_on_second_slide)
        self.click(self.next_button_on_second_slide)
        self.click(self.next_button_on_second_slide)

    def get_todo_header_title(self):
        """ Get the text of the 'To-Do' header title """
        return self.get_element_text(self.todo_header_title)

    def get_test_line_name_text(self):
        """ Get the text of the test line name """
        return self.get_element_text(self.test_line_name_text)

    def get_test_line_number_text(self):
        """ Get the text of the test line number """
        return self.get_element_text(self.test_line_number_text)
