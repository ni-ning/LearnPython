#!/usr/bin/env python
# -*-coding:utf-8 -*-

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

print(a.keys() & b.keys())
print(a.keys() - b.keys())

print(a.items() & b.items())

# 以现有字典推导，修改或者过滤字典元素
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)

# 字典keys()和items()返回的是集合视图对象，可以运用集合运算


