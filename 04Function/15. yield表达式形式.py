#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# yield 的语句形式： yield 1
# yield的表达式形式：x = yield


'''
# 实例一
def eat(name):
    print('%s is ready to eat...' % name)
    while True:
        food = yield
        print('%s is eating %s' % (name, food))

g = eat('alex')
print(g)
next(g)   # 第一次时，等价于，g.send(None)
g.send('包子1')  # 就是一次next()操作 + 给 yield 传递参数
g.send('包子2')
g.send('包子3')
'''

'''
# 实例二
def starter(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        next(res)  # 初始化一下
        return res
    return wrapper

@starter
def eat(name):
    print('%s is ready to eat...' % name)
    while True:
        food = yield
        print('%s is eating %s' % (name, food))

g = eat('alex')
g.send('包子1')
'''


# 实例三，有返回值
def init(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        next(res)  # 初始化一下
        return res
    return wrapper

@init
def eat(name):
    print('%s is ready to eat...' % name)
    food_list = []
    while True:
        food = yield food_list
        food_list.append(food)
        print('%s is eating %s' % (name, food))

g = eat('alex')
print(g.send('包子1'))
print(g.send('包子2'))
print(g.send('包子3'))

'''
x = yield res 分析如下：
g.send('111')，先把111传给yield，由yield赋值给x，再往下执行，
直到再一次碰到yield，然后把yield返回值返回
'''

