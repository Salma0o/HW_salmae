import time
import logging
import pytest
from selenium.webdriver.common.by import By
from AppTests.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
@pytest.mark.Security
class TestSecurity(BaseClass):
    def test_add_recipe_file(self,setup):
        setup.get("http://127.0.0.1:5000/")
        log = self.getLogger()
        log.info("Getting number of recipes before adding file")
        NUMPRecipesBefore = setup.find_elements(By.CLASS_NAME,"content")
        log.info(f"Number of recipes before adding file: {len(NUMPRecipesBefore)}")

        # Click on "Add Recipe" button
        time.sleep(3)
        log.info("Clicking on 'Add Recipe' button")
        setup.find_element(By.CLASS_NAME, "ADD").click()

        # Fill out recipe form
        time.sleep(3)
        log.info("Filling out recipe form")
        setup.find_element(By.CSS_SELECTOR, "input[placeholder='Choose a name for your recipe...']").send_keys(
            "Demo recipe")
        setup.find_element(By.CSS_SELECTOR, "textarea[name='description']").send_keys("That is a demo recipe")
        setup.find_element(By.XPATH, "//textarea[@placeholder='Write the ingredients in clear way...']") \
            .send_keys("That is a demo recipe")
        setup.find_element(By.XPATH, "//textarea[@placeholder='Write the instructions in clear way...']") \
            .send_keys("That is a demo recipe")
        setup.find_element(By.CSS_SELECTOR, "input[placeholder='write your name...']").send_keys("John Doe")
        setup.find_element(By.XPATH, "//input[@placeholder='provide the date']").send_keys("02/14/2023")
        time.sleep(3)

        # Upload recipe image
        logging.info("Uploading recipe image")
        setup.find_element(By.XPATH, "//input[@name='filename']").send_keys(
            r"C:\Users\salma\OneDrive\Desktop\BMP.bmp")  # Update this file path to the actual location of the file

        # Submit recipe form
        logging.info("Submitting recipe form")
        setup.find_element(By.XPATH, "//button[normalize-space()='ADD']").click()

        # Get the number of recipes after adding the file
        time.sleep(3)
        log.info("Getting number of recipes after adding file")
        time.sleep(3)
        setup.get("http://127.0.0.1:5000/")
        time.sleep(5)
        NUMPRecipesAfter = setup.find_elements(By.CLASS_NAME, "content")
        log.info(f"Number of recipes after adding file: {len(NUMPRecipesAfter)}")

        # Check if file was added successfully
        assert len(NUMPRecipesBefore) == len(NUMPRecipesAfter), "file was not added"
        log.info("File was added")