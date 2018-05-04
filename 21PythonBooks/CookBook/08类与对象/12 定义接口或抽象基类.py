#!/usr/bin/env python
# -*-coding:utf-8 -*-

# 抽象类：实现规范，检查类型
from abc import ABCMeta, abstractclassmethod


class IStream(object, metaclass=ABCMeta):
    @abstractclassmethod
    def read(self, maxbytes=-1):
        pass

    @abstractclassmethod
    def write(self, data):
        pass


# a = IStream()
"""
抽象类特点不能直接被实例化

抽象类目的是让别的类继承它并实现特定的抽象方法
另外一个用途在代码中检查某些类是否为特定类型，实现特定接口
"""


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


ss = SocketStream()


"""
标准库中有很多用到抽象基类的地方
collections模块定义了很多跟容器和迭代器(序列、映射、集合等)有关的抽象基类
numbers库定义了跟数字对象(整数、浮点数、有理数等)有关的基类
io库定义了很多跟I/O操作相关的基类

类型检查
"""

import collections

print(isinstance([1, 2, 3], collections.Sequence))
print(isinstance([1, 2, 3], collections.Iterable))
print(isinstance([1, 2, 3], collections.Sized))

print(isinstance([1, 2, 3], collections.Mapping))
print(isinstance(dict(x=1), collections.Mapping))
