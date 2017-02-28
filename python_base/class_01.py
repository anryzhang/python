# coding:utf-8

class People(object):
    '所有基类'
    empCount = 0

    def __init__(self, Salary='', house=''):
        self.Salary = Salary
        self.house = house

    def distance_from(self):
        if self.Salary > 10000:
            self.house = '可以租住在2环与3环之间'  + str(People.empCount)
            return self.house
        elif 5000 < self.Salary < 10000:
            self.house = '3环到4环'
            return self.house
        elif self.Salary <= 5000:
            self.house = '5环'
            return self.house


sales = People(12000)

print sales.distance_from()

print type(sales)

print  People.__doc__

print People.__name__

print People.__module__

print People.__base__

print People.__dict__

