#coding:utf-8

fruits = ['banana','apple','mango']
for index in range(len(fruits)):
    print "Current fruits is " + fruits[index]
else:
    print 'no fruits'


print "="*10

for t in fruits:
    print 'current fruits is ' + t

    if t == 'apple':
        print 'my love it ' + t
    else:
        print 'are you love it'
