#!/usr/bin/env python
# -*-coding:utf-8 -*-
from functools import reduce

filter_con_list = list()

filter_con_list.append(True)
filter_con_list.append(True)
filter_con_list.append(True)

res = reduce(lambda x, y: (x & y), filter_con_list)  # 先取前两个元素调用函数，得到结果再和下一个元素调用函数

print(res)