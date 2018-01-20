#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# for 循环形式
symbols = '*&^(%@'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# 列表推导
symbols1 = '*&^(%@'
codes1 = [ord(symbol) for symbol in symbols1]
print(codes1)
# 通常的原则是，只用列表推导来创建新的列表，并且尽量保持简短

# filter, map实现
symbols2 = '*&^(%@'
codes2 = list(filter(lambda c: c < 127, map(ord, symbols2)))
print(codes2)
