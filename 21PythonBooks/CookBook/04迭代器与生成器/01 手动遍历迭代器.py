#!/usr/bin/env python
# -*-coding:utf-8 -*-


def manual_iter1(filename):
    with open(filename, 'r') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration:   # StopIteration 用来指示迭代的结尾
            pass


def manual_iter2(filename):
    with open(filename, 'r') as f:
        while True:
            line = next(f, None)  # 通过返回一个指定值来标记结尾
            if line is None:
                break
            print(line, end='')


manual_iter1('test')
print('-----------我是分割线-------------')
manual_iter2('test')


items = [1, 2, 3]
it = iter(items)   # Invokes items.__iter__()
print(it)          # <list_iterator object at 0x000001F2E74FDA20>

next(it)           # Invokes it.__next__()
next(it)           # Invokes it.__next__()
next(it)           # Invokes it.__next__()

# next(it)         # 正常流程会抛出 StopIteration
next(it, None)     # 可以添加指定值来标记结尾
next(it, None)     # 可以添加指定值来标记结尾
next(it, None)     # 可以添加指定值来标记结尾
next(it, None)     # 可以添加指定值来标记结尾

