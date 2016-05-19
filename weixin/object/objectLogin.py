#!/user/bin/env python
# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def objectLoginHome(self):
    self.logKey = self.driver.find_element_by_class_name('ucenter-username')


def objectLog(self):
    self.loginName = self.driver.find_element_by_xpath('html/body/ion-nav-view/div[2]/ion-view/ion-content/div/form/div[1]/input')
    self.number = self.driver.find_element_by_xpath('html/body/ion-nav-view/div[2]/ion-view/ion-content/div/form/div[2]/a')
    self.loginPass = self.driver.find_element_by_xpath('html/body/ion-nav-view/div[2]/ion-view/ion-content/div/form/div[2]/input[1]')
    self.logButton = self.driver.find_element_by_xpath('html/body/ion-nav-view/div[2]/ion-view/ion-content/div/form/div[5]/button')


def objectLogout(self):
    self.logOut = self.driver.find_element_by_xpath(".//*[@id='profile']/div[4]")


def allData(self):
    self.logName = u'18710924623'
    self.logPass = u'1234'
    self.nameAccess = u'啦啦啦'