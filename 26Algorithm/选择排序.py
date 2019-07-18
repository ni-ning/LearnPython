# -*-coding:utf-8 -*-

'''
选择排序 Select Sort

- 一趟中找出最小值
'''


def select_sort_simple(li):
    li_new = []
    for trip in range(len(li)):
        min_value = min(li)
        li_new.append(min_value)
        li.remove(min_value)
    return li_new
# 缺点 新li_new 和 min remove 两个O(n)


li = [3, 2, 4, 1, 5, 6, 9, 7]
print(select_sort_simple(li))


def select_sort(li):
    for trip in range(len(li) - 1):             # 第 trip 趟
        min_index = trip                        # 无序区第一数，默认为最小的, 列表的下标是一种很好的操作思路
        for index in range(trip+1, len(li)):
            if li[index] < li[min_index]:
                min_index = index
        if min_index != trip:
            li[trip], li[min_index] = li[min_index], li[trip]


li = [3, 2, 4, 1, 5, 6, 9, 7]
print(select_sort_simple(li))



