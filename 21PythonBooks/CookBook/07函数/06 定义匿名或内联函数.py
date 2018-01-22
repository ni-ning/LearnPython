#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
lambda表达式典型的使用场景是排序或数据reduce
"""

"""
lambda表达式有使用限制：只能指定单个表达式，它的值就是最后的返回值
且不能包含其他的语言特性，如多个语句、条件表达式、迭代以及异常处理等等
"""

add = lambda x, y: x + y
print(add(1, 2))


