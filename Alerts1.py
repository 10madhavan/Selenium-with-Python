from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#open alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)

alertwindow=driver.switch_to.alert

print(alertwindow.text)
alertwindow.send_keys("welcome")
#alertwindow.accept()   #ok
alertwindow.dismiss()  #cancel

time.sleep(30)
driver.quit()