#!/usr/bin/env python
# -*-coding:utf-8 -*-

import itertools

natuals = itertools.count(1)
# for n in natuals:
#     print(n)

cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)

ns = itertools.repeat('A', 3)
for n in ns:
    print(n)

"""
非常有用的迭代器函数
"""

for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# itertools.chain() 可以把一组迭代对象串联起来，形成一个更大的迭代器
print(list(itertools.chain('ABC', 'XYZ')))

# itertools.groupby() 把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))  # group 也是一个迭代器

"""
itertools.groupby() 实际上的挑选规则是通过函数完成的，
只要作用于函数的两个元素相等，这两个元素就被认为是在一组的，而函数返回值作为组的key
如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key
"""
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c:c.lower()):
    print(key, list(group))