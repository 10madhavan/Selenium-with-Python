from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

   #conditional commands:
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()
Search_box=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
   #is_displayed()
print("Display status: ",Search_box.is_displayed())
   #is_enabled()
print("Enabled status: ",Search_box.is_enabled())
if(Search_box.is_displayed()==Search_box.is_enabled()):
   print("Search Box is displayed and Enabled")
else:
   print("Not Working....")

   #is_selected() - for radio buttons and check boxes
rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")
print("default radio buttons status.....")
print("Male is selected? ",rd_male.is_selected())
print("Female is selected?",rd_female.is_selected())

rd_male.click()
print("After selecting male radio buttons status.....")
print("Male is selected? ",rd_male.is_selected())
print("Female is selected?",rd_female.is_selected())

rd_female.click()
print("After selecting female radio buttons status.....")
print("Male is selected? ",rd_male.is_selected())
print("Female is selected?",rd_female.is_selected())


time.sleep(3)
#browser commands: close() and quit()
#close() - close single browser window
#quit() - close multiple browser window
driver.quit() 