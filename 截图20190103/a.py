from selenium import webdriver

import time
url_login = "https://passport.cnblogs.com/user/signin"
driver = webdriver.Chrome()
driver.get(url_login)
try:
    driver.find_element_by_id("input1").send_keys(u"上海-悠悠")
    driver.find_element_by_id("input2").send_keys("xxx")
    #登录id是错的，定位会抛出异常
    driver.find_element_by_id("signin1").click()
except Exception as msg:
    print(u"异常原因 %s"%msg)
    #图片名称可以加个时间戳
    nowTime = time.strftime("%Y%m%d.%H.%M.%S")
    t = driver.get_screenshot_as_file("%s.jpg" % nowTime)
    print(u"截图结果: %s"%t)
    driver.close()
