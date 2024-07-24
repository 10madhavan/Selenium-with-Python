from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

src_ele=driver.find_element(By.ID,"draggable")
tar_ele=driver.find_element(By.ID,"droppable")

act=ActionChains(driver)
act.drag_and_drop(src_ele,tar_ele).perform()


time.sleep(30)
driver.quit()