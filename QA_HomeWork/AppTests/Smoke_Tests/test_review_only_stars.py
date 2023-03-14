import pytest
from selenium.webdriver.common.by import By
import time
from AppTests.BaseClass import *


@pytest.mark.usefixtures("setup")
@pytest.mark.Smoke
class TestSmoke(BaseClass):
    def test_review_submission(self, setup):
        # Navigate to the website
        setup.get("http://127.0.0.1:5000/")
        log = self.getLogger()

        # Click on a recipe to go to its page
        setup.find_element(By.CLASS_NAME, "recipeName").click()

        # Get the number of reviews before submission
        reviews_before = setup.find_elements(By.CLASS_NAME, "NAME")
        log.info(f"Number of reviews before submission: {len(reviews_before)}")
        time.sleep(3)

        # Click on the first star to rate the recipe
        setup.find_element(By.CSS_SELECTOR, "label[for='star1']").click()
        time.sleep(3)

        # Submit the review
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(3)

        # Get the number of reviews after submission
        reviews_after = setup.find_elements(By.CLASS_NAME, "NAME")
        log.info(f"Number of reviews after submission: {len(reviews_after)}")

        # Check that the number of reviews has not changed after submission
        assert len(reviews_after) == len(reviews_before), "Failed! Review was added"
        log.info("Review was not added!")