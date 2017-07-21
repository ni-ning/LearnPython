#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

""""
闭包:定义在内部函数包含对外部作用域而非全局作用域的引用，该内部函数就称为闭包函数
"""
# x = 1 # 全局作用域，不满足条件
def f1():
    x =1  #  外部作用域而非全局作用域，满足条件
    def f2():
        # x = 1 # f2()的内部作用域，不满足条件
        print(x)
    return f2

f = f1()   # f就是闭包函数，包裹着一层东西，f2的外层的x=1
print(f)

x = 1000000
f() # f包含着一层作用局 x=1，找名字的时候，优先找包着的作用域

# 闭包应用：惰性计算
"""
from urllib.request import urlopen
res = urlopen('http://www.baidu.com').read()
print(res.decode('utf-8'))
"""
from urllib.request import urlopen
def index(url):
    def get():
        return urlopen(url).read().decode('utf-8')
    return get

oldboy_get = index('http://crm.oldboyedu.com')
print(oldboy_get())
print(oldboy_get.__closure__[0].cell_contents)  # http://crm.oldboyedu.com

# 闭包的意义：返回的函数对象，不仅仅是一个函数对象，在该函数外还包裹了一层作用域，
# 这使得，该函数无论在何处调用，优先使用自己外层包裹的作用域


