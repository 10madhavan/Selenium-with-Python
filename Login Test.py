#Test case
#---------------------------
#open web browser
#open url (https://admin-demo.nopcommerce.com/login)
#provide email (admin@yourstore.com)
#provide passwrd  (admin)
#click login
#capture actual title 
#verify expected title
#close browser

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click() #if there is no ID or NAME in the element, use XPATH 

act_title=driver.title
exp_title="Dashboard / nopCommerce administration"

if act_title==exp_title:
    print("Login Test passed")
    print("Thank you...")
else:
    print("Login Test failed")

time.sleep(3000)
driver.close()