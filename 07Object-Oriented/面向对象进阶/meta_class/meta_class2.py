#!/usr/bin/env python
# -*-coding:utf-8 -*-


class Mymeta(type):

    def __init__(cls, cls_name, cls_bases, cls_dic):
        print('类Chinese定义时执行......')

        super(Mymeta, cls).__init__(cls_name, cls_bases, cls_dic)

    def __call__(cls, *args, **kwargs):
        print('开始执行Chinese实例化......')

        # 调用cls，即Chinese下的函数__new__
        # 在该函数完成：1. 产生空对象 obj 2. 初始化  3. 返回obj
        obj = cls.__new__(cls, *args, **kwargs)

        return obj


class Chinese(object, metaclass=Mymeta):

    def __init__(self, name, age):
        print('初始化Chinese对象时执行.....')
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking....' % self.name)

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        cls.__init__(obj, *args, **kwargs)
        return obj


person = Chinese('Linda', 18)
print(person.name)
print(person.age)




