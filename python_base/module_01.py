# coding:utf-8
import return_fun

return_fun.sum(1, 5)

return_fun.total = return_fun.sum(6, 6);

print return_fun.total;

print '='*10

Moner = 200

def addMoney():

    global  Moner
    Moner = Moner + 1


print Moner

addMoney()
print Moner