from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# driver=webdriver.Chrome()
driver=webdriver.Edge()
# driver=webdriver.Firefox()
                                                                               
driver.get("https://www.iplt20.com/")
driver.maximize_window()

time.sleep(30)
driver.quit()