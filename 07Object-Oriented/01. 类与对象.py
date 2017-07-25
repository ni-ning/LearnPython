#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

"""
现实生活中，先是有人这样的一个个对象，随着文明的发展，然后总结出人 --> 类
而程序中，先有类 -->  对象
"""


#  类是一些列对象共有的特征(变量的定义)和技能(函数的定义)的结合体
class Chinese:
    country = 'China'

    def __init__(self, name, age, sex):  # 每个对象都有自己的特性
        self.name = name  # p1.name = 'Linda'
        self.age = age    # p1.age = 18
        self.sex = sex    # p1.sex = 'female'

    def talk(self):  # self就是一个位置形参
        print('%s is talking' % self.name)

print('类的使用：属性的引用和实例化')
# 属性的引用
print(Chinese.country)
print(Chinese.talk)
# Chinese.talk("123")

Chinese.x = 1
print(Chinese.x)  # 向Chinese的名称空间，增加x=1，OK


# 实例化: 执行该类的初始化方法，并且p1作为第一个参数
p1 = Chinese('Linda', 18, 'female')   # Chinese.__init__(p1, 'Linda', 18, 'female')
p2 = Chinese('Tom', 20, 'male')       # Chinese.__init__(p2, 'Tom', 20, 'male')


print('对象的使用')
# 对象的使用：只有一种，就是属性引用
print('p1.name->', p1.name)  # p1名称空间中的name
print('p1.age->', p1.age)    # p1名称空间中的age
print('p1.sex->', p1.sex)    # p1名称空间中的sex

print(p1.country)  # 类名称空间中的country
print(p2.country)  # 类名称空间中的country

p1.talk()   # Chinese.talk(p1)
p2.talk()   # Chinese.talk(p2)

# 与之对比 类调用方法 Chinese.talk("123")



# 类的名称空间
print(Chinese.__dict__)

# 对象的名称空间
print(p1.__dict__)
print(p1.age)     # 本质：p1.__dict__['age']


print(p1.country, id(p1.country))  # 先到对象的名称空间，再到类的名称空间，找不到就报错
print(p1.country, id(p1.country))

print(Chinese.talk)  # <function Chinese.talk at 0x0000005B40B7C488>
# 调用类的函数Chinese.talk() 第一个参数手动填

print(p1.talk)       # <bound method Chinese.talk of <__main__.Chinese object at 0x0000005B40B9A080>>
print(p2.talk)       # <bound method Chinese.talk of <__main__.Chinese object at 0x0000005B40B9A0F0>>
# 调用绑定方法 p1.talk() 第一个参数系统会默认填写

p1.talk()  # Chinese.talk(p1)，如下所示
Chinese.talk(p2)

"""
类：数据属性和函数
对象：数据属性和绑定方法

定义在类内部的变量，是所有对象共有的，id全一样
定义在类内部的函数，是绑定到所有对象的，是給对象来用的，obj.func()，obj作为第一个参数

绑定方法：绑定到谁身上，就是给谁用的，谁来调用就会把自己当做第一个参数传入
"""


# 补充内容
x = 1 # x = int(1) ,每创建一个对象，要做三件事
print(id(x))    # 代表内存中的位置
print(type(x))  # 类型
print(x)        # 对应值

# is 身份运算符
x = 1
y = 1
print(x is y) #  返回 True 比较的是id(x) 是否 等于 id(y)

print(x == y)

"""
在命令行模式下
x = 300
y = 300

x is y 返回 False
"""

# 最后的最后
# *****  对象是特征(变量)与技能(函数)的结合，类是一系列对象共有的特征与技能的结合体  *****

