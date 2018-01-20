#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
字典中键映射多个值
"""

# 保持元素插入的顺序
d = {
    'a': [1, 2, 3, 4],
    'b': [4, 5]
}

# 去掉重复元素，且不关心元素的顺序
e = {
    'a': {1, 2, 3, 4},
    'b': {4, 5}
}

# 自动初始化每个key对应的值
from collections import defaultdict

dic = defaultdict(list)
dic['a'].append(1)
dic['a'].append(2)
dic['a'].append(3)
print(dic)

dic1 = defaultdict(set)
dic1['a'].add(1)
dic1['a'].add(2)
dic1['a'].add(3)
print(dic1)

"""
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
"""