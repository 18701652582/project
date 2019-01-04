import time

from selenium import webdriver


time.sleep(1)
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()
driver.close()
