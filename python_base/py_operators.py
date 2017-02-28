# coding:utf-8
a = 21
b = 10
c = 0

c = a + b

print '1 - c 的值:', c

print a // b

print a <> b
print a != b

print a & b
print 'test'
print a and b

print a or b

print a | b

print a ^ b

print ~a
print ~b

print a << 2

print '-- ' * 10

a = 10

b = 20

list = [1, 2, 3, 4, 5, 6, 7]

# 成员运算符
if (a in list):
    print 'a  在list 中'
else:
    print 'a 不在 list 中'

if (b not in list):
    print 'b 不在 list中'
else:
    print 'b在 list 中'

print '__ ' * 10

# 身份运算
a = 20
b = 20

if(a is b):
    print 'a 和 b 有相同的标识'

if(id(a) == id(b)):
    print 'a 和 b 的地址相同'

b = 30

if(a is not b):
    print a ,'和', b ,'a b 没有相同的标识'

print '__ ' * 10

