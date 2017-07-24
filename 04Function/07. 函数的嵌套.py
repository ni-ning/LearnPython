#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
1 函数的嵌套调用
2 函数的嵌套定义
"""


# 函数的嵌套调用
def max2(x, y):
    return x if x > y else y


def max4(a, b, c, d):
    res1 = max2(a, b)
    res2 = max2(c, d)
    res3 = max2(res1, res2)
    return res3

print(max4(1, 2, 3, 4))


# 函数的嵌套定义
def f1():
    def f2():
        print('from f2')
        def f3():
            print('from f3')
        f3()
    f2()
f1()

