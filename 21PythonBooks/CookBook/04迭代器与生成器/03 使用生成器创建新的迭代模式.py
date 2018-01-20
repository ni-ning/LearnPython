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


