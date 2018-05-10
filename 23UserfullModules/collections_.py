#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
collections是Python内建的一个集合模块，提供了很多有用的集合类
"""

p = (1, 2)  # tuple可表示二位坐标，但是不直观

"""
nametuple是一个函数，它用来创建一个自定义的tuple对象
并且规定了tuple元素的个数，并可以用属性而不是索引的来引用tuple的某个元素
"""
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)



