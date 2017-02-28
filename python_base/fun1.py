#coding:utf-8

def test():
    mylist.append([1,2,3])
    print mylist
    return

mylist = []

test()

def printInfo(arg1, *vartuple):
    print arg1

    for var in vartuple:
        print var

    return

printInfo(10)

printInfo(70,60,50)
