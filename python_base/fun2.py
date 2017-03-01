# coding:utf-8
def ChangeInt(a):
    a = 10

    print a

    return

b = 2
ChangeInt(b)


print b  # 结果是 2


def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print "函数内取值: ", mylist
    return


# 调用changeme函数
mylist = [10, 20, 30];

changeme(mylist);

print "函数外取值: ", mylist

