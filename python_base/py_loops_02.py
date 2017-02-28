#coding:utf-8
for le in 'python':
    print le

print '== ' * 10

fr = [1,2,3,4]

for i in fr:
    print i

print '== ' * 10


fr = ['a','b','c']

for index in range(len(fr)):
    print fr[index]


print '== '* 10


for num in range(10,20):
    for i in range(2,num):
        if(num % i == 0):
            j = num/i
            print '%d 等于 %d * %d ' %(num,i,j)
            break
    else:
        print num, '是一个质数'

print '== ' * 10




