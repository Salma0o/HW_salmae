import pytest
from selenium.webdriver.common.by import By
import time
from AppTests.BaseClass import *


@pytest.mark.usefixtures("setup")
@pytest.mark.Smoke
class TestSmoke(BaseClass):
    def test_navigation_to_home_from_add(self, setup):
        # Navigate to home page and set up logger
        setup.get("http://127.0.0.1:5000/")
        log = self.getLogger()
        log.info("Navigating to home page from add...")

        # Navigate to recipe add page and check page title
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.CLASS_NAME, "ADD").click()
        RecipeAddTitle = setup.find_element(By.TAG_NAME, "h1").text
        assert RecipeAddTitle == "The Recipes Archive", "Failed to navigate to recipe add"
        log.info("Successfully navigated to recipe add")

        # Click on home page link and check page title
        time.sleep(3)
        setup.find_element(By.TAG_NAME, "a").click()
        HomePageTitle = setup.find_element(By.CLASS_NAME, "HeadTitle").text
        assert HomePageTitle == "The Honeycomb", "Failed to enter home page"
        log.info("Successfully navigated to home page")