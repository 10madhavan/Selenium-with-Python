
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
country=Select(driver.find_element(By.XPATH,"//select[@id='country']"))

#select option from the dropdown
country.select_by_visible_text("India")
#course.select_by_value("usa")
#course.select_by_index(4)

#capture all the option and print
alloption=country.options
#print("Total no of country: ",len(alloption))

#for opt in alloption:
#    print(opt.text)

#select option from dropdown without using Select method
#for opt in alloption:
 #   if opt.text=="India":
 #       opt.click()
  #      break

time.sleep(30)
driver.quit()