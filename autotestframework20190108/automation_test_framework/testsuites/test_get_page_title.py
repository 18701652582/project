# coding = utf-8
import unittest

from autotestframework20190108.automation_test_framework.framework.browser_engine import BrowserEngine
from autotestframework20190108.automation_test_framework.pageobjects.baidu_homepage import HomePage


class GetPageTitle(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_get_title(self):

        homepage = HomePage(self.driver)
        print(homepage.get_page_title())