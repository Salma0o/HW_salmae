import time
import pytest
from selenium.webdriver.common.by import By
from AppTests.BaseClass import *


@pytest.mark.usefixtures("setup")
@pytest.mark.Smoke
class TestSmoke(BaseClass):
    def test_navigate_to_home_page_from_recipe_info(self,setup):
        # Navigate to the homepage
        setup.get("http://127.0.0.1:5000/")
        log = self.getLogger()
        log.info("Navigating to the home page")

        # Click on a recipe and navigate to the recipe alteration page
        setup.find_element(By.CLASS_NAME,"recipeName").click()
        time.sleep(3)
        setup.find_element(By.CSS_SELECTOR,".btn-hover.color-2").click()
        time.sleep(3)
        RecipeAlterTitle = setup.find_element(By.CLASS_NAME,"recipe_alter").text
        assert RecipeAlterTitle == "Recipe update","Failed to navigate to recipe alter"
        log.info("Successfully navigated to recipe alter")

        # Navigate back to the homepage
        time.sleep(3)
        setup.find_element(By.TAG_NAME,"a").click()
        HomePageTitle = setup.find_element(By.CLASS_NAME,"HeadTitle").text
        assert HomePageTitle == "The Honeycomb","Failed to enter home page"
        log.info("Successfully navigated to home page")