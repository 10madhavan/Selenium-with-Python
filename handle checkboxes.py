from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://artoftesting.com/samplesiteforselenium")
driver.maximize_window()

#select specific checkbox
#driver.find_element(By.XPATH,"//input[@value='Automation']").click()

#select all the checkbox
#approach 1
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
#print(len(checkboxes))
#for i in range(len(checkboxes)):
#    checkboxes[i].click()

#approach 2
for checkbox in checkboxes:
    checkbox.click()

#select multiple checkbox by choice
#for checkbox in checkboxes:
#    name=checkbox.get_attribute('value')
#    if name=='Automation' or 'Performance':
#        checkbox.click()
        
#select last checkbox
#for i in range(len(checkboxes)-1,len(checkboxes)):
#   checkboxes[i].click()

#select first checkbox
#for i in range(len(checkboxes)):
#    if i<1:
#        checkboxes[i].click()

#clear all the ccheckboxes
time.sleep(5)
for checkbox in checkboxes:
     if checkbox.is_selected():
         checkbox.click()



time.sleep(30)
driver.quit()