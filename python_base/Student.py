#coding:utf-8

class Student:
    __name = ""
    def __init__(self,name):
        self.__name = name

    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name = name

if __name__ == "__main__":
    student = Student('tester')
    print student.getName()

    student.setName('test01')
    print student.getName()