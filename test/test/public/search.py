#coding:utf-8

import os
import time
from selenium.webdriver.common.keys import Keys


def searchAddress(self):
    #搜索地址
    self.driver.find_element_by_id('com.geometry:id/home_tab').click()
    adNew = self.driver.find_element_by_id('com.geometry:id/locationText')
    adNew.click()
    address = self.driver.find_element_by_id('com.geometry:id/searchET')
    address.click()
    address.send_keys(u"上梅林")
    time.sleep(5)
    self.driver.find_element_by_id('com.geometry:id/titleTV').click()
    time.sleep(5)
    if adNew.text == u"上梅林":
        print 'sucess'
    time.sleep(5)


def searchGoods(self):
    #搜索商品
    self.driver.find_element_by_id('com.geometry:id/home_tab').click()
    self.driver.find_element_by_id('com.geometry:id/searcher').click()
    self.driver.find_element_by_id('com.geometry:id/searchEdit').send_keys(u'冰泉')
    self.driver.find_element_by_id('com.geometry:id/searchTv').click()
    self.driver.find_element_by_id('com.geometry:id/addToCartBtn').click()
    self.driver.find_element_by_id('com.geometry:id/bot_cart_container').click()
    self.driver.find_element_by_id('com.geometry:id/btn_commit_order').click()
    print 'ok'
    time.sleep(5)
