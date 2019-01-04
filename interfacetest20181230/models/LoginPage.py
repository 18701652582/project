# coding=utf-8
from interfacetest20181230.models.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
	'''
			登录页面的登录窗口
	'''
	user_name = (By.NAME, "username")
	pass_word = (By.NAME, "password")
	btn_login = (By.CLASS_NAME, "login-btn")

	def __init__(self, driver):
		BasePage.__init__(self, driver)
		self.driver = driver
		self.input_username = self.find_element(*self.user_name)
		self.input_password = self.find_element(*self.pass_word)
		self.btn_login = self.find_element(*self.btn_login)

	def login(self, username, password):
		self.input_username.send_keys(username)
		self.input_password.send_keys(password)
		self.btn_login.click()