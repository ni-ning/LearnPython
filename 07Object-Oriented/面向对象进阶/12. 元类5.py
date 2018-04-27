#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com


class Mymeta(type):
    def __call__(self, *args, **kwargs):  # self=Foo,args=('Linda',),kwargs={'age':18}

        # 调用__new__ 制造对象
        print(args, kwargs)
        obj = self.__new__(self)  # Foo.__new__(self) 类调用，不会自动传值
        print(obj)  # <__main__.Foo object at 0x00000060A5C05EF0>

        # 调用__init__初始化对象
        self.__init__(obj, *args, **kwargs)  # Foo.__init__(obj,'Linda',18)  类调用，不会自动传值

        # 返回对象
        return obj


class Foo(metaclass=Mymeta):  # Foo=Mymeta('Foo', (object,), {})
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)

obj = Foo('Linda', age=18)  # Mymeta.__call__(Foo, 'Linda', age=18)
print(obj)
print(obj.__dict__)


"""
把握一个原则：谁加(),调用它所属类的__call__方法，__call__方法需做三件事：
1. 制造对象
2. 初始化操作
3. 返回对象
"""

