#!/user/bin/env python
# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from object import objectAddress
from object import objectGoods


def searchAddress(self):
    objectAddress.allData(self)
    sleep(20)
    #self.driver.switch_to.context('WEBVIEW_1')
    objectAddress.objectHome(self)
    self.homeKey.click()
    #self.driver.find_element_by_xpath('.//*[@id="home_btn"]/div/button').click()
    self.addressKey.click()

    #输入地址
    objectAddress.objectAddress(self)
    sleep(5)
    self.sendAddress.send_keys(self.name1)
    sleep(2)
    self.sendAddress.send_keys(self.name2)
    #sleep(2)
    #self.sendAddress.send_keys(self.name3)
    sleep(5)

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



def searchGoods(self):
    objectGoods.allData(self)
    sleep(10)
    #self.driver.switch_to.context('WEBVIEW_1')
    objectAddress.objectHome(self)
    self.searchGoods.click()

    #第一级商品列表
    sleep(5)
    objectGoods.objectGoodList1(self)
    for l in self.top_goodlist:
        if l.text == self.goodList1:
            print l.text
            l.click()
            break

    #第二级商品列表
    sleep(5)
    objectGoods.objectGoodList2(self)
    for s in self.sec_goodlist:
        if s.text == self.goodList2:
            print s.text
            s.click()
            break

    #选择商品添加购物车
    sleep(5)
    '''
    self.driver.find_element_by_xpath("html/body/ion-nav-view/div/ion-tabs/ion-nav-view[2]/div/ion-view/div[2]/ion-content/div/div[2]/ul/li[4]/div/div[2]/div[3]/div[2]/div/div/span/em").click()
    '''
    objectGoods.objectGood(self)
    print len(self.goodChoose)
    for good in self.goodChoose:
        if good.find_element_by_class_name('font-two-line-ellipsis').text == self.goodAccept:
            print good.find_element_by_class_name('font-two-line-ellipsis').text
            sleep(2)
            good.find_element_by_tag_name('span').click()
            print 'add'
            sleep(5)
            break



