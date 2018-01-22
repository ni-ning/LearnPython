#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
Python没有类型声明，阅读代码很难知道应该传递什么样的参数给这个函数
注解起到很重要作用
"""


def add(x: int, y: int) -> int:
    return x + y


print(add(1, 3))
print(help(add))
print(add.__annotations__)
