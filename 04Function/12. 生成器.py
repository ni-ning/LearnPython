#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
生成器函数：只要函数体包含yield关键字，该函数就是生成器函数
"""


def foo():
    return 1
    return 2
    return 3
    return 4

res1 = foo()
print(res1)  # 1

res2 = foo()
print(res2)  # 1


def foo():
    print('first')
    yield 1
    print('second')
    yield 2
    print('third')
    yield 3
    print('fourth')
    yield 4
    print('fifth')

g = foo() # 生成迭代器，但不会执行函数了
print(g)  # <generator object foo at 0x0000005037CCF150>
g.__iter__()
print(g.__next__())  # g 是迭代器，触发迭代器g的执行，进而触发函数执行，碰到yield就返回
print(g.__next__())  # 从上次返回点，再次执行
print(g.__next__())
print(g.__next__())

print('===============')
g1 = foo()
for i in g1:
    print(i)
