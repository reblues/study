#!/user/bin/env python
# -*- coding:utf-8 -*-
import unittest
import os

caselist = os.listdir('E:\\study\\jiheshequ\\test_case')
for a in caselist:
    s = a.split('.')[1]
    if s == 'py':
        os.system('E:\\study\\jiheshequ\\test_case\\%s >>log.txt 2>&1'%a)
