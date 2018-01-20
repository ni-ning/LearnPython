#!/usr/bin/env python
# -*-coding:utf-8 -*-

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# zip先将键和值反转过来
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price)
print(max_price)
# (1, 2, 3) 和(1, 2, 4)相比较的时候，依次比较各项

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# max、min函数中提供的key参数来获取最大值、最小值对应键的信息
print(max(prices, key=lambda k: prices[k]))
print(min(prices, key=lambda k: prices[k]))
# 如果想得到值，还得进行一步操作
print(prices[max(prices, key=lambda k: prices[k])])
print(prices[min(prices, key=lambda k: prices[k])])
