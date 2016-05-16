#!/user/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time,unittest


def Login(self):
    driver = self.driver
    driver.maximize_window()
    target = driver.find_element_by_id("lbNormal")
    ActionChains(driver).move_to_element(target).perform()
    time.sleep(2)

    driver.find_element_by_id("idInput").send_keys("18710924623")
    driver.find_element_by_id("pwdInput").send_keys("yang9351yu")
    driver.find_element_by_id("loginBtn").click()
    time.sleep(2)
    print "登录成功"

def Logout(self):
    driver = self.driver
    time.sleep(2)
    aim = driver.find_element_by_link_text(u"退出")
    print aim.text
    aim.click()
