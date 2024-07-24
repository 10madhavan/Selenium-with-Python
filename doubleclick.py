from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


driver.find_element(By.ID,"field1").clear()
driver.find_element(By.ID,"field1").send_keys("RO45")
button=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")

act=ActionChains(driver)

act.double_click(button).perform()


time.sleep(30)
driver.quit()

