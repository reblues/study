#!/user/bin/env python
#  -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def objectGoodList1(self):
    self.top_goodlist = self.driver.find_elements_by_xpath(".//*[@id='productCategorys']/div/div")

def objectGoodList2(self):
    self.sec_goodlist = self.driver.find_elements_by_xpath(".//*[@id='productSecCategorys']/div/div[4]/ion-item")

def objectGood(self):
    self.goodChoose = self.driver.find_elements_by_xpath("html/body/ion-nav-view/div/ion-tabs/ion-nav-view[2]/div/ion-view/div[2]/ion-content/div/div[2]/ul/li")





def allData(self):
    self.goodList1 = u'休闲食品'
    self.goodList2 = u'休闲零食'
    self.goodAccept = u'傻二哥黑米锅巴(香辣味)100G'
