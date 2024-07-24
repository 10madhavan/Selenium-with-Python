from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#windowID=driver.current_window_handle
#print("ID",windowID)

driver.find_element(By.LINK_TEXT,"nopCommerce").click()
windowIDs=driver.window_handles

# Approach 1
# parentwindowID=windowIDs[0]
# childwindowID=windowIDs[1]
# #print(parentwindowID,childwindowID)

# driver.switch_to.window(childwindowID)
# print("Title: ",driver.title)
# driver.switch_to.window(parentwindowID)
# print("Title: ",driver.title)

# Approach 2
for winid in windowIDs:
    driver.switch_to.window(winid)
    print(driver.title)


time.sleep(30)
driver.quit()
