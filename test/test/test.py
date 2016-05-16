#coding:utf-8


from appium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import os
import time
from public import login, search, orderCommit
from object import orderCommitObject



class test(unittest.TestCase):

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



    def test_orderConfirm(self):
        time.sleep(10)
        #login.Login(self)
        #search.searchAddress(self)
        #search.searchGoods(self)
        self.driver.find_element_by_id('com.geometry:id/cart_tab').click()
        self.driver.find_element_by_id('com.geometry:id/btn_commit_order').click()


        #订单确认
        orderCommitObject.odrerObject(self)
        orderCommitObject.nameObject(self)
        try:
            for i in range(5):
                send = self.order1[i]
                print orderCommit.orderCommit(send,self.name1[i])
                time.sleep(3)

            self.driver.swipe(500, 1000, 500, 200, 800)
            for j in range(6):
                print self.order2[j].text
        except Exception, e:
            print e

        #finally:
        #    login.Logout(self)




if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(test)

    unittest.TextTestRunner(verbosity=2).run(suite)