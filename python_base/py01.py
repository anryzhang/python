#coding:utf-8

"""
类里的 self 传入的就是类实例的对象.
"""

class Foo(object):
    def __new__(cls,*args,**kwargs):
        print '先打出来'
        temp = super(Foo,cls).__new__(cls,*args,**kwargs)
        print id(temp)
        return temp

    def __init__(self):
        print 'in __init__() 测试'
        print id(self)


p = Foo()
print id(p)
print dir(p)
