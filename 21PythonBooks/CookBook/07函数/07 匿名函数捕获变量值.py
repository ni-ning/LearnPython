#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
lambda在运行时绑定值，而不是定义时绑定
如果想让匿名函数在定义时就捕获值，可以让那个参数值定义为默认参数即可
"""

funcs = [lambda x: x+n for n in range(5)]
for f in funcs:
    print(f(0))

"""
实际效果是运行是n的值为迭代的最后一个值
4
4
4
4
4
"""

funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
    print(f(0))

"""
通过使用函数默认值参数形式，lambda函数在定义时就能绑定到值
0
1
2
3
4
"""