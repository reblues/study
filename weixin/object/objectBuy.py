#!/user/bin/env python
# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep



def objectCart(self):
    self.payKey = self.driver.find_element_by_xpath('html/body/ion-nav-view/div/ion-tabs/ion-nav-view[3]/div/ion-view/div[3]/div/div[2]')

def objectOrder(self):
    self.objectOrder = self.driver.find_element_by_xpath(".//*[@id='confirm_order']/div/div[3]/div")
    self.objectPayWay = self.driver.find_element_by_xpath(".//*[@id='confirm_order']/div/div[11]/div/div[3]/label/input")
    self.objectToPay = self.driver.find_element_by_xpath("html/body/ion-nav-view/div[2]/ion-view/div/div[2]")

def objectChooseaddress(self):
    self.addAddress = self.driver.find_element_by_xpath(".//*[@id='foot']/div/div/button")

def objectAddAddress(self):
    self.addressName = self.driver.find_element_by_xpath(".//*[@id='add_address']/div/div[2]/div/div[2]/input")
    self.addressNew = self.driver.find_element_by_xpath(".//*[@id='add_address']/div/div[7]/div/div[2]/input")
    self.addTel = self.driver.find_element_by_xpath(".//*[@id='add_address']/div/div[4]/div/div[2]/input")
    self.conserve = self.driver.find_element_by_xpath("html/body/ion-nav-view/div[2]/ion-view/ion-header-bar/button")

def cheakout(self):
    self.cheakOrder = self.driver.find_element_by_xpath(".//*[@id='btn2']/div/button")

def orderPage(self):
    self.cheakName = self.driver.find_element_by_xpath("html/body/ion-nav-view/div[5]/ion-view/ion-content/div[1]/div/div[2]/div[2]/div/span[2]")
    self.cheakTel = self.driver.find_element_by_xpath("html/body/ion-nav-view/div[6]/ion-view/ion-content/div[1]/div/div[2]/div[3]/div/span[2]")
    self.cheakAddress = self.driver.find_element_by_xpath("html/body/ion-nav-view/div[6]/ion-view/ion-content/div[1]/div/div[2]/div[4]/div/span[2]")
    self.cheakPayway = self.driver.find_element_by_xpath("html/body/ion-nav-view/div[6]/ion-view/ion-content/div[1]/div/div[2]/div[5]/div/span[2]")
    self.back = self.driver.find_element_by_xpath("html/body/ion-nav-view/div[6]/ion-view/ion-header-bar/a/button")



def allData(self):
    self.addName = u'测试'
    self.allAddress = u'测试测试'
    self.addTel = u'12345678900'
    self.payWay = u'货到付款'

