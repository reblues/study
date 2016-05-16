#!/user/bin/env python
# -*- coding:utf-8 -*-

from time import sleep


def orderCommit(object):

    str = len(object)
    for i in range(str):
        send = object[i]
        if object[i].text:
            print object[i].text
            sleep(3)
        else:
            print 'not found'
            sleep(3)
    #print [object[i].text for i in range(len(object)) if object[i].text]



def forSearch(id,name):

    #在多个相同id的路径中选出需要的，id为路径，name为需要选出来的text名称
    ids = id
    for i in ids:
        if i.text == name:
            i.click()
            break










