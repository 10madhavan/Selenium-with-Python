from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

driver=webdriver.Chrome()                                                                     
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
max_slider=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")

print("Before moving......")
print("Min slider location: ",min_slider.location) # {'x': 59, 'y': 250}
print("Max slider location: ",max_slider.location) # {'x': 612, 'y': 250}

act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-39,0).perform()

print("After moving......")
print("Min slider location: ",min_slider.location) 
print("Max slider location: ",max_slider.location) 


time.sleep(30)
driver.quit()