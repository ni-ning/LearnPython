#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
通过下标访问列表或元组的代码，可读性差
可以通过名称来访问元素
"""
# 命名元组
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub.addr)
print(sub.joined)


def compute_cost0(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total
# 这样代码，表意不清楚，并且非常依赖记录的结构


Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


"""
命名元组另一个用途就是作为字典的替代，因为字典需要更多的内存空间
如果你需要构建一个非常大的包含字典的数据结构，那么使用命名元组会更加高效
但是需要注意的是，不像字典那样，一个命名元组是不可更改的
"""
# 实例方法_replace()，创建一个新的命名元组
s = Stock('ACME', 100, 123.45)
s = s._replace(shares=75)
print(s)

# _repalce() 当你的命名元组拥有可选或者缺失字段时候， 它是一个非常方便的填充数据的方法
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)


def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}

print(dict_to_stock(a))
print(dict_to_stock(b))

"""
如果你的目标是定义一个需要更新很多实例属性的高效数据结构，那么命名元组并不是你的最佳选择。
这时候你应该考虑定义一个包含 __slots__ 方法的类
"""