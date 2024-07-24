from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='dob']").click()

month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
month.select_by_visible_text("Feb")

year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
year.select_by_visible_text("2003")
dates=driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for date in dates:
    if date.text=="22":
        date.click()
        break


time.sleep(30)
driver.quit()