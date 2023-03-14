from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://127.0.0.1:5000/")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.CLASS_NAME,"content")).perform()
driver.find_element(By.CLASS_NAME,"recipeName").click()
description = driver.find_element(By.CLASS_NAME,"recipe_title").text
ingredients = driver.find_element(By.CLASS_NAME,"ingredient").text
instructions = driver.find_element(By.CLASS_NAME,"instructions").text
publisher = driver.find_element(By.CLASS_NAME,"Publisher").text
date = driver.find_element(By.CLASS_NAME,"recipe_date").text
assert description == "Description", "the description filed is missing"
print("description filed successfully displayed")

assert ingredients == "For this recipe you'll need:", "the ingredients filed is missing"
print("ingredients filed successfully displayed")

assert instructions == "This is how you do it :", "the instructions filed is missing"
print("instructions filed successfully displayed")

assert publisher == "This recipe was written by :", "the publisher filed is missing"
print("publisher filed successfully displayed")

assert date == "Publish date :", "the date filed is missing"
print("date filed successfully displayed")
