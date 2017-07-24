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


# 实例化:
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
print(p1.age)     # p1.__dict__['age']

