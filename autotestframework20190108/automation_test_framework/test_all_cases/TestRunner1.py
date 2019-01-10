# coding = utf-8
import unittest
import time
from autotestframework20190108.automation_test_framework.framework.HTMLTestRunner import HTMLTestRunner




# 用例路径
case_path = r"D:\PyCharm2018\project\autotestframework20190108\automation_test_framework\testsuites"
# 报告存放路径
report_path = r"D:\PyCharm2018\project\autotestframework20190108\automation_test_framework\report"


def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test_*.py", top_level_dir=None)
    print(discover)
    return discover


if __name__ == "__main__":
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py', top_level_dir=None)
    print(discover)

    now = time.strftime("%Y-%m-%d-%H_%M_%S")
    filename = report_path + '/result_' + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例执行情况：")
    runner.run(discover)
    fp.close()


