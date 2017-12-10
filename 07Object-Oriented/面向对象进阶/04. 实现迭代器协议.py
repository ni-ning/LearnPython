#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com


class Foo(object):
    def __init__(self, n, stop):
        self.n = n
        self.stop = stop

    def __next__(self):
        if self.n >= self.stop:
            raise StopIteration  # for循环会捕捉这个异常

        x = self.n
        self.n += 1
        return x

    def __iter__(self):
        return self

obj = Foo(0,10)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

print('******')
for i in obj:
    print(i)

from collections import Iterator
print(isinstance(obj, Iterator))