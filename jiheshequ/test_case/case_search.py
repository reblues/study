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

    def test_search(self):
        u'''搜索地址及商品'''
        sleep(10)
        search.searchAddress(self)
        search.searchGoods(self)
        #self.driver.swipe(500, 1000, 500, 200, 800)

        '''
        self.driver.find_element_by_id('com.geometry:id/cart_tab').click()
        self.driver.find_element_by_id('com.geometry:id/btn_commit_order').click()
        sleep(5)

        #订单确认
        orderCommitObject.odrerObject(self)
        orderCommit.orderCommit(self.order1)
        #try:
        str = len(self.order1)
        for i in range(str):
                send = self.order1[i]
                if self.order1[i].text:
                    print self.order1[i].text
                    sleep(3)
                else:
                    self.driver.swipe(500, 1000, 500, 200, 800)
                    print self.order1[i].text
                    sleep(3)
                #print orderCommit.orderCommit(send,self.name1[i])
                #sleep(3)
                #self.driver.swipe(500, 1000, 500, 200, 800)
        #except Exception, e:
        #    print e

        #finally:
        '''
if __name__ == '__main__':
    unittest.main()
