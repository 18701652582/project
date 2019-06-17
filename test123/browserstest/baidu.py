#encoding:utf-8
'''
@projrct = project
@file = baidu
@author = Administrator
@create_time = 2019/6/13 9:52
'''


from test123.browserstest.CallingDifferentBrowsers import *
import os.path
from configparser import ConfigParser
from test123.browserstest.ComputationTime import ComputationTime

@ComputationTime
def baidu(name):
	driver = startBrowser(name)
	driver.get("http://www.baidu.com")
	baidu_title = driver.title
	#print(baidu_title)
	try:
		assert baidu_title == "百度一下，你就知道"
		print("访问百度成功！")
	except Exception as e:
		print("访问百度失败：%s" %e)
	driver.quit()

if __name__ == '__main__':
	config = ConfigParser()
	file_path = os.path.dirname(os.path.abspath('.')) + r'\browserstest\browserType.ini'
	print(file_path)

	config.read(file_path)
	names = []
	name1 = config.get("browserType", "browser1")
	name2 = config.get("browserType", "browser2")
	name3 = config.get("browserType", "browser3")
	name4 = config.get("browserType", "browser4")
	name5 = config.get("browserType", "browser5")
	names.append(name1)
	names.append(name2)
	if str(name3).lower() == str(name4).lower() and str(name4).lower() == str(name5).lower():
		#print(1)
		names.append(name3)

	print(names)
	for name in names:
		baidu(name)