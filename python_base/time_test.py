# coding:utf-8

import time

timer = time.time()
print timer

print '='*10
pass

localTime = time.localtime()

print (localTime)

print '格式化时间='*3

print time.strftime("%Y-%m-%d %H:%M:%S", localTime)

print '日历模块'

import calendar

cal = calendar.month(2017,2)
print cal

print dir(time)