#!/usr/bin/env python
# -*-coding:utf-8 -*-


class Node(object):

    def __init__(self, value):
        self._value = value
        self._children = []

    def __str__(self):
        return "Node({})".format(self._value)

    __repr__ = __str__

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

"""
yield from iterable 本质上等于 for item in iterable: yield item
>>> def g(x):
...     yield from range(x, 0, -1)
...     yield from range(x)
...
>>> list(g(5))
[5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
"""


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)

    # Outputs Node(0), Node(1), Node(3), Node(4), Node(2), Node(5)

    """
    Python的迭代器协议要求一个__iter__()方法返回一个特殊的迭代器对象，这个迭代器对象实现了__next__()方法
    并通过StopIteration异常标识迭代的完成
    """
