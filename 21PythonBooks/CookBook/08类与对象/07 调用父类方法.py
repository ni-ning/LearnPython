#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
在子类中调用父类的某个已经被覆盖的方法
"""


class A(object):
    def spam(self):
        print('A.spam')


class B(A):
    def spam(self):
        print('B.spam')
        super().spam()


b = B()
# b.spam()
# print(b.__dict__)  # {}
# print(B.__dict__)  # 'spam': <function B.spam at 0x00000183B0B80D90>
# print(A.__dict__)  # 'spam': <function A.spam at 0x00000183B0B80730>


# super()函数的一个常见用法是在 __init__()方法中确保父类被正确初始化
# 初始化是保证obj.__dict__有正确属性值有效手段，如果父类__init__没有执行，会导致obj.__dict__属性值缺少

class A(object):
    def __init__(self):
        self.x = 0


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1


# 讨论 在子类中直接指定基类的函数名实现调用，会出现什么问题

class Base(object):
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        Base.__init__(self)
        print('A.__init__')

# 总结 大部分代码这样做没什么问题，但是在更复杂涉及到多继承的代码中就有可能导致奇怪的问题产生


class B(Base):
    def __init__(self):
        Base.__init__(self)
        print('B.__init__')


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('C.__init__')


# c = C()  # 可能两次调用 Base.__init__(), 没什么坏处，但有时候却不是


# 换成super() 可完美解决

class Base(object):
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')


class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')


class C(A, B):
    def __init__(self):
        super().__init__()
        print('C.__init__')


# c = C()
# print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>)

"""
为了弄清楚原理，我们需要花点时间解释一下Python是如何实现继承的：
对于自定义的每一个类，Python会计算出一个方法解析顺序(MRO)列表，这个MRO列表就是一个简单的所有基类的线性顺序表
为了实现继承，Python会在MRO列表上从左到右开始查找基类，直到找到第一个匹配这个属性的类为止
"""

"""
MRO列表的构造是通过一个C3线性化算法，它实际上就是合并所有父类的MRO列表并遵循如下三条准则：
1. 子类会先于父类被检查
2. 多个父类会根据它们在列表中顺序被检查
3. 如果对下一个存在两个合法的选择，选择第一个父类
"""

# 当使用super()函数时，Python会在MRO列表中继续搜索下一个类。只要每个重定义的方法都使用super()并且只调用一次
# 那么控制流会遍历整个MRO列表，每个方法也只会被调用一次，这就是第二个方法只会调用一次Base.__init__()原因

"""
super()有个令人吃惊的地方，并不一定去查找某个类在MRO中下一个直接父类，甚至可以在一个没有直接父类的类中调用它
"""


class A(object):
    def spam(self):
        print('A.spam')
        super().spam()    # 类A中使用 super().spam() 实际上调用的是跟类A毫无关系的类B中的 spam() 方法


class B(object):
    def spam(self):
        print('B.spam')


class C(A, B):
    pass


c = C()
c.spam()
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

"""
遵循通用原则：
首选，确保在继承体系中所有相同名字的方法拥有可兼容的参数签名(比如相同的参数个数和参数名称)
其次，最好确保最顶层的类提供了这个方法的实现，这样的话在MRO上面的查找链肯定可以找到某个确定的方法
"""