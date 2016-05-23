#!/user/bin/env python
# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


def objectHome(self):
    self.homeKey = self.driver.find_element_by_xpath('html/body/ion-nav-view/div/ion-tabs/div/a[1]')
    self.addressKey = self.driver.find_element_by_xpath('html/body/ion-nav-view/div/ion-tabs/ion-nav-view/div/ion-view/div[1]/div[1]/span')
    self.searchGoods = self.driver.find_element_by_xpath('html/body/ion-nav-view/div/ion-tabs/div/a[2]/i')


def objectAddress(self):
    self.sendAddress = self.driver.find_element_by_id('suggestId')


def addressAccept(self):
    self.allAddress = self.driver.find_elements_by_class_name('lister')

def homeButton(self):
    self.buttonHomeKey = self.driver.find_element_by_xpath('html/body/ion-nav-view/div/ion-tabs/div/a[1]')
    self.cartKey = self.driver.find_element_by_xpath('html/body/ion-nav-view/div/ion-tabs/div/a[4]')
    self.loginKey = self.driver.find_element_by_xpath('html/body/ion-nav-view/div/ion-tabs/div/a[5]')




def allData(self):
    self.name1 = u"上梅"
    self.name2 = u"林"
    #self.name3 = u"林"
    self.findName = u'上梅林\n深圳市福田区'
    self.assureName = u"上梅林"