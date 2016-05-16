#!/user/bin/env python
# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from public import search


class case_Search(unittest.TestCase):

    def setUp(self):
        print("set up env for android testing...")
        self.desired_caps = {
            'platformName': 'Android',
            'platformVersion': '5.1.1',
            'deviceName': 'KIW-TL00',
            'browserName': '',
            'appPackage': 'com.android.chrome',
            'appActivity': 'org.chromium.chrome.browser.ChromeTabbedActivity',
            'unicodeKeyboard': 'true',
            'resetKeyboard': 'true'
        }
        self.driver = webdriver.Remote(command_executor='http://localhost:4723/wd/hub', desired_capabilities=self.desired_caps)
        self.driver.get('http://release.thy360.com/o2o_weixin/index.html#/tab/platformHome')
        self.driver.implicitly_wait(30)


    def tearDown(self):
        print("clean up the settings...")
        self.driver.quit()


    def test_search(self):
        search.searchAddress(self)




if __name__ == '__main__':
    unittest.main()

