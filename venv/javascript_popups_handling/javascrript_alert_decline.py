from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://learn.letskodeit.com/p/practice")
driver.find_element_by_xpath("//input[@id='confirmbtn']").click()
time.sleep(3)
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()
driver.close()