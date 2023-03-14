import pytest
import time
from selenium.webdriver.common.by import By
from AppTests.BaseClass import *


@pytest.mark.usefixtures("setup")
@pytest.mark.Smoke
class TestSmoke(BaseClass):
    def test_navigate_to_recipe_info(self, setup):
        setup.get("http://127.0.0.1:5000/")
        log = self.getLogger()
        log.info("Navigate to recipe info")

        # Click on a recipe name to navigate to recipe info
        setup.find_element(By.CLASS_NAME, "recipeName").click()

        # Check if the title of the recipe info page is "Description"
        RecipeInfoTitle = setup.find_element(By.CLASS_NAME, "recipe_title").text
        assert RecipeInfoTitle == "Description", "Failed to navigate to recipe info"
        log.info("Successfully navigated to recipe info")

        # Click on "back to home" button to navigate to the home page
        time.sleep(3)
        setup.find_element(By.CLASS_NAME, "BeeToHome").click()
        HomePageTitle = setup.find_element(By.CLASS_NAME, "HeadTitle").text
        assert HomePageTitle == "The Honeycomb", "Failed to enter home page"
        log.info("Successfully navigated to home page")

