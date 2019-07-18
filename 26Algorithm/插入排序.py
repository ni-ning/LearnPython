# -*-coding:utf-8 -*-

'''
插入排序

- 初始时手里(有序区)只有一张牌
- 每次(从无序区)摸一张牌, 插入到手里已有牌的正确位置
'''


def insert_sort(li):
    for trip in range(1, len(li)):  # trip 表示摸到牌的下标, 即无序区
        temp = li[trip]
        index = trip - 1            # 手里的牌, 即有序区, 最后的下淼
        while index >= 0 and li[index] > temp:
            li[index+1] = li[index]
            index -= 1
        li[index+1] = temp

# 1s 处理 1000 0000

