from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)

# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("02/22/2022")  #mm/dd/yyyy

year="2022"
month="February"
date="22"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break
    else: 
        # driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click()  #next arrow
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click()  #previous arrow

dates=driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break


time.sleep(30)
driver.quit()