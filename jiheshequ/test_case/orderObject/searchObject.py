#!/user/bin/env python
# -*- coding:utf-8 -*-
'''地址定位和商品购买'''


#首页元素
def homeObject(self):
    self.searchHome = self.driver.find_element_by_id('com.geometry:id/home_tab')
    self.searchTitleAddress = self.driver.find_element_by_id('com.geometry:id/locationText')
    self.searchGoods = self.driver.find_element_by_id('com.geometry:id/searcher')


#地址搜索
def searchAddressObject(self):
    self.searchAddress = self.driver.find_element_by_id('com.geometry:id/searchET')


#选择地址
def addressAccept(self):
    self.chooseAddress = self.driver.find_elements_by_id('com.geometry:id/addressDetilTV')


#搜索商品
def searchGoodsObject(self):
    self.searchTitleGoods = self.driver.find_element_by_id('com.geometry:id/searchEdit')
    self.searchAccept = self.driver.find_element_by_id('com.geometry:id/searchTv')


#搜索商品列表
def GoodsObject(self):
    self.goodAccept = self.driver.find_elements_by_xpath('//android.widget.ListView/android.widget.LinearLayout')


#搜索页面购物车
def cart(self):
    self.cart = self.driver.find_element_by_id('com.geometry:id/bot_cart_container')


#数据
def searchData(self):
    self.address = u"下梅林"
    self.addressAccept = u'福田区福田梅山路与梅林路交汇处'
    self.goods = u'面'
    self.goodsAccept = u'康师傅酸菜牛肉面550ML*12[美宜家便利店]'
    self.goodsName = 'com.geometry:id/productName'
    self.goodsButton ='com.geometry:id/addToCartBtn'