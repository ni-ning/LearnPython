#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com


class Mymeta(type):
    def __init__(self, cls_name, cls_bases, cls_dic):
        print(self)
        print(cls_name)
        print(cls_bases)
        print(cls_dic)

    # def __new__(cls, *args, **kwargs):
    #     print('Mymeta.__new__')

    def __call__(self, *args, **kwargs):
        print('mymeta.__call__')
        # new 新建 obj

        # 初始化赋值操作

        return 123123123


class Chinese(object, metaclass=Mymeta):
    # 本质 Chinese=Mymeta('Chinese',(object,),{})
    # Mymeat.__init__(Chinese,'Chinese',(object,),{})
    x = 1

    def __int__(self, name, age):  # 仅仅只是初始化操作
        self.name = name
        self.age = age


obj = Chinese('Linda', 18)
# 加(),触发执行Chinese所属类的__call__方法，即Mymeta.__call__方法
# Mymeta.__call__('Linda', 18)，返回值正常操作应为Chinese的对象
# 造一个Chinese对象返回；初始化赋值操作

print(obj)





