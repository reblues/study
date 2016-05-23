#!/user/bin/env python
# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from object import objectLogin
from object import objectAddress

def Login(self):
    sleep(10)
    #self.driver.switch_to.context('WEBVIEW_1')

    objectLogin.allData(self)
    '''
    objectAddress.homeButton(self)
    self.loginKey.click()
    sleep(3)
    objectLogin.objectLoginHome(self)
    self.logKey.click()
'''
    #填写账号密码
    objectLogin.objectLog(self)
    self.loginName.send_keys(self.logName)
    sleep(2)
    self.number.click()
    sleep(2)
    self.loginPass.send_keys(self.logPass)
    sleep(2)
    self.logButton.click()
    sleep(5)
'''
    #验证登陆
    objectLogin.objectLoginHome(self)
    if self.logKey.text == self.nameAccess:
        print self.logKey.text + '  login'
    objectAddress.homeButton(self)
    self.buttonHomeKey.click()
    '''



def Logout(self):
    #退出登陆
    sleep(5)
    objectAddress.objectHome(self)
    self.loginKey.click()
    sleep(2)
    objectLogin.objectLoginHome(self)
    self.logKey.click()
    sleep(2)
    objectLogin.objectLogout(self)
    self.logOut.click()
    print 'logout'

