
from selenium.webdriver.common.by import By
import time
import logging
import pytest
from AppTests.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
@pytest.mark.Security
class TestSecurity(BaseClass):

    def test_add_review(self, setup):
        # Load the web page
        setup.get("http://127.0.0.1:5000/")
        log = self.getLogger()

        # Click on the recipe name to go to the recipe page
        setup.find_element(By.CLASS_NAME, "recipeName").click()

        # Get the number of reviews before adding a new review
        reviews_before = setup.find_elements(By.CLASS_NAME, "NAME")
        log.info(f"Number of reviews before adding new review: {len(reviews_before)}")

        # Fill in the review text
        time.sleep(3)
        setup.find_element(By.CSS_SELECTOR, "textarea[name='review_text']").send_keys("add only review")
        log.info("Entered review text")

        # Click the submit button
        time.sleep(3)
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        log.info("Clicked submit button")

        # Get the number of reviews after adding a new review
        time.sleep(3)
        reviews_after = setup.find_elements(By.CLASS_NAME, "NAME")
        logging.info(f"Number of reviews after adding new review: {len(reviews_after)}")

        # Verify that the number of reviews hasn't changed
        assert len(reviews_after) == len(reviews_before), "failed! review was added"
        log.info("review was not added")

        # Quit the browser
        setup.quit()