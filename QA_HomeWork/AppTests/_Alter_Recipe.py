from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.maximize_window()
alter_name = "apple pie"
alter_date = "1000"
driver.get("http://127.0.0.1:5000/alter_recipe/4")
driver.find_element(By.CLASS_NAME,"recipe_name").send_keys(alter_name)
driver.find_element(By.CLASS_NAME,"publish_date").send_keys(alter_date)
driver.find_element(By.XPATH,"//button[normalize-space()='Update']").click()
after_name = driver.find_element(By.CLASS_NAME,"recipe_title").text
after_date = driver.find_element(By.CLASS_NAME,"recipe_date").text
assert alter_name == alter_name,"failed to alter name"
print("name updated!")
assert alter_date == alter_date,"failed to alter date"
print("date updated!")