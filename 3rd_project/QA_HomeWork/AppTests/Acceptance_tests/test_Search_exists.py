import pytest
import time
import os
from selenium.webdriver.common.by import By
from AppTests.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
@pytest.mark.Acceptance
class TestAcceptance(BaseClass):
    # Defining a test function that takes 'setup' as a parameter
    def test_recipe_search_existing(self, setup):
        # Setting the value of the variable 'searched_for' to "Bread"
        searched_for = "Bread"

        # Opening the website specified by the URL
        setup.get("http://127.0.0.1:5000/")

        # Creating a logger object to record events and messages
        log = self.getLogger()

        # Waiting for 3 seconds to let the website load
        time.sleep(3)

        # Finding the search bar element using ID and entering 'searched_for' as its value
        setup.find_element(By.ID, "searchbar").send_keys(searched_for)

        # Finding the submit button element using ID and clicking on it
        setup.find_element(By.ID, "submit").click()

        # Taking a screenshot of the web page after the search results are displayed
        test_name = "test_recipe_search_existing"
        screenshot_folder = "screenshots"
        os.makedirs(screenshot_folder, exist_ok=True)
        screenshot_path = f"{screenshot_folder}/{test_name}_{int(time.time())}.png"
        setup.save_screenshot(screenshot_path)

        # Finding the recipe that is displayed using h2 tag and saving its text as 'RecipeInDisplay'
        RecipeInDisplay = setup.find_element(By.TAG_NAME, "h2").text

        # Asserting that the displayed recipe matches the searched recipe, ignoring case sensitivity
        assert RecipeInDisplay.upper() == searched_for.upper()

        # Logging a message to indicate that the recipe search works correctly when searching for an existing recipe.
        log.info("Recipe search works when searching for an existing recipe")