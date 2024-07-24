from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#count no of rows and columns
rows=driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
columns=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th")
print("No of rows: ",len(rows))
print("No of columns: ",len(columns))

#read specific row and column data
data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]")
print(data.text)

#read all the rows and columns data
# print("All the rows and columns data........")

# for r in range(2,len(rows)+1):
#     for c in range(1,len(columns)+1):
#         data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]")
#         print(data.text,end="       ")
#     print()

#read data based on condition

for r in range(2,len(rows)+1):
    author=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if author=="Mukesh":
        bookname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
        print(bookname,"        ",author,"      ",price)


time.sleep(30)
driver.quit()