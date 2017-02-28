# coding:utf-8
from Student import Student

student = Student('dd');
print student.getName()

if __name__ == '__main__':
    student.setName('ss')
    print student.getName()

    print range(0, 10, 2)

print "=" * 60

import random


def compareNum(num1, num2):
    if (num1 > num2):
        return 1
    elif (num1 == num2):
        return 0
    else:
        return -1


num1 = random.randrange(1, 9)
num2 = random.randrange(1, 9)

print "num1 = ", num1
print "num2 = ", num2

print compareNum(num1, num2)
