#!/usr/bin/env python
# -*-coding:utf-8 -*-


# 定义生产器函数
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)


"""
一个生成器函数的主要特征是它只会回应在迭代中使用的next操作
一旦生成器函数返回退出，迭代终止
"""

