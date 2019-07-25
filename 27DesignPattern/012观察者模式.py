# -*- coding:utf-8 -*-
'''
定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，
所有依赖于它的对象都得到通知并被自动更新。观察者模式又称"发布-订阅"模式
'''

from abc import ABCMeta, abstractmethod


# 抽象观察者
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice):   # notice 是 Notice类的对象
        pass


# 抽象主题
class Notice(object):
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)


# 具体主题，即发布者
class StaffNotice(Notice):
    def __init__(self, company_info):
        super(StaffNotice, self).__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()   # 推送


# 具体观察者，即订阅者
class Staff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


# Client
notice = StaffNotice('初始公司信息')
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
print(s1.company_info)
print(s2.company_info)

notice.company_info = '公司今年业绩非常行好，给大家发奖金！！！'
print(s1.company_info)
print(s2.company_info)

notice.detach(s2)
notice.company_info = '明天公司放假！'
print(s1.company_info)
print(s2.company_info)

'''
适用场景：
 - 当一个抽象模型有两方面，其中一个方面依赖于另一方面，将这两者封装在独立对象中以使它们可以各自独立地改变和复用
 - 当一个对象的改变需要同时改变其他对象，而不知道具体有多少对象有待改变
 - 当一个对象必须通知其他对象，而它又不能假定其他对象是谁，换言之，你不希望这些对象是紧密耦合的
 
优点：
 - 目标和观察者之间的抽象耦合最小
 - 支持广播通信
'''