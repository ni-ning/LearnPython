#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

# key参数是callable，并且是从rows中接收一个单一元素，返回的值被用来排序
rows_by_fname = sorted(rows, key=itemgetter('fname'))  # 比来lambda稍微快点
rows_by_fname2 = sorted(rows, key=lambda item: item.get('fname'))
print(rows_by_fname)
print(rows_by_fname2)

# 支持多个keys，同样适用于max，min
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

