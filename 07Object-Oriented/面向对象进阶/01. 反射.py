#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
什么是反射？
反射的概念是由Smith在1982年首次提出的，主要指程序可以访问、检测和修改它本身状态或行为的一种能力(自省)

Python面向对象中的反射：通过字符串的形式操作对象的相关属性。Python中的一切事物都是对象(都可以使用反射)
"""


class Chinese:
    country = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age

print(Chinese.country)   # 本质：Chinese.__dict__['country']

p = Chinese('Linda', 18)
print(p.name)           # 本质 p.__dict__['name']


# 四个可以实现自省的函数, 下列方法适用于类和对象（一切皆对象，类本身也是一个对象）
# hasattr
print(hasattr(p, 'name'))            # 'name' 字符串
print(hasattr(Chinese, 'country'))  # 与对象一样，'country'也是字符串

# setattr
setattr(p, 'x', 666666)
print(p.__dict__)
print('p.x', p.x)

# getattr
# getattr(p, 'y')  # 报错 'Chinese' object has no attribute 'y'
print(getattr(p, 'y', 'not exists'))
print(getattr(p, 'name'))  # Linda

if hasattr(p, 'x'):
    res = getattr(p, 'x')
    print(res)

# delattr
print(Chinese.country)
delattr(Chinese, 'country')
# print(Chinese.country)       # AttributeError: type object 'Chinese' has no attribute 'country'


# 反射当前模块成员

import sys
m = sys.modules[__name__]
print(m)  # <module '__main__' from 'E:/s17/07Object-Oriented/面向对象进阶/01. 反射.py'>, 一切皆对象

if hasattr(m, 'Chinese'):
    res = getattr(m, 'Chinese')
    print(res)       # <class '__main__.Chinese'>
    obj = res('Tom', 20)
    print(obj.name)  # Tom


#　应用
# 1. 见反射示例
# 2. 动态导入模块(基于反射当前模块成员)

m = __import__('sys')
print(m)      # <module 'sys' (built-in)>
print(m.path)

# 另外相同用法
import importlib
m1 = importlib.import_module('os')
print(m1)
