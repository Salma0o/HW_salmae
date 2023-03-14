from AppTests.conftest import *
from AppTests.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
@pytest.mark.Acceptance
class TestAcceptance(BaseClass):

    def test_image_match(self, setup):
        # Navigate to the home page and get the logger object
        setup.get("http://127.0.0.1:5000/")
        log = self.getLogger()

        # Get the source of the home page image and the recipe info page image
        home_image = setup.find_element(By.CLASS_NAME, "home_image").get_attribute("src")
        setup.find_element(By.CLASS_NAME, "recipeName").click()
        info_image = setup.find_element(By.CLASS_NAME, "info_image").get_attribute("src")

        # Compare the two images and log the result
        try:
            assert home_image == info_image, "The pictures displayed in home and info page do not match"
            log.info("The pictures displayed in home and info page match.")
        except AssertionError as e:
            log.error(e)
            setup.save_screenshot("screenshot.png")
            raise