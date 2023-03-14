from selenium.webdriver.common.by import By
import time
import pytest
from AppTests.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
@pytest.mark.Acceptance

class TestAcceptance(BaseClass):
    def test_add_name(self, setup):
        setup.get("http://127.0.0.1:5000/")
        log = self.getLogger()

        # Click on the recipe name to access the review section
        setup.find_element(By.CLASS_NAME, "recipeName").click()

        # Get the number of reviews before adding a new one
        reviews_before = setup.find_elements(By.CLASS_NAME, "NAME")
        log.info(f"Number of names before adding new name: {len(reviews_before)}")

        # Add a name without a review
        time.sleep(3)
        setup.find_element(By.CSS_SELECTOR, "input[placeholder='write your name...']").send_keys("Add only name")
        log.info("Entered name")
        setup.save_screenshot("add_name.png")
        time.sleep(3)
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        log.info("Clicked submit button")
        setup.save_screenshot("submit_button.png")
        time.sleep(3)

        # Get the number of reviews after adding a new one
        reviews_after = setup.find_elements(By.CLASS_NAME, "NAME")
        log.info(f"Number of names after adding new name: {len(reviews_after)}")

        # Check if the number of reviews is still the same as before, indicating that the new review was not added
        assert len(reviews_after) == len(reviews_before), "failed! name was added"
        log.info("Name was not added")

        setup.save_screenshot("test_add_name.png")
        setup.quit()