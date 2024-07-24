from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()              #maximize the screen

#Id or Name locators
#driver.find_element(By.ID,"small-searchterms").clear()
#driver.find_element(By.ID,"small-searchterms").send_keys("Apple MacBook Pro 13-inch ")
#driver.find_element(By.NAME,"q").send_keys("Apple MacBook Pro 13-inch")

#linktext & partial linktext 
driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()


time.sleep(3000)
driver.close()