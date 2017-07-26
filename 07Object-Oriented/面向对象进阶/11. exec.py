#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
exec：三个参数
参数一：字符串形式的命令
参数二：全局作用域
参数三：局部作用域
exec会在指定的局部作用域内执行字符串内的代码，除非明确地使用global关键字
"""

s = "print(x)"
g = {'x': 10000000}
l = {'x': 1}
exec(s, g, l)  # 涉及找名字操作


s1 = "y=2"
exec(s1, g, l)
print(g)
print(l)  # y=2 添加到局部作用域字典


s2 = """
global z
z = 3
"""
exec(s2, g, l)
print(g['z'])  # z=3 添加到全局作用域字典
print(l)

# exec 自己定义全局和局部作用域执行命令，只是提供一种模拟方法