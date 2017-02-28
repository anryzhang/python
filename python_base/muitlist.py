# coding:utf-8

item_one = 1
item_two = 2
item_three = 3

total = item_one + \
        item_two + \
        item_three

print total

a = b = c = 1
print a

print b

print c

print "=" * 30

b = 2

print a

print b

print c

print '=' * 30

dd = 'test'

print dd.__len__()

print dd[1:dd.__len__()]

print '列表操作 == ' * 5

list = ['a', 1, 4, 5]
tlist = [123, 678]

print list

print list[2]

print list * 2

print list + tlist

print '元组 == ' * 5

tuples = ('1', 'a', 1, 4, 6)
tuple2 = (123, 453)

print tuples

print tuples[2]

print tuples * 2

print tuples + tuple2

print '元字典 == ' * 5

dicts = {}

dicts['list'] = list

dicts['tuple'] = tuples

print dicts

print dicts['list']

print dicts['tuple']

print dicts.keys()

print dicts.values()

print '数据类型转换 == ' * 5

print int(a)
print long(a)
print float(a)
print complex(a)

print str(a)
print repr(a)

print tuple(list)

print dict(dicts)
