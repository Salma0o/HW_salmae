import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.maximize_window()
driver.get("http://127.0.0.1:5000/")
NUMPRecipesBefore=driver.find_elements(By.CLASS_NAME,"content")
print(len(NUMPRecipesBefore))
time.sleep(3)
driver.find_element(By.CLASS_NAME,"RecipeName").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[normalize-space()='Delete']").click()
NUMPRecipesAfter=driver.find_elements(By.CLASS_NAME,"content")
print(len(NUMPRecipesAfter))
assert len(NUMPRecipesBefore) > len(NUMPRecipesAfter), "failed to delete recipe"
print("recipe deleted")