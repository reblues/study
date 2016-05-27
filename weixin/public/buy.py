#!/user/bin/env python
# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from object import objectAddress
from object import objectBuy
from public import cheak


def cartBuy(self):
    objectBuy.allData(self)

    #进入购物车
    objectAddress.homeButton(self)
    self.cartKey.click()
    objectBuy.objectCart(self)
    self.payKey.click()
    sleep(3)


    #订单页面添加地址
    '''
    objectBuy.objectOrder(self)
    self.objectOrder.click()
    sleep(3)
    objectBuy.objectChooseaddress(self)
    self.addAddress.click()
    sleep(3)
    objectBuy.objectAddAddress(self)
    self.addressName.send_keys(self.addName)
    sleep(3)
    self.addTel.send_keys(self.addTel)
    sleep(3)
    self.addressNew.send_keys(self.allAddress)
    self.conserve.click()
    sleep(3)
'''

    #提交订单
    self.driver.swipe(600, 1500, 600, 800, 800)
    objectBuy.objectOrder(self)
    self.objectPayWay.click()
    self.objectToPay.click()
    sleep(3)

    #检查订单
    objectBuy.cheakout(self)
    self.cheakOrder.click()
    cheak.cheakMean(self.cheakName, self.addName)
    cheak.cheakMean(self.cheakTel, self.addTel)
    cheak.cheakMean(self.cheakAddress, self.allAddress)
    cheak.cheakMean(self.cheakPayway, self.payWay)

    #返回
    self.back.click()
    objectAddress.homeButton(self)
    self.buttonHomeKey.click()













