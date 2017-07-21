#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
装饰器：修饰别人的工具，修饰添加功能，工具指的是函数

装饰器本身可是任何可调用对象，被装饰的对象也可以是任何可调用对象

为什么要用装饰器：
    开放封闭原则：对修改是封闭的，对扩展是开放的
    装饰器就是为了在不修改被装饰对象的源代码以及调用方式的前提下，为其添加新功能
"""

import time


def timmer(func):
    def wrapper(*args, **kwargs):
        star_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print('run time is %s' % (stop_time - star_time))
        return res
    return wrapper

@timmer  # 固定语法，index=timmer(index)，只有一个输入参数，即下方的函数名，===> index=wrapper
def index():
    time.sleep(3)
    print('welcome to index')
    return 2

"""
f = timmer(index)  # f <==> wrapper
f()   # wrapper()
# 为保证调用方式不变
index = timmer(index)
index()
"""

"""
index = timmer(index)  # index   <===> wrapper
index()                # index() <===> wrapper()
"""

res = index()
print(res)

@timmer
def foo(name):
    time.sleep(1)
    print('from foo', name)

res1 = foo('Linda')


