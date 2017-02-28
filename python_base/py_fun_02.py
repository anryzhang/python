# coding:utf-8

mylist = [1, 2, 3, 4, 5]


def change_list(list):
    newlist = []
    for i in list:
        newlist.append(i + 10)
    return newlist


    # for i in xrange(len(list)):
    #     list[i] += 10
    # return list


newList = change_list(mylist)

print (newList)

print mylist

print id(newList)
print id(mylist)
