#!/user/bin/env python
# -*- coding:utf-8 -*-
'''登陆页面元素'''

def loghomeObject(self):
    self.loghomeButton = self.driver.find_element_by_id("com.geometry:id/account_tab")
    self.loginButton = self.driver.find_element_by_id('com.geometry:id/name')

def loginObject(self):
    self.passNameButton = self.driver.find_element_by_id('com.geometry:id/phoneEdit')
    self.passKeyButton= self.driver.find_element_by_id('com.geometry:id/verifyCodeEdit')
    self.acceptButton = self.driver.find_element_by_id('com.geometry:id/eulaCheckBox')
    self.loginButton = self.driver.find_element_by_id('com.geometry:id/loginBtn')

def logoutObject(self):
    self.logoutButton = self.driver.find_element_by_class_name('android.widget.Button')




def loginData(self):
    self.passName = u'10000000018'
    self.passKey = u'1234'
    self.userName = u"哈哈哈"