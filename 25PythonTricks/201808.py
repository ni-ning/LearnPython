#!/usr/bin/env python
# -*-coding:utf-8 -*-

# 20180811
# How to merge two dictionaries
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}
print(z)        # {'a': 1, 'b': 3, 'c': 4}

z = dict(x, **y)
print(z)        # {'a': 1, 'b': 3, 'c': 4}

"""
In these examples, Python merges dictionary keys in the order listed in the expression, 
overwriting duplicates from left to right.
"""


# 20180812
# Different ways to test multiple flags at once in Python
x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    print('passed')

if 1 in (x, y, y):
    print('passed')

# These only test for truthiness
if x or y or z:
    print('passed')

if any((x, y, z)):
    print('passed')


# 20180813
# How to sort a Python dict by value
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
print(sorted(xs.items(), key=lambda x: x[1]))   # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
print(sorted(xs, key=lambda k: xs[k]))          # ['d', 'c', 'b', 'a']

from operator import itemgetter
print(sorted(xs.items(), key=itemgetter(1)))    # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

