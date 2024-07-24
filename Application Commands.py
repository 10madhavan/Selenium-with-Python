from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

   #Application commands: get(), title, current_url, page_source
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
print("Title: ",driver.title)
print("Current URL: ",driver.current_url)
print("Source code:",driver.page_source)

time.sleep(3)
driver.quit() 