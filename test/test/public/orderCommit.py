#coding:utf-8

import time

from appium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import os
import time


def orderCommit(object, element):
    if object.text == element:
        equal = 'true'
    else:
        equal = object.text
    return equal


