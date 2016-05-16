#!/user/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time,unittest,re
import sys
sys.path.append("\public")
from public import login
from public import out


class Weibo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "http://weibo.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    #登录“reblues”
    def test_weibo_login(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)

        login.Login(self)

        out.Out(self)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

    if __name__ == "__main__":
        unittest.main


