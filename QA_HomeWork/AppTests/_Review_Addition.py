from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.maximize_window()
driver.get("http://127.0.0.1:5000/recipe_info/1")
reviews_before=driver.find_elements(By.CLASS_NAME, "NAME")
print(len(reviews_before))
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"label[for='star1']").click()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='write your name...']").send_keys("Add Review Test")
driver.find_element(By.CSS_SELECTOR,"textarea[name='review_text']").send_keys("That is a good test")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(3)
reviews_after=driver.find_elements(By.CLASS_NAME, "NAME")
print(len(reviews_after))
assert len(reviews_after) > len(reviews_before), "failed to add review"
print("review added")