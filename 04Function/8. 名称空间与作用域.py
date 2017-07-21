#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 一：名称空间
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

# 3. 局部名称空间: 调用函数时会产生局部名称空间，只在函数调用时临时绑定，调用结束解除绑定
x = 10000
def func():
    x = 1
    print(x)
    def f1():
        pass

# 名称空间是一种思想，import this


"""
二：作用域：规定的范围，如何找到名字
    1. 全局作用域：内置名称空间和全局名称空间
    2. 局部作用域：局部名称空间
"""
# 名字的查找顺序：局部名称空间  --> 全局名称空间  -->  内置名称空间
x = 1
def func():
    x = 2
    print(x)
func()  # 执行的时候有效  2

# 查看全局作用域内的名字：globals()
# 查看局部作用域内的名字：locals()

print(globals())
print(locals())
print(globals() is locals())  # 全局的局部就是全局


x = 1000
def func(y):
    x = 2
    print(locals())  # {'y': 1, 'x': 2}
    print(globals()) # 可以看得到全局

func(1) # 局部作用域只在执行的时候有效

# 全局作用域：全局有效，在文件任何位置都被访问到，除非del 删除，否则会一直存活到文件调用结束
# 局部作用域：局部有效，只能在局部范围调用，只在函数调用时有效，函数调用结束时失效









