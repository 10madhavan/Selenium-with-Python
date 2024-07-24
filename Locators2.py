from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
sliders=driver.find_elements(By.CLASS_NAME,"a-carousel-card")
print("No.of slide is ",len(sliders))
links=driver.find_elements(By.TAG_NAME,"a")
print("No.of Links in this page is ",(len(links)))


time.sleep(3000)
driver.close()