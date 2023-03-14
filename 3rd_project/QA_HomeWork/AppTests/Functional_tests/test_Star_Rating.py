import logging
import pytest
from selenium.webdriver.common.by import By
import time
from AppTests.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
@pytest.mark.functional

class TestFunctional(BaseClass):
    def test_add_stars(self, setup):
        log = self.getLogger()

        # Navigating to the website
        log.info("Navigating to the website")
        setup.get("http://127.0.0.1:5000/")

        # Clicking on the recipe name
        log.info("Clicking on the recipe name")
        setup.find_element(By.CLASS_NAME, "recipeName").click()

        # Checking the number of stars before adding new ones
        logging.info("Checking the number of stars before adding new ones")
        stars_before = setup.find_elements(By.ID, "STARS")
        logging.debug(f"Number of stars before adding new ones: {len(stars_before)}")

        # Adding new stars
        logging.info("Adding new stars")
        for i in range(1, 6):
            log.info(f"Clicking on star {i}")
            setup.find_element(By.CSS_SELECTOR, f"label[for='star{i}']").click()

            log.info(f"Entering name for star {i}")
            setup.find_element(By.CSS_SELECTOR, "input[placeholder='write your name...']").send_keys(f"Star {i}")

            log.info(f"Entering review text for star {i}")
            setup.find_element(By.CSS_SELECTOR, "textarea[name='review_text']").send_keys("That is a good test")

            log.info(f"Submitting review for star {i}")
            setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            time.sleep(1)

        # Checking the number of stars after adding new ones
        log.info("Checking the number of stars after adding new ones")
        stars_after = setup.find_elements(By.ID, "STARS")
        logging.debug(f"Number of stars after adding new ones: {len(stars_after)}")

        # Assertion to check if stars were added successfully
        assert len(stars_after) > len(stars_before), "Failed to add stars"
        log.info("Stars added successfully")