#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
迭代的概念: 重复+上一次迭代的结果为下一次迭代的初始值
重复的过程称为迭代，每次重复即一次迭代，并且每次迭代的结果是下一次迭代的初始值

"""
# while True: #只满足重复，因而不是迭代
#     print('====>')

#迭代
l = [1, 2, 3]
count = 0
while count < len(l):
    print('====>', l[count])
    count += 1

# 字符串、列表、元组有下标
# 字典、元组无下标

# 为什么要有迭代器？对于没有索引的数据类型，必须提供一种不依赖索引的迭代方式

# 可迭代的对象，具有__iter__()方法
[1, 2].__iter__()
'hello'.__iter__()
(1, 2).__iter__()
{'a': 1, 'b': 2}.__iter__()
{1, 2, 3}.__iter__()
f = open('a.txt', 'w', encoding='utf')
f.__iter__()

# 迭代器：执行__iter()__方法，得到的结果就是迭代器
i = [1, 2, 3, 4, 5].__iter__()
print(i)
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
# print(i.__next__()) # 抛出异常：StopIteration

dic = {'a': 1, 'b': 2}
i = dic.__iter__()
while True:
    try:
        key = i.__next__()
        print(dic[key])
    except StopIteration:
        break

"""
s = 'hello'
len(s) <===> s.__len()__

iter(s) <===> s.__iter__()
next(s) <===> s.__next__()
"""

# 如何判断一个对象是可迭代的对象，还是迭代器对象
from collections import Iterable, Iterator

# 下列数据类型是可迭代的对象
print(isinstance('abc', Iterable))
print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({'a': 1}, Iterable))
print(isinstance({1, 2}, Iterable))
print(isinstance(f, Iterable))

# 下列数据类型是可迭代器对象
print(isinstance('abc', Iterator))
print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance({'a': 1}, Iterator))
print(isinstance({1, 2}, Iterator))
print(isinstance(f, Iterator))  # True
# f.__next__() # f具有__next__()方法，就是可迭代对象

"""
可迭代对象：只有__iter__()方法，执行该方法得到迭代器对象

迭代器协议：
    对象有__next__()方法
    对象有__iter__()方法，对于迭代器对象来说，执行__iter__()方法，结果任然是它本身

为了符合for循环资本原理，无论时可迭代对象还是迭代器执行__iter__()方法，都会生成迭代器
for循环就是迭代循环
"""
f1 = f.__iter__()
print(f1 is f)  # True

dic = {'a':1, 'b': 1}
for k in dic:   # i=iter(dic)  k=next(i) for循环本质遍历迭代器
    print(k)

"""
迭代器的优点和缺点
优点：
    1. 提供了一种不依赖下标的迭代方式
    2. 就迭代器本身来说，更节省内存
缺点：
    1. 无法获取迭代器对象的长度
    2. 不如序列类型灵活，是一次性的，只能往后取值，不能往前退


"""
# 假设a.txt是几个G的文件
f = open('b.txt', 'r', encoding='utf-8')

# 一次性把文件调入到内存中，效率太低
# for line in f.readlines():
#     print(line)

# 文件本身就是迭代器
print(next(f),end='')
print(next(f),end='')

for line in f:
    print(line, end='')
print()
print('==============,分隔符，迭代器 f 是一次性的')
for line in f:
    print(line, end='')


# 补充
i = enumerate([1, 2, 3, 4])
i.__iter__()
i.__next__() # (0, 1)
# enumerate 是迭代器
print(next(i))
print(next(i))
print(next(i))