import pytest
from selenium import webdriver

# URL for the Aircall login page
_air_call_url = "https://phone.aircall.io/"


# This function allows command line option to choose browser
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


# Fixture for setting up and tearing down the WebDriver instance
@pytest.fixture(autouse=True)
def setup(request):
    global driver

    # Get the browser name from the command line option
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        # Configure Chrome options
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-web-security")
        driver = webdriver.Chrome(options=options)

    # Open the Aircall login page
    driver.get(_air_call_url)

    # Maximize the browser window
    driver.maximize_window()

    # Provide the driver instance to the tests using this fixture
    request.cls.driver = driver
    yield driver

    # Close and quit the driver after tests
    if driver is not None:
        driver.close()
        driver.quit()
