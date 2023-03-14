import logging
import pytest
from selenium.webdriver.common.by import By
import time
from AppTests.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
@pytest.mark.Security
class TestSecurity(BaseClass):
    def test_search_non_existing_recipe(self, setup):
        # Navigate to the homepage
        setup.get("http://127.0.0.1:5000/")
        log = self.getLogger()
        searched_for = "This recipe does not exist"

        # Enter a search term for a non-existing recipe
        log.info("Navigated to the homepage")
        time.sleep(3)
        setup.find_element(By.ID, "searchbar").send_keys(searched_for)
        setup.find_element(By.ID, "submit").click()

        # Check if the user is still on the homepage after searching for the non-existing recipe
        HomePageTitle = setup.find_element(By.CLASS_NAME, "HeadTitle").text
        assert HomePageTitle == "The Honeycomb", "Failed when searching for non existing recipe"
        logging.info("Stayed in Homepage when searching for recipe not existing")