from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://mypage.rediff.com/login/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@value='Login']").click()
time.sleep(3)
driver.switch_to.alert.accept()

time.sleep(30)
driver.quit()