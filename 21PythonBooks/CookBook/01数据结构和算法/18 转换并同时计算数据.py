#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
先转换或过滤数据，然后在序列上执行聚合函数，如min(), max(), sum()
"""

# 优雅的实现方式
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)  # 平方和

# 判断是否存在.py文件
import os
files = os.listdir('.')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')


# 转换拼接
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))


# 取特定关键字值最小值
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

"""
当生成器表达式作为单独参数传递给函数的时候，可以少一个括号
"""
sum((x * x for x in nums))
sum(x * x for x in nums)
# 上面两个等价


# 这种方式会多创建临时列表，不利于大型数据
nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])

