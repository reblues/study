#coding:utf-8

import os
import time
from selenium.webdriver.common.keys import Keys


def Login(self):

    #点击“注册登录”按钮
    passname = u'10000000018'
    passkey = u'1234'
    button = self.driver.find_element_by_id("com.geometry:id/account_tab")
    button.click()
    time.sleep(3)
    login = self.driver.find_element_by_id('com.geometry:id/name')
    login.click()
    time.sleep(3)
    self.driver.find_element_by_id('com.geometry:id/eulaCheckBox').click()

    #登录
    name = self.driver.find_element_by_id('com.geometry:id/phoneEdit')
    name.click()
    name.send_keys(passname)
    psd = self.driver.find_element_by_id('com.geometry:id/verifyCodeEdit')
    psd.click()
    psd.send_keys(passkey)
    blogin = self.driver.find_element_by_id('com.geometry:id/loginBtn')
    blogin.click()
    time.sleep(10)
    #此处加上检测登录是否成功的代码
    getname = self.driver.find_element_by_id('com.geometry:id/name').text
    username = u"哈哈哈"
    if getname == username:
        print u'登陆成功'
    time.sleep(5)


def Logout(self):
    button = self.driver.find_element_by_id("com.geometry:id/account_tab")
    button.click()
    self.driver.find_element_by_id('com.geometry:id/headView').click()
    time.sleep(3)
    self.driver.find_element_by_class_name('android.widget.Button').click()

    print u'退出成功'


