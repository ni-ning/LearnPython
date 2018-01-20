#!/usr/bin/env python
# -*-coding:utf-8 -*-

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
d['foo'] = 100
for key in d:
    print(key, d[key])

"""
有序字典
1. 内部维护键插入顺序的双向列表
2. 一个OrderDict大小是普通字典的两倍，当大量数据时需权衡
"""


