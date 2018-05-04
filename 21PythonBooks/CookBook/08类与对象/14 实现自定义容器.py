#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
实现一个自定义的类来模拟内置的容器类功能，比如字典和列表
"""

import collections
import bisect


class A(collections.Iterable):
    pass


# 序列：实现索引、固定长度、切片，扩展默认排序
class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items =sorted(initial) if initial is not None else []

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def add(self, item):
        bisect.insort(self._items, item)  # 在排序列表中插入元素后，仍然保证有序


"""
collections中很多抽象类会为一些常见容器提供默认的实现，只需要实现自己感兴趣的方法即可
"""


class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    def __getitem__(self, index):
        print('Getting: ', index)
        return self._items[index]

    def __setitem__(self, index, value):
        print('Setting: ', index, value)
        self._items[index] = value

    def __delitem__(self, index):
        print('Deleting: ', index)
        del self._items[index]

    def insert(self, index, value):
        print('Inserting: ', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Len')
        return len(self._items)


if __name__ == '__main__':
    items = SortedItems()
    print(isinstance(items, collections.Iterable))
    print(isinstance(items, collections.Sequence))
    print(isinstance(items, collections.Container))
    print(isinstance(items, collections.Sized))
    print(isinstance(items, collections.Mapping))

    """
    使用collections中的抽象基类可以确保自定义的容器实现了所有必要的方法
    """
    print('**************************************************')
    a = Items([1, 2, 3])
    len(a)
    a.append(4)
    a.insert(0, 1000)
    print(list(a))
