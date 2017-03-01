# coding:utf-8
class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1*6

    def displayCount(self):
        print "total Employee %d" %Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ', salary: ', self.salary


emp1 = Employee('zara',2000)

emp2 = Employee('manni',5000)

emp1.displayCount()
emp1.displayEmployee()

emp1.age = 26

print '='*10

emp2.displayCount()
emp2.displayEmployee()

print hasattr(emp1,'age')

print hasattr(emp2,'age')

setattr(emp1,'age',30)

print emp1.age

print '类变量,可以内部类或外部类使用'

print 'total Employee %d' %Employee.empCount

