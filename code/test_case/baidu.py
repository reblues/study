#!/user/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time,unittest,re


class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    #搜索
    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        time.sleep(2)

        driver.find_element_by_xpath(".//*[@id='kw']").send_keys(u"百度")
        driver.find_element_by_xpath(".//*[@id='su']").click()
        time.sleep(3)
        print "搜索成功"

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

    if __name__ == "__main__":
        unittest.main
