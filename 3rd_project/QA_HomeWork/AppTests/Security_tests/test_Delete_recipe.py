import pytest
from selenium.webdriver.common.by import By
from AppTests.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
@pytest.mark.Security
class TestSecurity(BaseClass):

    def test_delete_recipe(self,setup):
        setup.get("http://127.0.0.1:5000/")
        log = self.getLogger()
        log.info("Accessing the website...")
        # Get number of recipes before deletion
        log.info("Getting the number of recipes before deletion...")
        NUMPRecipesBefore = setup.find_elements(By.CLASS_NAME, "content")
        num_recipes_before = len(NUMPRecipesBefore)
        log.info(f"Number of recipes before deletion: {num_recipes_before}")

        # Click on the recipe name
        log.info("Clicking on the recipe name...")
        setup.find_element(By.CLASS_NAME, "RecipeName").click()

        # Click on the delete button
        log.info("Clicking on the delete button...")
        setup.find_element(By.XPATH, "//a[normalize-space()='Delete']").click()

        # Get number of recipes after deletion
        log.info("Getting the number of recipes after deletion...")
        NUMPRecipesAfter = setup.find_elements(By.CLASS_NAME, "content")
        num_recipes_after = len(NUMPRecipesAfter)
        log.info(f"Number of recipes after deletion: {num_recipes_after}")

        # Assert that the number of recipes has decreased
        log.info("Asserting that the number of recipes has decreased...")
        assert num_recipes_before > num_recipes_after, "Failed to delete recipe"
        log.info("Recipe deleted")