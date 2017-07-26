#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
__call__：对象后面加括号，触发执行

注：构造方法的执行是由创建对象触发的，即：对象=类名()；而对于__call__方法的执行是由对象加括号触发的，即对象()或者类()()

"""


class Foo:
    def __call__(self, *args, **kwargs):
        print('========>')

obj = Foo()       # 类可以调用，类也是对象
print(type(obj))  # <class '__main__.Foo'>
print(type(Foo))  # <class 'type'>，类Foo的类为 type

# obj()      # TypeError: 'Foo' object is not callable，obj不可执行
obj()        # 类内部实现 __call__方法， ========>

"""
obj可以加()执行，因为obj所属的类Foo实现了__call__方法
同理Foo可以加()执行，那Foo所属的类type也得有__call__方法

对象可以执行的原因，落脚点为__call__方法，那控制__call__方法，实现对应对象的执行过程
"""