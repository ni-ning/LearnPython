#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com


def foo():
    print('from foo')


def bar(name):
    print('bar ==>', name)

foo()          # 定义时无参，调用无参
bar('Linda')  # 定义时有参，调用时有参
