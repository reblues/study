#!/user/bin/env python
# -*- coding:utf-8 -*-
import unittest
import time
import HTMLTestRunner
from test_case.data_read import readExcle

#导入case
from test_case import case_login, case_search




#将用例组装数组
allCaseNames = [
    case_login.case_Login,
    case_search.case_Search

]


#创建测试套件
testunit = unittest.TestSuite()


#循环读取数组中的用例
strCases = readExcle()
lenth = len(strCases)
for case in allCaseNames:
    strCaseName = str(case).split('\'')[1]
    for i in range(lenth):
        if strCases[i] == strCaseName:
            print i
            testunit.addTest(unittest.makeSuite(case))


#取前面时间
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))


#定义报告存放路径
filename = 'E:\\study\\jiheshequ\\result\\' + now + 'result.html'
fp = file(filename, 'wb')


runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'几何社区测试报告',
    description=u'用例执行情况：'
)


#执行用例
runner.run(testunit)
fp.close()


