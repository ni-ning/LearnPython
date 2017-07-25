#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 什么是继承： 一种创建新类的方式
class ParentClass1:
    pass

class ParentClass2:
    pass

class SubClass1(ParentClass1):
    pass

class SubClass2(ParentClass1, ParentClass2):
    pass

print(SubClass1.__bases__)  # 元组形式 (<class '__main__.ParentClass1'>,)
print(SubClass2.__bases__)  # 元组形式 (<class '__main__.ParentClass1'>, <class '__main__.ParentClass2'>)

# Python2中类分为：新式类和经典类
class Foo(object): # 新式类
    pass

class Bar:  # 经典类，不继承object
    pass


# Python3中类新式类
class Foo1(object):  # 等同于 class Foo1: pass
    pass


# 寻找继承关系

# 继承的好处一：减少冗余代码
# 在子类定义新的属性，覆盖父类的属性，称为派生

class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print('eat...')

    def talk(self):
        print('%s is talk...' % self.name)

class People(Animal):

    #　重复代码　->  需改进
    # def __init__(self, name, age, sex, education):
    #     self.name = name
    #     self.age = age
    #     self.sex = sex
    #     self.education = education

    def __init__(self, name, age, sex, education):
        Animal.__init__(self, name, age, sex)    # 子类调用父类的方法
        self.education = education

    def talk(self):
        print('%s say hello' % self.name)


class Pig(Animal):
    pass


class Dog(Animal):
    pass

peo1 = People('Linda', 18, 'female','本科')  # People.__init__()，现在People里找__init__()，找不到再到父类Animal里面找
pig1 = Pig('Tom', 20, 'male')
dog1 = Dog('旺财', 4, 'male')

peo1.talk()
pig1.talk()
dog1.talk()

print(peo1.education)

# 小练习：下列代码的结果是

class Parent:
    def foo(self):
        print('Parent.foo')
        self.bar()   # s.bar()，然后遵循从低往上找.....

    def bar(self):
        print('Parent.bar')


class Sub(Parent):

    def bar(self):
        print('Sub.bar')

s = Sub()
s.foo()  # s.foo，首先对象的__dict__，没有；自己类Sub.__dict__，没有；再到父类Parent.__dict__里面找
# s.foo()执行结果
# Parent.foo
# Sub.bar

print('*************')

class Sub(Parent):
    def __init__(self):
        self.bar = 123

    def bar(self):
        print('Sub.bar')
s1 = Sub()

print(s1.__dict__)  # {'bar': 123}
# s1.bar() # s1.__dict__['bar']，优先对象自己的__dict__
