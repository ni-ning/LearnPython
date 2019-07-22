# -*- coding:utf-8 -*-
'''
将一个事物的两个维度分离，使其都可以独立地变化，如画图程序形状和颜色
'''
from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    # 组合方式进行耦合 - 松耦合
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self, shape):
        pass


class Rectangle(Shape):
    name = '长方形'

    def draw(self):
        self.color.paint(self)


class Circle(Shape):
    name = '圆形'

    def draw(self):
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print('红色的%s' % shape.name)


class Green(Color):
    def paint(self, shape):
        print('绿色的%s' % shape.name)


shape = Rectangle(Red())
shape.draw()

shape2 = Circle(Green())
shape2.draw()

'''
应用场景：
当事物有两个维度上的表现，两个维度都可能扩展

优点：
 - 抽象与实现分离
 - 优秀的扩展能力
'''