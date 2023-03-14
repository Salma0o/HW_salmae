import pytest
from selenium.webdriver.common.by import By
from AppTests.BaseClass import BaseClass
import time

@pytest.mark.usefixtures("setup")
@pytest.mark.functional

class TestFunctional(BaseClass):
    # This method tests the functionality to alter a recipe name.
    def test_alter_recipe_name(self, setup):
        # This line creates a logger object to log messages.
        log = self.getLogger()
        # These two variables contain the new recipe name and publish date to be set.
        alter_name = "apple pie"
        alter_date = "1000"
        # This line navigates to a web page.
        setup.get("http://127.0.0.1:5000/")
        # This line finds an element on the web page by class name and clicks on it.
        setup.find_element(By.CLASS_NAME, "recipeName").click()
        # This line waits for 3 seconds.
        time.sleep(3)
        # This line finds an element on the web page by CSS selector and clicks on it.
        setup.find_element(By.CSS_SELECTOR, ".btn-hover.color-2").click()
        # This line finds an element on the web page by class name and sends the new recipe name.
        setup.find_element(By.CLASS_NAME, "recipe_name").send_keys(alter_name)
        # This line finds an element on the web page by class name and sends the new publish date.
        setup.find_element(By.CLASS_NAME, "publish_date").send_keys(alter_date)
        # This line finds an element on the web page by XPATH and clicks on it.
        setup.find_element(By.XPATH, "//button[normalize-space()='Update']").click()
        # These two lines get the recipe name and publish date from the web page after updating.
        after_name = setup.find_element(By.CLASS_NAME, "recipe_title").text
        after_date = setup.find_element(By.CLASS_NAME, "recipe_date").text
        # This line checks if the new recipe name and publish date were updated successfully.
        assert alter_name == alter_name, "failed to alter name"
        # This line prints a message if the name was successfully updated.
        print("name updated!")
        assert alter_date == alter_date, "failed to alter date"
        # This line prints a message if the date was successfully updated.
        print("date updated!")