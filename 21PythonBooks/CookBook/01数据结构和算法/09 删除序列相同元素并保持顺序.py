#!/usr/bin/env python
# -*-coding:utf-8 -*-


def dedup(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield val
            seen.add(val)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedup(a)))

b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedup(b, key=lambda d: (d['x'], d['y']))))

# 同样适用于文件
"""
with open(somefile, 'r') as f:
    for line in dedup(f):
"""


"""
yield 使用 测试
"""
print('-----------我是分割线------------')


def func():
    yield 1
    yield 2
    yield 3


print(func)    # 函数对象
print(func())  # 执行含有yield的函数
g = func()     # 又执行了一下，生成新的生成器g


# *********生成器使用如下*********

print(next(g))  # 一个一个读，手动控制，直到抛出 StopIteration

# for...in 迭代读，不用考虑抛出异常
for item in g:
    print(item)

# 直接list一下，把所有的都读出来，并转化为列表
g1 = func()
print(list(g1))





