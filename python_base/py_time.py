#coding:utf-8
import  time

import datetime

ticks = time.time()

print ticks
print int(ticks)*1000
print time.mktime(time.localtime())
print datetime.datetime.now().microsecond

print '-- ' * 10

print time.localtime(ticks)

print time.asctime(time.localtime())

print time.strftime('%Y-%m-%d %H:%M:S',time.localtime())

print '== ' * 10

import  calendar

cal = calendar.month(2016,6)

print cal


