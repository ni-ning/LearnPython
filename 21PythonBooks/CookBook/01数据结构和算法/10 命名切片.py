#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])

SHARES = slice(20, 23, 1)
PRICE = slice(31, 37)
cost1 = int(record[SHARES]) * float(record[PRICE])
print(cost1)

print(SHARES.start)
print(SHARES.stop)
print(SHARES.step)

"""
你还能通过调用切片的 indices(size) 方法将它映射到一个确定大小的序列上，
这个方法返回一个三元组 (start, stop, step) ，所有值都会被合适的缩小以满足边界限制，
从而使用的时候避免出现 IndexError 异常"""
s = "HelloWorld"
a = slice(5, 50, 2)
print(a.indices(len(s)))

for i in range(*a.indices(len(s))):
    print(s[i])

