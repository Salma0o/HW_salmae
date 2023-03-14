import time
from selenium.webdriver.common.by import By
import pytest
from AppTests.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
@pytest.mark.functional
class TestFucnctional(BaseClass):
    def test_add_recipe(self, setup):
        log = self.getLogger()
        setup.get("http://127.0.0.1:5000")
        log.info("Test case: add recipe")

        # Get the number of recipes before adding a new one
        NUMPRecipesBefore = len(setup.find_elements(By.CLASS_NAME, "content"))

        # Click the "Add" button to start creating a new recipe
        setup.find_element(By.CLASS_NAME, "ADD").click()
        time.sleep(3)

        # Fill in the form fields with demo data
        setup.find_element(By.CLASS_NAME, "Recipe_name").send_keys("Demo recipe")
        setup.find_element(By.CLASS_NAME, "Description").send_keys("That is a demo recipe")
        setup.find_element(By.CLASS_NAME, "Ingredients").send_keys("That is a demo recipe")
        setup.find_element(By.CLASS_NAME, "Instructions").send_keys("That is a demo recipe")
        setup.find_element(By.CLASS_NAME, "Publisher").send_keys("John Doe")
        setup.find_element(By.ID, "Date").send_keys("02/14/2023")

        # Upload an image file for the recipe
        time.sleep(3)
        setup.find_element(By.XPATH, "//input[@name='filename']").send_keys(
            r"C:\Users\salma\OneDrive\Desktop\Berry-Smoothie-Bowl.jpg")
        setup.find_element(By.XPATH, "//button[normalize-space()='ADD']").click()
        time.sleep(5)

        # Get the number of recipes after adding a new one
        NUMPRecipesAfter = len(setup.find_elements(By.CLASS_NAME, "content"))

        # Check if the number of recipes has increased by 1
        assert NUMPRecipesAfter > NUMPRecipesBefore

        # Log the success message
        log.info("Test passed: add recipe - recipe added successfully")