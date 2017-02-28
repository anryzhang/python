# coding:utf-8
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount


counter = JustCounter()

counter.count()

counter.count()

print counter.publicCount

# Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问属性，如下代码

print counter._JustCounter__secretCount
