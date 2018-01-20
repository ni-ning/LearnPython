#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
实现一个优先级队列
"""
import heapq


class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def nlargest(self, n):
        pri_tuple = heapq.nsmallest(n, self._queue)
        return [item[-1] for item in pri_tuple]

    def nsmallest(self, n):
        pri_tuple = heapq.nlargest(n, self._queue)
        return [item[-1] for item in pri_tuple]


class Item(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Item({})".format(self.name)

    __repr__ = __str__


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 10)

print(q.nlargest(2))  # 只是获取，不弹出
print(q.pop())  # 弹出值最小的，即优先级最高的

a = (1, Item('foo'))
b = (5, Item('bar'))

# Python在做元祖比较的时候，如果前面的比较已经可以确定结果了
# 后面的比较操作就不会发生了
print(a < b)

