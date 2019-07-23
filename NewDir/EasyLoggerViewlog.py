from selenium import webdriver

from selenium.webdriver.support.ui import  Select



import time

driver = webdriver.Chrome("../driverdetails/chromedriver.exe")

driver.maximize_window()

driver.get('https://account.logger.mobi/login')

driver.find_element_by_id('username').send_keys('ranchhod.ramani@pulsesolutions.net')

driver.find_element_by_id('password').send_keys('1234567890')

driver.find_element_by_id('btnSubmit').click()

driver.execute_script("window.scrollTo(0,200)")

driver.find_element_by_xpath('/html/body/section/div[5]/div/div/div/div[4]/div[1]/div/table/tbody/tr[5]/td/a').click()

time.sleep(3)
driver.find_element_by_xpath('/html/body/div[10]/div/div[5]/a[1]').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/section/div[8]/div/div/div/div[6]/div[3]/div/a').click()

select = Select(driver.find_element_by_id('drpDevices'))

# select by visible text
select.select_by_visible_text('Zte')

Display_table = driver.find_element_by_id('sample_6')

print(Display_table .text)


