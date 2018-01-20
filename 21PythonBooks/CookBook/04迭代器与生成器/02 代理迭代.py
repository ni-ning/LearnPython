#!/usr/bin/env python
# -*-coding:utf-8 -*-

# 定义__iter__()方法，将迭代操作代理到容器内部对象上去


class Node(object):
    def __init__(self, value):
        self._value = value
        self._children = []

    def __str__(self):
        return 'Node({})'.format(self._value)

    __repr__ = __str__

    def add_child(self, node):
        self._children.append(node)

    # Python的迭代器协议需要__iter__()方法返回一个实现了__next__()方法的迭代器对象
    def __iter__(self):
        return iter(self._children)


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)

    # __iter__()方法简单的将迭代请求传递给内部 _children属性
    for ch in root:
        print(ch)
