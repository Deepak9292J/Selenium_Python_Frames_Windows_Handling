from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://learn.letskodeit.com/p/practice")

number_of_frames = driver.find_elements_by_tag_name("iframe")
print(len(number_of_frames))

driver.switch_to.frame(0)
driver.find_element_by_id("search-courses").send_keys("python")
driver.switch_to.default_content()
driver.find_element_by_xpath("//input[@id='name']").send_keys("Success switch")




