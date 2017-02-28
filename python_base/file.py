# coding:utf-8

fo = open('foo.txt', 'ab+')

print '文件名:', fo.name

print "是否已经关闭: ", fo.closed

print "访问模式: ", fo.mode

fo.write('test word\n')

fo.close()

fo2 = open('foo.txt', 'r')

str = fo2.read()

print str

fo2.close()
