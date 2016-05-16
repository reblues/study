#!/user/bin/env python
# -*- coding:utf-8 -*-
'''订单确认页面元素'''


def odrerObject(self):
    self.objOrderTitle = self.driver.find_element_by_id('com.geometry:id/tv_title')
    self.objOrderSendMean1 = self.driver.find_element_by_id('com.geometry:id/rb_order_ensure_deliver')
    self.objOrderSendMean2 = self.driver.find_element_by_id('com.geometry:id/rb_order_user_talk')
    self.objOrderSendTime1 = self.driver.find_element_by_id('com.geometry:id/tv_immedi_send_time')
    self.objOrderSendTime2 = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'定时送')]")
    self.objOrderPayWay1 = self.driver.find_element_by_id('com.geometry:id/tv_balance_desc')
    self.objOrderPayWay2 = self.driver.find_element_by_id('com.geometry:id/rbtn_ensure_order_online_payway')
    self.objOrderPayWay3 = self.driver.find_element_by_id('com.geometry:id/rbtn_ensure_order_offline_payway')
    self.objOrderMoney1 = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'合计:')]")
    self.objOrderMoney = self.driver.find_element_by_id('com.geometry:id/tv_cart_order_payAmount')
    self.objOrderSendPay = self.driver.find_element_by_id('com.geometry:id/tv_cart_expressDesc')
    self.objOrderCommit = self.driver.find_element_by_id('com.geometry:id/btn_commit_order')
    self.order1 = (self.objOrderTitle, self.objOrderSendMean1, self.objOrderSendMean2, self.objOrderSendTime1, self.objOrderSendTime2, self.objOrderPayWay1, self.objOrderPayWay2, self.objOrderPayWay3, self.objOrderMoney1, self.objOrderMoney, self.objOrderSendPay, self.objOrderCommit)



