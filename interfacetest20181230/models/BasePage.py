# coding=utf-8
from selenium import webdriver

TIME_OUT = 5  # 超时时间


class BasePage(object):
	def __init__(self, driver):
		"""初始化浏览器"""
		self.driver = driver
		'''
		if driver_type == "ie":
			try:
				self.driver = webdriver.Ie()
			except Exception,e:
				print e
		elif driver_type == "chrome":
			try:
				self.driver = webdriver.Chrome()
			except Exception,e:
				print e
		else:
			try:
				self.driver = webdriver.Firefox()   
			except Exception,e:
				print e
		'''

	def opendriver(self, url):
		self.driver.get(url)
		self.driver.maximize_window()
		self.driver.implicitly_wait(TIME_OUT)

	def find_element(self, by, value):
		"""查找元素"""
		try:
			return self.driver.find_element(by=by, value=value)
		except Exception:
			print("1111")

	def find_elements(self, by, value):
		"""查找元素集合"""
		try:
			return self.driver.find_elements(by=by, value=value)
		except Exception:
			print("222")

	def is_element_isexist(self, By, Value):
		"""判断元素是否存在"""
		try:
			self.driver.find_element(by=By, value=Value)
			return True
		except Exception:
			print("333")
			return False

	def close(self):
		"""当前关闭浏览器tab"""
		try:
			self.driver.close()
		except Exception:
			print("4444")

	def quit(self):
		"""退出浏览器进程"""
		try:
			self.driver.quit()
		except Exception:
			print("5555")