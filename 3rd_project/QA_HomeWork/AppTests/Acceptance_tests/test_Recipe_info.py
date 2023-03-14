import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from AppTests.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
@pytest.mark.Acceptance

class TestAcceptance(BaseClass):
    def test_recipe_info_fields(self, setup):
        # Load the website and get logger
        setup.get("http://127.0.0.1:5000/")
        log = self.getLogger()

        # Hover over content and click on recipe name
        action = ActionChains(setup)
        action.move_to_element(setup.find_element(By.CLASS_NAME, "content")).perform()
        setup.find_element(By.CLASS_NAME, "recipeName").click()

        # Get information from recipe info page
        # Get the recipe description
        description = setup.find_element(By.CLASS_NAME, "recipe_title").text
        # Get the recipe ingredients
        ingredients = setup.find_element(By.CLASS_NAME, "ingredient").text
        # Get the recipe instructions
        instructions = setup.find_element(By.CLASS_NAME, "instructions").text
        # Get the recipe publisher
        publisher = setup.find_element(By.CLASS_NAME, "Publisher").text
        # Get the recipe publish date
        date = setup.find_element(By.CLASS_NAME, "recipe_date").text

        # Take screenshot of recipe info page
        setup.save_screenshot("recipe_info.png")
        log.info("Screenshot of recipe info page taken.")

        # Check that all necessary fields are displayed correctly
        # Check if the recipe description field is displayed correctly
        assert description == "Description", "The description field is missing"
        log.info("Description field successfully displayed.")
        # Check if the recipe ingredients field is displayed correctly
        assert ingredients == "For this recipe you'll need:", "The ingredients field is missing"
        log.info("Ingredients field successfully displayed.")
        # Check if the recipe instructions field is displayed correctly
        assert instructions == "This is how you do it :", "The instructions field is missing"
        log.info("Instructions field successfully displayed.")
        # Check if the recipe publisher field is displayed correctly
        assert publisher == "This recipe was written by :", "The publisher field is missing"
        log.info("Publisher field successfully displayed.")
        # Check if the recipe publish date field is displayed correctly
        assert date == "Publish date :", "The date field is missing"
        log.info("Date field successfully displayed.")
