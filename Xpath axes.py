from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

   #self
text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Infosys L')]/self::a").text
print("Name: ",text_msg)

   #parent
text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Infosys L')]/parent::td").text
print("Parent name: ",text_msg)

   #child
childs=driver.find_elements(By.XPATH,"//a[contains(text(),'Infosys L')]/ancestor::tr/child::td")
print("No of childs: ",len(childs))

   #ancestor
text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Infosys L')]/ancestor::tr").text
print("Ancestor: ",text_msg)

   #descendant
descendant=driver.find_elements(By.XPATH,"//a[contains(text(),'Infosys L')]/ancestor::tr/descendant::*")
print("Descendant length: ",len(descendant))

   #following
followings=driver.find_elements(By.XPATH,"//a[contains(text(),'Infosys L')]/ancestor::tr/following::*")
print("following length: ",len(followings))

   #following-siblings
followingsiblings=driver.find_elements(By.XPATH,"//a[contains(text(),'Infosys L')]/ancestor::tr/following-sibling::*")
print("Following-sibling length: ",len(followingsiblings))

   #preceding
precedings=driver.find_elements(By.XPATH,"//a[contains(text(),'Infosys L')]/ancestor::tr/preceding::tr")
print("Preceding length: ",len(precedings))

   #preceding-siblings
precedingsibling=driver.find_elements(By.XPATH,"//a[contains(text(),'Infosys L')]/ancestor::tr/preceding-sibling::tr")
print("Preceding-sibling length: ",len(precedingsibling))



time.sleep(10)
driver.quit()