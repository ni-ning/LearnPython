# -*- coding:utf-8 -*-
'''
将对象组合成树形结构以表示"部分-整体"的层次结构
组合模式使得用户对单个对象和组合对象的使用具有一致性，如例子中draw方法
'''

from abc import ABCMeta, abstractmethod


# 抽象组件
class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


# 叶子组件
class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(str(self))

    def __str__(self):
        return '点(%s, %s)' % (self.x, self.y)


# 叶子组件
class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return '线段[%s, %s]' % (self.p1, self.p2)

    def draw(self):
        print(str(self))


# 复合组件
class Picture(Graphic):
    def __init__(self, iterable):
        self.children = []
        for g in iterable:
            self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print('----  复合图形  ----')
        for g in self.children:
            g.draw()
        print('----  复合图形  ----')


# 客户端
# p1 = Point(1, 1)
# p2 = Point(2, 2)
# l1 = Line(p1, p2)
# l1.draw()

p1 = Point(2, 3)
l1 = Line(Point(3, 4), Point(6, 7))
l2 = Line(Point(1, 5), Point(2, 8))
pic1 = Picture([p1, l1, l2])

p2 = Point(4, 4)
l3 = Line(Point(1, 1), Point(2, 2))
pic2 = Picture([p2, l3])

pic = Picture([pic1, pic2])     # 先总体，再细节，即先理解就是两个复合图形组成的更复杂的复合图形
pic.draw()

'''
适用场景：
 - 表示对象的"部分-整体"层次结构(特别结构是递归的)
 - 希望用户忽略组合对象与单个对象的不同，用户统一地使用组合结构中的所有对象
 
优点：
 - 定义了包含基本对象和组合对象的类层次结构
 - 简化客户端代码，即客户端可以一致地使用组合对象和单个对象
 - 更容易增加新类型组合，如 圆 叶子组件
'''


