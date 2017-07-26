#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

# 1. 类也是对象
class Foo:
    pass

obj = Foo()
print(type(obj))
print(type(Foo))

"""
python中一切皆是对象，类本身也是一个对象，当使用关键字class的时候，
python解释器在加载class的时候就会创建一个对象(这里的对象指的是类而非类的实例)，
因而我们可以将类当作一个对象去使用，同样满足第一类对象的概念，可以：

1. 把类赋值给一个变量
2. 把类作为函数参数进行传递
3. 把类作为函数的返回值
4. 在运行时动态地创建类
"""

def func():
    class Foo:
        pass
    print(Foo)
func()  # <class '__main__.func.<locals>.Foo'>， 在运行时动态地创建类

# 2. 什么是元类
"""
元类是类的类，是类的模板
元类是用来控制如何创建类的，正如类是创建对象的模板一样，而元类的主要目的是为了控制类的创建行为
元类的实例化的结果为我们用class定义的类，正如类的实例为对象(f1对象是Foo类的一个实例，Foo类是 type 类的一个实例)
type是python的一个内建元类，用来直接控制生成类，python中任何class定义的类其实都是type类实例化的对象

+-----------+               +---------+             +-------------+
|           |  instance of  |         | instance of |             |
| instance  +-------------> +  class  +-------------+  metaclass  |
|           |               |         |             |             |
+-----------+               +---------+             +-------------+

类是实例对象的模板，元类是类的模板
"""

# 研究元类为了控制 关键字class行为，实现定制，如CRM自定制框架


# 3. 创建类的两种方式

# 方式一： 使用class 关键字
class Chinese(object):
    print('======>')  # 定义类会执行内部代码
    print('======>')
    print('======>')
    country ='China'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' % self.name)

print(Chinese.__bases__)  # (<class 'object'>,)

# 创建类的三要素
# 1. 类名
# 2. 继承的父类
# 3. 类体

# 第一步：准备工作
class_name = 'Chinese1'
class_bases = (object,)
class_body = """
country='China'
def __init__(self, name, age):
    self.name = name
    self.age = age
def talk(self):
    print('%s is talking' % self.name)
"""

class_dic = {}
exec(class_body, globals(), class_dic)
print(class_dic)  # 类名称空间

# 第二步：用type实例化出Chinese1，类名、类的继承，类体的名称空间
Chinese1 = type(class_name, class_bases, class_dic)
print(Chinese1)  # <class '__main__.Chinese1'>

"""
我们看到，type 接收三个参数：
第 1 个参数是字符串 ‘Chinese’，表示类名
第 2 个参数是元组 (object, )，表示所有的父类
第 3 个参数是字典，类体执行的结果
"""