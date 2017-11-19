#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

x = 1000
def func():
    global x
    x = 0
func()
print(x)
# 在func()执行过程中，修改了外部状态

# 函数式编程，模拟数学上的函数概念；不会修改外部状态

