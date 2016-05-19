#!/user/bin/env python
# -*- coding:utf-8 -*-
import xlrd

def read_data():
    myfile = xlrd.open_workbook('E:\\study\\weixin\\data\\data.xls')
    table = myfile.sheet_by_name('data')
    valuesRow = table.nrows
    runCase = []
    for i in range(valuesRow):
        if table.cell(i, 0).value == 'Y':
            runCase.append(table.cell(i, 1).value)
    return runCase