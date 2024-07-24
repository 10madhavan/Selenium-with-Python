from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#click on link
#driver.find_element(By.LINK_TEXT,"Digital downloads").click()

#find no of link in the page
links=driver.find_elements(By.XPATH,"//a")
print("No.of Links in this page is ",(len(links)))

#print all the link names
for link in links:
    print(link.text)


time.sleep(30)
driver.quit()