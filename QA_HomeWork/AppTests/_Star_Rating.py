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
stars_before=driver.find_elements(By.ID,"STARS")
print(len(stars_before))
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"label[for='star1']").click()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='write your name...']").send_keys("Star 1")
driver.find_element(By.CSS_SELECTOR,"textarea[name='review_text']").send_keys("That is a good test")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"label[for='star2']").click()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='write your name...']").send_keys("Star 2")
driver.find_element(By.CSS_SELECTOR,"textarea[name='review_text']").send_keys("That is a good test")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"label[for='star3']").click()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='write your name...']").send_keys("Star 3")
driver.find_element(By.CSS_SELECTOR,"textarea[name='review_text']").send_keys("That is a good test")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"label[for='star4']").click()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='write your name...']").send_keys("Star 4")
driver.find_element(By.CSS_SELECTOR,"textarea[name='review_text']").send_keys("That is a good test")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"label[for='star5']").click()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='write your name...']").send_keys("Star 5")
driver.find_element(By.CSS_SELECTOR,"textarea[name='review_text']").send_keys("That is a good test")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(3)
stars_after=driver.find_elements(By.ID,"STARS")
print(len(stars_after))
assert len(stars_after) > len(stars_before),"failed to add stars"
print("stars added")