#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
封装为类的私有属性，但是Python语言并没有访问控制

Python程序员不去依赖语言特性去封装数据，而是通过遵循一定的属性和方法命名规则来达到这个效果
"""
# 第一个约定是任何以单下划线_开头的名字都应该是内部实现


class A(object):
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        '''
        A public method
        '''
        pass

    def _internal_method(self):
        pass
# 使用下划线开头的约定同样适用于模块名和模块级别函数


# 在类定义中使用两个下划线(__)开头的命名


class B(object):
    def __init__(self):
        self.__private = 0       # _B.__private

    def __private_method(self):  # _B.__private_method()
        print('B.__private_method:  %s' % self)

    def public_method(self):
        self.__private_method()
        print('self.__private', self.__private)


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1       # _C.__private

    def __private_method(self):  # _C.__private__method()
        print('C.__private_method:  %s' % self)


b = B()
b.public_method()
# 使用双下划线会导致访问名称变成其他形式，那么继承时及时看上去是相同的名称，不会发生覆盖问题

"""
大多数而言，非公共名称以单下划线开头
涉及到子类， 并且有些内部属性应该在子类中隐藏起来，那么才考虑使用双下划线方案
最后，定义的一个变量和某个保留关键字冲突，可以使用单下划线作为后缀 lambda_ = 2.0
"""

