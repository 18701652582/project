# coding=utf-8
from interfacetest20181230.models.BasePage import BasePage
from selenium.webdriver.common.by import By


class Index(BasePage):
	'''
			首页
	'''
	user_menu = (By.ID, "userSetting")
	user_info = (By.XPATH, "//a[@href='user/userInfo']")
	language_span = (By.ID, "changeLanguage")
	chinese_li = (By.XPATH, "//li[@value='zh_cn']")
	english_li = (By.XPATH, "//li[@value='en']")

	def __init__(self, driver):
		BasePage.__init__(self, driver)
		self.driver = driver
		self.usermenu = self.find_element(*self.user_menu)
		self.userinfo = self.find_element(*self.user_info)
		self.languagespan = self.find_element(*self.language_span)
		self.chinase = self.find_element(*self.chinese_li)
		self.english = self.find_element(*self.english_li)

	def chengeLanguage(self):
		self.languagespan.click()
		self.english.click()
		self.driver.implicitly_wait(5)