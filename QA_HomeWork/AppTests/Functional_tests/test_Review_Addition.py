import pytest
from selenium.webdriver.common.by import By
import time
from AppTests.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
@pytest.mark.functional

class TestFunctional(BaseClass):
    def test_add_review(self, setup):
        log = self.getLogger()

        # Navigate to the website
        log.info("Test case: Add review")
        setup.get("http://127.0.0.1:5000/")

        # Click on the recipe name
        setup.find_element(By.CLASS_NAME, "recipeName").click()

        # Get the number of reviews before adding a new one
        reviews_before = setup.find_elements(By.CLASS_NAME, "NAME")
        log.info(f"Number of reviews before adding a new review: {len(reviews_before)}")

        time.sleep(3)

        # Add a new review
        setup.find_element(By.CSS_SELECTOR, "label[for='star1']").click()
        setup.find_element(By.CSS_SELECTOR, "input[placeholder='write your name...']").send_keys("Add Review Test")
        setup.find_element(By.CSS_SELECTOR, "textarea[name='review_text']").send_keys("That is a good test")
        time.sleep(3)
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(6)

        # Get the number of reviews after adding a new one
        reviews_after = setup.find_elements(By.CLASS_NAME, "NAME")
        log.info(f"Number of reviews after adding a new review: {len(reviews_after)}")

        # Check if the new review was added successfully
        assert len(reviews_after) > len(reviews_before), "Failed to add review"
        log.info("New review added successfully")