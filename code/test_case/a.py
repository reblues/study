#!/user/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Firefox()
driver.get("http://weibo.com/")
print driver.title
time.sleep(10)

driver.find_element_by_xpath(".//*[@id='pl_login_form']/div[2]/div[1]/div/a[2]").click()
time.sleep(5)

driver.find_element_by_xpath(".//*[@id='pl_login_form']/div[2]/div[3]/div[1]/div/input").send_keys("534948651@qq.com1")
driver.find_element_by_xpath(".//*[@id='pl_login_form']/div[2]/div[3]/div[1]/div/input").send_keys(Keys.BACK_SPACE)
driver.find_element_by_xpath(".//*[@id='pl_login_form']/div[2]/div[3]/div[2]/div/input").send_keys("xdsir9351.")
driver.find_element_by_xpath(".//*[@id='pl_login_form']/div[2]/div[3]/div[6]/a").click()

print "登录成功"
time.sleep(5)
above=driver.find_element_by_xpath(".//*[@id='plc_top']/div/div/div[3]/div[1]/ul/li[2]/a/em[1]")
ActionChains(driver).move_to_element(above).perform()
time.sleep(1)
menu=above.find_element_by_xpath(".//*[@id='plc_top']/div/div/div[3]/div[2]/div[1]/div[1]/ul/li[2]/a")
ActionChains(driver).move_to_element(menu).perform().click()
time.sleep(3)


'''driver.close()'''