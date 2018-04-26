#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
改变对象实例的打印或显示输出，让它们更具可读性
"""


class Pair(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Pair(%s, %s)' % (self.x, self.y)

    __repr__ = __str__


p = Pair(3, 4)
print(p)   # Pair(3, 4)
