# coding:utf-8

"""
嵌套函数
"""


def outer():
    def inner():
        print 'inner'

    return inner


p = outer()

# print type(p)

p()

print "== " * 10


def printInfo(arg1, *var):
    print "输出:", arg1

    for i in var:
        print 'test:', i

    return


printInfo(70, 10, 30)

print '== ' * 10

sum = lambda arg1, arg2: arg1 + arg2

print '相加后的值' , sum(10,20)

print '== ' * 10

Money = 200
def addMoney():
    global  Money
    Money = Money + 1

print Money

addMoney()

print Money