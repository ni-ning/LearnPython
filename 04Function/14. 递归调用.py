#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
递归调用：在函数调用过程中，直接或间接调用了函数本身，这就是函数递归调用
"""

# def f1():
#     print('from f1')
#     def f2():
#         print(f1)   # 能找到f1
#     f2()
# f1()

# def f1():
#     print('from f1')
#     f1()
# f1()

# def f1():
#     print('from f1')
#     f2()
#
# def f2():
#     print('from f2')
#     f1()
# f2()

import sys
print(sys.getrecursionlimit())  # 递归层 1000

"""
应用实例
age(5) = age(4) + 2
age(4) = age(3) + 2
age(3) = age(2) + 2
age(2) = age(1) + 2
age(1) = 18

age(n) = age(n-1) n>1
age(1) = 18       n=1
"""


def age(n):
    if n == 1:
        return 18
    return age(n-1) + 2

print(age(5))


"""
递归：递推和回溯两个阶段
1. 必须有一个明确的结束条件
2. 每次进入更深一层递归时，问题规模相比上次递归都应有所减少
3. 递归效率不高
"""
# 算法：解决问题的方法

# 二分法，前提有序序列
l = [1, 2, 10, 33, 53, 71, 73, 75, 85, 92, 101, 201, 999, 11111]


def search(find_num, seq):
    # 必须有一个明确的结束条件
    if len(seq) == 0:
        print('not exists')
        return
    mid_index = len(seq)//2
    mid_num = seq[mid_index]
    print(seq, mid_num)
    if find_num > mid_num:
        # in the righ side
        seq = seq[mid_index+1:]
        search(find_num, seq)
    elif find_num < mid_num:
        # in the left side
        seq = seq[:mid_index]
        search(find_num, seq)
    else:
        print('find it')  # return None

search(32, l)
