#coding:utf-8

fo = open('test.txt','r+')

print fo.name

print fo.closed

print fo.mode

print fo.softspace

str = fo.read()

print str

fo.close()

print '== ' * 10

fo = open('test.txt','a+')

fo.write('test write ')

str2 = fo.read()

print str2

print fo.tell()

