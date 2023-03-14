
from selenium.webdriver.common.by import By
import time
import pytest
from AppTests.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
@pytest.mark.Security
class TestSecurity(BaseClass):
    def test_search_number(self, setup):
        # Navigate to the website's homepage
        setup.get("http://127.0.0.1:5000/")
        log = self.getLogger()
        log.info("Starting test_search_number")

        # Enter a long number in the search bar
        searched_for = "1246576878786675656454433232346567687998989898989898978675654536"
        setup.get("http://127.0.0.1:5000/")
        time.sleep(3)
        setup.find_element(By.ID, "searchbar").send_keys(searched_for)
        setup.find_element(By.ID, "submit").click()

        # Check if the homepage title is still "The Honeycomb" (indicating that the search did not redirect to a different page)
        HomePageTitle = setup.find_element(By.CLASS_NAME, "HeadTitle").text
        assert HomePageTitle == "The Honeycomb", "Failed when searching for number"
        log.info("Stayed in Homepage when searching for number")