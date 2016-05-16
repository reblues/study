#!/user/bin/env python
# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from object import objectAddress


def searchAddress(self):
    objectAddress.allData(self)
    sleep(30)
    self.driver.switch_to.context('WEBVIEW_1')
    objectAddress.objectHome(self)
    self.homeKey.click()
    #self.driver.find_element_by_xpath('.//*[@id="home_btn"]/div/button').click()
    self.addressKey.click()

    #输入地址
    objectAddress.objectAddress(self)
    self.sendAddress.send_keys(self.name1)
    sleep(2)
    self.sendAddress.send_keys(self.name2)
    sleep(2)
    #self.sendAddress.send_keys(self.name3)
    #sleep(5)

    #选择地址
    objectAddress.addressAccept(self)
    for ad in self.allAddress:
        if ad.text == self.findName:
            ad.click()
            break
    sleep(3)

    #确认地址
    objectAddress.objectHome(self)
    if self.addressKey.text == self.assureName:
        print self.addressKey.text
