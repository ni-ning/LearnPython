#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
类的单例模式
"""


def singleton(cls):
    __instances__ = {}

    def get_instance(*sub, **kw):
        key = (cls, tuple(sub), tuple(sorted(kw.items())))
        if key not in __instances__:
            __instances__[key] = cls(*sub, **kw)
        return __instances__[key]

    return get_instance


if __name__ == '__main__':

    @singleton
    class Foo(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age


    f1 = Foo('Linda', 18)
    f2 = Foo('Linda', 18)
    f3 = Foo('Jonathan', 28)

    print(id(f1))   # 2084750555512, f1==f2
    print(id(f2))   # 2084750555512, f1==f2
    print(id(f3))   # 2084750555064, f3单独实例
