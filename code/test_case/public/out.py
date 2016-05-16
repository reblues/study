from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time


def Out(self):
    driver = self.driver
    aim = driver.find_element_by_xpath(".//*[@id='plc_top']/div/div/div[3]/div[2]/div[2]/a/em")
    if aim.is_displayed() == True:
        ActionChains(driver).move_to_element(aim).perform()
        time.sleep(2)
        objQuitName = driver.find_element_by_xpath(".//*[@id='plc_top']/div/div/div[3]/div[2]/div[2]/div/ul/li[9]/a")
        print objQuitName.text

        if objQuitName.is_displayed() == True:
            objQuitName.click()

        else:
            print "error"

    '''aim = driver.find_element_by_xpath(".//*[@id='plc_top']/div/div/div[3]/div[2]/div[2]/a/em")
    ActionChains(driver).move_to_element(aim).perform()
    WebDriverWait(driver, 15).until(driver.find_element_by_xpath(".//*[@id='plc_top']/div/div/div[3]/div[2]/div[2]/div/ul/li[9]/a"))
    driver.find_element_by_xpath(".//*[@id='plc_top']/div/div/div[3]/div[2]/div[2]/div/ul/li[9]/a").click()'''

    #aim = driver.find_element_by_xpath(".//*[@id='plc_top']/div/div/div[3]/div[2]/div[2]/a/em")
    #ActionChains(driver).move_to_element(aim).perform()
    #time.sleep(2)
    #driver.find_element_by_xpath(".//*[@id='plc_top']/div/div/div[3]/div[2]/div[2]/div/ul/li[9]/a").click()
    #print "quit"
