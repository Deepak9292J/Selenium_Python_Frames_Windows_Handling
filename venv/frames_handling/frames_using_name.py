from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://learn.letskodeit.com/p/practice")

#Switching to frame with the help of iframe name.
driver.switch_to.frame("iframe-name")
driver.find_element_by_id("search-courses").send_keys("python")

driver.switch_to.default_content()
driver.find_element_by_xpath("//input[@id='name']").send_keys("Success switch")
