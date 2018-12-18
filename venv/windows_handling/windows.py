from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://learn.letskodeit.com/p/practice")
parent_handle = driver.current_window_handle
driver.find_element_by_xpath("//button[@id='openwindow']").click()
time.sleep(3)
handles = driver.window_handles
for handle in handles:
    if handle not in parent_handle:
        driver.switch_to.window(handle)
        print(driver.title)
        driver.find_element_by_xpath("//input[@id='search-courses']").send_keys("python")
        time.sleep(3)
        driver.close()
        break

driver.switch_to.window(parent_handle)
print(driver.title)
