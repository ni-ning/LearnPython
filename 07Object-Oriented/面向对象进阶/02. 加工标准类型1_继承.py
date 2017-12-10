#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 加工的是类，继承实现
class List(list):
    def __init__(self, item, tag=False):
        super(List, self).__init__(item)
        self.tag = tag

    def append(self, p_object):
        if not isinstance(p_object, str):
            raise "params must be str"

        super(List, self).append(p_object)

    @property
    def mid(self):
        return self[int(len(self)/2)]

    def clear(self):
        if not self.tag:
            raise 'Permission deny'
        super(List, self).clear()
        self.tag = False

l = List([1, 2, 3, 4])
l.append('a')
print(l.mid)
print(l)

l.tag = True
l.clear()
print(l)
