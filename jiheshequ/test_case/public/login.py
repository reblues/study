#coding:utf-8

import os
import time
from test_case.orderObject.loginObject import loghomeObject
from test_case.orderObject.loginObject import loginObject
from test_case.orderObject.loginObject import loginData
from test_case.orderObject.loginObject import logoutObject
from selenium.webdriver.common.keys import Keys


def Login(self):
    #录入数据
    loginData(self)

    #进入“注册登录”主页面
    time.sleep(3)
    loghomeObject(self)
    self.loghomeButton.click()
    time.sleep(3)
    self.loginButton.click()
    time.sleep(3)

    #进入登陆页面
    loginObject(self)
    self.passNameButton.click()
    self.passNameButton.send_keys(self.passName)
    self.passKeyButton.click()
    self.passKeyButton.send_keys(self.passKey)
    #self.acceptButton.click()
    self.loginButton.click()
    time.sleep(10)

    #此处加上检测登录是否成功的代码
    loghomeObject(self)
    if self.loginButton.text == self.userName:
        print 'login sucess'
    time.sleep(5)


def Logout(self):
    #进入“退出登录”主页面
    loghomeObject(self)
    self.loghomeButton.click()
    time.sleep(3)
    self.loginButton.click()
    time.sleep(3)

    #进入退出登陆页面
    logoutObject(self)
    self.logoutButton.click()
    print 'logout sucess'


