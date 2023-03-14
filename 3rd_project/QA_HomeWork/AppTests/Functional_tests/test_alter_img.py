
from selenium.webdriver.common.by import By
import time
import pytest
from AppTests.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
@pytest.mark.functional

class TestFucnctional(BaseClass):
    # Load the website and create a logger
    def test_homepage_to_recipe_info(self, setup):
        setup.get("http://127.0.0.1:5000")
        log = self.getLogger()

        # Navigate to the recipe information page from the homepage
        log.info("Test case: homepage to recipe info")
        setup.find_element(By.CLASS_NAME, "recipeName").click()
        time.sleep(3)
        setup.find_element(By.CSS_SELECTOR, ".btn-hover.color-2").click()
        time.sleep(3)

        # Add a new image to the recipe information page
        log.info("Adding new image to the recipe information page")
        setup.find_element(By.CSS_SELECTOR, "input[name='filename']").send_keys(
            r"C:\Users\salma\OneDrive\Desktop\pro_recipe\Chocolate-Raspberry-Tart.jpg")
        time.sleep(2)
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(3)

        # Check that the new image is displayed on the page
        new_image = setup.find_element(By.CLASS_NAME, "info_image").get_attribute("src")
        assert new_image == "http://127.0.0.1:5000/display/Chocolate-Raspberry-Tart.jpg"
        log.info("Test passed: homepage to recipe info - image successfully altered")

