#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 定义名字的方法
import time
name = 'Linda'
def func():
    pass
class Foo(object):
    pass

# 名称空间：名字与值的绑定关系
# 三种名称空间
# 1. 内置名称空间: 随着Python解释器启动而产生
print(sum)  # <built-in function sum>
# 查看内置名称
import builtins
for i in dir(builtins):
    print(i)

# 2. 全局名称空间：文件的执行会产生全局名称空间，指的是文件级别定义的就会放入全局名称空间
x = 1
if x == 1:
    y = 2
