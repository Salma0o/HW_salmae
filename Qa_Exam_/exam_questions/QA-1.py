import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service("chromedriver_linux64/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(4)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"name").send_keys("Salma")
driver.find_element(By.NAME,"email").send_keys("Salmaay96@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("1234")
driver.find_element(By.CLASS_NAME,"form-check-label").click()
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
driver.find_element(By.CSS_SELECTOR,"label[for='inlineRadio1']").click()
driver.find_element(By.NAME,"bday").send_keys("05/01/1996")
driver.find_element(By.XPATH,"//input[@value='Submit']").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='alert alert-success alert-dismissible']")))
alert = (driver.find_element(By.TAG_NAME,"strong").text)
assert alert == "Success!" ,"failed to sign in"
print("successfully signed in ")