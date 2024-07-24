from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

   #Navigational commands: back(), forward(), refresh()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.back()
driver.forward()
driver.refresh()

time.sleep(30)
driver.quit()