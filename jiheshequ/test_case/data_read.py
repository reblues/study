# -*- coding:utf-8 -*-
import xlrd

def readExcle():
    myfile = xlrd.open_workbook('E:\study\jiheshequ\data\data.xls')
    table = myfile.sheet_by_name('data')
    valuesrow = table.nrows
    strCase = []
    for i in range(0, valuesrow):
        if table.cell(i, 0).value == u"Y":
            strCase.append(table.cell(i,1).value)
    return strCase

