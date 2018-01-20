#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列

# 列表推导
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])
# 潜在缺陷，如果输入非常大就可能产生非常大的结果集，占用大量内存
# 如果对内存比较敏感，可用生成器表达式迭代产生过滤元素

# 生成器表达式
pos = (n for n in mylist if n > 0)
print(pos)
for x in pos:
    print(x)

# 有时候过滤规则比较复杂，不能简单使用 列表推导或生成器表达式，如过滤异常等
# filter() 函数
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)
# filter()函数创建了一个迭代器，list一下全部取出来

# 过滤操作的一个变种就是将不符合条件的值用新值替代
clip_neg = [n if n > 0 else 0 for n in mylist]
clip_pos = [n if n < 0 else 0 for n in mylist]

# 另外一个值得关注的过滤工具 itertools.compress()
# compress(iterable, Boolean序列), 类似数组 Array[a>5]
from itertools import compress
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
more5 = [n > 5 for n in counts]
res = list(compress(addresses, more5))
print(res)
