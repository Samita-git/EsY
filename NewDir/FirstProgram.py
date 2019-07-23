import time

from selenium import webdriver

driver = webdriver.Chrome("../driverdetails/chromedriver.exe")

driver.get("https://www.google.com/")

driver.set_page_load_timeout(10)

driver.maximize_window()

driver.find_element_by_name("q").send_keys("Search")

time.sleep(10)

driver.find_element_by_name("btnk").click()

print("Search on google done successfully")

driver.close()

driver.quit()

time.sleep(2)

print("my first program executed successfully")



