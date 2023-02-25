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
HomePageName = driver.find_element(By.CLASS_NAME,"recipeName").text
HomePagePublisher= driver.find_element(By.CLASS_NAME,"recipePublisher").text
print("HomePageName: ",HomePageName,"HomePagePublisher: ",HomePagePublisher)
driver.find_element(By.CLASS_NAME,"recipeName").click()
InfoName = driver.find_element(By.TAG_NAME,"h2").text
InfoPulisher = driver.find_element(By.CLASS_NAME,"InfoPublisher").text
print("InfoName: ",InfoName,"InfoPulisher: ",InfoPulisher)
assert HomePageName == InfoName,"the name doesn't match"
print("recipe names match!!")
assert HomePagePublisher == InfoPulisher,"the publisher name doesn't match"
print("publisher names match!!")