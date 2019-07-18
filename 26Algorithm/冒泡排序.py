# -*-coding:utf-8 -*-
import random

'''
冒泡排序 Bubble Sort

- 列表每两个相邻的数, 如果前面比后面大, 则交换这两个数
- 一趟排序完成后, 则无序区减少一个数, 有序区增加一个数
- 代码关键点: 趟、无序区范围
'''


def bubble_sort(li):
    for trip in range(len(li) - 1):                 # 第trip趟
        exchange = False
        for index in range(len(li) - trip - 1):     # 对无序区进行相邻数的交换
            if li[index] > li[index + 1]:
                li[index], li[index+1] = li[index+1], li[index]
                exchange = True
        print(li)
        if not exchange:    # 当一趟无交换, 则认为已排序
            return


# li = [random.randint(0, 10000) for i in range(100)]
# print(li)
# bubble_sort(li)
# print(li)

# li = [1, 3, 2, 5, 7, 9, 4, 0]
# bubble_sort(li)

li = [9, 8, 7, 1, 2, 3, 4, 5]
bubble_sort(li)
