from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://www.amazon.in/")
driver.maximize_window()

   #absolute/full xpath
#driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input").send_keys("T-shirts")
#driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input").click()

#relative xpath Syntax: //tagname[@attribute='value']     instead of tagname, we can use * symbol for.ex: //*[@attribute='value']
driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("T-shirts")
driver.find_element(By.XPATH,"//*[@id='nav-search-submit-button']").click()

   #xpath options: or , and , contains() , start-with() , text() 
   # or is used to execute any one attribute is correct
   # and is used to both attributes should be correct 
#driver.find_element(By.XPATH,"//input[@id='twotabsearchtxtbox' or @name='field-keywords']").send_keys("T-shirts")  
#driver.find_element(By.XPATH,"//*[@id='nav-search-submit-button' and @class='nav-input nav-progressive-attribute']").click()   

   #contains()
   #start-with()
#driver.find_element(By.XPATH,"//input[contains(@id,'twotabsearch')]").send_keys("T-shirts") 
#driver.find_element(By.XPATH,"//input[starts-with(@id,'nav-search')]").click()  

   #text()
#driver.find_element(By.XPATH,"//a[text()='Mobiles']").click()  

time.sleep(3000)
driver.close()