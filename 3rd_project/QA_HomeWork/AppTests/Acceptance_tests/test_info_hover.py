import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from AppTests.BaseClass import BaseClass
import os

@pytest.mark.usefixtures("setup")
@pytest.mark.Acceptance
class TestAcceptance(BaseClass):

    def test_web(self, setup):
        # Navigate to homepage
        setup.get("http://127.0.0.1:5000/")
        log = self.getLogger()

        # Move mouse to a recipe card to reveal recipe name and publisher
        action = ActionChains(setup)
        action.move_to_element(setup.find_element(By.CLASS_NAME, "content")).perform()
        HomePageName = setup.find_element(By.CLASS_NAME, "recipeName").text
        HomePagePublisher = setup.find_element(By.CLASS_NAME, "recipePublisher").text
        log.info(f"HomePageName: {HomePageName}, HomePagePublisher: {HomePagePublisher}")

        # Take screenshot of homepage
        setup.save_screenshot(os.path.join(os.getcwd(), "screenshots", "homepage.png"))

        # Click on recipe card to navigate to recipe info page
        setup.find_element(By.CLASS_NAME, "recipeName").click()
        InfoName = setup.find_element(By.TAG_NAME, "h2").text
        InfoPulisher = setup.find_element(By.CLASS_NAME, "InfoPublisher").text
        log.info(f"InfoName: {InfoName}, InfoPulisher: {InfoPulisher}")

        # Assert that the recipe name and publisher in the homepage matches with the recipe name and publisher in the info page
        assert HomePageName == InfoName, "The recipe names do not match"
        log.info("Recipe names match!")
        assert HomePagePublisher == InfoPulisher, "The publisher names do not match"
        log.info("Publisher names match!")

        # Take screenshot of info page
        setup.save_screenshot(os.path.join(os.getcwd(), "screenshots", "infopage.png"))