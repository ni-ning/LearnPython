#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
给某个实例attribute增加除访问与修改之外的其他处理逻辑，比如类型检查或合法性验证
"""


class Person(object):
    def __init__(self, first_name, last_name="NN"):
        self._first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Cant't delete attribute")


p = Person('Linda')
print(p.__dict__)
print(p.first_name)

p.first_name = 'test'
print(p.first_name)

# p.first_name = 1000  # TypeError: Expected a string

del p.last_name
print(p.__dict__)

# property的一个关键特征是它看上去跟普通的attribute没什么两样，但是访问它的时候会自动触发 getter, setter, deleter

# 一个Python类准备加入到一个基于远程过程调用的大型分布式系统中。
# 这种情况下，直接使用get/set方法(普通方法调用)而不是property或许会更容易兼容
