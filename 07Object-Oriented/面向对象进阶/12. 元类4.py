#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
__call__
__new__
__init__
"""

class Mymeta(type):
    def __init__(self, name, bases, dic):
        print('__init__')
        # 控制Foo行为
        super().__init__(name, bases, dic)

    def __new__(cls, *args, **kwargs):
        print('__new__', *args)
        print('__new__', **kwargs)
        return type.__new__(cls, *args, **kwargs)

class Foo(metaclass=Mymeta):
    # Foo=Mymeta('Foo', (object,), {}) -->Mymeta.__init__(Foo, 'Foo', (object,), {})
    # Mymeta.__init__(Foo, 'Foo', (object,), {}) 中的第一参数Foo从何而来，肯定在这之前要造出来
    pass