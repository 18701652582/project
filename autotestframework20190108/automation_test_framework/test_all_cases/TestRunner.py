

#coding=utf-8

import HTMLTestRunner
import unittest
import time


# 用例路径
case_path = r"D:\PyCharm2018\project\autotestframework20190108\automation_test_framework\testsuites"
# 报告存放路径
report_path = r"D:\PyCharm2018\project\autotestframework20190108\automation_test_framework\report"

def createsuite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path,pattern='test_*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit
if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
    filename = report_path + '/result_' + now + '.html'
    fp = open(filename, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'功能测试报告',
        description=u'用例执行情况：')
    runner.run(createsuite())


    #关闭文件流，不关的话生成的报告是空的
    fp.close()



