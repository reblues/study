#!/user/bin/env python
# -*- coding:utf-8 -*-
import unittest
import HTMLTestRunner
import time
from public import dataRead
from test_case_wx import test_case_buy


allCaseName = [
    test_case_buy.case_Search
]
teseunit = unittest.TestSuite()


#确定要运行的case
strCase = dataRead.read_data()

lens = len(strCase)
for case in allCaseName:
    strCaseName = str(case).split('\'')[1]
    for i in range(lens):
        if strCase[i] == strCaseName:
            print i
            teseunit.addTest(unittest.makeSuite(case))

now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))


filename = 'E:\\study\\weixin\\result\\' + now + 'resule.HTML'
fp = file(filename, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'测试报告',
    description=u'用例执行情况:'
)

runner.run(teseunit)
fp.close()