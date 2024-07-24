from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
                                                                               
driver.get("https://www.iplt20.com/")
driver.maximize_window()
cookybtn=driver.find_element(By.XPATH,"//button[normalize-space()='Accept cookies']").click()
more=driver.find_element(By.XPATH,"/html/body/header/div[2]/div/div[3]/div/div/nav/ul/li[7]/a")
abtus=driver.find_element(By.XPATH,"/html/body/header/div[2]/div/div[3]/div/div/nav/ul/li[7]/ul/li[1]/a")

#mousehover
act=ActionChains(driver)
act.move_to_element(more).move_to_element(abtus).click().perform()


time.sleep(30)
driver.quit()