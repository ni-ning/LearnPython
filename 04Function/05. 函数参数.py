#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 一：从大的角度来看，函数的参数分两种：形参(变量名)和实参(值)

# 定义阶段
def foo(x, y): # x=1, y=2
    print(x)
    print(y)

# 调用阶段
foo(1, 2)

# 补充：函数定义阶段到底干了什么事情,只检测函数体语法错误，并不会执行

def bar(x, y):  # 定义阶段不会报错
    xxxxxxxxxxxx
    yyyyyyyyyyyy
    zzzzzzzzzzzz

"""
语法错误 SyntaxError：
print('''''
if x>y print('xx')
"""

# bar(1,2)  # 调用时才会判断报错，NameError: name 'xxxxxxxxxxxx' is not defined


# 二：详细的区分函数参数分为五种：位置参数，关键字参数，默认参数，可变长参数(*args, **kwargs),命名关键字参数
'''名词：高度总结了技术的功能'''

# 1. 位置参数，有顺序区分
def foo(x, y, z):  # 位置形参：必须被传值的参数
    print(x, y, z)

foo(1, 2, 3) # 位置实参数：与形参一一对应

# 2. 关键字参数(对实参而言)，key=value
foo(z=1, y=2, x=3)

# 关键字参数需要注意问题：
# (1) 关键字实数必须放在位置实参后面
# (2) 不能重复对一个形参传值
foo(1, z=3, y=2)  # 正确
# foo(x=1,2,z=3)  # 错误
# foo(1, x=1,y=2,z=3) # 错误

# 3. 默认参数(针对形参而言)
def register(name, age, sex='Male'): # 形参 sex='Male'，默认参数
    print(name, age, sex)
register('Jonathan', 40, 'Male')
register('Tom', 30)
register('Linda', 28, 'Female')
# 默认参数需要注意的问题
# (1) 默认参数必须跟在非默认参数之后  def register（sex='male,name,age):pass 在定义阶段就会报错
# (2) 默认参数在定义阶段赋值了，而且只在定义阶段赋值一次
# (3) 默认参数的值通常定义成不可变类型
a = 10000000
def foo(x, y=a):
    print(x,y)
a=0
foo(1)  # 1, 10000000

# 4. 可变长参数
# 说明：从实参角度传入的参数有位置实参，关键字实参，从而可变长形参也要定义两种参数来接收******
def foo(x, y, *args): # * 会把溢出的按位置传入的实参都接收，以元组的形式赋值给args
    print(x, y, args)
foo(1, 2, 3, 4, 5, 6, 7)  # 1 2 (3, 4, 5, 6, 7)

# 任意参数的求和
def add(*args):
    res = 0
    for item in args:
        res += item
    return res
print(add(1, 2, 3, 4, 5))

def foo(x, y, **kwargs): #  ** 会把溢出的按关键字传入的实参都接收，以字典的形式赋值给kwargs
    print(x, y)
    print(kwargs)

foo(y=1, x=2, name='Linda', age=18)  # {'name': 'Linda', 'age': 18}

# 5. 命名关键字参数(了解)
# * 后面定义的参数为命名关键字参数，这类参数必须被传值，而且必须以关键字实参传入
def foo(name, age, *, sex, height):
    print(name,age,sex,height)

foo('Linda', 18, sex='Female', height='170cm')

# 参数顺序
def foo(name, age=18, *args, sex='female', **kwargs):
    print('name==>', name)
    print('age==>', age)
    print('args==>', args)
    print('sex==>', sex)
    print('kwargs==>', kwargs)

foo('alex',1,2,3,4,5,sex='female',a=1,b=2,c=3) # age=1

# 补充 *args  **kwargs
def foo(*args):
    print(args)
# foo(1,2,3,4) # 1,2,3,4 <===> *(1,2,3,4)
# *['A', 'B', 'C', 'D']  <===> 'A', 'B', 'C', 'D'

def foo(**kwargs):
    print(kwargs)
foo(**{'a':1,'b':2})  # 等同于 foo(a=1,b=2)

# 引申一下为装饰器做准备
print('**********************************************')
def foo(x, y, z):
    print('from foo',x, y, z)

def wrapper(*args, **kwargs):
    print(args)          # args=(1,2,3)
    print(kwargs)      # kwargs={'a':1,'b':2}
    foo(*args, **kwargs) # foo(*(1,2,3),**{'a':1,'b':2} ==> foo(1,2,3,a=1,b=2)

#wrapper(1,2,3,a=1,b=2)  ==> foo(1,2,3,a=1,b=2)
# 所以wrapper传入的参数会原封不动地传给foo，传入的参数正确与否就以foo需要的为准
wrapper(1, 2, 3)