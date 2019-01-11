# coding = utf-8
import unittest
import time
from autotestframework20190108.automation_test_framework.framework.HTMLTestRunner import HTMLTestRunner
from autotestframework20190108.automation_test_framework.framework.sendmail import *



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
    runner = HTMLTestRunner(stream=fp, title=u"XXXXX测试报告", description=u"用例执行情况：")

    '''
    	#定时运行脚本
    	k = 1
    	while k < 2:
    		timing = time.strftime('%H_%M', time.localtime(time.time()))
    		if timing == '14_18':  # 14_18指14:18,这个可以根据需要设定时间
    			print('start to run scripts!')
    			runner.run(discover)  # 运行所有的case
    			print('Finish running scripts!')
    			break
    		else:
    			time.sleep(3)
    			print(timing)
    	'''
    runner.run(discover)
    fp.close()

    new_report = new_report(report_path)
    send_mail(new_report)


