import pytest
from selenium.webdriver.common.by import By
from AppTests.BaseClass import *


@pytest.mark.usefixtures("setup")
@pytest.mark.Smoke
class TestSmoke(BaseClass):
    def test_home_page_title(self, setup):
        # Get the driver object from the fixture
        driver = setup
        # Set up the logger object
        log = self.getLogger()
        # Navigate to the home page
        setup.get("http://127.0.0.1:5000/")
        # Find the title element and get its text
        HomePageTitle = setup.find_element(By.CLASS_NAME, "HeadTitle").text
        # Take a screenshot of the home page
        setup.get_screenshot_as_file("HomePage.png")
        # Check that the title matches the expected value
        assert HomePageTitle == "The Honeycomb", "Failed to enter home page"
        # Log a success message
        log.info("Successfully navigated to home page")


def test_crossBrowser(crossBrowser):
    # Print the crossBrowser fixture, which is being passed in as an argument
    print(crossBrowser)