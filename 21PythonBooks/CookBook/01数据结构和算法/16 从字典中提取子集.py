#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 构造一个字典，他是另外一个字典的子集
# 字典推导
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
p1 = {key: value for key, value in prices.items() if value > 200}

tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}

print(p1)
print(p2)

# 通过创建一个元组序列然后把它传给 dict() 函数也能实现
p3 = dict((key, value) for key, value in prices.items() if value > 200)
print(p3)

# 完成同一件事会有多种方式
p4 = {key: prices[key] for key in prices.keys() & tech_names}
# 但是比第一种方式要慢，如果对性能有要求，需花时间做测试

