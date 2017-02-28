#coding:utf-8

def outer(func):

    def inner():
        print "test"
        func()
        print 'ts'

    return inner

@outer
def foo():
    print 'in foo'

foo()

