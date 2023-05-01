from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService
import pprint
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
chrome_driver_path="C:/Users/Manish singh/chromedriver.exe"
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeQvVOm_I11CAcX6_eMrnFWjjG-UKs0F30eQqbuczfufeLQeg/viewform")
time.sleep(5)
my_details=["Manish","Kumar","manishkumarnit3@gmail.com"]
inputs=driver.find_elements(by=By.CLASS_NAME,value="whsOnd.zHQkBf")

for i in range(len(my_details)):
    inputs[i].send_keys(my_details[i])
submit=driver.find_element(by=By.CLASS_NAME,value="NPEfkd.RveJvd.snByac")
submit.click()
time.sleep(5)
driver.quit()



