#!/user/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time,unittest,re


def sendMail(self):
    driver = self.driver
    time.sleep(2)
    #进入写信页面
    span = driver.find_element_by_class_name("oz0")
    for sp in span:
        if sp.text = u'写信':
            sp.click()

    #填写收件人信息
    driver.find_element_by_class_name("nui-editableAddr-ipt").send_keys("reblues@163.com")
    driver.find_element_by_class_name("nui-ipt-input").send_keys("hello")
    time.sleep(2)

    #富文本
    driver.switch_to_frame("driver.find_elements_by_tag_name("iframe")[4]")




