# -*- coding:utf-8 -*-

# 单纯地纯计算切换反而会降低运行效率

import time


# 串行执行
def consumer(res):
    '''任务1:接收数据,处理数据'''
    pass


def producer():
    '''任务2:生产数据'''
    res = []
    for i in range(10000000):
        res.append(i)
    return res


start = time.time()
res = producer()
consumer(res)
stop = time.time()
print(stop - start)     # 1.0780932903289795


# 基于yield并发执行
def consumer():
    res = []
    '''任务1:接收数据,处理数据'''
    while True:
        x = yield
        res.append(x)


def producer():
    '''任务2:生产数据'''
    g = consumer()
    next(g)
    for i in range(10000000):
        g.send(i)


start = time.time()
# 基于yield保存状态,实现两个任务直接来回切换,即并发的效果
producer()
stop = time.time()
print(stop - start)     # 1.8630154132843018