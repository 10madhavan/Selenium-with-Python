from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

driver.get("https://www.facebook.com/")
driver.maximize_window()

#tag & id  syntax: tagname#valueofID
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc@gmail.com")
#driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc")    #"input" is a tag name,(optional) 

#tag & class  syntax: tagname.valueofclass
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")   #inputtext _55r1 _6luy [sometimes classname not taken after space (inputtext "_55r1 _6luy").
#driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc@gmail.com")  #tag name is optional

#tag & attributes  syntax: tagname[attribute=value] double qoutes is not requird
#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abc@gmail.com") 
driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("abc@gmail.com")

#tag , class & attribute  syntax: tagname.valueofclass[attribute=value]
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("xyz")


time.sleep(3000)
driver.close()
