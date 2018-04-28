#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
定义了很多数据结构的类，不想写__init__函数
"""

import math


class Structure1(object):
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Structure1):
    _fields = ['name', 'shares', 'price']


class Point(Structure1):
    _fields = ['x', 'y']


class Circle(Structure1):
    _fields = ['radius']

    @property
    def area(self):
        return math.pi * self.radius ** 2


s = Stock('ACME', 50, 90.1)
print(s.name)
print(s.shares)
print(s.price)

# p = Point(1)  # TypeError: Expected 2 arguments
c = Circle(3)
print(c.area)


class Structure2(object):
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))


# 将不在_fields中的名称加入到属性中去
class Structure3(object):
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))


if __name__ == '__main__':

    class Stock(Structure2):
        _fields = ['name', 'shares', 'price']

    s1 = Stock('ACME', 50, 90.11)
    s2 = Stock('ACME', 50, price=90.11)
    s3 = Stock('ACME', shares=50, price=90.11)
    # s4 = Stock('ACME', shares=50, price=90.11, aa=1)
