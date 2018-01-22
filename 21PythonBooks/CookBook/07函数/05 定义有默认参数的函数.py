#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
直接在函数定义中给参数指定一个默认值，并放到参数列表最后即可
"""


def spam(a, b=42):
    print(a, b)


spam(1)
spam(1, 2)


# 如果默认参数是一个可修改的容器，比如列表、集合或者字典，可使用None作为默认值
def bar(a, b=None):
    if b is None:
        b = []
    print(a, b)


bar(1, [1, 2])
bar(2)

# 测试一下某个默认参数是否传递过来
"""
object是python中所有类的基类，可以创建object类的实例
但是这些类没有任何有用的方法，也没有任何实例数据
"""
_no_value = object()


def foo(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
    else:
        print('b value is supplied')


foo(1)
foo(1, 2)
foo(1, None)


"""
默认参数的值仅仅在函数定义的时候赋值一次
默认参数的值应该是不可变的对象，如None、True、False、数字或字符串
"""
