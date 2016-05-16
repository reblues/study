#!/user/bin/env python
# -*- coding:utf-8 -*-
import os
import time
from test_case.orderObject.searchObject import homeObject
from test_case.orderObject.searchObject import searchAddressObject
from test_case.orderObject.searchObject import addressAccept
from test_case.orderObject.searchObject import searchGoodsObject
from test_case.orderObject.searchObject import GoodsObject
from test_case.orderObject.searchObject import cart
from test_case.orderObject.searchObject import searchData
from orderCommit import forSearch
from selenium.webdriver.common.keys import Keys


def searchAddress(self):

    #主页点击地址搜索
    searchData(self)
    homeObject(self)
    self.searchHome.click()
    self.searchTitleAddress.click()

    #输入地址页面
    searchAddressObject(self)
    self.searchAddress.click()
    self.searchAddress.send_keys(self.address)
    time.sleep(5)

    #选择地址
    addressAccept(self)
    forSearch(self.chooseAddress, self.addressAccept)
    time.sleep(5)

    #验证地址
    if self.searchTitleAddress.text == self.address:
        print self.address + 'address sucess'
    time.sleep(5)


def searchGoods(self):

    #数据导入
    searchData(self)
    #主页搜索按钮
    homeObject(self)
    self.searchHome.click()
    self.searchGoods.click()

    #搜索商品
    searchGoodsObject(self)
    searchData(self)
    self.searchTitleGoods.send_keys(self.goods)
    self.searchAccept.click()
    time.sleep(3)

    #添加要选择的商品
    GoodsObject(self)
    goods = self.goodAccept
    for good in goods:
        if good.find_element_by_id(self.goodsName).text == self.goodsAccept:
            good.find_element_by_id(self.goodsButton).click()
            print good.find_element_by_id(self.goodsName).text + ' add sucess'
            break
    time.sleep(3)
    #进入购物车
    cart(self)
    self.cart.click()
    time.sleep(5)

