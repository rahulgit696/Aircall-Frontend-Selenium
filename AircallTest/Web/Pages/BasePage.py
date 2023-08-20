from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    """ This class represents the base page for Selenium interactions """

    def __init__(self, driver):
        """
        Constructor to initialize the BasePage.

        Args:
            driver (WebDriver): The Selenium WebDriver instance.
        """
        self.driver = driver

    def click(self, by_locator):
        """
        Clicks on an element located by the given locator.

        Args:
            by_locator (tuple): Locator strategy and value.

        Returns:
            None
        """
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text):
        """
        Enters text into an element located by the given locator.

        Args:
            by_locator (tuple): Locator strategy and value.
            text (str): Text to be entered.

        Returns:
            None
        """
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        """
        Retrieves the text of an element located by the given locator.

        Args:
            by_locator (tuple): Locator strategy and value.

        Returns:
            str: Text of the element.
        """
        element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
        return element.text
