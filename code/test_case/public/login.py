#!/user/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time


def Login(self):
    driver = self.driver
    driver.maximize_window()
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id='pl_login_form']/div[2]/div[1]/div/a[2]").click()
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id='pl_login_form']/div[2]/div[3]/div[1]/div/input").send_keys("534948651@qq.com1")
    driver.find_element_by_xpath(".//*[@id='pl_login_form']/div[2]/div[3]/div[1]/div/input").send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath(".//*[@id='pl_login_form']/div[2]/div[3]/div[2]/div/input").send_keys("xdsir9351.")
    driver.find_element_by_xpath(".//*[@id='pl_login_form']/div[2]/div[3]/div[6]/a").click()
    print "登录成功"


