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
driver.find_element(By.CSS_SELECTOR,"#searchbar").send_keys("Honey Spice Bread")
driver.find_element(By.CSS_SELECTOR,"#submit").click()
RecipeInDisplay= driver.find_element(By.TAG_NAME,"h2").text
assert RecipeInDisplay == "Honey Spice Bread","FAILED to load Recipe"
print("recipe search work when search for existing recipe")
driver.find_element(By.CLASS_NAME,"BeeToHome").click()
driver.find_element(By.CSS_SELECTOR,"#searchbar").send_keys("This recipe does not exist")
driver.find_element(By.CSS_SELECTOR,"#submit").click()
HomePageTitle = driver.find_element(By.CLASS_NAME,"HeadTitle").text
assert HomePageTitle == "The Honeycomb","Failed when searching for non existing recipe"
print("Stayed in Homepage when searching for recipe not Existing")