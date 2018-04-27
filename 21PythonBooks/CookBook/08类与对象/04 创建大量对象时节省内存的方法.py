#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
对于一些只是当做简单数据结构的类而言，给类添加__slots__属性来极大的减少实例所占的内存
"""


class Date(object):
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

"""
当定义__slots__后，Python就会为实例使用一种更加紧凑的内部表示。
实例通过一个很小的固定大小的数组来构建，而不是为每个实例定义一个字典，这跟元组或列表很类似。
在__slots__中列出的属性在内部被映射到这个数组的指定小标上，
"""

"""
减少对__slots__的使用，即使附加实现了不能添加新的属性
Python的很多特性都依赖于普通的基于字典的实现
"""


d = Date(2018, 4, 27)
# d.x = 1  抛异常
