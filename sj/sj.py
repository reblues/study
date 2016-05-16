#coding:utf-8
import unittest
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class MyTestCase(unittest.TestCase):

    def setUp(self):
        print("set up env for android testing...")
        self.desired_caps = {
            'platformName': 'Android',
            'platformVersion': '4.4',
            'deviceName': 'Android Emulator',
            'browserName': '',
            'appPackage':'com.wedo.dealer',
            'appActivity':'.activity.DealerLoginActivity'
        }
        self.driver = webdriver.Remote(command_executor='http://localhost:4723/wd/hub', desired_capabilities=self.desired_caps)
        self.driver.implicitly_wait(30)
        #self.driver.get('http://baidu.com')

    def tearDown(self):
        print("clean up the settings...")
        self.driver.quit()

    def test_android(self):
        #登陆

        self.driver.find_element_by_id("com.wedo.dealer:id/username").send_keys(u"18710924623")
        self.driver.find_element_by_id("com.wedo.dealer:id/password").send_keys(u"123456")
        self.driver.find_element_by_id("com.wedo.dealer:id/nextBtn").click()
        print 'login'
        sleep(5)
        #self.driver.swipe(500, 1000, 500, 200, 800)
        #sleep(5)




        #滑动


        self.driver.find_element_by_id("com.wedo.dealer:id/rb3").click()
        self.driver.find_element_by_id("com.wedo.dealer:id/btn_hotSell").click()
        sleep(3)
        self.driver.swipe(914, 365, 400, 365, 500)
        print 'swipe'

        try:

            self.driver.find_element_by_xpath("/android.widget.FrameLayout[0]/android.view.View/android.widget.FrameLayout[1]/android.widget.LinearLayout[0]/android.widget.ListView[0]/android.widget.FrameLayout[0]/android.widget.LinearLayout[1]/android.widget.LinearLayout[0]/android.widget.ImageView[contains(@index,'0')]").click()
            print 'delete2'
            sleep(5)
        except Exception, e:
            print e


        try:
            self.driver.find_element_by_id("com.wedo.dealer:id/certain").click()
            print 'delete3'
            sleep(3)
        except Exception, e:
            print e


        finally:
            self.driver.find_element_by_id("android:id/up").click()
            print 'delete5'


            #self.driver.find_element_by_id("android:id/up").click()
            #退出
            self.driver.find_element_by_id("com.wedo.dealer:id/rb3").click()
            sleep(3)
            self.driver.swipe(500, 1000, 500, 200, 800)
            login = self.driver.find_element_by_id('com.wedo.dealer:id/logout')
            login.click()
            sleep(3)
            print 'logout'



if __name__ == '__main__':
    unittest.main()
