#!/usr/bin/env python
# -*-coding:utf-8 -*-


class Mymeta(type):

    def __init__(cls, cls_name, cls_bases, cls_dic):
        print('类Chinese定义时执行......')

        super(Mymeta, cls).__init__(cls_name, cls_bases, cls_dic)

    def __call__(cls, *args, **kwargs):
        print('开始执行Chinese实例化......')

        # Create and return a new object.
        # 输入参数 cls 表示创建相应类的空的对象，重点是空对象
        obj = object.__new__(cls)

        # 调用Chinese下的__init__，初始化obj
        cls.__init__(obj, *args, **kwargs)

        # 返回完成初始化的obj
        return obj


class Chinese(object, metaclass=Mymeta):

    def __init__(self, name, age):
        print('初始化Chinese对象时执行.....')
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking....' % self.name)


person = Chinese('Linda', 18)
print(person.name)
print(person.age)




