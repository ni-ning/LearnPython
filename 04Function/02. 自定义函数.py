#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 为什么要定义函数？ 先定义后使用。如果没有定义而直接使用，相当于引用了一个不存在的变量名
# foo()   # NameError: name 'foo' is not defined

def foo():
    print('print from foo')
foo()
print(foo)  # 定义了一个名字foo，指向一段代码

# 小结：函数的使用包含两个阶段：函数定义和函数使用

"""
语法:
def 函数名(参数1， 参数2， .....):
    文档注释
    1. 函数功能
    2. 输入参数解析
    3. 输出参数说明
    函数体
    return 值
"""

# 定义函数的三种形式
# 一 无参函数：如果函数的功能仅仅只是执行一些操作而已，无参函数通常无返回值

# 补充 三元表达式，就是简单的if...else 判断，成立写前面，不成立的写后面 res = x if x > y else y
x = 10
y = 2
if x > y:
    print(x)
else:
    print(y)
res = x if x > y else y # 注意返回结果如何实现
print(res)


# 二 定义有参函数：函数的功能执行依赖于外部传入的参数，有参函数通常有返回值
def my_max(x, y):
    res = x if x > y else y
    return res

# 三 空函数
def auth():
    """认证功能"""
    pass

# 小结：写程序，可以用空函数来定义整个架构，看看需要实现什么功能

def insert():
    """插入功能"""
    pass
def select():
    """查询功能"""
    pass
def update():
    """修改功能"""
    pass
def delete():
    """删除功能"""
    pass