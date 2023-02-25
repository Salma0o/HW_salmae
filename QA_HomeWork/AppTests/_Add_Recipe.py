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
driver.get("http://127.0.0.1:5000")
NUMPRecipesBefore=driver.find_elements(By.CLASS_NAME,"content")
print(len(NUMPRecipesBefore))
time.sleep(3)
driver.find_element(By.CLASS_NAME,"ADD").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Choose a name for your recipe...']").send_keys("Demo recipe")
driver.find_element(By.CSS_SELECTOR,"textarea[name='description']").send_keys("That is a demo recipe")
driver.find_element(By.XPATH,"//textarea[@placeholder='Write the ingredients in clear way...']").send_keys("That is a demo recipe")
driver.find_element(By.XPATH,"//textarea[@placeholder='Write the instructions in clear way...']").send_keys("That is a demo recipe")
driver.find_element(By.CSS_SELECTOR,"input[placeholder='write your name...']").send_keys("John Doe")
driver.find_element(By.XPATH,"//input[@placeholder='provide the date']").send_keys("02/14/2023")
time.sleep(3)
driver.find_element(By.XPATH, "//input[@name='filename']").send_keys(r"C:\Users\salma\OneDrive\Desktop\Berry-Smoothie-Bowl.jpg")
driver.find_element(By.XPATH,"//button[normalize-space()='ADD']").click()
time.sleep(3)
NUMPRecipesAfter=driver.find_elements(By.CLASS_NAME,"content")
print(len(NUMPRecipesAfter))
assert len(NUMPRecipesBefore) < len(NUMPRecipesAfter), "failed to add recipe"
print("recipe added")