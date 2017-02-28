#coding:utf-8

count = 0
while (count < 9 ):
    print '当前count是:' , count
    count += 1

print '== ' * 10

i = 1

while i < 10:
    i += 1;
    if i%2 > 0:
        print i
        continue
    else:
        print '条件不成立时:' , i

print '== ' * 10

i = 1
while 1:
    print i
    i += 1
    if i > 10:
        print '条件成立,跳出while'
        break

print '== ' * 10

var = 1

while var == 1:
    num =  raw_input('输入一个数字:')
    print '你输入的数字是:', num
    print type(num)
    if num == str(10):
        print '你输入正确了,游戏结束'
        break
    print 'test'






