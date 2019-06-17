#encoding:utf-8
'''
@projrct = project
@file = ComputationTime
@author = Administrator
@create_time = 2019/6/17 16:36
'''
import time

#定义一个装饰器，计算启动浏览器访问网址到浏览器退出的时间
def ComputationTime(func):
	def showTime(name):
		start_time = time.time()
		func(name)
		end_time = time.time()
		print('spend is {}'.format(end_time - start_time))
		print("quit the browser name: %s" %name)
		print("####################")
	return showTime