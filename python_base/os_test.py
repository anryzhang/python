# coding:utf-8
import os

print dir(os)

# os.remove('test_rename.txt')
os.rename('test.txt', 'test_rename.txt')

print '重命名文件成功'
