#!/user/bin/env python
# -*- coding:utf-8 -*-
import unittest
from appium import webdriver
from time import sleep



class case_Send(unittest.TestCase):

    def setUp(self):
        print("set up env for android testing...")
        self.desired_caps = {
            'platformName': 'Android',
            'platformVersion': '5.1.1',
            'deviceName': 'KIW-TL00',
            'browserName': '',
            'appPackage': 'com.geometry',
            'appActivity': '.activity.StartActivity',
            'unicodeKeyboard': 'true',
            'resetKeyboard': 'true'
        }
        self.driver = webdriver.Remote(command_executor='http://localhost:4723/wd/hub', desired_capabilities=self.desired_caps)
        self.driver.implicitly_wait(30)
        #self.driver.get('http://baidu.com')

    def tearDown(self):
        print("clean up the settings...")
        self.driver.quit()

    def test_send(self):
        u'''登陆登出'''
        sleep(10)



if __name__ == '__main__':
    unittest.main()
