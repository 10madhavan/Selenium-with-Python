from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
#driver.get("https://the-internet.herokuapp.com/basic_auth")

#syntax:  https://username:password@url
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

time.sleep(5)
driver.quit()